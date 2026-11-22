# Privilege Algebra

## Canonical privilege set

```text
Π = {READ, LIFT, PROJECT, REWRITE_DERIVED, OVERWRITE_CANON}
```

Ordinary BRANE report execution grants:

```text
Π_report = {READ, LIFT, PROJECT, REWRITE_DERIVED}
```

and denies:

```text
OVERWRITE_CANON
```

## Meaning

- READ — inspect canonical module state
- LIFT — embed canonical state into B⁶
- PROJECT — produce an artifact from QMO⁶
- REWRITE_DERIVED — create transformed transient realization
- OVERWRITE_CANON — mutate canonical module state

## Safety rule

```text
OVERWRITE_CANON ∉ Π_report
```

Canonical updates require a separate explicit maintenance transaction with versioning, audit log, and rollback policy.

## Least privilege

Each module receives only operations needed for the current stage. The Library cannot change API edges. The API cannot rewrite library prose. The AI cannot modify canonical mathematics. BRANE can coordinate but cannot silently promote derived state into canon.
