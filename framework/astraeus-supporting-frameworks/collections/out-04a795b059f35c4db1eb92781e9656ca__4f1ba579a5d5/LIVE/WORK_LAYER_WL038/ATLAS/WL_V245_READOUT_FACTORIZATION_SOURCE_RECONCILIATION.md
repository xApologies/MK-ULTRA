# WL-v245 — Readout-Factorization and Corridor-Pullback Source Reconciliation

**QMO:** QMO-AST-DM-WL-129  
**Work layer:** WL-038  
**Parent promotions:** 0  
**Status:** SOURCE RECONCILIATION / PROVENANCE CORRECTION

## Purpose

Reconcile the WL-037/WL-038 geometry-first deductions against the mounted Dark Matter API 2.2 source archive before declaring architectural closure.

## Finding 1 — the readout-factorization theorem already exists in the parent source

Dark Matter API 2.2 source artifact

```text
sources/ATLAS_V36/122_DARK_MATTER_AS_READOUT_FACTORIZATION_DEFECT.md
```

already proves the exact criterion:

```text
G_R = Gbar_R o M_R
```

if and only if `G_R` is constant on every `M_R` fiber, and defines

```text
D_R={(x,y): M_R(x)=M_R(y), G_R(x)!=G_R(y)}.
```

Therefore WL-v241 is not a newly discovered parent theorem. It is a **live-branch recovery and normalization** of the already-source-backed V15 theorem.

This correction strengthens rather than weakens the branch: the factorization criterion is parent-source mathematics and does not depend on the new work layer.

## Finding 2 — the corridor pullback already exists in the parent source

Dark Matter API 2.2 source artifact

```text
sources/ATLAS_V36/04_CORRIDORS_AS_PULLBACKS.md
```

defines a corridor as the pullback

```text
W_gamma := gamma^*(T5)
```

along a path `gamma:I=[0,1]->S3`, and states conditionally that when the Time-Shell bundle is locally trivial along the path,

```text
W_gamma ~= S2 x I.
```

The shared Chirality-Corridor source independently gives the same open-corridor topology and the S3-class interpretation.

Therefore the WL-037 complement-carrier observation

```text
S3 minus two open 3-balls ~= S2 x [0,1]
```

is best classified as an **independent standard-topology realization/cross-check of an already recovered corridor type**, not as a newly created dark carrier ontology.

## Finding 3 — the new work-layer contribution is route closure, not invention of the ingredients

The genuinely new live-work contribution is the composition/retyping:

```text
corridor-native inherited states
-> source-native Time-Shell boundary lift/transport
-> formal invariant residue/Q machinery
-> parent-source stress-energy/gravity/readout gates
-> already-defined DM qualification locus.
```

The work layer is therefore closing the route among pre-existing source-backed objects while preserving every source boundary.

## Ruling

```text
WL-v241 classification:
    LIVE-BRANCH RECOVERY OF PARENT-SOURCE THEOREM

WL-v237 complement carrier classification:
    STANDARD-TOPOLOGY CROSS-CHECK OF SOURCE CORRIDOR TYPE

No parent promotion required.
```
