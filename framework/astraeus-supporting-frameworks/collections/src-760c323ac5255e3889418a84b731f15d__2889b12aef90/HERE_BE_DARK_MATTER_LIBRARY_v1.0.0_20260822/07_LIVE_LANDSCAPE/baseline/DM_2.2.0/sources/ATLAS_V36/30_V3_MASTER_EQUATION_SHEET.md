# 30 — Atlas v3 Master Equation Sheet

## Time-Space

```text
S2 -> T5 -> S3
T5_std ~= S3 x S2.
```

## Chirality

```text
chi_3 in Gamma(E_chi3 -> S3)
chi_p = local S2 chirality readout.
```

## Helicon domain candidate

```text
E_H -> S3
H_3 in Gamma_adm(E_H)
nabla^H_(gamma_dot) H = 0
P_gamma^H : H_alpha -> H_beta.
```

## S3-to-S2 transduction

```text
H_p^loc = Tau_H,p(H_3,chi_p).
```

## Local ER foam

```text
ER_p[n]=(V_p[n],E_p[n],W_p[n],chi_p[n],rho_p[n],sigma_p[n])
w_ij[n]=a_ij[n] wbar_ij[n].
```

## Transient edge update

```text
a_ij[n+1]
=
Clip_[0,1](a_ij[n]
+Gamma_ij^+(1-a_ij[n])
-Gamma_ij^- a_ij[n]
+R_ij[n]).
```

## Persistent coarse-grained load

```text
Abar_ij^(N)=(1/N) sum_n a_ij[n]
Abar_ij^(N) -> E[a_ij]
```

under stationary ergodic hypotheses.

## Helicon split

```text
H_3 = H_D + delta H_R.
```

Candidate branches:

```text
H_D -> persistent ER/geometry load -> dark-sector curvature

delta H_R -> H_g -> graviton -> continuity perturbation -> h_mn.
```

## Dark sector criterion

```text
D_H,p = Ker(rho_vis,p) intersect (H_p^loc \ Ker(rho_G,p)).
```

## Local Einstein closure

```text
G_mn[g_p]
=
8*pi*G(T_mn^vis[p]+T_mn^H[p]).
```

## Bianchi/source exchange

```text
nabla^m(T_mn^vis+T_mn^H)=0

nabla^m T_mn^vis = J_n^H
nabla^m T_mn^H   = -J_n^H.
```

## Historical local effective dark chart candidate

```text
R_dark,p(H_D) = (B_p,phi_p,ER_p,L_p,...).
```

No identity among `B`, `phi`, `ER`, and `H_D` is assumed.
