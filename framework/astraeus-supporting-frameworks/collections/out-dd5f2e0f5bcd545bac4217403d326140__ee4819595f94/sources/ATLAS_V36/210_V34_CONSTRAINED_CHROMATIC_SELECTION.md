# V34 — Constrained Chromatic Selection

## Status

NEW DERIVED MATHEMATICS.

## Motivation

V33 supplied a Resolution-level hidden density profile

    Delta bold_rho_H^R.

V34 shows that density alone cannot uniquely recover a chromatic/basin state.

The current hidden S3 work, however, contains more information than density alone:

- hidden port-response operator Lambda_H;
- admissible history support;
- chirality / orientation constraints;
- persistence / closure constraints;
- Resolution and Bandwidth constraints.

These may lawfully restrict the density fiber if and only if the relevant constraint map is explicitly typed.

## Definition — admissible structural selector

Let

    A_H^R
    subseteq
    X_chi

be the set of chromatic-representation states compatible with the declared hidden-network data at Resolution R.

A_H^R is NOT assigned an explicit formula here.

Its future construction may use only already-typed inputs such as:

    Lambda_H,
    admissible history support,
    chirality constraints,
    persistence,
    closure,
    Resolution,
    Bandwidth,
    boundary data.

## Definition — constrained density fiber

For density value r,

    F_chi,H^R(r)
    =
    F_chi(r)
    intersect
    A_H^R.

For a profile over cells a,

    F_chi,H^R(bold_rho)
    =
    product_a
    F_chi,H,a^R(rho_a)

subject to any explicitly declared cross-cell compatibility constraints.

## Fiber trichotomy

For each admitted density/profile input, exactly one structural status holds:

### 1. Empty fiber

    F_chi,H^R = empty.

Interpretation:
the proposed chromatic representation is incompatible with the hidden-network state.

The chromatic route fails for that input.

### 2. Singleton fiber

    |F_chi,H^R| = 1.

Interpretation:
the currently admitted constraints uniquely select a chromatic representative.

Only in this case may Beta_R be treated as a deterministic function on that input.

### 3. Degenerate fiber

    |F_chi,H^R| > 1.

Interpretation:
the current source data underdetermine the chromatic representation.

The route remains nonunique.

## Constraint-monotonicity theorem

If

    A_2 subseteq A_1,

then

    F_chi(r) intersect A_2
    subseteq
    F_chi(r) intersect A_1.

Therefore adding valid structural constraints can only preserve or reduce representational ambiguity.

It cannot create new admissible states outside the original density fiber.

## Canonical selection criterion

A canonical local map

    Beta_R

is earned only on the subset of inputs for which the constrained fiber is singleton.

Equivalently,

    Dom_unique(Beta_R)
    =
    {
      r
      |
      |F_chi,H^R(r)| = 1
    }.

Outside that domain Beta_R remains set-valued or undefined.
