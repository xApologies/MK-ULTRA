# 22 — S³-to-S² Helicon Transduction

## Purpose

The global Helicon section on `S3` and the local Helicon realization inside a readable `S2` spacetime are not assumed to be identical mathematical types.

## Local transduction

For each `p in S3`, let

```text
Sigma_p = pi^(-1)(p) ~= S2.
```

Define a typed transduction

```text
Tau_H,p : Germ_p(E_H, H_3) x C_p -> HLoc_p
```

where

- `Germ_p(E_H,H_3)` is the local germ of the S3 Helicon state,
- `C_p` is the local chirality/address state on `Sigma_p`,
- `HLoc_p` is the local readable Helicon mode space on the S2 projection.

Then

```text
H_p^loc = Tau_H,p(H_3, chi_p).
```

This is **transduction**, not ordinary restriction, unless a later proof identifies the types.

## Local ER realization

Define

```text
rho_ER,p : HLoc_p x C_p -> ER_p
```

with

```text
ER_p = (V_p, E_p, W_p, chi_p, rho_p, sigma_p).
```

The recovered ER-foam equation says the Time-Shell substrate is a minimal boundary-adjacency configuration preserving bulk ordering consistency. Atlas v3 therefore places the ER graph on the local S2 projection while allowing its admissibility to be controlled by the S3 Helicon state.

## Local field readouts

The local Helicon realization can feed several downstream readouts:

```text
rho_Q,p  : (chi_p,H_p^loc,ER_p,...) -> Q_p
rho_G,p  : (chi_p,H_p^loc,ER_p,...) -> GR_p
rho_M,p  : (chi_p,H_p^loc,ER_p,...) -> Matter_p
```

No equality among these codomains is assumed.

## Cross-address consistency

Given `gamma:p_alpha->p_beta`, transport then transduction should agree with transduction then appropriate local evolution:

```text
Tau_H,beta(P_gamma^H H_alpha, P_gamma^chi chi_alpha)
~=
U_HLoc(gamma) Tau_H,alpha(H_alpha,chi_alpha).
```

The equality is exact only if the required intertwining law is proved. Otherwise its defect defines a measurable/correctable transduction obstruction.

## Corridor form

Because

```text
W_gamma = gamma^*(T5) ~= S2 x I
```

on the standard branch, the corridor is the natural five-dimensional carrier through which the S3 Helicon state acquires a continuous family of local S2 realizations:

```text
{H_s^loc}_{s in I}.
```

Thus a portal/corridor is not an added tunnel. It is the S2-fibered realization of a path through the S3 continuity/Helicon domain.
