# ASTRAEUS RAINBOW ROAD OBJECT MATHEMATICS API

**Version:** 0.5.0  
**Status:** LIVE / RECURSIVE-CLOSURE / CERTIFIED INTERNAL SELF-PROMOTION  
**Root domain:** `@rainbow_road_recursive_domain`  
**Mathematics root:** `@object_mathematics`

## Runtime ontology

The API is a queryable presentation of Rainbow Road, not an external database pointed at it.

```text
Primitive Structural Zero
        |
        v
Rainbow Road Dynamic Recursive Closure Domain
        |
        +-- Transduction Geometry
        +-- Bandwidth Algebra
        +-- Resolution & Readout
        +-- Identity Through History
        +-- Holonomy & Chirality
        |
        v
closed-domain unity / current whole-domain closure
```

`0` and `1` remain structural labels/objects rather than presumed arithmetic numbers.

## Möbius runtime

White/superpose and Black/neon are local presentation classes of one Road. Traversal can return to a prior local presentation without returning to an identical History state.

**Return is not reset.**

## Closure

`Cl_RR(X)` recursively incorporates internally certified consequences. Semantic closure is idempotent under an unchanged domain contract; History remains append-only.

Internal results can self-promote with a valid Closure Certificate. New primitives/axioms/domain rules cannot.

## Perturbation

`runtime/rainbow_road_runtime.py perturb <scenario>` executes a sandbox reclosure probe. It reports impact cones, hard-guard conflicts, and certificates requiring revalidation without mutating canon.

## Query examples

```bash
python runtime/astraeus_math_api.py domain
python runtime/astraeus_math_api.py object @rainbow_road_recursive_domain
python runtime/astraeus_math_api.py closure-contract
python runtime/astraeus_math_api.py certificates
python runtime/astraeus_math_api.py frontier
python runtime/astraeus_math_api.py crawl @recovery_witness_counterexample_crawl --depth 3

python runtime/rainbow_road_runtime.py status
python runtime/rainbow_road_runtime.py traverse --laps 2
python runtime/rainbow_road_runtime.py close
python runtime/rainbow_road_runtime.py perturb P-001
python runtime/rainbow_road_runtime.py perturb P-004
```

## Logic caveat

Recursive sensitivity is a stress test, not a truth oracle. A false premise can remain internally consistent, and contradiction behavior depends on the logic admitted by the domain. The runtime therefore preserves provenance, reports defects, and separates sandbox reclosure from canonical promotion.


## QMO-addressed semantic live model

Every canonical `@handle` is simultaneously a query address and metadata address. The live metadata layer is not a replacement for the mathematical object; it is the synchronized semantic record of what that object means, its status, typed neighborhood, provenance, closure state, and recovery/history obligations.

Current metadata lives at `library/QMO_METADATA_LIBRARY.json`; metadata history is append-only at `live_model/QMO_METADATA_HISTORY.jsonl`.


## Dependency Landscape QMO Constructor

`@dependency_landscape` constructs a typed dependency network from QMO and/or registered Dependency Landscape inputs. Registered landscapes are themselves QMOs with History, Resolution/Bandwidth context, provenance, and metadata address. The constructor is recursive: landscapes may be used as later inputs.

Landscape inclusion preserves member status and never promotes a member merely because it is mapped.

## Structural Command Namespace — v0.6.0

Canonical discovery is now `@help`. Structural API commands live in `api/COMMAND_REGISTRY.json` and are **not** QMOs by default. The first invocation token resolves against the command registry; later `@...` arguments resolve as QMO/landscape addresses according to the command contract.

This preserves a typed separation:

`@command` = executable structural implementation when used in command position.

`@QMO` = queryable mathematical object when used in object/address position.

`@help` has no QMO record. `@dependency_landscape` is intentionally dual-role: the constructor is a structural command and its mathematical constructor semantics are also represented by a QMO backing object.

