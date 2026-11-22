# QMO Handoff

Input: QMOAddressPlan(qmo_id, request_id, root_handle, ordered_nodes[handle,relation,depth,placement,expected_content_types,recovery_profile], strict_coverage, language, artifact_profile).

Output: QMORecoveryResult with recovered packages in identical order, unresolved receipts, provenance map, package-version map, deterministic-order hash, and coverage receipt.

Library must not reorder the QMO except under an explicit declared recovery profile.
