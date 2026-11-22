# 2. Core Bandwidth Algebra

## BA-D1 — Native Bandwidth path structure

Define the native Bandwidth structure `C_B` by:

- objects: organizational states;
- generating morphisms: `Gen(B)`;
- identities: `id_x`;
- composition: typed composition wherever target/source match.

For:

```text
a : x -> y
b : y -> z
```

define:

```text
b o a : x -> z.
```

Associativity holds wherever all compositions are typed:

```text
c o (b o a) = (c o b) o a.
```

`C_B` is the category/path-like core. The project retains the historical name **Bandwidth Algebra** and writes the operative closure as `A_B`.

## BA-D2 — Bandwidth Algebra

```text
A_B = Cl_comp( Gen(B) union {id_x} ).
```

`A_B` is the closure of available generators under typed admissible composition and identities.

The exact universal-algebra species is deliberately layered rather than forced:

- native layer: typed partial composition/category-like path algebra;
- ordered-capacity layer: lattice of Bandwidth restrictions/expansions;
- optional linearization: a conventional path algebra over a coefficient semiring/ring when downstream spectral machinery requires it.

## BA-D3 — Corridor word

A corridor is an admissible operator word:

```text
c = a_n ... a_2 a_1
```

with every adjacent pair composable.

Thus corridor existence is an algebraic membership/typing question.

## BA-D4 — History word

A history retains its ordered operator word even when two words have the same endpoint operator. Endpoint equality does not erase history.

## BA-D5 — Bandwidth restriction

For `B' <= B`:

```text
Gen(B') subseteq Gen(B)
A_B' -> A_B.
```

Pure restriction cannot create a new formal transformation.

## BA-D6 — Bandwidth expansion

For `B <= B+`:

```text
A_B -> A_B+.
```

Expansion adds generators and/or admissible composites.

## BA-D7 — Join and meet of Bandwidth states

When two Bandwidth states share a common typed domain:

```text
B1 join B2 := composition-closure of Gen(B1) union Gen(B2)
B1 meet B2 := largest common typed substructure supported by both.
```

These operations describe combined and shared organizational freedom.

## BA-D8 — Saturation

At state `x`:

```text
Sat_B(x) iff Free_B(x) = empty.
```

Saturation is not destruction. The state and `id_x` may persist while no additional nontrivial transformation is currently admissible.

## BA-D9 — Modifier

An artifact, occupancy pattern, boundary, or persistent structure may modify Bandwidth via a typed map:

```text
M : A_B -> A_B'.
```

A modifier must be classified as restriction, expansion, redirection, or mixed transformation. This resolves the source statement that persistence can consume freedom while also increasing coherence: not every persistence event is a pure restriction.
