# Report Projection Pseudocode

```text
FUNCTION PROJECT_STREAMING_REPORT(qmo6, request):
    output ← OPEN_TEMP_ARTIFACT(request.format)

    WRITE title and recovery metadata

    FOR node6 IN qmo6.traversal_order:
        chunk ← qmo6.knowledge[node6.key]

        WRITE section heading(chunk.display_name)
        WRITE definition(chunk.definition)
        WRITE equations(chunk.equations)
        WRITE symbol definitions(chunk.symbols)
        WRITE derivations(chunk.derivations)
        WRITE models(chunk.models)
        WRITE analogies(chunk.analogies)
        WRITE dependency role(node6.dependency)
        WRITE implications(chunk.implications)
        WRITE provenance(chunk.provenance)

        IF chunk unresolved:
            WRITE explicit unresolved notice and reason

    FLUSH output incrementally
    COMPUTE sha256
    RETURN artifact
```

Presentation layers may add transitions and formatting, but may not delete recovered content unless explicitly requested.
