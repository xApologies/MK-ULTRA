# WL-v155 — Metric-Action Selection: API-Atomic Frontier

**Status:** API crawl / no parent promotion

## Query

Seed `@dm_metric_action_selection` against Dark Matter API 2.2 and Time-Space API 4.3.

## API return

The current DM2.2 record defines the object as an `OpenActionSelection`:

`Select S_H in S_H^cov(Q_H,g); then T_H_mn=-(2/sqrt(-g)) delta S_H/delta g^(mn).`

Its direct dependencies are the already-closed `@dm_covariant_hidden_action_family`, the already-closed `@dm_q_completion_family`, and `@quantum_action_functional`. Time-Space A14 supplies the Quantum Action Principle and a stationary-action rule for field configurations, but it does not choose a physical action functional from the hidden covariant family.

## Next-handle decision

No narrower current Dark Matter selector handle is exposed. Per the API-first rule, do **not** manufacture a new selector theorem. Preserve `@dm_metric_action_selection` as open and pivot to the API's separate concrete strategy for `@dm_dark_matter_qualification_nonempty`: `QMO-XAPI-CAND-001 -> @initial_data_set`.

## Guardrail

Closed admissible family != selected physical member. Stationary configuration != selection of the action law itself.
