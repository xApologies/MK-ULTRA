# Five-Dimensional Module Architecture

## Generic module

A module is modeled as:

```text
M⁵ = I × D × Χ × R × P
```

A module object is:

```text
m = (i,d,χ,r,p)
```

The missing sixth coordinate is deliberate. A module does not own global execution realization. BRANE adds that coordinate when the module participates in a request.

## AI⁵

```text
AI⁵ = (policy_identity, traversal_relation, chirality_rule, recursion_policy, policy_provenance)
```

Required operations:

```text
interpret(request)
rank(candidates, context)
continue_or_terminate(node, context)
place_continuation(frontier)
validate_collapse(tree)
```

## API⁵

```text
API⁵ = (handle_identity, typed_edge_relation, chirality_metadata, recursive_closure, canonical_provenance)
```

Required operations:

```text
resolve(handle)
neighbors(handle, relation_filter)
recover_closure(root, policy)
recover_equations(handle)
recover_provenance(handle)
```

## Library⁵

```text
Library⁵ = (knowledge_identity, semantic_relation, chirality_context, recovery_depth, source_provenance)
```

Required operations:

```text
recover(handle, qmo_context)
recover_equations(handle)
recover_models(handle)
recover_analogies(handle)
recover_explanations(handle, language)
assemble_chunk(handle)
```

## Module independence

Changing one module must not require rewriting the others, provided all modules satisfy the same embedding contract.

```text
replace(AI⁵)      ⟹ API⁵ and Library⁵ remain valid
replace(API⁵)     ⟹ AI⁵ and Library⁵ remain valid
replace(Library⁵) ⟹ AI⁵ and API⁵ remain valid
```

Compatibility is checked by BRANE before execution.
