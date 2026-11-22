from __future__ import annotations
import time
from collections import deque
from dataclasses import dataclass
from .models import (Decision,IntentModel,RankRecord,DecisionRecord,ContinuationRecord,InvalidReferenceRecord,
                     AIRequestContext,ValidationReceipt,FailureReceipt,LibraryRecoveryPlan)
from .policies import DEFAULT_POLICY,policy_from_options
from .utils import stable_hash,edge_key
from .errors import InterpretationError,RootAuthorityError,CollapseValidationError,ExternalModuleError

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
        root:str; ordered_nodes:list=None; continuation_handles:list=None; cycle_references:list=None; frontier:list=None
        def __post_init__(self):
            self.ordered_nodes=[] if self.ordered_nodes is None else self.ordered_nodes
            self.continuation_handles=[] if self.continuation_handles is None else self.continuation_handles
            self.cycle_references=[] if self.cycle_references is None else self.cycle_references
            self.frontier=[] if self.frontier is None else self.frontier
        def ordered_handles(self): return [n.handle for n in self.ordered_nodes]

class MK43AI1C:
    version='1.C.1'; contract_version='2.0'; internal_dimension=5
    canonical_state_policy='READ_ONLY'; rewrite_policy='DERIVED_ONLY'
    domain_ids=('generic','mk43-ultra','gravity','canonical-mathematics')
    chirality_model='request-oriented-tree-policy-v2'; provenance_model='derived-validation-and-failure-receipt-v2'
    capabilities=('interpret','rank','continue_or_terminate','place_continuation','collapse','validate_collapse')
    def __init__(self,policy=DEFAULT_POLICY):
        policy.validate(); self._policy=policy; self._context=AIRequestContext(); self._last_receipt=None; self._last_decisions=[]; self._last_failure=None; self._last_metrics={}; self._authorized_root=None
    def dimension_model(self): return {'identity':True,'dependency':True,'chirality':True,'recursion':True,'provenance':True}
    def canonical_fingerprint(self): return stable_hash({'version':self.version,'policy':self._policy.fingerprint(),'domains':self.domain_ids,'contract':self.contract_version})
    def healthcheck(self):
        try: self._policy.validate(); return set(self.dimension_model())=={'identity','dependency','chirality','recursion','provenance'}
        except Exception:return False
    def fork_request_context(self): return MK43AI1C(self._policy)
    def close(self): self._context.close()
    def _options(self,request): return dict(getattr(request,'options',{}) or {})
    def _probe_api_roots(self,api,subject):
        if api is None: return (), 'REQUEST_UNVERIFIED'
        if not callable(getattr(api,'probe_subject',None)): raise RootAuthorityError('API lacks probe_subject')
        try: probed=api.probe_subject(subject)
        except Exception as exc: raise RootAuthorityError(f'API root probe failed: {exc}') from exc
        if isinstance(probed,str): candidates=(probed,)
        elif isinstance(probed,(list,tuple)): candidates=tuple(str(x) for x in probed if str(x).strip())
        else: candidates=()
        if not candidates: raise RootAuthorityError('API returned no canonical root candidates')
        resolver=getattr(api,'resolve',None)
        if callable(resolver):
            verified=[]
            for c in candidates:
                try:
                    result=resolver(c)
                    if result is not None: verified.append(c)
                except Exception: continue
            candidates=tuple(verified)
            if not candidates: raise RootAuthorityError('API candidates failed canonical resolution')
        return candidates,'API5'
    def interpret_structured(self,request,api=None):
        if getattr(request,'operation',None)!='generate_report': raise InterpretationError('unsupported operation')
        subject=str(getattr(request,'subject','')).strip()
        if not subject: raise InterpretationError('subject required')
        options=self._options(request)
        candidates,authority=self._probe_api_roots(api,subject) if api is not None else ((subject,),'REQUEST_UNVERIFIED')
        budgets={}  # Tree completion has no numeric hard-cap policy.
        return IntentModel(getattr(request,'request_id',None),'generate_report',subject,tuple(candidates),str(getattr(request,'depth','complete')),
            str(options.get('audience','general')),str(getattr(request,'artifact_format','markdown')),str(options.get('completeness_mode',getattr(request,'depth','complete'))),
            budgets,options,tuple(candidates[1:]),(f'request:{getattr(request,"request_id",None) or "anonymous"}',f'subject:{subject}',f'root_authority:{authority}'),authority)
    def interpret(self,request,api=None):
        structured=self.interpret_structured(request,api=api); self._authorized_root=structured.root_candidates[0] if structured.root_authority=='API5' else None
        options=self._options(request); policy=policy_from_options(options)
        title=getattr(request,'title',None) or f"{structured.subject.lstrip('@').replace('_',' ').title()} Recovery Report"
        tp={**policy.__dict__,'termination_handles':tuple(options.get('termination_handles',())),'defer_handles':tuple(options.get('defer_handles',())),'invalid_handles':tuple(options.get('invalid_handles',())),'root_authority':structured.root_authority}
        return RecoveryIntent('generate_report',structured.subject,structured.root_candidates[0],getattr(request,'language','en'),getattr(request,'artifact_format','markdown'),getattr(request,'depth','complete'),getattr(request,'direction','both'),getattr(request,'coverage_mode','annotated'),title,tp)
    def recover_graph(self,api,intent):
        try:
            graph=api.recover_closure(intent.root_hint,direction=getattr(intent.direction,'value',intent.direction),depth=intent.depth)
            if graph is None: raise ExternalModuleError('API returned no graph')
            self._last_failure=None; return graph
        except Exception as exc:
            self._last_failure=FailureReceipt('API','API_RECOVERY_FAILED',str(exc),False,True,(f'root:{intent.root_hint}',))
            raise ExternalModuleError(str(exc)) from exc
    def recover_library_partial(self,library,plan):
        packages=[]; failures=[]
        for h in plan.handles:
            try:
                packages.append(library.recover(h))
            except Exception as exc:
                failures.append(FailureReceipt('LIBRARY','LIBRARY_HANDLE_FAILED',str(exc),True,True,(f'handle:{h}',)))
        self._last_failure=failures[-1] if failures else None
        return {'packages':packages,'failures':tuple(failures),'partial':bool(failures),'complete':not failures}
    def _features(self,e,context):
        prov=1.0 if getattr(e,'provenance',None) else 0.0; confidence=str(getattr(e,'confidence','canonical')).lower(); conf=1.0 if confidence in {'canonical','verified','high'} else .5
        target=str(getattr(e,'target','')); subject=str(context.get('subject','')).lower(); alignment=1.0 if subject and subject.strip('@').replace('_',' ') in target.lower().replace('_',' ') else 0.0
        continuity=1.0 if getattr(e,'source',None)==context.get('node_handle') else .5; cycle=1.0 if target in set(context.get('path',())) else 0.0
        redundancy=float(context.get('target_counts',{}).get(target,0)>0); centrality=float(context.get('centrality',{}).get(target,0.0))
        recursive_reentry=float(bool(context.get('recursive_reentry',False)))
        saturation=float(context.get('domain_saturation',0.0))
        return {'relevance':alignment+conf,'centrality':centrality,'alignment':alignment,'continuity':continuity,'provenance':prov,'admissibility':1.0,'redundancy':redundancy,'cycle':cycle,'recursive_reentry':recursive_reentry,'domain_saturation':saturation}
    def _score(self,f,p): return p.relevance_weight*f['relevance']+p.centrality_weight*f['centrality']+p.alignment_weight*f['alignment']+p.continuity_weight*f['continuity']+p.provenance_weight*f['provenance']+p.admissibility_weight*f['admissibility']-p.redundancy_penalty*f['redundancy']-p.cycle_penalty*f['cycle']-p.recursive_reentry_weight*f['recursive_reentry']-p.domain_saturation_weight*f['domain_saturation']
    def rank_records(self,candidates,context):
        rows=[]
        for c in list(candidates):
            f=self._features(c,context); s=self._score(f,self._policy); rows.append((c,s,tuple(k.upper() for k,v in f.items() if v>0),f))
        rows.sort(key=lambda x:(-x[1],)+edge_key(x[0])); return [RankRecord(c,s,i+1,r,f,self._policy.policy_id) for i,(c,s,r,f) in enumerate(rows)]
    def rank(self,candidates,context): return [r.candidate for r in self.rank_records(candidates,context)]
    def continue_or_terminate(self,node,edge,intent,context):
        """Return a semantic Tree decision; never terminate on a counter."""
        handle=str(getattr(edge,'target','')); p=intent.traversal_policy
        if not handle or not getattr(edge,'relation',None): return Decision.REJECT_INVALID.value
        if handle in set(p.get('invalid_handles',())): return Decision.REJECT_INVALID.value
        if handle in set(p.get('defer_handles',())): return Decision.DEFER.value
        if handle in set(p.get('termination_handles',())): return Decision.TERMINATE.value

        path=tuple(context.get('path',()) or ())
        represented=set(context.get('represented_handles',()) or ())
        scheduled=set(context.get('scheduled_handles',()) or ())

        # Recursive domain re-entry is a canonical leaf: preserve the handle,
        # register continuation, and do not reopen the represented domain.
        if handle in path or bool(context.get('recursive_reentry',False)):
            return Decision.TERMINATE.value
        if handle in represented or handle in scheduled or bool(context.get('already_represented',False)):
            return Decision.TERMINATE.value

        # When a proposed target's local neighborhood substantially re-enters the
        # current branch/QMO, the target is the semantic boundary.  BRANE computes
        # this from API-provided routes; no fixed node/edge/depth count is involved.
        if bool(context.get('domain_reentry',False)):
            return Decision.TERMINATE.value

        return Decision.CONTINUE.value
    def place_continuation(self,node,edge,realization):
        h=str(edge.target)
        if h not in realization.continuation_handles: realization.continuation_handles.append(h)
        rec=ContinuationRecord(h,str(node.handle),'TERMINATION_BOUNDARY',int(node.depth)+1,tuple(getattr(node,'path',()))+(h,),self._policy.policy_id,stable_hash({'h':h,'p':node.handle,'d':node.depth+1}))
        self._context.continuations.append(rec); return rec
    def collapse(self,graph,intent):
        if getattr(intent,'root_hint',graph.root)!=graph.root: raise RootAuthorityError('intent root does not match API graph root')
        out=TraversalRealization(root=graph.root); out.rejected_invalid=[]; start=time.monotonic(); q=deque([(graph.root,0,None,None,(graph.root,),())]); order=0
        visited=set(); nodes_used=0; edges_used=0; decisions=[]; target_counts={}; max_depth=0
        centrality={}
        for e in getattr(graph,'edges',[]): centrality[e.target]=centrality.get(e.target,0)+1
        while q:
            h,d,parent,rel,path,relpath=q.popleft(); sig=h
            if sig in visited: continue
            visited.add(sig); max_depth=max(max_depth,d)
            node=TraversalNode(h,d,parent,rel,order,'root' if parent is None else 'branch',path,relpath); out.ordered_nodes.append(node); order+=1; nodes_used+=1
            candidates=list(graph.neighbors(h,intent.direction)); context={'root':graph.root,'subject':intent.subject,'node_handle':h,'path':path,'centrality':centrality,'target_counts':target_counts,'represented_handles':tuple(visited)}
            for rr in self.rank_records(candidates,context):
                e=rr.candidate; edges_used+=1; target=str(getattr(e,'target','')); target_counts[target]=target_counts.get(target,0)+1
                if target in path:
                    out.cycle_references.append((h,target)); decisions.append(self._decision_record(node,e,Decision.TERMINATE.value,rr,('CYCLE_REGISTERED',))); continue
                dctx={'path':path,'represented_handles':tuple(visited),'already_represented':target in visited}; decision=self.continue_or_terminate(node,e,intent,dctx); decisions.append(self._decision_record(node,e,decision,rr,(decision,)))
                if decision==Decision.CONTINUE.value: q.append((target,d+1,h,e.relation,path+(target,),relpath+(e.relation,)))
                elif decision==Decision.TERMINATE.value:
                    leaf=TraversalNode(target,d+1,h,e.relation,order,'leaf',path+(target,),relpath+(e.relation,)); out.ordered_nodes.append(leaf); order+=1; nodes_used+=1; max_depth=max(max_depth,d+1)
                    if intent.traversal_policy.get('continuation_enabled',True): self.place_continuation(node,e,out)
                elif decision==Decision.DEFER.value:
                    if target and target not in out.frontier: out.frontier.append(target)
                else:
                    rec=InvalidReferenceRecord(target,h,getattr(e,'relation',None),'INVALID_REFERENCE',tuple(x for x in (getattr(e,'provenance',None),) if x),self._context.next_sequence())
                    out.rejected_invalid.append(rec); self._context.rejected_invalid.append(rec)
        elapsed=(time.monotonic()-start)*1000
        self._last_metrics={'nodes_used':nodes_used,'edges_used':edges_used,'max_depth':max_depth,'elapsed_ms':elapsed,'completion_mode':'SEMANTIC_TREE_LEAF'}
        self._last_decisions=decisions; self._last_receipt=self._make_receipt(out,graph,intent); return out
    def _decision_record(self,node,e,decision,rr,reasons): return DecisionRecord(str(getattr(e,'target','')),getattr(node,'handle',None),decision,rr.score,rr.rank,tuple(reasons)+rr.reason_codes,self._policy.policy_id,tuple(x for x in (getattr(e,'provenance',None),) if x),self._context.next_sequence(),self._context.request_id)
    def _make_receipt(self,r,g,intent):
        handles=[n.handle for n in r.ordered_nodes]; known=set(getattr(g,'nodes',set())); nofab=not(set(handles)-known)
        encountered=[]
        for n in r.ordered_nodes: encountered.extend(str(getattr(e,'target','')) for e in g.neighbors(n.handle,intent.direction))
        rejected={x.candidate_handle for x in getattr(r,'rejected_invalid',[])}; accounted=set(handles)|set(r.frontier)|set(r.continuation_handles)|{b for _,b in r.cycle_references}|rejected
        branch_ok=set(encountered)<=accounted; orders=[n.order for n in r.ordered_nodes]; deterministic=orders==list(range(len(orders)))
        m=dict(self._last_metrics); budget_ok=True  # compatibility field: no numeric completion budget exists.
        continuation_ok=all(h in {n.handle for n in r.ordered_nodes} or h in set(encountered) for h in r.continuation_handles)
        invalid_sep=not(rejected.intersection(set(r.frontier)))
        root_authorized=(intent.traversal_policy.get('root_authority')=='API5' and self._authorized_root==g.root) or intent.traversal_policy.get('root_authority')=='REQUEST_UNVERIFIED'
        inp=stable_hash({'root':g.root,'nodes':sorted(known),'edges':[getattr(e,'__dict__',str(e)) for e in getattr(g,'edges',[])]})
        out=stable_hash({'root':r.root,'nodes':[getattr(n,'__dict__',str(n)) for n in r.ordered_nodes],'continuations':r.continuation_handles,'frontier':r.frontier,'cycles':r.cycle_references,'rejected':[x.__dict__ for x in getattr(r,'rejected_invalid',[])]})
        checks={'ROOT':r.root==g.root,'ROOT_AUTH':root_authorized,'BRANCH':branch_ok,'NOFAB':nofab,'ORDER':deterministic,'BUDGET':budget_ok,'CONT':continuation_ok,'INVALID':invalid_sep}; errors=tuple(k for k,v in checks.items() if not v)
        return ValidationReceipt(not errors,checks['ROOT'],checks['ROOT_AUTH'],checks['BRANCH'],checks['NOFAB'],checks['ORDER'],checks['BUDGET'],checks['CONT'],checks['INVALID'],inp,out,m,errors)
    def validate_collapse(self,realization,graph):
        if not realization.ordered_nodes or realization.root!=graph.root: raise CollapseValidationError('root or realization invalid')
        unknown={n.handle for n in realization.ordered_nodes}-set(graph.nodes)
        if unknown: raise CollapseValidationError('fabricated handles: '+','.join(sorted(unknown)))
        receipt=self._make_receipt(realization,graph,type('I',(),{'direction':'both','traversal_policy':{'root_authority':'REQUEST_UNVERIFIED'}})()) if self._last_receipt is None else self._last_receipt
        if not receipt.valid: raise CollapseValidationError('collapse receipt invalid: '+','.join(receipt.errors))
        return None
    def plan_library_recovery(self,realization):
        hs=[]
        for n in realization.ordered_nodes:
            if n.handle not in hs: hs.append(n.handle)
        return LibraryRecoveryPlan(tuple(hs),tuple((h,i) for i,h in enumerate(hs)),('definitions','equations','models','analogies','explanations','provenance'))
    def validation_receipt(self): return self._last_receipt
    def decision_provenance(self): return tuple(self._last_decisions)
    def failure_receipt(self): return self._last_failure

def create_module(): return MK43AI1C()
