# Local Mini API

Database:

    resolution_operator_qmo.sqlite

This SQLite database is the package-local QMO/API.

## Core queries

List all QMO objects:

```sql
SELECT qmo_address, object_type, authority, title
FROM qmo_objects
ORDER BY qmo_address;
```

Resolve one address:

```sql
SELECT *
FROM qmo_objects
WHERE qmo_address='@resolution_operator';
```

Find equations for an object:

```sql
SELECT e.equation_id, e.label, e.expression, e.status
FROM equations e
JOIN qmo_equations qe ON qe.equation_id=e.equation_id
JOIN qmo_objects q ON q.qmo_id=qe.qmo_id
WHERE q.qmo_address='@resolution_operator';
```

Follow dependencies:

```sql
SELECT src.qmo_address AS source,
       d.relation,
       dst.qmo_address AS target,
       d.authority
FROM dependencies d
JOIN qmo_objects src ON src.qmo_id=d.source_qmo_id
JOIN qmo_objects dst ON dst.qmo_id=d.target_qmo_id
WHERE src.qmo_address='@resolution_operator';
```

Read provenance:

```sql
SELECT q.qmo_address, p.event_type, p.description, p.authority_before, p.authority_after
FROM provenance p
LEFT JOIN qmo_objects q ON q.qmo_id=p.qmo_id
ORDER BY p.provenance_id;
```

Open questions:

```sql
SELECT qmo_address, question, blocker_type, status
FROM v_open_questions;
```

## Views

- `v_qmo_registry`
- `v_dependency_edges`
- `v_equation_ledger`
- `v_open_questions`
- `v_current_authority`
- `v_artifact_manifest`

## Authority convention

Current-authority views expose only present authority.
Retired/incorrect/drift material remains queryable in provenance and aliases.
