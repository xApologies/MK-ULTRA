# 48 — Geometry-First Refactor

Atlas v6 restores the explicit AERA rule:

> Calculus is not native substrate mathematics. It is a readable continuum approximation.

The following v5 constructions are therefore retyped:

| v5 smooth expression | v6 native object | smooth/readable specialization |
|---|---|---|
| `UT(S^3)` as primitive | Direction/Address Bundle over continuity domain | `UT(S^3)` when the readout is smooth |
| `L(gamma)=integral ||gamma_dot|| ds` | intrinsic path valuation `ell(c)=1` | arclength integral |
| `nabla_T T` bending | finite turning / transport defect | covariant derivative |
| `F=dA+A wedge A` | same-endpoint transport coherence defect / holonomy | curvature 2-form |
| variational action | constrained configuration optimization | Euler-Lagrange limit |
| Jacobi operator | configuration-graph spectral operator | differential Jacobi operator when justified |

No v5 result is deleted. Its status changes from candidate native representation to smooth readout where appropriate.
