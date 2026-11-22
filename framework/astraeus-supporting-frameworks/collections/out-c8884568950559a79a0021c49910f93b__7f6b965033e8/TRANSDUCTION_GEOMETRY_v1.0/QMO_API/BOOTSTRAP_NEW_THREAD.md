# Bootstrap / Restore in a New Thread

This package is intended to survive thread loss.

## Minimal restore sequence

1. Upload this ZIP.
2. Read `CURRENT_RELEASE_MANIFEST.json`.
3. Verify `PACKAGE_CHECKSUMS.sha256`.
4. Read `LIVE_RUNTIME_STATE.md`.
5. Load `QMO_SCHEMA.json`.
6. Query `QMO.sqlite` or the JSON registries.
7. Read the canonical Markdown only when deeper narrative context is needed.
8. Resume from `next_question` in `LIVE_RUNTIME_STATE.md`.

## Recovery priority

```text
manifest
-> runtime state
-> schema
-> object/edge/equation registries
-> SQLite
-> ledger
-> canonical report
-> notes
```

## Rebuildability

`QMO.sqlite` is disposable.

It can be rebuilt from:

```text
QMO_OBJECT_REGISTRY.json
QMO_EDGE_REGISTRY.json
QMO_EQUATION_REGISTRY.json
QMO_LEDGER_REGISTRY.json
```

The canonical human-readable model is preserved in:

```text
MK43_Transduction_API_CURRENT_CANONICAL.md
```

## Continuation rule

Do not infer that a later thread must remember this conversation.

The package itself is the continuation boundary.

Treat its manifests, registries, hashes, statuses, and provenance as the source of truth for the live QMO state.
