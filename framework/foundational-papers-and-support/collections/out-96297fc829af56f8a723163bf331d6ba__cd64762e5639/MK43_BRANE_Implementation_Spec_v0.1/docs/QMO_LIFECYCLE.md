# QMO Lifecycle

## Definition

A Queryable Mathematical Object is the transient structural object produced by the API for one request and used inside BRANE to coordinate library recovery and report assembly.

## Visibility

The QMO is private to BRANE. The runtime, human-facing AI, and human do not need to know it exists.

## State model

```text
NEW
→ REQUEST_COMPILED
→ API_RESOLVING
→ STRUCTURE_COMPLETE
→ LIBRARY_RECOVERING
→ COVERAGE_VALIDATING
→ REPORT_ASSEMBLING
→ ARTIFACT_VALIDATING
→ COMPLETE
→ DESTROYED
```

Failure states:

```text
FAILED_REQUEST
FAILED_API
FAILED_LIBRARY
FAILED_COVERAGE
FAILED_REPORT
CANCELLED
```

## Required QMO contents

- request identity;
- root handle;
- canonical node set;
- canonical typed edge set;
- dependency layers or traversal organization;
- provenance references;
- traversal policy metadata;
- continuation handles;
- library recovery requirements;
- per-handle coverage state;
- report assembly state;
- validation state.

## Teardown

After artifact validation, the QMO is destroyed by default. Optional encrypted diagnostic retention may be introduced later but is outside version 0.1.

## No silent partial success

If the library cannot resolve a handle, the QMO records it explicitly. The final report must include an unresolved appendix or the request must fail according to policy. Missing chunks must never be silently omitted.
