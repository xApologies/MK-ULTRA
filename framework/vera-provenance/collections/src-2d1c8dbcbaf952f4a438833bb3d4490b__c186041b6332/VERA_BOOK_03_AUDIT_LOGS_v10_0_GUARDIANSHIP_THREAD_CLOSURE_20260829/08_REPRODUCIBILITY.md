# Chapter 8: Reproducibility

## Primitive distinction

The subject of **Reproducibility** is treated as mathematical structure, not bookkeeping. Let a decorated occurrence be
\[
\widetilde x=(x,H_x,W_x,A_x),
\]
where \(x\) is carrier content, \(H_x\) retained history, \(W_x\) witness data, and \(A_x\) authority/context. The tuple is richer than the carrier. Fields may be forgotten only after the active theory proves the forgotten distinctions irrelevant.

A transition is written
\[
\widetilde x \xrightarrow{f,w_f} \widetilde y.
\]
The map \(f\) may be partial. Undefinedness means the present mathematics does not license an output. The witness records why the transition is admissible.

## Definition 8.1 - admissibility

A proposed transition is admissible when its source and target are typed, every required premise is available under the active authority, the invariant contract is preserved, a sufficient witness exists or is reconstructible, and the result remains inside the declared closure domain.

This separates *possible*, *admissible*, and *realized*. Collapsing these stages can silently turn an option into a fact.

## Equivalence layers

Distinguish
\[
\widetilde x\sim_F\widetilde y,\qquad x\sim_K y,\qquad \rho_R(x)=\rho_R(y).
\]
Formal equivalence may preserve history, authority, witnesses, and invariants. Carrier equivalence forgets decoration. Readout equivalence may forget still more. Under the declared projections,
\[
\widetilde x\sim_F\widetilde y\Rightarrow x\sim_Ky\Rightarrow \rho_R(x)=\rho_R(y),
\]
while converses require additional hypotheses.

## Proposition 8.1 - separation

If two admissible occurrences have the same carrier but differ in contract-relevant decoration, carrier-only storage is insufficient to distinguish them.

**Proof.** The forgetful projection \(p(\widetilde x)=x\) maps two contract-distinct inputs to one image. It is non-injective on the relevant quotient. No procedure receiving only the image can determine which input occurred without additional information. ∎

## Composition

For
\[
\widetilde x\xrightarrow{f}\widetilde y\xrightarrow{g}\widetilde z,
\]
the composite \(g\circ f\) is licensed only when the output obligations of \(f\) satisfy the input obligations of \(g\). A composite witness contains both stage witnesses and any compatibility certificate required at their interface.

Endpoint equality is weaker than compositional interchangeability. Equal carriers may enable different future maps when their retained decoration differs.

## Failure taxonomy

- **type failure:** source outside the map domain;
- **witness failure:** evidence insufficient;
- **authority failure:** source exists but lacks authority for this role;
- **history loss:** required distinction projected away;
- **closure failure:** result leaves the admitted domain;
- **alias failure:** names and identities confused;
- **silent repair:** data changed without a recorded transformation.

Unresolved is not false. Rejected is not unavailable. These statuses carry different information.

## Counterexample pattern

Let paths \(P\) and \(Q\) begin at one occurrence and terminate at the same carrier \(v\), but record different intermediate events. If a later admissibility rule depends on those events, the futures differ although the endpoint agrees. Endpoint-only state is therefore insufficient.

## Theorem 8.2 - erased distinctions cannot be internally recovered

Let \(q:X\to Q\) be a quotient. If \(x_1,x_2\) belong to different contract-relevant classes but \(q(x_1)=q(x_2)\), no function \(r:Q\to X\) can satisfy \(r(q(x_i))=x_i\) for both \(i=1,2\).

**Proof.** The common quotient value has one image under a function and cannot be sent simultaneously to two distinct required values. ∎

## Consequence for Audit Logs

Preserve distinctions until a theorem licenses their quotient; preserve witnesses until reconstruction no longer depends on them; represent uncertainty as unresolved structure rather than filling a gap with an invented selector.

## Audit questions

1. What is the carrier?
2. Which decoration is contract-relevant?
3. What produced this occurrence?
4. Which witness establishes the claim?
5. Which equivalence is active?
6. What was intentionally forgotten?
7. Can the object be reconstructed?
8. Which downstream claims depend on the distinction?
