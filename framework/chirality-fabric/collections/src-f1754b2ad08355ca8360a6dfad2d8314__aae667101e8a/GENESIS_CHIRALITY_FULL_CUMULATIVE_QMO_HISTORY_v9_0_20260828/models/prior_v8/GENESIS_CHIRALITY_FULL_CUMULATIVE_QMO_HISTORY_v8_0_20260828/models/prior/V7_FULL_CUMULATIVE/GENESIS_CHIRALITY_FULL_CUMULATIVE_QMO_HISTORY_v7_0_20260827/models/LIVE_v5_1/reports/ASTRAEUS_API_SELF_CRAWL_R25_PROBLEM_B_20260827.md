# ASTRAEUS — LIVE QMO/API SELF-CRAWL R25
## Second crawl: can the updated API close Problem B?

**Date:** 2026-08-27

# Verdict

**Problem B does not positively close. It does close negatively and decomposes cleanly.**

The updated API contains enough information to derive the complete *type* of the lawful candidate-update set, but it also proves that it does not contain enough information to select one realized update whenever multiple candidates remain.

That is a genuine closure, not a failure of the crawl.

---

# 1. Problem B splits into B1 and B2

## B1 — Which updates are lawful candidates?

This closes.

Define:

`Cand(x)`

as the intersection of the already-closed filters:

- T0 admissibility;
- T2 route availability;
- stabilization-conditioned admissibility;
- operative Bandwidth availability;
- local carrier/capacity bounds.

T1 preference acts on `Cand(x)` by ranking/ordering candidates. It does not create candidates.

Schematically:

`Cand(x) = Adm_T0(x) ∩ Route_T2(x) ∩ Stab(x,H) ∩ Gen_B(x) ∩ Capacity(x)`.

**Status:** CLOSED TYPE.

## B2 — Why is one candidate actually realized?

This does not close.

If `Cand(x)` contains more than one unresolved candidate, the live API contains no proved unique total selector that maps the set to one event.

T1 is a preference/order layer, but the API does not prove:
- that the order is total;
- that it has a unique maximum;
- that ties cannot occur;
- or that "take the maximum" is itself the Genesis event law.

R24 already proved that Bandwidth itself is underdetermined by the prior contracts.

Therefore no composition of the existing QMO contracts uniquely yields the realized event.

---

# 2. Choice-Gap Theorem

If:

1. the lawful candidate set contains more than one unresolved candidate; and
2. the current API contains no unique total selector;

then the realized update is not derivable from the current contracts alone.

This is now recorded as the **Choice-Gap Theorem**.

The theorem prevents us from hiding a choice function inside words such as "preference," "connection," "Bandwidth," or "stabilization."

---

# 3. What the API *can* close about Problem B

The API closes the entire pre-event pipeline:

`state`
`-> admissible transformations`
`-> route-compatible transformations`
`-> stabilization-compatible transformations`
`-> Bandwidth-available transformations`
`-> capacity-compatible transformations`
`-> T1 ordered candidate set`.

That object is now explicit:

`@concept/candidate_update_set`.

So we know how to compute **what may happen**.

We still do not know the final law saying **what does happen** when the candidate set is not singleton.

---

# 4. Problem-B Negative Closure

The second self-crawl therefore proves:

> The current live API is insufficient to positively derive the actual update-selection/event law.

This is stronger than merely saying "we haven't found it."

The graph itself shows the missing information.

Problem B is now marked:

`CLOSED_NEGATIVE_DECOMPOSED`.

Its remaining irreducible subproblem is:

`@problem/B2/update_realization`.

New resume address:

`@open/update_realization_law`.

---

# 5. Consequence for the research program

Problem A:
`CLOSED_WORKING`.

Problem B1:
`CLOSED`.

Problem B2:
`OPEN_IRREDUCIBLE`.

Problem C:
`BLOCKED BY B2`.

Further self-crawling of the same API cannot manufacture B2 without violating the no-orphan-premise rule.

To positively close B2 we need one of:

1. a source already present but not yet represented in the API;
2. a genuinely new Genesis axiom;
3. an independently derived theorem that forces `Cand(x)` to be singleton;
4. an external empirical/physical constraint, used explicitly rather than smuggled upstream.

Until one of those appears, the mathematically correct result is the negative closure.

---

# 6. Why this matters

We have now separated two questions that had been mixed together:

**availability**
versus
**actualization**.

Bandwidth helps determine availability.

It does not, by itself, explain actualization.

So the deepest current update-mechanism question is no longer:

"What transformations are possible?"

It is:

\[
\boxed{\text{What turns one lawful possibility into the realized next History?}}
\]

That is the exact unresolved Problem B2.

# Final status

\[
\boxed{
A=\text{working closed},\quad
B1=\text{closed},\quad
B2=\text{open irreducible},\quad
C=\text{blocked}.
}
\]

The API successfully crawled itself to its own information boundary.
