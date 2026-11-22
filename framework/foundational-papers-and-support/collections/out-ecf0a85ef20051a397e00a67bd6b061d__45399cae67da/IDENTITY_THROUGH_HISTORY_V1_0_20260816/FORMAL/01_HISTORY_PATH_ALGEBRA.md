# 01 — History Path Algebra

## 1. State and history objects

Let `X` be a typed organizational state domain and let `E_H` be the admitted directed transitions.

A finite admissible History is a composable path

```text
h = e_n ... e_2 e_1 : x_0 -> x_n.
```

The path has:

```text
src(h)=x_0,
tgt(h)=x_n.
```

If `tgt(h1)=src(h2)`, History composition is

```text
h2 o h1.
```

Each state has a trivial History `1_x`.

An inverse History is **not** assumed. Therefore the native object is a path category / path algebra, not automatically a groupoid.

## 2. History prefixes

For

```text
h=(e_1,...,e_n)
```

define the prefix History

```text
h|k = e_k ... e_1.
```

Prefix structure lets persistence ask whether Identity survives every stage rather than only the final endpoint.

## 3. History is not coordinate time

History records ordered admissible continuation. A source may later transduce that ordering into clock time, proper time, recursive depth, or another readable ordering. Those identifications are not primitive.

## 4. S3 interpretation

In the Atlas, the principal History carrier is the `S3` continuity domain. A History is therefore first interpreted as an admissible ordered route through continuity addresses. Its local `S2` readouts need not preserve the full History.

## Status

**NATIVE ALGEBRAIC SCAFFOLD, source-aligned with Transduction Geometry D43-D49 and Tome recursion/inheritance.**
