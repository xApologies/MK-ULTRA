# Astraeus Dark Matter — E081–E084 Batch

## E081 — turn the E080 spectrum idea into a state-level invariant

E080 used the spectrum/rank of the matched operator difference `DeltaLambda_H`. E081 makes the comparator cleaner. V31 already gives

```text
DeltaLambda_H = Lambda_full - Lambda_vis >=_PSD 0
```

with `DeltaLambda_H != 0` for a genuine multi-port hidden component. A nonzero finite positive-semidefinite matrix has positive trace, therefore

```text
tr(Lambda_full) - tr(Lambda_vis)
= tr(DeltaLambda_H)
> 0.
```

So the full and visible states themselves carry different response traces. Under any structural relabeling of the readable ports, `Lambda -> P Lambda P^T` with `P` a permutation matrix, and trace/rank/spectrum are unchanged.

New closed internal object: `@dm_port_response_trace_invariant`.

This is finite graph/operator mathematics, not a physical observable claim. The remaining question is only whether the boundary projection symmetry acts on this response representation by a trace-preserving similarity/conjugacy.

## E082 — conditionally carry the trace into invariant residue

Source archaeology found a useful contract rather than a bespoke dark-matter rule:

```text
Time-Shell transported invariants include topological organization.
F_p = Inv(Pi^(-1)(p))
```

The Boundary Projection axiom says projection preserves organizational relationships while changing representation, and the v36 Projection/Residue Survival Test explicitly leaves the exact compared invariant inventory to the declared experiment/model.

Define the selected response tag

```text
I_Lambda(N) = tr(Lambda_N).
```

E081 proves `I_Lambda(full)>I_Lambda(vis)`. E082 uses one much narrower working assumption than E080: on this selected response sector, the admissible projection-symmetry action preserves the similarity class (or at least the trace) of `Lambda`. Then `I_Lambda` is invariant under the selected projection symmetry and qualifies as declared residue data. Hence the matched projection-residue bundles are conditionally distinguishable.

New object: `@dm_conditional_response_trace_residue_survival`.

`PD-DM-004` is therefore reduced to the smaller `PD-DM-010`: type one projection-symmetry action on the response representation.

## E083 — the explicit trace distinction survives Q completion

DM 2.1/2.2 already closes the standard Q-completion family and proves that a full/visible residue-bundle distinction cannot be erased merely by appending the standard Q-handoff structure when morphisms preserve the residue-bundle constituent.

Therefore the E082 trace-residue distinction yields, conditionally,

```text
B_full^R not ~=_F B_vis^R
=>
Q_full not ~=_Q Q_vis.
```

New object: `@dm_response_trace_q_handoff_witness`.

No chromatic dictionary, scalar-field identity, or new field ontology is needed for this route.

## E084 — return to UCM Gate 2, but only at one tensor component

The v31 source already types

```text
rho_E : E_U -> R
```

as a scalar native-load readout on admissible UCM source/event states, while explicitly rejecting a global scalar-only factorization of the full stress tensor. V32 separately recovers

```text
@energy_density ENTERS @stress_energy_tensor
```

and proves the weaker fact actually needed here:

```text
Delta rho_read[u] != 0
=>
Delta T_mn != 0.
```

E079 already gives a conditional full/visible event separation. E084 therefore speed-tapes exactly one event-level component property:

```text
Delta rho_E != 0
=>
Delta rho_read[u] != 0
```

for one fixed readable observer/normalization. Nothing stronger is assumed. This conditionally closes UCM Gate 2:

```text
P_T(e_full) != P_T(e_vis).
```

New object: `@dm_conditional_event_density_source_separation`.

The broad `PD-DM-009` and the old density debt `PD-DM-003` are now compressed into one event-scoped question:

```text
PD-DM-011:
prove one source-grounded native-event-density -> readable-density component map
that does not annihilate the selected Delta rho_E.
```

## Current direction

Primary frontier:

```text
@dm_event_density_component_survival
```

Highest-leverage proof debt:

```text
PD-DM-011
```

Next pass: search only the Time-Shell/native-energy/readout neighborhood for one zero-reflecting component map. Do not derive full `P_T`. If this bounded attack stalls, switch to `PD-DM-010` and type the projection-symmetry response action.

## Promotion state

- DM 2.2 baseline mutations: 0
- parent/API promotions: 0
- physical dark-matter promotions: 0
- canonical edge promotions: 0
- unconditional new internal theorem: E081 response-trace invariance
- conditional forward closures: E082, E083, E084
- new working assumptions: 2
- new proof debts: 2, with older debts narrowed/merged
- new live objects: 4
- new QMO records: 4
- new certificates: 4
