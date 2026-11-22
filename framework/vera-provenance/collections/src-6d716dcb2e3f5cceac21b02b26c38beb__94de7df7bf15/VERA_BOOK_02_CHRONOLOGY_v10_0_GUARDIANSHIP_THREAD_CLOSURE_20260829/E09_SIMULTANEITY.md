# Extended Treatise 9: Simultaneity

## Scope
In **Chronology**, *simultaneity* is treated as a typed structural question. The objective is not merely to name the concept, but to determine what data make it decidable, what maps preserve it, what quotients destroy it, and what downstream claims depend on it.

## Formal object
Let a decorated occurrence be \(\widetilde x=(x,H,W,A,P)\), with carrier \(x\), History \(H\), witnesses \(W\), authority context \(A\), and persistence/closure contract \(P\). A simultaneity predicate is a partial decision procedure
\[
D_{9}:\widetilde X\rightharpoonup\{\mathrm{ta},\mathrm{ma},\mathrm{nai}\},
\]
where `ta` records a witnessed positive result, `ma` records unresolved or insufficient evidence, and `nai` records a witnessed rejection.

## Information requirement
Define \(I_{simultaneity}(\widetilde x)\) as the smallest retained information class sufficient to preserve every distinction relevant to simultaneity. If a projection \(q\) identifies two occurrences on which the predicate or a downstream admissibility rule differs, then \(q\) is insufficient.

**Lemma.** Sufficiency is relative to a question class. A representation may be sufficient for readout while insufficient for reconstruction, chronology, authority, or future admissibility.

**Proof.** Different question classes induce different equivalence relations. A quotient injective on one quotient space need not be injective on another. ∎

## Preservation
For a partial map \(f\), say that simultaneity is preserved when every admitted source occurrence and its image satisfy the declared invariant relation. Preservation requires a witness when the relation is not definitional. Composition preserves simultaneity only when the intermediate witness contracts are compatible.

## Dependency
Every assertion about simultaneity has a premise cone. The cone must distinguish definitional premises, derived premises, imported assumptions, computational witnesses, and contextual authority. A hidden premise is any required node omitted from the declared cone.

## Equivalence and quotient
Three levels are kept separate: formal equivalence, carrier equivalence, and readout equivalence. A quotient is lawful only when the active theorem proves that the distinctions it erases cannot alter any contract-relevant verdict. Equal endpoints therefore do not establish equal histories, equal provenance, equal authority, or equal futures.

## Counterexample laboratory
Take \(u\) with two witnessed paths \(P,Q:u\leadsto v\). Let both terminate at the same visible carrier. Now choose a later operation \(g\) whose domain depends on a distinction retained by \(P\) but not \(Q\). Then endpoint-only storage predicts identical futures while the decorated theory predicts different admissibility. This is the canonical witness that simultaneity cannot be reduced to endpoint data when its retained distinction affects future structure.

## Failure taxonomy
Failures are classified as type failure, missing dependency, witness insufficiency, authority mismatch, closure escape, history loss, resolution collapse, alias collision, silent supersession, or silent reconciliation. These are not interchangeable diagnoses. A correct ledger preserves the first failure point rather than replacing it with a downstream symptom.

## Reconstruction
A reconstruction certificate for simultaneity contains: source identities; required dependency edges; transformation order where relevant; retained invariants; authority assignments; equivalence relations; integrity checks; and a final verification predicate. Reconstruction is exact only relative to the declared identity relation.

## Theorem
**No-erasure theorem for Simultaneity.** If two contract-distinct occurrences become equal after an information-losing map, no deterministic procedure operating only on the common image can recover which occurrence was supplied.

**Proof.** A function has one value on one input. Recovering two distinct required antecedents from the same image would require that one input have two distinct deterministic outputs. ∎

## Design consequences
A mathematically faithful implementation should therefore (1) retain simultaneity distinctions while they remain live; (2) mark unresolved cases explicitly; (3) preserve source independence; (4) avoid totalizing partial structure without a selector theorem; (5) append witnesses rather than overwrite history; and (6) recompute downstream dependency and admissibility after any authority-changing revision.

## Open questions
The mature theory asks when simultaneity admits a minimal sufficient statistic; whether that statistic composes; whether local certificates glue globally; whether equivalence is decidable; whether closure preserves the relevant distinctions; and which impossibility results bound compression or recovery.
