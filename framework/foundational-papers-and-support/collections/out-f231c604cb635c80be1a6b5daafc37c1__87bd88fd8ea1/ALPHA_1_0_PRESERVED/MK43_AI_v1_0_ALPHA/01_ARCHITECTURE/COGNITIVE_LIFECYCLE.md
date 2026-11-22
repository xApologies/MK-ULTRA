# Cognitive Lifecycle

1. Receive normalized request and isolated request context.
2. Interpret intent without inventing canonical entities.
3. Resolve candidate roots through API⁵.
4. Select a root or return a structured ambiguity result.
5. Build traversal policy from request constraints.
6. Recover graph neighborhoods or closure streams from API⁵.
7. Rank candidate branches.
8. Decide CONTINUE, TERMINATE, DEFER, or REJECT_INVALID.
9. Place continuations for every intentionally terminated reachable branch.
10. Request Library⁵ content only for selected realized nodes.
11. Collapse the realized tree into an ordered finite object.
12. Validate completeness, provenance, determinism, and policy compliance.
13. Return the derived realization to BRANE; never return QMO internals.
