# 132 — UCM Full-vs-Visible Source Projection Closure

## Purpose

V16 left a downstream fork:

```text
dark gravity
-> hidden stress-energy
or
-> hidden GR boundary/topology input.
```

The recovered Universal Coupling Mechanism (UCM) sharpens that fork because its **readable stress-energy projection already consumes topology-bearing substrate telemetry**.

This file asks a narrower question:

> When the full UCM coupling ledger and the ordinary visible-matter reconstruction are placed in the same downstream GR problem, what part of the v16 hidden-topology branch remains independent of stress-energy?

The result is a representation theorem. It does not assert that geometry is fundamentally matter.

---

## 1. Recovered UCM source projection

A complete UCM coupling event records at least

```text
L_U
=
(
  O,
  Chi,
  A,
  P,
  Rred,
  S,
  B,
  corridor,
  ancestry,
  residual,
  ...
).
```

The recovered source defines the downstream energy-momentum projection schematically as

```text
T_mn
=
Pi_read(
  O,
  Chi,
  A,
  P,
  Rred,
  S,
  B
).
```

where

```text
O    = occupancy
Chi  = chirality organization
A    = adjacency / topology relation
P    = persistence
Rred = redistribution
S    = strain / survivability
B    = Bandwidth allocation.
```

Thus adjacency/topology, redistribution, and survivability are **already source-side inputs** to the UCM readable energy-momentum object.

Define the full UCM source map

```text
T_U : L_U -> StressEnergy_R
```

by

```text
T_U(L) := Pi_read^UCM(L).
```

---

## 2. Ordinary visible source reconstruction

At Resolution `R`, define an ordinary matter/radiation reconstruction

```text
T_vis^R : L_U -> StressEnergy_R.
```

`T_vis^R` contains only the source contribution reconstructible through the declared ordinary readable sector at that Resolution.

It is **not** assumed to equal `T_U`.

Both objects must live in the same tensor bundle / convention before subtraction is meaningful.

Define the source residual

```text
T_D^R(L)
:=
T_U(L) - T_vis^R(L).
```

The symbol `D` means **dark-source residual relative to the ordinary readable reconstruction**. It does not name a particle or new substance.

---

## 3. External GR data after UCM source compression

V16 used

```text
beta_R
```

for all non-source GR data.

Because UCM already compresses topology-bearing coupling telemetry into `T_U`, v17 separates

```text
beta_ext^R
```

for only those downstream GR inputs **not already represented in `Pi_read^UCM`**, such as declared external/asymptotic initial or boundary data, global solution branch data, and gauge/readout conventions when required.

Then the downstream GR realization is typed as

```text
g_U^R(L)
=
Gamma(
  T_U(L),
  beta_ext^R(L)
).
```

The ordinary visible-source reconstruction in the same GR problem is

```text
g_vis^R(L)
=
Gamma(
  T_vis^R(L),
  beta_ext^R(L)
).
```

The same `beta_ext^R` is intentionally used in both equations.

---

## 4. Theorem V17-T1 — UCM source residual necessity

Assume the full and visible reconstructions use the same deterministic GR solution map `Gamma` and the same external GR data `beta_ext^R`.

If

```text
g_U^R(L) != g_vis^R(L),
```

then

```text
T_U(L) != T_vis^R(L),
```

and therefore

```text
T_D^R(L) != 0.
```

### Proof

If `T_U(L)=T_vis^R(L)` and both calls use the same `beta_ext^R(L)`, then their complete inputs to `Gamma` are identical. Determinism gives `g_U^R(L)=g_vis^R(L)`, contradicting the premise. QED.

This is a necessity result. The converse requires a nondegenerate gravitational response and is not automatic.

---

## 5. Corollary V17-C1 — UCM-internal topology is not an independent downstream source branch

Suppose a change in native adjacency/topology, chirality, redistribution, strain, persistence, or Bandwidth changes the UCM ledger and is read by `Pi_read^UCM`.

Then any resulting downstream source distinction is already represented by

```text
Delta T_U.
```

Therefore those **UCM-internal source variables do not also need to be inserted as a second independent `beta_ext` dark source** in the same chart.

This narrows the v16 fork:

```text
V16:
  hidden stress-energy
  OR hidden boundary/topology.

V17 UCM specialization:
  UCM-internal topology-bearing load -> T_U
  external GR problem data           -> beta_ext.
```

A topology distinction can remain upstream and geometric while its downstream GR source representation is stress-energy-like.

---

## 6. Nonlinear gravity guardrail

Even though the source residual is additive in a common tensor space,

```text
T_U = T_vis + T_D,
```

v17 does **not** assert

```text
Delta g = Gamma(T_D).
```

For nonlinear GR the correct comparison is

```text
g_full = Gamma(T_vis + T_D, beta_ext)

g_vis  = Gamma(T_vis,       beta_ext)

Delta g = g_full - g_vis
```

when the subtraction is meaningful in the declared common chart/readout.

Thus the Atlas preserves the v14 nonlinear-closure warning.

---

## 7. Dark-sector interpretation

The strongest current statement is now:

```text
ordinary visible source projection
is a partial readout of
full UCM substrate transaction.
```

If the full UCM source produces a gravitational distinction not reproduced by the visible source reconstruction, then the downstream ordinary-GR description contains a nonzero residual source tensor

```text
T_D^R.
```

The upstream carrier of that residual may still be:

- ER adjacency organization;
- persistence;
- redistribution;
- corridor strain;
- Bandwidth allocation;
- chirality-conditioned topology;
- persistent environmental residual organization.

No dark particle is required by this theorem.

---

## Status

```text
UCM Pi_read topology-bearing source inputs             RECOVERED
UCM gravity projection of same substrate transaction   RECOVERED
Full UCM source map T_U                                V17 TYPED
Visible source map T_vis^R                             V17 TYPED
Source residual T_D^R                                  V17 DEFINED
UCM source-residual necessity theorem                  PROVED
UCM-internal topology absorbed into Pi_read source     PROVED BY DECLARED PROJECTION SCOPE
External beta_ext factorization for real galaxies      OPEN
T_D numerical calibration                              OPEN
```
