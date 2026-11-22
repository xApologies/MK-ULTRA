# R07 — Derivation Ledger
## Chirality Conservation

## P7-01 — Population count is not chirality
The supplied seed pair is mirror-related with opposite orientation while preserving the same number of occupied/nonoccupied entries. Therefore population count alone cannot distinguish the two seed orientations.

This agrees with the supplied *Holonomy and Chirality* source: arrangement, not population count alone, carries the primitive chirality distinction.

Hence

\[
\boxed{\text{chirality is not an occupancy-count scalar}.}
\]

---

## P7-02 — The current quotient does not alter either source seed internally
The R01/R05 equivalence relation identifies exactly one selected **cross-source null interface pair**. It performs no same-source identification inside `A` and no same-source identification inside `B`.

R02 therefore proved

\[
j_A:A\hookrightarrow Q,
\qquad
j_B:B\hookrightarrow Q
\]

are injective.

Consequently the complete internal incidence/label arrangement of each seed survives on its source image:

\[
A_F\cong A,
\qquad
B_F\cong B.
\]

Since the seed handedness is carried by that arrangement, the current weak quotient Fusion preserves each source seed's handed class on its embedded image.

Thus

\[
\boxed{
\chi(A_F)=\chi(A),
\qquad
\chi(B_F)=\chi(B).
}
\]

This is the first genuine chirality-conservation statement for the current operator.

---

## P7-03 — The shared null locus does not acquire a scalar handedness
The point

\[
q=j_A(a_\star)=j_B(b_\star)
\]

is a carrier locus whose state label remains null:

\[
\lambda_Q(q)=N\mapsto\varnothing.
\]

But chirality is a relational/organizational property of the seed arrangement, not the set value stored at a single locus.

Therefore the inference

\[
q\text{ is null}\Rightarrow\chi(q)=0
\]

is a type error unless a separate pointwise chirality field has first been defined.

R07 defines no such field. The correct statement is that `q` carries **two source ancestries in the Fusion witness**, not a newly invented third handedness.

---

## P7-04 — Opposite-pair Fusion is balanced, not annihilated
For the current mirror pair,

\[
\chi_B=m(\chi_A),
\]

so under any conventional sign coordinate,

\[
\epsilon(\chi_B)=-\epsilon(\chi_A).
\]

Hence

\[
S_\chi
=
\epsilon(\chi_A)+\epsilon(\chi_B)
=0.
\]

But

\[
C_\chi
=|
\epsilon(\chi_A)|+|\epsilon(\chi_B)|
=2.
\]

Therefore

\[
\boxed{
S_\chi=0
\not\Rightarrow
C_\chi=0.
}
\]

The signed net cancels while both local chirality structures remain present and provenance-recoverable.

The correct classification is:

\[
\boxed{
\text{globally chirality-balanced in the additive summary, locally chirality-retentive.}
}
\]

---

## P7-05 — Pair opposition parity is preserved in the decorated Fusion record
For the current certified mirror pair,

\[
\Pi_\chi(A,B)=-1.
\]

By P7-02, the source-image orientations remain unchanged. Therefore

\[
\Pi_\chi(A_F,B_F)
=
\Pi_\chi(A,B)
=-1.
\]

Thus the opposite-handed **relationship** survives Fusion when the source-image/witness decomposition is retained.

This is stronger than the scalar net `S_chi=0` because it records the pair relation rather than only a cancellation result.

---

## P7-06 — The complete conserved object is profile-valued, not scalar-valued
Suppose one attempted to summarize Fusion chirality by only `S_chi`. The states `LR` and `RL` both give

\[
S_\chi=0,
\]

and any future more complicated collection could also have zero net while containing nontrivial local chirality.

The scalar therefore cannot encode:

- which source carried which orientation;
- whether the pair was opposite or an unresolved mixture;
- source order/provenance;
- the interface placement relation `rho`;
- local chirality ancestry after Fusion.

The tagged profile

\[
\mathbf X_F
\]

retains these distinctions.

Hence the minimum adequate current conservation law is:

\[
\boxed{
\mathbf X_F
=
\mathsf{Embed}_F(\mathbf X_{AB})
}
\]

up to the source-isomorphism convention already licensed by R02/R06.

A scalar `S_chi` is only a derived observable of that profile.

---

## P7-07 — Bare `Q` does not intrinsically conserve ordered chirality provenance
R06 proved that the bare carrier does not canonically determine the ordered source pair. The source-swap construction gives an isomorphic carrier:

\[
Q(A,B)\cong Q(B,A).
\]

Therefore from bare `Q` alone one cannot in general recover the ordered profile

\[
((A,\chi_A),(B,\chi_B)).
\]

So chirality conservation has the same layered information profile as reversibility:

\[
\boxed{
\text{decorated Fusion: chirality provenance conserved}
}
\]

while

\[
\boxed{
\text{bare carrier: ordered chirality provenance not canonically readable}.
}
\]

This is not chirality destruction. It is loss of an intrinsic recovery handle after provenance is forgotten.

---

## P7-08 — Same-handed test cases are outside the current certified Fusion domain
The roadmap requests `L+L` and `R+R` tests. For those pairs,

\[
\Pi_\chi=+1.
\]

But the current R01 operator was certified for the recovered **mirror/null/contact mode**. R07 therefore may not silently extend that operator to same-handed pairs.

For the current operator:

\[
\boxed{
\mathfrak F^{NN}_0(L,L)=\mathrm{undefined},
\qquad
\mathfrak F^{NN}_0(R,R)=\mathrm{undefined}
}
\]

unless a later operator explicitly enlarges the admissible domain.

If such an extension were later defined, an additive signed summary would yield `+2` or `-2` depending on convention. That arithmetic is a **counterfactual diagnostic**, not a current Fusion result.

---

## P7-09 — Mirroring both sources preserves current admissibility and balance
Apply the mirror involution to both sources:

\[
(L,R)\mapsto(R,L).
\]

Then

\[
\Pi_\chi
\mapsto
(-\epsilon_L)(-\epsilon_R)
=
\Pi_\chi=-1,
\]

and

\[
S_\chi\mapsto-S_\chi=0.
\]

Therefore a global mirror preserves the opposite-pair admissibility class and the zero signed balance.

At the ordered provenance level it swaps the handed labels associated with the two source positions. At the bare symmetric carrier level the output may be isomorphic to the original carrier.

---

## P7-10 — Mirroring only one source leaves the current Fusion domain
Mirror only `A` in an `L,R` pair:

\[
(L,R)\mapsto(R,R),
\]

or mirror only `B`:

\[
(L,R)\mapsto(L,L).
\]

In either case

\[
\Pi_\chi:+(-1)\mapsto+1.
\]

The current mirror-pair admissibility condition is therefore broken.

Hence the current operator does not interpret a one-sided mirror as chirality nonconservation. It classifies it as a **different input that is outside the certified domain**.

---

## P7-11 — Compatible mirror maps induce an involution on the bare fused carrier
Assume the recovered pair has a label-preserving mirror isomorphism

\[
M:A\xrightarrow{\cong}B
\]

with

\[
M(a_\star)=b_\star,
\qquad
M^{-1}:B\xrightarrow{\cong}A.
\]

Define a map on the disjoint union that swaps the source copies through `M` and `M^{-1}`. Because the selected interface pair is mapped to itself as an equivalence class, the map respects the quotient relation and descends to

\[
\widehat M:Q\to Q.
\]

On the source images,

\[
\widehat M(j_A(a))=j_B(M(a)),
\]

\[
\widehat M(j_B(b))=j_A(M^{-1}(b)).
\]

At the interface,

\[
\widehat M(q)=q.
\]

Applying twice returns every source-image point:

\[
\widehat M^2=\mathrm{id}_Q.
\]

Therefore

\[
\boxed{\widehat M\in\mathrm{Aut}(Q),\qquad \widehat M^2=\mathrm{id}.}
\]

The bare mirror-pair quotient is therefore **mirror-self-isomorphic** under the compatibility assumptions.

This does not mean local chirality is absent. The automorphism exchanges the two opposite-handed source images.

---

## P7-12 — Fusion and global mirror commute up to canonical isomorphism in the current symmetric mode
Because the mirror maps preserve the interface span, mirroring before taking the pushout and mirroring the completed pushout produce canonically isomorphic bare carriers:

\[
\boxed{
M\big(A\sqcup_{J_N}B\big)
\cong
M(A)\sqcup_{J_N}M(B).
}
\]

For the exact opposite pair this is the structural statement that

\[
\mathsf{Mirror}\circ\mathsf{Fusion}
\simeq
\mathsf{Fusion}\circ(\mathsf{Mirror}\times\mathsf{Mirror})
\]

on the current mirror-compatible domain.

At the **decorated ordered** level the witness/provenance tags must also be mirrored/swapped. Otherwise the bare carrier may be symmetric while the ordered historical record is not literally identical.

---

## P7-13 — No emergent single handedness is derived
The current Fusion output contains two embedded opposite-handed source images and one shared null interface class. Nothing in R01-R06 supplies a rule

\[
\chi_F:Q\to\{L,R\}
\]

that assigns one handed class to the entire fused carrier.

Therefore the statements

- `Fusion output is L`,
- `Fusion output is R`,
- `Fusion output has chirality 0 as a new local state`

are all unsupported.

The strongest current result is the conserved **chirality profile** plus the derived balance/parity summaries.

---

## P7-14 — R07 conservation law
For every input in the **current certified mirror/null/contact Fusion mode**, the decorated output satisfies

\[
\boxed{
\mathsf{ChProf}\big(\mathfrak F^{NN}_0(A,B;\rho)\big)
\simeq
\big((A_F,\chi_A),(B_F,\chi_B),\Pi_\chi=-1,S_\chi=0,\rho,\eta_F\big)
}
\]

with

\[
\chi(A_F)=\chi_A,
\qquad
\chi(B_F)=\chi_B.
\]

Thus current Fusion is:

\[
\boxed{
\textbf{SOURCEWISE CHIRALITY-PRESERVING,
OPPOSITION-PRESERVING,
NET-BALANCED,
AND NOT CHIRALITY-ANNIHILATING.}
}
\]

A single scalar conservation law is inadequate; the conserved work-layer object is profile/provenance-valued.
