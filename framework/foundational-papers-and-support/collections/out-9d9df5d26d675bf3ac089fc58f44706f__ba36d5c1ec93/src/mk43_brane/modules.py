from __future__ import annotations
from dataclasses import dataclass, field
from collections import deque
from typing import Iterable
import hashlib, json, copy
from .models import *
from .errors import HandleResolutionError, ApiRecoveryError

def _stable(obj)->str:
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()

def _dims(): return {'identity':True,'dependency':True,'chirality':True,'recursion':True,'provenance':True}

@dataclass
class DeterministicCollapseAI:
    version:str='2.1.0'; contract_version:str='2.0'; internal_dimension:int=5; canonical_state_policy:str='READ_ONLY'; rewrite_policy:str='DERIVED_ONLY'; domain_ids:tuple[str,...]=('generic',)
    def healthcheck(self): return True
    def dimension_model(self): return _dims()
    def fork_request_context(self): return copy.deepcopy(self)
    def canonical_fingerprint(self): return _stable({'version':self.version,'policy':'deterministic','domains':self.domain_ids})
    def interpret(self,request):
        title=request.title or f"{request.subject.lstrip('@').replace('_',' ').title()} Recovery Report"
        policy={'termination_handles':tuple(request.options.get('termination_handles',()))}
        return RecoveryIntent(request.operation,request.subject,request.subject,request.language,request.artifact_format,request.depth,request.direction,request.coverage_mode,title,policy)
    def rank(self,candidates,context): return sorted(candidates,key=lambda x:(x.relation,x.target,x.source,x.provenance or ''))
    def continue_or_terminate(self,node,edge,intent,context):
        if edge.target in intent.traversal_policy['termination_handles']: return 'TERMINATE'
        if edge.target in set(context.get('path',())) or context.get('already_represented'): return 'TERMINATE'
        return 'CONTINUE'
    def place_continuation(self,node,edge,realization): realization.continuation_handles.append(edge.target)
    def collapse(self,graph,intent):
        out=TraversalRealization(root=graph.root); q=deque([(graph.root,0,None,None,(graph.root,),())]); order=0; inspected=0; seen=set()
        while q:
            h,d,p,r,path,rels=q.popleft(); signature=(h,path,rels,d)
            if signature in seen: continue
            seen.add(signature); node=TraversalNode(h,d,p,r,order,'root' if p is None else 'branch',path,rels); out.ordered_nodes.append(node); order+=1
            context={'path':path,'relations':rels}
            for e in self.rank(graph.neighbors(h,intent.direction),context):
                if e.target in path: out.cycle_references.append((h,e.target)); continue
                decision=self.continue_or_terminate(node,e,intent,context)
                if decision=='TERMINATE':
                    leaf=TraversalNode(e.target,d+1,h,e.relation,order,'leaf',path+(e.target,),rels+(e.relation,)); out.ordered_nodes.append(leaf); order+=1; self.place_continuation(node,e,out)
                else: q.append((e.target,d+1,h,e.relation,path+(e.target,),rels+(e.relation,)))
        return out
    def validate_collapse(self,r,g):
        if not r.ordered_nodes or r.root!=g.root: raise ApiRecoveryError('invalid finite realization')
        unknown={n.handle for n in r.ordered_nodes}-g.nodes
        if unknown: raise ApiRecoveryError('AI fabricated handles')

@dataclass
class InMemoryAPI5:
    edges:list[EdgeRecord]; aliases:dict[str,str]=field(default_factory=dict); equations:dict[str,tuple[str,...]]=field(default_factory=dict); provenance:dict[str,tuple[str,...]]=field(default_factory=dict); chirality:dict[str,str]=field(default_factory=dict); inadmissible:set[str]=field(default_factory=set); version:str='fixture-2.1.0'; contract_version:str='2.0'; internal_dimension:int=5; domain_ids:tuple[str,...]=('fixture',); canonical_state_policy:str='READ_ONLY'; rewrite_policy:str='DERIVED_ONLY'
    def healthcheck(self): return True
    def dimension_model(self): return _dims()
    def fork_request_context(self): return copy.deepcopy(self)
    def canonical_fingerprint(self): return _stable({'edges':[e.__dict__ for e in self.edges],'aliases':self.aliases,'equations':self.equations,'provenance':self.provenance,'chirality':self.chirality,'inadmissible':sorted(self.inadmissible)})
    def resolve(self,s):
        n=s.strip(); handles={e.source for e in self.edges}|{e.target for e in self.edges}
        if n in self.aliases:return self.aliases[n]
        if n in handles:return n
        c='@'+n.lower().replace(' ','_')
        if c in handles:return c
        raise HandleResolutionError(n)
    def neighbors(self,h,direction):
        g=CanonicalGraph('',set(),list(self.edges)); return g.neighbors(h,direction)
    def recover_closure(self,root,intent):
        g=CanonicalGraph(root,{root},[]); q=[root]; seen=set()
        while q:
            h=q.pop(0)
            if h in seen: continue
            seen.add(h)
            for e in self.neighbors(h,intent.direction):
                original=e
                if e.relation.startswith('INVERSE:'):
                    rel=e.relation.removeprefix('INVERSE:')
                    original=next((x for x in self.edges if x.source==e.target and x.target==e.source and x.relation==rel),e)
                g.add_edge(original)
                if e.target not in seen:q.append(e.target)
        self.validate_graph(g); return g
    def probe_subject(self):
        if self.aliases: return next(iter(self.aliases))
        handles=sorted({e.source for e in self.edges}|{e.target for e in self.edges})
        if not handles: raise HandleResolutionError('empty API')
        return handles[0]
    def recover_equations(self,h): return self.equations.get(h,())
    def recover_provenance(self,h): return self.provenance.get(h,())
    def resolve_chirality(self,node,intent,provenance):
        if node.handle in self.chirality:return self.chirality[node.handle]
        if node.parent is None:return 'S0:ROOT'
        edge=next((e for e in self.edges if e.source==node.parent and e.target==node.handle and e.relation==node.incoming_relation),None)
        if edge and edge.chirality:return edge.chirality
        return 'CHI:'+hashlib.sha256(f'{node.parent}|{node.incoming_relation}|{node.handle}'.encode()).hexdigest()[:16]
    def admissible(self,node,intent,chirality,provenance): return node.handle not in self.inadmissible and bool(chirality) and bool(node.handle)
    def validate_graph(self,g):
        if g.root not in g.nodes: raise ApiRecoveryError('root missing')
        if any(not e.source or not e.target or not e.relation for e in g.edges): raise ApiRecoveryError('invalid edge')

@dataclass
class InMemoryLibrary5:
    packages:dict[str,KnowledgePackage]; version:str='fixture-2.1.0'; contract_version:str='2.0'; internal_dimension:int=5; domain_ids:tuple[str,...]=('fixture',); canonical_state_policy:str='READ_ONLY'; rewrite_policy:str='DERIVED_ONLY'
    def healthcheck(self): return True
    def dimension_model(self): return _dims()
    def fork_request_context(self): return copy.deepcopy(self)
    def canonical_fingerprint(self):
        return _stable({h:{'display_name':p.display_name,'chunks':[c.__dict__ for c in p.chunks],'unresolved':p.unresolved_reason,'version':p.version,'expected':p.expected_chunk_types} for h,p in self.packages.items()})
    def _typed(self,h,t):
        p=self.packages.get(h); return tuple(c for c in (p.chunks if p else ()) if c.chunk_type==t)
    def recover_equations(self,h,context,language): return self._typed(h,'equation')
    def recover_models(self,h,context,language): return self._typed(h,'model')
    def recover_analogies(self,h,context,language): return self._typed(h,'analogy')
    def recover_explanations(self,h,context,language): return tuple(c for c in self._typed(h,'definition')+self._typed(h,'explanation')+self._typed(h,'derivation')+self._typed(h,'implication'))
    def assemble_chunk(self,h,context,language):
        p=self.packages.get(h)
        if not p:return KnowledgePackage(h,h,unresolved_reason='NOT_FOUND',realization_key=context.key.encode())
        chunks=list(self.recover_explanations(h,context,language))+list(self.recover_equations(h,context,language))+list(self.recover_models(h,context,language))+list(self.recover_analogies(h,context,language))
        used={id(c) for c in chunks}; chunks.extend(c for c in p.chunks if id(c) not in used)
        expected=p.expected_chunk_types or tuple(sorted({c.chunk_type for c in p.chunks if c.chunk_type not in {'summary','heading','index'}}))
        return KnowledgePackage(h,p.display_name,chunks,p.unresolved_reason,p.version,context.key.encode(),expected)
    def recover(self,h,context,language): return self.assemble_chunk(h,context,language)
    def recover_batch(self,handles:Iterable[tuple[str,Realization6Coordinate]],language): return [self.assemble_chunk(h,c,language) for h,c in handles]
