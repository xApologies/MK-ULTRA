# Work-Layer Atlas v130 — T5 / S2-Fiber / S3-Continuity Rebind and QFT–GR Readout Bridge

**Work layer:** WL-006  
**Date:** 2026-08-17  
**Status:** SOURCE-MATCHED REBIND / DARK-MATTER INTEGRATION CANDIDATE — NOT PARENT PROMOTED  
**Parent promotions:** 0

## Trigger

Genesis supplied the recovered chirality-landscape/QFT–GR bridge packages and clarified the intended organizational picture:

- localized `S2` projections are readable physical domains;
- `S3` supplies structural continuity among those localized projections;
- the total Time-Space organization supplies the coherent global context;
- the relationship should be fluid/continuous rather than a collection of independent objects.

The supplied Version 1 bridge resolves an important notation drift and gives a direct formal source for this architecture.

## 1. Source-authoritative Version 1 geometry

The recovered Version 1 release declares the operative geometry:

`S2 --> T5 --pi--> S3`

with

`Sigma_p := pi^(-1)(p) ~= S2`, for `p in S3`.

Source roles:

- `T5` = five-dimensional universe / Time-Space;
- `S3` = continuity domain relating localized spacetime projections;
- `Sigma_p ~= S2` = localized readable spacetime projection;
- QFT, GR, ER foam, and local chirality readout operate inside a selected `S2` fiber;
- chirality also transports horizontally through `S3`.

Dimensional bookkeeping is source-explicit:

`dim(T5) = dim(S3) + dim(S2) = 3 + 2 = 5`.

## 2. Supersession firewall

Version 1 explicitly supersedes the older chirality-landscape assignment:

`S4 = universe / Time-Space`

in favor of:

`T5 = universe / Time-Space`
`S2 fibers = localized spacetime projections`
`S3 base = continuity domain among S2 projections`.

This does **not** rewrite the separate parent Dark Matter Live 0.14.0 / Atlas v125 branch, whose recovered candidate geometry uses `S4 -> S3 -> S2` language. The two source branches retain provenance until a typed reconciliation is completed.

Therefore current work-layer rule:

- do not call the total five-dimensional Time-Space object `S4` inside the Version 1 bridge branch;
- if an `S4` object is reintroduced, give it a new explicit role (for example a closure/admissibility object) rather than silently restoring the superseded identity.

## 3. Local physical domain

For one localized projection `Sigma_p ~= S2`, Version 1 places:

`QFT_p`
`GR_p`
`ER_p`
`chi_p`.

Global chirality is represented by

`pi_chi : E_chi -> T5`
`chi in Gamma(E_chi)`.

Local chirality is the restriction/pullback

`chi_p := i_p^*(chi)`.

The local representation maps are

`rho_Q,p  : chi_p -> QFT_p`
`rho_G,p  : chi_p -> GR_p`
`rho_ER,p : chi_p -> ER_p`.

Thus the local QFT/GR bridge is not an inverse identification. It is common ancestry:

`QFT_p <- chi_p -> GR_p`.

## 4. Global common-fabric bridge

The formal bridge package defines a global chirality/admissibility realization

`Fabr_chi = [G_chi]_G`

and operative state

`F = Op(Fabr_chi; B,R,H)`.

Separate readout maps are introduced:

`rho_Q : F -> Q_QFT`
`rho_G : F -> Q_GR`.

The common-ancestry relation is

`R_QG = { (q,g) | exists F: q=rho_Q(F), g=rho_G(F) }`.

This is a strong fit to the dark-matter readout strategy: matter/QFT and gravity/GR may differ as readable representations while retaining one formal ancestry.

## 5. S3 continuity generates corridor geometry

For a path

`gamma : [0,1] -> S3`

between localized projection addresses, pull back the total Time-Space fibration:

`W_gamma := gamma^*(T5)`.

In the locally trivial case:

`W_gamma ~= S2 x [0,1]`

and

`boundary(W_gamma) = Sigma_alpha union (-Sigma_beta)`.

Therefore the previously recovered Chirality Corridor is not an externally inserted tunnel in this branch. It is the restriction of five-dimensional Time-Space to an admissible `S3` continuity path.

This directly supports the geometry-first dark-matter self-corridor work while giving it a global carrier source.

## 6. Horizontal versus local organization

Version 1 proposes the connection split

`nabla^chi = nabla_V^chi + nabla_H^chi`

where:

- vertical/local organization acts within an `S2` fiber;
- horizontal continuity transports chirality among fibers along `S3`.

The exact connection typing remains open, but the role separation is source-explicit.

For the current dark-matter branch, this suggests:

- localized galaxy/readout structure is fiber-local;
- hidden persistent History/corridor organization may live in the horizontal `S3` transport sector;
- the dark question is whether two global/history states can be locally matter-equivalent while locally gravity-inequivalent after the corresponding readout.

## 7. Sharpened dark readout condition

Let `F0,F1` be two operative states of one formal fabric with differing `S3` History/holonomy organization.

At a selected localized `S2` fiber and Resolution `R`, require first:

`rho_Q,p,R(F0) = rho_Q,p,R(F1)`

or, when an additive difference object is typed,

`DeltaF in ker(rho_Q,p,R)`.

Then test whether

`rho_G,p,R(F0) != rho_G,p,R(F1)`

or

`DeltaF notin ker(rho_G,p,R)`.

This is the QFT/GR representation version of the existing matter-null / gravity-non-null dark condition.

It is not yet a physical dark-matter proof. It is a stronger native bridge target because the two readouts now descend from one recovered formal fabric object.

## 8. Global intertwining target

For formal corridor transport

`P_W^chi : F_a -> F_b`

and readable sector transport `U_s(W)`, the source proposes

`rho_s o P_W^chi = U_s(W) o rho_s`.

Locally along `gamma`:

`rho_s,beta o P_gamma^chi = U_s(gamma) o rho_s,alpha`.

This is now a high-priority dark-matter bridge obligation. If the diagram can be typed for the gravity sector while a selected matter readout quotients out the same History distinction, the project obtains a direct formal path from hidden continuity to differential gravitational readout.

## 9. Home Improvement analogy — controlled translation

Genesis's analogy is useful if kept role-based:

- **Tim / local side** = a localized `S2` readable projection;
- **fence** = the `S3` relational/continuity interface through which localized projections remain structurally connected without becoming identical;
- **Wilson / larger context** = the global Time-Space organization that is not exhausted by one local readout.

The analogy should not be read as three independent substances. The source geometry is a fibration/continuity structure: localized fibers are distinct but continuously organized by one total object.

## 10. Relation to current rotational/shear branch

The v128-v129 work remains compatible after rebinding:

`localized S2 galaxy`
`-> nontrivial rotational self-History / holonomy`
`-> S3 continuity/corridor organization`
`-> cross-Resolution algebraic section`
`-> local Time-Shell / frame readout`
`-> QFT/GR representation test`.

The new source package makes the last step substantially cleaner because QFT and GR are already typed as distinct local representations of one chirality/fabric ancestry.

## 11. New integration target

Construct and test a sector-specific commuting square:

`F_alpha --P_gamma^chi--> F_beta`
` | rho_G,alpha            | rho_G,beta`
` v                        v`
`GR_alpha --U_G(gamma)--> GR_beta`

while allowing a selected matter/QFT quotient to identify the corresponding formal states at Resolution `R`.

This becomes protocol `AST-DM-WL-P003`.

## 12. Status

Source-matched:

- `S2 -> T5 -> S3` Version 1 geometry;
- `S2` local QFT/GR/ER/chirality placement;
- `S3` corridor pullback `W_gamma ~= S2 x I`;
- common-fabric QFT/GR representation relation;
- universal intertwining candidate as an open typing target.

Work-layer candidate:

- use hidden `S3` History/holonomy as the formal distinction quotiented out by matter but retained by gravity;
- integrate this with rotational shear, black-hole anchor, Bandwidth Algebra, and Time-Shell frame transport.

Open:

- reconcile parent Dark Matter `S4 -> S3 -> S2` terminology with Version 1 `S2 -> T5 -> S3` without deleting either provenance branch;
- type `rho_Q,p,R` and `rho_G,p,R` sufficiently for a dark readout theorem;
- type the gravity intertwining map and downstream observable;
- determine whether an `S4` closure object remains useful under a new, non-universe role.

**Parent promotions:** 0.
