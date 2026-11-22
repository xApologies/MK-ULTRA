# 11 — Master Equation Sheet

## Time-Space projection architecture

```text
pi : T5 -> S3
Sigma_p = pi^(-1)(p) ~= S2
```

## Global and local chirality

```text
pi_chi : E_chi -> T5
chi in Gamma(E_chi)
chi_p = i_p^*(chi)
```

## Tangent/connection split

```text
V = ker(d pi)
T(T5) = V direct_sum H
nabla^chi = nabla_V^chi + nabla_H^chi
```

## Local readouts

```text
Phi_p = rho_Q,p(chi_p)
g_p   = rho_G,p(chi_p)
ER_p  = rho_ER,p(chi_p)
```

## Local QFT/GR relation

```text
R_QG,p = {(q,g) | exists c: q=rho_Q,p(c), g=rho_G,p(c)}
```

## Einstein compatibility target

```text
G_mn[rho_G,p(chi_p)]
=
8 pi G T_mn[rho_Q,p(chi_p),rho_G,p(chi_p)]
```

## Continuity path and corridor

```text
gamma : I -> S3
W_gamma = gamma^*(T5)
W_gamma ~= S2 x I     [locally trivial bundle along gamma]
boundary(W_gamma) = Sigma_alpha union (-Sigma_beta)
```

## Chirality transport

```text
P_gamma^chi : chi_alpha -> chi_beta
```

## Portal factorization

```text
C_alpha_beta = Pi_beta o P_gamma^chi o L_alpha
```

## Representation intertwining

```text
rho_s,beta o P_gamma^chi
=
U_s(gamma) o rho_s,alpha
```

## Local energy balance

```text
dE_D/dt = P_in - P_out + P_source
```
