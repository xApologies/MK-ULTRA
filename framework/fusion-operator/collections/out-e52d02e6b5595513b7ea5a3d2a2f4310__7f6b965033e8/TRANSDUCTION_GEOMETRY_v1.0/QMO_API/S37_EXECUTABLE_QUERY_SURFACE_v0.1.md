# S37 — EXECUTABLE QUERY SURFACE / API CONSOLIDATION v0.1

Status: STRONG PASS / PORTABLE REFERENCE RUNTIME

## Purpose

Expose the Unified Transduction Object through a small executable query surface.

## Implemented reference operations

```text
GET_OBJECT
GET_FORMAL_LAYER
GET_DEPENDENCIES
GET_PROVENANCE
GET_RESEARCH_DEBT
FORMAL_IDENTITY
OBSERVATIONAL_IDENTITY
VIEW
AVAILABLE_TRANSFORMS
RESOLUTION_GEOMETRY
HISTORY
HOLONOMY
IDENTITY_TEST
ROBUSTNESS
TRANSPORT
ROADMAP
```

## Runtime philosophy

The reference runtime is deliberately small and stdlib-only.

It is not a symbolic theorem prover.

It is a portable recovery/query layer that:
- reads the QMO/Library registries;
- preserves the critical semantic distinctions;
- exposes the roadmap;
- returns schema-level responses when a concrete instantiated object is absent;
- refuses to pretend a transport mutation occurred when only the contract is known.

## Query examples

```text
python transduction_runtime_v0_1.py <workspace> ROADMAP

python transduction_runtime_v0_1.py <workspace> GET_OBJECT --handle @admissibility_relation

python transduction_runtime_v0_1.py <workspace> VIEW --handle @formal_lift_family --resolution R3 --bandwidth B2 --history H7

python transduction_runtime_v0_1.py <workspace> HOLONOMY --handle @chirality --kind chirality --loop loop_01
```

## Validation target

A fresh runtime must be able to:
1. load without external dependencies;
2. read current registries;
3. answer ROADMAP;
4. retrieve known QMO objects;
5. return formal/observational identity distinction;
6. expose Bandwidth Algebra and Resolution Landscape metadata;
7. expose research debt;
8. expose transport mutation contract without fabricating execution.

## Result

The mathematical landscape is now queryable at a minimal executable level.

Next:
S38 Recovery Bootstrap + fresh-model test.
