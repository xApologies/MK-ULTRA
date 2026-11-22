# CHIRALITY FUSION OPERATOR — Fusion Algebra v1.0 Candidate

## Algebra card

| Property | v1.0 candidate status |
|---|---|
| Objects | finite labeled chirality carriers/composites with provenance |
| Binary operation | partial null-interface pushout Fusion |
| Domain | mirror chirality + label-compatible null/contact interface + witness |
| Recursive operation | fixed-diagram finite colimit / generated quotient |
| Associativity | structural up to canonical isomorphism on compatible static diagrams |
| Full History associativity | not strict by default |
| Commutativity | structural source-swap isomorphism |
| Full provenance commutativity | not strict by default |
| Identity | gluing-layer `J_N` candidate only; no certified Fusion identity |
| Idempotence | not a current law; typed `F(A,A)` undefined |
| Reversibility | bare irreversible / seam conditional / witness provenance-reversible |
| Chirality invariant | tagged sourcewise chirality profile |
| Null invariant | shared seam remains null-labeled; relation/witness carries new structure |
| Readout | Resolution-relative; coarse aliasing allowed |
| History | retained execution word / provenance-valued holonomy |
| Phase holonomy | unestablished |
| Macro-chirality | unestablished |
| Physical realization | unestablished |

## Canonical recursive carrier

\[
Q_G=
\left(\bigsqcup_{v\in V}X_v\right)/\!\sim_G.
\]

For `n` primitive four-locus seeds and `k` independent two-point seams whose equivalence classes do not overlap,

\[
|Q_G|=4n-k.
\]

More generally, if the seam equivalence classes are `S`,

\[
|Q_G|
=
\sum_v|X_v|
-
\sum_{C\in S}(|C|-1).
\]

## Composition law

For a fixed compatible interface graph `G`, any legal sequence that executes exactly the edges of `G` realizes the same generated equivalence relation and therefore the same structural quotient up to the canonical source tagging/isomorphism.

The **full** Fusion record also stores execution History:

\[
\mathfrak F_G^{rec}
=(Q_G,\lambda_G,\mathbf X_G,W_G^{net},h,\mathrm{Inv}_G,R,B).
\]

Thus the correct algebraic slogan is:

\[
\boxed{
\text{carrier confluence does not imply provenance confluence.}
}
\]
