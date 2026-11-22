# R05 — Counterexample Ledger

## C5-01 — Literal duplicate-empty-set model

Suppose one writes two literal set values `emptyset_A` and `emptyset_B` and requires

\[
\varnothing_A\neq\varnothing_B
\]

while both are empty sets. In ordinary extensional set theory, any two sets with no members are equal. Therefore this cannot supply address distinction.

**Ruling:** FAILED. Distinction belongs in address tags, not in the empty-set value.

---

## C5-02 — Singleton-collapse substitution

The expression

\[
\{\varnothing,\varnothing\}=\{\varnothing\}
\]

is true because duplicate elements do not multiply in a set. But it destroys the source-address distinction and supplies no interface maps, no shared carrier, no chirality placement, no gluing witness, and no provenance.

**Ruling:** REJECTED AS FUSION MODEL. It is ordinary extensional set reduction.

---

## C5-03 — Pair without identification

The ordered pair

\[
(a_\star,b_\star)
\]

or singleton relation

\[
\{(a_\star,b_\star)\}
\]

is nonempty and perfectly represents a relation between null addresses. But the two addresses remain distinct.

**Ruling:** VALID PRE-FUSION RELATION; INSUFFICIENT AS FUSED CARRIER.

---

## C5-04 — Graph edge without quotient

A graph edge joining the two null nodes records contact/adjacency, but it does not identify the endpoints. Thus it models the R01 placement condition more naturally than the Fusion result itself.

**Ruling:** VALID CONTACT MODEL; NOT THE CURRENT FUSION OPERATOR.

---

## C5-05 — Incompatible-label pushout attempt

Let the selected source labels be

\[
\lambda_A(a_\star)=N,
\qquad
\lambda_B(b_\star)=E.
\]

Then no label-preserving interface object `J` can map its one point simultaneously to both selected loci while preserving a single state label. Equivalently, a descended `lambda_Q(q)` would be forced to equal both `N` and `E`.

**Ruling:** FAILS IN THE LABELED CATEGORY. This formalizes the R01 typed-interface counterexample.

---

## C5-06 — Bare unlabeled quotient

If labels are erased before quotienting, one may identify the selected points even when their original states were incompatible. The resulting carrier exists as a set, but the operation no longer certifies a state-consistent Fusion interface.

**Ruling:** MATHEMATICAL QUOTIENT EXISTS; TYPED FUSION FAILS.

---

## C5-07 — Quantum vocabulary substituted for interface algebra

Calling the relation "entanglement" or the quotient "superposition" supplies neither the address distinction nor the pushout proof.

**Ruling:** TYPE ERROR under R03/R04.

---
