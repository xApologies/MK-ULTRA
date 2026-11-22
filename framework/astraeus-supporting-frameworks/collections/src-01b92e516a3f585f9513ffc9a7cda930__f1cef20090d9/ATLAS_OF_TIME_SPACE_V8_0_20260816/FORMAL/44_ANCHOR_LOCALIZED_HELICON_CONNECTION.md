# 42 — Anchor-Localized Helicon Connection on S³

## Status

`CURRENT_CANDIDATE LOCALIZATION MECHANISM`.

This file answers v4 Crossroad J with a smooth mechanism. It is sufficient to localize hidden Helicon curvature on the minimal `S3 x S2` carrier; it is not yet asserted to be the unique physical mechanism.

## Anchor set

Let

```text
A = { (p_a,q_a) }
```

be a finite or locally finite set of distinguished continuity addresses on `S3`. In the current galaxy interpretation, `p_a` may be associated with a localized `S2`/black-hole anchor address. The mathematics only requires an anchor datum; the physical origin remains separately typed.

## Smooth localization field

Let `eta:S3->R` solve the screened elliptic equation

```text
(-Delta_3 + mu_H^2) eta
=
sum_a q_a K_sigma(d_3(p,p_a)),
```

where

- `Delta_3` is the Laplace-Beltrami operator of the admitted `S3` metric;
- `mu_H >= 0` is a localization scale;
- `K_sigma` is a smooth normalized anchor kernel;
- `d_3` is geodesic distance on `S3`.

For `mu_H>0` the compact-base zero-mode obstruction is removed and the solution is unique under standard elliptic hypotheses.

## Round-S³ radial profile

For one ideal point anchor on a round `S3` of radius `R3`, away from the source a radial profile `eta(theta)` satisfies

```text
eta'' + 2 cot(theta) eta' - (mu_H R3)^2 eta = 0.
```

With `kappa=sqrt((mu_H R3)^2-1)` on the hyperbolic branch, the Green-profile shape is proportional to

```text
G_mu(theta)
propto
sinh[kappa(pi-theta)]
/
[ sin(theta) sinh(kappa pi) ].
```

A smooth `K_sigma` regularizes the source pole.

## Nonhomogeneous Helicon connection

Use the `S3 ~= SU(2)` test connection but allow its amplitude to vary:

```text
A_H = k(p) theta,
k(p)=k_0 + alpha eta(p).
```

Then

```text
F_H
=
dk ^ theta
+
k(k-1) theta ^ theta.
```

This is the crucial v5 result:

```text
nonuniform anchor data
 -> nonuniform connection amplitude
 -> localized Helicon curvature
```

on the same smooth topologically trivial Time-Space carrier.

## Why this resolves the v4 no-go

The v4 no-go assumed a homogeneous connection and address-independent readout. Here `dk != 0` near localized anchor profiles, so the hypothesis of that theorem is explicitly broken without invoking exotic topology or singular Time-Space.
