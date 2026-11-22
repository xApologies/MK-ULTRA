# AST-DM-WL-P004 — Horizontal Holonomy / S4 Closure Dark-Geometry Test

**Work layer:** WL-007  
**Status:** PROTOCOL CANDIDATE — NOT PARENT PROMOTED

## Goal

Test whether the Version 1 five-dimensional Time-Space can carry a nontrivial horizontal continuity/rotation structure even when the bare `S2`-over-`S3` bundle is topologically trivial, and whether that structure is matter/QFT-null but gravity/GR-non-null at a fixed localized Resolution.

## Phase 0 — bundle hypothesis

Declare whether the model under test is an ordinary locally trivial `S2` sphere bundle over `S3` with standard `O(3)/SO(3)` structure group.

If yes, record the external classification result:

`T5 ~= S2 x S3`

as bare bundle topology.

If no, state the generalized/singular structure explicitly. Do not apply the triviality theorem outside its hypotheses.

## Phase 1 — anchor and loop

Use the recovered marked continuity address:

`b_H -> [H]_R -> p_H in S3`

and local fiber

`Sigma_H=pi^(-1)(p_H)~=S2`.

Choose a closed `S3` continuity loop

`gamma_H(0)=gamma_H(1)=p_H`.

## Phase 2 — finite horizontal transport

Transport local chirality/frame organization with

`P_gamma_H^chi`.

Define

`Hol_H(gamma_H):=P_gamma_H^chi:chi_H->chi_H`.

Compare:

- `H0`: `Hol_H(gamma_H)=id`;
- `H1`: `Hol_H(gamma_H)!=id`.

Because `S3` is simply connected, persistent nonidentity holonomy on a contractible loop excludes a flat defect-free horizontal transport model under the ordinary smooth hypotheses.

## Phase 3 — localized matter/QFT equivalence

At one fixed localized fiber and Resolution `R`, require

`rho_Q,p_H,R(F0)=rho_Q,p_H,R(F1)`.

If an additive difference object is typed:

`DeltaF in ker(rho_Q,p_H,R)`.

Failure means the controlled horizontal structure is already locally matter-readable at that Resolution.

## Phase 4 — gravity/GR separation

Test

`rho_G,p_H,R(F0)!=rho_G,p_H,R(F1)`.

Then type the factorization into the rotational frame branch:

`Hol_H(gamma_H) -> frame representation -> FD_R`.

Only a typed map to an accepted GR observable advances beyond formal dark geometry.

## Phase 5 — S4 closure representation

Use the candidate global closure object

`S4_cl=Susp(S3)`

with regular slice `j_c:S3->S4_cl` and

`kappa_c=j_c o pi:T5->S4_cl`.

Test which parts of the horizontal distinction survive the closure/readout and which are quotiented out. Do not identify `S4_cl` with total Time-Space.

## Phase 6 — physical admission

Required before any physical dark-matter claim:

1. accepted downstream rotating-spacetime/frame observable;
2. conventional baryonic/GR null model;
3. parameter discipline / frozen prediction;
4. evidence that the additional response is required by observation rather than merely allowed by the formalism.

## Pass classes

- `P004-A`: ordinary-bundle topology typed.
- `P004-B`: nontrivial finite horizontal holonomy typed.
- `P004-C`: matter/QFT-equivalent and gravity/GR-inequivalent formal pair.
- `P004-D`: S4 closure compatibility typed.
- `P004-E`: downstream GR observable and null-model comparison.

Only `P004-E` is eligible for physical dark-matter admission.

## Guardrails

- bare topology and connection data are different objects;
- `S4_cl != T5`;
- `S3 != dark matter`;
- nontrivial holonomy alone is not dark matter;
- black-hole anchoring is a galactic specialization, not a generic corridor axiom;
- keep QFT and GR readouts distinct despite common ancestry;
- geometry/algebra first; scalar profiles only as downstream readouts.
