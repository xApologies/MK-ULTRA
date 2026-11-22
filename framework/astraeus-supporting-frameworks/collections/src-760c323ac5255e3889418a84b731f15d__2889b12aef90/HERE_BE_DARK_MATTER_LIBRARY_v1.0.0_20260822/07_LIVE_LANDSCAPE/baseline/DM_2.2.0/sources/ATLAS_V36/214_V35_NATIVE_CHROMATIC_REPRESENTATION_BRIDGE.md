# V35 — Native / Chromatic Representation Bridge

## Status

NEW DERIVED TYPING STRUCTURE built from recovered source domains.

This document does not assert that the required representation relation has already been recovered as a source equation.

## Source-level type distinction

The AERA Phase III native state is represented schematically by

    s_i = (chi_i^N, rho_i^N, sigma_i, A_i)

where `chi_i^N` is native chirality / occupancy organization and `rho_i^N`
is a source-scoped orientation embedding variable.

A separate downstream chromatic representation uses multi-component fields

    chi^C = (chi_1^C, ..., chi_n^C).

The repeated symbol `chi` does not establish identity.

Therefore:

    chi^N != chi^C

as typed records unless a representation map is supplied.

## Native state space

Let

    X_N^R

denote the native admissibility state space restricted to the declared
Resolution-R problem.

## Chromatic representation space

Let

    X_C^R

denote the admitted downstream chromatic/basin representation space at the
same declared Resolution scope.

## Representation relation

The weakest lawful bridge is a relation

    R_NC^R
    subseteq
    X_N^R x X_C^R.

Interpretation:

    (x,z) in R_NC^R

means only that `z` is an admitted chromatic/basin representation of native
state `x` at scope R.

No functionality, injectivity, surjectivity, or inverse is assumed.

A deterministic representation map

    r_NC^R : X_N^R -> X_C^R

is a special case in which every native state has one represented output.

## Why a relation is required

Without R_NC^R there is no typed operation by which native admissibility,
history, chirality, closure, or network incidence can be transferred to the
chromatic representation.

Similarity of names is not a map.

This is the representation firewall required before v34's
`Adm_chi^R` can be completed.
