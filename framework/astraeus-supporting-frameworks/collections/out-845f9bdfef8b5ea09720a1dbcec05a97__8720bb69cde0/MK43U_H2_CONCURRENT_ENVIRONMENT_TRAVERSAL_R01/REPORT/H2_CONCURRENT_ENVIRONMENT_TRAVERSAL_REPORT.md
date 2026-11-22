# MK43 Ultra — Concurrent H + H Environment Traversal R01

## Run status

**ACTUALLY EXECUTED.** Two independent copies of the supplied Hydrogen v2 manifold were instantiated as `H_A` and `H_B`, injected concurrently into one shared ER-foam environment, traversed through `T0 -> T7`, and then passed through three `R0 -> R7` relational-ecology cycles.

This run uses a **reconstructed source-grounded execution layer**, because the supplied Pipeline 1 scaffold explicitly says it is not a full simulator and Pipeline 2 supplies reference pseudocode rather than bodies for all operators. The reconstruction is fully included in `RUNNER/` and does not contain an `H + H -> H2` rule.

## What was held fixed

- The 13 supplied H-v2 source channels were not edited.
- `H_A` and `H_B` remained ancestry-distinct throughout the run.
- R0-R7 never rewrote the supplied chirality field.
- The environment inherited the supplied ER-foam tile and reacted to both manifolds.
- The H-specific pair-closure field remained a manifold property. It was allowed to enter R4 as a candidate; it was not an output target.

## T0 -> T7 observation

The two manifolds were present concurrently from T0.

| Stage | temporal category | env |chi| mean | persistent env memory | Time-Shell interface mean |
|---|---|---:|---:|---:|
| T0 | time-independent | 0.000000000 | 0.000000000 | 0.000000000 |
| T1 | time-independent | 0.001239482 | 0.000000000 | 0.000000000 |
| T2 | time-independent | 0.003181401 | 0.000000000 | 0.000000000 |
| T3 | time-independent | 0.005628340 | 0.000000000 | 0.000000000 |
| T4 | time-independent | 0.007131460 | 0.000000000 | 0.002510460 |
| T5 | NOT(time-independent); persistence/Time-Shell admissible | 0.010107974 | 0.003501727 | 0.003686397 |
| T6 | temporally meaningful interaction regime | 0.013274571 | 0.009850903 | 0.005454222 |
| T7 | stable recursive identity / temporal history readable | 0.011947114 | 0.008865812 | 0.005454222 |


The key transition is T5. Environmental chirality polarization already exists earlier, but **persistent environmental memory remains exactly zero through T4**. At T5 the runner changes from ER persistence index `p=0` to `p=1`, the persistent-memory field becomes nonzero (`0.003501727` mean), and the Time-Shell interface field is now active (`0.003686397` mean; `0.035923032` max).

This implements the discrete category change as:

`T0-T4 = time-independent`

`T5 = NOT(time-independent); persistence / Time-Shell admissible`

rather than silently equating T5 with ordinary downstream time dependence.

The shared environment is measurably reactive. At T6 its mean absolute chirality polarization reaches `0.013274571`, then relaxes to `0.011947114` at T7 while retaining nonzero topology memory.

## R0 -> R7, three cycles

| Cycle | gross A->B | gross B->A | R4 candidate | recoverability | R5 margin | R6 survival | stable pair edge |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 0.039533175 | 0.039533175 | 0.209228382 | 0.599076746 | 0.507772631 | 0.774060671 | True |
| 2 | 0.039533175 | 0.039533175 | 0.203878580 | 0.605371284 | 0.517369193 | 0.776629170 | True |
| 3 | 0.039533175 | 0.039533175 | 0.201749613 | 0.608540292 | 0.521951929 | 0.777844993 | True |


The R2 transfer is **grossly nonzero but net symmetric**. Each cycle moves about `3.953%` of one manifold's continuity inventory in each direction across the shared surface, while each H inventory remains conserved and the two identities do not merge.

R4 produces a genuine pair-corridor candidate. R5 does not select it by name; it selects it because its recoverability margin stays positive. R6 passes every source-stated survivability gate in all three cycles.

### R7 topology

**Post-run classification:** `H2-class weak symmetric shell-sharing ecology`.

Graphically, the result is:

`H_A  -- stable shared corridor --  H_B`

not:

`H_A + H_B -> one merged identity`.

The final continuity inventory error is `0.000e+00` and chirality rewrite is zero.

## Post-run benchmark check

Only after the run was complete, the result was compared with the Pipeline 2 H+H benchmark:

- expected: `weak symmetric shell-sharing equilibrium`
- must not: `bounded nitrogen corridor, topology merger, runaway strengthening`
- success shape: `coupling persists across full-cycle recursion and saturates at stable equilibrium`

**Benchmark-shape match:** `True`.

The executed topology has symmetric shell sharing, no identity merger, no runaway strengthening, and the pair edge survives all three R0-R7 cycles.

## Ablation check

The same run was repeated with only the H-v2 `pair_closure_topology_H2` input zeroed. The environment and all universal pipeline rules were unchanged.

**Ablation final pair edge:** `False`.

R4 then generated zero pair-corridor candidate and R5/R6 did not create a pair edge. This demonstrates that the environment itself does not contain a hidden `hydrogen -> H2` rule; the interaction branch depends on the manifold-supplied pair-closure topology.

## Sensitivity

The R5 corridor was re-scored under candidate weighting powers 1, 2, and 3 and burden multipliers 0.5, 1, 2, and 4. **11 of 12** tested cases retain a positive margin. The single failure is the deliberately severe combination `candidate_weight_power=3` with `burden_multiplier=4`; this supplies an explicit failure boundary rather than a claim of unlimited robustness. The exact rows are in `SENSITIVITY/R5_recoverability_sensitivity.csv`.

The T5 source-style binary N6 interface was also extracted at five persistence thresholds. The interface remains nonempty throughout the sweep; details are in `SENSITIVITY/T5_timeshell_boundary_threshold_sweep.csv`.

## What this run establishes inside the reconstructed mathematical environment

1. Two independent H mathematical objects can be carried concurrently through one shared ER-foam ecology.
2. The environment acquires a joint chirality response rather than remaining neutral.
3. The T5 persistence transition creates the first persistent environmental memory and activates a Time-Shell-relevant boundary field.
4. The two H objects enter nonzero symmetric shell sharing without identity merger.
5. Their manifold-supplied pair-closure topology generates an R4 corridor candidate.
6. That candidate remains recoverable at R5 and survivable at R6 for three cycles.
7. The resulting R7 graph is one stable pair corridor between two preserved H identities, which is therefore classified after the run as H2-class topology.

## Boundary

This is an execution of the declared reconstructed mathematical model. It is not a claim that the lost historical runner has been recovered, and it is not a claim of experimental atomic-physics validation. The complete reconstruction choices are frozen in `LEDGER/OPERATOR_CONTRACT.json` so they can be challenged or replaced individually without changing the source data.
