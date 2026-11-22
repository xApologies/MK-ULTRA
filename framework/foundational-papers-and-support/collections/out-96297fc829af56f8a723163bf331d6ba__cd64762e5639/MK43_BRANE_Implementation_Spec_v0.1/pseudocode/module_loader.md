# Module Loader Pseudocode

```text
FUNCTION LOAD_BRANE(package_path):
    manifest ← READ_MANIFEST(package_path)
    VERIFY_PACKAGE_CHECKSUMS(manifest)

    intelligence ← LOAD_MODULE(manifest.collapse_intelligence)
    api ← LOAD_MODULE(manifest.api)
    library ← LOAD_MODULE(manifest.library)

    VERIFY_CONTRACT(intelligence, manifest.contracts.intelligence)
    VERIFY_CONTRACT(api, manifest.contracts.api)
    VERIFY_CONTRACT(library, manifest.contracts.library)

    compatibility ← NEGOTIATE_SCHEMAS(intelligence, api, library)
    IF NOT compatibility.success:
        RAISE INCOMPATIBLE_MODULES

    REGISTER_SEALED_BRANE(
        brane_id=manifest.brane_id,
        intelligence=intelligence,
        api=READ_ONLY(api),
        library=library,
        policy=manifest.policy
    )
```
