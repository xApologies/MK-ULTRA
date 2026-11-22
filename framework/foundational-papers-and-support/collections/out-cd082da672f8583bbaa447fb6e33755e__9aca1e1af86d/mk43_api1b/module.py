from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from collections import deque
from threading import RLock
from typing import Any, Sequence
import hashlib, json, copy, re, os

try:
    from mk43_brane.models import CanonicalGraph, EdgeRecord, TraversalDirection
    from mk43_brane.errors import HandleResolutionError, ApiRecoveryError
except Exception:  # standalone diagnostic mode
    from dataclasses import dataclass, field
    from enum import Enum
    class TraversalDirection(str, Enum):
        UPSTREAM='upstream'; DOWNSTREAM='downstream'; BOTH='both'
    @dataclass(frozen=True)
    class EdgeRecord:
        source:str; relation:str; target:str; provenance:str|None=None; confidence:str='canonical'; chirality:str|None=None
    @dataclass
    class CanonicalGraph:
        root:str; nodes:set[str]=field(default_factory=set); edges:list[EdgeRecord]=field(default_factory=list)
        def add_edge(self,e): self.nodes.update((e.source,e.target)); self.edges.append(e)
    class HandleResolutionError(KeyError): pass
    class ApiRecoveryError(RuntimeError): pass

_NORMALIZE_RE = re.compile(r'[^a-z0-9]+')
_GLOBAL_CACHE: dict[str, dict[str, Any]] = {}
_GLOBAL_LOCK = RLock()

def _norm(value: str) -> str:
    raw=value.strip().lstrip('@')
    raw=re.sub(r'([a-z0-9])([A-Z])',r'\1_\2',raw)
    return _NORMALIZE_RE.sub('_', raw.lower()).strip('_')

def _stable_hash(obj: Any) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':'), default=str).encode()).hexdigest()

@dataclass(frozen=True)
class _Snapshot:
    canon_root: Path
    fingerprint: str

class API5Module:
    version = '1.B.0'
    contract_version = '2.0'
    internal_dimension = 5
    canonical_state_policy = 'READ_ONLY'
    rewrite_policy = 'DERIVED_ONLY'
    chirality_model = 'deterministic-edge-and-path-derived-v1'
    provenance_model = 'object-specific-canonical-registry-v1'
    domain_ids = ('mk43-ultra', 'gravity', 'canonical-mathematics')
    capabilities = (
        'resolve','neighbors','recover_closure','recover_equations','recover_provenance',
        'resolve_chirality','admissible','probe_subject','validate_graph'
    )

    def __init__(self, *, _snapshot: _Snapshot|None=None, _request_id: str|None=None):
        root = Path(__file__).resolve().parent.parent / 'CANON_4_3_PRESERVED'
        self._snapshot = _snapshot or _Snapshot(root, self._compute_fingerprint(root))
        self._request_id = _request_id
        self._lock = RLock()
        self._index = None
        self._handles = None
        self._normal = None
        self._aliases = None
        self._equations = None
        self._registry_provenance = None

    @staticmethod
    def _compute_fingerprint(root: Path) -> str:
        h=hashlib.sha256()
        for p in sorted(x for x in root.rglob('*') if x.is_file()):
            h.update(p.relative_to(root).as_posix().encode()); h.update(b'\0')
            with p.open('rb') as f:
                for chunk in iter(lambda:f.read(1024*1024), b''): h.update(chunk)
        return h.hexdigest()

    def dimension_model(self):
        return {'identity':True,'dependency':True,'chirality':True,'recursion':True,'provenance':True}

    def fork_request_context(self):
        clone=API5Module(_snapshot=self._snapshot, _request_id=hashlib.sha256(os.urandom(32)).hexdigest()[:24])
        # immutable caches may be shared safely after materialization
        with self._lock:
            clone._index=self._index; clone._handles=self._handles; clone._normal=self._normal
            clone._aliases=self._aliases; clone._equations=self._equations; clone._registry_provenance=self._registry_provenance
        return clone

    def canonical_fingerprint(self): return self._snapshot.fingerprint

    def integrity_report(self):
        baseline_path=self._snapshot.canon_root.parent/'CANON_BASELINE.json'
        errors=[]
        try: baseline=json.load(baseline_path.open(encoding='utf-8')).get('files',{})
        except Exception as exc: return {'status':'FAIL','errors':[f'baseline:{exc}'],'checked':0}
        for rel,expected in baseline.items():
            p=self._snapshot.canon_root/rel
            if not p.is_file(): errors.append('missing:'+rel); continue
            h=hashlib.sha256(p.read_bytes()).hexdigest()
            if h!=expected: errors.append('modified:'+rel)
        return {'status':'PASS' if not errors else 'FAIL','errors':errors,'checked':len(baseline)}

    def healthcheck(self):
        required=['RP42_DEPENDENCY_INDEX.json','MK43_Ultra_API_CURRENT_CANONICAL.md','CURRENT_RELEASE_MANIFEST.json','ALIAS_REGISTRY.json']
        return all((self._snapshot.canon_root/x).is_file() for x in required) and len(self._snapshot.fingerprint)==64 and self.integrity_report()['status']=='PASS'

    def _load_core(self):
        if self._index is not None: return
        key=self._snapshot.fingerprint
        with _GLOBAL_LOCK:
            cached=_GLOBAL_CACHE.get(key)
            if cached and 'index' in cached:
                self._index=cached['index']; self._handles=cached['handles']; self._normal=cached['normal']; self._aliases=cached['aliases']; return
            with (self._snapshot.canon_root/'RP42_DEPENDENCY_INDEX.json').open(encoding='utf-8') as f: idx=json.load(f)
            handles=frozenset(idx.get('handles',()))
            normal={}
            for h in sorted(handles):
                key_norm=_norm(h); normal.setdefault(key_norm,h); normal.setdefault(key_norm.replace('_',''),h)
            aliases={}
            ap=self._snapshot.canon_root/'ALIAS_REGISTRY.json'
            if ap.is_file():
                raw=json.load(ap.open(encoding='utf-8')).get('aliases',{})
                for alias,meta in raw.items(): aliases[alias]=meta['canonical'] if isinstance(meta,dict) else str(meta)
            for group in idx.get('alias_groups',()):
                valid=[x for x in group if x in handles]
                if valid:
                    canonical=sorted(valid,key=lambda x:(len(x),x))[0]
                    for alias in group: aliases.setdefault(alias,canonical)
            cached=_GLOBAL_CACHE.setdefault(key,{})
            cached.update(index=idx,handles=handles,normal=normal,aliases=aliases)
            self._index=idx; self._handles=handles; self._normal=normal; self._aliases=aliases

    def _load_registries(self):
        if self._equations is not None: return
        key=self._snapshot.fingerprint
        with _GLOBAL_LOCK:
            cached=_GLOBAL_CACHE.get(key,{})
            if 'equations' in cached:
                self._equations=cached['equations']; self._registry_provenance=cached['registry_provenance']; return
            equations={}; provenance={}
            for p in sorted(self._snapshot.canon_root.glob('*_EQUATION_REGISTRY.json')):
                try: data=json.load(p.open(encoding='utf-8'))
                except Exception: continue
                for rec in data.get('equations',()):
                    eq=rec.get('equation')
                    objects=rec.get('objects') or rec.get('handles') or ()
                    if not objects and rec.get('object'): objects=[rec['object']]
                    for h in objects:
                        if eq: equations.setdefault(h,[]).append(eq)
                        prov=rec.get('provenance')
                        if prov: provenance.setdefault(h,[]).append(f'{p.name}:{prov}')
            for p in sorted(self._snapshot.canon_root.glob('*_OBJECT_REGISTRY.json'))+sorted(self._snapshot.canon_root.glob('*_MECHANISM_REGISTRY.json')):
                try: data=json.load(p.open(encoding='utf-8'))
                except Exception: continue
                for key in ('objects','mechanisms'):
                    vals=data.get(key,())
                    if isinstance(vals,dict): vals=vals.values()
                    for rec in vals:
                        if not isinstance(rec,dict): continue
                        h=rec.get('handle') or rec.get('id')
                        prov=rec.get('provenance') or rec.get('source')
                        if isinstance(h,str) and h.startswith('@') and prov: provenance.setdefault(h,[]).append(f'{p.name}:{prov}')
            self._equations={k:tuple(dict.fromkeys(v)) for k,v in equations.items()}
            self._registry_provenance={k:tuple(dict.fromkeys(v)) for k,v in provenance.items()}
            cached=_GLOBAL_CACHE.setdefault(key,{})
            cached.update(equations=self._equations,registry_provenance=self._registry_provenance)

    def resolve(self, subject: str) -> str:
        self._load_core(); s=subject.strip()
        if s in self._aliases:
            target=self._aliases[s]
            if target in self._handles:return target
        if s in self._handles:return s
        candidate='@'+_norm(s)
        if candidate in self._handles:return candidate
        key_norm=_norm(s); mapped=self._normal.get(key_norm) or self._normal.get(key_norm.replace('_',''))
        if mapped:return mapped
        raise HandleResolutionError(subject)

    def probe_subject(self):
        self._load_core()
        for candidate in ('@gravity','@time_shell','@genesis_field'):
            if candidate in self._handles:return candidate
        if not self._handles: raise HandleResolutionError('empty API')
        return sorted(self._handles)[0]

    def _edge(self, rec, inverse=False):
        source,target=rec['source'],rec['target']; relation=rec['relation']
        if inverse: source,target=target,source; relation='INVERSE:'+relation
        chirality=rec.get('chirality') or ('CHI:'+hashlib.sha256(f"{rec['source']}|{rec['relation']}|{rec['target']}".encode()).hexdigest()[:16])
        return EdgeRecord(source,relation,target,rec.get('provenance'),rec.get('confidence','canonical'),chirality)

    def neighbors(self, handle: str, direction):
        self._load_core(); h=self.resolve(handle)
        try: direction=TraversalDirection(direction)
        except Exception: pass
        out=[]
        if direction in (TraversalDirection.DOWNSTREAM,TraversalDirection.BOTH):
            out.extend(self._edge(r) for r in self._index.get('edge_records_out',{}).get(h,()))
        if direction in (TraversalDirection.UPSTREAM,TraversalDirection.BOTH):
            out.extend(self._edge(r,True) for r in self._index.get('edge_records_in',{}).get(h,()))
        return tuple(out)

    def recover_closure(self, root: str, intent):
        root=self.resolve(root); direction=getattr(intent,'direction',TraversalDirection.BOTH)
        policy=getattr(intent,'traversal_policy',{}) or {}
        max_depth=int(policy.get('max_depth',256)); budget=int(policy.get('edge_budget',100000)); max_nodes=int(policy.get('node_budget',100000))
        graph=CanonicalGraph(root,{root},[]); q=deque([(root,0)]); seen=set(); count=0; edge_keys=set()
        while q:
            h,depth=q.popleft()
            if h in seen:continue
            if len(seen)>=max_nodes: break
            seen.add(h)
            if depth>=max_depth:continue
            for edge in self.neighbors(h,direction):
                count+=1
                if count>budget:break
                if edge.relation.startswith('INVERSE:'):
                    rel=edge.relation.split(':',1)[1]
                    canonical=EdgeRecord(edge.target,rel,edge.source,edge.provenance,edge.confidence,edge.chirality)
                else: canonical=edge
                key=(canonical.source,canonical.relation,canonical.target,canonical.provenance)
                if key not in edge_keys: graph.add_edge(canonical); edge_keys.add(key)
                nxt=edge.target
                if nxt not in seen:q.append((nxt,depth+1))
            if count>budget:break
        self.validate_graph(graph); return graph

    def recover_equations(self, handle: str) -> Sequence[str]:
        h=self.resolve(handle); self._load_registries(); return self._equations.get(h,())

    def recover_provenance(self, handle: str) -> Sequence[str]:
        h=self.resolve(handle); self._load_core(); self._load_registries(); vals=[]
        vals.extend(self._registry_provenance.get(h,()))
        for rec in self._index.get('edge_records_out',{}).get(h,()):
            if rec.get('provenance'): vals.append(rec['provenance'])
        for rec in self._index.get('edge_records_in',{}).get(h,()):
            if rec.get('provenance'): vals.append(rec['provenance'])
        if not vals: vals.append(f'RP42_DEPENDENCY_INDEX.json:handle:{h}')
        return tuple(dict.fromkeys(vals))

    def resolve_chirality(self, node, intent, provenance):
        if any('CHIRALITY_CONTRADICTION' in str(p) for p in provenance): return 'CHI:UNRESOLVED'
        if getattr(node,'parent',None) is None:return 'S0:ROOT'
        raw=f"{node.parent}|{node.incoming_relation}|{node.handle}|{'|'.join(provenance)}|{getattr(intent,'subject','')}"
        return 'CHI:'+hashlib.sha256(raw.encode()).hexdigest()[:16]

    def admissible(self, node, intent, chirality, provenance):
        try: h=self.resolve(node.handle)
        except Exception:return False
        if not chirality or chirality=='CHI:UNRESOLVED' or not provenance:return False
        if getattr(node,'parent',None) is not None:
            rel=getattr(node,'incoming_relation',None)
            parent=getattr(node,'parent',None)
            direct=any(e.target==h and (e.relation==rel or e.relation=='INVERSE:'+str(rel)) for e in self.neighbors(parent,TraversalDirection.BOTH))
            if not direct:return False
        return True

    def validate_graph(self, graph):
        self._load_core()
        if graph.root not in graph.nodes or graph.root not in self._handles: raise ApiRecoveryError('root missing or noncanonical')
        for e in graph.edges:
            if not e.source or not e.target or not e.relation: raise ApiRecoveryError('malformed edge')
            if e.source not in self._handles or e.target not in self._handles: raise ApiRecoveryError('fabricated handle')
            canonical_rel=e.relation.removeprefix('INVERSE:')
            found=any(r['source']==e.source and r['target']==e.target and r['relation']==canonical_rel for r in self._index.get('edge_records_out',{}).get(e.source,()))
            if not found: raise ApiRecoveryError(f'fabricated edge: {e.source} {e.relation} {e.target}')
        return None

    def close(self):
        # Canonical files are never modified; dropping references is sufficient.
        self._index=None; self._handles=None; self._normal=None; self._aliases=None
        self._equations=None; self._registry_provenance=None

def create_module(): return API5Module()
