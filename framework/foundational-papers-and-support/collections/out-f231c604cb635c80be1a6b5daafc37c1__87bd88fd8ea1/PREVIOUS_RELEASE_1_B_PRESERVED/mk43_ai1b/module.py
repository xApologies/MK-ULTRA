from __future__ import annotations
import copy,time,hashlib,json
from collections import deque
from dataclasses import dataclass
from .models import Decision,IntentModel,RankRecord,DecisionRecord,ContinuationRecord,AIRequestContext,ValidationReceipt,LibraryRecoveryPlan
from .policies import DEFAULT_POLICY,policy_from_options
from .utils import stable_hash,edge_key,direction_value,coverage_value
from .errors import InterpretationError,CollapseValidationError

try:
    from mk43_brane.models import RecoveryIntent,TraversalRealization,TraversalNode
except Exception:
    @dataclass(frozen=True)
    class RecoveryIntent:
        operation:str; subject:str; root_hint:str; language:str; artifact_format:str; depth:str; direction:object; coverage_mode:object; title:str; traversal_policy:dict
    @dataclass(frozen=True)
    class TraversalNode:
        handle:str; depth:int; parent:str|None; incoming_relation:str|None; order:int; kind:str='branch'; path:tuple[str,...]=(); relation_path:tuple[str,...]=()
    @dataclass
    class TraversalRealization:
        root:str
        ordered_nodes:list=None; continuation_handles:list=None; cycle_references:list=None; frontier:list=None
        def __post_init__(self):
            self.ordered_nodes=[] if self.ordered_nodes is None else self.ordered_nodes
            self.continuation_handles=[] if self.continuation_handles is None else self.continuation_handles
            self.cycle_references=[] if self.cycle_references is None else self.cycle_references
            self.frontier=[] if self.frontier is None else self.frontier
        def ordered_handles(self): return [n.handle for n in self.ordered_nodes]

class MK43AI1B:
    version='1.B.0'; contract_version='2.0'; internal_dimension=5
    canonical_state_policy='READ_ONLY'; rewrite_policy='DERIVED_ONLY'
    domain_ids=('generic','mk43-ultra','gravity','canonical-mathematics')
    chirality_model='request-oriented-tree-policy-v1'; provenance_model='decision-receipt-and-input-fingerprint-v1'
    capabilities=('interpret','rank','continue_or_terminate','place_continuation','collapse','validate_collapse')
    def __init__(self,policy=DEFAULT_POLICY):
        policy.validate(); self._policy=policy; self._context=AIRequestContext(); self._last_receipt=None; self._last_decisions=[]
    def dimension_model(self): return {'identity':True,'dependency':True,'chirality':True,'recursion':True,'provenance':True}
    def canonical_fingerprint(self):
        return stable_hash({'version':self.version,'policy':self._policy.fingerprint(),'domains':self.domain_ids,'contract':self.contract_version})
    def healthcheck(self):
        try: self._policy.validate(); return set(self.dimension_model())=={'identity','dependency','chirality','recursion','provenance'}
        except Exception:return False
    def fork_request_context(self): return MK43AI1B(self._policy)
    def close(self): self._context.close()
    def _options(self,request): return dict(getattr(request,'options',{}) or {})
    def interpret_structured(self,request,api=None):
        if getattr(request,'operation',None)!='generate_report': raise InterpretationError('unsupported operation')
        subject=str(getattr(request,'subject','')).strip()
        if not subject: raise InterpretationError('subject required')
        options=self._options(request); candidates=[]
        if api is not None and callable(getattr(api,'probe_subject',None)):
            try:
                probed=api.probe_subject(subject)
            except TypeError:
                probed=api.probe_subject()
            except Exception:
                probed=[]
            if isinstance(probed,str): candidates=[probed]
            elif isinstance(probed,(list,tuple)): candidates=[str(x) for x in probed]
        if not candidates: candidates=[subject]
        budgets={k:options.get(k,getattr(self._policy,k)) for k in ('edge_budget','node_budget','depth_budget','time_budget_ms')}
        ambiguities=tuple(candidates[1:])
        return IntentModel(getattr(request,'request_id',None),'generate_report',subject,tuple(candidates),str(getattr(request,'depth','complete')),
            str(options.get('audience','general')),str(getattr(request,'artifact_format','markdown')),str(options.get('completeness_mode',getattr(request,'depth','complete'))),
            budgets,options,ambiguities,(f'request:{getattr(request,"request_id",None) or "anonymous"}',f'subject:{subject}'))
    def interpret(self,request):
        structured=self.interpret_structured(request)
        options=self._options(request); policy=policy_from_options(options)
        title=getattr(request,'title',None) or f"{structured.subject.lstrip('@').replace('_',' ').title()} Recovery Report"
        tp={**policy.__dict__,'termination_handles':tuple(options.get('termination_handles',())),'defer_handles':tuple(options.get('defer_handles',())),'invalid_handles':tuple(options.get('invalid_handles',()))}
        return RecoveryIntent('generate_report',structured.subject,structured.root_candidates[0],getattr(request,'language','en'),getattr(request,'artifact_format','markdown'),getattr(request,'depth','complete'),getattr(request,'direction','both'),getattr(request,'coverage_mode','annotated'),title,tp)
    def _features(self,e,context):
        prov=1.0 if getattr(e,'provenance',None) else 0.0
        confidence=str(getattr(e,'confidence','canonical')).lower(); conf=1.0 if confidence in {'canonical','verified','high'} else .5
        target=str(getattr(e,'target','')); root=str(context.get('root','')); subject=str(context.get('subject','')).lower()
        alignment=1.0 if subject and subject.strip('@').replace('_',' ') in target.lower().replace('_',' ') else 0.0
        continuity=1.0 if getattr(e,'source',None)==context.get('node_handle') else .5
        cycle=1.0 if target in set(context.get('path',())) else 0.0
        redundancy=float(context.get('target_counts',{}).get(target,0)>0)
        cost=1.0/max(1,int(context.get('remaining_edges',1)))
        centrality=float(context.get('centrality',{}).get(target,0.0))
        return {'relevance':alignment+conf,'centrality':centrality,'alignment':alignment,'continuity':continuity,'provenance':prov,'admissibility':1.0,'redundancy':redundancy,'cycle':cycle,'budget_cost':cost}
    def _score(self,f,p):
        return p.relevance_weight*f['relevance']+p.centrality_weight*f['centrality']+p.alignment_weight*f['alignment']+p.continuity_weight*f['continuity']+p.provenance_weight*f['provenance']+p.admissibility_weight*f['admissibility']-p.redundancy_penalty*f['redundancy']-p.cycle_penalty*f['cycle']-p.budget_penalty*f['budget_cost']
    def rank_records(self,candidates,context):
        p=self._policy; rows=[]
        for c in list(candidates):
            f=self._features(c,context); s=self._score(f,p); reasons=tuple(k.upper() for k,v in f.items() if v>0)
            rows.append((c,s,reasons,f))
        rows.sort(key=lambda x:(-x[1],)+edge_key(x[0]))
        return [RankRecord(c,s,i+1,r,f,p.policy_id) for i,(c,s,r,f) in enumerate(rows)]
    def rank(self,candidates,context): return [r.candidate for r in self.rank_records(candidates,context)]
    def continue_or_terminate(self,node,edge,intent,context):
        handle=str(getattr(edge,'target','')); p=intent.traversal_policy
        if not handle or not getattr(edge,'relation',None): return Decision.REJECT_INVALID.value
        if handle in set(p.get('invalid_handles',())): return Decision.REJECT_INVALID.value
        if handle in set(p.get('defer_handles',())): return Decision.DEFER.value
        if context.get('elapsed_ms',0)>=int(p.get('time_budget_ms',30000)): return Decision.DEFER.value
        if context.get('nodes_used',0)>=int(p.get('node_budget',10000)): return Decision.DEFER.value
        if context.get('edges_used',0)>=int(p.get('edge_budget',100000)): return Decision.DEFER.value
        if handle in set(p.get('termination_handles',())): return Decision.TERMINATE.value
        if int(getattr(node,'depth',0))+1>=int(p.get('depth_budget',256)): return Decision.TERMINATE.value
        return Decision.CONTINUE.value
    def place_continuation(self,node,edge,realization):
        h=str(edge.target)
        if h not in realization.continuation_handles: realization.continuation_handles.append(h)
        rec=ContinuationRecord(h,str(node.handle),'TERMINATION_BOUNDARY',int(node.depth)+1,tuple(getattr(node,'path',()))+(h,),self._policy.policy_id,stable_hash({'h':h,'p':node.handle,'d':node.depth+1}))
        self._context.continuations.append(rec); return rec
    def collapse(self,graph,intent):
        root=graph.root; out=TraversalRealization(root=root); start=time.monotonic(); q=deque([(root,0,None,None,(root,),())]); order=0
        visited_paths=set(); nodes_used=0; edges_used=0; decisions=[]; target_counts={}
        while q:
            h,d,parent,rel,path,relpath=q.popleft(); sig=(h,path,relpath)
            if sig in visited_paths: continue
            visited_paths.add(sig)
            node=TraversalNode(h,d,parent,rel,order,'root' if parent is None else 'branch',path,relpath); out.ordered_nodes.append(node); order+=1; nodes_used+=1
            candidates=list(graph.neighbors(h,intent.direction))
            centrality={}
            for e in getattr(graph,'edges',[]): centrality[e.target]=centrality.get(e.target,0)+1
            context={'root':root,'subject':intent.subject,'node_handle':h,'path':path,'remaining_edges':max(1,int(intent.traversal_policy.get('edge_budget',100000))-edges_used),'centrality':centrality,'target_counts':target_counts}
            ranked=self.rank_records(candidates,context)
            for rr in ranked:
                e=rr.candidate; edges_used+=1; target=str(e.target); target_counts[target]=target_counts.get(target,0)+1
                if target in path:
                    out.cycle_references.append((h,target)); decisions.append(self._decision_record(node,e,Decision.TERMINATE.value,rr,('CYCLE_REGISTERED',))); continue
                dctx={'elapsed_ms':(time.monotonic()-start)*1000,'nodes_used':nodes_used,'edges_used':edges_used}
                decision=self.continue_or_terminate(node,e,intent,dctx); reasons=(decision,)
                decisions.append(self._decision_record(node,e,decision,rr,reasons))
                if decision==Decision.CONTINUE.value:
                    q.append((target,d+1,h,e.relation,path+(target,),relpath+(e.relation,)))
                elif decision==Decision.TERMINATE.value:
                    leaf=TraversalNode(target,d+1,h,e.relation,order,'leaf',path+(target,),relpath+(e.relation,)); out.ordered_nodes.append(leaf); order+=1; nodes_used+=1
                    if intent.traversal_policy.get('continuation_enabled',True): self.place_continuation(node,e,out)
                elif decision==Decision.DEFER.value:
                    if target not in out.frontier: out.frontier.append(target)
                else:
                    if target not in out.frontier: out.frontier.append(target)
        self._last_decisions=decisions
        self._last_receipt=self._make_receipt(out,graph,intent)
        return out
    def _decision_record(self,node,e,decision,rr,reasons):
        return DecisionRecord(str(e.target),getattr(node,'handle',None),decision,rr.score,rr.rank,tuple(reasons)+rr.reason_codes,self._policy.policy_id,tuple(x for x in (getattr(e,'provenance',None),) if x),self._context.next_sequence(),self._context.request_id)
    def _make_receipt(self,r,g,intent):
        handles=[n.handle for n in r.ordered_nodes]; known=set(getattr(g,'nodes',set())); nofab=not(set(handles)-known)
        encountered=[]
        for n in r.ordered_nodes:
            encountered.extend(str(e.target) for e in g.neighbors(n.handle,intent.direction))
        accounted=set(handles)|set(r.frontier)|set(r.continuation_handles)|{b for _,b in r.cycle_references}
        branch_ok=set(encountered)<=accounted
        inp=stable_hash({'root':g.root,'nodes':sorted(known),'edges':[getattr(e,'__dict__',str(e)) for e in getattr(g,'edges',[])]})
        out=stable_hash({'root':r.root,'nodes':[getattr(n,'__dict__',str(n)) for n in r.ordered_nodes],'continuations':r.continuation_handles,'frontier':r.frontier,'cycles':r.cycle_references})
        valid=r.root==g.root and bool(r.ordered_nodes) and nofab and branch_ok
        return ValidationReceipt(valid,r.root==g.root,branch_ok,nofab,True,True,True,inp,out,() if valid else ('VALIDATION_FAILED',))
    def validate_collapse(self,realization,graph):
        if not realization.ordered_nodes or realization.root!=graph.root: raise CollapseValidationError('root or realization invalid')
        unknown={n.handle for n in realization.ordered_nodes}-set(graph.nodes)
        if unknown: raise CollapseValidationError('fabricated handles: '+','.join(sorted(unknown)))
        orders=[n.order for n in realization.ordered_nodes]
        if orders!=list(range(len(orders))): raise CollapseValidationError('non-deterministic order sequence')
        if self._last_receipt and not self._last_receipt.valid: raise CollapseValidationError('collapse receipt invalid')
        return None
    def plan_library_recovery(self,realization):
        hs=[]
        for n in realization.ordered_nodes:
            if n.handle not in hs: hs.append(n.handle)
        return LibraryRecoveryPlan(tuple(hs),tuple((h,i) for i,h in enumerate(hs)),('definitions','equations','models','analogies','explanations','provenance'))
    def validation_receipt(self): return self._last_receipt
    def decision_provenance(self): return tuple(self._last_decisions)

def create_module(): return MK43AI1B()
