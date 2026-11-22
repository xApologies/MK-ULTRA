# WL-v263 — Adjacency Extractor to UCM Admission Reduction

**Work layer:** WL-041  
**Status:** TYPE-REDUCTION / REPRESENTATION BRIDGE PARTIALLY CLOSED  
**Parent promotions:** 0

## Source-side adjacency is not missing

The chirality source explicitly treats the 2x2x2 arrangement as primary and lists

```text
occupancy,
adjacency,
orientation,
handedness
```

as structural properties of the chirality byte/tiny manifold.

Therefore there is no need to invent adjacency from scratch. Define the ordinary structural extractor

```text
Adj : LayeredChiralityGeometry -> AdjacencyRecord
```

that forgets all data except the source-declared incidence/adjacency relation.

For the full and visible records:

```text
A_full^LC := Adj(C_z),
A_vis^LC  := Adj(P_top(C_z)).
```

Projection loss can therefore be tested directly as

```text
A_full^LC ?= A_vis^LC.
```

## UCM-side typing

UCM independently consumes an adjacency/topology coordinate `A` and has an explicit corridor-incidence branch.

The old single missing symbol

```text
phi_A : LayeredChiralityGeometry -> UCM.Adjacency
```

is therefore reduced into two roles:

```text
Adj                    [SOURCE-AVAILABLE STRUCTURAL EXTRACTION]
ι_A^U : AdjacencyRecord -> UCM.AdmittedAdjacency   [OPEN SCHEMA/PHYSICAL ADMISSION]
```

with

```text
phi_A = ι_A^U o Adj.
```

## Why this matters

The missing physics is no longer 'how can layered geometry have adjacency?'

The missing problem is narrower:

```text
Does the source-declared layered adjacency satisfy the exact UCM admissibility/schema contract for an operative coupling event?
```

No identification of an internal channel with an ER throat is made.
