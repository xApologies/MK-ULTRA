# R05 — Definitions Ledger

## D5-01 — State-value alphabet

Use the abstract state alphabet

\[
\Sigma_0=\{N,E\}
\]

with interpretation map

\[
\mu:\Sigma_0\to\mathcal V,
\qquad
\mu(N)=\varnothing,
\qquad
\mu(E)=\{\varnothing\}.
\]

The abstract labels prevent type confusion between a carrier point and the set-valued state it expresses.

## D5-02 — Labeled finite carrier

A null-interface carrier is a pair

\[
(X,\lambda_X),
\qquad
\lambda_X:X\to\Sigma_0,
\]

where `X` is a finite set of **addresses/loci** and `lambda_X` assigns a state label.

A null locus is an element `x in X` such that

\[
\lambda_X(x)=N.
\]

The locus `x` is not the empty set. Its interpreted state is the empty set:

\[
\mu(\lambda_X(x))=\varnothing.
\]

## D5-03 — Label-preserving map

A map

\[
f:(X,\lambda_X)\to(Y,\lambda_Y)
\]

is label-preserving when

\[
\lambda_Y\circ f=\lambda_X.
\]

The finite labeled carriers and label-preserving maps form the working category `FinSet/Sigma_0` (the finite slice over the state alphabet).

## D5-04 — Null interface template

Define

\[
J_N=(\{j\},\lambda_J),
\qquad
\lambda_J(j)=N.
\]

An interface selection is a pair of injective label-preserving maps

\[
i_A:J_N\hookrightarrow A,
\qquad
i_B:J_N\hookrightarrow B.
\]

Write

\[
a_\star=i_A(j),
\qquad
b_\star=i_B(j).
\]

## D5-05 — Pre-fusion contact relation

Before quotient identification, the tagged disjoint union keeps the selected loci distinct. Define the one-interface contact relation

\[
R_{AB}=\{(\iota_A(a_\star),\iota_B(b_\star))\}.
\]

Then

\[
|R_{AB}|=1,
\]

so

\[
R_{AB}\neq\varnothing.
\]

This is the first rigorous sense in which a relation between two null-labeled positions can exist without modifying their state value.

## D5-06 — Null-interface pushout

The **null-interface pushout carrier** is

\[
Q=A\sqcup_{J_N}B,
\]

constructed concretely as

\[
Q=(A\sqcup B)/\sim,
\]

where `~` is the smallest equivalence relation satisfying

\[
\iota_A(i_A(j))\sim\iota_B(i_B(j)).
\]

Let

\[
j_A:A\to Q,
\qquad
j_B:B\to Q
\]

be the canonical maps.

## D5-07 — Shared null class

The selected interface class is

\[
q=j_A(a_\star)=j_B(b_\star).
\]

Because the interface maps preserve the label `N`, define

\[
\lambda_Q([x])=
\begin{cases}
\lambda_A(x),&x\in A,\\
\lambda_B(x),&x\in B.
\end{cases}
\]

The compatibility condition makes this well-defined at `q`, and

\[
\lambda_Q(q)=N.
\]

## D5-08 — Null-value preservation invariant

Define the null invariant

\[
\mathsf{NullPres}(q)
\iff
\mu(\lambda_Q(q))=\varnothing.
\]

The Fusion interface passes the null-preservation test iff `NullPres(q)` holds.

## D5-09 — Gluing witness / Fusion witness

A **gluing witness** is external data certifying that the quotient realizes the selected interface span. A minimal work-layer witness is

\[
W_G=(J_N,i_A,i_B,Q,j_A,j_B).
\]

The stronger Fusion witness adds the placement/orientation/provenance record:

\[
\eta_F=
(q,(A,a_\star),(B,b_\star),\rho,\mathsf{FUSE}).
\]

The empty set is not a container for `eta_F`. Rather,

\[
\eta_F\in\mathcal W_F
\]

for a separate witness/provenance space `W_F`.

## D5-10 — Labeled wedge special case

When each source has a chosen interface basepoint and `J_N` is one point, the underlying pushout is the pointed-set wedge pattern

\[
A\vee B
\cong
(A\sqcup B)/(a_\star\sim b_\star).
\]

R05 calls it a **labeled null wedge** only as a special-case description. The primary definition remains the labeled pushout because it generalizes cleanly to larger interface templates.

## D5-11 — Preferred Null-Interface Algebra

The preferred algebraic object is

\[
\mathcal N_F(A,B;J_N)
=
\big(
J_N\xrightarrow{i_A}A,
J_N\xrightarrow{i_B}B,
Q,
\lambda_Q,
j_A,j_B,
W_G,
\eta_F
\big).
\]

This is a **labeled span + finite pushout + external witness**.

## D5-12 — Raw gluing versus Fusion

Raw gluing is the pushout square and carrier `Q`.

Fusion remains the decorated object carrying `eta_F` and inherited provenance/invariant data. Thus R05 retains the R01 distinction

\[
\mathsf{gluing}\neq\mathsf{Fusion}.
\]

---
