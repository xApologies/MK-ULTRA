# Chirality Lift Pseudocode

```text
FUNCTION CHIRALITY_LIFT(node5, request, context):
    identity   ← node5.identity
    dependency ← RESOLVE_REQUEST_RELATIVE_DEPENDENCY(node5, context.graph)
    chirality  ← RESOLVE_CHIRALITY(node5, request, context)
    recursion  ← context.recursive_depth(node5)
    provenance ← node5.provenance
    realization← BUILD_REALIZATION_STATE(node5, request, context)

    REQUIRE ADMISSIBLE(identity, dependency, chirality,
                       recursion, provenance, realization)

    RETURN Node6(
        identity,
        dependency,
        chirality,
        recursion,
        provenance,
        realization
    )
```
