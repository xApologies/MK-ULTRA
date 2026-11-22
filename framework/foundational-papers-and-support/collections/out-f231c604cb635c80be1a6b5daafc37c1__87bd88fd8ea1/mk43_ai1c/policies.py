from __future__ import annotations
from dataclasses import dataclass, asdict, replace
from types import MappingProxyType
import hashlib, json
from .errors import PolicyError

@dataclass(frozen=True)
class TraversalPolicy:
    """Adaptive Tree/Branch/Leaf policy.

    No numeric node, edge, depth, branch, realization, or time value is a
    completion law.  A Tree closes only through semantic TERMINATE decisions.
    """
    policy_id: str = 'mk43-ai-tree-leaf-v2'
    cycle_policy: str = 'REGISTER'
    admissibility_policy: str = 'API_REQUIRED'
    continuation_enabled: bool = True
    deterministic_seed: int = 43
    relevance_weight: float = 3.0
    centrality_weight: float = 2.0
    alignment_weight: float = 3.0
    continuity_weight: float = 1.5
    provenance_weight: float = 1.5
    admissibility_weight: float = 2.0
    redundancy_penalty: float = 2.0
    cycle_penalty: float = 3.0
    recursive_reentry_weight: float = 4.0
    domain_saturation_weight: float = 3.0
    terminate_below: float = -1e9
    defer_below: float = -1e9

    def validate(self):
        if self.cycle_policy not in {'REGISTER','REJECT'}:
            raise PolicyError('unsupported cycle policy')
        return True

    def fingerprint(self):
        return hashlib.sha256(json.dumps(asdict(self),sort_keys=True,separators=(',',':')).encode()).hexdigest()

DEFAULT_POLICY=TraversalPolicy()
POLICY_REGISTRY=MappingProxyType({DEFAULT_POLICY.policy_id:DEFAULT_POLICY})

_LEGACY_HARD_CAP_OPTIONS={
    'major_branch_limit','edge_budget','node_budget','depth_budget','time_budget_ms','max_depth'
}

def policy_from_options(options):
    options=dict(options or {})
    # Legacy hard-cap options are intentionally ignored.  They may arrive from
    # older Runtime clients, but they never participate in Tree completion.
    for key in _LEGACY_HARD_CAP_OPTIONS:
        options.pop(key,None)
    allowed={k for k in TraversalPolicy.__dataclass_fields__ if k!='policy_id'}
    control={'termination_handles','defer_handles','invalid_handles','audience','completeness_mode'}
    unknown=set(options)-allowed-control
    if unknown:
        raise PolicyError('unknown policy options: '+','.join(sorted(unknown)))
    changes={k:options[k] for k in allowed if k in options}
    p=replace(DEFAULT_POLICY,**changes)
    p.validate()
    return p
