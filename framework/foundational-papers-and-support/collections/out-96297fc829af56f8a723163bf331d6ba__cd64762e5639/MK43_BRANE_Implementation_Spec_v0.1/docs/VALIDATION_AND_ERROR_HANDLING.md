# Validation and Error Handling

## Validation gates

1. BRANE package integrity.
2. Module contract compatibility.
3. Request schema validity.
4. API handle resolution.
5. Canonical graph validity.
6. QMO closure and provenance validity.
7. Library chunk coverage.
8. Report structural completeness.
9. Artifact readability and checksum.

## Fail-closed behavior

A module that cannot load, a request that cannot be resolved, or an artifact that fails validation returns an explicit failure receipt. BRANE must never claim that a report was generated without returning a real artifact.

## Partial coverage policy

Configurable modes:

- `strict`: fail when any required handle lacks library coverage;
- `annotated`: generate report with explicit unresolved sections;
- `structural_only`: permitted only when explicitly requested, returning QMO-derived structure rather than pretending it is a full report.

## Cycle and explosion protection

- maintain visited-node identities;
- distinguish canonical cycles from repeated rendering;
- use edge budgets and continuation handles;
- prevent duplicate full expansion of identical subgraphs;
- set artifact size and section-count telemetry;
- stream output rather than building a single in-memory string when large.
