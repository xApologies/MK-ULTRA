# Module Loading Pseudocode

```text
FUNCTION LOAD_MODULE(slot, package):
    manifest ← READ_MANIFEST(package)

    REQUIRE manifest.role == slot.role
    REQUIRE manifest.internal_dimension == 5
    REQUIRE manifest.contract_version compatible with slot
    REQUIRE manifest.canonical_state_policy == READ_ONLY
    REQUIRE manifest.rewrite_policy == DERIVED_ONLY
    REQUIRE CHECKSUM(package) == manifest.checksum
    REQUIRE SIGNATURE_VALID(package) if signature policy enabled

    namespace ← CREATE_ISOLATED_NAMESPACE(slot, manifest.module_id, manifest.version)
    instance ← IMPORT_ENTRYPOINT(package, namespace)

    REQUIRE instance implements slot.protocol
    REQUIRE instance.healthcheck() == READY

    slot.mount(instance)
    RETURN MountReceipt
```

Replacement:

```text
FUNCTION REPLACE_MODULE(slot, new_package):
    REQUIRE no active request OR enter drain mode
    old ← slot.current
    candidate ← LOAD_MODULE_IN_STAGING(new_package)
    RUN compatibility tests(candidate)
    IF tests pass:
        slot.atomic_swap(candidate)
        retire(old)
    ELSE:
        discard(candidate)
        preserve(old)
```
