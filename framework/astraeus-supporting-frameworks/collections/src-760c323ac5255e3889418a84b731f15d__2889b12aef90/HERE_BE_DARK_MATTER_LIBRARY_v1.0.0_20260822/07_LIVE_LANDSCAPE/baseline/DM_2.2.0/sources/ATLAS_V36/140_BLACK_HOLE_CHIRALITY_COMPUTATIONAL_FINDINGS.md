# 140 — Black-Hole Chirality Computational Findings

## Status

Read-only structural analysis of the recovered 32x32x32 experimental projection.

The source is synthetic/model-generated. These results test internal organization, not nature.

## 1. Adjacency coherence

Recovered six-neighbor graph:

```text
agreement edges = 82872
conflict edges  = 12360
total           = 95232
agreement density = 0.8702116935
conflict density  = 0.1297883065
```

A 200-trial count-preserving random-shuffle control gives:

```text
mean conflict density = 0.4980884577
sd                    = 0.0016390651
observed z            = -224.70
```

Interpretation:

The archived field is strongly spatially organized relative to a density-matched random occupancy field.

This does not establish physical significance because the field generator itself may impose that organization.

## 2. Connected organization

Face-adjacency components:

```text
+1 state:
  4 components
  largest = 15413 / 15420 = 0.999546

-1 state:
  4 components
  largest = 17344 / 17348 = 0.999769

two-sided interface:
  1 connected component
  12826 / 12826 cells
```

Thus the occupied and complement descriptions are each almost entirely coherent, while their two-sided interface is one connected distributed network.

## 3. Conflict-edge enrichment in black-hole boundary channels

Mean recovered channel value on conflict edges divided by agreement edges:

```text
horizon channel             1.738 x
shell-curvature proxy       2.200 x
near-shell response         1.518 x
outer coupling              1.425 x
inner coupling              1.698 x
```

This descriptively aligns chirality arbitration/conflict with the source's black-hole shell/coupling region.

Again, this is not independent validation because the source channels were created within the same experimental black-hole projection.

## 4. Radial transaction ordering

Using the source's normalized grid coordinates, radial peak locations are approximately:

```text
inner coupling          r ~ 0.5875
horizon                 r ~ 0.6125
outer coupling          r ~ 0.6375
shell-curvature proxy   r ~ 0.6625
near-shell response     r ~ 0.7125
```

The source itself therefore expresses an ordered structure:

```text
interior coupling
-> horizon
-> exterior coupling
-> shell-curvature region
-> environmental response.
```

V18 treats this as a useful computational **transaction-layer scaffold**, not as a newly discovered physical black-hole profile.

## 5. Relevance to the dark-matter cartography

The archive is useful because it supplies precisely the black-hole-marked preselection neighborhood missing from v17:

```text
BH core/horizon/environment channels
+ chirality lattice
+ adjacency relation set
+ shell-facing conflict/agreement candidates
+ R4/R5/R6 domain laws.
```

What remains missing is a numerical instantiation of the R5 recoverability/strain scoring and edgewise Transition Capacity sufficient to compute `Phi_H^*` and `rho_E,H^R` without invention.

The correct next step is therefore to recover those quantities from existing source material or leave them unresolved—not fit astronomy around the gap.
