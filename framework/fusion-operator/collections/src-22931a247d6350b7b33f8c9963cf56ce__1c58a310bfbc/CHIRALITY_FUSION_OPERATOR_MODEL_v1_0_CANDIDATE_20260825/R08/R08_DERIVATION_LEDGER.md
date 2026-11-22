# R08 — Derivation Ledger
## Resolution / Readout

### P8-01 — Same formal object can have multiple readable identities
Let `F` be one fixed full Fusion record. The maps

\[
\mathrm{Read}_{R0}(F),
\mathrm{Read}_{R1}(F),
\mathrm{Read}_{R2}(F),
\mathrm{Read}_{R3}(F)
\]

retain progressively more distinctions. They are not required to be equal because their codomains and quotient kernels differ.

For the current pair:

\[
\mathrm{Read}_{R0}(F)=0,
\]

\[
\mathrm{Read}_{R1}(F)
=(\{\!\{L,R\}\!\},-1,0,2),
\]

while `R2` additionally exposes `q`, and `R3` additionally exposes ordered source/witness/provenance data.

Therefore readable identity is Resolution-relative even when Formal Identity is fixed.

### P8-02 — Coarsening loses distinction without destroying source structure
Let `c_{32}` be the map that forgets ordered provenance/witness fields from the full readout. Then

\[
c_{32}(\mathrm{Read}_{R3}(F))
=
\mathrm{Read}_{R2}(F).
\]

Similarly,

\[
c_{21}(\mathrm{Read}_{R2}(F))
=
\mathrm{Read}_{R1}(F),
\]

and

\[
c_{10}(\mathrm{Read}_{R1}(F))
=
\mathrm{Read}_{R0}(F).
\]

No operation here modifies `F`; only readout classes are merged. Thus coarsening gives observational loss, not formal destruction.

### P8-03 — Refinement can separate without creating
Let `F_AB` and `F_BA` be two decorated Fusion records differing only in ordered source/provenance assignment. At `R2` the order is forgotten, so

\[
F_{AB}\sim_{R2}F_{BA}.
\]

At `R3`, ordered provenance is retained, so

\[
F_{AB}\not\sim_{R3}F_{BA}.
\]

The difference did not come into existence at `R3`; it was already formal and merely became distinguishable.

### P8-04 — Bare scalar balance is maximally insufficient for the current chirality question
The map

\[
\mathrm{Read}_{R0}(F)=S_\chi(F)
\]

returns `0` for the current `LR` mirror pair. It also returns `0` for the source-swapped `RL` record and for any other comparison record whose declared signed summary vanishes.

Therefore

\[
S_\chi=0
\]

does not identify the source geometry, seam, local chirality distribution, provenance, or even the presence of nonzero local chirality content.

This formally extends the R07 statement `net balance != annihilation` into a Resolution statement: **a scalar readout can make nontrivial chirality observationally invisible.**

### P8-05 — Occupancy count readout is chirality-blind
The exact fused carrier has

\[
(n_N,n_E)=(3,4).
\]

Any second formal arrangement with the same label populations lies in the same `R_occ` readout class, even if its arrangement/chirality differs. Hence

\[
\text{equal population readout}
\not\Rightarrow
\text{equal chirality structure}.
\]

This follows because the source seed distinction is arrangement/orientation-sensitive rather than count-sensitive.

### P8-06 — Local chirality may be visible while ordered ancestry is not
At `R1_chi`, the output retains

\[
\{\!\{L,R\}\!\},\Pi_\chi,S_\chi,C_\chi,
\]

but not the ordered source tags. Thus an observer may validly read **two opposite local chiralities are present** without being able to say which historical source contributed which side.

This separates chirality visibility from provenance visibility.

### P8-07 — Seam visibility is independent of source-order visibility
At `R2_seam`, `q` is explicitly retained, while ordered witness/provenance fields remain quotiented away. Therefore

\[
\mathrm{Vis}_{R2}(q;F)=1
\]

can coexist with

\[
\mathrm{Vis}_{R2}(\text{source order};F)=0.
\]

Seeing the seam does not reconstruct the history of how the seam formed.

### P8-08 — Hidden seam is not absent seam
At any Resolution whose kernel identifies records that differ only by seam annotation,

\[
\mathrm{Vis}_R(q;F)=0.
\]

But `q` remains a constituent of the formal Fusion carrier. Thus

\[
\text{seam unreadable at }R
\not\Rightarrow
q\notin Q.
\]

### P8-09 — Formal chirality conservation can survive observational chirality death
R07 established sourcewise local chirality preservation in the formal record. Suppose coarsening maps all records with the same `S_chi` to one observational class. Then the local `L/R` difference lies in the readout kernel even though it remains formal.

Therefore

\[
\mathsf{ChProf}(F)\text{ preserved}
\quad\land\quad
\mathrm{Vis}_R(\mathsf{ChProf};F)=0
\]

is consistent.

This is not a contradiction; it is exactly formal-versus-observational identity separation.

### P8-10 — Resolution and Bandwidth produce different failure statements
Let `F` be a formally defined Fusion operation/readout target.

If

\[
B<B_{\min},
\]

the relevant transformation/configuration is not operationally supported under the current Bandwidth condition.

If instead

\[
R<R_{\mathrm{emerge}}(d),
\]

the feature `d` may remain formal and operative while being unreadable.

Hence

\[
\boxed{
\text{unavailable due to Bandwidth}
\neq
\text{invisible due to Resolution}
}
\]

and neither statement can be substituted for the other.

### P8-11 — Two-parameter status table
For a fixed formal feature `d` and operation `Fus`, there are four logically distinct regimes:

1. `Avail_B=1`, `Vis_R=1`: operation supported and distinction readable.
2. `Avail_B=1`, `Vis_R=0`: operation supported but distinction readout-aliased.
3. `Avail_B=0`, `Vis_R=1` on an archived/formal record: distinction can be represented/read while a new operation is not currently supported.
4. `Avail_B=0`, `Vis_R=0`: neither current operative support nor readout distinction is available.

This is why the variables must remain separately typed.

### P8-12 — The row-like output admits a lossless representation explanation
Let the source occupancy display be flattened as

\[
x=(1,0,0,1),
\]

corresponding to

\[
\begin{bmatrix}1&0\\0&1\end{bmatrix}.
\]

Let the display-coordinate permutation be

\[
\sigma=(0,3,1,2),
\]

meaning

\[
\mathrm{Realize}_\sigma(x)
=(x_0,x_3,x_1,x_2)
=(1,1,0,0),
\]

which renders as

\[
\begin{bmatrix}1&1\\0&0\end{bmatrix}.
\]

Because `sigma` is bijective, `sigma^{-1}` reconstructs the source display exactly. Therefore this downstream row-like appearance is **not structurally corrupt if the declared readout contract includes this coordinate permutation**.

This proves that visual mismatch alone is insufficient to diagnose corruption.

### P8-13 — The same row-like output can be a contract failure under a different contract
Suppose instead the declared contract is identity realization:

\[
\mathrm{Realize}_{\mathrm{id}}(x)=x.
\]

Then receiving

\[
y=(1,1,0,0)\neq x
\]

violates that contract unless another declared admissible transformation intervenes.

Thus the classification depends on the typed map:

\[
\boxed{
\text{same visual pair}
\Rightarrow
\begin{cases}
\text{valid re-expression},& y=\mathrm{Read}_R(x),\\
\text{contract failure},& y\neq\mathrm{Read}_R(x).
\end{cases}}
\]

### P8-14 — Endpoint appearance cannot establish underlying-state corruption
A downstream representation `y` carries less logical information than the tuple

\[
(x,\mathcal C_R,y).
\]

Without `C_R`, the inference

\[
y\neq x\Rightarrow\text{corruption}
\]

is invalid because multiple admissible `Realize_R` maps can change presentation while preserving the formal object.

Corruption is therefore a **contract/provenance statement**, not a shape adjective.

### P8-15 — Same source / different projection theorem
Let `F` be fixed. If `R_i` and `R_j` have different kernels or realization maps, then in general

\[
\mathrm{Read}_{R_i}(F)
\neq
\mathrm{Read}_{R_j}(F).
\]

This does not imply `F` changed. It expresses one formal source under different observational equivalence structures.

### P8-16 — Different source / same projection theorem
If `Read_R` is noninjective, there exist formal `F\ne G` with

\[
\mathrm{Read}_R(F)=\mathrm{Read}_R(G).
\]

The current source-swap pair `F_AB,F_BA` supplies an explicit example at every readout that discards source order. Thus equal downstream output cannot establish identical formal provenance.

### P8-17 — Cross-Resolution section provides the correct provenance object
For the nested chain, let

\[
s_F=(s_0,s_1,s_2,s_3),
\qquad
s_i=\mathrm{Read}_{R_i}(F).
\]

Because each coarsening map is defined by forgetting only finer distinctions,

\[
c_{ji}(s_j)=s_i.
\]

Therefore the family is compatible and tracks one formal Fusion record across the chain. This is preferable to treating each readable output as a separate ontology.

### P8-18 — Feature-specific emergence is not whole-object emergence
In the illustrative chain:

- signed balance is available at `R0`;
- local chirality becomes visible at `R1`;
- the seam becomes visible at `R2`;
- ordered provenance/witness becomes visible at `R3`.

These are **feature-specific** emergence levels under one declared chain. They do not mean the Fusion object itself comes into existence at `R3`.

### P8-19 — Readout may make Fusion look merely correlated/paired without changing the formal object
A coarse structural readout may retain only the fact that two opposite chirality classes co-occur, while discarding the shared seam and Fusion witness. Such an output can resemble a paired/correlated description even though the formal source is a Fusion record.

This is a representational aliasing statement only. R08 does not reclassify the underlying object as classical correlation, nor does it use quantum correlation terminology as proof.

### P8-20 — Readout cannot prove a native whole-carrier handedness
No prior run defines a scalar `chi(Q)` for the fused carrier. A realization layer may display one orientation cue, but unless that cue is the image of a formally defined whole-carrier chirality observable, it cannot create such an observable.

Therefore

\[
\text{displayed handed-looking image}
\not\Rightarrow
\text{formal whole-carrier handedness}.
\]

### P8-21 — R09 visibility handoff without pre-solving holonomy
The Resolution source permits a formal holonomy class `h` to have a Resolution-conditioned image `h_R`. R08 can therefore license the statement:

\[
\text{if a nontrivial formal holonomy residue exists, its visibility may be Resolution-dependent.}
\]

R08 does **not** establish that the Fusion operator has nontrivial holonomy, nor that a quantum phase is holonomy. Those are R09 proof obligations.
