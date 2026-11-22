# 93 — Time-Shell Forward Realization

## Source lineage

Transduction Geometry v1.0 distinguishes a forward realization/transduction family `f_!` from backward
restriction/readback `f^*`. The source treats forward realization as cocartesian-lift-like and explicitly warns that the
forward and backward maps should not be forced to be inverses.

## Boundary contexts

Let `C_TS` be the Atlas candidate category/typed graph of Time-Shell contexts. Objects are persistent boundary contexts:

```text
U = (dXi_U, I_U, R_U, B_U, chi_U, Hist_U, Prov_U)
```

and a typed shell relation is:

```text
f : U -> V.
```

Let `F(U)` denote the admissible persistent organizational states over context `U`.

## Forward realization

For `x in F(U)`, define the forward shell realization candidate:

```text
f_! x in F(V).
```

The total lift is:

```text
(U,x) -> (V,f_!x).
```

The forward realization must preserve the Time-Shell invariant contract at the declared Resolution:

```text
I_T(x) recoverable from I_T(f_!x).
```

It may introduce target-local/readable structure and may change representation type.

## Cocartesian universality target

The stronger categorical condition is:

> any competing admissible realization over a composite base relation factors uniquely through the selected forward lift.

This is a **test target**, not yet promoted as a Time-Shell theorem.

## Provenance law

```text
Prov(f_!x) = Closure(Prov(x) + declared relation f + declared realization operations).
```

No undeclared ancestry may appear.

## Status

STRUCTURALLY SUPPORTED / CANDIDATE UNIVERSAL PROPERTY.
