# 97 — Time-Shell Adjunction Test

## Test target

For a typed Time-Shell context relation:

```text
f : U -> V,
```

test whether:

```text
f_! dashv f^*.
```

The required universal property is a natural bijection/equivalence:

```text
Hom_V(f_!x, y)
  <->
Hom_U(x, f^*y)
```

for every admissible `x in F(U)` and `y in F(V)` in the declared operator domain.

## Geometry-first formulation

The test does not require calculus. It requires only:

- typed objects;
- admissible arrows;
- composition;
- Identity;
- forward realization;
- sourceward restriction;
- natural compatibility under composition.

## Recursive test protocol

For each candidate operator family:

```text
1. choose finite admissible context/object slice;
2. construct f_! and f^* explicitly;
3. enumerate/characterize arrows on both Hom sides;
4. build the candidate correspondence;
5. test naturality under one Dynamic Closure Recursion step;
6. repeat after closure changes the available Bandwidth Algebra.
```

A candidate that works only before closure but fails after the induced admissibility change is rejected as a universal
Time-Shell adjunction.

## Stronger-than-static requirement

Because the Atlas uses Dynamic Closure Recursion, the adjunction must itself survive admissibility evolution:

```text
f_!^(n) dashv f*^(n)
```

must remain coherent with the induced `A_B^n -> A_B^(n+1)` transition whenever both stages remain in the claimed domain.

## Current verdict

UNPROVED / TESTABLE.
