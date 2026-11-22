# Work-Layer Atlas v135 — Sector-Relative Holonomy Visibility and the Dark Resolution Window

**Work layer:** WL-011  
**Date:** 2026-08-17  
**Status:** FINITE ALGEBRAIC WORK-LAYER THEOREM + CONSTRUCTIVE MODEL-CLASS WITNESS / NO PARENT PROMOTION

## 1. Why this move

The live project has accumulated four source-backed ingredients that have not yet been combined into one algebraic object:

1. Bandwidth Algebra retains ordered History even when two histories have the same endpoint (`BA-D4`).
2. Distinct formal corridor words may have one coarse Resolution image (`BA-T2`).
3. A formal holonomy class may be visible at some Resolutions and quotient-trivial at others (`RL9`, `RL-T3`).
4. Chirality Landscape Version 1 gives distinct local readable maps from one common formal ancestry into QFT and GR:

```text
rho_Q,p : formal/local chirality organization -> QFT_p
rho_G,p : formal/local chirality organization -> GR_p.
```

Dark Matter API 2.2 defines the physical dark-readout target by equal matter readout and unequal gravity readout.

The correct algebra-first question is therefore not "what scalar profile does dark matter have?" but:

> At which Resolutions can one nontrivial formal History/holonomy class be quotient-trivial to the matter/QFT sector while remaining nontrivial to the gravity/GR sector?

## 2. Anchored formal History pair

Use the recovered black-hole marked continuity address

```text
p_H in S3,
Sigma_H = pi^(-1)(p_H) ~= S2.
```

Let `gamma_H` be a closed admissible `S3` continuity loop based at `p_H` and let

```text
h_H := Hol_H(gamma_H)
```

be its finite History/chirality return transport.

Choose a formal local state `x` over `Sigma_H` and define

```text
x_0 := x,
x_1 := h_H . x
```

where the dot denotes the admitted action/transport of the History class on the formal local state.

Require only:

```text
h_H != id
```

in the formal History/transport algebra.

The projected endpoint may remain the same. Nontriviality resides in the retained History/holonomy, not in a changed coordinate endpoint.

## 3. Sector-relative Resolution visibility

For each modeled Resolution `R`, define sector-relative visibility of the anchored History class on `x` by readout inequality.

### QFT / matter-side visibility set

```text
Pers_Q(h_H;x)
=
{
  R in Res
  |
  rho_Q,p_H,R(x_1) != rho_Q,p_H,R(x_0)
}.
```

### GR / gravity-side visibility set

```text
Pers_G(h_H;x)
=
{
  R in Res
  |
  rho_G,p_H,R(x_1) != rho_G,p_H,R(x_0)
}.
```

These are sector-specific analogues of the Resolution Landscape persistence profile. They do not assert that QFT and GR use the same quotient or the same observable algebra.

## 4. Dark Resolution Window

Define

```text
DarkRes(h_H;x)
:=
Pers_G(h_H;x) \ Pers_Q(h_H;x).
```

Equivalently, `R` belongs to `DarkRes(h_H;x)` exactly when

```text
rho_Q,p_H,R(x_1) = rho_Q,p_H,R(x_0)
```

while

```text
rho_G,p_H,R(x_1) != rho_G,p_H,R(x_0).
```

This is the algebraic version of the current statement that **Resolution is the domain in which a dark distinction can appear**.

It does not make Resolution a material substance or identify `S3` with dark matter.

## 5. Theorem V135-T1 — Sector-relative hidden-holonomy witness

Assume:

1. `x_0` and `x_1` have common formal ancestry and differ only by an admitted nontrivial anchored History/holonomy action `h_H`;
2. the local QFT and GR readouts are defined at Resolution `R`;
3. `R in DarkRes(h_H;x)`.

Then the pair is QFT-equivalent and GR-inequivalent at that Resolution:

```text
rho_Q,p_H,R(x_0)=rho_Q,p_H,R(x_1),
rho_G,p_H,R(x_0)!=rho_G,p_H,R(x_1).
```

If the ordinary matter readout factors through the selected QFT representation and the declared gravity readout is nondegenerate on the selected GR distinction, then

```text
M_R(x_0)=M_R(x_1),
G_R(x_0)!=G_R(x_1),
```

and therefore

```text
(x_0,x_1) in D_R.
```

### Proof

The first two displayed relations follow directly from membership in `DarkRes(h_H;x)`. The downstream matter/gravity relations follow under the stated factorization/nondegeneracy hypotheses. Membership in `D_R` then follows from the parent Dark Matter API definition. QED.

### Scope

This theorem is exact as a typed implication. It does **not** prove that an actual galaxy supplies such a pair, nor that the currently open `rho_G`/intertwining map is physically complete.

## 6. Theorem V135-T2 — Dark-window characterization

By definition,

```text
DarkRes(h_H;x)
=
Pers_G(h_H;x) \ Pers_Q(h_H;x).
```

Therefore:

```text
DarkRes(h_H;x) != empty
```

if and only if there exists at least one modeled Resolution at which the selected History distinction survives the gravity/GR readout but is observationally merged by the QFT/matter readout.

This gives a Resolution-indexed classification without any scalar density profile.

## 7. Constructive finite witness

The work-layer model class is nonempty as pure algebra.

Take one local formal identity class with two History-distinct states

```text
x_0,
x_1=h.x_0,
h!=id,
h^2=id
```

for a simple `Z2`-type return transport.

Choose three ordered modeled Resolutions

```text
R_c < R_d < R_f.
```

Declare readout partitions:

### Coarse Resolution `R_c`

```text
QFT:  {x_0,x_1}
GR:   {x_0,x_1}
```

Both sectors merge the History distinction.

### Intermediate Resolution `R_d`

```text
QFT:  {x_0,x_1}
GR:   {x_0},{x_1}
```

The matter/QFT sector still identifies the states, while gravity/GR distinguishes them.

### Fine Resolution `R_f`

```text
QFT:  {x_0},{x_1}
GR:   {x_0},{x_1}
```

Both sectors distinguish the formal History.

Then

```text
Pers_Q(h;x_0) = {R_f},
Pers_G(h;x_0) = {R_d,R_f},
DarkRes(h;x_0) = {R_d}.
```

This witness satisfies the algebraic architecture and proves that a nonempty dark Resolution window is mathematically possible in the work-layer model class.

It is **not an astronomical fit** and not a parent-API dark-matter witness.

## 8. Identity versus zero firewall

The matter/QFT readout in this theorem may send the nontrivial return transport to the **identity morphism/readout equivalence class**.

Do not rewrite this automatically as additive zero.

```text
composition identity != additive zero.
```

If a later linearized representation defines a difference object and sends that difference to an additive zero, that is a separate typed representation.

## 9. Relation to Bandwidth Algebra

The witness is native to the current algebra-first method:

```text
formal Bandwidth Algebra A_B
-> formal History/corridor word h
-> Resolution presentations
-> sector-specific readout equivalence
-> dark Resolution window.
```

`BA-T2` supplies the possibility that different formal corridor words share one coarse presentation. `RL-T3` supplies Resolution-dependent holonomy visibility. Version 1 supplies separate QFT and GR readouts.

No scalar Bandwidth valuation is required.

## 10. Relation to the black-hole anchor

The theorem itself works for any admitted local continuity address.

For the galactic specialization, `p_H` and `Sigma_H` provide the recovered black-hole anchored local domain. The black-hole/Bandwidth-Algebra saturation result from WL-v127 remains an independent local admissibility constraint; it is not required for the abstract dark-window theorem.

## 11. Research consequence

The project now has three different levels of claim:

```text
A. algebraic nonemptiness:
   PROVED in the work-layer finite witness.

B. source-native galaxy realization:
   OPEN — requires one admitted rotational/S3 History class whose sector visibility profiles differ.

C. physical dark-matter admission:
   OPEN — requires downstream GR/observable comparison and conventional null-model control.
```

The next direct test should therefore compute/construct the pair

```text
Pers_Q(h_H;x), Pers_G(h_H;x)
```

for one source-admitted anchored rotational History class before returning to scalar phenomenology.

## 12. Status

**Source-backed ingredients:** BA-D4, BA-T2, RL9/RL-T3, Version 1 separate `rho_Q`/`rho_G`, parent dark-readout definition `D_R`.

**Work-layer definitions:** sector-relative visibility profiles and `DarkRes`.

**Work-layer theorem:** V135-T1/T2.

**Constructive witness:** finite three-Resolution `Z2` History model.

**Not proved:** actual galactic realization, physical GR completion, astronomy, dark-matter identity.

**Parent promotions:** 0.
