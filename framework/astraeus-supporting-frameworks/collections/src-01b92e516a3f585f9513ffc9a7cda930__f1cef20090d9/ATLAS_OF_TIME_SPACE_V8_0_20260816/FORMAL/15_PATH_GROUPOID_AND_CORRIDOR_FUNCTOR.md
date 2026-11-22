# 15 — Path Groupoid and Corridor Functor

## 15.1 Admissible path category

Let `Path_adm(S3)` be the path category whose:

- objects are continuity addresses `p in S3`;
- morphisms are admissible piecewise-smooth paths `gamma:p->q`;
- composition is path concatenation;
- identity is the constant path.

When only reversible paths/transport are retained, use the corresponding path groupoid.

---

## 15.2 Chirality-section category

Associate to every address `p` the local formal chirality section space:

```text
C_p^formal(B).
```

For reversible transport, admissible isomorphisms between these section spaces form the target transport groupoid.

---

## 15.3 Corridor transport functor

The chirality connection defines:

```text
P^chi : Path_adm(S3) -> ChirTransport
```

by:

```text
p |-> C_p^formal(B)
gamma |-> P_gamma^chi.
```

For composable paths:

```text
gamma_ab : a -> b
gamma_bc : b -> c,
```

parallel transport satisfies:

```text
P_(gamma_bc * gamma_ab)^chi
=
P_gamma_bc^chi o P_gamma_ab^chi.
```

For the constant path:

```text
P_id_p^chi = id_(C_p).
```

This is the categorical closure of the existing corridor composition law.

---

## 15.4 Corridor geometry functor

Each path also determines a geometric pullback corridor:

```text
W_gamma := gamma^*(T5).
```

On the standard bundle branch:

```text
W_gamma ~= S2 x I.
```

Thus the same base path has two related images:

```text
gamma
|-> W_gamma           (geometric corridor)
gamma
|-> P_gamma^chi       (chirality transport).
```

The portal operator:

```text
C_alpha_beta = Pi_beta o P_gamma^chi o L_alpha
```

is therefore the readable factorization of a path-indexed corridor transport.

---

## 15.5 Reverse corridor

For reversible transport:

```text
P_(gamma^-1)^chi = (P_gamma^chi)^-1.
```

This does not imply that every transduction possesses an inverse. Noninvertible transformations remain outside the reversible transport groupoid.

---

## 15.6 Bandwidth and Resolution

Bandwidth restricts the available morphisms:

```text
Path_adm,B(S3) subset Path_adm(S3).
```

Resolution acts on the readout of transported sections:

```text
rho_R,beta o P_gamma^chi
```

and may identify formally different transports.

Thus:

```text
formal corridor identity != observational corridor identity.
```

---

## Proposition AT-P15.1 — Corridor composition closure

Under existence of the two connections and reversible admissibility of the composed paths, corridor transport is associative because path concatenation and parallel transport are associative up to the standard path-reparameterization equivalence.

**Status:** PROVED CONDITIONAL ON CONNECTION EXISTENCE.
