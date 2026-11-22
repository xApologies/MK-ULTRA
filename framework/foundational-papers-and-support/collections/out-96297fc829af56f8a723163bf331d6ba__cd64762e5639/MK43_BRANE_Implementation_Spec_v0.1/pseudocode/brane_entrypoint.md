# BRANE Entrypoint Pseudocode

```text
FUNCTION HANDLE_RUNTIME_REQUEST(envelope):
    request_id ← CREATE_REQUEST_ID()

    TRY:
        VALIDATE_REQUEST_SCHEMA(envelope)
        modules ← MODULE_LOADER.ACTIVE_MODULES()
        ASSERT_COMPATIBLE(modules)

        compiled_request ← COLLAPSE_INTELLIGENCE.COMPILE(envelope)
        qmo ← QMO_WORKSPACE.CREATE(request_id, compiled_request)

        graph ← API_ADAPTER.RECOVER_GRAPH(compiled_request)
        qmo.ATTACH_CANONICAL_GRAPH(graph)

        realization ← COLLAPSE_INTELLIGENCE.REALIZE(graph, compiled_request.policy)
        qmo.ATTACH_REALIZATION(realization)

        chunks ← LIBRARY_ADAPTER.RECOVER(qmo.RECOVERY_REQUIREMENTS())
        qmo.ATTACH_LIBRARY_RESULTS(chunks)

        coverage ← VALIDATOR.CHECK_LIBRARY_COVERAGE(qmo)
        APPLY_COVERAGE_POLICY(qmo, coverage, compiled_request.coverage_mode)

        artifact ← REPORT_ASSEMBLER.BUILD(qmo, compiled_request.report_spec)
        receipt ← VALIDATOR.VALIDATE_ARTIFACT(artifact, qmo)

        QMO_WORKSPACE.DESTROY(qmo)
        RETURN SUCCESS_RESPONSE(request_id, artifact, receipt)

    CATCH error:
        QMO_WORKSPACE.DESTROY_IF_PRESENT(request_id)
        RETURN FAILURE_RESPONSE(request_id, SANITIZE(error))
```
