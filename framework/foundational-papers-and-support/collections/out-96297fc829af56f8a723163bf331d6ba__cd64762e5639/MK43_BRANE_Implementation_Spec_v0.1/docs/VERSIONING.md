# Versioning Strategy

## Independent version axes

- BRANE container version;
- Collapse Intelligence version;
- API version;
- Library version;
- QMO schema version;
- runtime protocol version;
- report schema version.

## Example manifest identity

```text
BRANE: 0.1.0
Collapse Intelligence: 0.1.0
API: 4.3
Library: 1.0-draft
QMO schema: 1.0-draft
Runtime protocol: 1.0-draft
```

## Upgrade rules

- API updates can be loaded without changing intelligence when the adapter contract remains stable.
- New API handles create library coverage obligations.
- Library updates do not modify the API graph.
- Intelligence updates alter traversal realization only and require regression tests proving canonical invariants remain unchanged.
- A BRANE package version changes whenever its manifest composition changes.
