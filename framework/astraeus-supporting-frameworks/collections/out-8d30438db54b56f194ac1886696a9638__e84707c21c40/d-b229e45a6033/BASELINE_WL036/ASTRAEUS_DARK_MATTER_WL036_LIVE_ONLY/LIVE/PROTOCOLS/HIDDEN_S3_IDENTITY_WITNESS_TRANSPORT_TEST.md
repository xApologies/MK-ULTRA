# AST-DM-WL-P026 — Hidden-S3 Identity-Witness Transport Test

**Work layer:** WL-035  
**Status:** SOURCE-INSTANCE TYPING PROTOCOL

## Objective

Test whether the already-typed Dark Matter hidden relational-state bundle can carry the Identity Through History witness-transport structure without inventing a new global state space.

## Inputs

```text
pi_H:E_H^R->T_H
R_H(t)=(V_t,E_t,w_t,chi_t,H_t)_R
```

and an admissible bundle History:

```text
h:t0 -> ... -> tn.
```

## Stage A — endpoint witness data

Recover source-supported candidate Identity-Witness data for endpoint fiber states.

If no declared invariant contract can be recovered for the chosen pair, STOP:

```text
IDENTITY_CONTRACT_UNTYPED.
```

## Stage B — segment transport

For each History segment, ask whether a source-supported action corresponding to:

```text
T_Id(h_i)
```

exists on that witness data.

Do not infer this from the presence of a History component alone.

## Stage C — composition

Only if each segment is typed, test the existing composition condition:

```text
T_Id(h2 o h1)=T_Id(h2)oT_Id(h1).
```

## Stage D — holonomy

For a closed History, recover the returned witness transformation and compare its Identity class with `id`.

This can feed the WL-v215 hidden-loop pair generator.

## Stop boundary

This protocol does not perform:

```text
@dm_hidden_state_embedding
@dm_metric_action_selection
gravity readout
dark-matter qualification.
```

A typed Identity transport is candidate witness metadata, not physical admission.

## Current handle

```text
@history_transport
```
