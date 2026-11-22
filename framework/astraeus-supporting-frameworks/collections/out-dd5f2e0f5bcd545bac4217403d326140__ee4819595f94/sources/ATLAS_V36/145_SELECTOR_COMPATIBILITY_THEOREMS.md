# 145 — Selector Compatibility Theorems

## Setup

Let `C_feas` be a finite nonempty feasible corridor set. Let

```text
Xi : C_feas -> O_Xi
S  : C_feas -> O_S
```

be score maps into totally ordered sets sufficient to define `Argmax Xi` and `Argmin S`.

Set

```text
C_Xi = Argmax Xi
C_S  = Argmin S
C_*  = C_Xi intersect C_S.
```

No calculus, probability, metric, or scalar normalization is required.

## Theorem V19-T1 — simultaneous-selection criterion

There exists a corridor satisfying both recovered selection rules if and only if

```text
C_* != empty.
```

### Proof

A corridor satisfies both rules exactly when it belongs to both extremizer sets. By the definition of set intersection, such a corridor exists exactly when their intersection is nonempty. QED.

## Corollary V19-C1 — uniqueness

If

```text
|C_*| = 1,
```

then the two rules jointly select a unique corridor.

If

```text
|C_*| > 1,
```

the recovered selector layer alone is underdetermined.

## Theorem V19-T2 — opposite-order equivalence

Suppose that for every distinct pair `c1,c2 in C_feas`,

```text
S(c1) < S(c2)
iff
Xi(c1) > Xi(c2).
```

Then

```text
Argmin S = Argmax Xi.
```

### Proof

Let `c` minimize `S`. For every `d != c`, `S(c) < S(d)`, so by the assumed opposite ordering `Xi(c) > Xi(d)`. Hence `c` maximizes `Xi`. The reverse implication is symmetric. QED.

## Corollary V19-C2 — strictly decreasing constitutive representation

If there exists a strictly decreasing function `f` on the realized strain values such that

```text
Xi(c) = f(S(c))
```

for all feasible corridors, then

```text
Argmin S = Argmax Xi.
```

This is a mathematical sufficient condition only. V19 does **not** claim that the source supplies such an `f`.

## Theorem V19-T3 — selector conflict certificate

If

```text
C_* = empty
```

while the two source rules are asserted to govern the same corridor-selection event, then the combined model is inconsistent at that event unless at least one of the following is changed explicitly:

```text
domain typing
stage assignment
score definition
feasibility constraints
source priority / supersession status.
```

A post-hoc weighted average does not resolve the source conflict; it introduces a new selector.
