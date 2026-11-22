from pathlib import Path
import hashlib
from .models import *
from .errors import CoverageError,ArtifactValidationError,PrivilegeViolation
class Validator:
    def coverage(self,q):
        expected=[q.key_for_node(n) for n in q.realization.ordered_nodes] if q.realization else []; unresolved=[]; recovered=[]; incomplete=[]
        for k in expected:
            p=q.packages.get(k)
            if p and p.resolved:
                recovered.append(k)
                returned={c.chunk_type for c in p.chunks if c.status=='recoverable'}
                missing=set(p.expected_chunk_types)-returned
                if missing: incomplete.append(k+':'+','.join(sorted(missing)))
            else: unresolved.append(k)
        dup=tuple(sorted({k for k in expected if expected.count(k)>1})); q.coverage=CoverageReceipt(len(expected),len(recovered),tuple(unresolved),dup,tuple(incomplete)); return q.coverage
    def enforce(self,r,mode):
        if mode is CoverageMode.STRICT and not r.complete: raise CoverageError('strict coverage failed')
    def substantive(self,q):
        if q.intent.depth!='complete': return
        for key,p in q.packages.items():
            if not p.resolved: continue
            meaningful=[c for c in p.chunks if c.chunk_type not in ('summary','heading','index') and len(c.content.strip())>=20]
            types={c.chunk_type for c in meaningful}
            if not meaningful or not (types & {'definition','explanation','equation','derivation','model','analogy','implication'}): raise CoverageError('complete report would substitute synopsis/index content')
            if p.expected_chunk_types and not set(p.expected_chunk_types)<=types: raise CoverageError('complete report omitted expected knowledge families')
    def fingerprints(self,modules): return {r:getattr(getattr(modules,r).instance,'canonical_fingerprint')() for r in ('ai','api','library')}
    def immutable(self,before,modules):
        after=self.fingerprints(modules)
        if before!=after: raise PrivilegeViolation('canonical module state changed during ordinary request')
    def artifact(self,path,q,fmt):
        p=Path(path)
        if fmt!='markdown' or p.suffix.lower()!='.md': raise ArtifactValidationError('artifact format mismatch')
        if not p.is_file() or p.stat().st_size==0: raise ArtifactValidationError('artifact missing or empty')
        raw=p.read_bytes(); raw.decode('utf-8'); expected=set(q.lifted); missing=expected-q.rendered_realizations
        if missing: raise ArtifactValidationError('artifact omitted realizations')
        return ArtifactReceipt(str(p),'markdown','UTF-8',len(raw),hashlib.sha256(raw).hexdigest(),len(q.rendered_realizations),len(q.coverage.unresolved if q.coverage else ()))
