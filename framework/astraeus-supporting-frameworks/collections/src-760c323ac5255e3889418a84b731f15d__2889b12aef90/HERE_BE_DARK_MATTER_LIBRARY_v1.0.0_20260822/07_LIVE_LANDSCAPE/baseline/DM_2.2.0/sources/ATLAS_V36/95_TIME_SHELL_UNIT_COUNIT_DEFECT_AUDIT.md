# 95 — Time-Shell Unit/Counit Defect Audit

## Source recovery

Transduction Geometry v1.0 already contains promoted audit objects:

```text
@adjoint_transduction_audit
@unit_defect
@counit_defect
```

with the definitions:

```text
unit defect   = discrepancy between x and f^* f_! x
counit defect = discrepancy between f_! f^* y and y.
```

The Atlas adopts these as **audit objects** without assuming an adjunction theorem.

## Unit round-trip

For source state `x in F(U)`:

```text
eta_x : x -> f^* f_! x.
```

Define the typed unit defect ledger:

```text
D_eta(x) = (
  d_Id,
  d_chi,
  d_Hist,
  d_Inv,
  d_R,
  d_B,
  d_Prov
).
```

The source Identity round-trip passes when the required components vanish or remain within their declared admissible
equivalence classes.

## Counit reconstruction

For target state `y in F(V)`:

```text
epsilon_y : f_! f^* y -> y.
```

Define:

```text
D_epsilon(y) = (
  d_target_local,
  d_Id,
  d_chi,
  d_Hist,
  d_Inv,
  d_Prov
).
```

A nonzero target-local defect can be legitimate when `y` contains information unavailable from source context `U`.

## No inverse requirement

The audit explicitly rejects:

```text
f^* = f_!^(-1)
```

as a general Time-Shell requirement.

## Round-trip persistence criterion

A source state is **Time-Shell round-trip persistent** over `f` when:

```text
IdWitness(x, f^*f_!x) exists
```

and every declared invariant in `I_T` remains recoverable.

## Status

RECOVERED AUDIT ARCHITECTURE + ATLAS TYPING.
