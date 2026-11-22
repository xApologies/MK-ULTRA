# AST-DM-WL-P025 — Holonomy-Filtered Hidden-Witness Test

**Work layer:** WL-035  
**Status:** SOURCE-CONSTRAINED CANDIDATE-WITNESS PROTOCOL

## Objective

Use an existing hidden Identity-breaking History loop as candidate witness data without claiming that holonomy is dark matter.

## Stage A — source pair

Recover a source-admissible closed History loop `gamma_H` satisfying:

```text
Read_R(end) ~ Read_R(start)
Hol_Id(gamma_H) !~_Id id
```

If unavailable, STOP.

## Stage B — Time-Shell History address

Represent the History only through source-supported fields of:

```text
TSAddress=(Sigma_p,b,[h]_Id,chi,Inv,R,B,O).
```

Do not infer equality of fields not fixed by the source.

## Stage C — hidden-state admission

Ask whether the candidate is admitted by the existing:

```text
@dm_hidden_state_embedding.
```

If the physical selector remains unavailable, return:

```text
HIDDEN_EMBEDDING_OPEN
```

and STOP.

## Stage D — projection-residue survival

Only after admission, evaluate the existing gate:

```text
@dm_projection_residue_survival
```

and require a non-isomorphic full/visible residue-bundle distinction.

## Stage E — Q survival / dark readout

Only if Stage D passes, use the already-closed `@dm_q_survival`, then test the Dark Matter API's own readout condition:

```text
M_R(x0)=M_R(x1)
G_R(x0)!=G_R(x1).
```

## Guardrails

- generic `Read_R` equality != DM matter-readout equality by identity;
- Identity holonomy != gravity readout;
- History holonomy != dark matter;
- Time-Shell History address != hidden-state embedding;
- bundle survival != metric-action selection;
- no parent promotion.
