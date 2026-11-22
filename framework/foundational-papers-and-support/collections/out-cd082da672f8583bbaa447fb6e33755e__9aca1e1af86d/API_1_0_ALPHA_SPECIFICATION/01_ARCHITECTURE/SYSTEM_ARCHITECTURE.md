# API 5.0 System Architecture

```text
BRANE 2.1
   │
   ▼
API⁵ Adapter
   ├── Request Context Factory
   ├── Subject / Alias Resolver
   ├── Canonical Object Store
   ├── Typed Dependency Graph Engine
   ├── Equation Registry Router
   ├── Provenance Engine
   ├── Chirality Resolver
   ├── Admissibility Engine
   ├── Closure Recovery Engine
   ├── Graph Validator
   └── Integrity / Fingerprint Service
          │
          ▼
Preserved API 4.3 Canon
```

## Architectural rule

The canonical substrate is immutable during requests. Every query operates through a request-local context and may create only derived objects. No request can overwrite, delete, normalize away, or silently promote canonical records.

## Five internal dimensions

```text
API⁵ = (Identity, Dependency, Chirality, RecursiveDepth, Provenance)
```

- **Identity**: canonical handle, aliases, object class, namespace.
- **Dependency**: typed incoming/outgoing edges and graph-family membership.
- **Chirality**: orientation and request-relative continuation state.
- **RecursiveDepth**: traversal level, closure horizon, path ancestry.
- **Provenance**: source lines, recovery pass, registry source, confidence, audit status.

BRANE supplies the sixth coordinate—realization—outside the API module.
