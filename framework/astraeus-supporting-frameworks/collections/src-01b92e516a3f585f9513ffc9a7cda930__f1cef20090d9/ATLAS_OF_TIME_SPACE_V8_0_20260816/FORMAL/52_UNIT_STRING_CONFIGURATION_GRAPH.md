# 52 — Unit String Configuration Graph

Define the configuration graph

```text
Gamma_U = (V_U, E_U, W_U)
```

with

```text
V_U = U_1.
```

An edge

```text
(c_i,c_j) in E_U
```

exists iff there is at least one typed Bandwidth-Algebra generator that transforms `c_i` into `c_j` while preserving the required Unit String invariant and all active chirality/persistence/admissibility constraints.

Weights `W_U` may record a tuple rather than one scalar:

```text
w_ij = (
  bandwidth_status,
  chirality_compatibility,
  identity_witness,
  holonomy_change,
  persistence_status,
  configuration_cost
).
```

Scalarization is downstream and task-specific.

This graph is the native candidate phase/configuration space for coherent Unit-String restructuring.
