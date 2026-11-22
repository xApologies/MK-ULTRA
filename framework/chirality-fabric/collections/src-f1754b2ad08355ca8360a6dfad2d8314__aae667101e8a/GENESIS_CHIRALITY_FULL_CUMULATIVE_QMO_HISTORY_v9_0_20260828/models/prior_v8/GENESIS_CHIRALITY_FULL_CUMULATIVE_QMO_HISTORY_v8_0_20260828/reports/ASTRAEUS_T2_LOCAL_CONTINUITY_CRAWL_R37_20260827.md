# ASTRAEUS — T2 LOCAL-CONTINUITY CRAWL R37

**Date:** 2026-08-27

## Verdict

The torus-continuity model closes structurally and then reaches one exact roadblock: **the basin-specific Bandwidth tangent rule is missing.**

## Primitive local geometry

`T2 = S1_A × S1_B`.

Each S1 has six cyclic basin sectors in rainbow order.

At coarse basin-cell level, continuity gives only four primitive oriented crossings from each ordered cell:

`A+`, `A-`, `B+`, `B-`.

There are 36 cells and 144 oriented local adjacency edges.

This replaces the old ten arbitrary one-side color substitutions per cell as the primitive-dynamics candidate. Long-range color changes become composed History paths.

## Closure R37.1 — Reachability

Every starting cell reaches all 36 cells using only neighboring cyclic crossings.

So continuity preserves the useful global reachability of the old 360-edge graph while using only 144 local primitive edges.

Shortest-path distribution over all ordered cell pairs:

`{0: 36, 1: 144, 2: 288, 3: 360, 4: 288, 5: 144, 6: 36}`.

Maximum coarse distance: `6` boundary crossings.

## Closure R37.2 — Winding History

Lift the six-sector torus discretization to `Z²`.

A complete traversal of one S1 factor requires six neighboring basin crossings and returns to the same torus cell while changing winding History.

Representative length-six nonzero winding loops:

[
  [
    [
      1,
      0
    ],
    [
      "A+",
      "A+",
      "A+",
      "A+",
      "A+",
      "A+"
    ]
  ],
  [
    [
      -1,
      0
    ],
    [
      "A-",
      "A-",
      "A-",
      "A-",
      "A-",
      "A-"
    ]
  ],
  [
    [
      0,
      1
    ],
    [
      "B+",
      "B+",
      "B+",
      "B+",
      "B+",
      "B+"
    ]
  ],
  [
    [
      0,
      -1
    ],
    [
      "B-",
      "B-",
      "B-",
      "B-",
      "B-",
      "B-"
    ]
  ]
]

Thus same current Resolution cell does not determine History.

This is the coarse discrete realization of `π1(T2)=Z×Z`.

## Closure R37.3 — Resolution depth unifies with lifted torus History

Resolution depth need not be a second independent history object.

A finite inherited Resolution history can be represented by a lifted torus path:

`H_R = ((cell_0,lift_0),...,(cell_n,lift_n))`.

The torus cell records current shared basin Resolution.

The lifted coordinate records accumulated winding/history.

In the continuous refinement, `Z²` becomes the universal cover `R²`.

So the earlier graph-valued Resolution-depth model and the torus path model are compatible descriptions of one inherited transport object.

## Bandwidth location

Before Bandwidth filtering, the local tangent alphabet is:

`{A+, A-, B+, B-}`.

The operative tangent set must be some subset:

`T_B(x) ⊆ {A+, A-, B+, B-}`.

At the coarse level there are 15 possible nonempty availability masks per cell.

The current recovered model does not uniquely choose one.

## Failure R37.F1 — Torus geometry alone does not actualize

The torus is symmetric under reversal of either circular coordinate.

Topology alone therefore cannot prefer `A+` to `A-`, or `B+` to `B-`.

It supplies:
- continuity;
- local adjacency;
- orientation labels;
- winding;
- path History;
- same-endpoint/different-History structure.

It does not supply the operative tangent selection.

## Closed architecture

`T2`
`-> four local oriented tangent candidates`
`-> Bandwidth filter`
`-> connection`
`-> continuous path`
`-> sector crossing`
`-> basin update`
`-> retained winding / Resolution History`.

A19/KOR remains downstream as a witness/completion gate if needed.

## Exact roadblock

The next missing map is:

`(basin, Resolution-depth History) -> T_B(x) ⊆ {A+,A-,B+,B-}`.

Further deletion or ranking of tangent directions without that law would be invention.

## Final status

- T2 local continuity: PASS.
- 36-cell reachability: CLOSED.
- old arbitrary long-range primitive jumps: unnecessary.
- winding/History: CLOSED structurally.
- Resolution depth as lifted torus path: CLOSED as model identification.
- topology-only actualization: FAIL.
- basin-specific Bandwidth tangent law: ROADBLOCK / OPEN.
