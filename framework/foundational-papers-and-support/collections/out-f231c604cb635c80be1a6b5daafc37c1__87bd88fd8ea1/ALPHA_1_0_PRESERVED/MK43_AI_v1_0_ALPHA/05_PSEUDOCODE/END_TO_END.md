# End-to-End AI⁵ Pseudocode

```text
FUNCTION HANDLE_AI_REQUEST(request, api_capability, library_capability, qmo_context):
    ASSERT request IS normalized
    context ← FORK_REQUEST_CONTEXT(request.request_id)
    before_api ← api_capability.CANONICAL_FINGERPRINT()
    before_library ← OPTIONAL_FINGERPRINT(library_capability)

    intent ← INTERPRET(request, api_capability, context)
    root ← RESOLVE_ROOT(intent, api_capability, context)
    policy ← BUILD_POLICY(intent, request.constraints, context)

    tree ← REALIZE_TREE(root, policy, api_capability, context)
    recovery_plan ← PLAN_LIBRARY_RECOVERY(tree, intent, context)
    chunks ← OPTIONAL_LIBRARY_RECOVER(recovery_plan, library_capability, context)

    collapse ← COLLAPSE(tree, chunks, intent, policy, context)
    receipt ← VALIDATE_COLLAPSE(collapse, tree, policy, context)

    ASSERT before_api == api_capability.CANONICAL_FINGERPRINT()
    ASSERT before_library == OPTIONAL_FINGERPRINT(library_capability)
    ASSERT receipt.valid

    DESTROY_REQUEST_CONTEXT(context)
    RETURN collapse, receipt
```
