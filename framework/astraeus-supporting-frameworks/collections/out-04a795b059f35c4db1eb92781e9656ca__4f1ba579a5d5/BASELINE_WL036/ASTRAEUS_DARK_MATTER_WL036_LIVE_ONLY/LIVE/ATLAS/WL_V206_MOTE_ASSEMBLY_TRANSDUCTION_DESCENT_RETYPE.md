# WL-v206 — Mote Assembly as a Transduction-Descent Problem

**QMO:** QMO-AST-DM-WL-090  
**Work layer:** WL-033  
**Parent promotions:** 0  
**Status:** CROSS-SOURCE QMO COMPOSITION / ROLE RETYPE

## Query

Combine the Time-Space mote-assembly gap with the frozen Transduction Geometry v1.0 admissibility/gluing API.

## Recovered Transduction Geometry objects

The executable Transduction Geometry query surface returns:

```text
@admissibility_relation
Type: structural relation
Definition: Adm_f(x,y), admissible continuation along dependency arrows.
```

```text
@transduction_descent
Type: descent architecture
Definition: local-to-global gluing architecture for connections/admissibility data.
```

```text
@gluing_data
Type: transition data
Definition: representative local transition maps plus their
            equivalence/gauge class for reconstruction and descent auditing.
```

The formal layer also defines:

```text
D21 Descent-Compatible Local Family
D22 Global Realization Object
D23 Glue: partial operator from descent-compatible local families
          to global realizations
D25 Gluing Witness
D26 Realizable(X) iff a valid gluing witness exists
```

## Retype

The source statement

```text
Mote Ensemble -> ER Foam
```

is therefore best treated at the work layer as a **realization problem**:

```text
local mote family
  + admissible pair/overlap data
  + transition maps
  + descent compatibility
        |
        v
      Glue
        |
        v
candidate global ER-adjacency realization
```

This does not solve the API's open assembly item. It prevents us from inventing a second general assembly algebra when a formal gluing architecture already exists.

## Important distinction

```text
@mote_ensemble -> @er_foam
```

is a registered Time-Space dependency.

```text
@transduction_descent
```

is a generic local-to-global formal architecture.

Their work-layer composition is a **role match**, not a new parent edge and not an identity theorem.

## Next handle

```text
@gluing_data
```

The next question is now concrete:

> What source-supported transition/overlap data can be instantiated for a mote ensemble so that the generic Glue machinery has an actual input?
