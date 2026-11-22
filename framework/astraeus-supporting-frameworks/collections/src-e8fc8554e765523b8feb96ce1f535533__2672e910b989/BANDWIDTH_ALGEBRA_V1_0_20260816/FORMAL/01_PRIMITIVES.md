# 1. Primitives

Let `X` be a typed organizational domain. In the current Atlas, `X` may be Time-Space `T^5`, an `S^3` continuity domain, a localized `S^2` projection, or another declared subdomain.

## BA-P1 — State class

`Ob(X)` is the class of addressable organizational states/configurations in `X`.

## BA-P2 — Admissibility relation

```text
Adm_X(x,y)
```

means that a transformation from state `x` to state `y` is organizationally admissible in `X`.

## BA-P3 — Primitive transformation

A primitive available transformation is typed:

```text
a : x -> y
```

with `Adm_X(x,y)` satisfied.

## BA-P4 — Formal Bandwidth state

A Bandwidth state `B` determines a generator assignment:

```text
Gen_B(x) = { a : x -> y | a is currently available under B }.
```

Bandwidth is therefore not merely “how much room remains.” Its native content is **which transformations remain supportable**.

## BA-P5 — Identity transformation

Every state retains:

```text
id_x : x -> x.
```

Identity is needed for algebraic closure but is not counted as nontrivial remaining freedom.

## BA-P6 — Nontrivial freedom set

```text
Free_B(x) = Gen_B(x) \ {id_x}.
```

A state is operatively saturated when `Free_B(x)` is empty.

## BA-P7 — Recursive depth

Bandwidth may be indexed by recursive depth `d`, but different Resolution readouts may inherit from the same formal Bandwidth object. A depth-indexed scalar `B_d` is therefore not automatically a distinct ontological Bandwidth.
