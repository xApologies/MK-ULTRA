# 51 — Finite Turning / Configuration Geometry

Let a normalized configuration be

```text
c = ((p_0,d_0),...,(p_n,d_n)).
```

For each adjacent stage, let

```text
P_i : Dir(p_i) -> Dir(p_{i+1})
```

be the declared admissible direction transport.

Define the turning defect

```text
delta_i = Dist_Dir(d_{i+1}, P_i(d_i)).
```

where `Dist_Dir` is a declared geometric comparison on direction classes.

A native configuration score can be any admissibly defined algebraic/geometric functional such as

```text
B_turn(c) = sum_i w_i * delta_i^2
```

when scalar valuation is useful. The primary data are the defects `{delta_i}`, not the summation itself.

Configuration selection is then written without variational calculus:

```text
c* in ArgOpt { Cost(c) | c in U_1 and all Atlas admissibility constraints hold }.
```

`ArgOpt` is deliberately generic: a local theory must declare whether it means minimum cost, maximum continuity efficiency, lexicographic constraint selection, or another ordering.
