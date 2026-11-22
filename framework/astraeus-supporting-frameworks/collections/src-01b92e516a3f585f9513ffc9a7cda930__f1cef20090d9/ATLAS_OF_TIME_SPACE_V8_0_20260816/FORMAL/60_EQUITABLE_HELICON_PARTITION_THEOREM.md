# 60 — Equitable Helicon Partition Theorem

This file closes the main v6 operator-intertwining question under an explicit structural condition.

## Configuration graph

Let

```text
Gamma_U = (V_U,E_U,w)
```

be the weighted Unit-String configuration graph, and let

```text
L_U = D - W
```

be its scalarized native spectral operator on a selected typed sector.

Restrict to Helicon-compatible vertices `V_Hel` and partition them by the equivalence relation `~_H` induced by `J_H`.

Let the classes be

```text
C_1,...,C_m.
```

## Equitable condition

The Helicon partition is **equitable** when, for every pair of classes `C_a,C_b`, the total transition weight

```text
q_ab(c) = sum_{d in C_b} w(c,d)
```

is independent of the chosen representative `c in C_a`.

Then write simply

```text
q_ab.
```

## Quotient operator

Define the Helicon quotient adjacency

```text
(W_H)_ab = q_ab
```

and quotient degree

```text
(D_H)_aa = sum_b q_ab.
```

The quotient spectral operator is

```text
L_H^Q = D_H - W_H.
```

## Lift map

Let

```text
Q : R^m -> R^{|V_Hel|}
```

lift a Helicon-class amplitude to a configuration amplitude constant on each class:

```text
(Qh)(c) = h_a,  c in C_a.
```

## Theorem

If the Helicon partition is equitable, then

```text
L_U Q = Q L_H^Q.
```

### Proof

For `c in C_a`,

```text
(L_U Qh)(c)
=
deg(c) h_a - sum_b sum_{d in C_b} w(c,d) h_b.
```

By equitability,

```text
sum_{d in C_b} w(c,d) = q_ab
```

and

```text
deg(c) = sum_b q_ab.
```

Therefore

```text
(L_U Qh)(c)
=
(sum_b q_ab) h_a - sum_b q_ab h_b
=
(L_H^Q h)_a
=
(Q L_H^Q h)(c).
```

Hence

```text
L_U Q = Q L_H^Q.
```

QED.

## Spectral consequence

If

```text
L_H^Q h = lambda h,
```

then

```text
L_U(Qh)=lambda(Qh).
```

Thus every quotient Helicon mode lifts to a Unit-String configuration mode.

Equivalently:

```text
Spec(L_H^Q) subseteq Spec(L_U)
```

for the class-constant sector.

## Meaning

This is the first exact, calculus-free closure of the v6 intertwining problem.

It does **not** prove that the historical `L_H` is numerically identical to `L_H^Q`. It proves that a Helicon spectral operator arises canonically as a quotient of Unit-String configuration geometry whenever Helicon identity classes form an equitable partition.

The remaining recovery problem is now sharply typed:

```text
Historical L_H  ?=  quotient operator L_H^Q
```

rather than the vague earlier question

```text
Unit String modes ?= Helicon modes.
```

## Status

**THEOREM UNDER DECLARED EQUITABILITY CONDITION.**
