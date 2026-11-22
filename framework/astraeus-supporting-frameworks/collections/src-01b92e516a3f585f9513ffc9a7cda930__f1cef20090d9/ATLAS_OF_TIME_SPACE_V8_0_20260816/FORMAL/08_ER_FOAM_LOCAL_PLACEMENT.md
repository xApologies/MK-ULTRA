# 08 — ER Foam Local Placement

ER foam is placed inside the localized readable spacetime projection `Sigma_p`.

A recovered boundary-adjacency relation has the form:

```text
E_partial = argmin over A_partial [
    sum_(i,j) W_ij (A_ij - Pi(A_bulk)_ij)^2
    + lambda sum_i kappa_i Phi(A_partial,i)
].
```

Interpretive role:

```text
local chirality organization
 -> admissible adjacency/order
 -> ER-foam/local substrate structure
 -> Helicon and other readable/local modes.
```

## Required future typing

A later Atlas version should explicitly define how:

```text
W_ij = W_ij(chi_i,chi_j,...)
```

or an equivalent chirality-conditioned adjacency law enters the ER-foam minimization/closure object.
