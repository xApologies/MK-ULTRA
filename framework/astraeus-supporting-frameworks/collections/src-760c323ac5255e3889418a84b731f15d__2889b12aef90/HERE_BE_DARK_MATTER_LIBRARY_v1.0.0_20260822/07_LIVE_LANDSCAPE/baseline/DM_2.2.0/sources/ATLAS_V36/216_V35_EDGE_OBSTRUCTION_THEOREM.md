# V35 — Required-Edge Obstruction Theorem

## Status

NEW DERIVED MATHEMATICS.

## Edge lift set

For a required hidden-network edge

    e = (u,v)

and a candidate chromatic configuration z, define

    L_e(z)
    =
    {
      (x_u,x_v)
      |
      (x_u,z(u)) in R_NC^R,
      (x_v,z(v)) in R_NC^R
    }.

Define the positive-admissibility subset

    L_e^+(z)
    =
    {
      (x_u,x_v) in L_e(z)
      |
      A(x_u,x_v) > 0
    }.

## Theorem — edge obstruction

If there exists a required edge e in E_H such that

    L_e^+(z) = empty,

then

    L_adm^R(z | W_H^R) = empty

and therefore

    Adm_C^R(z | W_H^R) = 0.

## Proof

Every admissible lift must assign native representatives to u and v whose
native edge is admissible.

If no such pair exists for one required edge, no globally admissible lift
can exist.

QED.

## Path corollary

If ell is an admissible lift of a required hidden path

    P = (e_1,...,e_m),

then each native edge satisfies

    A(e_k) > 0

and therefore

    A(P) = product_k A(e_k) > 0.

Thus a candidate representation that forces a zero-admissibility edge cannot
represent an admissible hidden S3 corridor.

## Use

This is a hard falsifier.

A candidate chromatic/basin representation can be rejected before any
Time-Shell or stress-energy calculation when it cannot lift the required
hidden-network incidence structure into native admissibility.
