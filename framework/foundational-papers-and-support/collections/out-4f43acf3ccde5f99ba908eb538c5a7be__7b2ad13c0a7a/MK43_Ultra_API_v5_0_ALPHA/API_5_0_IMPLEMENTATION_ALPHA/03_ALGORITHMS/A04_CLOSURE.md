# A04 — Bounded Recursive Closure Recovery

```text
INPUT: root_handle, recovery_intent
OUTPUT: CanonicalGraph

1. Resolve and validate root.
2. Initialize queue with TraversalNode(root, depth=0, path=[root]).
3. Initialize visited-state keyed by (handle, direction, intent-scope).
4. While queue is not empty:
   a. Pop next node according to deterministic traversal policy.
   b. Recover node-specific provenance.
   c. Resolve node chirality.
   d. Admit node only if admissible.
   e. Add node to request-local graph.
   f. If termination condition reached, continue.
   g. Fetch direct typed neighbors for allowed directions.
   h. Filter relation types by intent and admission policy.
   i. For each edge in canonical order:
      i. verify edge provenance and canonical membership;
      ii. construct candidate child path;
      iii. enforce cycle, depth, node, edge, and time budgets;
      iv. resolve child provenance and chirality;
      v. evaluate admissibility;
      vi. add accepted direct edge without path promotion;
      vii. enqueue child if continuation is allowed.
5. Attach equations and provenance references per node.
6. Record rejected continuations and reasons in diagnostics.
7. Validate complete graph.
8. Return immutable graph.
```
