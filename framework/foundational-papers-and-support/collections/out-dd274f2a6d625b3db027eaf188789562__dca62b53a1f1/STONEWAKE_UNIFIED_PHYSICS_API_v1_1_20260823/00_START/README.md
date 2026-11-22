# Current API companion mapping

> Current API: [GR/QMO](../../../../../../api/gr-qmo/00_START_HERE.md). Its supplied [definitions](../../../../../../api/gr-qmo/INTEGRATION_SPEC.md) and [object dictionary](../../../../../../api/gr-qmo/INSTALLED_OBJECTS.md) govern current API use. The superseded instructions in this block are retired; no equivalence of old runtime behavior or unprovided mathematics is implied. [Original guide and provenance](provenance://unavailable/content-sha256/8da27841b5ad5f0eb1a335b27e1c86127ac7a6ee187d5d62406757f52d1cec98/README.md).

The following retained sections describe this source collection. Historical implementation examples and domain-specific results are not a claim that GR/QMO implements those older interfaces.

# STONEWAKE Unified Physics API v1.1

**Engine root:** `@stonewake_physics`  
**QMO ID:** `QMO-STONEWAKE-PHYSICS-001`  
**Build date:** 2026-08-23

This package is the recursive-expanded engine-facing **single queryable mathematical object** for STONEWAKE physics.

It combines the mathematical content and dependency structure supplied by:

> Current API: [GR/QMO](../../../../../../api/gr-qmo/00_START_HERE.md). Its supplied [definitions](../../../../../../api/gr-qmo/INTEGRATION_SPEC.md) and [object dictionary](../../../../../../api/gr-qmo/INSTALLED_OBJECTS.md) govern current API use. The superseded instructions in this block are retired; no equivalence of old runtime behavior or unprovided mathematics is implied. [Original guide and provenance](provenance://unavailable/content-sha256/8da27841b5ad5f0eb1a335b27e1c86127ac7a6ee187d5d62406757f52d1cec98/README.md).

The game engine does not call five independent APIs. It calls:

```text
@stonewake_physics
```

A runtime interaction asks the root QMO for a local mathematical view. Rainbow Road/corridor routing identifies relevant objects/equations, and the engine then compiles that `LocalPhysicsQMO` into the reduced numerical physics realization required by the active simulation.

```text
native 3+1+1 state
    -> @stonewake_physics
    -> Rainbow Road / corridor resolution
    -> LocalPhysicsQMO
    -> reduced/local 1+3 physics realization
    -> readout
    -> Metal
```

## Contents

- `01_ROOT_QMO/` — canonical root definition.
- `02_MACHINE/STONEWAKE_PHYSICS_QMO.sqlite` — queryable QMO database.
- `02_MACHINE/stonewake_physics_api.py` — minimal query surface.
- `02_MACHINE/unified_*_registry.jsonl` — flat machine-readable equations, objects, and edges.
- `03_MATH_SOURCES/` — math-first source payloads retained for inspection.
- `04_VALIDATION/` — build counts, tests, and hashes.

## Current compiled size

- Objects: **2,797**
- Equations: **898**
- Typed/direct/composed edges: **83,398**

The equation registry is an accelerator, not a claim that every mathematical expression in every source has been uniquely classified as an equation. Canonical math source files are included so no mathematical source content used by this build is replaced by the extracted index.


## v1.1 recursive realization expansion

Adds typed physics-sector hubs, QFT/matter/thermal/fluid/EM/plasma/optics/molecular/transport bridges, source-derived atomic/molecular carrier structures, bounded dependency-expanding local QMO queries, and derived-QMO templates including plasma channel and poison cloud. The graph is intentionally dense but not semantically meaningless all-to-all.
