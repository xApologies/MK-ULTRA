# V36 — Native Chirality Factorization

## Status

SOURCE-RECONCILIATION + NEW DERIVED RELATION MATHEMATICS.

## Recovered exact parent

The current formal Time-Space primitive layer already contains

    chi : E -> Omega

where

    E
    =
    Inherited State Bundle,

and

    Omega
    =
    Chirality Space.

The current primitive description types Omega as the admissibility space
for chirality organization and chi as the map assigning admissible
chirality organization to inherited organizational states.

Therefore v35's entire native-to-representation bridge is not missing.

The native-to-chirality stage is already typed.

## Representation target

Let

    X_C^R

denote one selected downstream chromatic / basin representation space at
Resolution R.

No universal identity between Omega and X_C^R is assumed.

## Remaining representation relation

Define the unresolved downstream relation

    R_OmegaC^R
    subseteq
    Omega x X_C^R.

Interpretation:

    (omega,z) in R_OmegaC^R

means that z is an admitted X_C^R representation of chirality organization
omega at Resolution R.

No functionality, injectivity, surjectivity, invertibility, or transport
law is presumed.

## Graph of the exact Chirality Map

Define

    Graph(chi)
    =
    {
      (xi,omega) in E x Omega
      |
      omega = chi(xi)
    }.

Because chi is a function, every xi in E has exactly one chirality image
within the declared domain.

## Corrected v35 factorization

Define the native-to-chromatic relation by relational composition:

    R_NC^R
    =
    Graph(chi) ; R_OmegaC^R.

Equivalently,

    R_NC^R
    =
    {
      (xi,z)
      |
      (chi(xi),z) in R_OmegaC^R
    }.

## Closure

The missing bridge has therefore been reduced from

    native state
    -> ?
    -> chromatic representation

to

    E
    --chi-->
    Omega
    --R_OmegaC^R-->
    X_C^R.

Only the second arrow remains unresolved.

## Scope guardrail

This closure concerns representation assignment.

Native edge admissibility can still depend on state coordinates not
contained in chi(xi), including any separately typed orientation,
continuity, topology, depth, occupancy, or environment data.

Therefore the exact Chirality Map does not collapse the full native
admissibility state into Omega.
