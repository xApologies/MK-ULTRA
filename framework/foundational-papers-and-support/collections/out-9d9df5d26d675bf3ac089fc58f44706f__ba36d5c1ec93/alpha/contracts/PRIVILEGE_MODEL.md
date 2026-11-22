# Privilege Model

## Ordinary request mode

AI⁵: read API-derived graph; write only traversal state.

API⁵: read canonical handles and edges; generate derived closure; no canonical mutation.

Library⁵: read knowledge records; create derived language/report chunks; no canonical mutation.

BRANE⁶: create ephemeral QMO⁶; coordinate modules; write artifact; destroy QMO⁶.

## Maintenance mode

Canonical updates are outside ordinary report generation. They require:

```text
maintenance_request
→ authenticate
→ snapshot
→ validate migration
→ apply versioned update
→ audit
→ commit or rollback
```

No ordinary `generate_report` request can enter maintenance mode.
