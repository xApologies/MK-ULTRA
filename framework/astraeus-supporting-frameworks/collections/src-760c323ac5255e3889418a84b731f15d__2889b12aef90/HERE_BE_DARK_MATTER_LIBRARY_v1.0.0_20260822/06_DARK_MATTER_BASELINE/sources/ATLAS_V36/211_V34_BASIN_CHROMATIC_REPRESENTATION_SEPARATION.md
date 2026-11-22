# V34 — Basin / Chromatic Representation Separation

## Status

SOURCE-RECONCILIATION RULING.

## Recovered records

One recovery branch gives six named visible basin identities:

    Red, Orange, Yellow, Green, Blue, Violet

with historical 1/7 ... 6/7 labels and 0/7, 7/7 bounds.

A separate recovered downstream field representation uses

    chi = (chi_1, ..., chi_7).

The current evidence does not supply a complete source-authoritative bijection between these two representations.

## Ruling

Do not write

    basin index = chromatic field component

and do not write

    1/7, ..., 6/7 = measured energy amplitudes

as universal identities.

The source corpus itself states that:

    basin identity precedes decimal representation

and the Reader's Companion states that:

    basin organization -> field intensity

is a translation, not an identity.

## Typed holding structure

Until the dictionary is recovered, retain two distinct representation spaces:

    X_basin
    =
    basin-organization representation

and

    X_chi
    =
    multi-component chromatic-field representation.

Permit only an explicitly typed candidate correspondence

    D_Bchi :
    Dom(D_Bchi) subseteq X_basin
    ->
    X_chi

or a relation

    R_Bchi
    subseteq
    X_basin x X_chi.

No inverse is assumed.

## Consequence

V33's `BasinOrg_R` should be read generically as the organizational codomain of the Time-Shell basin translation, not as automatically identical to the seven-component chromatic continuum field.

This prevents a historical representation mismatch from becoming a false theorem.
