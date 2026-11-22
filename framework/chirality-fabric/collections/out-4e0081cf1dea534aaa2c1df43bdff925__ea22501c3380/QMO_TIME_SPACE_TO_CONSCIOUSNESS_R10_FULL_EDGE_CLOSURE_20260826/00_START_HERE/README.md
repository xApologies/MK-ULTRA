# QMO Time-Space → Consciousness — R10 Full Edge Closure

Root handle: `@qmo_time_space_to_consciousness_r10`

This package replaces the earlier shortest-route query product with a ten-pass recursive closure over the strict typed edge graph of `@mk43_unified_qmo_v2`. The parent API is read-only and was not modified.

## Crawl

- Seed QMO: `@qmo_time_space_to_consciousness`
- Seed handles: @consciousness, @graviton, @time_space
- Requested iterations: **10**
- Executed iterations: **10**
- First fixed point: iteration **8**
- Wave counts (including seed wave): **[3, 472, 351, 568, 33, 11, 17, 4, 0, 0, 0]**
- Recovered handles: **1459**
- Raw strict edge witnesses internal to the closure: **160057**
- Canonical typed edge triples: **79624**
- Weak components: **1**

Iterations after the fixed point are deliberately retained as zero-growth passes because Genesis explicitly requested ten iterations.

## Recovered core spine

`@time_space → @genesis_field → @resolution → @bandwidth → @persistence → @chirality → @helicon → @graviton → @time_shell → @spacetime → @black_hole → @black_hole_cosmology → @cosmology → @consciousness`

All 13 spine edges are present in the strict API closure. See `02_GRAPH/CORE_DEPENDENCY_SPINE.md` for relation/provenance details.

## Machine surfaces

- `03_MACHINE/QMO_TIME_SPACE_TO_CONSCIOUSNESS_R10.sqlite` — queryable compact QMO database
- `03_MACHINE/qmo_api.py` — minimal query CLI
- `03_MACHINE/EDGE_REGISTRY_STRICT_ALL_WITNESSES.jsonl` — every strict source/derived witness inside the closure
- `03_MACHINE/EDGE_REGISTRY_CANONICAL_TYPED.jsonl` — one strongest witness per `(source, relation, target)` triple
- `02_GRAPH/FULL_CANONICAL_ADJACENCY.json` — canonical adjacency view
- `04_AUDIT/ITERATION_LEDGER.json` — ten-pass crawl ledger

## Status discipline

Graph connectivity is not identity and is not automatic theorem entailment. `SUPPORTS`, `DEPENDS_ON`, `COMPOSED_DEPENDENCY`, and other relations retain their source semantics and provenance. Derived cosmology edges remain derived where the parent API marks them derived.
