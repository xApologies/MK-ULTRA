# AST-DM-WL-P013 — UCM Direct Rotational-History Dark-Readout Test

**Work layer:** WL-022  
**Purpose:** Test an already-defined S3 History-bearing localized galaxy candidate directly through the recovered Universal Coupling Mechanism and existing graviton/Time-Shell/metric gravity branch.

## P013-0 — Fix Resolution and local matter readout

Choose Resolution `R` and one localized galaxy/readout domain `Sigma_g^2`.

Select candidate Histories:

```text
H0 = trivial/common-mode relative rotational History
H1 = persistent nontrivial shear/holonomy History.
```

Require as a test control:

```text
Read_Q^R(M_g(H0)) = Read_Q^R(M_g(H1)).
```

If this fails, the selected pair is not a dark-readout pair at R.

## P013-1 — Complete admitted UCM runtime records

Construct complete records

```text
X0^R = Complete_UCM(M_g(H0), E_g, C_fixed)
X1^R = Complete_UCM(M_g(H1), E_g, C_fixed).
```

Hold intended comparison controls fixed. Record every field that cannot be fixed and justify why.

Fail if either record is not an admitted persistent-manifold UCM input.

## P013-2 — Perturbation gate

Compute/source-evaluate

```text
P0 = Perturb(M0,E_g)
P1 = Perturb(M1,E_g).
```

Record

```text
Sep_P = [P0 != P1].
```

A null result here means the selected History distinction is not a UCM source distinction under the chosen completion.

## P013-3 — ER redistribution gate

```text
D0 = R_ER(P0)
D1 = R_ER(P1)
Sep_ER = [D0 != D1].
```

Retain any annihilation of the distinction as a candidate-null outcome.

## P013-4 — R4 corridor gate

```text
C4_0 = Corridors_R4(D0,E_g)
C4_1 = Corridors_R4(D1,E_g)
Sep_R4 = [C4_0 != C4_1].
```

Do not infer selected topology from candidate-set difference alone.

## P013-5 — R5 ordered-resolution gate

```text
Q5_0 = Resolve_R5(C4_0)
Q5_1 = Resolve_R5(C4_1)
Sep_R5 = [Q5_0 != Q5_1].
```

This is the principal UCM coupling-resolution comparison.

## P013-6 — R6/R7 persistence gate

```text
S6_0 = Stabilize_R6(Q5_0)
S6_1 = Stabilize_R6(Q5_1)
Sep_R6 = [S6_0 != S6_1].
```

Run R7 persistence/recoverability verification for both ledgers. A candidate dark distinction must not rely on a nonpersistent failed topology.

## P013-7 — Existing gravity handoff

Use only the recovered gravity chain:

```text
UniversalCouplingEvent
-> readable graviton / graviton projection
-> continuity perturbation
-> Time-Shell projection operator
-> weak-field metric perturbation
-> projected spacetime metric
-> gravity/GR readout.
```

Define only the composed test readout

```text
Read_G^R(Xk).
```

Then

```text
Sep_G = [Read_G^R(X0) != Read_G^R(X1)].
```

Do not create an alternative scalar gravity law if this branch already supplies the required comparison.

## P013-8 — Dark-readout verdict

PASS AS INTERNAL DARK-READOUT WITNESS only if

```text
Read_Q^R(X0) = Read_Q^R(X1)
```

and

```text
Read_G^R(X0) != Read_G^R(X1).
```

Otherwise retain one of:

```text
FAIL_MATTER_EQUIVALENCE
NULL_AT_PERTURB
NULL_AT_ER_REDISTRIBUTION
NULL_AT_R4
NULL_AT_R5
NULL_AT_R6_R7
NULL_AT_GRAVITY_PROJECTION
INCOMPLETE_TYPING
```

## P013-9 — Optional component diagnostics

Only after the direct gravity comparison, optionally inspect:

```text
coupling telemetry
relational load
native rho_E
readable density
Delta T_mn
```

for explanatory decomposition. These are not prerequisites for the direct UCM gravity test.

## P013-10 — Observational admission

An internal dark-readout witness is not by itself physical dark matter. Physical admission additionally requires a declared map to accepted galactic observables and comparison against ordinary matter/GR/null alternatives under frozen parameters.
