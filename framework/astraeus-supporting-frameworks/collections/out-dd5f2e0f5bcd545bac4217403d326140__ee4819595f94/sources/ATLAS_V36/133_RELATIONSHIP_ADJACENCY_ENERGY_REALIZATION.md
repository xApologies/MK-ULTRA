# 133 — Relationship-as-Adjacency Energy Realization

## Purpose

The fresh API gives the native local energy-density socket

```text
rho_E = Relationship * TransitionCapacity / ContainmentVolume.
```

V16 typed the `TransitionCapacity` factor through Bandwidth support but left `Relationship` and `ContainmentVolume` open.

V17 follows the existing project language instead of inventing a new physical field.

Recovered Transduction Geometry states:

```text
Relationship ~ Adjacency
```

and refines path edges as **admissible relational adjacency**, not generic graph connectivity.

The recovered ER Time-Shell equation separately supplies weighted adjacency data `W_ij` and adjacency states `A_ij`.

---

## 1. Resolution-qualified relational neighborhood

At Resolution `R`, let

```text
N_R = (V_R, E_R)
```

be the current admissible ER / S3 continuity neighborhood.

For each active relation `e=(i,j)` define

```text
a_ij in AdjacencyState_R
```

and a nonnegative relation weight

```text
w_ij >= 0.
```

In the recovered ER Time-Shell sector, `w_ij` may be instantiated by `W_ij`, whose source meanings include:

```text
adjacency importance
local coherence strength
ER connectivity density.
```

Define a finite-sector relationship contribution

```text
r_ij := w_ij * a_ij
```

when the chosen adjacency realization `a_ij` is scalar-valued and nonnegative.

This scalar realization is a **sector model**, not a claim that every relationship in MK43 is fundamentally a real number.

---

## 2. Relationship valuation

For an address `i`, let

```text
Star_R(i)
```

be its incident admissible relational neighborhood.

Introduce

```text
rel_R : RelationalNeighborhood_R -> R_nonnegative
```

with minimum axioms:

```text
rel_R(empty)=0
monotonicity under addition of admissible nonnegative relations
admissible-isomorphism invariance
nontriviality.
```

A finite weighted-adjacency realization is

```text
Rel_R(i)
=
SUM_(j : (i,j) in E_R) r_ij.
```

For undirected ER adjacency each edge is counted once in a regional total and may appear in both endpoint-local ledgers.

---

## 3. Heterogeneous transition capacities

V16 defines transition capacity from the Resolution-qualified Bandwidth-supported transition family.

For each relation `e=(i,j)`, write

```text
t_ij := Tcap_R(e) >= 0.
```

The homogeneous local API form

```text
rho_E = Rel*Tcap/V
```

assumes a single capacity value for the relationship aggregate.

For heterogeneous edge capacities, the minimal additive-channel refinement is

```text
E_rel,R(i)
=
SUM_j r_ij * t_ij.
```

Then local density becomes

```text
rho_E^R(i)
=
E_rel,R(i) / V_R(i).
```

This edgewise sum is introduced as an explicit **additive-channel realization assumption**. It is not silently claimed as recovered API canon.

---

## 4. Theorem V17-T2 — API factorization is recovered in the homogeneous-capacity limit

If all active incident relationships at address `i` share one transition capacity

```text
t_ij = t_i
```

then

```text
E_rel,R(i)
=
SUM_j r_ij t_i
=
(
  SUM_j r_ij
) t_i
=
Rel_R(i) * Tcap_R(i).
```

Therefore

```text
rho_E^R(i)
=
Rel_R(i) * Tcap_R(i) / V_R(i),
```

which is exactly the recovered API form after collision-safe renaming.

QED.

---

## 5. Theorem V17-T3 — Saturated relation channels contribute zero relational transition energy

For any relation `e`, if Bandwidth saturation empties its supported transition family, v16 gives

```text
Tcap_R(e)=0.
```

Therefore

```text
r_e * Tcap_R(e)=0.
```

regardless of finite `r_e`.

Thus strong relationship / adjacency can coexist with zero transition-energy contribution in a saturated channel.

This distinction becomes important near black-hole saturation.

---

## 6. Regional energetic load

For a finite relation set `E(N)`, count every undirected relation once and define

```text
E_rel,R(N)
=
SUM_(e in E(N)) r_e t_e.
```

This quantity is a finite native relational-transition load for the chosen additive realization.

It is not yet calibrated to joules and is not identified with total relativistic energy without the downstream energy translator.

---

## 7. Why this matters for the dark branch

The UCM source projection already reads adjacency/topology, redistribution, strain, persistence, chirality, and Bandwidth into the downstream energy-momentum ledger.

V17 now gives the native energy-density socket a concrete ER/S3 realization candidate:

```text
ER adjacency relationship
x
Bandwidth-supported Transition Capacity
/
Resolution-qualified containment
-> native relational energy density
-> full UCM source projection
-> gravity.
```

This is the first v17 route that connects the recovered `Relationship` term to an existing Time-Space object without creating a new dark-matter primitive.

---

## Status

```text
Relationship ~ adjacency semantics                        RECOVERED
ER A_ij adjacency semantics                              RECOVERED
ER W_ij weighting semantics                              RECOVERED
Relationship valuation rel_R                             V17 TYPED
Finite weighted realization SUM r_ij                     V17 CANDIDATE REALIZATION
Heterogeneous additive edge-energy realization           V17 EXPLICIT ASSUMPTION
Homogeneous API-factorization theorem                    PROVED
Saturated-channel zero-contribution theorem              PROVED
Absolute physical calibration                            OPEN
```
