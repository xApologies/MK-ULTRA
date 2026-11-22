# AST-DM-WL-P009 — UCM Source-Projection Quotient Test

**Work layer:** WL-015  
**Status:** STRUCTURAL SOURCE-SENSITIVITY PROTOCOL — NOT PARENT PROMOTED

## Goal

Determine whether a controlled History/corridor difference that survives as a finite continuity-operator difference also survives the recovered UCM readable source projection.

## P009-0 — Select History pair

Use either a source-native pair or the WL-v138 structural witness:

```text
H0,H1.
```

Require controlled ordinary matter comparison.

## P009-1 — Recover/admit UCM ledger pair

Construct only from declared source variables:

```text
L0,L1 in L_U.
```

Record which components differ:

```text
O,Chi,A,P,Rred,S,B,corridor,ancestry,residual,...
```

Do not infer unrecorded component changes.

## P009-2 — Evaluate source-projection class

Recover/evaluate

```text
Pi_U^R(L0),
Pi_U^R(L1).
```

Classify:

- `SOURCE_MERGED` if equal;
- `SOURCE_SEPARATED` if unequal;
- `SOURCE_UNINSTANTIATED` if no source-evaluable ledger instance exists.

## P009-3 — Cross-check v138

If using the minimal hidden-corridor witness, verify the ledger records the changed operative adjacency/corridor structure corresponding to

```text
Lambda0 != Lambda1.
```

Do not infer source separation merely from this difference.

## P009-4 — Source tensor residual

Only in `SOURCE_SEPARATED`, record the downstream tensor difference

```text
DeltaT_U^R = Pi_U^R(L1)-Pi_U^R(L0)
```

in one declared common tensor convention.

## P009-5 — Ordinary-GR admission

Hold

```text
beta_ext^R
```

fixed across the comparison and test whether the selected GR solution/readout distinguishes the two source tensors.

A source difference that is observationally degenerate does not pass the dark-gravity gate.

## P009-6 — Resolution profile

If compatible Resolution projections are available, repeat across `Res` and record

```text
Pers_U(H0,H1).
```

Compare its emergence threshold with the matter/QFT threshold from P007/P136.

## Firewalls

```text
ledger difference != source-projection difference
```

```text
DeltaLambda != DeltaT_U != Delta g
```

```text
rho_E != full UCM ledger != T_mn
```
