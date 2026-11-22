# 66 — Helicon Quotient of Admissibility Dynamics

Let the Helicon equivalence classes from v7 be

```text
C_1,...,C_m.
```

Assume they form an equitable partition with respect to the configuration admissibility kernel `A_U`, meaning

```text
q_ab(c) = sum_{d in C_b} A_U(c,d)
```

is independent of `c in C_a`.

Define

```text
(A_H^Q)_ab = q_ab.
```

Because the Unit-String kernel is normalized,

```text
sum_b (A_H^Q)_ab = 1.
```

Thus `A_H^Q` is itself a normalized Helicon-class transition kernel.

Define

```text
(T_H^Q h)_a = sum_b (A_H^Q)_ab h_b
```

and

```text
L_H^Q = I - T_H^Q.
```

For the class-constant lift `Q`:

```text
T_U Q = Q T_H^Q
```

and therefore

```text
L_U Q = Q L_H^Q.
```

This is stronger than the generic v7 graph-Laplacian statement because the operator now inherits the **recovered AERA admissibility algebra**.

## Spectral admissibility

If

```text
T_H^Q h_alpha = mu_alpha h_alpha,
```

then

```text
L_H^Q h_alpha = lambda_alpha^Q h_alpha
```

with

```text
lambda_alpha^Q = 1 - mu_alpha.
```

The phrase `spectral admissibility value` in the historical source is therefore naturally compatible with either `mu_alpha` or the defect-normalized `lambda_alpha^Q`.

## Status

**THEOREM UNDER CONFIGURATION-LIFT + EQUITABILITY CONDITIONS.**
