# QMO-Addressed Live Metadata Model — v0.4.0

- QMO metadata addresses: 187
- Address key: canonical `@handle`
- Operational object registry remains separate from semantic metadata library.
- Metadata current-state library: `library/QMO_METADATA_LIBRARY.json`
- Machine registry: `api/QMO_METADATA_REGISTRY.json`
- Append-only semantic history: `live_model/QMO_METADATA_HISTORY.jsonl`
- Human live model: `live_model/ASTRAEUS_API_LIVE_MODEL.md`
- SQLite mirror tables: `qmo_metadata`, `qmo_metadata_history`
- Canonical mutation hook: closure promotion triggers QMO metadata synchronization.
- Immediate predecessor v0.3 is content-address referenced instead of recursively nested.

Validation requires a 1:1 match between operational QMO handles and metadata addresses.
