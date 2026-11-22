# 37 — Variable S³ Connection and Localization

## Homogeneous connection is insufficient for halos

The homogeneous test connection

```text
A_k = k theta
```

has spatially constant curvature invariants. It can produce nontrivial continuity memory, but by itself it cannot distinguish one S3 address from another.

To obtain localized structure introduce a scalar Helicon amplitude / order profile

```text
eta : S3 -> R
```

and define

```text
A_eta = eta theta.
```

Then

```text
F_eta
=
d eta ^ theta
+ eta(eta-1) theta ^ theta.
```

The connection now contains two sources of local structure:

1. gradient / address variation `d eta`,
2. local non-Abelian curvature `eta(eta-1)`.

A local load scalar can therefore be built from

```text
I2[eta](p)
=
|| d eta ^ theta
   + eta(eta-1) theta ^ theta ||^2.
```

## Helicon persistence functional — candidate

A minimal smooth functional capable of selecting persistent profiles is

```text
E_H[eta,A]
=
integral_S3 [
  a ||F_A||^2
  + b ||D_A chi_3||^2
  + V(eta,chi_3)
] dVol_3.
```

This is a model family, not yet the recovered unique Helicon action.

## Localization question

A dark halo requires a nonuniform persistent solution

```text
eta(p) != constant
```

whose induced local S2 geometry survives perturbation and reproduces the required rotation/lensing/clustering behavior.

The mathematical problem has therefore been reduced from

```text
Does simple S3 topology hide dark matter?
```

to

```text
What stabilizes nonuniform non-radiative Helicon connection profiles on S3?
```

That is Crossroad J.
