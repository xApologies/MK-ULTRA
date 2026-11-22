# 40 — Atlas v4 Master Equation Sheet

## Five-dimensional carrier

```text
S2 -> T5_std -> S3,
T5_std ~= S3 x S2.
```

## S3 Helicon connection

```text
A_H in Omega^1(S3, g_H)
F_H = dA_H + A_H ^ A_H.
```

## Canonical SU(2) test

```text
theta = g^(-1) dg
d theta + theta ^ theta = 0
A_k = k theta
F_k = k(k-1) theta ^ theta.
```

## Variable localization ansatz

```text
A_eta = eta theta
F_eta = d eta ^ theta + eta(eta-1) theta ^ theta.
```

## Corridor transport

```text
P_gamma^H = P exp(-integral_gamma A_H)
Hol_H(ell) = P_ell^H.
```

## Connection invariants

```text
I2(p) = <F_H,F_H>_p
```

```text
CS[A_H]
= (1/8 pi^2) integral_S3 tr(A_H ^ dA_H + (2/3)A_H^3) mod Z.
```

For `A_k=k theta`:

```text
CS[A_k] = N(2k^3 - 3k^2) mod Z
```

up to orientation/trace convention.

## Local Helicon transduction

```text
H_p^loc = Tau_H,p(Germ_p(H_3),chi_p).
```

## Local ER realization

```text
ER_p[n] = rho_ER,p(H_p^loc,chi_p,...).
```

## Transient incidence

```text
w_ij[n] = a_ij[n] wbar_ij[n]
0 -> active -> 0.
```

## Persistent coarse load

```text
Wbar_ij^(N) = (1/N) sum_n w_ij[n]
L_p = sum_(i,j) E[w_ij] K_ij.
```

## Primary dark geometric readout

```text
Delta g_H,p = G_H,p(I_H(p)).
```

```text
g_full,p = g_vis,p + Delta g_H,p.
```

## Apparent dark source

```text
T_mn^app,H
=
(1/8 pi G)
[
G_mn(g_full)-G_mn(g_vis)
].
```

## Local QFT/GR common ancestry

```text
Q_p = rho_Q,p(chi_p,H_p^loc,ER_p,...)
g_p = rho_G,p(chi_p,H_p^loc,ER_p,...).
```

## Global intertwining targets

```text
Tau_H,beta(P_gamma^H H, P_gamma^chi chi)
~= U_HLoc(gamma) Tau_H,alpha(H,chi).
```

## v4 hard result

```text
homogeneous A_H
+ equivariant local readout
=> no localized halo profile.
```

Therefore the next target is a stable nonuniform S3 Helicon/chirality profile.
