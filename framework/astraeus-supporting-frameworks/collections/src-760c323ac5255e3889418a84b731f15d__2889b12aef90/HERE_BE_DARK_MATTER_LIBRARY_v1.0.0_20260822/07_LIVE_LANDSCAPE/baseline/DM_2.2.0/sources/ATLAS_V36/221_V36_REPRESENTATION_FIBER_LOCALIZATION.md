# V36 — Representation-Fiber Localization Theorem

## Status

NEW DERIVED MATHEMATICS.

## Relation fibers

For xi in E define

    R_NC^R[xi]
    =
    {
      z in X_C^R
      |
      (xi,z) in R_NC^R
    }.

For omega in Omega define

    R_OmegaC^R[omega]
    =
    {
      z in X_C^R
      |
      (omega,z) in R_OmegaC^R
    }.

## Theorem

For every xi in E,

    R_NC^R[xi]
    =
    R_OmegaC^R[chi(xi)].

## Proof

By the v36 factorization,

    (xi,z) in R_NC^R

iff

    (chi(xi),z) in R_OmegaC^R.

Therefore the set of z related to xi is exactly the set of z related to
chi(xi).

Hence

    R_NC^R[xi]
    =
    R_OmegaC^R[chi(xi)].

QED.

## Corollary 1 — empty-fiber obstruction

If

    R_OmegaC^R[chi(xi)] = empty,

then

    R_NC^R[xi] = empty.

The native state xi has no admitted representation in the selected
chromatic/basin representation space.

## Corollary 2 — singleton representation

If

    |R_OmegaC^R[chi(xi)]| = 1,

then xi has exactly one admitted X_C^R representation.

## Corollary 3 — representation degeneracy

If

    |R_OmegaC^R[chi(xi)]| > 1,

then all pointwise representation ambiguity for the fixed native state xi
is localized to the Omega -> X_C^R representation stage.

## Important qualification

This theorem localizes representation ambiguity.

It does not imply that every two native states with the same chirality image
are physically or admissibly equivalent.

If

    chi(xi_1) = chi(xi_2),

the selected chromatic representation fibers are equal, but other native
state coordinates may still distinguish xi_1 and xi_2.
