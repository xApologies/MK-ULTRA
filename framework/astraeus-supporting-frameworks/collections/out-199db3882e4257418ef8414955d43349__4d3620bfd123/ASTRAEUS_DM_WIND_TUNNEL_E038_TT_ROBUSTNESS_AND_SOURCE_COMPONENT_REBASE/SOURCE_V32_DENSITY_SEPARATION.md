# 201 — Density Separation Witness for Readable Stress-Energy

## Status

```text
EXACT_CONDITIONAL_THEOREM
uses established stress-energy decomposition
requires component-preserving native->readable density typing
```

## 1. Problem

V31 proved that a scalar density does not uniquely determine a general stress-energy tensor.

That no-go remains correct.

But uniqueness is stronger than what the dark-network test actually needs.

To defeat

```text
T_full = T_vis
```

we only need **one readable tensor component that differs**.

## 2. Readable density component

Fix the same readable normalized timelike observer `u` for both states.

Define

```text
rho[T;u] = T_mn u^m u^n.
```

Let

```text
DeltaT = T_full - T_vis.
```

Then

```text
Delta rho_read
=
rho[T_full;u] - rho[T_vis;u]
=
DeltaT_mn u^m u^n.
```

## 3. Density-separation theorem

### Theorem 201.1

If

```text
Delta rho_read != 0,
```

then

```text
DeltaT != 0.
```

### Proof

Assume for contradiction that `DeltaT = 0`. Then every contraction of `DeltaT` is zero, in particular

```text
DeltaT_mn u^m u^n = 0,
```

contradicting `Delta rho_read != 0`.

Therefore

```text
Delta rho_read != 0
=>
T_full != T_vis.
```

QED.

## 4. Native hidden-load application

V29 supplies

```text
Delta rho_H > 0
```

under the positive hidden Relationship x TransitionCapacity assumptions.

The recovered API says

```text
@energy_density ENTERS @stress_energy_tensor.
```

The remaining typing requirement is therefore much smaller than the full v31 `P_T` problem.

Define the native-to-readable density transduction

```text
T_rho,R : rho_E(native) -> rho_readable.
```

The needed witness condition is merely

```text
T_rho,R(Delta rho_H) != 0
```

for the same readable observer/normalization.

If that condition holds, Theorem 201.1 gives

```text
T_full != T_vis.
```

## 5. What this does not prove

The theorem does not reconstruct:

```text
energy flux q_m,
pressure p,
anisotropic stress pi_mn,
the full equation of state,
the metric response,
a halo profile,
or dark matter identity.
```

It proves only that **one nonzero preserved density component is sufficient to separate two stress-energy tensors**.

This is compatible with the v31 no-go:

```text
one scalar does not determine a tensor,
```

while simultaneously establishing:

```text
one differing tensor component is enough to prove the tensors differ.
```

## 6. New primary question

The former large question

```text
P_T(u_full) ?= P_T(u_vis)
```

has a smaller sufficient attack:

```text
Does the Time-Shell/readable energy-density transduction annihilate Delta rho_H?
```

If yes, the static-load stress-source route dies.

If no, readable stress-energy separation is established for that pair.
