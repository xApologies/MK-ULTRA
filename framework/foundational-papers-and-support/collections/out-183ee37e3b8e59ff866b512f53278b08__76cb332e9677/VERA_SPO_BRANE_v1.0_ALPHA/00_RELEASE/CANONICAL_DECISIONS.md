# Canonical Decisions — 1.0 Alpha

## D01 — API is a mapped object
The auditory API is not treated as merely a coordinate system surrounding an SPO. The API itself is the canonical domain-wide mapped Sound Profile Object: `SPO_API^5`.

## D02 — BRANE creates an independent SPO
BRANE uses its standard AI/API/Library composition and private QMO^6 workspace, then applies an SPO projection `π_SPO` to emit an independent `SPO_instance` for a user/request/context.

## D03 — Preserve the existing three external BRANE roles
No two-port fork is required for 1.0 Alpha. AI, API, and Library remain the external module roles because the supplied BRANE schema and contracts require them.

## D04 — Library may be thin but remains useful
Library^5 may initially contain only event definitions, transformation templates, device capability records, profile version history, evidence/provenance, and rollback material.

## D05 — Separate authoring from realtime execution
External authoring AI may help translate clinician/user requirements into candidate structured profile packages. The deployed realtime loop does not permit a generative model to improvise arbitrary transformations.

## D06 — Safety is an independent gate
A candidate transformation must pass Vera's safety gate even if the classifier and user profile both request it.

## D07 — Uncertainty defaults to preservation
If event identity, safety class, transform admissibility, or device capability is uncertain, the runtime preserves the original semantic/safety information and does not suppress the event.

## D08 — Safety-critical semantics may not be erased
Safety classes and preservation rules are explicit in the canonical API-level object and inherited by every independent SPO instance.

## D09 — User agency is mandatory
Every deployed policy requires a direct override / transparency path. Clinical authority does not remove user control.

## D10 — SPO is provisional terminology
`SPO = Sound Profile Object` remains provisional until the planned Genesis Point source archaeology is completed. Historical canonical naming, if found, supersedes this label through a controlled migration rather than silent rewriting.
