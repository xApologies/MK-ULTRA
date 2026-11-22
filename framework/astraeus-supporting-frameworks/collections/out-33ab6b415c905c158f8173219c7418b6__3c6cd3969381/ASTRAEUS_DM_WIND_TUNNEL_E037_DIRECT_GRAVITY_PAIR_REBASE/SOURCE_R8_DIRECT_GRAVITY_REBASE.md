# WL-v261 — Direct-Gravity Handoff Precedence Reconciliation

**Work layer:** WL-041  
**Status:** CONTINUITY CORRECTION / SOURCE-GROUNDED REBASE  
**Parent promotions:** 0

## Problem found in R7

WL-v258 / P033 carried an older source-level requirement forward into the priority layered branch:

```text
UCM event difference -> require P_T / readable T_mn separation -> gravity.
```

That is a valid **source-component** route, but it is no longer the only or primary gravity test in the live branch.

An earlier later-stage work-layer rebase, WL-v146, had already recovered the direct UCM gravity handoff:

```text
Read_G^R
=
MetricGravityReadout_R
 o TimeShellProjection_R
 o ContinuityPerturbation_R
 o GravitonProjection_R
 o U_UCM.
```

and explicitly ruled:

```text
No new scalar density profile and no new global P_T formula is required for this direct gravity comparison.
```

Parent DM2.2 v27 independently gives the direct Time-Shell criterion

```text
G_TS = Pi_T o A_g,
```

with full-vs-visible separation when

```text
G_TS(response_full) != G_TS(response_visible).
```

## Reconciliation

The priority layered branch is therefore retyped:

```text
PRIMARY:
explicit full/visible pair
-> UCM incidence/dynamic separation
-> existing gravity-admissibility / Time-Shell projection
-> readable metric/gravity comparison.

OPTIONAL SUFFICIENT COMPONENT CHECK:
UCM telemetry/density
-> readable stress-energy T_mn
-> fixed-boundary GR comparison.
```

`T_mn` remains crucial for GR/source accounting and for the final parent qualification locus where required, but it is **not a mandatory intermediate bottleneck before testing the already-recovered direct gravity channel**.

## Remaining direct-gravity gate

Parent v27 still requires an exact gravitational/tensor admissibility role `A_g`. Its existence/role is recovered; complete operator typing remains open.

Therefore this correction removes a duplicated bottleneck without claiming a gravity witness.
