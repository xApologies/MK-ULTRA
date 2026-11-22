# V35 — Admissibility Equivalence and Quotient

## Status

NEW DERIVED MATHEMATICS.

V34 required singleton chromatic fibers for a pointwise deterministic inverse.
V35 shows that pointwise uniqueness may be stronger than necessary.

## Admissible antecedent signature

For a candidate chromatic state/configuration z define

    Sig_A^R(z)
    =
    {
      ell
      |
      ell in L_adm^R(z | W_H^R)
    }.

Define

    z ~_A z'

iff

    Sig_A^R(z) = Sig_A^R(z').

This is an equivalence relation.

## Quotient

Define

    Q_A^R
    =
    X_C^R / ~_A.

A point in Q_A^R records the chromatic representation only up to the
distinctions currently visible to native admissibility.

## Refined fiber classification

Let

    F_C,H^R(W_H^R)

be the v34 constrained chromatic fiber.

There are now four useful statuses:

1. EMPTY:
       F = empty.

2. POINT-UNIQUE:
       |F| = 1.

3. CLASS-UNIQUE:
       |F| > 1
       but
       |F / ~_A| = 1.

4. CLASS-DEGENERATE:
       |F / ~_A| > 1.

Point-unique is sufficient but may not be necessary for downstream
realization.

## Time-Shell descent criterion

Let

    T_TS : X_C^R -> Y_R

be any future typed Time-Shell translation on the relevant representation
space.

T_TS factors through the admissibility quotient iff

    z ~_A z'
    =>
    T_TS(z) = T_TS(z').

When this condition holds, there exists a unique map

    Tbar_TS : Q_A^R -> Y_R

such that

    T_TS = Tbar_TS o q_A

where

    q_A : X_C^R -> Q_A^R

is the quotient map.

## Consequence

If the constrained chromatic fiber contains several point states but exactly
one admissibility class, and the Time-Shell translation is constant on that
class, then no pointwise inverse is required.

The physically relevant representation may be the quotient class.

This is a major reduction of the inverse-dictionary burden, but the
Time-Shell descent condition remains open and must be tested rather than
assumed.
