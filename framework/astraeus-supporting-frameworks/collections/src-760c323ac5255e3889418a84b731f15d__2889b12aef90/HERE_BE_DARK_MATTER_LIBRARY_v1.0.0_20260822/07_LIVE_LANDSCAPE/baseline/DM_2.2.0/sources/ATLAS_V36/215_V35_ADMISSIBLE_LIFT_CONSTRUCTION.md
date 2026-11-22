# V35 — Admissible-Lift Construction

## Status

API-NATIVE DERIVATION CONDITIONAL ON A TYPED REPRESENTATION RELATION.

## Recovered native admissibility

The AERA admissibility algebra contains an edge score

    A_ij
    =
    alpha_ij theta_ij gamma_ij

with transition rule

    edge allowed iff A_ij > 0.

For a path P = (e_1,...,e_m),

    A(P)
    =
    product_k A(e_k).

## Hidden network

Let

    G_H^R = (V_H,E_H)

be the currently selected hidden S3 network/corridor support at Resolution R.

Let

    z : V_H -> X_C^R

be a candidate chromatic/basin configuration over the network support.

## Native lift

A native lift of z is a map

    ell : V_H -> X_N^R

such that

    (ell(v), z(v)) in R_NC^R

for every v in V_H.

## Admissible native lift

Define the admissible-lift set

    L_adm^R(z | W_H^R)
    =
    {
      ell
      |
      (ell(v),z(v)) in R_NC^R for all v,
      A(ell(u),ell(v)) > 0 for every required edge (u,v) in E_H,
      and every additionally declared history/chirality/persistence/
      closure/Resolution/Bandwidth condition is satisfied
    }.

The additional conditions are not filled by invention. They are admitted
only when separately typed.

## Induced chromatic admissibility

Define

    Adm_C^R(z | W_H^R)
    =
    1
    iff
    L_adm^R(z | W_H^R) is nonempty.

Otherwise

    Adm_C^R(z | W_H^R)
    =
    0.

This is the existential pushforward of native admissibility through the
representation relation.

## Theorem — type-correctness

If R_NC^R is a typed relation and the native admissibility predicate is
typed on X_N^R, then Adm_C^R is a well-defined Boolean predicate on candidate
chromatic configurations.

No new physical coefficient is needed.

## Important limitation

Adm_C^R(z)=1 means:

    at least one admissible native organization realizes z.

It does NOT imply:

- the native antecedent is unique;
- the representation is physically complete;
- the Time Shell translation is injective;
- z is dark matter.
