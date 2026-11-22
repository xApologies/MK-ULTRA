# 134 — Native Containment Measure

## Purpose

The native API energy-density equation requires `Containment Volume`, but Time-Space should not silently import ordinary Euclidean volume at the substrate level.

Project language already gives the required semantics:

```text
Boundary = separator + address + containment context + relationship-enabling interface
Occupancy = allocation + localization = state-in-boundary.
```

V17 therefore types containment first and permits ordinary physical volume only as a downstream calibrated realization.

---

## 1. Resolution-qualified containment cells

At Resolution `R`, let

```text
C_R
```

be the set of distinguishable contained addresses in the selected boundary / domain.

A native containment measure is a map

```text
nu_R : P_fin(C_R) -> R_nonnegative
```

on finite distinguishable regions, with:

```text
nu_R(empty)=0
nu_R(A)>0 for nonempty elementary cells
finite additivity on disjoint contained regions
admissible-isomorphism invariance.
```

The containment volume of region `N` is

```text
V_R(N):=nu_R(C_R(N)).
```

---

## 2. Normalized cell realization

For a finite discrete substrate model one may choose native cell units

```text
nu_R({i})=1.
```

Then

```text
V_R(N)=|C_R(N)|.
```

This is a normalized **containment count**, not a claim that one cell equals one cubic meter.

A later calibration map may supply

```text
Cal_V^R : V_R -> PhysicalVolume
```

when a downstream readable spatial geometry exists.

---

## 3. Resolution dependence

Containment is Resolution-qualified.

If `R2` distinguishes a refinement of `R1`, there is a forgetting/coarsening map

```text
q_21 : C_R2 -> C_R1.
```

No equality

```text
V_R2 = V_R1
```

is assumed in native units.

Physical volume agreement, where appropriate, is a requirement on the later calibration maps, not on raw address counts.

---

## 4. Local relational energy density

Using Formal 133, for an elementary containment region `i`:

```text
rho_E^R(i)
=
[
  SUM_j r_ij t_ij
]
/
nu_R(i).
```

For a finite region `N`:

```text
E_rel,R(N)
=
SUM_(e in E(N)) r_e t_e
```

and

```text
rho_bar_E^R(N)
=
E_rel,R(N)/V_R(N).
```

Again, this is a native relational-transition density prior to physical-unit calibration.

---

## 5. Theorem V17-T4 — Volume-weighted union law

For disjoint contained regions `A` and `B`, assume the regional energy ledger counts cross-boundary relations separately rather than double-counting them inside both region energies.

Then

```text
V_R(A union B)=V_R(A)+V_R(B)
```

and, when no cross-boundary energy term is assigned to the interior total,

```text
E_R(A union B)=E_R(A)+E_R(B).
```

Therefore

```text
rho_bar(A union B)
=
[
 V_A rho_bar(A)
 +
 V_B rho_bar(B)
]
/
(V_A+V_B).
```

QED.

The cross-boundary bookkeeping convention must be declared for coupled regions.

---

## 6. Theorem V17-T5 — Finite-resolution boundedness

Suppose at fixed Resolution `R`:

```text
deg(i) <= d_max
0 <= r_ij <= r_max
0 <= t_ij <= t_max
nu_R(i) >= nu_min > 0.
```

Then

```text
rho_E^R(i)
<=
d_max * r_max * t_max / nu_min.
```

### Proof

At most `d_max` incident channels contribute; each contribution is at most `r_max*t_max`; divide by the positive lower containment measure. QED.

This is a finite native boundedness result. It does not imply that all continuum projections are bounded without additional assumptions.

---

## 7. Black-hole significance

A black-hole saturation region may have extreme relationship weight / geometric stress while particular transition channels lose capacity.

Formal 133 shows

```text
strong Rel
+
Tcap=0
->
zero contribution from that transition channel.
```

Formal 134 adds that no point divergence is forced at finite Resolution when the local relationship degree, weights, capacities, and inverse containment measure remain bounded.

This supports a geometry-first treatment of saturation without inserting infinite native density by definition.

---

## Status

```text
Boundary as containment context                          RECOVERED
Occupancy as state-in-boundary                           RECOVERED
Native containment measure nu_R                         V17 TYPED
Normalized address-count realization                    V17 CANDIDATE
Physical-volume calibration                             OPEN
Volume-weighted union theorem                           PROVED WITH BOOKKEEPING CONDITION
Finite-resolution boundedness theorem                   PROVED
Continuum-limit boundedness                             NOT CLAIMED
```
