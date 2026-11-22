# AST-DM-WL-P006 — Persistent UCM Residual -> Projection-Residue Bundle -> Q/Action Gate-B Test

**Work layer:** WL-010  
**Status:** PROTOCOL CANDIDATE — NOT PARENT PROMOTED

## Goal

Test Gate B without inventing a Helicon bridge, a scalar stress-energy law, or an identity between two different source notions of residue.

## Controlled source family

Prefer the black-hole-anchored S3 History pair as a control family:

```text
F0: Hol_H(gamma_H)=id
F1: Hol_H(gamma_H)!=id
```

while holding the declared localized S2 matter/QFT readout, Resolution, external GR data, and comparison conventions fixed.

The holonomy pair is a control/provenance selection only. It is not assumed to produce a residual.

## Test B0 — UCM event and persistent residual

For each controlled state, form or recover the source-native UCM event

```text
e_i=U_dyn(F_i).
```

Extract the ledger residual

```text
r_i=ResidualFieldState(e_i).
```

Require, for a candidate branch,

```text
Persist_R7(r_i)=true
```

and rotational/S3 corridor provenance as required by QMO-052.

Record PASS / FAIL / UNTYPED.

## Test B1 — type firewall and boundary realization

Do not identify `r_i` with `F_p=Inv(Pi^-1(p))`.

Search for or type a source-admissible map

```text
beta_res^R(r_i)
```

into a Persistent-Boundary-supported realization.

If no such map is source-backed, record

```text
B1 = UNTYPED
```

and stop the Q-bundle handoff for that witness.

## Test B2 — Projection Residue Bundle

If B1 passes, apply the existing Time-Space boundary projection / invariant residue machinery.

Required object:

```text
B_r=(M_r,F_r,pi_F,r)
```

or a rigorously declared restriction of the source-defined Residue / Quantum Field Bundle.

Check that its construction is genuinely induced by boundary projection and invariant residue, not by renaming `ResidualFieldState`.

## Test B3 — full-vs-visible source target

For the same UCM transaction/comparison class, recover

```text
T_D^R=T_U-T_vis^R.
```

Require the same external GR problem data in the full and visible reconstruction.

Check the hidden/visible exchange/conservation identity before action selection.

## Test B4 — Q/action core

Search only the admitted Q-completion family first:

```text
C_Q,T^R(B_r,T_D;g).
```

A pass requires one Q whose existing action/state constituent `S_Q`:

- extends the admitted residue bundle;
- lies in the covariant hidden-action family;
- has metric variation `V_g[S_Q]=T_D^R`;
- satisfies the exchange law.

Do not invent an unrelated action.

## Test B5 — rotational refinement

Only after B0-B4, test QMO-041:

```text
C_Q,T,rot^R != empty.
```

The known Helicon-mediated rotational route is currently blocked by WL-v133; another source-backed equivariance route may still be recovered.

## Test B6 — physical admission

Only after the action/source gate succeeds, test the existing DM2.2 dark-qualification conditions:

- same ordinary matter readout;
- nonzero hidden/readable stress-energy separation;
- nondegenerate gravitational response;
- persistence/boundary/Q gates;
- matched external data;
- conventional null-model comparison where applicable.

## Scalar prohibition

Do not replace Tests B2-B4 by

```text
rho_E -> T_mn.
```

V31 source-domain no-go remains active.

## Pass classes

- `P006-B0`: persistent UCM residual witness.
- `P006-B1`: residual-to-persistent-boundary realization typed.
- `P006-B2`: projection-residue bundle constructed.
- `P006-B3`: source tensor/exchange target passes.
- `P006-B4`: source-matched Q/action witness.
- `P006-B5`: rotational symmetry refinement.
- `P006-B6`: physical dark qualification witness.
