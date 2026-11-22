# Astraeus Writing Index — MK-147 Checkpoint 7

Checkpoint 7 seals the PSSP mechanism and places it under:

`@sfo/aera/transcription/pssp`

## PSSP writing chain

- `@sfo/binding_circle/identity_binding` — Binding makes the latent phase-state part of the practitioner's admissible inherited identity.
- `@sfo/aera/transcription` — Aera transcription layer.
- `@sfo/aera/transcription/pssp` — canonical PSSP mechanism.
- `@sfo/aera/transcription/pssp/phase_state` — latent/compact bound state (“spiky ball”).
- `@sfo/aera/transcription/pssp/shadow_manifold` — expanded active manifold/scaffold.
- `@sfo/aera/transcription/pssp/corridor_architecture` — permissible internal structural routes.
- `@sfo/aera/transcription/pssp/basin_signature` — structural basin requirements; not power.
- `@sfo/aera/transcription/pssp/stabilization` — basin-conditioned energy-density stabilization.
- `@sfo/aera/transcription/pssp/shaping_handoff` — downstream conscious shaping.
- `@sfo/aera/transcription/pssp/failure_modes` — realization/stabilization failure.

## Canonical mechanism

`Binding → Bound Phase State → PSSP Shadow Manifold → Basin Energy/Stabilization → Shaping`

## Hard rule

**Basin signature specifies construction, not power.**

## SQLite retrieval

All knowledge below PSSP:

```sql
SELECT linked_handle, heading, content, authority, source_path
FROM sfo_knowledge_closure
WHERE root_handle='@sfo/aera/transcription/pssp'
ORDER BY unit_id;
```

PSSP equations:

```sql
SELECT linked_handle, expression, context, source_label, authority
FROM sfo_equation_closure
WHERE root_handle='@sfo/aera/transcription/pssp'
ORDER BY equation_id;
```

Full-text search:

```sql
SELECT unit_id, heading, source_path
FROM knowledge_fts
WHERE knowledge_fts MATCH 'PSSP OR "shadow manifold"';
```

## Next major mechanism

Genesis Minds.
