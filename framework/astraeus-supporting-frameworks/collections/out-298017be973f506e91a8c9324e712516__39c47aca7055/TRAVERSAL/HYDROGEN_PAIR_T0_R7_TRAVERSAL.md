# Two-Hydrogen Pair — Pipeline-Native Traversal

**Inputs:** two ancestry-distinct copies of the supplied H v2 manifold, `H_A` and `H_B`.  
**Rule:** no element-specific chemistry rule is added to Pipeline 1 or Pipeline 2.  
**Status:** SOURCE-CONSTRAINED TOPOLOGY TRAVERSAL.

## Why this is not a chemistry lookup

The environment contains universal domain rules. The H-specific information is carried by the input manifold itself. In particular, the supplied H v2 manifold explicitly contains a nonzero `pair_closure_topology_H2` field and environment-admissibility / closure / redistribution fields derived during the hydrogen manifold construction.

The supplied Pipeline 2 explicitly prohibits rules such as “hydrogen always forms H2.” R4 may form corridor candidates; R5 may select only the lowest-strain recoverable constrained topology; R6 must test survivability; R7 must verify persistence.

## Pipeline 1 preparation

Run each H manifold through T0-T7 independently. Both arrive at the Pipeline 2 handoff as H-class, ancestry-preserving, coupling-ready topologies.

## Pipeline 2 pair ecology

### R0 — Identity registration
Record `H_A` and `H_B` as separate ancestry sources. Chirality is read-only.

### R1 — Interaction surface mapping
Map local adjacency, shell-facing surfaces, compatibility, and overlap possibilities. No coupling is forced.

### R2 — Controlled continuity transfer
Permit bounded shell-sharing / continuity exchange while preserving both source identities.

### R3 — Persistent coupling ecology
If the pair interaction recurs coherently, preserve pair corridor/shell-sharing memory as a real ecology rather than transient contact.

### R4 — Corridor formation / elastic coupling

```text
R4 forms possibility.
```

R4 consumes local adjacency, read-only chirality, deformation/strain context, and ancestry. It may emit a pair corridor candidate but cannot decide the final topology.

The supplied H manifold has nonempty support for both its pair-closure topology and environment-admissibility fields; their positive-support intersection contains 32,764 of 32,768 grid sites. This is a descriptive source-manifold fact, not an R4 scoring formula.

### R5 — Ordered topology resolution

```text
R5 resolves possibility.
```

R5 compares accessible corridor topologies under finite bandwidth, chirality occupancy, elastic strain, recoverability, and ancestry preservation.

For a two-manifold H ecology there is no three-body corridor proliferation to resolve. The source H manifold supplies explicit H2 pair-closure admissibility, and the Pipeline 2 Phase-3 expectation for H+H is weak symmetric shell-sharing equilibrium. The R5-selected pair closure is retained only if it is the most recoverable accessible topology.

### R6 — Constrained survivability stabilization

```text
R6 stabilizes survivability.
```

R6 applies recursive recovery/damping. It must preserve a valid pair corridor and may reject it only if strain, bandwidth, chirality occupancy, or recoverability fail.

### R7 — Oscillatory persistence
Expose the pair topology to recursive oscillatory persistence. A valid pair remains coherent, ancestry remains recoverable, and the corridor cannot runaway-expand.

## R7 topology result

Under the supplied H-v2 pair-closure manifold contract and Pipeline 2 universal topology rules, the stable two-H branch is recorded as:

```text
H_A + H_B
   -> bounded pair corridor
   -> ordered pair closure
   -> survivable pair topology
   -> H2-class R7 topology
```

This traversal does not insert `H2` as a Pipeline rule. The output label names the recovered pair topology already represented by the H input manifold's `pair_closure_topology_H2` channel.
