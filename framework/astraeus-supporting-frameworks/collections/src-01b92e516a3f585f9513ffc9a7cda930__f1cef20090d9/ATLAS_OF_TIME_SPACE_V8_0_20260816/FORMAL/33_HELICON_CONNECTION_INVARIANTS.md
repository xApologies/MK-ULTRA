# 33 — S³ Helicon Connection Invariants

## Connection state

Let `A_H` denote the working S3 Helicon/chirality connection with curvature

```text
F_H = dA_H + A_H ^ A_H.
```

The Atlas requires quantities that are invariant under changes of local presentation before they are allowed to feed a physical readout.

## Quadratic curvature load

Define

```text
I2(p) = <F_H(p), F_H(p)>,
```

using the S3 metric and an invariant inner product on the internal algebra.

`I2` is the first local scalar candidate for continuity load.

## Chern–Simons history functional

Because the continuity base is three-dimensional, a natural orientation-sensitive history object is the Chern–Simons functional

```text
CS[A_H]
=
(1 / 8 pi^2)
integral_S3 tr(
  A_H ^ dA_H
  + (2/3) A_H ^ A_H ^ A_H
)
mod Z.
```

For the homogeneous test connection

```text
A_k = k theta
```

and winding convention

```text
N = (1 / 24 pi^2) integral_S3 tr(theta^3),
```

one obtains

```text
CS[A_k]
= N (2 k^3 - 3 k^2)  mod Z
```

up to the global orientation / trace convention.

At the flat endpoints `k=0` and `k=1`, the Chern–Simons class is gauge-trivial modulo integers, while intermediate nonflat states can carry fractional history.

## Atlas interpretation

The pair

```text
(I2, CS mod Z)
```

provides a minimal distinction between

- local connection load / curvature,
- global orientation-sensitive connection history.

This is a candidate mathematical realization of the older language that chirality/Helicon organization carries **history** even when the bare Time-Space carrier is topologically simple.

## Status boundary

The invariants are standard differential-geometric constructions. Their identification with Helicon persistence, dark matter, or physical energy remains an Atlas realization problem.
