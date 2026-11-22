# ASTRAEUS — EXECUTION RUN R17→R21
## Minimal Four-Address Cradle: Roadmap Execution Until Failure

**Date:** 2026-08-27  
**Roadmap basis:** Post-R16 execution roadmap.  
**Finite realization:** White grid `G7={k/7 : k=0,...,7}`, four second-order Cradle addresses, square adjacency by one-coordinate difference, nonzero transfer increments `δ=m/7`.

# Verdict

**R17 PASS. R18 DIAGNOSTIC PASS. R19 PASS. R20 PASS. R21 FAILS CLEANLY.**

The current conservative local kernel is exactly reversible on every admissible internal edge transfer. Consequently every admissible redistribution has an immediate one-step recovery. T4 persistence asymmetry collapses: within this finite closed model, recovery capability does not distinguish states in the way T4 requires.

This is a genuine failure boundary.

The next missing mathematics is therefore **not another definition of persistence**. It is a source-native mechanism that breaks exact redistribution reversibility or restricts recovery: stabilization hysteresis, Bandwidth loss/restriction, boundary leakage, a noninvertible Resolution/closure step, or another already-sourced asymmetry must become operational before T4 can be nontrivial.

---

# R17 — Minimal Four-Address Execution

Carrier:
`Q={q00,q01,q10,q11}`.

Adjacency:
square edges by Hamming distance one.

Undirected edges: 4.
Directed edges: 8.

Finite White grid:
`0,1/7,2/7,...,1`.

Total states:
`8^4 = 4096`.

Nontrivial admissible directed edge redistributions:
`71680`.

Active states with at least one nonzero internal transfer:
`4094`.

Sink states:
`2`.

Local kernel:
`R^δ_{u→v}(a|b)=(a-δ)|(b+δ)`.

## Audit

Acted-edge midpoint preserved for every enumerated transition:
`True`.

Block White-coordinate sum preserved:
`True`.

Exact one-step reverse transfer exists for every enumerated transition:
`True`.

### R17 verdict
**PASS.**

The local kernel is internally consistent on the complete finite state space.

---

# Chirality-seed audit

Exact diagonal families were instantiated as:

`χ+ : (a,b,b,a), a>b`.

`χ- : (a,b,b,a), a<b`.

Number of non-neutral χ+ seeds:
`28`.

Number of non-neutral χ- seeds:
`28`.

Neutral diagonal states:
`8`.

Among `1024` nonzero single-edge redistributions from exact χ± seeds, the number that remain exactly diagonal-symmetric is:

`0`.

Thus a nontrivial single-edge redistribution always leaves the exact diagonal chirality presentation.

This confirms the R16 constraint-repair mechanism: local redistribution creates a chirality-identity defect requiring subsequent History if the original chirality identity is to recover.

---

# R18 — Weak deterministic preference diagnostic

The roadmap's weak selector was implemented only as a diagnostic:

1. minimize diagonal-pair defect;
2. prefer target chirality sign;
3. minimize transfer magnitude;
4. deterministic address order.

It introduces no new admissible transition.

Across the exact χ± seeds, deterministic execution produced cycle-length distribution:

`{2: 56}`.

The selector therefore prevents combinatorial branching but does not solve persistence. It mostly chooses reversible repair cycles already present in the underlying graph.

### R18 verdict
**DIAGNOSTIC PASS, NO NEW MATHEMATICS.**

The selector can choose a route but cannot manufacture T4 asymmetry.

---

# R19 — Reachability closure

The state graph decomposes by the invariant block sum:

`S(x)=x00+x01+x10+x11`.

There are 29 possible integer sum classes `0,...,28`.

Every transition remains in its sum class.

Every fixed-sum class is connected under the current bidirectional transfer rules:

`True`.

Therefore every state with the same total White-coordinate sum is mutually reachable through finite internal redistribution histories.

This is much stronger than expected.

### Theorem R19.1 — Finite Redistribution Connectivity

For the enumerated four-node square with integer White units `0,...,7`, each fixed-total occupancy class is one connected component under admissible conservative edge transfers.

### R19 verdict
**PASS.**

The T2 reachable geometry is completely classified by total-sum strata in this realization.

---

# R20 — History lift

Because every nontrivial transition has an exact reverse, every transition generates a two-step identity-returning History:

`x --r--> y --r^-1--> x`.

Number of directed transition histories and corresponding immediate two-step recovery loops:

`71680`.

There are also many longer same-endpoint histories because each fixed-sum stratum is connected and contains cycles.

Endpoint equality therefore does not determine History.

### R20 verdict
**PASS.**

T3 is richly nontrivial even though the carrier dynamics are reversible.

---

# R21 — T4 recovery classification

R14/R15 define persistence using recoverable self-return after canonical redistribution.

But for every admissible local redistribution in this finite kernel:

`r : x→y`

the reverse edge transfer with the same magnitude is admissible:

`r^-1 : y→x`.

Therefore:

`r^-1 ∘ r = id_x`

at the carrier level.

No witness-based weaker recovery is even needed.

Hence:

`Rec_I(x) = Red_int(x)`

for every state x under the present internal redistribution contract.

There are no nonrecoverable internal redistributions.

The destabilizing set is empty:

`Fail_I(x)=∅`

for all x.

Therefore recovery-set inclusion cannot generate the T4 persistence asymmetry required by the roadmap.

## R21 verdict

\[
oxed{	extbf{FAIL — T4 COLLAPSES TO TRIVIAL UNIVERSAL RECOVERABILITY.}}
\]

This is the first genuine failure in the execution roadmap.

---

# Why this failure matters

The structural T4 law remains sound:

`persistence = recoverability under redistribution`.

What fails is this particular R16 finite realization.

The conservative edge kernel plus:
- bounded White carrier;
- bidirectional square adjacency;
- no loss;
- no hysteresis;
- no irreversible stabilization rule;

makes every local redistribution exactly reversible.

So the realization cannot express persistence **asymmetry**.

That means T4 cannot be produced merely by conservative topology-preserving transfer.

Something already suggested by the source must become operational.

---

# Candidate missing mechanisms — ordered by prior source support

## 1. Stabilization hysteresis

The source `.°.` stabilization operator is not numerically identical to "do nothing."

If stabilization changes the admissible transfer family after a redistribution, the exact reverse may cease to be admissible.

This is the cleanest candidate.

## 2. Bandwidth restriction

A reverse History may exist algebraically but exceed the current transformation-availability/Bandwidth contract.

Then recoverability becomes state-dependent.

## 3. Boundary leakage / open exchange

If redistribution may cross the persistent candidate boundary, block-sum conservation no longer guarantees local reversibility.

## 4. Noninjective Resolution/closure

If a redistribution passes through a noninjective stage, exact carrier inversion may be unavailable while witness recovery remains possible.

## 5. Destabilization gate

The source explicitly has a destabilization class. A transition entering that class may remove some recovery routes.

No new mechanism should be invented until these sourced possibilities are exhausted.

---

# Vera anti-recursion audit

No closed object was redefined.

- Cradle remained the Cradle.
- χ± remained second-order maximal-opposition classes.
- T0 remained admissibility.
- T1 remained preference.
- T2 remained reachability.
- T3 remained History.
- T4 remained recoverability under redistribution.

The run failed because the concrete redistribution realization made T4 trivial.

That failure is retained.

---

# Exact next attack

Do **not** proceed to R22/T5.

Return only to the one open parameter immediately upstream of the failure:

\[
oxed{	extbf{What does source stabilization `.°.` do to the admissible reverse-transfer set?}}
\]

The next run should test whether stabilization can be modeled from existing source constraints as a history-dependent restriction/hysteresis on `δ` or edge admissibility.

If stabilization leaves exact reversibility intact, test Bandwidth next.

Only after a sourced mechanism creates nontrivial `Rec_I(x)` should the roadmap resume at R21.

---

# Machine facts

- finite states: 4096
- directed nonzero transitions: 71680
- every transition exactly reversible: True
- fixed-sum classes all connected: True
- exact χ± single-edge symmetry-preserving nonzero moves: 0/1024
- T4 nonrecoverable redistributions: 0

# Final stopping point

\[
oxed{R21\ 	ext{FAIL}}
\]

Reason:

\[
oxed{	ext{conservative bidirectional redistribution} \Rightarrow
	ext{universal exact recovery} \Rightarrow
	ext{no persistence asymmetry}.}
\]

The map is healthy. The finite realization is missing the operational asymmetry that T4 requires.
