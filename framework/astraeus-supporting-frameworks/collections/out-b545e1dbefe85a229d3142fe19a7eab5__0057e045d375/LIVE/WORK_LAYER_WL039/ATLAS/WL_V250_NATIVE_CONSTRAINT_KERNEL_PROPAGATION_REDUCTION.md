# WL-v250 — Native Constraint-Kernel Propagation Reduction

**QMO:** QMO-AST-DM-WL-134  
**Work layer:** WL-039  
**Protocol:** AST-DM-WL-P032  
**Parent promotions:** 0  
**Status:** CONDITIONAL REDUCTION PROVED / INITIAL PHYSICAL CORRIDOR SEED OPEN

## Problem

P031 Stage W0 requires a corridor pair in the physical native domain

```text
X_corr,phys^R = X_corr^R intersect ker(C_native).
```

Corridor admissibility alone must not be mistaken for physical constraint-kernel membership.

## Source structures

Time-Space API 4.3 defines native constraints

```text
C_A, C_C, C_chi, C_W, C_T
```

for

```text
admissibility,
continuity,
chirality orbit,
topology class,
Time-Shell projection.
```

Physical native states satisfy

```text
C_a |Psi_phys> = 0,
```

and the native update preserves the physical kernel:

```text
U ker(C) subseteq ker(C).
```

The Chirality-Corridor source separately requires continuation compatibility, chirality compatibility, persistent identity, invariant residue preservation, Resolution, Bandwidth, recursive closure, and target closure.

The two lists overlap structurally, but they are not source-declared identical constraint systems.

## WL039-T3 — Kernel propagation reduction

Let

```text
Psi_0
```

be an initial corridor state satisfying

```text
Psi_0 in ker(C_native).
```

Suppose every actual corridor update step `U_n` used by the selected realization is typed as a native admissible update with

```text
U_n ker(C_native) subseteq ker(C_native).
```

Then every finite corridor stage

```text
Psi_n = U_(n-1)...U_1 U_0 Psi_0
```

also lies in

```text
ker(C_native).
```

### Proof

`Psi_0` lies in the physical kernel by hypothesis. Kernel preservation sends `Psi_0` into the kernel after one update. Repeating the same implication finitely many times preserves kernel membership at every stage. QED.

No derivative or integral is required.

## Exact reduction of W0

The physical-domain problem is therefore reduced from

```text
prove physicality separately at every corridor stage
```

to two source/selection questions:

```text
K0. Find one initial corridor seed Psi_0 in ker(C_native).
K1. Type the selected corridor update as a native kernel-preserving update.
```

If both pass, finite-stage physical kernel membership follows automatically.

## Guardrail

The corridor source writes a recursive update using the Prime Observation Operator and Recursive Closure Operator. Time-Space API 4.3 writes a native update `U` in its constraint algebra.

The current source record does **not** prove

```text
corridor recursive update = U
```

as a universal identity.

That typing remains K1.

Similarly,

```text
boundary state in dXi
```

does not by itself imply

```text
state in ker(C_native).
```

## Ruling

```text
STAGE-BY-STAGE PHYSICALITY PROBLEM: REDUCED.
INITIAL PHYSICAL CORRIDOR SEED: OPEN.
CORRIDOR-UPDATE / NATIVE-U TYPING: OPEN.
```
