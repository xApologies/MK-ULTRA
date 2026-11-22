# Astraeus Rainbow Road Object Mathematics API v0.8.0

**Version:** 0.7.0  
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


## Self-build pass 003 result

`CE-RW-001` refutes universal sufficiency of an unqualified core recovery witness. `@theorem_witness_fiber_separation` and `@recovery_discriminator` are internally closure-certified. The new frontier is `@recovery_history_signature_minimality`.


## QMO-addressed live model (v0.4)

The API now has a synchronized semantic live model. Every canonical QMO handle is also its metadata address.

```bash
python runtime/astraeus_math_api.py qmo @resolution
python runtime/astraeus_math_api.py meta @resolution
python runtime/astraeus_math_api.py meaning @resolution
python runtime/astraeus_math_api.py qmo-history @resolution
python runtime/astraeus_math_api.py api-live
python runtime/qmo_live_model.py validate
```

Operational registries answer what the API can do. The QMO-addressed metadata library answers what each object means, its current state, provenance, relations, closure state, and recovery contract. Metadata History is append-only.


## Dependency Landscape / structural @command help (v0.6)

```bash
python runtime/astraeus_math_api.py @help
python runtime/astraeus_math_api.py @help dependency_landscape
python runtime/astraeus_math_api.py dependency-landscape @recovery_history_signature_minimality @holonomy_history_signature --depth 2
python runtime/astraeus_math_api.py landscapes
python runtime/astraeus_math_api.py landscape @dl_history_signature
python runtime/astraeus_math_api.py landscape @dl_history_resolution_bridge
python runtime/astraeus_math_api.py landscape-history @dl_history_signature
```

Dependency Landscapes are queryable mathematical objects, not pictures or disposable reports. Their inputs may themselves be landscapes.


## Canonical command syntax

`@help` is the discovery command. It lists structural implementations, not QMOs. Canonical examples:

```bash
python runtime/astraeus_math_api.py @help
python runtime/astraeus_math_api.py @qmo @resolution
python runtime/astraeus_math_api.py @dependency_landscape @recovery_history_signature_minimality @holonomy_history_signature --depth 2
```

The old `/help` form is retained only as a compatibility alias and is not the canonical interface.


## Dependency Graph + Dependency Chain (v0.7)

`@dependency_graph` constructs focused graph QMOs. `@dependency_landscape` now accepts QMO, graph, and landscape inputs. `@dependency_chain` recursively crawls and resolves unique registered progression edges, constructs graph/landscape steps, and preserves the ordered chain as its own QMO.

```bash
python runtime/astraeus_math_api.py @qmo_types
python runtime/astraeus_math_api.py @graph_types
python runtime/astraeus_math_api.py @dependency_graph @A @B --mode path --register --handle @dg_example
python runtime/astraeus_math_api.py @dependency_landscape @dg_example @some_qmo --register --handle @dl_example
python runtime/astraeus_math_api.py @dependency_chain @some_frontier --max-steps 5 --register --handle @dc_example
python runtime/astraeus_math_api.py @chain @dc_example
```

A chain QMO may become a closed subdomain only after terminal fixed-point closure is certified.


## Bounded mathematical iteration

Black Rainbow is the closed landscape; Rainbow Road/Mobius supplies recursive runtime/carrier behavior. Use `@iterate` for a finite-horizon recursive QMO search. Example: `@iterate @seed --iterations 1000000 --mode chain --target @target`. The bound is a ceiling; the runtime terminates early on closure/fork/cycle/target/defect.
