# 157 — Global Runtime Capacity versus Local Envelope

## Purpose

Separate a **locally permitted constitutive maximum** from a **globally realizable
runtime flow**.

## Local envelope

For each persistent directed edge:

```text
U_ij^+
=
kappa_ij A_ij DeltaC_ij^+.
```

## Runtime capacity

Atlas v20 defines

```text
T_run(e)
=
sup {Phi(e) : Phi in F_run(G_*)}.
```

Since every globally feasible flow must also obey the local constitutive law,

```text
T_run(e_ij) <= U_ij^+.
```

Equality is **not** automatic.

## Strict-inequality mechanism

Suppose two candidate edges share a finite Bandwidth, ancestry, or conservation
constraint. Each edge may locally permit its own maximum while the two maxima
cannot occur simultaneously.

Then

```text
T_run(e_ij) < U_ij^+
```

can hold even though the local constitutive relation is satisfied exactly.

This is the correct mathematical place for global Time-Space constraints:

```text
local constitutive envelope
        ↓
R4 candidate availability
        ↓
R5 constrained selection
        ↓
R6 survivability
        ↓
R7 persistence
        ↓
globally realizable runtime capacity.
```

## Network consequence

Let `U` denote the edge-envelope assignment on a finite network. Any admissible
source-to-target runtime flow is also an ordinary capacity-constrained flow under
`U`. Therefore

```text
Cap_3^run(a,b)
<=
MinCut_U(a,b).
```

If the local envelopes can be jointly attained without violating any additional
Time-Space constraints, then equality reduces to the standard max-flow/min-cut
case from v20.

Otherwise the strict inequality records genuinely global recursive/topological
constraints that ordinary edge-capacity flow does not encode.

## Status

PROVED as a mathematical consequence of v20 feasible-flow capacity plus the
conditional local constitutive envelope.

No dark-matter identification follows from this result alone.
