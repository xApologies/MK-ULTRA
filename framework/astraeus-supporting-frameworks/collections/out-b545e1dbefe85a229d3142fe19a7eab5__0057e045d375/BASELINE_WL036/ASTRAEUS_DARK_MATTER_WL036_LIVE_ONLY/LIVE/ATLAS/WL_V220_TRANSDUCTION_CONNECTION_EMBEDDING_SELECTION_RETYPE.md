# WL-v220 — Transduction Connection / Hidden-Embedding Selection Retype

**QMO:** QMO-AST-DM-WL-104  
**Work layer:** WL-035  
**Parent promotions:** 0  
**Status:** OPEN SELECTOR ROLE / NO CROSS-SOURCE EDGE

## Source result

Transduction Geometry v1.0 defines:

```text
@transduction_connection
```

as:

```text
Connection = typed, provenance-preserving,
admissibility-aware selection rule for horizontal lifts.
```

Registered relations include:

```text
@transduction_connection SELECTS_LIFTS_IN @typed_lift_architecture
@chirality CONSTRAINS_ADMISSIBILITY_OF @transduction_connection
@transduction_descent GLUES_LOCAL_INSTANCES_OF @transduction_connection
@transduction_connection HAS_COHERENCE_OBSTRUCTION @transduction_curvature
```

The same source also promotes the distinction:

```text
ADMISSIBLE LIFT FAMILY != CONNECTION-SELECTED LIFT.
```

Structural lift existence can be defined independently of connection selection.

## Dark Matter comparison

Dark Matter 2.2 already separates:

```text
1. Is Emb_H,phys^R nonempty?
2. If nonempty, which iota_H is physically realized?
```

This is role-compatible with the Transduction split:

```text
structural lift existence
!=
connection-selected lift.
```

That gives a work-layer organizational retype of the OpenSlot:

```text
H-EXIST: existence of at least one constraint-preserving realization map;
H-SELECT: physical selection from the admitted family.
```

## Null interface result

Direct Transduction QMO path queries return no path from `@transduction_connection` to either:

```text
@inherited_state_bundle
@admissibility
```

inside the frozen Transduction QMO registry. Dark Matter 2.2 likewise contains no direct edge from `@transduction_connection` to `@dm_hidden_state_embedding`.

Therefore the selector role is architectural only. It is not a recovered hidden-state selector.

## Next handle

The Transduction API itself says global connection data requires coherent gluing of local selectors. Follow:

```text
@transduction_descent
```

and ask whether local lift data can produce the global map type required by `Emb_H,phys^R`.
