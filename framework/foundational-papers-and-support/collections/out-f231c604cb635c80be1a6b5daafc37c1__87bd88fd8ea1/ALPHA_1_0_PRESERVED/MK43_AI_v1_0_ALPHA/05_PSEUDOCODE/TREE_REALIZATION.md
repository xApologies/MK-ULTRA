# Tree Realization Pseudocode

```text
FUNCTION REALIZE_TREE(root, policy, api, context):
    tree ← NEW_TREE(root)
    visited ← EMPTY_SET()
    counters ← NEW_BUDGET_COUNTERS(policy)
    GROW(root, depth=0, parent=NULL)
    FINALIZE_BRANCH_ACCOUNTING(tree)
    RETURN tree

FUNCTION GROW(node, depth, parent):
    visited.ADD(node.handle)
    candidates ← api.NEIGHBORS(node.handle, context)
    admissible, invalid ← FILTER_ADMISSIBLE(candidates, api, context)
    tree.ADD_INVALID_REFERENCES(invalid)
    ranked ← RANK(admissible, node, policy, context)

    FOR candidate IN ranked:
        IF candidate.handle IN visited:
            tree.REGISTER_CYCLE_REFERENCE(node, candidate)
            CONTINUE

        decision ← CONTINUE_OR_TERMINATE(candidate, depth, counters, policy, context)
        tree.RECORD_DECISION(candidate, decision)

        MATCH decision.kind:
            CONTINUE:
                branch ← tree.ADD_BRANCH(node, candidate)
                counters.CONSUME(candidate)
                GROW(branch, depth + 1, node)
            TERMINATE:
                cluster ← tree.ADD_LEAF_CLUSTER(node, candidate)
                tree.ADD_CONTINUATION(PLACE_CONTINUATION(cluster, context))
            DEFER:
                tree.ADD_FRONTIER(candidate)
            REJECT_INVALID:
                tree.ADD_INVALID_REFERENCE(candidate)
```
