# Component Map

| Component | Responsibility | Canonical inputs | Outputs |
|---|---|---|---|
| `ManifestLoader` | Load and verify release metadata | manifests, checksums | verified release descriptor |
| `CanonicalStore` | Read canonical records | canonical Markdown, registries | immutable object views |
| `AliasResolver` | Resolve names and aliases | alias registry, handle set | canonical handle |
| `GraphIndex` | Serve typed adjacency and edge records | dependency index | edge sequences |
| `ClosureEngine` | Traverse admissible dependency closure | graph, intent | canonical graph |
| `EquationRouter` | Recover exact equations | equation registries, canonical source | ordered equations |
| `ProvenanceEngine` | Recover source-specific evidence | edge/object metadata | provenance records |
| `ChiralityEngine` | Resolve node orientation | object metadata, request intent | chirality label/state |
| `AdmissibilityEngine` | Decide legal continuation | node, edge, intent, provenance | admissible/rejected + reason |
| `GraphValidator` | Enforce graph invariants | recovered graph | pass or structured failure |
| `RequestContext` | Isolate per-request state | immutable shared stores | local caches, budgets, diagnostics |
| `API5Adapter` | Expose BRANE protocol | all services | API⁵ operations |
