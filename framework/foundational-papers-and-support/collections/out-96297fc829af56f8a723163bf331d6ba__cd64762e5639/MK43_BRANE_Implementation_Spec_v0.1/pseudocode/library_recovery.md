# Library Recovery Pseudocode

```text
FUNCTION RECOVER(requirements):
    results ← []

    FOR item IN requirements.in_qmo_order:
        package ← RECOVER_HANDLE(item.handle, item.context)

        IF package EXISTS:
            VALIDATE_CHUNK_PACKAGE(package)
            results.APPEND(package)
        ELSE:
            results.APPEND(UNRESOLVED_PACKAGE(item.handle, reason=NOT_FOUND))

    RETURN results

FUNCTION RECOVER_HANDLE(handle, context):
    canonical ← LOOKUP_HANDLE(handle)
    chunks ← QUERY_ALL_ACTIVE_CHUNKS(canonical)
    chunks ← FILTER_BY_CONTEXT(chunks, context)
    chunks ← ORDER_BY_TYPE_AND_SEQUENCE(chunks)
    provenance ← LOAD_PROVENANCE(chunks)

    RETURN KNOWLEDGE_PACKAGE(canonical, chunks, provenance)
```
