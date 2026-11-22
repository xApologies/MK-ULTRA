# 32 — Canonical SU(2) Test Connection on S³

## Purpose

`S3` is diffeomorphic to the Lie group `SU(2)`. This makes `SU(2)` a natural **test representation** for the S3 continuity connection. This file does not declare that physical Helicon gauge symmetry is SU(2).

## Maurer–Cartan form

Let

```text
theta = g^(-1) dg
```

be the left Maurer–Cartan form on `SU(2) ~= S3`, satisfying

```text
d theta + theta ^ theta = 0.
```

## Homogeneous one-parameter connection

Define

```text
A_k = k theta,
```

where `k` is a real parameter.

Its curvature is

```text
F_k
= dA_k + A_k ^ A_k
= k(k-1) theta ^ theta.
```

Hence

```text
F_k = 0  iff  k = 0 or k = 1.
```

For every

```text
k notin {0,1},
```

the connection is smooth, homogeneous, and nonflat.

## Interpretation

The standard carrier `S3 x S2` can therefore support a continuous family of nontrivial S3 connection states without invoking topological twisting of the S2 bundle.

The two flat endpoints have different gauge presentations but no local curvature load. Intermediate states carry curvature and therefore can generate nontrivial corridor holonomy.

## Curvature magnitude

For a round S3 metric of radius `R3` and a fixed invariant inner product on the Lie algebra,

```text
||F_k||^2
= C3 * k^2 (1-k)^2 / R3^4,
```

where `C3 > 0` depends only on normalization conventions.

The crucial property is not the numerical coefficient but spatial homogeneity:

```text
||F_k(p)||^2 = constant  for all p in S3.
```

This fact drives the v4 localization result.
