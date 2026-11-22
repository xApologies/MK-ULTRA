# BRANE 2.0 Acceptance Tests

## A1 Boundary opacity

Runtime can call BRANE but cannot enumerate or access AI⁵, API⁵, Library⁵, or QMO⁶.

## A2 Five-dimensional module validation

A module declaring any dimension other than five is rejected.

## A3 Role-slot validation

An API module cannot mount in AI or Library embedding slots.

## A4 Canonical immutability

A report request produces no canonical module-state changes.

## A5 Derived rewrite

Language and report transformations exist only in transient QMO⁶ or artifact state.

## A6 QMO privacy

No runtime response includes raw QMO nodes, raw graph structures, or private workspace paths.

## A7 Complete handle accounting

Every QMO-requested handle is resolved or explicitly unresolved.

## A8 No synopsis substitution

A complete-report request fails if output contains only headings, handles, or summary text.

## A9 Cycle safety

Recursive cycles terminate without duplicate unbounded output.

## A10 Streaming

Large reports are written incrementally and do not require a single in-memory string.

## A11 Cleanup

QMO⁶ workspace is destroyed after success and failure.

## A12 Module replacement isolation

Replacing one module does not alter the other mounted modules.

## A13 Artifact integrity

Returned file exists, is non-empty, and matches its SHA-256 receipt.
