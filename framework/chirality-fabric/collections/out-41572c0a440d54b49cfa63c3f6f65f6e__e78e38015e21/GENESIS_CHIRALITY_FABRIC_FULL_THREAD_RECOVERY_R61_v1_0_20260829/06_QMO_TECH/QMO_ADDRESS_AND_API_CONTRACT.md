# QMO ADDRESS AND API CONTRACT

## QMO meaning

A Queryable Mathematical Object is a dependency graph whose mathematical objects, equations, claims, relations, provenance, status, supersession, and open debt are assigned stable query addresses.

A QMO address is a handle, not the object itself.

## Address grammar

This package uses:

- `@qmo/...` — complete queryable objects;
- `@object/...` — mathematical objects;
- `@eq/...` — equations/maps/operators;
- `@claim/...` — statements with explicit status;
- `@open/...` — unresolved debt;
- `@source/...` — source artifacts;
- `@rule/...` — recovery/firewall rules.

## Required record properties

Every important record carries:

- stable address;
- name/type;
- definition or expression;
- status;
- authority/provenance;
- notes/firewalls where necessary.

## Typed directional relations

Relations are directional and typed. Reverse query traversal does not invert mathematical semantics.

Examples:

- `DEPENDS_ON`
- `COMPOSES_TO`
- `REALIZES`
- `PROJECTS_TO`
- `CARRIES`
- `RESOLVES_TO`
- `SUPERSEDES`
- `BLOCKED_BY`
- `COMPARES_TO`

## SQLite / API relationship

`genesis_chirality_recovery.sqlite` is the persistent addressed ledger.

`qmo_api.py` is a read-only query surface over that ledger.

The API does not contain an independent mathematical state. It exposes the database state.

## No-silent-merge rule

Independent source/live models are referenced by receipt and authority. Their claims enter this recovery QMO only through explicit current-state records. The parent archives remain independent provenance reservoirs.
