# Astraeus Dark Matter — E085–E088 Batch

## E085 — stop chasing the wrong generic density carrier

The bounded source crawl found a correction rather than the desired one-line calibration map. V33 proves that the scalar native density `rho_E` is a weighted compression of the Resolution-level profile `bold_rho_E^R`; it is not the universal spatial carrier into Time-Shell field-intensity translation.

The source-backed generic target is

```text
Delta bold_rho_H^R
  -> Beta_R
  -> BasinOrg_R
  -> F_TS^B
  -> FieldIntensity_R
  -> C_rho,u
  -> Delta rho_read[u].
```

`Beta_R` is partial and the remaining fidelity/calibration gates are open. Therefore E084's event-component assumption is preserved only as a local conditional shortcut. `PD-DM-011` is parked as an alternate profile/readout lane instead of becoming a new foundational excavation.

New diagnostic object: `@dm_density_profile_readout_factorization_gate`.

## E086 — explicit native continuity witness from the two-port network

The direct response lane is much cleaner. E063 supplies

```text
DeltaLambda_H
= w_eff [[1,-1],[-1,1]],
w_eff>0.
```

V27 proves

```text
Delta(deltaC)_P = -DeltaLambda_H c_P.
```

Choose the relative-port contrast

```text
c_* = (1,-1)^T.
```

Then

```text
DeltaLambda_H c_*
= 2 w_eff (1,-1)^T,
```

so

```text
Delta(deltaC)_P(c_*)
= -2 w_eff (1,-1)^T
!= 0,
```

and

```text
||Delta(deltaC)_P(c_*)||^2
= 8 w_eff^2 > 0.
```

This is an explicit finite hidden-vs-visible continuity-response witness. It requires no density calibration, chromatic map, UCM stress-source formula, or residue/Q handoff.

New closed internal object: `@dm_explicit_two_port_continuity_residual_witness`.

## E087 — attach that exact witness to the already-recovered Time-Shell gravity gate

The source gravity chain is

```text
continuity perturbation
  -> tensor/TT admissibility A_g
  -> Time-Shell projection Pi_T
  -> readable metric perturbation.
```

Define only where typed

```text
G_TS := Pi_T o A_g.
```

V27 gives the exact nonlinearity-safe criterion:

```text
G_TS(-Lambda_full c_*)
!=
G_TS(-Lambda_vis c_*)
```

iff the selected hidden-network difference is gravitationally distinguishable through this direct channel.

E086 already proves the two inputs differ. Distinct input still does not imply distinct output, so the remaining question is one projection fiber—not a new gravity theory.

New typed gate: `@dm_two_port_timeshell_gravity_fiber_test`.

New proof debt: `PD-DM-012`.

## E088 — speed-tape one gravity fiber and move

Rather than derive global `A_g`, a complete kernel for `Pi_T`, or any separate live gravity model, E088 makes one local working assumption:

```text
WA-DM-E088-001:
G_TS(-Lambda_full c_*)
!=
G_TS(-Lambda_vis c_*).
```

Combined with the already-carried matched ordinary-matter readout scaffold,

```text
M_R(N_full)=M_R(N_vis),
```

this places the selected pair in the formal dark-readout defect:

```text
matter channel identifies the pair,
gravity channel separates the pair.
```

New conditional object:

```text
@dm_conditional_direct_timeshell_dark_readout_witness.
```

This direct route bypasses the current UCM event-density gate, chromatic/basin reconstruction, and residue/Q branch for the purpose of **dark-readout scouting**. Those branches remain intact as independent cross-checks and as possible requirements of the stronger full qualification locus.

## Current direction

Primary frontier:

```text
@dm_two_port_timeshell_gravity_fiber_test
```

Highest-leverage proof debt:

```text
PD-DM-012
```

Next operation: attack only the selected `G_TS` fiber. Search the existing tensor/TT admissibility and Time-Shell projection neighborhood for one criterion that either separates or kills this explicit pair. Do not derive a separate gravity model. If the selected fiber stalls, return to `PD-DM-010` or the V33 profile route.

## Promotion state

- DM 2.2 baseline mutations: 0
- parent/API promotions: 0
- physical dark-matter promotions: 0
- canonical edge promotions: 0
- source-route correction: E085
- unconditional internal closure: E086
- typed open gate: E087
- conditional dark-readout closure: E088
- new working assumptions: 1
- new proof debts: 1
- new live objects: 4
- new QMO records: 4
- new certificates: 4
