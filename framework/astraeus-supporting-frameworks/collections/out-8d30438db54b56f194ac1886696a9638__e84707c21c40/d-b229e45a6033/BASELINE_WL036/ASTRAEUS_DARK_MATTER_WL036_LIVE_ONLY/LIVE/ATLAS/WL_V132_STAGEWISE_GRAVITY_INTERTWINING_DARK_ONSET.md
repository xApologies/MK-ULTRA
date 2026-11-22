# Work-Layer Atlas v132 — Stagewise Gravity Intertwining Reduction and Dark-Onset Localization

**Work layer:** WL-008  
**Date:** 2026-08-17  
**Status:** SOURCE-COMPOSED / EXTERNAL-MATH REDUCTION LEMMA — NOT PARENT PROMOTED  
**Parent promotions:** 0

## Trigger

WL-v130 identified the global gravity-sector intertwining target

`rho_G,beta o P_gamma^chi = U_G(gamma) o rho_G,alpha`

but left it as one large untyped obligation. WL-v131 sharpened the nontrivial dark candidate to horizontal `S3` connection/holonomy rather than bare bundle topology under ordinary bundle hypotheses.

The next task is to reduce the global gravity intertwining problem into auditable local stages using the already recovered gravity pipeline.

## 1. Source-backed gravity pipeline

Use the recovered ordered route:

`chirality`
`-> ER foam`
`-> Helicon`
`-> gravitational Helicon mode`
`-> Graviton`
`-> continuity perturbation`
`-> Time-Shell projection`
`-> h_mn`
`-> g_mn`
`-> curvature / GR`.

This route is source-backed as an ordered dependency/realization path. The individual arrows have different proof/typing maturity and are not collapsed into one pre-proved theorem.

## 2. Stage objects and vertical maps

For a localized fiber/address `alpha`, define stage objects:

`X_0^alpha = chi_alpha`
`X_1^alpha = ER_alpha`
`X_2^alpha = Helicon_alpha`
`X_3^alpha = H_g,alpha`
`X_4^alpha = Graviton_alpha`
`X_5^alpha = deltaC_alpha`
`X_6^alpha = TSProj_alpha`
`X_7^alpha = h_alpha`
`X_8^alpha = g_alpha`
`X_9^alpha = Curv_alpha`.

Let

`v_i^alpha : X_i^alpha -> X_(i+1)^alpha`

be the corresponding local vertical realization map whenever typed.

Then the local gravity readout is the composite candidate

`rho_G,alpha = v_8^alpha o ... o v_1^alpha o v_0^alpha`.

This equation is a work-layer factorization of the recovered route; it does not claim every `v_i` is already source-complete.

## 3. Horizontal transports

For an `S3` continuity path `gamma:alpha->beta`, let

`U_i(gamma):X_i^alpha->X_i^beta`

be the horizontal transport induced in stage `i`.

At the chirality stage:

`U_0(gamma)=P_gamma^chi`.

At the final GR stage:

`U_9(gamma)=U_G(gamma)`.

The missing physics/mathematics is therefore distributed across the induced `U_i` rather than hidden inside one opaque global operator.

## 4. Stagewise intertwining condition

For each `i=0,...,8`, require the square

`U_(i+1)(gamma) o v_i^alpha = v_i^beta o U_i(gamma)`.

Diagrammatically:

`X_i^alpha --v_i^alpha--> X_(i+1)^alpha`
`   | U_i                    | U_(i+1)`
`   v                        v`
`X_i^beta  --v_i^beta-->  X_(i+1)^beta`.

## 5. Reduction lemma

**External established mathematics / categorical composition.**

If every admitted stage square commutes, then the complete composite square commutes:

`U_G(gamma) o rho_G,alpha = rho_G,beta o P_gamma^chi`.

Equivalently:

`rho_G,beta o P_gamma^chi = U_G(gamma) o rho_G,alpha`.

Proof is by repeated substitution/composition of the stagewise commuting relations.

### Consequence

The global intertwining obligation is reduced from one monolithic proof target to a finite sequence of local equivariance/naturality tests.

A single failed stage identifies exactly where the proposed common-continuity realization breaks.

## 6. Dark-onset index

Let `F0,F1` be a controlled formal pair satisfying the fixed localized matter/QFT condition at Resolution `R`:

`rho_Q,p,R(F0)=rho_Q,p,R(F1)`.

Let `r_i(F)` be the induced state/readout of `F` at gravity stage `i`.

Define the first gravity-separation stage, when it exists:

`k_* = min { i | r_i(F0) != r_i(F1) }`.

Interpretation:

- no `k_*`: the selected hidden History does not enter the recovered gravity route for this model;
- `k_*=2`: separation first becomes readable in Helicon organization;
- later `k_*`: the distinction survives upstream but becomes gravity-readable only at a later transduction stage;
- a separation before a properly typed gravity-specific stage must not be mislabeled as a physical gravity effect.

This gives the dark-matter project a localization diagnostic instead of a scalar fit-first strategy.

## 7. Holonomy specialization

Use the WL-v131 controlled pair:

`F0: Hol_H(gamma_H)=id`
`F1: Hol_H(gamma_H)!=id`

for a closed loop based at the black-hole continuity address `p_H`.

At stage 0 this is a chirality/continuity transport distinction. The research question becomes:

**At which gravity stage, if any, does the nontrivial horizontal return transport first survive as a distinct stage object?**

This is the operational meaning of locating where the hidden `S3` History becomes a gravitational readout.

## 8. Helicon as the first priority stage

The source recovers within Helicon:

- rotational modes `H^(k)=R^kH`;
- helicon curvature;
- resonance against a rotational frame field;
- curvature binding;
- manifold shear and shear compensation;
- coherent helicon propagation;
- downstream substrate-bias / orientation restructuring / continuity redistribution before gravitational Helicon mode and Graviton.

Therefore `i=2` (Helicon) is the first **priority audit stage**, not a presumed answer.

The concrete source question is whether horizontal chirality return transport induces a well-defined Helicon-stage automorphism

`U_2(gamma):Helicon_alpha->Helicon_beta`

that is compatible with the local chirality-to-ER-to-Helicon maps.

If no such map can be typed, the current rotational dark branch fails before the GR sector.

## 9. Frame-dragging placement

Frame dragging should not be inserted at the beginning of the chain.

Candidate placement:

`nontrivial horizontal holonomy`
`-> first gravity-stage separation k_*`
`-> continuity perturbation / Time-Shell metric projection`
`-> local frame transport`
`-> accepted rotating-spacetime observable`.

Thus frame dragging becomes a late readable consequence of a successfully transported rotational/continuity distinction.

## 10. Relation to S4 closure candidate

The candidate `S4_cl=Susp(S3)` from WL-v131 remains a coarse continuity-closure representation. The stagewise gravity route lives in the local `S2` physical/readout side of `T5` and is not replaced by `S4_cl`.

A separate compatibility question remains: whether the horizontal distinction responsible for `k_*` survives or is identified by the `S4_cl` closure/readout.

## 11. New protocol

Protocol `AST-DM-WL-P005` audits the nine stage squares, locates `k_*`, and only then attempts frame/GR observable mapping.

## 12. Status

**Source-backed:** gravity route, Version 1 intertwining target, Helicon rotational/shear structures.

**External established mathematics:** stagewise commutation implies composite commutation.

**Work-layer candidate:** stage objects/maps as a common audit factorization, dark-onset index `k_*`, Helicon-first audit priority.

**Parent promotions:** 0.
