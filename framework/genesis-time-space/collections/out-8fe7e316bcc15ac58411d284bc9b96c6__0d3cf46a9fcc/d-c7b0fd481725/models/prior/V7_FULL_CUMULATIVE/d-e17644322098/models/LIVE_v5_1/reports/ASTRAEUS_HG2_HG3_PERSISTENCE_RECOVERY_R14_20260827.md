# ASTRAEUS — HG2 / HG3 CONTINUATION HACK R14
## Persistence as Recoverable Self-Return

**Date:** 2026-08-27
**Scope:** Genesis mathematics from T3 through T5 only
**Hard boundary:** no post-T5 mathematics is used.
**Starting point:** HG1 is conditionally closed by Address-Preserving Self-Inheritance.

# Final verdict

**HG2 CLOSES AT THE STRUCTURAL LAW LEVEL.**

The clean T3→T4 persistence law is:

> A T3 identity is T4-persistent relative to an admitted redistribution if, after that redistribution, there exists an admissible recovery History returning the result to the same declared identity class with required provenance intact.

Persistence is therefore **recoverable self-return under redistribution**, not coordinate immobility.

This also sharpens HG3:

> T5 is the closure regime in which the recoverable-self-return law becomes closed over the full admitted internal redistribution family of a bounded persistent domain.

The exact physical/native redistribution generator remains source-dependent, but the mathematics of persistence itself is now typed.

---

# 1. T3 starting object

Let `C3` denote the T3 History category.

Objects:
`x,y,z,...`

Morphisms:
ordered admissible histories

`h : x -> y`.

Composition:
`g ∘ h : x -> z`

when endpoints match.

Identity History:
`id_x : x -> x`.

No inverse is assumed.

Let `~_I` denote equivalence relative to the declared identity contract `I`.

This may preserve:
- carrier identity;
- chirality;
- required History/provenance;
- declared Resolution-independent distinctions.

It is not ordinary equality unless separately proved.

---

# 2. Redistribution as a T3 morphism family

A redistribution is not introduced as a new species of mathematics.

It is a distinguished class of admissible T3 histories.

For each object x, let:

`Red(x)`

be the declared family of admissible redistribution histories

`r : x -> y`.

This is the only source-specific input HG2 still needs: which T3 histories count as redistributions in the active T4 scope.

No metric, energy, time coordinate, or downstream physics is required.

---

# 3. Recovery

## Definition R14.D1 — Recovery History

Given a redistribution

`r : x -> y`,

a recovery History for r is an admissible T3 History

`k : y -> x'`

such that

`x' ~_I x`.

The composite

`k ∘ r : x -> x'`

is a **recoverable self-return**.

Important:
`k` need not be an inverse of `r`.

Thus:

`recovery != inversion`.

This agrees with the Fusion/provenance result that noninjective structure may remain recoverable through witness data.

---

# 4. Persistence predicate

## Definition R14.D2 — T4 Persistence

For object x and redistribution r in `Red(x)`:

`Pers_I(x;r)`

holds iff there exists an admissible recovery History k such that:

`k ∘ r : x -> x'`

with

`x' ~_I x`.

Equivalently:

`r` is persistence-compatible with x when x can recover its declared identity after r.

This is the first exact T4 predicate.

---

# 5. Why this is the minimal novelty from T3

T3 already has:
- objects;
- admissible histories;
- composition;
- identity histories;
- provenance.

To obtain persistence asymmetry, the only additional data required are:

1. identify which histories count as redistributions;
2. ask whether recovery to the same identity class exists.

No new algebraic operation is necessary.

Thus:

`Δ_34 = distinguished redistribution family + recovery criterion`.

## Theorem R14.1 — Minimal T4 Novelty

T4 persistence can be typed entirely inside the T3 History calculus plus a distinguished redistribution family and identity-equivalence contract.

### Verdict
**CLOSED.**

This is substantially cleaner than introducing a separate persistence scalar.

---

# 6. Persistence asymmetry

Two objects x and y may face the same class of admissible redistribution but differ in recovery.

For example:

`Pers_I(x;r)=true`
while
`Pers_I(y;r)=false`.

Therefore T4 asymmetry is simply asymmetry of recoverable self-return.

## Definition R14.D3 — Recovery Set

Define:

`Rec_I(x) = { r in Red(x) : Pers_I(x;r) }`.

Then persistence comparison can be made by set inclusion:

`x <=_P y`
iff
`Rec_I(x) ⊆ Rec_I(y)`,

after the redistribution domains have been made comparable.

No numeric persistence score is required.

## Theorem R14.2 — Persistence Preorder

Under a common comparable redistribution family, subset inclusion of recovery sets is reflexive and transitive.

Therefore T4 admits an order-theoretic persistence structure without assigning arbitrary numbers.

### Verdict
**CLOSED.**

This is simple, elegant, and sufficient for "persistence asymmetry."

---

# 7. Strict and witness-preserving recovery

Recovery must preserve the declared identity contract.

There are two forms.

## Strict recovery

`k ∘ r(x) = x`

at the formal carrier level.

## Witness-preserving recovery

`k ∘ r(x) = x'`

with

`x' ~_I x`

because the witness/provenance layer certifies the same persistent identity.

The second is more general.

## Theorem R14.3 — Strict Recovery Implies Witnessed Recovery

Every strict recovery is an I-recovery whenever equality implies I-equivalence.

The converse need not hold.

### Verdict
**CLOSED.**

---

# 8. Recovery does not erase History

A recovered object may return to the same identity class while retaining the fact that redistribution occurred.

Thus:

`x --r--> y --k--> x' ~_I x`

does not imply the composite History is the empty History.

The recovery loop:

`ℓ = k ∘ r`

remains part of provenance when the identity contract retains History.

## Theorem R14.4 — Persistent Return Without Historical Erasure

Identity recovery and History erasure are distinct.

### Verdict
**CLOSED.**

This is critical: persistence is compatible with change.

---

# 9. T4 persistence witness

A persistence witness for x over a redistribution family `R` is:

`W_P(x;R,I) = { (r,k_r,w_r) : r in R_recovered }`

where:
- r is a redistribution;
- `k_r` is a recovery History;
- `w_r` certifies `k_r ∘ r(x) ~_I x`.

The witness may be distributed across local fragments if global recovery is reconstructible.

## Definition R14.D4 — T4 Persistent Candidate

x is a T4 persistent candidate over test family `R_test` iff:

`R_test ⊆ Rec_I(x)`.

This makes the stage explicitly scope-dependent.

---

# 10. T4 near closure

T4 should not require recovery from every conceivable redistribution.

That would already be full closure.

Instead T4 is **partial recovery closure**:

there exists a nontrivial declared family

`R_test != ∅`

for which x is recoverable.

Different objects may support different recovery sets.

This produces persistence asymmetry.

## Theorem R14.5 — T4 Is Partial Recovery Closure

T4 can display persistence asymmetry whenever recovery sets are nonempty and nonidentical across objects, without requiring total closure.

### Verdict
**CLOSED.**

This exactly distinguishes T4 from T5.

---

# 11. T5 as saturation of recovery

Now define the internal redistribution family of a bounded candidate domain B:

`Red_int(B)`.

This contains every redistribution admitted by the T5 internal operator contract and remaining inside the declared scope.

## Definition R14.D5 — Recovery Saturation

B is recovery-saturated relative to I iff for every:

`x in B`
and every
`r in Red_int(x)`,

there exists a recovery History k such that:

`k ∘ r(x) ~_I x`

and all required provenance remains recoverable.

Symbolically:

`forall x in B, Red_int(x) ⊆ Rec_I(x)`.

This is the natural full-closure version of the T4 predicate.

---

# 12. T5 persistence closure

## Definition R14.D6 — T5 Persistent Domain

A T5 persistent domain is a scoped nonempty B satisfying:

1. **bounded scope** — B has a declared locality boundary;
2. **internal forward closure** — admitted internal redistributions remain within the T5 carrier up to declared equivalence;
3. **recovery saturation** — every admitted internal redistribution is recoverable to the same identity class;
4. **History retention** — required closure/recovery histories remain recoverable;
5. **witness closure** — required local/distributed witnesses jointly reconstruct persistent identity;
6. **operator closure** — applying admitted internal operations requires no object outside the declared T5 domain.

## Theorem R14.6 — T5 Recovery-Closure Theorem

A domain satisfying R14.D6 is closed under the T4 persistence law: every admitted internal redistribution preserves persistent identity by recoverable self-return.

### Verdict
**CLOSED BY DEFINITION + T3 COMPOSITION.**

This is the strongest T4→T5 closure obtained so far.

---

# 13. HG2 verdict

HG2 asked:

> What exact invariant and redistribution test converts History into persistence asymmetry?

Answer:

The invariant is not necessarily a scalar.

It is the declared identity contract I.

The test is:

`r is persistence-compatible with x`
iff
`there exists k with k ∘ r(x) ~_I x`.

Thus persistence asymmetry is the asymmetry of recovery sets.

## HG2
**CLOSED AT THE GENESIS MATHEMATICAL LAW LEVEL.**

Still source-dependent:
- which histories are classified as redistributions;
- which distinctions belong to I in a specific realization.

Those are parameters of the law, not missing mathematical species.

---

# 14. HG3 refinement

HG3 asked:

> Which T4 distinctions become one T5 carrier state, which survive in witness, and which are discarded?

Recovery saturation gives a clean criterion for the first part:

Two T4 presentations may occupy one T5 persistent identity class only when their mutual relation is compatible with the T5 identity contract and every identity-required distinction is either:
- mutually recoverable;
- retained in witness;
- or explicitly excluded from I.

This induces a persistent equivalence candidate:

`x ≈_5 y`

iff:
1. x and y lie in the same recovery-saturated persistent domain;
2. x is recoverable to y and y is recoverable to x under admitted T5 histories, up to I;
3. all noncollapsed I-required History/provenance is retained by W5.

## Theorem R14.7 — Mutual Recovery Equivalence

If recovery witnesses compose and I-equivalence is an equivalence relation, mutual T5 recoverability defines an equivalence relation on persistent presentations.

### Proof
Reflexive: identity History.
Symmetric: required by mutual recoverability.
Transitive: compose recovery histories.

### Verdict
**CLOSED RELATIVE TO COMPOSABLE RECOVERY WITNESSES.**

This gives HG3 its first mathematically generated quotient relation rather than an arbitrary one.

---

# 15. T5 quotient

Define:

`Q5 = B / ≈_5`.

Each equivalence class is one persistent carrier identity at the chosen T5 Resolution/identity contract.

Attach witness:

`W5([x])`

containing every History/provenance distinction required by I but not represented explicitly in the quotient carrier.

Then:

`P5 = (Q5,W5,I)`.

## Theorem R14.8 — Canonical Witnessed Quotient Candidate

Relative to a fixed recovery-saturated domain B, identity contract I, and complete recovery witness system, the quotient by mutual recoverability is canonical up to isomorphism of the equivalence classes.

### Verdict
**NEW CONDITIONAL CLOSURE.**

The word "canonical" is relative to the declared B, I, and recovery system.

---

# 16. What may be strictly discarded

A distinction d may be strictly discarded at T5 only if:

`d notin I`

and no theorem downstream of the roadmap requires d as part of persistent identity.

If d belongs to I but is absent from Q5, it must survive in W5.

## Theorem R14.9 — Persistent Information Partition

Every upstream distinction relevant to T5 must fall into exactly one declared class:

A. represented in carrier Q5;
B. omitted from carrier but retained/recoverable in W5;
C. explicitly outside the identity contract I.

No fourth "silently erased but later usable" class is admissible.

### Verdict
**CLOSED.**

---

# 17. The T4→T5 transition becomes elegant

We can now write:

`T3`
`History category`

`-> T4`
`recovery relation under selected redistributions`

`-> T5`
`recovery saturation + quotient by mutual recoverability + witness retention`.

That is:

`History`
`-> recoverability`
`-> persistence`.

Not:
`History -> arbitrary persistence scalar -> arbitrary closure`.

This is the cleanest roadmap interpretation so far.

---

# 18. Relation to dynamic recursion

Suppose a local system repeatedly undergoes:

`x_0 --r_1--> y_1 --k_1--> x_1 ~_I x_0`
`x_1 --r_2--> y_2 --k_2--> x_2 ~_I x_1`
`...`

Then the system can change continually while preserving persistent identity through repeated recoverable self-return.

Thus persistence is compatible with dynamic recursion.

## Theorem R14.10 — Dynamic Persistence

A recursively changing system can remain one persistent identity when every admitted update step is followed or accompanied by an admissible recovery path into the same identity class.

### Verdict
**CLOSED.**

This matches the user's conceptual requirement that the chirality block can recursively update without losing identity.

---

# 19. Local versus global recovery

Recovery need not happen instantaneously or within one tile.

If witnesses are distributed, a local redistribution may alter one site while recovery is realized through compatible neighboring histories.

Therefore global persistence can emerge from local recovery relations.

This gives a candidate update architecture:

`local redistribution`
`-> neighbor-compatible recovery propagation`
`-> global witness-compatible identity return`.

### Verdict
**ARCHITECTURAL CONSEQUENCE; EXACT TILE UPDATE REMAINS OPEN.**

---

# 20. Recovery loops and recurrence

A recovery composite:

`ℓ_r = k_r ∘ r : x -> x' ~_I x`

is an identity-returning loop up to I-equivalence.

Different loops may retain different History.

Thus T4/T5 naturally generate a family of identity-returning cycles.

No group is assumed because:
- inverses need not exist;
- two loops with the same endpoint need not be equivalent.

### Verdict
**CLOSED PRE-GROUP LOOP STRUCTURE.**

---

# 21. Persistence order

For comparable states x,y:

`x <=_P y`
iff
`Rec_I(x) ⊆ Rec_I(y)`.

If strict inclusion holds:

`x <_P y`.

This supplies a source-neutral meaning of "more persistent":

y can recover from every redistribution x can, and at least one more.

No scalarization is required.

### Verdict
**CLOSED.**

---

# 22. Persistence classes

Define:

`x ≡_P y`
iff
`Rec_I(x)=Rec_I(y)`.

This is an equivalence relation.

The quotient by persistence profile:

`T4 / ≡_P`

classifies states by recovery capability rather than appearance.

### Verdict
**NEW CLOSURE.**

This may become useful for T4 basin structure.

---

# 23. Persistence basin candidate

A T4 persistence basin can be defined as a connected/reachable family of T3 states sharing or monotonically increasing compatible recovery profiles under the declared routing structure.

This is a candidate structural basin definition.

It avoids treating "basin" as merely a color label.

### Verdict
**CANDIDATE; CONNECTIVITY/ORDER CONDITIONS NEED FINALIZATION.**

---

# 24. Exact remaining HG3 debt

HG3 is no longer "what could T5 possibly be?"

It is now narrowed to:

1. What is the exact T5 internal redistribution family `Red_int(B)`?
2. What exact distinctions belong to identity contract `I5`?
3. What boundary defines the maximal/minimal recovery-saturated B selected by the pipeline?

Once those three are supplied, the quotient:

`B / ≈_5`

and witness partition follow mechanically.

So HG3 is now mostly **parameter selection**, not missing mathematical form.

---

# 25. Textbook promotion candidates

The following results are suitable for Genesis textbook promotion because they close within the roadmap domain:

1. **Persistence as Recoverable Self-Return**.
2. **Recovery does not require inversion**.
3. **Recovery Set** `Rec_I(x)`.
4. **Persistence preorder by recovery-set inclusion**.
5. **T4 Partial Recovery Closure**.
6. **T5 Recovery Saturation**.
7. **Mutual Recovery Equivalence** `≈_5`.
8. **Witnessed T5 Quotient** `P5=(B/≈_5,W5,I)`.
9. **Persistent Information Partition**.
10. **Dynamic Persistence Theorem**.
11. **Persistence-profile equivalence**.

The exact redistribution generators and identity contract remain explicit interface parameters.

---

# 26. Final roadmap state after R14

## HG1
Cradle -> 2×2 chirality carrier:
**CLOSED CONDITIONALLY** on Address-Preserving Self-Inheritance.

## T0
Admissibility:
**CLOSED.**

## T1
Directional preference:
**CLOSED.**

## T2
Reachability geometry:
**CLOSED.**

## T3
Retained History:
**CLOSED.**

## HG2 / T4
Persistence asymmetry:
**CLOSED AS RECOVERABLE SELF-RETURN UNDER REDISTRIBUTION.**

## HG3 / T5
Full persistence closure:
**MATHEMATICAL FORM CONDITIONALLY CLOSED** as recovery saturation plus quotient by mutual recoverability plus witness retention.

Still open:
- exact T5 redistribution family;
- exact T5 identity contract;
- exact selected persistent boundary/domain.

No downstream target was used.

---

# 27. Strongest compact statement

\[
\boxed{
\text{Persistence is recoverability of identity under admissible change.}
}
\]

T4 occurs when that recoverability is partial and asymmetric.

T5 occurs when it becomes saturated over the admitted internal redistribution family of a bounded domain, after which mutually recoverable presentations can be quotiented into one persistent carrier identity while required History survives in witness.

This is the first fully coherent Genesis-native T3→T5 persistence mechanism.
