# WL-v239 — Canonical Pullback Equivalence for the Hidden-State Embedding

**QMO:** QMO-AST-DM-WL-123  
**Work layer:** WL-038  
**Parent promotions:** 0  
**Status:** PROVED WORK-LAYER MATHEMATICAL REDUCTION

## Problem

Dark Matter API 2.2 asks for a bundle monomorphism

```text
iota_H : E_H^R -> E
```

with base compatibility

```text
pi_E o iota_H = j_T o pi_H.
```

WL-037 retyped this through the pullback of the Time-Space Inherited State Bundle along the hidden-base map.

## Pullback

Let

```text
P_H := j_T^*E
     = {(t,e) in T_H x E : j_T(t)=pi_E(e)}.
```

Write

```text
pr_H : P_H -> T_H,
can  : P_H -> E
```

for the two canonical projections.

## Theorem — base-commuting maps are exactly pullback maps

There is a one-to-one correspondence between:

1. maps `iota:E_H^R->E` satisfying

```text
pi_E o iota = j_T o pi_H,
```

and

2. maps `eta:E_H^R->P_H` satisfying

```text
pr_H o eta = pi_H.
```

The correspondence is

```text
eta(x) = (pi_H(x), iota(x))
```

and

```text
iota = can o eta.
```

### Proof

If `iota` is base compatible, then

```text
pi_E(iota(x)) = j_T(pi_H(x)),
```

so `(pi_H(x),iota(x))` is by definition an element of `P_H`. Hence `eta` is well-defined and lies over `pi_H`.

Conversely, if `eta(x)=(t,e)` lies in `P_H` and `pr_H eta=pi_H`, then `t=pi_H(x)` and pullback membership gives

```text
pi_E(e)=j_T(pi_H(x)).
```

With `iota=can eta`, this is precisely the base-commuting condition.

Uniqueness follows because both pullback coordinates are fixed by `pi_H` and `iota`.

QED.

## Injectivity refinement on the corridor branch

The mounted Chirality-Corridor source describes the S3-class corridor as **embedded within an S4 organizational domain**. On that branch, take `j_T` to be the corresponding embedding of the hidden S3 continuation base into the Time-Space organizational domain.

An embedding is injective. Therefore `can:P_H->E` is injective on this pullback:

if

```text
can(t,e)=can(t',e'),
```

then `e=e'`, hence

```text
j_T(t)=pi_E(e)=pi_E(e')=j_T(t'),
```

and injectivity of `j_T` gives `t=t'`.

Thus, on the corridor branch,

```text
eta injective <=> iota=can o eta injective.
```

## Inheritance pullback

If the hidden-base continuation `C_H` satisfies

```text
C o j_T = j_T o C_H,
```

then the Time-Space inheritance morphism induces

```text
j_T^*I : P_H -> P_H
```

by

```text
j_T^*I(t,e)=(C_H(t), I(e)).
```

This is well-defined because

```text
pi_E(I(e))
= C(pi_E(e))
= C(j_T(t))
= j_T(C_H(t)).
```

For the corresponding maps `eta` and `iota`,

```text
eta o I_H = (j_T^*I) o eta
```

is equivalent to

```text
I o iota = iota o I_H.
```

## Closure

```text
TEST_CANONICAL_PULLBACK_EQUIVALENCE = PASS.
```

This closes the **retyping/equivalence question**. It does not prove that the physical hidden-network embedding family is nonempty.

## Guardrail

```text
pullback equivalence != physical embedding witness
```
