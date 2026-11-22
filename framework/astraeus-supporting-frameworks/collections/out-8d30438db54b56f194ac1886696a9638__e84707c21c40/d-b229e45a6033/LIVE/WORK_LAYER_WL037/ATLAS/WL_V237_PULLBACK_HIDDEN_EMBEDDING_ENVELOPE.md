# WL-v237 — Canonical Pullback Envelope for the Hidden-State Embedding

**QMO:** QMO-AST-DM-WL-121  
**Work layer:** WL-037  
**Parent promotions:** 0  
**Status:** CONDITIONAL BUNDLE CONSTRUCTION / EMBEDDING PROBLEM RETYPED

## Existing open object

Dark Matter 2.2 requires selection of

```text
iota_H in Emb_H,phys^R
```

with

```text
pi_E o iota_H = j_T o pi_H
I o iota_H = iota_H o I_H
iota_H(E_H^R) subset ker(C).
```

Prior WL-035 correctly rejected the mistake

```text
local state lift == global hidden-state embedding.
```

This pass does not repeat that mistake.

## Geometry-first construction

Use the already-declared base map

```text
j_T : T_H -> T.
```

Form the standard pullback of the Inherited State Bundle:

```text
j_T^*E
=
{(t,e) in T_H x E : pi_E(e)=j_T(t)}.
```

There is a canonical bundle map

```text
can : j_T^*E -> E,
can(t,e)=e,
```

covering `j_T`.

Now do **not** identify `E_H^R` with `j_T^*E`. Instead require a separate faithful bundle map

```text
eta_H : E_H^R -> j_T^*E.
```

If `eta_H` exists, define

```text
iota_H := can o eta_H.
```

The base commuting law then holds automatically.

## Remaining tests

The open physical embedding problem reduces to three explicit tests on `eta_H`:

```text
H1 — faithful/injective encoding of the hidden relational-state fiber;
H2 — inheritance equivariance:
     eta_H o I_H = (j_T^*I) o eta_H;
H3 — physical constraint support:
     eta_H(E_H^R) subset j_T^*ker(C).
```

If H1-H3 hold, the composite `iota_H` is an element of the already-defined constraint-preserving embedding family.

## Why this is progress

The global bundle map no longer has to be guessed directly. The hard question is localized to whether the existing hidden relational-state tuple

```text
R_H(t)=(V_t,E_t,w_t,chi_t,H_t)_R
```

has a faithful, inheritance-compatible, constraint-compatible representation inside the pullback inherited-state fibers.

This is a narrower problem than the prior unconstrained embedding search.

## Relation to S³ complement carrier

If `T_H` is instantiated by the hidden S³ complement carrier through the active `S4 -> S3 -> S2` geometry, `j_T` is geometrically interpreted as the inclusion of the hidden carrier domain into Time-Space. That geometric interpretation does not itself certify H1-H3.

## Guardrails

- Pullback bundle != existing DM relational-state bundle.
- Canonical map `can` does not solve faithful encoding `eta_H`.
- Base commutation alone does not solve inheritance or constraint preservation.
- This is not the rejected state-level LiftSet shortcut.
- No OpenSlot closure; no parent promotion.

## Next move

Test H1 using the Prime Dependency representation theorem plus the existing inherited-state semantics, then test whether Resolution/History data supply the required faithful distinction without importing mote adjacency.
