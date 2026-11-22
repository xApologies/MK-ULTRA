# WL-v207 — Mote Gluing-Data Instance Gap

**QMO:** QMO-AST-DM-WL-091  
**Work layer:** WL-033  
**Parent promotions:** 0  
**Status:** INSTANCE GAP / NO GENERAL-LAW GAP

## Handle recovery

`@gluing_data` is already a typed Transduction Geometry object:

```text
representative local transition maps
+
equivalence/gauge class
for reconstruction and descent auditing.
```

For the mote assembly problem, an instantiated gluing-data object would have to say at minimum:

```text
1. which local mote carriers are allowed to meet / overlap;
2. which relative-orientation transition is assigned on an overlap;
3. whether the pairwise transitions remain compatible on represented triple overlaps;
4. how local recovery identifies the resulting global object with an ER-adjacency presentation.
```

## What source already supplies

The chirality-cell source supplies pairwise local semantics:

```text
C_a ·_rho C_b = C_c
iff
A(C_a,C_b,rho)=1
```

and explicitly states:

```text
orientation generates adjacency
R_i(C_z)=C_i
```

The mote source supplies a two-layer `2x2x2` occupancy representation and says chirality-labelled motes can assemble into ER-foam lattices.

The canonical ER source supplies the target weighted-adjacency typing:

```text
W_ij >= 0
W_ij = W_ji
```

## What source does not supply

No mounted source currently supplies a complete mote-specific object containing:

```text
overlap selector
+ pairwise transition maps
+ triple-overlap coherence data
+ ER recovery/gluing witness.
```

Therefore the remaining assembly blocker is not the absence of a general gluing formalism. It is the absence of a **mote-specific gluing-data instance**.

## Source conflict firewall

The primitive chirality cell and the canonical mote have matching layered occupancy representations in the worked sector, but they are not promoted to ontological identity. A representation match may be used as candidate input; identity may not.

## Next handle

The Transduction Geometry API exposes the distributed object designed to package exactly this kind of local admissibility + overlap-transition structure:

```text
@chirality_fabric
```

Status in its own formal package: `STRONG_CANDIDATE`.
