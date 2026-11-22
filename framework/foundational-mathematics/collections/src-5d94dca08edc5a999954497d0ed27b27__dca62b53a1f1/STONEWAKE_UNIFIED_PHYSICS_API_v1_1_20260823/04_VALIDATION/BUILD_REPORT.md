# Build / Validation Report

## Result

`QMO-STONEWAKE-PHYSICS-001` compiled successfully as one engine-facing queryable mathematical object.

## Compiled registries

- objects: 2,763
- equations: 861
- edges: 81,085
- duplicate-expression hash groups retained (not deleted): 57

### Equation contribution by domain
- API43: 305
- DARK_MATTER: 503
- HIGGS: 19
- QFT_GR: 28
- RAINBOW_ROAD: 6

## Validation policy

1. Source mathematical status is preserved; open/derived/source/audit labels are not flattened into one truth status.
2. Handle collisions across mounted domains are namespaced in the database rather than silently overwritten.
3. Exact duplicate expressions are retained with separate source records and a common expression hash.
4. STONEWAKE integration edges are explicitly marked `ENGINE_INTEGRATION`; they are routing architecture, not promoted source physics.
5. The raw API 4.3 75k+ edge set is materialized into the unified edge registry/database, avoiding a runtime dependency on the 131 MB source dependency index.
6. Dark Matter equation and composed/live dependency material, Higgs equations/objects/edges, QFT-GR formal equations/graph, and Rainbow Road corridor equations are mounted into the same QMO.

## Query tests

- SQLite integrity check: **ok**
- `@chirality -> @graviton`: route resolved through the compiled dependency fabric.
- `@higgs_field`: present in the unified QMO.
- plasma concept: queryable through the API 4.3 plasma handle; a specific `plasma_channel` remains a request-relative child QMO rather than a predeclared source equation.
