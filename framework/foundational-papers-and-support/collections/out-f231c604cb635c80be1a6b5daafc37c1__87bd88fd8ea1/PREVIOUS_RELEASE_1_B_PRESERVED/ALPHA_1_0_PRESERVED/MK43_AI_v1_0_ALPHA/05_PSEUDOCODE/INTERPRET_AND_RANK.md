# Interpretation and Ranking Pseudocode

```text
FUNCTION INTERPRET(request, api, context):
    candidates ← api.PROBE_SUBJECT(request.subject, context)
    normalized ← NORMALIZE_CANDIDATES(candidates)
    RETURN IntentModel(
        request_id=request.request_id,
        operation=request.operation,
        subject=request.subject,
        root_candidates=normalized,
        constraints=request.constraints,
        interpretation_provenance=CAPTURE_INPUT_EVIDENCE(request, candidates)
    )

FUNCTION RANK(candidates, node, policy, context):
    records ← []
    FOR candidate IN candidates:
        features ← EXTRACT_DECLARED_FEATURES(candidate, node, context)
        score ← APPLY_POLICY_WEIGHTS(features, policy)
        records.APPEND(RankRecord(candidate, score, features, policy.id))
    RETURN STABLE_SORT(records, key=(-score, canonical_handle, edge_type))
```
