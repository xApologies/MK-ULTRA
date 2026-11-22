# R01 — Definitions Ledger
## A constructive finite model of the first Fusion Operator

### D-F01 — Seed-state alphabet

Let

\[
\mathbb S_0=\{N,E\},
\]

with the present exploratory interpretation

\[
N\equiv\varnothing,\qquad E\equiv\{\varnothing\}.
\]

`N` and `E` are **state labels on addressed loci**. Distinct loci carrying `N` are not different empty sets; their distinction is supplied by their addresses.

### D-F02 — Finite chirality seed

A finite chirality seed is

\[
C=(V,\lambda,\Delta,\chi,\partial V,\mathrm{Inv}),
\]

where:

- \(V\) is a finite set of addressed loci;
- \(\lambda:V\to\mathbb S_0\) is the state-label map;
- \(\Delta\) is the internal relational/diagonal structure;
- \(\chi\) is the seed chirality class/readout;
- \(\partial V\subseteq V\) is the boundary-eligible set;
- \(\mathrm{Inv}\) is the seed's provenance/invariant-residue record.

No Hilbert-space structure is assumed here.

### D-F03 — Mirror seed pair

Let \(M\) be the mirror action on the seed presentation. A pair \((C_A,C_B)\) is a mirror pair when

\[
\chi_B=M(\chi_A)
\]

and the state/relational presentation is the corresponding reflected seed geometry.

R01 does **not** assert that only mirror pairs can ever fuse. It certifies this mode because it is the one supplied by the recovered sketch.

### D-F04 — Null interface template

For the first operator, let

\[
J_N=\{j\}
\]

be a one-locus interface template with

\[
\lambda_J(j)=N.
\]

### D-F05 — Contact placement datum

A placement datum \(\rho\) specifies relative orientation and boundary contact. It must select injective maps

\[
i_A:J_N\hookrightarrow \partial V_A,
\qquad
i_B:J_N\hookrightarrow \partial V_B
\]

such that the selected loci are adjacent under the declared placement:

\[
\mathrm{Adj}_\rho(i_A(j),i_B(j))=1.
\]

### D-F06 — Mirror/null-contact admissibility

Define the first explicit fusion admissibility predicate

\[
A_F^{NN}(C_A,C_B,\rho)=1
\]

iff all of the following hold:

1. \(C_A,C_B\) are well-typed finite chirality seeds;
2. the interface maps are injective and boundary-eligible;
3. \(\lambda_A(i_A(j))=N=\lambda_B(i_B(j))\);
4. the selected loci are adjacent under \(\rho\);
5. the seed pair is mirror-related in the recovered R01 mode;
6. the quotient identification introduces no label contradiction on the selected interface.

This predicate is a **work-layer definition extracted from the supplied mirror/null-contact sketch**. It is not claimed as the universal MK43 chirality composition law.

### D-F07 — Raw interface quotient / gluing carrier

For \(A_F^{NN}=1\), form the disjoint union \(C_A\sqcup C_B\) and generate the smallest equivalence relation satisfying

\[
i_A(j)\sim_\rho i_B(j).
\]

The raw glued carrier is

\[
Q_\rho(C_A,C_B)
=
(C_A\sqcup C_B)/{\sim_\rho}.
\]

The shared equivalence class is written

\[
q=[i_A(j)]=[i_B(j)].
\]

Because both representatives carry the same label \(N\), the label map descends unambiguously:

\[
\lambda_Q(q)=N.
\]

### D-F08 — Fusion relation record

The fusion relation record is the nonempty relational object

\[
\eta_F
=
\big(q,\,
(A,i_A(j)),\,
(B,i_B(j)),\,
\rho,\,
\textsf{FUSE}\big).
\]

Important:

\[
\eta_F\neq\varnothing
\]

does **not** imply that the null label itself changed:

\[
\lambda_Q(q)=N=\varnothing.
\]

Existence is in the relation/provenance record, not inside the empty set.

### D-F09 — Baseline fusion residue

Define the provenance-preserving tagged residue

\[
\mathrm{Inv}^{(0)}_F
=
\mathrm{tag}_A(\mathrm{Inv}_A)
\boxplus
\mathrm{tag}_B(\mathrm{Inv}_B)
\boxplus
\mathrm{tag}_F(\eta_F),
\]

where \(\boxplus\) is a tagged coproduct/ledger union, **not arithmetic addition**.

R01 therefore does not require

\[
\mathrm{Inv}_A=\mathrm{Inv}_B.
\]

Identity reduction, invariant compression, or loss is deferred to R02 and later runs.

### D-F10 — Baseline Fusion Operator

The first certified work-layer Fusion Operator is

\[
\mathfrak F^{NN}_0(C_A,C_B;\rho)
=
\big(
Q_\rho(C_A,C_B),
\eta_F,
\mathrm{Inv}^{(0)}_F
\big)
\]

when \(A_F^{NN}(C_A,C_B,\rho)=1\), and is undefined otherwise.

This is a **decorated pushout/quotient construction** in elementary form.

### D-F11 — Formal versus operative fusion

`Formal Fusion` means \(\mathfrak F^{NN}_0\) is mathematically defined.

`Operative Fusion` at Bandwidth \(B\) requires the corresponding fusion transformation to be available in the active Bandwidth Algebra:

\[
f_\rho\in A_B.
\]

Bandwidth may therefore make a formally valid fusion unavailable without deleting the formal object.

Resolution \(R\) controls distinguishability/readout. It is not, by itself, a formal-existence condition. If the operation requires an observer/runtime to choose one interface among resolution-equivalent candidates, inadequate Resolution may make the **address selection** ambiguous even when formal fusion remains defined.

### D-F12 — Gluing versus fusion

Raw gluing is \(Q_\rho\).

Fusion is the decorated object

\[
(Q_\rho,\eta_F,\mathrm{Inv}^{(0)}_F).
\]

Therefore:

\[
\textsf{gluing}\neq\textsf{fusion}
\]

in the R01 work layer.

### D-F13 — Current nonclaims

R01 does not define:

- quantum amplitudes or phase;
- entanglement;
- subsystem factorization after fusion;
- chirality conservation after fusion;
- inverse/unfusion;
- holonomy of fusion;
- recursive multi-fusion.

Those are reserved by the roadmap.
