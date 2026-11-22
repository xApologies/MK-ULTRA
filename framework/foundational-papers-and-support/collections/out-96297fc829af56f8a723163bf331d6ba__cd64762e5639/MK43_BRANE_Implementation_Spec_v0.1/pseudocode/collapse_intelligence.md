# Collapse Intelligence Pseudocode

```text
FUNCTION REALIZE(canonical_graph, policy):
    tree ← NEW_TREE(root=canonical_graph.root)
    visited ← EMPTY_SET()
    GROW(tree.root, depth=0)
    RETURN tree

FUNCTION GROW(node, depth):
    visited.ADD(node.id)
    candidates ← canonical_graph.NEIGHBORS(node)
    ranked ← RANK(candidates, node, policy)

    FOR candidate IN ranked:
        IF candidate.id IN visited:
            tree.REGISTER_CYCLE_REFERENCE(node, candidate)
            CONTINUE

        decision ← DECIDE(candidate, depth, policy)

        IF decision == CONTINUE:
            branch ← tree.ADD_BRANCH(node, candidate)
            GROW(branch, depth + 1)

        ELSE IF decision == TERMINATE:
            tree.ADD_LEAF_CLUSTER(node, candidate)
            tree.ADD_CONTINUATION_HANDLE(candidate.handle)

        ELSE IF decision == DEFER:
            tree.ADD_FRONTIER(candidate)

        ELSE:
            tree.ADD_INVALID_REFERENCE(candidate)
```

Initial `DECIDE` is deterministic and policy-driven. Learned policy is a future interchangeable implementation.
