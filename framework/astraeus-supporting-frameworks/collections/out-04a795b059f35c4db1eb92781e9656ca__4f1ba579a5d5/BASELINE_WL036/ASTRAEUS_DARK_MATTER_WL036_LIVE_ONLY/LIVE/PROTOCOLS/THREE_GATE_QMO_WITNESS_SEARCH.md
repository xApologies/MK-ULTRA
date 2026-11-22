# AST-DM-WL-P015 — Three-Gate QMO Witness Search

## Target

Search for one candidate hidden state that survives all three API-constrained gate landscapes without adding a bespoke gravity law.

## Gates

1. `G_embed`: `@dm_hidden_state_embedding` against `@native_constraint_closure`.
2. `G_action`: `@dm_metric_action_selection` against `@total_action`.
3. `G_readout`: `@dm_dark_matter_qualification_locus` against `@time_shell` / `@graviton` / `@gravity`.

## Procedure

- Generate/crawl a QMO for the candidate hidden-state data.
- Compose only over exact API handles.
- Require an admissible route through each gate.
- Preserve the parent conditions of QMO-DM-QUAL-001.
- If the candidate fails any gate, record the first failure and do not patch it with a new edge.
- If all three gates admit the same candidate data, promote only to a work-layer witness candidate; physical dark matter still requires the parent nonemptiness/observational conditions.

## First candidate data

Use the existing rotational/shear/holonomy S3-History candidate as input data, not as a new law.
