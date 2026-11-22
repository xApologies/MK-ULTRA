# R09 — Definitions Ledger
## Holonomy

### D9-01 — Structural Fusion record
Let

\[
F
=
\mathfrak F_{\rm full}
=
(Q,\lambda_Q,A_F,B_F,q,\mathbf X_F,W_G,\eta_F,\mathrm{Inv}_F).
\]

R09 does not alter this carrier.

### D9-02 — Route alphabet and path word
Let `E_route` be the declared alphabet of admissible route-segment identifiers. A route word is a composable finite word

\[
\gamma=e_n\cdots e_1.
\]

Let `[gamma]_H` denote its History class under a declared path equivalence `~_H`.

R09's verifier uses the conservative work-layer rule

\[
\gamma_1\sim_H\gamma_2
\iff
\text{their exact route words agree},
\]

unless a reduction is explicitly declared. This does not claim the final theory must use the free path monoid.

### D9-03 — History monoid
With concatenation and empty word `epsilon`, route histories form a monoid

\[
\mathcal H=(E_{\rm route}^{\ast}/\!\sim_H,\cdot,[\epsilon]).
\]

No inverse is assumed.

### D9-04 — History-augmented Fusion state
Define

\[
\widetilde F=(F,h),
\qquad
h\in\mathcal H.
\]

This is a bookkeeping enlargement licensed by the source separation between structural state and History/provenance.

### D9-05 — Minimal provenance connection
For an admissible route edge `e`, define the minimal work-layer transport

\[
T_e^{\rm prov}(F,h)=(F,h\cdot[e]_H).
\]

The structural Fusion carrier is unchanged while route History is appended.

This is a **constructive work-layer realization** of the source History-append contract. It is not claimed to be the unique or physical Transduction Connection.

### D9-06 — Path transport under the minimal provenance connection
For

\[
\gamma=e_n\cdots e_1,
\]

\[
P_\gamma^{\rm prov}(F,h)
=
(F,h\cdot[\gamma]_H).
\]

### D9-07 — Provenance holonomy action
For a closed route `gamma:U->U`, define

\[
\mathrm{Hol}_{\rm prov}(\gamma)(F,h)
=
(F,h\cdot[\gamma]_H).
\]

It is provenance-trivial at `(F,h)` iff

\[
h\cdot[\gamma]_H=h
\]

under the declared History equivalence.

### D9-08 — Same-endpoint provenance defect
For two paths `gamma_1,gamma_2:U->V`, define

\[
K_{\rm prov}(\gamma_1,\gamma_2;F,h)
=
\mathrm{Def}_H
\big(
 h[\gamma_1],
 h[\gamma_2]
\big).
\]

For the verifier, `Def_H=0` for equal History classes and `1` otherwise.

### D9-09 — Component holonomy signature
Define the work-layer typed signature

\[
\mathrm{Sig}^{F}_{\rm Hol}(\gamma)
=
\big(
[\gamma]_H,
\mathrm{Hol}_{\rm struct},
\mathrm{Hol}_\chi,
\mathrm{Hol}_{\rm prov},
\mathrm{Hol}_\phi,
R,B,
\text{source receipt}
\big).
\]

The components are not identified with one another.

### D9-10 — Structural holonomy component
`Hol_struct(gamma)` is the returned action on the non-History structural record `F`. In the minimal provenance connection,

\[
\mathrm{Hol}_{\rm struct}(\gamma)=\mathrm{id}_F.
\]

This lets R09 isolate a nontrivial History residual without fabricating a structural deformation.

### D9-11 — Chirality path action
If a route registry supplies edge chirality actions

\[
\tau_e\in\{\mathrm{id}_\chi,m\},
\]

then

\[
\mathrm{Hol}_\chi(\gamma)
=
\tau_{e_n}\circ\cdots\circ\tau_{e_1}.
\]

This is a **conditional component definition**. Current R09 evidence does not supply a concrete nontrivial `tau_e` registry for actual Fusion routes.

### D9-12 — Mirror parity
For a route word whose chirality actions are only `id` and `m`, define

\[
\nu_\chi(\gamma)
=
\#\{e\in\gamma:\tau_e=m\}\pmod2.
\]

Then

\[
\mathrm{Hol}_\chi(\gamma)
=
\begin{cases}
\mathrm{id}_\chi,&\nu_\chi=0,\\
m,&\nu_\chi=1.
\end{cases}
\]

### D9-13 — Double-mirror word
Let

\[
\gamma_{mm}=m\,m.
\]

By R07,

\[
m^2=\mathrm{id}_\chi.
\]

Therefore its chirality component is trivial even though its History word need not be trivial.

### D9-14 — Conditional phase connection
A phase-valued holonomy requires additional edge data

\[
u_e\in U(1).
\]

Only then may one define

\[
\mathrm{Hol}_\phi(\gamma)
=
\prod_{e\in\gamma}u_e.
\]

No such Fusion-route phase assignment is presently derived. Therefore `Hol_phi` is **UNDEFINED / UNRESOLVED** for the current operator rather than silently set to the R04 quantum phase.

### D9-15 — History-sensitive readout
R08's `R3_full` reads full Fusion provenance but did not require transport-route History. R09 therefore defines a compatible refinement

\[
R_H\succeq R3_{\rm full}
\]

with

\[
\mathrm{Read}_{R_H}(F,h)
=
(\mathrm{Read}_{R3}(F),[h]_H).
\]

This extends the readout family; it does not retroactively redefine R08's `R3_full` contract.

### D9-16 — Holonomy visibility
For a component defect `d_Hol`, define

\[
\mathrm{Vis}_R(d_{\rm Hol})=1
\]

when the active readout separates outcomes differing only by that defect. A formal defect may exist with `Vis_R=0`.

### D9-17 — Coherence witness firewall
A **quantum coherence witness** must distinguish a coherent state from an incoherent state with the same classical populations. Provenance/path History alone does not satisfy this criterion.
