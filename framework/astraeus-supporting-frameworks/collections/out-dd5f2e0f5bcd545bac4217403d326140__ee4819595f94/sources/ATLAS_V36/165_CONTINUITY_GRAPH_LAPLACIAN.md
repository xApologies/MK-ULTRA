# 165 — Continuity Graph Laplacian

## Purpose

V23 proved that a pure divergence-free circulation cannot enter the established direct gravity channel merely by being added to the continuity flow.

The next question is whether the **continuity organization itself** changes the redistribution operator.

This file derives that dependence directly from the already-recovered finite ER continuity law. No new dark field is introduced.

---

## 1. Persistent continuity network

Let

```text
N=(V,E)
```

be a finite persistent continuity support selected by the existing R4-R7 machinery.

Choose an arbitrary orientation of the edges only for bookkeeping and define the incidence matrix

```text
B_N : R^E -> R^V.
```

For each edge `e=(i,j)`, recover the local response coefficient

```text
w_e = kappa_ij A_ij >= 0.
```

Let

```text
W_N = diag(w_e).
```

This uses the already-recovered constitutive flow relation

```text
Phi_ij = kappa_ij A_ij (C_j-C_i).
```

---

## 2. Edge flow in matrix form

Let

```text
c in R^V
```

be the finite continuity-state vector.

With the chosen orientation, the edge-difference vector is

```text
B_N^T c.
```

Hence the constitutive flow is

```text
phi = - W_N B_N^T c
```

up to the global sign convention chosen for orientation.

The runtime-capacity result from v20-v21 remains an independent finite bound:

```text
|phi_e| <= T_run(e).
```

Therefore

```text
w_e = local small-signal response coefficient
T_run(e) = globally realizable finite flow ceiling
phi_e = realized flow.
```

These three objects must not be conflated.

---

## 3. Redistribution operator

The recovered nodewise redistribution is the incidence divergence:

```text
delta C = B_N phi.
```

Substitution gives

```text
delta C = - B_N W_N B_N^T c.
```

Define

```text
L_N := B_N W_N B_N^T.
```

Then

```text
delta C = -L_N c.
```

`L_N` is the weighted graph Laplacian of the persistent continuity network.

### V24-T1 — Network sensitivity theorem

The redistribution operator is determined by the selected adjacency and local ER response coefficients:

```text
N, {kappa_ij A_ij}
        |
        v
      L_N.
```

Therefore two continuity organizations with the same local source vector need not produce the same redistribution response if their weighted Laplacians differ.

This supplies an explicit realization of the previously schematic dependence

```text
R_C^[N].
```

It does not prove that the complete nonlinear closure is globally equal to `L_N`; rather, `L_N` is the exact finite linear redistribution operator induced by the recovered local ER law on a fixed selected support.

---

## 4. Gauge / conservation structure

For every graph Laplacian,

```text
L_N 1 = 0.
```

Thus a uniform continuity offset produces no edge difference and no redistribution.

On a connected component, a source equation

```text
L_N c = s
```

is solvable only when

```text
sum_i s_i = 0
```

unless additional fixed-reference / boundary data are supplied.

After fixing the additive gauge, the response is represented by the Moore-Penrose inverse

```text
c = L_N^+ s.
```

This is finite algebra. No differential continuum approximation is required.

---

## 5. Relation to the v22-v23 cycle branch

For a circulation

```text
z in ker(B_N),
```

one still has

```text
B_N z = 0.
```

Therefore v23 remains correct: a free divergence-free circulation is invisible to the direct `B_N phi` source channel.

However, **adding or removing the relationships that support such a cycle changes `B_N` and therefore can change `L_N`.**

The surviving distinction is therefore:

```text
cycle flow z                  -> direct divergence may vanish
cycle-bearing topology N_z   -> redistribution operator L_N may change.
```

This is the operator-mediated branch in explicit finite form.

---

## 6. Saturation guardrail

The linear constitutive response is valid only while the resulting edge flows remain inside the v20-v21 runtime capacities:

```text
|w_e (c_j-c_i)| < T_run(e)
```

for the unsaturated branch.

When an edge reaches its runtime capacity, the selected feasible-flow family changes and the full R5/R6/R7/nonlinear closure must be re-evaluated.

Therefore `L_N` is an exact local operator on a fixed unsaturated selected support, not a license to ignore finite-capacity closure.

---

## Status

```text
Recovered local ER flow law                    RECOVERED
Incidence representation                       V24 DERIVED
Weighted continuity Laplacian L_N              V24 DERIVED
Network dependence of local redistribution     V24 PROVED
Complete nonlinear gravity closure = L_N       NOT CLAIMED
Dark matter = graph Laplacian                   NOT CLAIMED
```
