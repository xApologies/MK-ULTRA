# C03 — Chirality Relaxation and Knot Algebra

**Verdict:** CLOSED — `Z2 COHOMOLOGY-VALUED KNOT CANDIDATE WITH CAPACITY-WEIGHTED RELAXATION`

## Minimal diagnostic lift

Let `x_v in Z2` record whether a seed has reoriented relative to its C01 baseline. Let `f_e in Z2` record the candidate backreaction phase carried by a Fusion seam. The closure condition on each edge is

`x_u XOR x_v = f_e`.

In cochain language, `x` is a 0-cochain, `f` is a 1-cochain, and exact closure is

`delta x = f`.

### Closure theorem

A Fusion-backreaction seam pattern can be completely absorbed by chirality reorientation iff

`f in im(delta)`.

Equivalently, the XOR of `f_e` around **every cycle** is zero. If not, `[f] != 0` in `H^1(G;Z2)` and no sequence of vertex reorientations can erase the residual cycle syndrome.

This gives a mathematically precise work-layer candidate for a **continuous chirality knot**:

`K_chi := [f] in H^1(G;Z2)`.

The microscopic `x` representative may change repeatedly while the knot class remains fixed. Thus a stable object can be an equivalence class of reconfiguring chirality states rather than one frozen arrangement.

## Capacity-weighted relaxation

Assign every edge a positive capacity

`c_e = C(basin_u, basin_v, R_e, B_e) > 0`.

No physical calibration is imposed. Relaxation selects `x` by minimizing

`Phi_chi(x;f) = sum_e c_e * [x_u XOR x_v != f_e]`.

The six basin labels therefore can alter *where* the reorientation travels without changing the topological knot class.

## Single-seam cut theorem

If one Fusion seam `e=(a,b)` is treated as a hard backreaction constraint, satisfying it requires `x_a != x_b`. The violated soft constraints are exactly the edges crossing the cut between the two reorientation domains. Therefore the least disturbance is the weighted `a-b` min-cut in `G-e`.

On the exact equal-capacity C01 diagnostic:

- 16 conditional mirror-class Fusion sites were tested;
- 12 have minimum soft cut 2;
- 4 have minimum soft cut 3.

So a binary seam can have multi-edge consequences without any higher-valence Fusion operation.

## Finite knot/unbinding witness

The same-handed connectivity of the supplied two-layer map contains a two-vertex cross-layer component. Its four surrounding mirror-class seams form an exact coboundary; all four can be absorbed by a coherent two-layer reorientation with zero residual frustration.

Add one additional mirror-class seam elsewhere. The five-seam pattern has minimum residual frustration 1 and nontrivial cycle syndrome. Removing that one extra seam returns the pattern to the four-seam coboundary and the exact minimum drops to 0.

This is the first finite **unbinding -> relaxation** witness:

`nontrivial knot representative -> remove one seam -> trivial class -> complete relaxation`.

It is a structural model only. `Delta Phi_chi` is organizational release, not yet physical energy or Hawking luminosity.

## Exact finite dimensions

For this diagnostic graph:

- `|V| = 16`
- `|E| = 28`
- `dim H^1(G;Z2) = 13`
- mirror-class Fusion edge span accesses 11 independent cohomology directions under the declared A/B bridge.

The last number is a statement about this finite graph and candidate lift, not about the universe.
