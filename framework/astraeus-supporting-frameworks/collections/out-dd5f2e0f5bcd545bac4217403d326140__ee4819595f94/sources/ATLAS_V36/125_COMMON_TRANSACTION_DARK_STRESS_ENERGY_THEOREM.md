# 125 — Common-Transaction Dark Stress-Energy Theorem

## Purpose

Atlas v15 defined dark structure as a mismatch between ordinary matter readout and gravitational readout.
V16 asks a sharper question:

> If the downstream readable chart remains ordinary General Relativity, what must differ whenever gravity differs inside one matter-readable equivalence class?

The answer is **stress-energy readout**, provided the GR boundary / initial / gauge data are held fixed.

This is a readable-layer theorem. It does not make stress-energy or metric geometry native substrate objects.

---

## 1. Source-grounded common transaction

The recovered Universal Coupling Mechanism represents one coupling event as a shared substrate transaction:

```text
persistent manifold
-> ER perturbation
-> substrate redistribution
-> R4 corridor availability
-> R5 ordered topology resolution
-> R6 survivability stabilization
-> R7 persistence verification.
```

The same recovery supplies two downstream projections of that transaction:

```text
T_mn = Pi_read(O, Chi, A, P, Rred, S, B)
```

and

```text
G_mn = Pi_grav(Delta_ER^R).
```

Here `Rred` denotes redistribution, not Resolution.

The fresh API independently records:

```text
@general_energy PROJECTS_TO @stress_energy_tensor
@energy_density ENTERS @stress_energy_tensor.
```

Thus v16 treats stress-energy and gravitational geometry as **co-readouts of one substrate transaction**, not as unrelated objects.

---

## 2. Typed readouts

Fix a declared Resolution `R` and let `X_R` be the formal state / transaction class under comparison.

Define:

```text
M_R : X_R -> MatterReadout_R
T_R : X_R -> StressEnergy_R
G_R : X_R -> GravityReadout_R.
```

`M_R` is the ordinary matter-readable channel.

`T_R` is the total readable stress-energy channel, including every contribution admitted by the declared source projection.

`G_R` is the readable gravitational geometry.

V15 defined the dark pair set

```text
D_R
=
{(x,y) | M_R(x)=M_R(y), G_R(x)!=G_R(y)}.
```

---

## 3. General readable GR input map

A stress-energy tensor does not determine a unique global metric until the physical problem also fixes the relevant boundary, initial, gauge, topology, and convention data.

Collect those non-source inputs into a typed object

```text
beta_R : X_R -> GRBoundaryData_R.
```

Write the deterministic readable solution map as

```text
Gamma : StressEnergy_R x GRBoundaryData_R -> GravityReadout_R
```

so that

```text
G_R(x) = Gamma(T_R(x), beta_R(x)).
```

This is **not** asserted as a native Time-Space law. It is the downstream GR closure after all readable problem data have been declared.

---

## 4. Theorem V16-T1 — Dark GR Input Separation

For every dark pair

```text
M_R(x)=M_R(y)
and
G_R(x)!=G_R(y),
```

at least one of the following must hold:

```text
T_R(x) != T_R(y)
```

or

```text
beta_R(x) != beta_R(y).
```

### Proof

If both

```text
T_R(x)=T_R(y)
```

and

```text
beta_R(x)=beta_R(y),
```

then the two inputs to the deterministic map `Gamma` are identical, hence

```text
G_R(x)=G_R(y),
```

contradicting the dark-pair assumption. QED.

---

## 5. Corollary V16-C1 — Fixed-boundary dark gravity requires hidden stress-energy

If the GR boundary / initial / gauge / topology data are fixed on a matter-readable fiber,

```text
M_R(x)=M_R(y)
=>
beta_R(x)=beta_R(y),
```

then every dark pair on that fiber obeys

```text
T_R(x)!=T_R(y).
```

Define

```text
D_R^T
=
{
 (x,y) in D_R
 |
 T_R(x)!=T_R(y)
}.
```

On a fixed-`beta` fiber,

```text
D_R^T = D_R.
```

Therefore **dark gravity becomes a hidden stress-energy defect only after the readable GR boundary/topology data have been controlled.**

This does not imply a new particle species. The missing readable stress-energy may be a projection of native ER / continuity / relational organization.

---

## 6. Energetic versus hidden-boundary fork

V16 therefore separates two possible downstream programs.

### Branch A — energetic / hidden-source branch

```text
M_R(x)=M_R(y)
T_R(x)!=T_R(y)
G_R(x)!=G_R(y).
```

This is compatible with ordinary GR under fixed `beta`.

The missing readable source may be a projection of native ER / continuity / relational organization rather than particles.

### Branch B — hidden boundary / topology branch

```text
M_R(x)=M_R(y)
T_R(x)=T_R(y)
beta_R(x)!=beta_R(y)
G_R(x)!=G_R(y).
```

This is still compatible with ordinary GR, but the missing information is carried by readable boundary / initial / topology data rather than by a stress-energy difference.

It is therefore mathematically distinct from Branch A.

### Branch C — changed gravity/readout law

If both `T_R` and `beta_R` are held fixed while `G_R` differs, the declared deterministic GR map has failed or changed. That would be a modified-gravity / changed-readout branch rather than an ordinary-GR dark-source explanation.

---

## 7. Physical meaning for the current dark-matter branch

The result sharpens the v15 statement:

> **Ordinary General Relativity reduces every dark readout defect to hidden GR input data. If boundary/topology data are fixed on the matter-readable fiber, the missing input must be stress-energy. The upstream carrier of that stress-energy may remain geometric, relational, ER-connected, or transduced rather than particulate.**

This is the precise mathematical opening for the user intuition that the dark sector may be native energetic organization in a representation ordinary matter readout does not preserve.

---

## Status

```text
UCM common-transaction source                        RECOVERED
General-energy -> stress-energy API edge             RECOVERED
Energy-density -> stress-energy API edge             RECOVERED
Fixed-GR-chart solution map                          DOWNSTREAM TYPING
V16 Dark GR Input Separation Theorem                 PROVED
Fixed-beta hidden stress-energy corollary              PROVED
Dark matter = particle                               NOT REQUIRED
Dark matter = energy as a substance                  NOT CLAIMED
```
