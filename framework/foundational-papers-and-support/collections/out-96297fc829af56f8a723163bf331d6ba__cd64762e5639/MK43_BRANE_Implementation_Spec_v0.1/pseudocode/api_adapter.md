# API Adapter Pseudocode

```text
FUNCTION RECOVER_GRAPH(compiled_request):
    root ← RESOLVE_HANDLE(compiled_request.subject)
    ASSERT root EXISTS

    graph ← NEW_CANONICAL_GRAPH(root)
    queue ← [root]
    visited ← EMPTY_SET()

    WHILE queue NOT EMPTY:
        current ← queue.POP()
        IF current IN visited:
            CONTINUE
        visited.ADD(current)

        records ← READ_TYPED_EDGES(current, compiled_request.direction)
        FOR record IN records:
            VALIDATE_EDGE_RECORD(record)
            graph.ADD(record, provenance=record.provenance)
            IF SHOULD_RECURSE(record, compiled_request):
                queue.PUSH(record.target)

    RETURN graph
```
