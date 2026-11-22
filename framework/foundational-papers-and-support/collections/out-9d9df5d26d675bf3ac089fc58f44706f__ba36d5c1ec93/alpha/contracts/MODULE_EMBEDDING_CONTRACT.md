# Module Embedding Contract

Every module loaded into BRANE 2.0 must declare:

```text
module_role ∈ {AI, API, LIBRARY}
module_version
contract_version
internal_dimension = 5
canonical_state_policy = READ_ONLY
rewrite_policy = DERIVED_ONLY
chirality_model
provenance_model
entrypoint
capabilities
```

## Required validation

BRANE rejects a module when:

- role does not match the target embedding slot
- dimension is not five
- required methods are absent
- canonical state can be mutated during ordinary execution
- chirality metadata is missing
- provenance support is missing
- contract version is incompatible
- module signature or checksum fails policy

## Embedding operation

```text
embed(role, module, request_context) → embedded_module⁶
```

The embedded module receives a private execution context but no access to the runtime.

## Isolation

Module imports must use isolated namespaces or process boundaries. Package names may not determine module role. Role is assigned by the BRANE embedding slot and validated against the manifest.
