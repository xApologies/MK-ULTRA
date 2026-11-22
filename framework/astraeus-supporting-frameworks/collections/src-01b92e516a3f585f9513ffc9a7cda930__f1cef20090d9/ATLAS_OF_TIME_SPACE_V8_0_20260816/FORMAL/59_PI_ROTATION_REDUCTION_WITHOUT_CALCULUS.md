# 59 — Pi-Rotation Reduction Without Calculus

The recovered Helicon archive contains the half-turn relation

```text
H(theta + pi) = H(theta).
```

Atlas v7 expresses this natively as an involutive symmetry on Helicon-compatible configurations.

Let

```text
r_pi : U_Hel -> U_Hel
```

be the half-turn re-embedding operation, with

```text
r_pi o r_pi = id.
```

Define the induced operator on configuration amplitudes/functions:

```text
(R_pi f)(c) = f(r_pi(c)).
```

Then

```text
R_pi^2 = I.
```

The pi-even projector is

```text
P_+ = (I + R_pi)/2.
```

The pi-odd projector is

```text
P_- = (I - R_pi)/2.
```

A Helicon-readable half-turn-invariant mode lies in

```text
H_+ = Im(P_+).
```

## Symmetry compatibility condition

Let `L_U` be the native spectral operator on the Unit-String configuration graph. If configuration weights satisfy

```text
w(r_pi c, r_pi d) = w(c,d),
```

then

```text
L_U R_pi = R_pi L_U.
```

Therefore `H_+` and `H_-` are invariant subspaces of `L_U`.

This recovers the Helicon half-turn symmetry as an algebraic quotient/symmetry reduction, without angular derivatives.

## Status

**CONDITIONAL THEOREM.**

The conclusion follows exactly when the declared Unit-String configuration weights are pi-equivariant.
