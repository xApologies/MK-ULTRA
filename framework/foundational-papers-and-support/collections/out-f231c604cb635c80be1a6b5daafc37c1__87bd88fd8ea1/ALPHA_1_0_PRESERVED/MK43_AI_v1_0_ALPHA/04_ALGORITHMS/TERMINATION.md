# Continuation and Termination

Decision domain:

```text
CONTINUE | TERMINATE | DEFER | REJECT_INVALID
```

`TERMINATE` is a realization boundary, not deletion. It must create a leaf cluster and continuation handle.

Typical termination causes include coherent explanatory boundary, depth budget, node budget, edge budget, time budget, low marginal relevance, repeated semantic content, or explicit request scope.

`DEFER` preserves unresolved candidates in the frontier. `REJECT_INVALID` is reserved for malformed, inadmissible, or API-invalid references and must carry evidence.
