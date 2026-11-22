# GENESIS — 03 LEMMAS

# Lemma L1

## Scope Separation

### Statement

If c₁ and c₂ have no declared translation witness, then Denote(s,c₁) and Denote(s,c₂) cannot be identified by Genesis solely because the surface symbol s matches.

### Proof

By A3, surface-symbol equality is insufficient. Identity would require A4. Therefore the identification is unavailable.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L2

## Typed Composition

### Statement

If g₁:A→B and g₂:B→C are admitted relation records and AdmComp(g₂,g₁) holds, then g₂∘_Gg₁ is typed A→C.

### Proof

A2 supplies endpoint types. A9 supplies the extra scope/status/witness compatibility. The composite therefore inherits source A and target C on the admitted domain.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L3

## Graph Route Noninflation

### Statement

A path of registered relationships does not by itself establish identity, causation, realization, or mathematical composition.

### Proof

Each stronger relation requires a specific typed rule under A2/A4/A9/A13. Reachability supplies none of those witnesses.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L4

## Copula Firewall

### Statement

A Genesis predicative statement does not imply mathematical equality merely because its English gloss contains “is”.

### Proof

Genesis has no simple universal “is”; qualities are expressed by relation, inheritance, persistence, closure, or basin/expression constructions. A4 blocks equality without an identity witness.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L5

## Possession as Boundary Inclusion

### Statement

For a language-level possession phrase x-sha y, the first Genesis semantic record is DA(y,B_x), not Owns(x,y).

### Proof

This is exactly A5. Any ownership interpretation is an additional layer witness under A13.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L6

## Aspect Noncollapse

### Statement

No expression marked -ma, -ru, -ta, or -nai may be silently reclassified as another aspect.

### Proof

A6 keeps the four labels distinct absent a transition rule.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L7

## Root-Family Nonidentity

### Statement

If roots/words share a root family, Genesis does not infer their identity.

### Proof

D2 defines family as semantic neighborhood; A4 requires an identity witness. Therefore family membership is not identity.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L8

## Readout Aliasing

### Statement

If q_R is not injective, there exist distinct formal x,y with identical observational identity at R.

### Proof

Noninjectivity gives x≠y with q_R(x)=q_R(y). By D12 they are observationally identical while remaining formally distinct.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L9

## Readout Persistence

### Statement

If a formal distinction is merged by q_R, the distinction may remain present in the formal object even though it is unreadable at R.

### Proof

A11 states that readout merges rather than destroys formal distinctions. This is the Resolution & Readout result restated in Genesis terms.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L10

## Bandwidth/Resolution Separation

### Statement

A feature may be formally present but unreadable, or readable while a new transformation is bandwidth-forbidden.

### Proof

A11 concerns distinguishability; A12 concerns available transformation capacity. Neither implies the other.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L11

## Same Endpoint / Different History

### Statement

Two histories may have the same structural/readable endpoint while remaining distinct Genesis histories.

### Proof

A10 retains history unless a history equivalence identifies it. Fusion R09/R10 supplies explicit models of this phenomenon.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L12

## History Concatenation

### Statement

Admissible Genesis paths concatenate associatively at the word level.

### Proof

Sequence concatenation is associative. A9 is required at the seam; where it passes, (γ₃γ₂)γ₁ and γ₃(γ₂γ₁) are the same ordered word.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L13

## Identity-Witness Transport

### Statement

If an admissible path carries an identity witness chain whose local compositions close, formal identity persists along the path.

### Proof

By D19 each stage has a witness. Composition of the witnesses gives an endpoint witness under the model’s identity composition rule, satisfying D20.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L14

## Quotient Descent Criterion

### Statement

For a quotient q:X→X/~ and a map f:X→Y, a unique map f̄:X/~→Y with f=f̄∘q exists exactly when f is constant on equivalence classes.

### Proof

This is the standard quotient universal property. A14 imports it as the ordinary descent criterion where the target is an ordinary set/object.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L15

## Equivariant Descent Criterion

### Statement

When the quotient is by a group action and the target carries a compatible representation, equivariance—not literal equality—can be the correct descent law.

### Proof

Standard associated-bundle descent shows that equivariant data defines quotient/section data. A14 therefore must record the target equivalence type rather than demand literal equality universally.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L16

## Layer Nonpromotion

### Statement

A well-formed Genesis phrase with no mathematical layer witness has no licensed mathematical operator solely from grammar.

### Proof

A13 separates syntax/semantics from mathematics; A8 separately requires an operator signature.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L17

## Fusion Carrier/Witness Separation

### Statement

The pushout/colimit carrier of a Fusion diagram does not uniquely determine its seam/provenance/history witness.

### Proof

A15 stores witness separately; Fusion R05/R06/R09/R10 exhibits carriers with additional recoverability/history data.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L18

## Carrier Confluence / History Nonconfluence

### Statement

For a fixed compatible finite Fusion diagram, legal execution orders can yield canonically isomorphic carriers while retaining distinct history words.

### Proof

Fusion R10 proves carrier colimit confluence; A10 retains execution history absent a quotient identifying the words.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L19

## Boundary-Reference Relativity

### Statement

Changing speaker/listener boundary context may change KA/SA/A labeling while preserving the referenced formal identity.

### Proof

D13 makes demonstrative label context-relative; A4 allows identity to be preserved by a separate witness. Therefore reference class can change without identity change.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L20

## Failure Preservation

### Statement

A failed branch remains a Genesis mathematical record and cannot be replaced by absence.

### Proof

A6 makes -nai/failed a first-class aspect; A16 retains provenance and parents. Thus failure is an addressable result.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L21

## Representation Nonexhaustion

### Statement

A successful realization of an identity into one representation does not prove that representation exhausts whole-object identity.

### Proof

A4 separates identity from representation; A13 requires a layer witness only for the claimed representation. No surjectivity/exhaustiveness follows.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

# Lemma L22

## No Unwitnessed Target Rank

### Statement

If a target realization requires k independent distinctions and the source plus realization witness determines fewer than k, Genesis cannot certify the k-fold structure as source-derived.

### Proof

A11 forbids readout creation and A18 forbids target smuggling. Without a witness supplying the missing distinctions, the source-derived claim fails.

∎

### Consequence

This result may be reused only within the hypotheses and equivalence type stated above.

### Status

**PROVED IN GENESIS v0.1 FROM DECLARED AXIOMS / SUPPORT RESULTS.**

---

