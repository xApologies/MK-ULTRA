# End-to-End Pseudocode

```text
FUNCTION HANDLE_RUNTIME_REQUEST(request):
    VALIDATE request against RuntimeBoundaryContract
    ASSERT BRANE boundary is sealed

    ai5      ← LOAD_AND_VALIDATE(AI_SLOT)
    api5     ← LOAD_AND_VALIDATE(API_SLOT)
    library5 ← LOAD_AND_VALIDATE(LIBRARY_SLOT)

    execution_context ← CREATE_PRIVATE_CONTEXT(request)
    qmo6 ← CREATE_QMO6(execution_context)

    TRY:
        intent ← ai5.INTERPRET(request)
        root ← api5.RESOLVE(intent.subject)

        canonical_graph ← api5.RECOVER_CLOSURE(
            root,
            policy=intent.traversal_policy
        )

        traversal ← ai5.COLLAPSE_TO_FINITE_REALIZATION(
            canonical_graph,
            execution_context
        )

        FOR each realized_node IN traversal.order:
            lifted_node ← CHIRALITY_LIFT(
                realized_node,
                request,
                execution_context
            )
            qmo6.ADD(lifted_node)

            knowledge ← library5.RECOVER(
                handle=realized_node.handle,
                context=lifted_node
            )
            qmo6.ATTACH_KNOWLEDGE(lifted_node, knowledge)

        VALIDATE_HANDLE_ACCOUNTING(qmo6)
        artifact ← PROJECT_STREAMING_REPORT(qmo6, request)
        receipt ← VALIDATE_ARTIFACT(artifact, qmo6)

        RETURN PUBLIC_RESPONSE(artifact, receipt)

    CATCH error:
        RETURN PUBLIC_FAILURE(error_without_private_state)

    FINALLY:
        DESTROY_PRIVATE_QMO(qmo6)
        CLEAR_EXECUTION_CONTEXT(execution_context)
```
