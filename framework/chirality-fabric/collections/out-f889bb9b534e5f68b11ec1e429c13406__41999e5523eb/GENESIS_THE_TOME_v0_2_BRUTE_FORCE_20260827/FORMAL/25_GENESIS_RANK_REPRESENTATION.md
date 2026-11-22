# GENESIS — RECOVERABLE INDEPENDENCE, RANK, AND REPRESENTATION FORMATION

**Status:** Foundational extension candidate.  
**Purpose:** supply the missing mathematical layer between persistent closure and downstream vector-space / group representation.

Genesis does not define rank by counting visible objects, colors, coordinates, history stages, or labels. Rank is determined by **recoverable independence** relative to a declared operator system, scope, Resolution, and invariant contract.

## Primitive Extension PR0 — Recoverability Context

A recoverability context is a tuple

\[
\mathcal K=(\mathcal G,\Omega,\mathfrak O,\mathsf{Inv},\mathsf{Res},\mathsf{Hist})
\]

where \(\mathcal G\) is the ambient Genesis domain, \(\Omega\) the scoped carrier, \(\mathfrak O\) the admitted operator family, \(\mathsf{Inv}\) the invariant contract, \(\mathsf{Res}\) the Resolution/readout structure, and \(\mathsf{Hist}\) the retained history/provenance record.

**Nonclaim.** This tuple notation is metalanguage. It does not assert that Genesis is fundamentally set-theoretic.

## Definition GR1 — Recoverable Generation

For \(S\subseteq\Omega\), define the recoverable closure \(\operatorname{RCl}_{\mathcal K}(S)\) to be the least \(\mathcal K\)-admissible closed structure containing \(S\), when such a least closure exists.

Equivalently, \(x\in\operatorname{RCl}_{\mathcal K}(S)\) only when there exists an admitted finite derivation from \(S\) to \(x\) whose operator signatures, history, provenance, and invariant witnesses are retained.

## Definition GR2 — Recoverable Dependence

An element/address \(x\) is recoverably dependent on \(S\) when

\[
x\in\operatorname{RCl}_{\mathcal K}(S).
\]

It is recoverably independent of \(S\) when

\[
x\notin\operatorname{RCl}_{\mathcal K}(S).
\]

This is not linear dependence unless a later realization theorem identifies \(\operatorname{RCl}\) with linear span.

## Definition GR3 — Recoverably Independent Family

A finite family \(B=\{b_1,\ldots,b_n\}\) is recoverably independent when for every \(i\),

\[
b_i\notin \operatorname{RCl}_{\mathcal K}(B\setminus\{b_i\}).
\]

Order may be retained separately by History even when the independence predicate is applied to the underlying family.

## Definition GR4 — Recoverable Generating Family

\(B\) generates a persistent closed structure \(P\) when

\[
P\subseteq \operatorname{RCl}_{\mathcal K}(B)
\]

and every formal distinction required by the declared invariant contract is recoverable from \(B\).

## Definition GR5 — Genesis Basis

A Genesis basis for \(P\) is a recoverably independent generating family for \(P\).

A basis is always relative to \(\mathcal K\). There is no context-free Genesis basis.

## Definition GR6 — Genesis Rank

If every minimal Genesis basis of \(P\) has the same finite cardinality \(n\), define

\[
\operatorname{rank}_{G,\mathcal K}(P)=n.
\]

If minimal bases exist but cardinalities differ, rank is **undefined** until additional exchange structure is proved.

If no finite Genesis basis exists, the finite-rank predicate fails.

## Lemma GRL1 — Counting Firewall

The number of visible labels does not determine Genesis rank.

### Proof
Visible labels are readout values. By Readout Noncreation and Same Endpoint / Different History, distinct formal states may share a label and one formal state may admit multiple labels across Resolution. Therefore label cardinality is not invariant under admissible change of Resolution and cannot define rank without an additional theorem. ∎

## Lemma GRL2 — History Nonpromotion

If History \(H\) is recoverably generated from an ordered relation \(A|B\), then the triple notation \((A,B,H)\) does not imply rank three.

### Proof
By hypothesis \(H\in\operatorname{RCl}_{\mathcal K}(\{A,B\})\). Hence \(H\) is dependent on \(\{A,B\}\) in the Genesis sense. Adding a dependent address to a generating family does not establish a larger minimal independent family. ∎

## Lemma GRL3 — Two-Role Nonpromotion

The Cradle \(A|B\) does not by itself imply complex rank two.

### Proof
The bar records boundary/order. Rank requires a realization in which \(A,B\) are independent coordinates over a typed scalar structure. Neither coordinate linearity nor scalar action follows from boundary syntax alone. ∎

## Proposition GRP1 — Rank Can Increase Only by Nonrecoverable Novelty

Suppose \(P'\) is obtained from \(P\) by an admissible operation. If every new formal address of \(P'\) lies in \(\operatorname{RCl}_{\mathcal K}(B)\) for some Genesis basis \(B\) of \(P\), then

\[
\operatorname{rank}_{G,\mathcal K}(P')\le |B|
\]

whenever the rank is defined.

Thus a rank increase requires at least one new recoverably independent distinction.

## Definition GR7 — Basis Equivalence

Two Genesis bases \(B,C\) of the same persistent object \(P\) are equivalent under \(\sim_P\) when there are admissible recovery maps

\[
F:B\rightsquigarrow C,\qquad G:C\rightsquigarrow B
\]

whose composites preserve the declared identity/history/provenance invariants of \(P\).

## Definition GR8 — Representation Formation

A representation witness of rank \(n\) is a typed map

\[
\Phi:(P,\mathcal K)\to (V,\Sigma)
\]

such that:
1. \(\operatorname{rank}_{G,\mathcal K}(P)=n\);
2. \(V\) has independently defined rank/dimension \(n\);
3. \(\Phi\) preserves the declared invariant contract;
4. \(\Phi\) has the required recovery witness on its image;
5. no target structure is imported upstream solely through \(\Phi\).

## Theorem GRT1 — Rank-First Representation Firewall

A claim \(P\cong\mathbb C^n\) is unauthorized unless a Genesis rank-\(n\) theorem or an equivalent source-native dimension theorem has already been proved.

### Proof
Without a rank theorem, selecting \(\mathbb C^n\) uses target dimension as source structure. This violates No Target Smuggling. ∎

## Definition GR9 — Genesis Automorphism

For a persistent closed object \(P\), define \(\operatorname{Aut}_G(P)\) as the class of invertible admissible endomorphisms preserving the complete declared Genesis invariant contract.

This definition becomes a group only after closure under composition, identity, and inverses is proved in the chosen realization.

## Theorem GRT2 — Group-Emergence Threshold

A pre-persistent path category need not admit a total group multiplication on states. After persistence closure, the automorphism question becomes lawful.

### Proof
Before closure, the native composition is partial History concatenation between matched endpoints. A group requires a single carrier with total multiplication and inverses. Persistence closure supplies a stable object on which invertible endomorphisms may be defined. It does not guarantee their existence or identify their group. ∎

## Corollary GRC1 — SU(n) Selection Protocol

To derive \(SU(n)\) from Genesis one must prove, in order:
1. Genesis rank \(n\);
2. a complex-linear realization;
3. a positive Hermitian invariant;
4. preservation of that invariant by admissible automorphisms;
5. determinant-one / orientation normalization;
6. generation of all of \(SU(n)\), not merely a subgroup.

Failure at any stage leaves the group label open.

## No-Go GRN1 — Color Count Is Not Rank

Six rainbow basin anchors do not imply rank six, rank three, or any \(SU(n)\).

## No-Go GRN2 — Sphere Dimension Is Not Fiber Rank

The dimension of an \(S^k\)-class traversal/history manifold does not imply a \(\mathbb C^k\) representation fiber.

## No-Go GRN3 — Path Length Is Not Rank

A history containing \(m\) transitions does not imply representation rank \(m\).

## Open Problem GRO1 — Exchange

Under what Genesis axioms do finite minimal bases have equal cardinality? A matroid-like exchange theorem is a candidate, not yet earned.

## Open Problem GRO2 — Closure Rank

Can T5 persistence closure create a new recoverably independent direction, or only stabilize distinctions already present upstream?

## Open Problem GRO3 — Hermitian Emergence

What Genesis-native invariant, if any, produces a positive Hermitian form after complex representation formation?

## Open Problem GRO4 — Determinant-One

What Genesis-native conservation law selects unit determinant rather than a general unitary phase?

## Open Problem GRO5 — Rank Two vs Rank Three

Does any T5 persistent closed chirality object have a source-native finite rank, and if so what is it?

