# Request Lifecycle

```text
1. BRANE forks API request context.
2. API validates request-local budgets and policy.
3. Subject is normalized without changing canon.
4. Alias resolver returns one canonical handle or a structured ambiguity.
5. Closure engine seeds traversal at the canonical handle.
6. Graph index supplies typed edges.
7. Chirality and admissibility are evaluated per continuation.
8. Accepted nodes and edges enter the request-local graph.
9. Equations and provenance are recovered per object.
10. Graph validator checks identity, edge, provenance, path, and budget invariants.
11. API returns an immutable canonical graph to BRANE.
12. Request-local caches and temporary derived structures are destroyed.
```
