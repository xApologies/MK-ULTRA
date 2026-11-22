# R06 — Input Ledger
## Reversibility

**Run:** R06 / 10  
**Dependency:** R05 CLOSED  
**Question:** Can the current Fusion operation be undone, and under which retained-data regimes?

## Authorized inherited premises

### I6-01 — Preferred null-interface algebra [DERIVED / CLOSED R05]
R06 inherits the labeled one-point interface span

\[
J_N\xrightarrow{i_A}A,
\qquad
J_N\xrightarrow{i_B}B,
\]

and its finite labeled pushout

\[
Q=A\sqcup_{J_N}B
\cong
(A\sqcup B)/(a_\star\sim b_\star).
\]

The source maps

\[
j_A:A\to Q,
\qquad
j_B:B\to Q
\]

are part of the certified work-layer construction.

### I6-02 — Null preservation [DERIVED / CLOSED R05]
The fused interface class

\[
q=j_A(a_\star)=j_B(b_\star)
\]

remains null-labeled:

\[
\lambda_Q(q)=N,
\qquad
\mu(N)=\varnothing.
\]

The nonempty Fusion witness is external to the empty-set value.

### I6-03 — Source-image injectivity [DERIVED / CLOSED R02]
For the current one-interface Fusion mode,

\[
j_A,j_B
\]

are injective and

\[
A_F=j_A(A)\cong A,
\qquad
B_F=j_B(B)\cong B,
\]

with

\[
A_F\cap B_F=\{q\},
\qquad
Q=A_F\cup B_F.
\]

Exact inverse maps exist on each source image. R02 explicitly did **not** call this a global unfusion inverse.

### I6-04 — Bare carrier provenance loss [DERIVED / CLOSED R02]
The bare quotient carrier does not canonically distinguish the ordered source pair. Source swap produces an isomorphic carrier in the symmetric mode. Full tagged witness/provenance can preserve the order.

### I6-05 — Gluing witness [DERIVED / CLOSED R05; SOURCE-ALIGNED]
The current gluing witness is

\[
W_G=(J_N,i_A,i_B,Q,j_A,j_B),
\]

and the stronger Fusion witness includes

\[
\eta_F=(q,(A,a_\star),(B,b_\star),\rho,\mathsf{FUSE}).
\]

The supplied Transduction Geometry source independently names a **Gluing Witness** as a recoverable record of how local pieces assemble into a global realization. R06 uses that as source alignment, not as a proof that Fusion is reversible.

### I6-06 — Quantum firewall [DERIVED / CLOSED R03-R04]
Entanglement and superposition are state-layer properties. The minimal hybrid record may retain

\[
(Q,\eta_F,\mathrm{Inv}_F,W_{AB},\rho_{AB}),
\]

but no native fused Hilbert space or quantum Fusion dynamics has been derived.

## R06 may not assume

- a global inverse exists;
- the bare carrier `Q` uniquely determines the source span;
- a set-theoretic section of the quotient map is an unfusion operator;
- witness-assisted extraction proves physical reversibility;
- quantum-state bookkeeping is a unitary inverse;
- chirality is conserved;
- strong factor-erasing Fusion is reversible;
- physical realization or time reversal.

## Required roadmap tests

R06 must test:

1. left inverse;
2. right inverse;
3. local/source-image inverse;
4. inverse with provenance;
5. inverse with extra side information;
6. many-to-one quotient behavior;
7. irreversible identification;
8. exactly which information is retained, destroyed, or externalized.
