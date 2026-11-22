# QMO⁶ Manager Pseudocode

```text
CLASS QMO6Workspace:
    state = ABSENT
    nodes = private map
    edges = private list
    knowledge = private map

    initialize(request):
        transition(ABSENT, INITIALIZING)
        allocate private workspace

    add_node(node6):
        require state in {GRAPH_REALIZED, LIBRARY_RESOLVING}
        key = realization_key(node6)
        if key not in nodes:
            nodes[key] = node6

    attach_knowledge(node6, chunk):
        validate chunk provenance
        knowledge[node6.key] = chunk

    validate_complete(requested_handles):
        resolved = keys with knowledge
        unresolved = explicit unresolved records
        require requested_handles == resolved ∪ unresolved

    destroy():
        zero temporary buffers
        delete files
        clear maps
        transition(any_active_state, DESTROYED)
```
