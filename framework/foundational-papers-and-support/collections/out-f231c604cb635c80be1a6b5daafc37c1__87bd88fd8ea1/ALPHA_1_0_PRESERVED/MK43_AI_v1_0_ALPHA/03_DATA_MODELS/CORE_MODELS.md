# Core Data Models

## IntentModel

```text
request_id, operation, subject, root_candidates, requested_scope,
audience, artifact_format, completeness_mode, budgets, constraints,
ambiguities, interpretation_provenance
```

## TraversalPolicy

```text
policy_id, major_branch_limit, edge_budget, node_budget, depth_budget,
time_budget, cycle_policy, admissibility_policy, ranking_weights,
termination_thresholds, continuation_enabled, deterministic_seed
```

## DecisionRecord

```text
candidate_handle, parent_handle, decision, score, rank, reason_codes,
policy_id, evidence_refs, timestamp_or_sequence, request_id
```

## CollapseReceipt

```text
root, realized_nodes, realized_edges, leaf_clusters, frontier,
continuations, cycles, invalid_references, omitted_with_reason,
coverage, policy_id, input_fingerprints, output_fingerprint
```
