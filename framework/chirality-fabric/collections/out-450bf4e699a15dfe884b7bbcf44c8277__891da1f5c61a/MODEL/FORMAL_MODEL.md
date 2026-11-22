# CRD → QCD Formal Live Model v1.3

**Status:** source-corrected live model. Physical QCD inheritance remains open.

## 1. Upstream object

Use the frozen CRD state schema

`X=(G,C,x,f,beta,R,B,Inv,P,H,Pi_read)`.

One CRD block is a `2 x 2 x 2` cube of chirality bytes. The chirality byte itself is a `2 x 2 x 2` occupancy object. CRD relaxation acts through cooperative Cluster Portals; exact/coboundary sectors close while nontrivial cohomology defines persistent chirality-knot candidates.

## 2. Rainbow basin semantics

Let

`B6={Red,Orange,Yellow,Green,Blue,Violet}`

with source-locked structural expressions

`b=(0.142857,0.2857,0.42857,0.57,0.7,0.857)`.

These are structural basin values. Do not continue them by decimal pattern completion.

The infinite `142857...` grammar is assigned to the containing environment/runtime structural grammar and does not define an order on B6.

The Rainbow is the arc/geometry; basin colors are telemetry/readout labels. White denotes structural superposition rather than a seventh basin.

## 3. Road state and selector

Retain the overlay factorization

`Pi_YM = rho_YM o Pi_Q o S_RH`.

`S_RH` is an open partial selector from complete Road state—including History, chirality and B6 routing data—into a Helicon mode sector.

No basin ordering, root pairing, or QCD color assignment is assumed in its definition.

## 4. Time-Space/QFT handoff

The source Time-Space formalism provides

`H : T -> Q`

and the canonical handoff object

`Q=(M,F,pi_F,h,nabla,R^nabla,Gamma,A,P,S)`.

The projected residue at `p in M` is

`F_p = Inv(Pi^{-1}(p))`.

This is the controlling object for the six-to-three problem: determine which upstream distinctions survive the projection and which become equivalent under the projection symmetry.

The handoff supplies a finite-rank complex Hermitian vector bundle, connection and curvature. It does **not** by itself establish rank 3 or an SU(3) reduction.

## 5. Retained L07 target algebra

The conventional downstream target decomposition

`su(3) = (su(2) + u(1)) direct_sum m`

with real four-dimensional complement `m` remains valid as target mathematics. It is not an upstream derivation.

## 6. Retired C6 branch

All use of a basin `C6` cycle derived from repeating `142857` pattern completion is withdrawn.

Consequently no active basin-to-A2 root map, compact C6 generator orbit, or C6-derived link variable is available.

## 7. Retained L09A static gauge skeleton

For CRD residual

`r_x=f+delta x in C1(G;Z2)`

choose the target representation

`eta=diag(-1,-1,1) in SU(3)`

and define

`J_f(x)_e = eta^(r_x(e))`.

For a Portal flip `x -> x+y`, with `g_y(v)=eta^(y_v)`, one has

`J_f(x+y)_e = g_y(t(e)) J_f(x)_e g_y(s(e))^-1`.

Also

`Phi_f(x)=(3/4) sum_e c_e [1-(1/3)ReTr J_f(x)_e]`.

Thus the frozen cochain relaxation embeds as gauge-representative motion / gauge fixing in this restricted target sector. It does not by itself generate physical Yang-Mills evolution.

## 8. Correct physicality gate

After an actual source-derived projected link/connection `U_e(X)` exists, compare an updated Portal state `PX` with the exact cochain gauge skeleton:

`D_P(e)=U_e(PX) [g_P(t(e)) U_e(X) g_P(s(e))^-1]^-1`.

- `D_P=I` everywhere: downstream update is pure gauge on the tested sector.
- nontrivial gauge-invariant content of `D_P`: Road/Helicon projection contributes physical gauge-class motion.

No `U_e` may be constructed from the retired C6 lane generators.

## 9. Finish-line equation

Once `Pi_QCD` and downstream evolution are typed, test

`Pi_QCD o R_CRD = R_QCD o Pi_QCD`

or a predeclared approximate observable version.

This equation is the L09E finish line. Failure is retained as a theorem/no-go on the declared sector and does not rewrite CRD.


## 10. L08B source-closed Road→Helicon correspondence

Let `R_adm` be the class of complete Road states whose Portal contracts close.

Let

`H_Hel = {H_alpha | L_H(H_alpha)=lambda_alpha H_alpha}`.

The strongest source-closed Road→Helicon object is

`S_RH : R_adm ⇉ H_Hel`

(a partial, generally set-valued correspondence).

A unique mode function is not source-derived. Basin telemetry and Road History are retained in the Road state, but their direct map to the Helicon spectral index remains open.

This result is independent of the retired C6 branch.


## 11. L08C quotient-descent / residue-survival theorem

For the Time-Space quotient

`Pi : dXi -> M = dXi/G_Pi`,

a boundary feature `a:dXi->Y` survives as a well-defined projected attribute iff it factors through `Pi`:

`a = a_bar o Pi`.

Equivalently it must be constant on projection-equivalence classes; in the group-action presentation it must be `G_Pi`-invariant.

Applied to the Road/Helicon bridge, this exposes an additional carrier map

`iota_partial : Graph(S_RH) ⇀ dXi`

which is not source-closed by the mounted material.

Consequences:
- only the abstract quotient point and invariant residue are guaranteed once a boundary carrier exists;
- Road History, basin telemetry, chirality, Portal ordering, Helicon-mode labels and other fields are not automatically residue data;
- `Pi` is not a basin-label quotient and cannot be used to manufacture `B6 -> C3`.


## 12. L09C QFT-to-QCD reduction no-go

The Time-Space handoff supplies only a finite-rank complex Hermitian bundle `F->M` with unspecified finite rank.

No source theorem fixes rank three or a determinant-one `SU(3)` reduction.

Therefore QCD requires an additional witness

`W_3=(E_c,rho_c,h_c,omega_c,nabla_c)`,

with `rank_C(E_c)=3`, residue-compatible readout, determinant trivialization and a preserving connection.

QFT compatibility is source-closed; inherited QCD specialization is not.


## 13. Corridor-backed Road boundary carrier correction

For the corridor-backed Road sector,

`L_alpha : Sigma_alpha -> dXi_alpha`,
`P_W : dXi_alpha -> dXi_beta`,
`C_alpha_beta = Pi_beta o P_W o L_alpha`.

A Road composed from such Portal routes induces boundary transport

`P_Gamma = P_Wn o ... o P_W1`

where composable, and hence a terminal boundary carrier

`iota_R(Gamma)=b_Gamma in dXi`.

The remaining missing object is not Road→boundary in general, but the Helicon decoration/readout carrier

`iota_H : (b_Gamma,H_alpha) ⇀ dXi or Q`.

The quotient-descent theorem remains unchanged.


## 14. L08D Time-Shell→Q blocker

The exact Q target object exists, but the source does not complete the local morphism carrying a corridor-backed, Helicon-decorated persistent-boundary state into the QFT realization.

Required target:

`Lambda_HQ : D_HQ ⇀ Q_loc`.

It must satisfy base/residue compatibility, a typed Helicon representation, projection covariance, and transport/intertwining compatibility before any QCD reduction is attempted.


## 15. L09A2 defect class = restricted gauge orbit

With `J_{f,x}(e)=eta^(f(e)+delta x(e))`:

`J_{f,x} ~_gauge J_{f',x'}` iff `[f]=[f'] in H^1(G;Z2)`.

Therefore local fixed-`f` relaxation is gauge fixing, while an unbinding that changes `[f]` changes a gauge-invariant closed-loop parity sector.

The subgroup remains abelian; this is not yet Yang-Mills self-interaction.
