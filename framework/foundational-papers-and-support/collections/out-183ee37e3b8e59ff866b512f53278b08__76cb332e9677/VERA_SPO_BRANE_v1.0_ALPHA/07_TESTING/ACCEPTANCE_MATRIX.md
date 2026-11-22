# Acceptance Matrix — 1.0 Alpha / 1.B Target

| ID | Requirement | Expected |
|---|---|---|
| T01 | API module is a canonical mapped SPO object | PASS |
| T02 | Canonical state is READ_ONLY | PASS |
| T03 | Ordinary rewrites are DERIVED_ONLY | PASS |
| T04 | BRANE constructs private QMO^6 | PASS |
| T05 | `π_SPO` emits a new independent SPO identity | PASS |
| T06 | SPO records parent API fingerprint | PASS |
| T07 | Unknown event defaults to PRESERVE | PASS |
| T08 | Low-confidence event defaults to PRESERVE | PASS |
| T09 | Protected event cannot be attenuated by ordinary user rule | PASS |
| T10 | Missing rule defaults to PRESERVE | PASS |
| T11 | Unsupported device transform is rejected/fallback preserve | PASS |
| T12 | User transparency override wins | PASS |
| T13 | Realtime decision cannot mutate SPO | PASS |
| T14 | Profile revision creates new SPO instance | PASS |
| T15 | Prior version remains recoverable | PASS |
| T16 | Corrupt/unverifiable policy refuses transformed mode | PASS |
| T17 | Raw audio retention defaults off | PASS |
| T18 | Clinical unknowns are not fabricated by authoring AI | PASS |
| T19 | API/AI/Library domain_ids need not overlap | PASS |
| T20 | Genesis Point reconciliation preserves both histories until promotion | PASS |
