# 1. Primitives

## R1 — Formal carrier

Let `Fabr` be a formal global fabric and `A_B(Fabr)` its Bandwidth Algebra.

## R2 — Resolution index

Let `Res` be an indexing structure of modeled Resolutions. In monotone scopes, `R_i <= R_j` means `R_j` is at least as fine as `R_i`. General non-monotone Resolution systems are represented by a Resolution graph.

## R3 — Resolution congruence

For each `R`, define an equivalence/congruence `K_R` on the formal algebra. It encodes distinctions unavailable at `R`.

## R4 — Resolution quotient

```text
q_R : A_B -> A_B^R
A_B^R := A_B / K_R.
```

## R5 — Resolution equivalence

```text
x ~_R y  iff  q_R(x) = q_R(y).
```

## R6 — Readable geometry

```text
Geo_R(B) := Spec_T(A_B / K_R).
```

## R7 — Observational identity map

```text
Obs_R : FormalIdentity -> ObservationalIdentity_R.
```

`Obs_R` need not be injective. Its fibers are the formal identities conflated by readout at `R`.

## R8 — Resolution domain of a readout class

For a readable class `[x]_R`, define

```text
Dom_R([x]_R) := q_R^{-1}([x]_R).
```

This is the formal domain that shares one readable address at `R`.

## R9 — Persistence profile

```text
Pers(x) := { R in Res | x has a nontrivial distinguishable image at R }.
```

## R10 — Emergence Resolution

`R_emerge(x)` is the first modeled Resolution at which `x` becomes distinguishable, when a minimum exists.

## R11 — Blind core

```text
Blind(B) := { x | Pers(x) = empty }.
```

Blindness is observational under the modeled readout family, not formal nonexistence.
