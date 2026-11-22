from __future__ import annotations
from dataclasses import dataclass,asdict,replace
from types import MappingProxyType
import hashlib,json
from .errors import PolicyError

@dataclass(frozen=True)
class TraversalPolicy:
    policy_id:str='mk43-ai-default-v1'; major_branch_limit:int=64; edge_budget:int=100000; node_budget:int=10000
    depth_budget:int=256; time_budget_ms:int=30000; cycle_policy:str='REGISTER'; admissibility_policy:str='API_REQUIRED'
    continuation_enabled:bool=True; deterministic_seed:int=43; relevance_weight:float=3.0; centrality_weight:float=2.0
    alignment_weight:float=3.0; continuity_weight:float=1.5; provenance_weight:float=1.5
    admissibility_weight:float=2.0; redundancy_penalty:float=2.0; cycle_penalty:float=3.0; budget_penalty:float=1.0
    terminate_below:float=-1e9; defer_below:float=-1e9
    def validate(self):
        if min(self.edge_budget,self.node_budget,self.depth_budget,self.time_budget_ms)<1: raise PolicyError('budgets must be positive')
        if self.cycle_policy not in {'REGISTER','REJECT'}: raise PolicyError('unsupported cycle policy')
        return True
    def fingerprint(self):
        return hashlib.sha256(json.dumps(asdict(self),sort_keys=True,separators=(',',':')).encode()).hexdigest()

DEFAULT_POLICY=TraversalPolicy()
POLICY_REGISTRY=MappingProxyType({DEFAULT_POLICY.policy_id:DEFAULT_POLICY})

def policy_from_options(options):
    options=dict(options or {}); allowed={k for k in TraversalPolicy.__dataclass_fields__ if k!='policy_id'}
    unknown=set(options)-allowed-{'termination_handles','defer_handles','invalid_handles','audience','completeness_mode'}
    if unknown: raise PolicyError('unknown policy options: '+','.join(sorted(unknown)))
    changes={k:options[k] for k in allowed if k in options}; p=replace(DEFAULT_POLICY,**changes); p.validate(); return p
