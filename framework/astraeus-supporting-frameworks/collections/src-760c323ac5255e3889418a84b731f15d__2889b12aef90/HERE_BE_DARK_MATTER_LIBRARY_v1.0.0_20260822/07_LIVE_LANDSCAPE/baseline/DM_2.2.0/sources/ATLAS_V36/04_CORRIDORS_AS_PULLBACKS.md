# 04 — Corridors as Pullbacks

## Construction

Let:

```text
gamma : I=[0,1] -> S3
```

join continuity addresses:

```text
gamma(0)=p_alpha
gamma(1)=p_beta.
```

Define the corridor as the pullback:

```text
W_gamma := gamma^*(T5).
```

The pullback square is:

```text
W_gamma  ----->  T5
  |               |
  |               | pi
  v               v
  I ----gamma-->  S3
```

## Corridor theorem (conditional on the ordinary bundle model)

If `pi:T5->S3` is a locally trivial `S2` bundle along `gamma`, then the pullback bundle over the contractible interval `I` is trivial:

```text
W_gamma ~= S2 x I.
```

Endpoint boundary:

```text
boundary(W_gamma)
=
Sigma_alpha union (-Sigma_beta).
```

This recovers the previously defined Chirality Corridor object from the Time-Space architecture rather than inserting it independently.

## Transport

Chirality transport along the corridor:

```text
P_gamma^chi : C_alpha -> C_beta.
```

The existing portal factorization becomes:

```text
C_alpha_beta = Pi_beta o P_gamma^chi o L_alpha.
```

## Composition

For composable paths `gamma_ab` and `gamma_bc`:

```text
gamma_ac = gamma_bc * gamma_ab
```

and, when transport is functorial:

```text
P_gamma_ac^chi
=
P_gamma_bc^chi o P_gamma_ab^chi.
```

This is the natural route to a corridor category/groupoid in a later Atlas version.
