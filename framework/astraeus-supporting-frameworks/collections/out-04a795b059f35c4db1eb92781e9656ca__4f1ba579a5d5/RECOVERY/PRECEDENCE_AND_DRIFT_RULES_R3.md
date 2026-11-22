# RECOVERY PRECEDENCE & DRIFT RULES R3

Use these rules to prevent historical local `current` fields from overriding the latest checkpoint.

## Authority order for resuming work

1. `RECOVERY/START_HERE.md` — wrapper recovery entry point.
2. `LIVE/STATE_VECTOR.json` — normalized current wrapper state.
3. Baseline `LIVE/RECOVERY/START_HERE.md`.
4. Baseline `LIVE/WATCHER/STATUS_LEDGER.json`.
5. Baseline Atlas v233 + QMO-AST-DM-WL-117 + protocol P029.
6. Earlier Atlas/QMO/journal/protocol artifacts are chronology/evidence, not current resume pointers.
7. Parent APIs and mathematics are read-only evidence surfaces.

## Historical-current rule

The live model is append-only and contains older sections that correctly said things like `Current next handle: @chirality_fabric` at the time they were written. Those sentences remain valuable chronology but **do not override** the latest frontier header.

## Known recovery-normalization cases

- Baseline CHANGELOG omits a WL-022 heading; Journal 0022 and Atlas v146 preserve the work. R3 chapter continuity restores the index entry without editing baseline bytes.
- Two historical protocol files share P016. Preserve both; cite by filename/title when that historical branch matters.
- `CHECKPOINT_METADATA.current_primary_test` preserves the earlier History->InfinityClass search description. The actual resume pointer is `current_next_handle = GLOBAL_RANK_FRESH_NON_LOOPING`, corroborated by Watcher, QMO-117, Atlas v233, P029, and the baseline START_HERE.

## Non-promotion rule

R3 is a recovery audit. It does not promote candidate mathematics, Rainbow Road, dark-matter objects, parent APIs, or physical claims.
