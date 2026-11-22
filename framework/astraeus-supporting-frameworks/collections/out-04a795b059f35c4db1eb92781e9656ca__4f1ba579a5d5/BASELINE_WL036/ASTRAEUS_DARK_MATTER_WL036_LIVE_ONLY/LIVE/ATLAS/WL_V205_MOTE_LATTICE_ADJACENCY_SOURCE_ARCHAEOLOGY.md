# WL-v205 — Mote-Lattice Adjacency Source Archaeology

**QMO:** QMO-AST-DM-WL-089  
**Work layer:** WL-033  
**Parent promotions:** 0  
**Status:** SOURCE AUDIT / GAP CONFIRMED AND RETYPED

## API question

Starting at the WL-v204 next handle:

```text
@mote_lattice
```

ask whether Time-Space API 4.3 already contains a source-native eight-site neighbor selector or a source-native rule deriving ER assembly from mote adjacency.

## Recovered local object family

Time-Space API 4.3 defines:

```text
Lambda_mote = {0,1}^3
n : Lambda_mote -> {0,1}
```

and the direct source chain:

```text
@mote
  -> @mote_lattice
  -> @mote_occupancy_function
  -> @mote_diagonal_rule
  -> @mote_chirality
  -> @chirality_occupancy_cube
```

The API also contains the recursive local update scaffold

```text
chi_(t+1)(x,y,z)
  = Pi_occ(
      sum_(n in N(x,y,z)) w_n chi_t(n)
      - lambda chi_t(x,y,z)
    )
```

but explicitly states:

```text
[OPEN] The exact adjacency graph N(x,y,z) for the eight-site mote
       has not been recovered.
```

and separately:

```text
[OPEN] Define adjacency edges on the eight-site lattice explicitly.
[OPEN] Derive ER-foam assembly rules from mote adjacency.
```

## Source archaeology result

Three nearby sources do **not** silently close this gap:

1. `@mote_diagonal_rule` constrains occupancy/chirality classification; it does not define site adjacency.
2. the older Planck-scale ER network source defines a weighted undirected adjacency `W_ij >= 0`, `W_ij=W_ji`; it does not select which mote sites or mote pairs carry an edge.
3. the Phase I-III primitive substrate rule `e_ij exists iff A(s_i,s_j,rho_ij)=1` is a general admissibility law on substrate states; the API does not provide a typed map identifying each eight-site mote coordinate with the complete primitive state required by that evaluator.

Therefore the missing object is now more precise:

```text
not: another gravity law
not: another density law
not: a scalar profile

missing: a mote-local / mote-interface admissibility instance
         that selects overlaps/edges and can be realized as ER adjacency.
```

## Next handle

The source-native next handle is not a new hand-written distance rule. It is the formal admissibility object already available in Transduction Geometry:

```text
@admissibility_relation
```

The next QMO asks whether the mote-to-ER assembly gap can be typed as a local-to-global admissibility/gluing problem rather than solved by inventing a nearest-neighbor metric.

## Guardrails

- `@mote_diagonal_rule != mote adjacency law`.
- `W_ij>=0, W_ij=W_ji` does not select edges.
- the 6-neighbor convention used in an older 32^3 boundary experiment is an experimental extraction convention, not canonical mote adjacency.
- primitive `A(s_i,s_j,rho_ij)` does not by itself provide the missing mote site-state realization.
- no ER H0/H1 incidence pair is promoted.
