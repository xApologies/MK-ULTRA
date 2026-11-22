# ASTRAEUS — T5→T0 QMO BACK-CRAWL R26
## Reverse the full live model and constrain the update law from the finish line

**Date:** 2026-08-27

# Result

Working backward from T5 does produce a new closure.

The missing Problem-B event law is more constrained than the forward crawl could see.

The forward crawl gives:
`Cand(x)` = every update that is lawful *now*.

The backward crawl gives:
`Viab_5(x)` = every update/state from which at least one lawful path to a T5 recovery-saturated witnessed closure still exists.

Therefore the update may only come from:

\[
Cand_5(x)=Cand(x)\cap Viab_5(x).
\]

This is the first forward/backward recursive closure of the roadmap.

---

# T5 → T4

T5 is defined as bounded recovery saturation plus witnessed closure/normalization.

Therefore T4 cannot merely produce a state that is locally persistent.

It must produce a state/history from which a recovery-saturated bounded closure remains reachable.

So T5 imposes a backward **viability condition** on T4.

Define the T5 viability kernel:

`Viab_5`

as the set of T4 presentations admitting at least one lawful continuation into a T5 closed object while preserving the required invariant/provenance contract.

This is not a new force or primitive. It is the backward image of the already-fixed finish condition.

---

# T4 → T3

T4 judges persistence by recoverability under redistribution.

Therefore T3 must retain enough History to distinguish:
- a route that remains T5-viable;
- a route that destroys all T5-viable continuations.

Thus History is not merely archival. It is an input to future viability.

Backward requirement:
T3 may not quotient histories whose distinction changes T5 viability.

---

# T3 → T2

T3 histories require composable routes.

Therefore T2 must retain every route distinction needed to decide future recovery/viability.

A T2 coarse quotient is illegal if it identifies routes with different T5 closure consequences.

---

# T2 → T1

T2 routes do not all contribute equally to downstream closure.

T1 preference is therefore constrained backward:

a preference rule cannot rank a nonviable route above all viable routes if the roadmap requires eventual T5 closure, unless the system is allowed to fail.

This does not yet create a unique preference function.

It gives a closure-compatibility condition on preference.

---

# T1 → T0

T1 can only rank transformations T0 already admits.

Therefore T0 admissibility must contain at least one T5-viable continuation at every state claimed to lie on a successful T0→T5 realization.

If:
`Adm_T0(x) ∩ Viab_5(x)=empty`,
then x is a dead state for the roadmap.

This gives a backward falsification test for T0 seeds.

---

# Backward Necessity Chain

The full reverse dependency is now:

`T5 recovery-saturated closure`
requires
`T4 persistent viable candidates`
requires
`T3 histories preserving viability distinctions`
requires
`T2 composable viable routes`
requires
`T1 preference compatible with viable continuation`
requires
`T0 at least one admissible viable transformation`.

This is a theorem about the roadmap's dependency structure, not a claim that later physics causes earlier mathematics.

---

# Problem B changes again

Forward-only:

`Cand(x)`.

Backward-only:

`Viab_5(x)`.

Recursive forward/backward closure:

\[
\boxed{Cand_5(x)=Cand(x)\cap Viab_5(x)}.
\]

Therefore Problem B2 is no longer:

"choose from every lawful candidate."

It is:

> choose from the candidates that are lawful now **and** remain compatible with eventual T5 closure.

This is much stronger.

---

# Can this close B2?

Potentially.

If:

\[
|Cand_5(x)|=1,
\]

then the update is forced by simultaneous forward admissibility and backward closure.

No additional event axiom is needed at that state.

If:

\[
|Cand_5(x)|>1,
\]

the Choice-Gap survives and an event/choice law is still missing.

So the correct next computation is no longer another abstract definition.

It is:

\[
\boxed{\text{Compute }Cand_5(x)\text{ in the concrete finite model and test singleton closure.}}
\]

That is an executable question.

---

# Important interpretation

This is exactly where recursion becomes useful without becoming circular.

T5 is not being used as a cause acting backward in time.

The fixed T5 contract is used as a **mathematical boundary condition**.

Forward laws say what can happen.

Backward closure says which of those possibilities can belong to a complete T0→T5 solution.

The intersection can force the path.

That is ordinary constraint closure, not retrocausality.

---

# Final verdict

**NEW CLOSURE EARNED.**

Forward:
`Cand(x)`.

Backward:
`Viab_5(x)`.

Closed recursive candidate set:
`Cand_5(x)=Cand(x)∩Viab_5(x)`.

Problem B2 remains open in general, but it may close *without a new axiom* if the forward/backward intersection is singleton throughout the concrete successful trajectory.

The next attack should compute exactly that.
