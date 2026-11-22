from __future__ import annotations
import json, zipfile, hashlib, importlib.util, sys, tempfile, shutil, base64
from pathlib import Path
from uuid import uuid4
from dataclasses import dataclass
from .ports import *
from .errors import ModuleCompatibilityError

@dataclass(frozen=True)
class TrustPolicy:
    require_checksum:bool=True
    require_signature:bool=False
    trusted_public_keys:dict[str,bytes]|None=None
    max_archive_bytes:int=256*1024*1024
    max_members:int=10000
    max_uncompressed_bytes:int=2*1024*1024*1024

class PortLoader:
    REQUIRED_CONTRACT='2.0'; MANIFEST='brane_module.json'
    METHODS={
      PortKind.AI:('interpret','rank','continue_or_terminate','place_continuation','collapse','validate_collapse','dimension_model','fork_request_context','canonical_fingerprint','healthcheck'),
      PortKind.API:('resolve','neighbors','recover_closure','recover_equations','recover_provenance','resolve_chirality','admissible','probe_subject','validate_graph','dimension_model','fork_request_context','canonical_fingerprint','healthcheck'),
      PortKind.LIBRARY:('recover','recover_equations','recover_models','recover_analogies','recover_explanations','assemble_chunk','recover_batch','dimension_model','fork_request_context','canonical_fingerprint','healthcheck')}
    @classmethod
    def from_instance(cls,role,instance,name=None,*,development_mode=False):
        required=('canonical_state_policy','rewrite_policy','domain_ids','contract_version','internal_dimension')
        if not development_mode:
            missing=[x for x in required if not hasattr(instance,x)]
            if missing: raise ModuleCompatibilityError('instance lacks explicit module declarations')
        m=ModuleManifest(name or type(instance).__name__,role,str(getattr(instance,'version','0')),str(getattr(instance,'contract_version','')),f'{type(instance).__module__}:{type(instance).__name__}',int(getattr(instance,'internal_dimension',0)),str(getattr(instance,'canonical_state_policy','')),str(getattr(instance,'rewrite_policy','')),str(getattr(instance,'chirality_model','builtin')),str(getattr(instance,'provenance_model','builtin')),tuple(getattr(instance,'domain_ids',())),tuple(getattr(instance,'capabilities',())))
        x=LoadedModule(m,instance); cls.validate(x,role); return x
    @staticmethod
    def _safe_extract(z,td,policy):
        if len(z.infolist())>policy.max_members: raise ModuleCompatibilityError('module archive member limit exceeded')
        total=sum(x.file_size for x in z.infolist())
        if total>policy.max_uncompressed_bytes: raise ModuleCompatibilityError('module archive expansion limit exceeded')
        base=td.resolve()
        for member in z.infolist():
            target=(td/member.filename).resolve()
            if base!=target and base not in target.parents: raise ModuleCompatibilityError('unsafe module archive path')
            if member.is_dir(): continue
            mode=(member.external_attr>>16)&0o170000
            if mode==0o120000: raise ModuleCompatibilityError('symbolic links are not allowed in module archives')
        z.extractall(td)
    @staticmethod
    def _verify_signature(raw,detached_signature,signer,policy):
        if not policy.require_signature:return
        if not detached_signature or not signer: raise ModuleCompatibilityError('detached module signature required')
        keys=policy.trusted_public_keys or {}
        if signer not in keys: raise ModuleCompatibilityError('untrusted module signer')
        try:
            from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
            sig=base64.b64decode(detached_signature) if isinstance(detached_signature,str) else detached_signature
            Ed25519PublicKey.from_public_bytes(keys[signer]).verify(sig,raw)
        except Exception as e: raise ModuleCompatibilityError('module signature verification failed') from e
    @classmethod
    def from_zip(cls,path,role,expected_sha256=None,*,detached_signature=None,signer=None,trust_policy=None):
        policy=trust_policy or TrustPolicy(); p=Path(path).resolve()
        if not p.is_file(): raise ModuleCompatibilityError('module not found')
        if p.stat().st_size>policy.max_archive_bytes: raise ModuleCompatibilityError('module archive size limit exceeded')
        raw=p.read_bytes(); actual=hashlib.sha256(raw).hexdigest()
        if policy.require_checksum and not expected_sha256: raise ModuleCompatibilityError('detached module checksum required')
        if expected_sha256 and actual.lower()!=expected_sha256.lower(): raise ModuleCompatibilityError('detached module checksum mismatch')
        td=Path(tempfile.mkdtemp(prefix=f'brane_{role.value}_'))
        namespace=f'_brane_{role.value}_{uuid4().hex}'
        try:
            with zipfile.ZipFile(p) as z:
                try:m=ModuleManifest.from_dict(json.loads(z.read(cls.MANIFEST)))
                except Exception as e: raise ModuleCompatibilityError('invalid module manifest') from e
                if m.role is not role: raise ModuleCompatibilityError('wrong module role')
                cls._verify_signature(raw,detached_signature,signer,policy); cls._safe_extract(z,td,policy)
            modname,factory=m.entrypoint.split(':',1); package_path=td.joinpath(*modname.split('.')); file=package_path.with_suffix('.py'); subloc=None
            if not file.is_file(): file=package_path/'__init__.py'; subloc=[str(package_path)]
            if not file.is_file(): raise ModuleCompatibilityError('entrypoint not found')
            spec=importlib.util.spec_from_file_location(namespace,file,submodule_search_locations=subloc)
            if spec is None or spec.loader is None: raise ModuleCompatibilityError('cannot create isolated module spec')
            module=importlib.util.module_from_spec(spec); sys.modules[namespace]=module; spec.loader.exec_module(module); instance=getattr(module,factory)()
            lm=LoadedModule(m,instance,p,td,namespace); cls.validate(lm,role); return lm
        except Exception:
            for name in list(sys.modules):
                if name==namespace or name.startswith(namespace+'.'):sys.modules.pop(name,None)
            shutil.rmtree(td,ignore_errors=True); raise
    @classmethod
    def validate(cls,lm,role=None):
        m,i=lm.manifest,lm.instance
        if role and m.role is not role: raise ModuleCompatibilityError('wrong module role')
        if m.contract_version!=cls.REQUIRED_CONTRACT or str(getattr(i,'contract_version',''))!=m.contract_version: raise ModuleCompatibilityError('contract mismatch')
        if m.internal_dimension!=5 or int(getattr(i,'internal_dimension',0))!=5: raise ModuleCompatibilityError('module must be five-dimensional')
        if m.canonical_state_policy!='READ_ONLY' or getattr(i,'canonical_state_policy',None)!='READ_ONLY': raise ModuleCompatibilityError('canonical state must be READ_ONLY')
        if m.rewrite_policy!='DERIVED_ONLY' or getattr(i,'rewrite_policy',None)!='DERIVED_ONLY': raise ModuleCompatibilityError('rewrite policy must be DERIVED_ONLY')
        if not m.chirality_model or not m.provenance_model: raise ModuleCompatibilityError('chirality/provenance declaration required')
        for fn in cls.METHODS[m.role]:
            if not callable(getattr(i,fn,None)): raise ModuleCompatibilityError(f'{m.role.value} missing {fn}')
        dims=i.dimension_model()
        if not isinstance(dims,dict) or set(dims)!={'identity','dependency','chirality','recursion','provenance'} or not all(v is True for v in dims.values()): raise ModuleCompatibilityError('semantic five-dimensional contract failed')
        if i.healthcheck() is not True: raise ModuleCompatibilityError('module healthcheck failed')

class BraneLoader:
    @classmethod
    def from_instances(cls,ai,api,library): return cls.assemble(PortLoader.from_instance(PortKind.AI,ai),PortLoader.from_instance(PortKind.API,api),PortLoader.from_instance(PortKind.LIBRARY,library))
    @classmethod
    def from_zips(cls,a,b,c,checksums,*,trust_policy=None):
        if not checksums: raise ModuleCompatibilityError('detached checksums required for all module ports')
        return cls.assemble(PortLoader.from_zip(a,PortKind.AI,checksums.get('ai'),trust_policy=trust_policy),PortLoader.from_zip(b,PortKind.API,checksums.get('api'),trust_policy=trust_policy),PortLoader.from_zip(c,PortKind.LIBRARY,checksums.get('library'),trust_policy=trust_policy))
    @classmethod
    def assemble(cls,ai,api,library):
        for lm,role in ((ai,PortKind.AI),(api,PortKind.API),(library,PortKind.LIBRARY)): PortLoader.validate(lm,role)
        # Domain identifiers describe the independent knowledge/operation spaces owned
        # by each module. They are not a compatibility requirement. Composition occurs
        # exclusively through the Brane port contracts validated above.
        #
        # AI, API, and Library may therefore expose disjoint domain_ids without being
        # rewritten, merged, or forced to claim one another's domains.
        return BraneModules(ai,api,library)
