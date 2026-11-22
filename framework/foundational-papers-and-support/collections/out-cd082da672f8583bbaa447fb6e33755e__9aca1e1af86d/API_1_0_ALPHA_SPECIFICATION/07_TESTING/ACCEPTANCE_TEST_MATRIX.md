# API 5.B Acceptance Test Matrix

| ID | Test | Required result |
|---|---|---|
| T01 | Load unmodified 4.3 package | PASS |
| T02 | Detect one-byte canonical modification | FAIL CLOSED |
| T03 | Report five dimensions and no realization dimension | PASS |
| T04 | Fork two contexts and verify no shared mutable state | PASS |
| T05 | Resolve exact canonical handle | PASS |
| T06 | Resolve registered alias | PASS |
| T07 | Unknown subject | structured failure |
| T08 | Ambiguous subject | structured failure with candidates |
| T09 | Outgoing neighbors equal canonical index records | PASS |
| T10 | Incoming neighbors equal canonical index records | PASS |
| T11 | Composed path is not promoted to direct edge | PASS |
| T12 | Closure obeys depth budget | PASS |
| T13 | Closure obeys node and edge budgets | PASS |
| T14 | Cyclic graph terminates deterministically | PASS |
| T15 | Equation recovery preserves exact text and order | PASS |
| T16 | Provenance differs appropriately by object | PASS |
| T17 | Missing provenance causes required rejection | PASS |
| T18 | Chirality is deterministic | PASS |
| T19 | Contradictory chirality becomes unresolved | PASS |
| T20 | Fabricated edge is rejected | PASS |
| T21 | Graph validation catches broken path continuity | PASS |
| T22 | Graph validation catches noncanonical node | PASS |
| T23 | Canonical fingerprint unchanged after 1,000 requests | PASS |
| T24 | Concurrent contexts remain isolated | PASS |
| T25 | Healthcheck reports component-specific status | PASS |
| T26 | BRANE 2.1 protocol conformance | PASS |
| T27 | Full recovery of selected canonical handles | PASS |
| T28 | Package checksum verification | PASS |
| T29 | Deterministic output under repeated equal requests | PASS |
| T30 | No writes occur inside canonical package | PASS |
