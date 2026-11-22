# 64 — Recovered Admissibility Transition Operator

Atlas v7 used a generic weighted configuration Laplacian. The historical AERA archive supplies a more native algebra and therefore removes much of that arbitrariness.

## Recovered admissibility law

Phase II defines

```text
A_ij = alpha_ij * theta_ij * gamma_ij
```

with transition allowed iff `A_ij > 0`, together with

```text
A(P) = product_m A(e_m)
```

for path admissibility,

```text
A_ik = sum_j A_ij A_jk
```

for composition, and

```text
sum_j A_ij = 1
```

as a conservation/normalization identity.

These relations already have the algebraic form of a normalized transition kernel.

## Native transition operator

For a scalar amplitude/function `f` on admissible states define

```text
(T_A f)(i) = sum_j A_ij f(j).
```

Because

```text
sum_j A_ij=1,
```

`T_A` preserves the constant mode:

```text
T_A 1 = 1.
```

No differential operator is required.

## Path composition

The matrix product law

```text
(T_A^2)_ik = sum_j A_ij A_jk
```

matches the recovered two-step admissibility composition.

Likewise, `T_A^n` encodes n-step admissible propagation in the scalarized recovered sector.

## Geometry-first spectral operator

Two equivalent spectral conventions are available:

```text
transition convention: T_A
```

or

```text
defect/Laplacian convention: L_A = I - T_A.
```

They have the same eigenvectors. If

```text
T_A h = mu h,
```

then

```text
L_A h = (1-mu) h.
```

Therefore the choice between them is an eigenvalue normalization choice, not a change of mode geometry.

## Consequence for v7

The previous generic `D-W` operator is retained only as a broad graph-theoretic option. The **preferred native Atlas operator** is now the recovered admissibility transition family based on `A_ij`.

## Status

**RECOVERED ALGEBRA + ATLAS OPERATOR EXTRACTION.**
