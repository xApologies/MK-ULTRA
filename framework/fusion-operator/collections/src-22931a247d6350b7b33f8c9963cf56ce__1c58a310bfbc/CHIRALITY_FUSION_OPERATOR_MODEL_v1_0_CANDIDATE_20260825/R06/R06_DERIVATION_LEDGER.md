# R06 — Derivation Ledger
## Reversibility

## P6-01 — The quotient projection has no functional left inverse
The pre-Fusion tagged interface loci are distinct:

\[
\iota_A(a_\star)\neq\iota_B(b_\star).
\]

Fusion identifies them:

\[
\pi(\iota_A(a_\star))=q=\pi(\iota_B(b_\star)).
\]

Assume for contradiction that

\[
\ell:Q\to D
\]

satisfies

\[
\ell\circ\pi=\mathrm{id}_D.
\]

Then

\[
\ell(q)=\ell(\pi(\iota_A(a_\star)))=\iota_A(a_\star)
\]

and also

\[
\ell(q)=\ell(\pi(\iota_B(b_\star)))=\iota_B(b_\star).
\]

Therefore

\[
\iota_A(a_\star)=\iota_B(b_\star),
\]

contradicting tagged disjointness.

Hence

\[
\boxed{\text{no functional left inverse of }\pi\text{ exists}.}
\]

This is the exact carrier-level irreversibility introduced by quotient identification.

---

## P6-02 — Right inverses of `pi` exist but are not unfusion
The finite quotient map `pi` is surjective. A section may choose one representative from every fiber, giving

\[
s:Q\to D,
\qquad
\pi\circ s=\mathrm{id}_Q.
\]

For the exact one-interface Fusion, all fibers are singleton except

\[
\pi^{-1}(q)=\{\iota_A(a_\star),\iota_B(b_\star)\}.
\]

Therefore there are exactly two representative sections: one chooses the A-side interface representative and one chooses the B-side representative.

Neither recovers both source interface loci. Thus

\[
\boxed{\text{section}\neq\text{unfusion}.}
\]

A right inverse of the quotient projection only re-embeds one representative per quotient class.

---

## P6-03 — Exact quotient preimage is relation-valued
If `D` and `pi` are retained, the full preimage relation

\[
\Pi^{-1}_{\mathcal P}(x)=\pi^{-1}(x)
\]

recovers the complete quotient fiber. In particular,

\[
\Pi^{-1}_{\mathcal P}(q)
=
\{\iota_A(a_\star),\iota_B(b_\star)\}.
\]

This preserves both interface antecedents, unlike a section.

However, `Pi^{-1}_P` is not derivable from bare `Q`; it requires the original quotient presentation or equivalent witness data.

---

## P6-04 — Bare Fusion has no global ordered inverse
The current symmetric carrier construction admits the source-swap equivalence

\[
Q(A,B)\cong Q(B,A).
\]

The ordered inputs `(A,B)` and `(B,A)` are distinct whenever source order/provenance matters, while their bare fused carriers are isomorphic.

Therefore the map that forgets source tags/witness data is not injective on ordered source presentations. A two-sided inverse would imply injectivity, so

\[
\boxed{\mathfrak F_{\mathrm{bare}}\text{ has no global ordered inverse}.}
\]

This remains true even before considering further alternative decompositions of a bare carrier.

---

## P6-05 — Marking only the shared point is insufficient
Suppose `Q` and `q` are retained but `A_F` and `B_F` are not. To undo the quotient one must determine which non-interface loci belong to each side.

The datum `q` specifies only the point that must be split. It does not specify a partition

\[
Q\setminus\{q\}
=
(A_F\setminus\{q\})\sqcup(B_F\setminus\{q\}).
\]

Therefore

\[
(Q,q)
\]

does not in general determine the source pair.

Hence a seam marker is stronger than a shared-point marker.

---

## P6-06 — Seam data gives a structural cut inverse up to isomorphism
Retain

\[
S_F=(A_F,B_F,q).
\]

Because R02 established injective source maps,

\[
j_A:A\xrightarrow{\cong}A_F,
\qquad
j_B:B\xrightarrow{\cong}B_F.
\]

Define `U_cut` by splitting `q` into two null-labeled copies `q_A,q_B` while leaving every other source-image locus unchanged.

Then there are canonical label-preserving isomorphisms

\[
\alpha:A\xrightarrow{\cong}A^\sharp,
\qquad
\beta:B\xrightarrow{\cong}B^\sharp,
\]

obtained from `j_A,j_B` away from the interface and sending

\[
a_\star\mapsto q_A,
\qquad
b_\star\mapsto q_B.
\]

Thus

\[
\boxed{
\mathfrak U_{\mathrm{cut}}(\mathfrak F_S(A,B,\ldots))
\cong
(A,B,\ldots)
}
\]

for the current one-interface mode.

If the cut result is fused again along the restored interface copies, the two copies are reidentified and one recovers the seam-decorated quotient up to canonical isomorphism:

\[
\boxed{
\mathfrak F_S(\mathfrak U_{\mathrm{cut}}(Q;S_F))
\cong
(Q;S_F).
}
\]

Therefore the current Fusion is **conditionally structurally reversible up to isomorphism when the seam/source-image registry is retained**.

---

## P6-07 — Full witness gives provenance-level left inversion
The R05 witness stores

\[
W_G=(J_N,i_A,i_B,Q,j_A,j_B)
\]

and `eta_F` stores the source-side interface/provenance record.

Define `U_W` to extract the stored source span and tagged source provenance. For every admissible input presentation `X`,

\[
\boxed{
\mathfrak U_W(\mathfrak F_W(X))=X
}
\]

provided equality is understood at the level of the retained source presentation/record.

Thus `U_W` is a **left inverse of the witness-decorated archival Fusion map**.

This result is not deep dynamics: the output explicitly retains the source data required for recovery. Its significance is information accounting—Fusion can externalize the distinction lost in the quotient carrier into its witness record.

---

## P6-08 — Witness-level right inversion is image-restricted
Take an arbitrary tuple resembling a Fusion record. It need not satisfy the pushout square, label compatibility, source-map injectivity, orientation/provenance constraints, or witness coherence.

Therefore `F_W o U_W` cannot be the identity on an unrestricted codomain of arbitrary tuples.

Restrict instead to the image

\[
\operatorname{Im}(\mathfrak F_W).
\]

For a valid output `Y=F_W(X)`, extraction and refusion reproduce the same certified record up to the equivalence convention used for stored presentations:

\[
\boxed{
\mathfrak F_W(\mathfrak U_W(Y))\simeq Y,
\qquad
Y\in\operatorname{Im}(\mathfrak F_W).
}
\]

So the decorated operator is invertible **on its valid image**, not on arbitrary output-shaped data.

---

## P6-09 — Carrier loss versus record loss
The quotient carrier replaces two tagged interface loci by one class:

\[
\{a_\star,b_\star\}\longrightarrow\{q\}.
\]

At the carrier level, the distinction

\[
\text{``A-side interface copy'' versus ``B-side interface copy''}
\]

is no longer encoded as two distinct points.

But the full witness retains that distinction through `i_A,i_B,j_A,j_B,eta_F` and tagged invariant residue.

Therefore:

\[
\boxed{
\text{carrier-level information loss}
\neq
\text{full-record information loss}.
}
\]

The current Fusion can be lossy in its carrier projection while reconstruction-lossless in its fully decorated archival representation.

---

## P6-10 — Discarding witness data makes the loss effective
Let

\[
\mathrm{Forget}:\mathcal Q_W\to\mathcal Q
\]

discard `W_G`, source-image registry, `eta_F`, and source tags.

Then

\[
\mathrm{Forget}\circ\mathfrak F_W
=
\mathfrak F_{\mathrm{bare}}.
\]

By P6-04, `F_bare` has no global ordered inverse. Hence discarding the recovery data converts provenance-reversible Fusion into an effectively irreversible representation.

This gives a precise preservation rule:

> **Reversibility is a property of the operator plus the retained state, not of the quotient shape alone.**

---

## P6-11 — Quantum-state record recovery is not quantum dynamical reversibility
R04 permits the hybrid archival record

\[
(Q,\eta_F,\mathrm{Inv}_F,W_{AB},\rho_{AB}).
\]

If `rho_AB` is carried verbatim as metadata, `U_W` may recover that record. But no quantum Fusion channel

\[
\mathcal E_F
\]

has been derived, and no proof of unitarity, isometry, complete positivity with reversible inverse, or coherence-preserving dynamics has been supplied.

Therefore

\[
\boxed{
\text{state-record recoverability}
\not\Rightarrow
\text{quantum dynamical reversibility}.
}
\]

Conditionally, if a future native fused Hilbert lift provides an isometry

\[
V_F:\mathcal H_{AB}\to\mathcal H_F,
\]

then

\[
V_F^\dagger V_F=I_{AB}
\]

would provide a left inverse on the image of `V_F`. R04 left `V_F` unproved, so R06 does not promote this condition.

---

## P6-12 — No physical/time-reversal conclusion
The current Fusion Operator is a formal carrier/interface construction. R06 derives no physical Hamiltonian, action, dissipative law, thermodynamic cost, time-reversal symmetry, or laboratory process.

Thus the words *reversible* and *irreversible* in R06 refer to **mathematical reconstruction from specified retained data**, unless explicitly qualified otherwise.
