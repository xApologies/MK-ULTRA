# 124 — Atlas v15 Master Synthesis

## Main closure

V15 followed the fresh native-energy branch into gravity and found a structural result more useful than a guessed dark-energy-density formula:

> **The dark-matter sector is naturally characterized by a mismatch between typed readout equivalence relations.**

At fixed Resolution `R`, let

```text
M_R = ordinary matter-readable projection
G_R = gravitational projection.
```

The exact dark readout defect is

```text
D_R
=
{
  (x,y)
  |
  M_R(x)=M_R(y)
  and
  G_R(x)!=G_R(y)
}.
```

`D_R` is nonempty exactly when gravity does not factor through the ordinary matter readout.

This gives a precise mathematical meaning to the historical phrase

```text
dark matter = unreadable topology.
```

The topology is not absent. The ordinary matter-readable channel conflates formal states that the gravitational channel can still distinguish.

---

## Resolution / Bandwidth / chirality reconciliation

The current roles now separate cleanly:

```text
Resolution
    -> determines distinguishability within each typed readout carrier

Bandwidth
    -> determines available organizational transformations
    -> also enters the recovered persistence scalar used by native energy

chirality
    -> organizes orientation / compatibility / transport
    -> constrains ER/corridor morphology and continuity paths
```

Therefore the **darkness** of the sector is primarily a readout/Resolution statement, while chirality may still govern the geometry and transport of the hidden organization.

This resolves the earlier false choice “chirality before or after dark matter?” into typed roles rather than one forced linear ordering.

---

## Native energy correction

The fresh API contains two energy roles:

```text
E_MK(H) = [Pi(U_n)-Pi(U_0)] / epsilon_MK
```

and

```text
rho_E = Rel * Tcap / V.
```

The first is a history-relative persistence difference and vanishes on a closed history.

The second is a local energy-density role.

Thus

```text
E_MK(H_closed)=0
```

does not imply

```text
rho_E=0.
```

Persistent load-bearing ER geometry can therefore remain a candidate local energetic organization without violating the recovered closed-history law.

---

## Energy to gravity

The fresh API directly records

```text
@general_energy -> @stress_energy_tensor
@energy_density -> @stress_energy_tensor.
```

The gravity branch independently records

```text
continuity flow
-> delta C
-> nonlinear gravitational closure
-> Pi_TS^grav
-> readable metric.
```

V15 therefore imposes a downstream compatibility filter:

```text
Ein(g_Phi) = kappa T_E(x).
```

This yields

```text
Flow_EG(N)
subseteq
Flow(N),
```

the subset of native continuity flows whose readable gravity agrees with the energy/stress-energy representation of the same formal state.

This does not yet make the native constitutive flow unique, but it can reject incompatible flow realizations without fitting astronomy.

---

## Repair of the v14 reference problem

V14 used one `N_ref`.

V15 shows why that reference was not automatically canonical.

Matter readout defines a fiber

```text
F_M,R(x) = M_R^-1(M_R(x)),
```

not necessarily a unique formal state.

A pairwise v14 residual remains valid after a representative is declared:

```text
Delta g_D(x,y) = g(x)-g(y)
```

for `y` in the same matter-readable fiber.

But dark-sector existence is the representative-independent statement

```text
G_R(F_M,R(x)) is non-singleton.
```

A unique numerical dark residual requires an additional source-grounded section/selection rule.

This is now an explicit theorem-level boundary, not an unspecified gap.

---

## Current strongest candidate statement

> **Dark matter is not presently identified with a new particle, with S3 itself, with a black hole, or with chirality. The current Atlas identifies the dark phenomenon as gravitationally distinguishable structure inside an ordinary matter-readout equivalence class of persistent ER-connected Time-Space organization. When the native-energy/stress-energy representation is also nontrivial on that hidden structure, the sector is an energetic geometric load that is matter-unreadable but gravitationally readable.**

---

## Updated chain

```text
Genesis / Time-Space
-> Resolution + Bandwidth
-> persistent organization / native energy roles
-> chirality-organized ER continuity
-> conditional ER -> S3 translation
-> closure-stable BH/ER neighborhood
-> admissible Flow(N)
-> Energy-Gravity filter Flow_EG(N)
-> D_C Phi
-> nonlinear gravitational closure
-> Pi_TS^grav
-> gravitational readout G_R

parallel ordinary branch:
formal organization
-> particle/matter-readable organization
-> matter readout M_R

Dark condition:
M_R(x)=M_R(y)
but
G_R(x)!=G_R(y).
```

---

## Next physics target

Do **not** open numerical halo fitting yet.

Next recover/test:

1. the explicit native-to-stress-energy realization `T_E` for the ER/S3 dark candidate;
2. whether the energy-gravity compatibility filter reduces `Flow_EG(N_H^R)` to a unique or small class around the black-hole marked neighborhood;
3. whether a canonical reference section is recovered from existing Resolution, Bandwidth, Identity, or minimum/maximum admissibility rules;
4. only then derive a radial/filamentary gravitational profile and freeze it before astronomy comparison.
