# Current API companion mapping

> Current API: [GR/QMO](../../../../../../api/gr-qmo/00_START_HERE.md). Its supplied [definitions](../../../../../../api/gr-qmo/INTEGRATION_SPEC.md) and [object dictionary](../../../../../../api/gr-qmo/INSTALLED_OBJECTS.md) govern current API use. The superseded instructions in this block are retired; no equivalence of old runtime behavior or unprovided mathematics is implied. [Original guide and provenance](provenance://unavailable/content-sha256/63d0acf082b80aff2c710841c1a3caaad82ebbb6acdca7f3523ef4274afb78c8/ACCEPTANCE_TESTS.md).

The following retained sections describe this source collection. Historical implementation examples and domain-specific results are not a claim that GR/QMO implements those older interfaces.

# Acceptance Tests

## A1 — Runtime opacity

Given a loaded BRANE, the runtime can request a report but cannot enumerate API handles, library tables, QMO state, or intelligence internals through the public contract.

## A2 — Real artifact requirement

A successful response must contain an existing non-empty artifact and checksum. The system cannot report success using conversational text alone.

## A3 — API invariance

Run identical API graph recovery before and after a Collapse Intelligence policy update. Canonical handles, equations, and edges must be byte- or semantically equivalent.

## A4 — Modular API replacement

> Current API: [GR/QMO](../../../../../../api/gr-qmo/00_START_HERE.md). Its supplied [definitions](../../../../../../api/gr-qmo/INTEGRATION_SPEC.md) and [object dictionary](../../../../../../api/gr-qmo/INSTALLED_OBJECTS.md) govern current API use. The superseded instructions in this block are retired; no equivalence of old runtime behavior or unprovided mathematics is implied. [Original guide and provenance](provenance://unavailable/content-sha256/63d0acf082b80aff2c710841c1a3caaad82ebbb6acdca7f3523ef4274afb78c8/ACCEPTANCE_TESTS.md).

## A5 — Modular library replacement

Replace Library 1.0 fixture with Library 1.1 fixture. API graph is unchanged; recovered chunk content changes only according to library version.

## A6 — QMO privacy

No QMO payload appears in the runtime response, report metadata, logs exposed to the caller, or artifact unless diagnostic mode is explicitly enabled.

## A7 — Complete handle accounting

Every handle requested by the QMO is either rendered in the report or explicitly listed unresolved. Silent omission fails validation.

## A8 — Cycle safety

A cyclic canonical graph terminates report generation without infinite duplicate expansion. Cycle references remain represented.

## A9 — Large artifact streaming

Generate an artifact larger than available single-string memory threshold. Report completes using streaming output and remains readable by ordinary Markdown tools.

## A10 — No synopsis substitution

A request with `depth=complete` must contain expanded knowledge sections. A handle list or executive summary alone fails report validation.
