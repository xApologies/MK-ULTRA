# Release Scope

## In scope

- Formal distinction between API-level mapped SPO and BRANE-built independent SPO instance.
- Mapping of SPO semantics onto the existing BRANE AI/API/Library port architecture.
- Authoring-plane, BRANE-plane, and realtime-device-plane separation.
- Acoustic-event object model.
- Candidate transduction operations: `PRESERVE`, `ATTENUATE`, `TRANSFORM`, `EMPHASIZE`.
- Vera safety gate and failure semantics.
- Versioning, provenance, rollback, and immutable canonical source rules.
- Machine-readable schemas and a non-audio Python scaffold.
- Acceptance tests for architectural invariants.

## Out of scope

- Clinical diagnosis.
- Clinical treatment recommendations.
- A validated autism/TBI/PTSD sensory profile.
- A medical-device claim.
- Production acoustic classification.
- Production DSP / adaptive filtering.
- Headphone or earbud hardware design drawings.
- FDA/DoD/VA certification.
- Operational military deployment.
- A claim that any specific manufacturer is a partner.

## Alpha status

This release is intended to eliminate architectural ambiguity before a 1.B executable audio prototype.
