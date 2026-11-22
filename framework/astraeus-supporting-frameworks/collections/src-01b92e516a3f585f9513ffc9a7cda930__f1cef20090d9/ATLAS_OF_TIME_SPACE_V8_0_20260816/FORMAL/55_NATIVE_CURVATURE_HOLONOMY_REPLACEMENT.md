# 55 — Native Curvature as Transport Defect

Atlas v4-v5 used smooth connection curvature expressions as exploratory readout mathematics. Atlas v6 restores the native Transduction Geometry definition.

For two admissible paths

```text
p,q : a -> b
```

and state `x` at `a`, compare

```text
P_p(x)
P_q(x).
```

Transduction Curvature is the typed coherence defect

```text
Curv_T(p,q;x) := Def( P_p(x), P_q(x) ).
```

For a closed loop `ell`, the returned transport class defines holonomy.

```text
Hol(ell;x) = [P_ell(x)].
```

The smooth formulas

```text
F = dA + A wedge A
R^rho_sigma_mu_nu
```

are downstream realizations when a smooth representation exists.

This native definition handles corners, discrete changes, transient ER incidences and topology-sensitive paths without first assuming differentiability.
