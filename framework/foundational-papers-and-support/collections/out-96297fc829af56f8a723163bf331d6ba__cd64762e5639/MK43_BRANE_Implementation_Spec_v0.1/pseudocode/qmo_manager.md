# QMO Manager Pseudocode

```text
FUNCTION CREATE(request_id, compiled_request):
    qmo ← {
        id: RANDOM_INTERNAL_ID(),
        request_id: request_id,
        state: NEW,
        request: compiled_request,
        graph: null,
        realization: null,
        recovery_requirements: [],
        recovered_chunks: [],
        validation: {}
    }
    REGISTER_EPHEMERAL(qmo)
    RETURN qmo

FUNCTION ATTACH_REALIZATION(qmo, tree):
    qmo.realization ← tree
    qmo.recovery_requirements ← ORDERED_HANDLES_FROM(tree)
    qmo.state ← STRUCTURE_COMPLETE

FUNCTION DESTROY(qmo):
    ZERO_TRANSIENT_BUFFERS(qmo)
    REMOVE_EPHEMERAL_REGISTRATION(qmo.id)
```
