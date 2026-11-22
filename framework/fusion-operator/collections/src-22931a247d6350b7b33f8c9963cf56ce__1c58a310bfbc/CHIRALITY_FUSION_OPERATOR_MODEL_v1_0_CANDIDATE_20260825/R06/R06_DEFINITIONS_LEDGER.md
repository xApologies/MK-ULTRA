# R06 — Definitions Ledger
## Reversibility

### D6-01 — Tagged pre-Fusion carrier
Let

\[
D=A\sqcup B
\]

be the tagged disjoint union before interface identification.

### D6-02 — Quotient projection
Let

\[
\pi:D\to Q
\]

be the canonical quotient projection for the one-interface relation

\[
\iota_A(a_\star)\sim\iota_B(b_\star).
\]

The distinguished fiber is

\[
\pi^{-1}(q)=\{\iota_A(a_\star),\iota_B(b_\star)\}.
\]

Every other fiber is a singleton in the current exact one-interface construction.

### D6-03 — Functional left inverse of `pi`
A function

\[
\ell:Q\to D
\]

is a left inverse of `pi` iff

\[
\ell\circ\pi=\mathrm{id}_D.
\]

Such a map would recover every tagged pre-Fusion locus from its quotient image.

### D6-04 — Functional right inverse / section of `pi`
A function

\[
s:Q\to D
\]

is a right inverse of `pi` iff

\[
\pi\circ s=\mathrm{id}_Q.
\]

A section chooses one representative from each quotient fiber.

### D6-05 — Fiber-valued inverse relation
Define the exact preimage relation

\[
\Pi^{-1}_{\mathcal P}:Q\to\mathcal P(D),
\qquad
x\mapsto\pi^{-1}(x).
\]

This is set-valued, not a single-valued inverse function.

### D6-06 — Seam registry
A **seam registry** is

\[
S_F=(A_F,B_F,q,\lambda_Q|_{A_F},\lambda_Q|_{B_F}),
\]

with

\[
A_F\cup B_F=Q,
\qquad
A_F\cap B_F=\{q\}.
\]

It marks which part of the fused carrier descended from each source image.

### D6-07 — Cut / structural unfusion operator
Given `(Q,S_F)`, define

\[
\mathfrak U_{\mathrm{cut}}(Q;S_F)
=(A^\sharp,B^\sharp,J_N^\sharp),
\]

where the shared point `q` is duplicated into distinct null-labeled copies `q_A,q_B`:

\[
A^\sharp=(A_F\setminus\{q\})\cup\{q_A\},
\]

\[
B^\sharp=(B_F\setminus\{q\})\cup\{q_B\},
\]

with

\[
\lambda(q_A)=N=\lambda(q_B).
\]

The new one-point interface template maps to `q_A` and `q_B` respectively.

### D6-08 — Witness extraction operator
For the full decorated Fusion record

\[
\widehat Q_F=(Q,\lambda_Q,W_G,\eta_F,\mathrm{Inv}_F),
\]

define

\[
\mathfrak U_W(\widehat Q_F)
\]

to return the source span and source provenance explicitly stored in `W_G`, `eta_F`, and the tagged invariant record.

This is **provenance extraction**, not automatically a dynamical reversal.

### D6-09 — Bare Fusion map
Let

\[
\mathfrak F_{\mathrm{bare}}:\mathcal D_F\to\mathcal Q,
\qquad
(A,B,J_N,i_A,i_B,\ldots)\mapsto(Q,\lambda_Q),
\]

forget witness/source-image decomposition after forming the quotient.

### D6-10 — Seam-decorated Fusion map
Let

\[
\mathfrak F_{S}:\mathcal D_F\to\mathcal Q_S
\]

retain `(Q,S_F)`.

### D6-11 — Witness-decorated Fusion map
Let

\[
\mathfrak F_W:\mathcal D_F\to\mathcal Q_W
\]

retain the full gluing/Fusion witness and tagged provenance.

### D6-12 — Reversibility classes
R06 uses four classifications:

- **IRREVERSIBLE:** no inverse exists from the declared retained output data.
- **CONDITIONALLY REVERSIBLE:** inversion exists only with extra seam/side data or only up to isomorphism.
- **PROVENANCE-REVERSIBLE:** the full witness/provenance record permits exact source-record reconstruction on the image of Fusion.
- **DYNAMICALLY REVERSIBLE:** an actual evolution law has an inverse dynamics. This class is not established by structural bookkeeping alone.
