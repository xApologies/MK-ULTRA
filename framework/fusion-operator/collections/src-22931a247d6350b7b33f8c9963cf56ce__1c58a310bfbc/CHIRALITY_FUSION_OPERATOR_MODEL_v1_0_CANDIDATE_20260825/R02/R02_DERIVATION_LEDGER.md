# R02 — Derivation Ledger
## Do A and B survive Fusion?

# 1. Start from the exact R01 construction

R01 supplies

\[
Q=(C_A\sqcup C_B)/\sim
\]

where the generated equivalence relation has one cross-source identification

\[
a_\star\sim b_\star,
\]

and no pair of distinct elements of \(C_A\) is identified with each other, nor any pair of distinct elements of \(C_B\).

Let

\[
q=[a_\star]=[b_\star].
\]

# 2. Source-image injectivity

Define

\[
j_A=\pi\circ\iota_A,
\qquad
j_B=\pi\circ\iota_B.
\]

Suppose

\[
j_A(a_1)=j_A(a_2).
\]

Then \(a_1\sim a_2\). But the R01 equivalence relation has no nontrivial same-source identifications. Therefore

\[
a_1=a_2.
\]

Hence \(j_A\) is injective. The same proof gives injectivity of \(j_B\).

Therefore

\[
A_F=j_A(C_A)\cong C_A,
\qquad
B_F=j_B(C_B)\cong C_B.
\]

**R02 Result T1 — Embedded Source-Image Theorem**

> In the exact R01 one-interface quotient, each source carrier survives as an embedded source image of the fused carrier.

This result is structural. It does not say the images remain independent.

# 3. Intersection of the source images

The only cross-source equivalence class is \(q\). Therefore

\[
A_F\cap B_F=\{q\}.
\]

The global carrier is covered by the two source images:

\[
Q=A_F\cup B_F.
\]

Thus the native R01 structure is a **one-point amalgam/pushout-like union**, not two disjoint post-Fusion carriers.

For the concrete 4-locus + 4-locus seed pair:

\[
|C_A|=4,
\quad |C_B|=4,
\quad |Q|=4+4-1=7.
\]

# 4. The sources survive as images, not as free factors

If the native carrier were merely the disjoint pair, its carrier size would be 8. It is 7.

If one incorrectly modeled the finite carrier as a Cartesian product,

\[
|C_A\times C_B|=16,
\]

which is again not 7.

Therefore the R01 carrier is neither the original disjoint union nor a finite Cartesian-product factorization.

A Hilbert tensor statement

\[
\mathcal H_F\stackrel{?}{=}\mathcal H_A\otimes\mathcal H_B
\]

is not even typed at this stage: no Hilbert spaces were part of R01. R02 therefore refuses to use tensor factorization as a premise.

**R02 Result T2 — No Native Independent-Factor Result**

> R01 preserves source images but does not supply an independent-factor decomposition of the fused carrier.

# 5. Recovery maps

Because \(j_A\) and \(j_B\) are injective, their inverse maps on the images exist:

\[
\rho_A=j_A^{-1}:A_F\to C_A,
\qquad
\rho_B=j_B^{-1}:B_F\to C_B.
\]

These are exact **local/source-image recoveries**.

However, R01 does not supply a canonical total map

\[
r_A:Q\to C_A.
\]

To extend \(\rho_A\) from \(A_F\) to all of \(Q\), one must choose where every element of \(B_F\setminus\{q\}\) is sent. A structure-preserving extension would require additional data equivalent to a compatible collapse/comparison map from B into A.

The pushout/quotient construction itself provides maps **from the sources into Q**. It does not automatically provide projections **from Q back onto each source**.

Therefore:

- exact recovery on the canonical source images: YES;
- canonical total projection onto A or B: NOT SUPPLIED;
- independent separation: NOT ESTABLISHED.

# 6. Constructional versus intrinsic recovery

The full Fusion construction carries source-tagged residue and the Fusion relation record. With the construction witness retained, one can distinguish the A-side source image from the B-side source image and invert each source embedding on its image.

But remove the witness/tags and retain only the undecorated carrier \(Q\). The symmetric mode admits at least source-swap ambiguity:

\[
Q_\rho(C_A,C_B)\cong Q_{\rho^{op}}(C_B,C_A).
\]

Thus the carrier alone does not canonically encode the **ordered** decomposition "this half was A, that half was B." The decorated provenance is doing real mathematical work.

This is aligned with the supplied Identity Through History distinction: same/readable presentation is weaker than a full recoverable Identity Witness.

**R02 Result T3 — Provenance-Dependent Source Recovery**

> The current source decomposition is constructionally recoverable from the Fusion witness/cospan, but it is not licensed as a unique ordered decomposition of the bare quotient carrier.

# 7. Does separation destroy information?

There are two meanings of separation.

## 7.1 Witness-assisted reconstruction
Given \((j_A,j_B,\eta_F)\), one may duplicate the shared class \(q\) back into two addressed interface representatives and recover source presentations isomorphic to \(C_A\) and \(C_B\).

That is a reconstruction of the inputs from the construction record.

It is **not yet** an inverse Fusion operator. R06 owns that stronger question.

## 7.2 Separation from Q alone
Without the source cospan/provenance, splitting \(q\) requires selecting:

- how many preimages q had;
- which source each preimage belonged to;
- how the relations incident at q partition among them;
- what orientation/provenance each recovered source carried.

Those choices are not supplied by the bare quotient.

Therefore intrinsic separation can lose information even when witness-assisted reconstruction succeeds.

# 8. Can different source pairs yield the same fused result?

At the **carrier-equivalence** level, yes in the weak sense already forced by swap symmetry:

\[
Q_\rho(C_A,C_B)\cong Q_{\rho^{op}}(C_B,C_A).
\]

The same quotient carrier class therefore does not distinguish the ordered source pair.

At the **full decorated Fusion-object** level, R01 deliberately retained

\[
\mathrm{tag}_A(\mathrm{Inv}_A),
\qquad
\mathrm{tag}_B(\mathrm{Inv}_B),
\qquad
\eta_F.
\]

Consequently R02 does **not** license equality of two full Fusion objects produced by genuinely different provenance records. If later normalization intentionally quotients those tags, that is a new operation and must state what information it discards.

# 9. Required roadmap models

## Model S — subsystem-preserving tensor/product model

**Verdict: NOT ESTABLISHED as the native model.**

R01 has no Hilbert typing, and the finite quotient carrier is not a product or disjoint pair. Weak embedded source images survive, but this is not independent-factor survival.

## Model Q — quotient/fusion model

**Verdict: SATISFIED.**

The output is exactly a quotient/pushout-like global carrier. Source images and provenance remain identifiable under the Fusion witness, while the source images intersect at q and are not freely separable.

## Model E — emergent composite with no canonical source factorization

**Verdict: NOT ESTABLISHED in the strong sense.**

Q is a new composite carrier, but R02 has just proved that the exact R01 source images embed in it. A new Hilbert/state space with destroyed source factorization has not been derived.

# 10. R02 classification

The exact current operator is classified as:

\[
\boxed{\textbf{MODEL Q — QUOTIENT FUSION}}
\]

with the refinement:

\[
\boxed{
\text{one global carrier}
+
\text{two overlapping provenance-recoverable source images}
+
\text{no native independent-factor decomposition}
}
\]

This is **weak quotient Fusion**, not yet strong factor-erasing Fusion.

# 11. Consequence for the phrase “no differentiation”

The R01/R02 mathematics does not support the strongest statement that A and B have no differentiation anywhere after Fusion.

What it supports is narrower:

1. the two interface loci become one shared class q;
2. the output is one connected global carrier;
3. A and B remain recoverable as overlapping source images when the Fusion construction/provenance is retained;
4. A and B are not freely separable native factors of that carrier.

Therefore "no differentiation" may become a **future stronger Fusion candidate**, but it cannot be used as a property of \(\mathfrak F^{NN}_0\) without an additional operator that erases or internalizes source decomposition.
