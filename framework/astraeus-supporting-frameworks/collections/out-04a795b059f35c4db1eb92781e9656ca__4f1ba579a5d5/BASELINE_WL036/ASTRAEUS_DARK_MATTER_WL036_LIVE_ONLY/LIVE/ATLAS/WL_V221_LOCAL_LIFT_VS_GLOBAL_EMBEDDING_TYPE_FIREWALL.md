# WL-v221 — Local Lift vs Global Embedding Type Firewall

**QMO:** QMO-AST-DM-WL-105  
**Work layer:** WL-035  
**Parent promotions:** 0  
**Status:** TYPE_LEVEL_MISMATCH IDENTIFIED

## The apparent shortcut fails

Transduction Geometry defines the formal lift family at the state level:

```text
LiftSet(f,x) = { y in F(V) | Adm_f(x,y) }.
```

A connection selects a member of this state-level lift family when defined.

Dark Matter 2.2, however, asks for a **global bundle embedding map**:

```text
iota_H:E_H^R ↪ E
```

satisfying base commutation, inheritance equivariance, injectivity, and constraint-kernel admission.

Therefore:

```text
state lift y in LiftSet(f,x)
!=
global embedding iota_H in Emb_H,phys^R.
```

The hidden-state OpenSlot cannot be closed by simply renaming a connection-selected state lift as `iota_H`.

## Source-native repair direction

Transduction Geometry already supplies the correct level-changing architecture:

```text
@transduction_descent
```

which glues local connection/admissibility data. Its formal layer defines:

```text
D21 Descent-Compatible Local Family
D22 Global Realization Object G(X)
D23 partial Glue operator
D25 Gluing Witness W_G(X,G)
D26 Realizable(X)
```

This is the first source-native route capable in principle of moving from local state lifts to a global realization object.

## Next handle

```text
@transduction_descent
```

with the specific question: does the Dark Matter hidden bundle provide source-supported local cover/transition data whose glued global realization can be tested against `Emb_H,phys^R`?
