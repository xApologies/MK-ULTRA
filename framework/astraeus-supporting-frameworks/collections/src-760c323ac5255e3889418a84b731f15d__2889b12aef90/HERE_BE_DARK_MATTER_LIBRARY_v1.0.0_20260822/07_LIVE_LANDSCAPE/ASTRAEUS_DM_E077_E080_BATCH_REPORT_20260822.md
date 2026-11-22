# Astraeus Dark Matter — E077–E080 Batch

## E077 — recover the UCM source-scope closure

Source archaeology found that Atlas v17 had already closed a typing question that the Live Landscape was still carrying too loosely. The recovered UCM readable source projection explicitly consumes occupancy, chirality, adjacency/topology, persistence, redistribution, strain/survivability, and Bandwidth:

```text
T_U(L) = Pi_read^UCM(O, Chi, A, P, Rred, S, B).
```

Therefore UCM-internal topology-bearing telemetry belongs inside the full source ledger `T_U`; it is not a second independent `beta_ext` dark source. This is a source-scope closure only. It does not prove that the projection is nonconstant on the selected hidden direction.

New closed live object: `@dm_ucm_topology_source_scope_inclusion`.

## E078 — restore the two-gate blindness split

V29 factorizes the UCM readout as

```text
Pi_U = P_T o U_dyn.
```

The previous single sensitivity debt compressed two distinct possible failures. The correct gates are:

```text
Gate 1: U_dyn(u_full) != U_dyn(u_vis)
Gate 2: P_T(e_full) != P_T(e_vis).
```

`u_full != u_vis` does not prove Gate 1, and `e_full != e_vis` does not prove Gate 2. `PD-DM-007` is therefore superseded by `PD-DM-008` (dynamic-event survival) and `PD-DM-009` (event-to-source fiber separation).

New diagnostic object: `@dm_ucm_two_gate_factorization`.

## E079 — fast-forward Gate 1 with one corridor witness

Rather than numerically solve the entire R4/R5/R6/R7 selector, select one full-only corridor candidate `C_H` and require only the already-recovered guards: R5 constrained selection, R6 survivability, and R7 persistence. If that candidate is retained in the full event and absent from the visible event, then

```text
U_dyn(u_full) != U_dyn(u_vis).
```

This is registered as a working assumption, not a theorem of global corridor existence.

New conditional object: `@dm_conditional_ucm_dynamic_event_witness`.

## E080 — replace the abstract residue discriminator with an explicit one

The hidden-network response theorem already gives

```text
DeltaLambda_H = Lambda_full - Lambda_vis >=_PSD 0,
```

and the selected two-port bridge has

```text
DeltaLambda_H = w_eff [[1,-1],[-1,1]],  w_eff>0.
```

Hence its spectral discriminator is explicit:

```text
spec(DeltaLambda_H) = {0, 2 w_eff},
rank(DeltaLambda_H) = 1,
trace(DeltaLambda_H) = 2 w_eff > 0.
```

The old generic assumption “some residue discriminator survives” is replaced by a concrete candidate: preserve this response-spectrum invariant in the declared Resolution-R invariant-residue comparison. If preserved, the projection-residue bundles are distinguishable and the already-closed Q-survival theorem carries the distinction into the Q handoff.

New object: `@dm_response_spectrum_residue_discriminator`.

`PD-DM-004` is now narrowed to one question: does boundary projection / invariant residue preserve this explicit response-spectrum discriminator?

## Current direction

Primary frontier:

```text
@dm_response_spectrum_residue_discriminator
```

Highest-leverage proof debt:

```text
PD-DM-004
```

Do one bounded source/API crawl for a response-spectrum -> invariant-residue preservation contract. If none appears, switch immediately to the already-small direct density gate `PD-DM-003`; do not descend generic bundle foundations.

## Promotion state

- DM 2.2 baseline mutations: 0
- parent/API promotions: 0
- physical dark-matter promotions: 0
- canonical edge promotions: 0
- source-derived closures: E077, E078 diagnostic
- new working assumptions: 2
- new proof debts: 2 (with PD-DM-007 superseded)
- new live objects: 4
- new QMO records: 4
- new certificates: 4
