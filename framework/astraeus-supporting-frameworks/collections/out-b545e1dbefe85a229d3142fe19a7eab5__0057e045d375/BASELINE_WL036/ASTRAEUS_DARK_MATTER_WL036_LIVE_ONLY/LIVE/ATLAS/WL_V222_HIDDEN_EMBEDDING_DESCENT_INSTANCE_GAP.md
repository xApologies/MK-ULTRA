# WL-v222 — Hidden Embedding / Descent Instance Gap

**QMO:** QMO-AST-DM-WL-106  
**Work layer:** WL-035  
**Parent promotions:** 0  
**Protocol:** AST-DM-WL-P027  
**Status:** HIDDEN_EMBEDDING_DESCENT_INSTANCE_GAP

## Descent API result

Transduction Geometry v1.0 types:

```text
@transduction_descent
```

as a local-to-global gluing architecture for connection/admissibility data, and registers:

```text
@transduction_descent GLUES_LOCAL_INSTANCES_OF @transduction_connection.
```

The formal layer defines a descent-compatible local family, candidate global realization `G(X)`, partial `Glue`, gluing witness `W_G(X,G)`, and `Realizable(X)`.

## Dark Matter source audit

Dark Matter 2.2 defines the global hidden bundle and global constraint-preserving embedding family:

```text
pi_H:E_H^R -> T_H
Emb_H,phys^R = { iota_H:E_H^R ↪ E | ... }.
```

But the current Dark Matter API does **not** supply a hidden-bundle local cover, overlap transition family, triple-overlap/descent data, or a gluing witness whose global realization is certified to lie in `Emb_H,phys^R`.

Therefore the generic local-to-global mathematics exists, but the hidden-state embedding problem does not yet have the DM-specific descent instance required to invoke it.

## Retyped OpenSlot

The hidden embedding problem can now be queried as two nested instance questions without changing the parent API:

```text
H-LOCAL:
Does E_H^R admit source-supported local realization/lift data compatible with j_T, I_H/I, and ker(C)?

H-GLOBAL:
Do those local data admit a valid gluing witness whose global realization is an injective member of Emb_H,phys^R?
```

If both pass, physical member selection remains a separate question.

This is a work-layer factorization of the research problem, not a source theorem and not a new parent edge.

## Disposition

The typed-lift side door reaches a more precise **instance-data gap**, but does not close `@dm_hidden_state_embedding`.

Stop here. Return to API next-handle discovery rather than inventing the missing local cover/transition data.
