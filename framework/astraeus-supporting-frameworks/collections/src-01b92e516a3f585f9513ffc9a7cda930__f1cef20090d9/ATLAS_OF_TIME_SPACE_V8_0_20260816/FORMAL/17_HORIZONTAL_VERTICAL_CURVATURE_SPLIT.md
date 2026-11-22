# 17 — Horizontal / Vertical Curvature Split

## Purpose

Make the statement “chirality operates locally on S2 and continuously across S3” mathematically explicit.

---

## 17.1 Adapted coordinates

On a local product chart:

```text
pi^(-1)(U) ~= U x S2,
```

use:

```text
y^a  = coordinates/directions on the S3 continuity base,
z^i  = coordinates/directions on the localized S2 fiber.
```

A local chirality connection can be decomposed as:

```text
A_chi = A_H + A_V
      = A_a dy^a + A_i dz^i.
```

This decomposition is chart-dependent in components but geometrically represents the chosen horizontal/vertical splitting.

---

## 17.2 Curvature blocks

The chirality curvature decomposes into:

```text
F_chi = F_HH + F_HV + F_VV.
```

where:

```text
F_HH : horizontal-horizontal curvature
F_HV : horizontal-vertical mixed curvature
F_VV : vertical-vertical curvature.
```

In local differential notation:

```text
F_ab = d_a A_b - d_b A_a + [A_a,A_b]
F_ai = d_a A_i - d_i A_a + [A_a,A_i]
F_ij = d_i A_j - d_j A_i + [A_i,A_j].
```

---

## 17.3 Atlas interpretation

### `F_VV` — local S2 organization

Candidate carrier for chirality curvature intrinsic to a localized readable spacetime projection. This is the natural location to compare with local QFT/gauge/ER-foam/GR representation data.

### `F_HH` — inter-projection continuity curvature

Measures path dependence accumulated entirely through the `S3` continuity directions.

### `F_HV` — local/global coupling curvature

Measures the failure of local `S2` chirality organization and `S3` transport to commute.

Invariantly, for horizontal `X` and vertical `Y`:

```text
F_chi(X,Y)
=
[nabla_X^chi,nabla_Y^chi]
-
nabla_[X,Y]^chi.
```

This is the first exact Atlas object that measures how local readable physics can depend on transport through the global continuity structure.

---

## 17.4 Mixed-curvature consistency condition

If:

```text
F_HV = 0
```

on a region, then horizontal transport and vertical chirality evolution commute locally (subject to standard domain conditions).

This gives the candidate “uniform local law” condition:

```text
transport between S2 projections
commutes with
local S2 chirality dynamics.
```

If `F_HV != 0`, the local representation can acquire path/history dependence under global transport.

---

## 17.5 Relation to the QFT/GR intertwining target

Define downstream defects:

```text
D_Q(gamma)
:=
rho_Q,beta o P_gamma^chi
-
U_Q(gamma) o rho_Q,alpha
```

and:

```text
D_G(gamma)
:=
rho_G,beta o P_gamma^chi
-
U_G(gamma) o rho_G,alpha.
```

Atlas v2.0 does not identify these directly with `F_HV`, but `F_HV` is the natural upstream obstruction candidate to exact sector intertwining.

This creates a concrete future test:

```text
F_HV = 0  ?=>  D_Q = D_G = 0
```

under fully typed representation maps.

---

## Status

**MAJOR NEW CARTOGRAPHIC STRUCTURE — v2.0**

This split is ordinary connection geometry applied to the Atlas architecture. The physical assignment of each block remains an MK43 interpretation to be tested against the API realization maps.
