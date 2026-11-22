# AST-DM-WL-P020 — Source-Backed Next-Handle Crawl

## Purpose
Continue API-first exploration after strict/direct dependency saturation without promoting lower-confidence source edges.

## Query policy
1. Dark Matter edges: high-confidence direct registry only.
2. Time-Space edges: high or medium confidence only when API status is recovered/direct-source.
3. Exclude any edge whose provenance is explicitly derived.
4. Preserve edge confidence, provenance, direction and origin API.
5. Rank handles by breadth across current OpenSlots and graph distance.
6. Prefer structural/readout handles over language-projection noise.
7. Generate a QMO pair against the relevant OpenSlot.
8. If the handle loops into an already-crawled branch, mark exhausted and ask for the next handle.
9. Never convert neighborhood overlap into an identity or new parent edge.

## Current pass
`@admissible_continuation -> @occupancy -> @containment_volume/@transition_capacity -> @native_unit_of_energy -> @correspondence_registry` were crawled as separate QMO objects.

## Falsification / null handling
Empty interfaces, missing direct edges, and loopbacks are retained as results rather than patched.
