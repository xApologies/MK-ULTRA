# End-to-End Pseudocode

FUNCTION PULL_QMO(qmo_plan, options):
    REQUIRE valid_qmo_plan(qmo_plan)
    context ← FORK_REQUEST_CONTEXT()
    results ← []
    unresolved ← []
    FOR node IN qmo_plan.nodes_in_order:
        result ← context.PULL(node.handle, options)
        IF result.status == RECOVERED:
            ATTACH node placement, depth, relation TO result
            results.APPEND(result)
        ELSE:
            unresolved.APPEND(EXPLICIT_UNRESOLVED(node,result.reason))
    receipt ← COVERAGE_AUDIT(qmo_plan.nodes,results,unresolved)
    RETURN QMORecoveryResult(results,unresolved,receipt,provenance_map,hash_map)
