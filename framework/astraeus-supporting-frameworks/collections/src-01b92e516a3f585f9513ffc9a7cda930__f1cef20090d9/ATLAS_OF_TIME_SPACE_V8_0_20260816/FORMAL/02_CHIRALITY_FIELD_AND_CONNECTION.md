# 02 — Chirality Field and Connection

## Global chirality carrier

Let:

```text
pi_chi : E_chi -> T5
```

be the chirality bundle/carrier.

A global chirality configuration is a section:

```text
chi in Gamma(E_chi).
```

## Local chirality

For a local projection inclusion:

```text
i_p : Sigma_p -> T5
```

define:

```text
chi_p := i_p^*(chi).
```

`chi_p` is the chirality field that QFT, GR, and ER foam read inside that localized spacetime domain.

## Vertical/horizontal split

For `pi:T5->S3`:

```text
V := ker(d pi)
```

is the vertical tangent distribution. Choosing a horizontal complement `H` gives:

```text
T(T5)=V direct_sum H.
```

This supplies a disciplined interpretation of two behaviors:

```text
nabla_V^chi = local change inside a selected S2 projection
nabla_H^chi = transport among S2 projections through S3 continuity.
```

Working shorthand:

```text
nabla^chi = nabla_V^chi + nabla_H^chi.
```

## Holonomy target

For a loop `gamma` in `S3`, horizontal transport may generate a chirality holonomy:

```text
Hol_chi(gamma).
```

This is a natural location for globally accumulated orientation/history information without forcing nontriviality into the bare bundle topology.
