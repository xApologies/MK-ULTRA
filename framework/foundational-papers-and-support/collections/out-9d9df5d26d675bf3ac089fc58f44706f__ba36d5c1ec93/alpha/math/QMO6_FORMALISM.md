# QMO⁶ Formalism

## Definition

A Queryable Mathematical Object in BRANE 2.0 is a finite, request-relative six-dimensional substructure:

```text
QMO⁶(q) ⊂ B⁶
```

It is generated from the coordinated embeddings of AI⁵, API⁵, and Library⁵.

```text
QMO⁶(q) = Collapse_q(ι_AI(AI⁵), ι_API(API⁵), ι_LIB(Library⁵))
```

## Components

```text
QMO⁶ = (
  root,
  node_realizations,
  typed_relations,
  dependency_layers,
  chirality_states,
  recursive_frontier,
  provenance_map,
  library_resolution,
  projection_requirements,
  validation_state
)
```

## Lifecycle

```text
ABSENT
→ INITIALIZING
→ API_RESOLVING
→ GRAPH_REALIZED
→ LIBRARY_RESOLVING
→ KNOWLEDGE_REALIZED
→ PROJECTING
→ ARTIFACT_VALIDATED
→ DESTROYED
```

Optional policy may replace `DESTROYED` with `ARCHIVED_ENCRYPTED`, but no external component receives a raw QMO.

## Completeness

For requested handle set `H_q` and recovered handle set `H_r`:

```text
Complete(q) ⇔ H_q = H_r ∪ H_unresolved
```

where every element of `H_unresolved` has an explicit reason record.

Silent omission is forbidden.

## Cycle safety

Let `V_seen` be visited realized identities. Traversal must satisfy:

```text
visit(v) only if realization_key(v) ∉ V_seen
```

A realization key may include identity plus context:

```text
key(v) = (handle, branch, chirality, recursive_depth)
```

## Projection

A report projection is order-preserving with respect to the selected traversal order:

```text
π_report(QMO⁶) = ordered_sections
```

Each section must be populated by library recoveries, not merely by handle labels.
