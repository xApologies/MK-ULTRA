# 91 — Dynamic Closure Recursion

## Purpose

Atlas v11 formalizes the recursive engine that has been used implicitly throughout MK43/AERA:
recursion does not merely iterate a fixed map on a fixed state space. Each recursive step can alter the
admissible transformation landscape through topological/identity closure.

## Native state

At recursive stage `n`, define the paired state:

```text
Z_n = (X_n, A_B^n)
```

where:

- `X_n` is the current organizational/topological state;
- `A_B^n` is the Bandwidth Algebra of transformations still available at that stage.

Let:

```text
U_n : X_n x A_B^n -> X_(n+1)
```

be an admissible update and:

```text
Cl : X -> Cl(X)
```

be the closure operator that determines the stabilized identity/topology class after update.

The next Bandwidth Algebra is not assumed equal to the previous one. It is reconstructed from the closure:

```text
A_B^(n+1) = Adm(Cl(X_(n+1)), R, chi, Id, Hist, ...)
```

Hence the recursion is:

```text
(X_n, A_B^n)
   -> X_(n+1)
   -> Cl(X_(n+1))
   -> A_B^(n+1)
   -> ...
```

## Definition — Dynamic Closure Recursion

A Dynamic Closure Recursion is a sequence

```text
Z_0 -> Z_1 -> Z_2 -> ...
```

with

```text
Z_n = (X_n, A_B^n)
```

such that each `A_B^(n+1)` is determined from the closure/readability/admissibility structure of the updated state,
rather than held fixed globally.

## Stabilizing branch

A branch is **Bandwidth-contracting** when

```text
Gen(A_B^(n+1)) subseteq Gen(A_B^n)
```

for the declared generator set. This need not occur at every stage, but when it persists it gives a finite or
asymptotic route toward closure.

A state is closure-stable in Identity class `[X]_Id` when:

```text
Succ_B(Cl(X)) subseteq [Cl(X)]_Id.
```

This reproduces the v9 persistence criterion in recursive-engine form.

## Failure amplification

Because `A_B^(n+1)` depends on the previous closure, a bad mathematical rule can alter not only one state but the
next admissibility landscape. A local inconsistency can therefore amplify structurally:

```text
bad update
 -> wrong closure
 -> wrong Bandwidth Algebra
 -> wrong next admissibility
 -> rapid recursive failure.
```

This is the formal reason recursive model branches can expose internal incompatibility quickly.

## Status

ATLAS_NATIVE — FORMALIZED v11.
