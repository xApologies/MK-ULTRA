# R46 — FIRST CONCRETE LOCALIZED STATE-FAMILY CRAWL

## Verdict

R45 asked for one actual localized state instance/state object rather than a generic symbolic p.

The Unified API contains the first sufficiently concrete state-family object:

`@dm_hidden_state_bundle`

with:

`pi_H:E_H^R -> T_H`

and fiber state:

`R_H(t)=(V_t,E_t,w_t,chi_t,H_t)_R`.

This is substantially more concrete than symbolic `p`: it explicitly carries vertices, relationships, weights, chirality and History at an indexed state.

It depends on the source's hidden S3 continuity network:

`G_H^R=(V_H,E_H,w)`,

with the source explicitly retaining active geometry `S4 -> S3 -> S2`.

## Source-backed evaluators now available

### Bandwidth / supportability

The source gives:

`T_run(e)=sup_{Phi in F_run(G_*)} Phi(e)`,

the maximum globally feasible continuity flow supported by an already-persistent relationship under active Time-Space constraints.

It also gives a local bound:

`U_ij^+=kappa_ij A_ij DeltaC_ij^+`

and:

`T_run(e_ij)<=U_ij^+`.

So the Bandwidth/supportability clause is no longer only a vague type: there is a concrete source functional acting on a relationship carrier.

### History admissibility

The source gives:

`e <=_H f iff S_R(e) subseteq S_R(f)`.

This History-Support Preorder orders relationships by inclusion of invariant-preserving admissible History support.

So History admissibility also has a concrete source relation.

### Witness / residue

The source gives the finite hidden-network witness:

`W_H^R=(Delta rho_H^R,Lambda_H)`

with History/chirality/persistence data separately typed when required.

It also gives the Projection-Residue Survival Test:

`B_full^R not ~=_F B_vis^R`

as a sufficient field-bundle survival witness.

## What this accomplishes

The R45 mask is now partially executable on **source relationship carriers**.

The strongest recovered clauses are:

- Bandwidth/supportability -> Runtime Transition Capacity;
- History compatibility -> History-Support Preorder;
- projection/invariant survival -> Projection-Residue Survival Test;
- chirality/History state -> explicit coordinates of R_H(t) plus witness package.

This is genuine progress toward a real localized mask.

## Exact new roadblock

Our newly derived torus candidates are:

`A+`, `A-`, `B+`, `B-`.

The source capacity/history functions act on concrete relationships such as `e_ij`.

What we still do not have is the bridge:

`torus local lift lambda  <->  source relationship / continuation carrier e_ij`.

Without that correspondence, it would be fabrication to plug `A+` directly into `T_run(e)`.

So the exact missing QMO is now:

`@open/torus_lift_to_network_edge`.

## Next chain

Crawl the Unified / Rainbow Road APIs for a typed bridge among:

- chirality address;
- chirality corridor;
- admissible continuation;
- continuation operator;
- inheritance morphism;
- environment address;
- hidden S3 relationship edge;
- local torus Resolution lift.

The goal is to identify what object in the source actually carries one local chirality/Resolution continuation.

Once that carrier is identified, apply:

`T_run`
+ History-support preorder
+ projection residue
+ Watcher gates

to each candidate carrier.

Then R47 can finally attempt a true lift-by-lift operative mask.
