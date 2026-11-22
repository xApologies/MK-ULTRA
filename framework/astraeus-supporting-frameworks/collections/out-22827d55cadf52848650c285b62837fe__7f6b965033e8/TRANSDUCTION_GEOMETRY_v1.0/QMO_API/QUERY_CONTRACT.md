# QMO Query Contract

The QMO is designed to be recoverable in a fresh thread or external runtime.

## Primary query surfaces

```text
object(handle)
neighbors(handle)
search(text)
ledger(L-###)
equation(handle)
path(source,target)
```

The reference CLI is:

```text
python qmo_api.py object @transduction_connection
python qmo_api.py neighbors @chirality_fabric
python qmo_api.py search "holonomy gluing"
python qmo_api.py ledger L-282
python qmo_api.py equation @transduction_curvature_defect
python qmo_api.py path @chirality @transduction_curvature --depth 6
```

## Query semantics

- Handles beginning with `@` are stable machine identities.
- Aliases resolve through `ALIAS_REGISTRY.json`.
- Edges are typed and provenance-bearing.
- Candidate status is preserved; queries must not silently promote candidates.
- Source provenance should be returned whenever a query result is used to support a claim.
- The SQLite database is a convenience index. JSON + canonical Markdown remain rebuildable source surfaces.
