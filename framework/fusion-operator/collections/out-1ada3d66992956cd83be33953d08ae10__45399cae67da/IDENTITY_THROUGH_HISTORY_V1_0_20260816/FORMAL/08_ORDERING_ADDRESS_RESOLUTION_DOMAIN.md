# 08 — Ordering Address and Resolution Domain

This module formalizes the user's Time-Shell marker intuition without treating a clock reading as fundamental time.

## 1. Ordering label

Let

```text
O_R : H_P -> Labels_R
```

assign a readable ordering label to a persistent History class at Resolution `R`.

A clock label such as

```text
12:06
```

is one possible downstream label in `Labels_R`; it is not the underlying History itself.

## 2. Fixed ordering address

For a selected label `o*`, define

```text
TS_o* = { b in dXi | O_R([h_b]) = o* }.
```

## 3. Resolution Domain

Define

```text
D_R(o*) = Read_R(TS_o*).
```

This is the organization distinguishable at the selected Time-Shell ordering address under Resolution `R`.

## 4. Resolution refinement theorem

Let higher Resolution correspond to a finer equivalence relation:

```text
K_R2 subseteq K_R1
```

for `R2 > R1`.

Then there is a canonical surjective forgetting map

```text
q_21 : D_R2(o*) -> D_R1(o*).
```

Therefore increasing Resolution can reveal finer structure at the **same ordering address** without creating a new underlying History.

## 5. Dimensional-access candidate

If a later model types distinguished components as independent Time-Space directions, define

```text
Acc_R(o*)
```

as the set of directions not annihilated by the Resolution quotient.

This is retained as a candidate only. `D_R(o*)` is established here as a readout refinement domain; it is **not yet identified with literal access to extra physical dimensions**.
