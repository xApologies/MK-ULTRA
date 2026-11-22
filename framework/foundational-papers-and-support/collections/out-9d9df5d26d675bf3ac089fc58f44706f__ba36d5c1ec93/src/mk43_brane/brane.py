from __future__ import annotations
from pathlib import Path
from uuid import uuid4
from threading import RLock
from collections import deque
import time
from dataclasses import replace
from inspect import signature, Parameter
from .models import *
from .loader import BraneLoader, PortLoader
from .ports import PortKind, BraneModules, LoadedModule
from .qmo import Qmo6
from .chirality import ChiralityLift
from .reporting import StreamingMarkdownRenderer
from .validation import Validator
from .errors import RequestValidationError, ModuleReplacementError

_PUBLIC_ERROR_MESSAGES={'RequestValidationError':'invalid request','ValueError':'invalid request','TypeError':'invalid request','HandleResolutionError':'subject could not be resolved','CoverageError':'recovery coverage failed','PrivilegeViolation':'canonical immutability or admissibility violation','ArtifactValidationError':'artifact validation failed','ModuleCompatibilityError':'module compatibility failure','ReportGenerationError':'report generation failed','ModuleReplacementError':'module replacement failed'}



class _RootAuthorityView:
    """BRANE-local compatibility view for AI/API root-probe signature variance.

    AI may request probe_subject(subject); API 1.B exposes probe_subject() plus
    resolve(subject). BRANE preserves both modules unchanged and mediates the call.
    """
    def __init__(self,api): self._api=api
    def __getattr__(self,name): return getattr(self._api,name)
    def probe_subject(self,subject=None):
        if subject is not None:
            return self._api.resolve(str(subject))
        return self._api.probe_subject()

class _AdmissibilityView:
    """BRANE-local compatibility view for API alias-equivalent edge validation."""
    def __init__(self,api): self._api=api
    def __getattr__(self,name): return getattr(self._api,name)
    def admissible(self,node,intent,chirality,provenance):
        if self._api.admissible(node,intent,chirality,provenance): return True
        if not chirality or not provenance or not getattr(node,'handle',None): return False
        if getattr(node,'parent',None) is None: return True
        try:
            child=self._api.resolve(node.handle); parent=self._api.resolve(node.parent)
            # Fallback is only for an alias-equivalence defect in the API's own
            # neighbor/admissibility comparison. Canonical explicit rejection remains
            # closed because an exact endpoint match does not trigger this fallback.
            for edge in self._api.neighbors(parent,TraversalDirection.BOTH):
                try: target=self._api.resolve(edge.target)
                except Exception: continue
                relation=str(edge.relation); incoming=str(node.incoming_relation)
                alias_equivalent=(str(edge.target)!=target or str(node.handle)!=child or str(node.parent)!=parent)
                if alias_equivalent and target==child and (relation==incoming or relation=='INVERSE:'+incoming or incoming=='INVERSE:'+relation): return True
        except Exception: return False
        return False

class Brane:
    __slots__=('__core',)
    def __init__(self,modules,output_dir,renderer=None,validator=None,lift=None): self.__core=_Core(modules,output_dir,renderer,validator,lift)
    def handle(self,envelope): return self.__core.handle(envelope)
    def replace_module(self,role,candidate): return self.__core.replace_module(role,candidate)
    def close(self): self.__core.close()
    def __dir__(self): return ['close','handle','replace_module']

class _Core:
    def __init__(self,modules,output_dir,renderer=None,validator=None,lift=None):
        self.modules=BraneLoader.assemble(modules.ai,modules.api,modules.library); self.output=Path(output_dir); self.renderer=renderer or StreamingMarkdownRenderer(); self.validator=validator or Validator(); self.lift=lift or ChiralityLift(); self.lock=RLock(); self.active=0; self.rollback=None; self.probation=0
    def _fork_modules(self,modules):
        def fork(lm):
            inst=lm.instance.fork_request_context()
            clone=LoadedModule(lm.manifest,inst)
            PortLoader.validate(clone,lm.manifest.role)
            return clone
        return BraneLoader.assemble(fork(modules.ai),fork(modules.api),fork(modules.library))
    def _execute(self,envelope,modules,output_dir,renderer=None,probe=False):
        execution_id=uuid4().hex; public_id=(envelope.get('request_id') if isinstance(envelope,dict) else getattr(envelope,'request_id',None)) or execution_id
        q=None; request_modules=None; output=Path(output_dir); before_files=set(output.glob(f'*{execution_id}*')) if output.exists() else set()
        try:
            req=envelope if isinstance(envelope,RuntimeRequest) else RuntimeRequest.from_dict(envelope)
            public_id=req.request_id or execution_id
            mounted_fingerprints=self.validator.fingerprints(modules)
            request_modules=self._fork_modules(modules)
            interpreter=request_modules.ai.instance.interpret
            params=signature(interpreter).parameters.values()
            accepts_api=any(p.name=='api' or p.kind is Parameter.VAR_KEYWORD for p in params)
            intent=interpreter(req,api=_RootAuthorityView(request_modules.api.instance)) if accepts_api else interpreter(req)
            q=Qmo6(execution_id,intent); q.transition(QmoState.REQUEST_COMPILED); q.transition(QmoState.API_RESOLVING)
            root=request_modules.api.instance.resolve(intent.root_hint)
            if intent.root_hint!=root: intent=replace(intent,root_hint=root); q.intent=intent
            graph,realization=self._crawl_qmo(root,intent,request_modules.api.instance,request_modules.ai.instance)
            request_modules.api.instance.validate_graph(graph); self._validate_bounded_realization(realization,graph); q.graph=graph; q.realization=realization; q.transition(QmoState.STRUCTURE_COMPLETE); q.transition(QmoState.LIFTING)
            lift_api=_AdmissibilityView(request_modules.api.instance)
            for node in realization.ordered_nodes:
                q.add_lifted(LiftedNode(node,self.lift.lift(node,request_id=execution_id,root=root,intent=intent,api=lift_api)))
            q.transition(QmoState.LIBRARY_RECOVERING); pairs=[(x.node.handle,x.coordinate) for x in q.lifted.values()]
            packages=list(request_modules.library.instance.recover_batch(pairs,intent.language))
            for (handle,coordinate),package in zip(pairs,packages):
                # BRANE owns realization placement. Libraries may return unresolved
                # containers without echoing the call-local realization key.
                if not package.realization_key:
                    package.realization_key=coordinate.key.encode()
                q.attach(package.realization_key,package)
            q.transition(QmoState.COVERAGE_VALIDATING); cov=self.validator.coverage(q); self.validator.enforce(cov,intent.coverage_mode); self.validator.substantive(q)
            self.validator.immutable(mounted_fingerprints,modules); q.transition(QmoState.REPORT_ASSEMBLING)
            path=(renderer or self.renderer).build(q,output); q.transition(QmoState.ARTIFACT_VALIDATING); receipt=self.validator.artifact(path,q,intent.artifact_format); self.validator.immutable(mounted_fingerprints,modules); q.transition(QmoState.COMPLETE)
            recovery={'root_handle':root,'expected_realizations':cov.expected_count,'recovered_realizations':cov.recovered_count,'unresolved_realizations':len(cov.unresolved),'incomplete_families':len(cov.incomplete_families),'qmo_exposed':False,'internal_execution_id':execution_id}
            if probe: recovery['staging_probe']=True
            return RuntimeResponse(public_id,'complete',receipt,recovery)
        except Exception as exc:
            if q and q.state not in (QmoState.COMPLETE,QmoState.DESTROYED): q.state=QmoState.FAILED
            if output.exists():
                for p in output.glob(f'*{execution_id}*'):
                    if p not in before_files:p.unlink(missing_ok=True)
            code=type(exc).__name__; return RuntimeResponse(public_id,'failed',errors=({'code':code,'message':_PUBLIC_ERROR_MESSAGES.get(code,'request failed')},))
        finally:
            if q and q.state is not QmoState.DESTROYED:q.destroy()
            for lm in ((request_modules.ai,request_modules.api,request_modules.library) if request_modules else ()):
                fn=getattr(lm.instance,'close',None)
                if callable(fn):
                    try:fn()
                    except Exception:pass

    @staticmethod
    def _canonical_edge(edge):
        """Return API-canonical orientation while preserving traversal orientation elsewhere."""
        if str(edge.relation).startswith('INVERSE:'):
            return EdgeRecord(edge.target,str(edge.relation).split(':',1)[1],edge.source,edge.provenance,edge.confidence,edge.chirality)
        return edge

    def _crawl_qmo(self,root,intent,api,ai):
        """Construct @Tree by conducting the API crawl under live AI leaf authority.

        No node, edge, depth, branch, realization, or time counter is a normal
        completion condition.  The finite Tree is produced by recursive re-entry,
        represented-domain closure, and explicit Collapse Intelligence decisions.
        """
        graph=CanonicalGraph(root,{root},[])
        realization=TraversalRealization(root=root)
        queue=deque([(root,0,None,None,(root,),())])
        expanded=set(); scheduled={root}; edge_keys=set(); order=0
        continuation_enabled=bool(getattr(intent,'traversal_policy',{}).get('continuation_enabled',True))
        target_counts={}; leaf_clusters=set()

        def add_frontier(handle):
            if handle and handle not in realization.frontier: realization.frontier.append(handle)

        def add_continuation(node,edge):
            if continuation_enabled:
                ai.place_continuation(node,edge,realization)

        def emit_leaf(node,edge,target,path,relpath,reason):
            nonlocal order
            # @Tree leaf clustering: one call-local leaf per canonical continuation
            # target and reason, rather than one duplicate realization per API path.
            cluster=(target,reason)
            if cluster not in leaf_clusters:
                leaf=TraversalNode(target,node.depth+1,node.handle,edge.relation,order,'leaf',path+(target,),relpath+(edge.relation,))
                realization.ordered_nodes.append(leaf); order+=1; leaf_clusters.add(cluster)
            add_continuation(node,edge)

        while queue:
            h,d,parent,rel,path,relpath=queue.popleft(); scheduled.discard(h)
            kind='root' if parent is None else 'branch'
            node=TraversalNode(h,d,parent,rel,order,kind,path,relpath)
            realization.ordered_nodes.append(node); order+=1

            if h in expanded:
                continue
            expanded.add(h)

            candidates=list(api.neighbors(h,intent.direction))
            context={'root':root,'subject':intent.subject,'node_handle':h,'path':path,
                     'relations':relpath,'target_counts':target_counts,
                     'represented_handles':tuple(expanded),'scheduled_handles':tuple(scheduled),
                     'qmo_nodes':len(graph.nodes),'qmo_edges':len(graph.edges)}
            ranked=list(ai.rank(candidates,context))

            for route_edge in ranked:
                source=api.resolve(str(route_edge.source)); target=api.resolve(str(route_edge.target))
                edge=EdgeRecord(source,route_edge.relation,target,route_edge.provenance,route_edge.confidence,route_edge.chirality)
                target_counts[target]=target_counts.get(target,0)+1
                canonical=self._canonical_edge(route_edge)
                key=(canonical.source,canonical.relation,canonical.target,canonical.provenance)
                if key not in edge_keys:
                    graph.add_edge(canonical); graph.nodes.update((source,target)); edge_keys.add(key)

                if target in path:
                    realization.cycle_references.append((h,target))
                    emit_leaf(node,edge,target,path,relpath,'RECURSIVE_PATH_REENTRY')
                    continue

                if target in expanded or target in scheduled:
                    emit_leaf(node,edge,target,path,relpath,'REPRESENTED_DOMAIN')
                    continue

                # Ask the API what the target would reopen, then give that topology
                # to Collapse Intelligence.  Re-entry is relative to this Tree, not a
                # fixed global count.
                target_neighbors=list(api.neighbors(target,intent.direction))
                neighbor_targets={api.resolve(str(e.target)) for e in target_neighbors}
                represented=set(expanded)|set(scheduled)|set(path)
                overlap=neighbor_targets & represented
                domain_reentry=bool(overlap and root in overlap) or bool(len(overlap)>1 and h in overlap)
                dctx={'path':path,'represented_handles':tuple(expanded),
                      'scheduled_handles':tuple(scheduled),'already_represented':False,
                      'recursive_reentry':False,'domain_reentry':domain_reentry,
                      'reentry_handles':tuple(sorted(overlap))}
                decision=str(ai.continue_or_terminate(node,edge,intent,dctx)).upper()
                if decision.endswith('CONTINUE'):
                    queue.append((target,d+1,h,edge.relation,path+(target,),relpath+(edge.relation,)))
                    scheduled.add(target)
                elif decision.endswith('TERMINATE'):
                    emit_leaf(node,edge,target,path,relpath,'AI_SEMANTIC_TERMINATION')
                elif decision.endswith('DEFER'):
                    add_frontier(target)
                else:
                    graph.edges=[e for e in graph.edges if (e.source,e.relation,e.target,e.provenance)!=key]
                    edge_keys.discard(key)

        return graph,realization

    @staticmethod
    def _validate_bounded_realization(realization,graph):
        if not realization.ordered_nodes or realization.root!=graph.root:
            raise ValueError('invalid finite realization')
        unknown={n.handle for n in realization.ordered_nodes}-set(graph.nodes)
        if unknown:
            raise ValueError('realization contains noncanonical handles')
        orders=[n.order for n in realization.ordered_nodes]
        if orders!=list(range(len(orders))):
            raise ValueError('realization order is nondeterministic')

    def handle(self,envelope):
        with self.lock:
            self.active+=1
            try:
                response=self._execute(envelope,self.modules,self.output)
                if response.status=='failed' and self.rollback is not None and self.probation>0:
                    failed=self.modules; self.modules=self.rollback; self.rollback=None; self.probation=0
                    try: failed.ai.close(); failed.api.close(); failed.library.close()
                    except Exception: pass
                    retry=self._execute(envelope,self.modules,self.output)
                    rr=dict(retry.recovery_receipt); rr['automatic_rollback']=True
                    return replace(retry,recovery_receipt=rr)
                if response.status=='complete' and self.probation>0:
                    self.probation-=1
                    if self.probation==0 and self.rollback is not None:
                        old=self.rollback; self.rollback=None
                        old.ai.close(); old.api.close(); old.library.close()
                return response
            finally:self.active-=1
    def replace_module(self,role,candidate):
        role=PortKind(role) if not isinstance(role,PortKind) else role; PortLoader.validate(candidate,role)
        with self.lock:
            if self.active: raise ModuleReplacementError('cannot replace module while requests are active')
            old_modules=self.modules; parts={'ai':old_modules.ai,'api':old_modules.api,'library':old_modules.library}; parts[role.value]=candidate
            staged=BraneLoader.assemble(parts['ai'],parts['api'],parts['library'])
            probe_subject=staged.api.instance.probe_subject(); staging_dir=self.output/'.staging'; staging_dir.mkdir(parents=True,exist_ok=True)
            probe=self._execute({'operation':'generate_report','subject':probe_subject,'request_id':f'stage-{uuid4().hex}','depth':'structural','coverage_mode':'annotated'},staged,staging_dir,probe=True)
            for p in staging_dir.glob('*'): p.unlink(missing_ok=True)
            try:staging_dir.rmdir()
            except OSError:pass
            if probe.status!='complete':
                if candidate not in (old_modules.ai,old_modules.api,old_modules.library): candidate.close()
                raise ModuleReplacementError('candidate failed staged operational compatibility')
            if self.rollback is not None:
                self.rollback.ai.close(); self.rollback.api.close(); self.rollback.library.close()
            self.rollback=old_modules; self.modules=staged; self.probation=1
            return {'status':'mounted','role':role.value,'version':candidate.manifest.version,'staged':True,'rollback_window_requests':1}
    def close(self):
        for x in (self.modules.ai,self.modules.api,self.modules.library):x.close()
        if self.rollback:
            for x in (self.rollback.ai,self.rollback.api,self.rollback.library):x.close()
            self.rollback=None
