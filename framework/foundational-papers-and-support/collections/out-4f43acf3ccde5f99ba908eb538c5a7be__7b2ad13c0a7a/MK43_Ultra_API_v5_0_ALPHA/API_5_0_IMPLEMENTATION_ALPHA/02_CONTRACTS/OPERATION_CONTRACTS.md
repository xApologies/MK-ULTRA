# Operation Contracts

## `resolve(subject)`

**Preconditions:** non-empty UTF-8 string; request context active.  
**Postconditions:** returns exactly one canonical handle.  
**Failures:** unknown subject, ambiguity, malformed subject, unavailable index.

## `neighbors(handle, direction)`

Returns immutable typed edge records from `edge_records_out` or `edge_records_in`. Direction must be explicit. Duplicate records may be retained where provenance or relation differs.

## `recover_closure(root, intent)`

Constructs a request-relative graph while preserving canonical identity. Traversal is bounded by depth, node, edge, time, and relation-policy budgets.

## `recover_equations(handle)`

Returns exact equations associated with the handle from dedicated registries and canonical-source references. No equation is synthesized silently.

## `recover_provenance(handle)`

Returns all directly recoverable source records for the handle, including line references, recovery passes, confidence, and audit status.

## `resolve_chirality(...)`

Maps canonical and request-local orientation evidence into a declared chirality state. Unknown evidence yields `UNRESOLVED`, never an invented orientation.

## `admissible(...)`

Evaluates local continuation against canonical admission policy, request intent, relation allowlist, chirality compatibility, provenance sufficiency, cycle policy, and resource budgets.

## `validate_graph(graph)`

Verifies every node exists, every edge is canonical, every path is traceable, every provenance record is attached to its object, all budgets were honored, and no canonical mutation occurred.
