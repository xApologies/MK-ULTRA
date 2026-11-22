# 05 - Tree-Cycle Holonomy Gate (Acyclicity Result)

## Statement

A connected tree T has

`beta_1(T)=|E|-|V|+1=0`.

Therefore it has no nontrivial graph cycles on which ordinary loop holonomy can be evaluated.

## Z2 gauge proof

Choose a root r and set `g_r=+1`. Traverse each tree edge outward. For an edge u-v with u already assigned, choose

`g_v = g_u sigma_uv`.

Then the transformed edge sign is

`sigma_uv' = g_u sigma_uv g_v = +1`.

Because a tree has a unique path from the root to each vertex, this assignment is consistent for every vertex. Hence every Z2 edge-sign configuration on a tree is gauge-equivalent to the trivial all-plus configuration.

## Consequence for E056

The E054-E056 weighted corridor **merge tree** cannot by itself carry a nontrivial loop-holonomy class. Therefore the new fractal/holonomy idea must not be retrofitted onto E056 by computing fictitious cycles on the merge tree.

A dark-matter holonomy test must instead use one of:

1. the original cyclic ER/connectivity graph before tree reduction;
2. a lifted transport square/commutative diagram in Resolution/context space;
3. a fiber attached to tree nodes/edges whose state is not represented by graph-cycle topology;
4. another source-authoritative path family with genuine alternative routes.

This acyclicity result is a Vera gate and a major reason the package is useful. It rules out only ordinary graph-loop holonomy on tree cycles; it does not rule out chirality or lifted/source/fiber holonomy.
