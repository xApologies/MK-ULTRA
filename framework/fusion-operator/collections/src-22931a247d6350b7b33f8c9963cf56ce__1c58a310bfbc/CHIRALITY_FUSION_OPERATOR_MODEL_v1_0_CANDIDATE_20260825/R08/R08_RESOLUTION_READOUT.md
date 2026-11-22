# R08 — Resolution / Readout
## Closed work-layer report

**Run:** R08 / 10  
**Verdict:** CLOSED  
**Classification:** FORMAL-PROFILE-PERSISTENT / RESOLUTION-RELATIVE / COARSENING-ALIASABLE / BANDWIDTH-SEPARATED  
**Next:** R09 — Holonomy

# Executive result

R08 answers the question that produced the earlier false-corruption hazard: **a downstream picture is not the formal object.**

The supplied Resolution & Readout source gives the governing architecture

\[
\mathrm{Read}_R
=
\mathrm{Realize}_R\circ q_R,
\qquad
A_B^R=A_B/K_R,
\]

with observational equivalence

\[
x\sim_R y
\iff
q_R(x)=q_R(y).
\]

Applied to the current Fusion object, this means one formal carrier/chirality/provenance record can legitimately have different readable presentations at different Resolutions. Coarsening may hide the seam, local chirality, or ordered provenance without removing those structures from the formal object.

For the current R07 profile,

\[
\Pi_\chi=-1,
\qquad
S_\chi=0,
\qquad
C_\chi=2.
\]

A scalar readout may return only `0`; a chirality-aware readout may reveal the unordered pair `{L,R}` and content `2`; a seam-aware readout may additionally reveal `q`; and the full provenance readout can distinguish ordered source history and Fusion witness. Those are different readouts of one formal object, not different objects.

R08 also gives an explicit resolution of the earlier diagonal-to-row example. The source display

\[
\begin{bmatrix}1&0\\0&1\end{bmatrix}
\]

can be rendered as

\[
\begin{bmatrix}1&1\\0&0\end{bmatrix}
\]

by a declared bijective coordinate permutation. Under that contract the change is lossless representation. Under an identity-coordinate contract the same output is a mismatch. Therefore:

\[
\boxed{
\text{visual difference alone does not diagnose corruption.}
}
\]

The decisive object is the declared readout/transport contract and its preserved invariants/provenance.

Finally, Resolution remains distinct from Bandwidth. Resolution governs **distinguishability**; Bandwidth governs **available organizational freedom / operative transformation capacity**. A feature can exist and be operative yet be unreadable, or an archived formal feature can be readable while a new transition is not currently Bandwidth-supported.

The result prepares R09 cleanly: if route-dependent holonomy exists, it must first exist as a formal residual transformation; only afterward may R08's Resolution machinery ask whether that residual is visible.

---

# R08 — Input Ledger
## Resolution / Readout

**Run:** R08 / 10  
**Dependency:** R07 CLOSED  
**Question:** Given one underlying fused carrier/profile, which chirality, seam, and provenance distinctions remain visible, aliased, or lost under different Resolution and Bandwidth-limited readout maps?

## Authorized inherited premises

### I8-01 — Current Fusion carrier [DERIVED / CLOSED R01-R06]
The active work-layer Fusion carrier remains the one-interface labeled pushout

\[
Q=A\sqcup_{J_N}B
\cong
(A\sqcup B)/(a_\star\sim b_\star),
\]

with shared null-labeled locus

\[
q=j_A(a_\star)=j_B(b_\star),
\qquad
\lambda_Q(q)=N\mapsto\varnothing.
\]

The full Fusion record retains seam/witness/provenance data in structures distinct from the empty-set value.

### I8-02 — Source-image survival and reversibility profile [DERIVED / CLOSED R02,R06]
The current source maps remain injective. Their images satisfy

\[
A_F\cap B_F=\{q\},
\qquad
Q=A_F\cup B_F.
\]

Bare `Q` is not a canonical ordered source record. Seam data permits structural cutting up to source isomorphism; full witness/provenance permits exact source-record recovery on the valid Fusion image.

### I8-03 — R07 chirality profile [DERIVED / CLOSED]
For the current certified mirror/null/contact Fusion mode:

\[
\Pi_\chi=-1,
\qquad
S_\chi=0,
\qquad
C_\chi=2.
\]

The fused object is sourcewise chirality-preserving and opposition-preserving. Net signed balance does not mean chirality annihilation. The primary conservation object is the tagged profile

\[
\mathbf X_F=
((A_F,\chi_A),(B_F,\chi_B),q,\Pi_\chi,S_\chi,\rho,\eta_F).
\]

No whole-carrier handedness was derived.

### I8-04 — Resolution & Readout source module [SOURCE]
The supplied `Resolution Readout(4).zip` defines Resolution as the structure determining which formal distinctions are readable at a selected observational scope. For formal Bandwidth Algebra `A_B` and Resolution congruence `K_R`, the source gives

\[
A_B^R=A_B/K_R,
\]

with

\[
x\sim_R y
\iff
q_R(x)=q_R(y).
\]

The source separates the Resolution quotient from the final representation realization:

\[
\mathrm{Read}_R
=
\mathrm{Realize}_R\circ q_R.
\]

It explicitly states that readout may merge formal distinctions but does not create formal distinctions.

### I8-05 — Formal versus observational identity [SOURCE]
The source defines

\[
\mathrm{Obs}_R:
\mathrm{FormalIdentity}
\to
\mathrm{ObservationalIdentity}_R,
\]

which need not be injective. Its fibers contain formal identities conflated by readout at `R`.

For a readable class `[x]_R`, its formal Resolution domain is

\[
\mathrm{Dom}_R([x]_R)=q_R^{-1}([x]_R).
\]

### I8-06 — Resolution Landscape [SOURCE]
The source defines a compatible family of readable geometries

\[
\mathcal L_R(B)=\{\mathrm{Geo}_R(B),q_{ji}\},
\]

with cross-Resolution sections satisfying the declared coarsening maps. Formal features can therefore be tracked through multiple readable views without treating those views as different underlying objects.

### I8-07 — Resolution/Bandwidth separation [SOURCE + CLOSED CORRIDOR DISCIPLINE]
The Resolution source states:

- changing Resolution changes which distinctions are readable;
- changing Bandwidth changes which transformations/configurations remain operationally available;
- therefore Resolution and Bandwidth are not interchangeable variables.

The corridor source independently requires both a Resolution threshold and a Bandwidth threshold. R08 preserves that separation exactly.

### I8-08 — Readout-relative death [SOURCE]
When formal distinctions merge under coarsening, the source classifies the distinction as observationally dead at that Resolution, not formally destroyed.

### I8-09 — Chirality arrangement source [SOURCE]
The supplied mirror-seed diagram distinguishes the two seed handedness classes by opposite arrangement/orientation. R08 therefore treats population-only readout as potentially chirality-blind: equal counts do not determine the seed arrangement.

### I8-10 — Earlier endpoint-error correction [DERIVED / CLOSED DISCIPLINE]
A row-like output that differs visually from a diagonal source cannot be classified as structural corruption from appearance alone. The declared transport/readout map must first be specified. R08 owns the rigorous readout formulation of this rule.

## R08 may not assume

- that every Resolution family is a total order;
- that every low-Resolution observer reads `S_chi=0`;
- that a hidden seam is an absent seam;
- that a hidden local chirality is annihilated chirality;
- that a non-diagonal display is corruption;
- that readout preserves source order or provenance unless its contract says so;
- that a finer readout creates a distinction that was not already formal;
- that Bandwidth shortage is the same failure as Resolution blindness;
- that `Realize_R` is injective;
- that one observational identity determines one formal identity;
- that a readout map creates a native whole-carrier handedness;
- that quantum interference visibility follows from structural Resolution alone;
- that relative phase equals holonomy;
- that any formal readout result establishes a physical observer or measurement apparatus.

## Required roadmap tests

R08 must establish or reject:

1. same formal source under multiple readout maps;
2. different formal sources sharing one readout;
3. a readout that hides seam/source provenance;
4. a readout that preserves local chirality but loses source order;
5. a readout that preserves only a scalar summary;
6. a readout that preserves only occupancy/population information;
7. explicit Resolution equivalence classes;
8. cross-Resolution refinement/coarsening consistency;
9. separation of Resolution blindness from Bandwidth unavailability;
10. a formal criterion for when a visually changed downstream representation is **not** corruption;
11. a formal criterion for when a representation mismatch **is** a readout-contract failure;
12. the carry-forward visibility framework needed by R09 without pre-solving holonomy.


---

# R08 — Definitions Ledger
## Resolution / Readout

### D8-01 — Full formal Fusion record
Let the current full structural record be

\[
\mathfrak F_{\mathrm{full}}
=
(Q,\lambda_Q,A_F,B_F,q,\mathbf X_F,W_G,\eta_F,\mathrm{Inv}_F).
\]

This is the formal object read by R08. A readout need not expose every component.

### D8-02 — Resolution quotient
For each modeled Resolution `R`, let `K_R` be a congruence on the relevant formal algebra/record class. Define

\[
q_R:\mathcal A_B\to\mathcal A_B/K_R.
\]

Two formal records are observationally equivalent at `R` when

\[
F\sim_R G
\iff
q_R(F)=q_R(G).
\]

### D8-03 — Readout map
A complete readout is

\[
\mathrm{Read}_R
=
\mathrm{Realize}_R\circ q_R.
\]

The quotient determines which distinctions survive. `Realize_R` determines how the surviving quotient is represented.

### D8-04 — Feature readout / mask model
For the finite Fusion work layer, a useful implementation is a typed feature projection. Let

\[
\mathcal D_F=
\{
\text{carrier},
\text{labels},
\text{seam},
\text{local chirality},
\text{pair opposition},
\text{signed balance},
\text{source order},
\text{witness},
\text{provenance}
\}.
\]

A Resolution mask `M_R subseteq D_F` defines a projection `P_R` retaining exactly the declared features. Its kernel is a finite realization of `K_R`:

\[
F\sim_R G
\iff
P_R(F)=P_R(G).
\]

This is a work-layer model of the source quotient rule, not a claim that every Resolution system is literally a coordinate mask.

### D8-05 — Observational fiber
For output `o` at Resolution `R`, define

\[
\mathrm{Fib}_R(o)
=
\{F\mid\mathrm{Read}_R(F)=o\}.
\]

If the fiber has more than one formal member, the readout is non-identifying at that output.

### D8-06 — Feature visibility
For a formal feature `d in D_F`, define

\[
\mathrm{Vis}_R(d;F)=1
\]

when changing `d` within the admissible comparison class can change the `R`-readout, and `0` otherwise.

This is stronger than merely printing a field name: a feature is visible only if the readout can distinguish alternatives that differ in that feature.

### D8-07 — Persistence profile of a feature

\[
\mathrm{Pers}(d;F)
=
\{R\in\mathrm{Res}\mid\mathrm{Vis}_R(d;F)=1\}.
\]

If the Resolution family admits a first visible level, call it

\[
R_{\mathrm{emerge}}(d;F).
\]

### D8-08 — Observational death
A formal distinction `d` is observationally dead at `R` when it remains part of the formal record but lies in the kernel of the readout:

\[
\mathrm{Vis}_R(d;F)=0.
\]

This is not formal erasure.

### D8-09 — Nested illustrative Resolution chain
Define the following **declared work-layer chain** for the current Fusion record:

- `R0_balance`: retain only signed balance `S_chi`;
- `R1_chi`: retain unordered local chirality multiset, opposition parity, signed balance, and chirality content;
- `R2_seam`: retain all `R1` information plus the existence/identity of the shared seam `q`;
- `R3_full`: retain ordered source images, seam, chirality profile, witness, and provenance.

The chain is ordered

\[
R0\le R1\le R2\le R3.
\]

Each coarsening map simply forgets the extra finer information.

The source allows non-monotone Resolution graphs. Therefore an independent occupancy branch is also permitted:

- `R_occ`: retain only occupancy/null-state population information.

`R_occ` is not silently inserted into the total chain.

### D8-10 — Occupancy readout
For the exact seven-locus fused carrier define

\[
\mathrm{Read}_{\mathrm{occ}}(F)
=(n_N,n_E),
\]

where `n_N` is the number of null-labeled loci and `n_E` the number of singleton-empty/existence-labeled loci.

For the current exact pair,

\[
(n_N,n_E)=(3,4).
\]

Because chirality is arrangement-sensitive, this count is not a chirality classifier.

### D8-11 — Unordered chirality readout

\[
\mathrm{Read}_{\chi}(F)
=
(\{\!\{\chi_A,\chi_B\}\!\},\Pi_\chi,S_\chi,C_\chi).
\]

For the current mirror pair:

\[
\mathrm{Read}_{\chi}(F)
=(\{\!\{L,R\}\!\},-1,0,2).
\]

This preserves local chirality content/opposition but discards ordered provenance.

### D8-12 — Seam readout

\[
\mathrm{Read}_{\mathrm{seam}}(F)
=
(\mathrm{Read}_{\chi}(F),q).
\]

This can distinguish a shared Fusion locus but still need not recover which historical source was first/second.

### D8-13 — Full provenance readout

\[
\mathrm{Read}_{\mathrm{full}}(F)
=
(A_F,\chi_A,B_F,\chi_B,q,W_G,\eta_F,\mathrm{Inv}_F).
\]

This is the current readout level sufficient for ordered source/provenance recovery, subject to the validity of the retained witness.

### D8-14 — Bandwidth availability predicate
Let

\[
\mathrm{Avail}_B(\mathfrak F)
\]

mean that the formal Bandwidth Algebra has enough available organizational freedom to support the relevant Fusion/transport operation. This is distinct from `Vis_R`.

### D8-15 — Resolution/Bandwidth state pair
The operative/readable condition is represented by the pair

\[
(B,R).
\]

`B` answers **can the transformation/configuration be supported?**  
`R` answers **which formal distinctions can be distinguished/read?**

### D8-16 — Representation contract
A readout contract is a tuple

\[
\mathcal C_R=(q_R,\mathrm{Realize}_R,\mathrm{codomain},\mathrm{invariants}).
\]

An output mismatch is assessed relative to this declared contract, not by visual comparison alone.

### D8-17 — Representation-only variation
Suppose `x` is a formal seed occupancy state and `sigma` is a bijection of display coordinates. Define

\[
\mathrm{Realize}_\sigma(x)=\sigma_*x.
\]

If `sigma` is part of the declared contract, then

\[
y=\mathrm{Realize}_\sigma(x)
\]

may look different from `x` while preserving all information recoverable through `sigma^{-1}`.

### D8-18 — Readout-contract corruption
For a deterministic declared readout contract `C_R`, an output `y` is contract-inconsistent for input `x` when

\[
y\ne\mathrm{Read}_R(x)
\]

and no declared admissible representation degree of freedom accounts for the discrepancy.

This is a **readout-contract failure**. It is not inferred merely from a different-looking matrix.

### D8-19 — Readout equivalence profile
For two formal records `F,G`, define

\[
\mathcal E(F,G)
=
\{R\mid F\sim_R G\}.
\]

This records the set of readouts under which the two formal records alias.

### D8-20 — Cross-Resolution Fusion section
A compatible family

\[
s_F=\{s_R\}
\]

is a Cross-Resolution Fusion section when each `s_R` is the readout class of the same formal Fusion record and the declared coarsening maps satisfy

\[
q_{ji}(s_{R_j})=s_{R_i}.
\]

This is the correct object for saying that one Fusion event is followed through multiple Resolution levels.


---

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


---

# R08 — Readout Decision Table
## Resolution / Readout

| Readout | Retains | Hides / aliases | Current Fusion output | What it may establish |
|---|---|---|---|---|
| `R0_balance` | `S_chi` | local L/R, seam, source order, witness, provenance | `0` | net signed balance only |
| `R1_chi` | unordered `{L,R}`, `Pi_chi`, `S_chi`, `C_chi` | ordered ancestry, witness, seam | `{L,R}, -1, 0, 2` | two opposite local chiralities remain represented |
| `R2_seam` | R1 data + `q` | ordered source/witness provenance | chirality profile + shared seam | seam and local opposition are distinguishable |
| `R3_full` | ordered source images, chirality, seam, witness, provenance | nothing intentionally dropped by this work-layer contract | full decorated record | current formal reconstruction/provenance questions |
| `R_occ` branch | label populations | arrangement, handedness, seam semantics, provenance | `(3 null, 4 existence)` | population only |
| bare carrier projection | quotient carrier | historical source order/witness | `Q` | carrier structure only |
| display permutation | declared reindexing | none if bijective and inverse retained | may render diagonal as row | presentation change, not source change |
| identity-display contract | same coordinates expected | n/a | row output mismatches source | contract failure unless another declared map exists |

## Same source / different projection

For fixed formal `F_AB`:

\[
\mathrm{Read}_{R0}(F_{AB})
\neq
\mathrm{Read}_{R1}(F_{AB})
\neq
\mathrm{Read}_{R2}(F_{AB})
\neq
\mathrm{Read}_{R3}(F_{AB})
\]

in the sense that they inhabit different typed readable codomains and expose different distinctions.

## Different source / same projection

For ordered provenance records `F_AB != F_BA`:

| Resolution | Equal output? | Reason |
|---|---:|---|
| `R0_balance` | yes | source order discarded |
| `R1_chi` | yes | chirality multiset unordered |
| `R2_seam` | yes | seam retained but source order still discarded |
| `R3_full` | no | ordered provenance/witness retained |
| `R_occ` | yes | only populations retained |

Therefore observational equality is readout-relative.


---

# R08 — Counterexample Ledger
## Resolution / Readout

### CE8-01 — Zero readout does not mean zero chirality
Current `R0_balance` returns `0`, but R07 proves `C_chi=2` and sourcewise L/R chirality survives. Therefore scalar zero cannot be read as annihilation.

### CE8-02 — Same counts do not mean same arrangement
Two 7-locus records can share `(n_N,n_E)=(3,4)` while differing in the placement of labels and thus in arrangement-sensitive chirality. Population equality is insufficient.

### CE8-03 — Same coarse output does not mean same provenance
`F_AB` and `F_BA` are distinct ordered provenance records but alias under any readout that forgets source order.

### CE8-04 — Hidden seam does not mean no Fusion seam
A seam-blind readout can quotient away the marker `q` while `q` remains in the formal pushout carrier.

### CE8-05 — Finer visibility is not formal creation
When `R1` separates local chirality that `R0` conflates, no new chirality is created. The distinction leaves the kernel of the finer quotient.

### CE8-06 — Row-like display is not automatically corruption
The coordinate permutation `sigma=(0,3,1,2)` maps `[1,0,0,1]` to `[1,1,0,0]` bijectively. Under that declared representation map, the row-like form is lossless.

### CE8-07 — The same row-like display can be wrong under an identity contract
If coordinates are declared fixed, receiving `[1,1,0,0]` from source `[1,0,0,1]` violates the contract. Therefore corruption is contract-relative, not appearance-relative.

### CE8-08 — Low Resolution is not low Bandwidth
A system may have enough Bandwidth to support the formal transformation while lacking Resolution to distinguish the seam. Conversely, an archived formal record can be read at high Resolution even if current Bandwidth does not support executing a new Fusion operation.

### CE8-09 — Seeing `q` does not recover `eta_F`
A readout that exposes the shared locus but discards witness/provenance does not prove which source history generated the seam.

### CE8-10 — Readout cannot manufacture whole-carrier chirality
A rendered image may look left- or right-biased. Without a formal `chi(Q)` observable, that visual bias is not a proof of emergent fused handedness.

### CE8-11 — Readout equality cannot prove physical identity
Two formal records can lie in the same observational fiber. Therefore one readout class cannot be substituted for formal identity without an injectivity proof.

### CE8-12 — Resolution blindness cannot prove nonexistence
If a feature lies in the blind core of the modeled readout family, that means no modeled readout distinguishes it. It does not prove the formal feature is absent.

### CE8-13 — A representation map may preserve information without preserving geometry as drawn
A bijection of display coordinates can preserve recoverable information while changing adjacency on the page. Whether such a map preserves *physical/geometric chirality* is a separate contract requirement. R08 therefore distinguishes representation invertibility from structure-preservation.

### CE8-14 — Quantum interference is not silently imported
R04 defined an interference-sensitive quantum basis. R08's structural Resolution quotient does not automatically guarantee that such a quantum measurement channel exists or remains coherent. Quantum visibility remains separately typed.


---

# R08 — Vera Audit
## Resolution / Readout

**Audit verdict:** PASS / CLOSED  
**Promotion verdict:** WORK LAYER ONLY

### V8-01 — Dependency audit
**PASS.** R08 begins from the exact R07 formal chirality profile and the supplied Resolution & Readout definitions. It does not invent a new Fusion carrier.

### V8-02 — Source terminology audit
**PASS.** `K_R`, `A_B/K_R`, `Read_R = Realize_R o q_R`, observational identity, Resolution Landscape, persistence profile, emergence Resolution, and readout-relative death preserve the source module's meanings.

### V8-03 — Formal/readable type audit
**PASS.** The formal Fusion record is not equated with any one rendered output. Quotient and realization are explicitly separated.

### V8-04 — Noncreation audit
**PASS.** Refinement is treated as revealing a pre-existing formal distinction, not creating one.

### V8-05 — Annihilation audit
**PASS.** Low-resolution/scalar readout `0` is not interpreted as chirality annihilation. R07's nonzero local chirality content remains formal.

### V8-06 — Provenance audit
**PASS.** Seam visibility, source-order visibility, and witness visibility are separately typed. Seeing one does not silently recover the others.

### V8-07 — Corruption audit
**PASS.** The earlier row-like example is no longer classified by appearance. R08 gives both an admissible bijective display transformation and an identity-contract failure case, proving that the readout contract is decisive.

### V8-08 — Resolution/Bandwidth audit
**PASS.** `R` controls distinguishability; `B` controls available organizational freedom/operative transformations. The two failure modes are not conflated.

### V8-09 — Resolution-order audit
**PASS.** The nested R0-R3 chain is explicitly an illustrative work-layer chain. The independent occupancy readout is kept as a branch because the source allows non-monotone Resolution graphs.

### V8-10 — Whole-carrier chirality audit
**PASS.** No `chi(Q)` scalar is manufactured by a displayed orientation cue.

### V8-11 — Quantum firewall
**PASS.** Structural Resolution/readout is not used to claim existence of a coherent quantum measurement channel or interference visibility.

### V8-12 — Holonomy firewall
**PASS.** R08 only establishes how a hypothetical/formal holonomy residue would be subjected to Resolution quotienting. It does not prove nontrivial Fusion holonomy or equate relative phase with holonomy.

### V8-13 — Physical observer audit
**PASS.** `Read_R` is a formal readout map. No physical human/device observer is inferred.

### V8-14 — Anti-recursion audit
**PASS.** Each major section performs a distinct job: source typing, quotient definition, nested/graph Resolution architecture, aliasing proofs, Bandwidth separation, explicit display-permutation construction, counterexamples, and R09 handoff.

### V8-15 — Falsifiability
R08 must be revised if an authenticated source or later formalism establishes any of the following contrary facts:

- Resolution itself changes the underlying formal Fusion carrier rather than its readable equivalence structure;
- the declared source `Read_R` is universally injective;
- Bandwidth and Resolution are proven to be one variable in the relevant domain;
- the current Fusion carrier has a native whole-carrier chirality observable that every admissible readout must preserve;
- the row-like transformation is forbidden by a stronger canonical readout contract;
- witness/provenance is intrinsically recoverable from bare readout without retained side information.

**Vera verdict:** R08 may close.


---

# R08 — Exit Verdict
## Resolution / Readout

**Status:** CLOSED

### Classification

\[
\boxed{
\textbf{FORMAL-PROFILE-PERSISTENT / RESOLUTION-RELATIVE / COARSENING-ALIASABLE / BANDWIDTH-SEPARATED}
}
\]

for the current certified mirror/null/contact weak quotient Fusion mode.

### Closed results

1. The full fused carrier/chirality/provenance record is a formal object distinct from its readouts.
2. Resolution acts through a quotient/congruence followed by a representation realization.
3. Readout can merge formal distinctions but cannot create new formal distinctions.
4. One formal Fusion record can have multiple typed readable presentations.
5. Different formal Fusion records can share a readout whenever the map is noninjective.
6. The current ordered source-swap pair aliases under every declared coarse readout that forgets source order and separates at the full provenance readout.
7. `S_chi=0` is a valid scalar summary but can hide the nonzero local chirality profile; it is not annihilation.
8. Occupancy population `(3,4)` does not determine chirality arrangement.
9. Local chirality can remain visible while ordered ancestry is hidden.
10. Seam `q` can be visible while Fusion witness/provenance remains hidden.
11. An unreadable seam or chirality feature remains formal; coarsening causes observational death, not formal destruction.
12. Resolution and Bandwidth are distinct: unreadable is not the same as operationally unavailable.
13. The diagonal-to-row example can be a lossless display reindexing under a declared bijection.
14. The same diagonal-to-row mismatch can be a readout-contract failure under an identity-coordinate contract.
15. Therefore endpoint appearance alone is insufficient to diagnose corruption.
16. A compatible Cross-Resolution Section is the correct object for tracking one Fusion record through multiple readout levels.
17. No native whole-carrier chirality scalar is created by readout.
18. R08 supplies a visibility framework for R09 without establishing nontrivial holonomy.

### Compact readout law

\[
\boxed{
\mathrm{Read}_R(\mathfrak F_{\mathrm{full}})
=
\mathrm{Realize}_R\!
\left(
q_R(\mathfrak F_{\mathrm{full}})
\right),
\qquad
\text{readout loss}\neq\text{formal destruction}.
}
\]

### Corruption criterion

\[
\boxed{
\text{Corruption/contract failure requires disagreement with the declared map, not merely disagreement with the source display.}
}
\]

### Not established

R08 does not establish:

- one universal physical Resolution ladder;
- a physical measurement apparatus;
- quantum interference visibility under Fusion;
- a native whole-carrier fused chirality observable;
- nontrivial Fusion holonomy;
- phase-holonomy identity;
- recursive Fusion associativity;
- physical realization.


---

# R08 — Carry-Forward Packet
## Licensed inputs for R09 — Holonomy

R09 may inherit as CLOSED:

- the full formal Fusion record as distinct from any readout;
- `Read_R = Realize_R o q_R` as the governing readout architecture;
- Resolution equivalence `F ~_R G iff q_R(F)=q_R(G)`;
- observational identity maps may be noninjective;
- one formal object may have multiple Resolution-conditioned readouts;
- different formal objects may alias at coarse Resolution;
- coarsening can observationally kill a distinction without formally destroying it;
- feature persistence profiles `Pers(d;F)` and feature emergence Resolution where defined;
- a compatible Cross-Resolution Section as the object tracking one formal feature through multiple views;
- the R0-R3 illustrative chain and separate occupancy branch as work-layer readout examples;
- the fact that local chirality, seam visibility, and provenance visibility have distinct readout requirements;
- `S_chi=0` may hide nonzero local chirality content;
- occupancy counts may hide arrangement/chirality;
- endpoint appearance alone cannot diagnose corruption;
- readout-contract violation is the typed corruption criterion;
- Resolution and Bandwidth remain separately typed;
- if a formal holonomy residue `h` exists, its readout image may be written `h_R` and its visibility can be Resolution-dependent.

R09 may **not** inherit as proved:

- that the current Fusion object has nontrivial holonomy;
- that two routes with the same endpoints differ by a nontrivial holonomy element;
- that a residual phase exists;
- that quantum relative phase `phi` equals holonomy;
- that a route-dependent chirality change exists;
- that holonomy is visible at every Resolution;
- that failure to read holonomy means trivial holonomy;
- that the old sketch encodes a loop/connection;
- physical realization.

### R09 active question

Given the now-separated formal object and Resolution-conditioned readout architecture, do distinct admissible Fusion/transport paths with the same endpoints leave a nontrivial **formal** residual transformation (chirality-, provenance-, phase-, or mixed-valued), and if so, at which readouts does that residual remain distinguishable?
