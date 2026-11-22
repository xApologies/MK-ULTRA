# Alpha Recovery Spine

Alpha is the authoritative reconstruction layer for BRANE 2.0. It is written so that an engineer who has lost all production code can recover the system without redesigning its core architecture.

## Canonical implementation thesis

BRANE is a six-dimensional sealed container. It accepts three independently replaceable five-dimensional modules. It reads canonical module state and may create derived rewrites, but may not silently overwrite canonical state. The three module embeddings cooperate around a private ephemeral QMO⁶. The QMO is projected into an artifact and then destroyed or explicitly archived under policy.

## Required reading order

1. `models/PROJECT_MODEL.md`
2. `math/SIX_DIMENSIONAL_BRANE.md`
3. `math/FIVE_DIMENSIONAL_MODULES.md`
4. `math/CHIRALITY_SET_LIFT.md`
5. `math/QMO6_FORMALISM.md`
6. `contracts/MODULE_EMBEDDING_CONTRACT.md`
7. `contracts/PRIVILEGE_MODEL.md`
8. `pseudocode/END_TO_END.md`
9. `recovery/REBUILD_FROM_ALPHA.md`

## Invariants

1. The runtime communicates only with BRANE.
2. BRANE exposes no direct API, AI, Library, or QMO interface.
3. AI⁵, API⁵, and Library⁵ remain modular and independently replaceable.
4. Canonical module state is immutable during ordinary report generation.
5. Rewrite means derived realization, not canonical overwrite.
6. QMO⁶ is private and ephemeral by default.
7. A complete report cannot be replaced by an index, synopsis, or list of handles.
8. Every requested handle is recovered or explicitly marked unresolved.
9. The external contract remains simple even when internal mathematics is sophisticated.
10. Recursive operations must be cycle-safe and bounded by explicit admissibility rules.
