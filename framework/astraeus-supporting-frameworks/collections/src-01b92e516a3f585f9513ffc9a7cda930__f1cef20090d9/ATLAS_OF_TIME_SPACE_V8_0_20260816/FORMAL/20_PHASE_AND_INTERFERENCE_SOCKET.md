# 20 — Phase / Interference Socket

## Scope

This file does not reopen the full quantum problem. It records the exact Atlas location at which relative corridor history can become a readable phase.

Let two admissible reversible corridors connect the same addresses:

```text
gamma_L, gamma_R : p_alpha -> p_beta.
```

Their relative chirality holonomy is:

```text
H_LR^chi
=
(P_gamma_R^chi)^-1 o P_gamma_L^chi.
```

Let a downstream quantum phase representation exist:

```text
rho_phase : G_chi -> U(1).
```

Then define:

```text
rho_phase(H_LR^chi)
=
exp(i Delta_phi_LR).
```

If the local quantum readout has amplitudes `psi_L` and `psi_R`, the ordinary interference cross term has the form:

```text
2 Re[ exp(i Delta_phi_LR) psi_L^* psi_R ].
```

The Atlas contribution is the upstream address of `Delta_phi_LR`:

```text
relative corridor history
-> chirality holonomy
-> phase representation
-> readable interference.
```

## Resolution condition

Distinct formal corridors can remain observationally identical at a coarse Resolution:

```text
gamma_L != gamma_R
but
rho_R(P_gamma_L^chi)=rho_R(P_gamma_R^chi).
```

This preserves the previously recovered Hidden Formal Corridor theorem as the algebraic background for unresolved path identity.

## Status

**CANDIDATE BRIDGE SOCKET, NOT YET PROMOTED TO QUANTUM THEOREM.**

The file is retained because it gives a mathematically exact target for later recovery of the original double-slit solution branch.
