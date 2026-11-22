# AST-DM-WL-P024 — Controlled ER-Throat Incidence Pair Test

**Work layer:** WL-034  
**Status:** EXECUTABLE SOURCE-RECOVERY PROTOCOL

## Objective

Test the smallest currently exposed API question:

```text
Does the controlled H0/H1 rotational-History pair produce different source-admitted ER-throat incidence or weighted-adjacency records?
```

## Inputs

- `H0`: common-mode/trivial relative orientation History.
- `H1`: persistent nontrivial relative orientation/shear/holonomy History.
- Same declared local Resolution and Bandwidth constraints.
- Same local matter/QFT readout requirement is retained for later qualification but is **not** assumed to have passed merely because Stage 1 passes.

## Stage A — representation admission

For each Hk, recover only source-supported mappings from the detailed mote state into the API's `@chirality_labelled_mote` class.

If either mapping is unavailable, STOP with `REPRESENTATION_SEAM_OPEN`. Do not invent it.

## Stage B — incidence recovery

Recover:

```text
I_k := ERThroatIncidence(H_k)
```

through the existing API handle `@er_throat_incidence`.

## Stage C — weight recovery

If incidence exists, follow the source-backed chain to `@weighted_adjacency` and recover `W_k`.

## Stage D — compare

PASS if:

```text
I_0 != I_1
```

or:

```text
W_0 != W_1
```

NULL if both are equal.

## Stage E — stop boundary

Do not continue to hidden-state embedding, metric-action selection, UCM, or gravity unless Stage D passes.

If Stage D passes, the next exact ingress is the already-registered `@er_foam` / `@dm_er_branch_readout_separation` seam.

## Guardrails

- orientation-history ancestry != pair separation;
- finite edge assembly != edge selection;
- chirality-labelled mote != modern detailed mote by identity;
- ER-throat incidence != dark matter;
- weighted adjacency != stress-energy or gravity;
- no parent promotion.
