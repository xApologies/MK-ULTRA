# A08 — Local Admissibility Evaluation

```text
INPUT: node, intent, chirality, provenance, optional_edge
OUTPUT: boolean decision plus diagnostic reason

REJECT when any condition holds:
- handle is absent from canonical handle set;
- direct edge is absent from canonical edge ledger;
- provenance is empty where provenance is required;
- relation type is excluded by intent;
- graph family is excluded by intent;
- confidence is below the intent threshold;
- audit status is rejected or fabricated;
- chirality is incompatible with an explicit local constraint;
- recursion/cycle/budget policy is exceeded;
- continuation would mutate or reclassify canon.

ACCEPT only when all required local constraints pass.
```
