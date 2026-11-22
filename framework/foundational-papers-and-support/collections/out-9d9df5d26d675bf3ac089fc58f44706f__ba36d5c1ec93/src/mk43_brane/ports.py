from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
class PortKind(str,Enum): AI='ai'; API='api'; LIBRARY='library'
@dataclass(frozen=True)
class ModuleManifest:
    name:str; role:PortKind; version:str; contract_version:str; entrypoint:str; internal_dimension:int=5; canonical_state_policy:str='READ_ONLY'; rewrite_policy:str='DERIVED_ONLY'; chirality_model:str='required'; provenance_model:str='required'; domain_ids:tuple[str,...]=(); capabilities:tuple[str,...]=(); sha256:str|None=None; signature:str|None=None; signer:str|None=None
    @classmethod
    def from_dict(cls,d):
        req=('name','role','version','contract_version','entrypoint','canonical_state_policy','rewrite_policy','chirality_model','provenance_model')
        miss=[k for k in req if not isinstance(d.get(k),str) or not d[k].strip()]
        if miss: raise ValueError('invalid manifest fields: '+', '.join(miss))
        return cls(d['name'].strip(),PortKind(d['role'].lower()),d['version'].strip(),d['contract_version'].strip(),d['entrypoint'].strip(),int(d.get('internal_dimension',0)),d['canonical_state_policy'].strip(),d['rewrite_policy'].strip(),d['chirality_model'].strip(),d['provenance_model'].strip(),tuple(map(str,d.get('domain_ids',()))),tuple(map(str,d.get('capabilities',()))),d.get('sha256'),d.get('signature'),d.get('signer'))
@dataclass
class LoadedModule:
    manifest:ModuleManifest; instance:object; source:Path|None=None; extraction_dir:Path|None=None; namespace:str|None=None
    def close(self):
        import shutil,sys
        try:
            fn=getattr(self.instance,'close',None)
            if callable(fn): fn()
        finally:
            if self.namespace:
                for name in list(sys.modules):
                    if name==self.namespace or name.startswith(self.namespace+'.'): sys.modules.pop(name,None)
            if self.extraction_dir and self.extraction_dir.exists(): shutil.rmtree(self.extraction_dir,ignore_errors=True)
@dataclass(frozen=True)
class BraneModules:
    ai:LoadedModule; api:LoadedModule; library:LoadedModule
