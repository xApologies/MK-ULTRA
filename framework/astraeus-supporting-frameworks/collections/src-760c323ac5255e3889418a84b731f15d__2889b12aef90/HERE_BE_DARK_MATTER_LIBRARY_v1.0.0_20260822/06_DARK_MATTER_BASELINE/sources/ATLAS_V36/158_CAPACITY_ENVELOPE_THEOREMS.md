# 158 — Capacity Envelope Theorems

## Theorem 21.1 — Local Flow Bound

Assume

```text
Phi_ij = kappa_ij A_ij (C_j-C_i)
kappa_ij >= 0
A_ij >= 0
```

and bounded feasible endpoint set `D_ij`.

Then

```text
|Phi_ij|
<=
kappa_ij A_ij DeltaC_ij^abs.
```

### Proof

By definition,

```text
|C_j-C_i| <= DeltaC_ij^abs
```

for every feasible endpoint pair. Multiplication by the nonnegative factor
`kappa_ij A_ij` preserves the inequality. QED.

---

## Theorem 21.2 — Runtime-Capacity Upper Bound

For v20 runtime capacity

```text
T_run(e_ij)
=
sup_{Phi in F_run} Phi_ij,
```

we have

```text
T_run(e_ij)
<=
U_ij^+
=
kappa_ij A_ij DeltaC_ij^+.
```

### Proof

Every `Phi` in `F_run` satisfies the local bound. The supremum of a set bounded
above by `U_ij^+` is also bounded above by `U_ij^+`. QED.

---

## Theorem 21.3 — Constraint Monotonicity

If the admissible runtime state set is tightened so that

```text
D'_ij subseteq D_ij,
```

then

```text
DeltaC_ij'^+ <= DeltaC_ij^+
```

and therefore

```text
U_ij'^+ <= U_ij^+
```

when `kappa_ij` and `A_ij` are unchanged.

### Interpretation

Resolution, Bandwidth, R5 strain/recoverability, ancestry, and persistence can
reduce the realizable drive without being inserted as arbitrary multiplicative
parameters.

---

## Theorem 21.4 — Zero-Admissibility Channel

If

```text
A_ij = 0,
```

then

```text
Phi_ij = 0
U_ij^+ = 0
T_run(e_ij)=0.
```

Thus an inadmissible relation carries no runtime continuity flow under this
constitutive branch.

---

## Theorem 21.5 — Boundedness

If

```text
0 <= kappa_ij <= kappa_max
0 <= A_ij <= A_max
C_min <= C <= C_max
```

on a finite region, then

```text
T_run(e_ij)
<=
kappa_max A_max (C_max-C_min).
```

The runtime edge capacity is finite.

## Source-status boundary

The theorems are exact **conditional mathematics**. Their physical applicability
is conditional on the recovered ER-flow constitutive relation being operative at
the Resolution under study.
