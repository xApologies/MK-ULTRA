# 116 — Native Continuity Source Recovery

## Purpose

Close the **type** of the v13 bottleneck

```text
R_cont(H;R) -> delta C_H
```

without inventing a dark-matter density, particle source, halo profile, or new coupling constant.

The key recovery is that Phase III already defines native continuity redistribution on the admissibility graph.

---

## 1. Recovered native continuity dynamics

For substrate states `s_i`, continuity flow `Phi_ij` exists only on admissible relations.

```text
A(s_i,s_j,rho_ij) > 0
```

The recovered local redistribution law is

```text
Delta C(s_i)
=
sum_{s_j in N(s_i)} Phi_ji
-
sum_{s_j in N(s_i)} Phi_ij.
```

For a closed region `U`, the recovered conservation law is

```text
sum_{s_i in U} Delta C(s_i) = 0.
```

Thus the native continuity perturbation is not fundamentally a continuum density derivative. It is a finite **incoming-minus-outgoing flow imbalance on admissible relations**.

---

## 2. Finite continuity-divergence operator

Define the native finite operator

```text
(D_C Phi)(i)
:=
sum_j Phi_ji - sum_j Phi_ij.
```

Then

```text
Delta C = D_C Phi.
```

`D_C` is only notation for the already-recovered Phase III rule. It does not add a new physical law.

For a selected finite region `U`, internal edge terms cancel pairwise, giving the boundary-flux identity

```text
sum_{i in U} (D_C Phi)(i)
=
sum_{i in U, j notin U} (Phi_ji - Phi_ij).
```

Hence continuity redistribution can be locally nonzero while closed-region continuity remains conserved.

---

## 3. Application to the translated black-hole neighborhood

Let

```text
N_H^R
```

be the closure-stable marked continuity neighborhood recovered in v13 from the black-hole marked star after the conditional `Theta_ER->S3` translation.

Let

```text
Flow(N_H^R)
```

be the set of continuity-flow realizations supported on its admissible relations and compatible with its existing decorations:

```text
chirality / orientation
Identity / History
Bandwidth
Resolution
black-hole invariant I_BH
corridor admissibility
closure.
```

Each admissible realization `Phi` induces

```text
delta C_Phi = D_C Phi.
```

Therefore the source-independent **typed** map is naturally set-valued until a constitutive flow-selection law is recovered:

```text
S_C(R_cont(H;R))
=
{
  D_C Phi
  |
  Phi in Flow(N_H^R)
}.
```

This is the strongest source-grounded statement presently justified.

---

## 4. What v14 closes

The v13 placeholder

```text
R_cont -> delta C
```

is no longer an untyped mystery.

It factors as

```text
closure-stable translated continuity organization
        ->
admissible continuity-flow realization
        ->
finite incoming/outgoing imbalance D_C
        ->
native continuity perturbation.
```

---

## 5. What remains open

The archive does **not** yet uniquely determine

```text
R_cont(H;R) -> Phi_H.
```

So v14 does not invent one.

Open constitutive problem:

```text
Which admissible flow realization is physically selected,
and what fixes its magnitude?
```

Possible recovered constraints include maximal admissibility continuity efficiency, edge tension, continuity strength, chirality compatibility, Bandwidth, and black-hole saturation, but no unique combined law is promoted here.

---

## Status

```text
Continuity perturbation type                 RECOVERED
Finite redistribution operator D_C           RECOVERED / RE-NOTATED
R_cont -> admissible flow class              V14 TYPED CANDIDATE
Unique R_cont -> Phi constitutive law         OPEN
No new dark source scalar                    PASS
No native calculus                           PASS
```
