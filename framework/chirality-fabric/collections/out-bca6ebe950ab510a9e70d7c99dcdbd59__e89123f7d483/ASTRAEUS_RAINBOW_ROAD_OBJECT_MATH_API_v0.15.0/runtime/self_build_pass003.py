#!/usr/bin/env python3
"""Self-build pass 003 witness-fiber counterexample replay.
This replay is diagnostic: it verifies CE-RW-001 and reports the current frontier.
Canonical mutations were committed in the v0.3.0 release build and remain certificate-governed.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ce=json.load(open(ROOT/'reports'/'COUNTEREXAMPLE_CE_RW_001.json',encoding='utf-8'))
a=ce['fine_lineages']['ell_alpha']; b=ce['fine_lineages']['ell_beta']
core=lambda x:(x['provenance_root'],x['identity_witness_class'],x['invariant_residue'])
aug=lambda x:core(x)+(x['history_token'],)
result={
 'pass':'SELF_BUILD_PASS_003_RECOVERY_WITNESS',
 'counterexample':ce['counterexample_id'],
 'core_collision':core(a)==core(b),
 'history_augmented_separation':aug(a)!=aug(b),
 'conclusion':'Unqualified core witness is not universally separating; an additional recovery discriminator is necessary on colliding fibers. Ordered History is sufficient for CE-RW-001; global minimality remains open.',
 'next_frontier':'@recovery_history_signature_minimality'
}
print(json.dumps(result,indent=2))
