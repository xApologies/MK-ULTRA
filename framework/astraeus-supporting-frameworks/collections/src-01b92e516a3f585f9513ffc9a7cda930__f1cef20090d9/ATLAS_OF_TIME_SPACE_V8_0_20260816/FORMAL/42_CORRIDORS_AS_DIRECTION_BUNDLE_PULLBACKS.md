# 40 — Corridors as Direction-Bundle Pullbacks

## Status

`DERIVED_FROM_ATLAS_CANDIDATE + STANDARD_BUNDLE_MATHEMATICS`.

## Path in the continuity domain

Let

```text
gamma : I=[0,1] -> S3
```

join two continuity addresses `p_alpha` and `p_beta`.

Pull back the unit tangent bundle:

```text
W_gamma := gamma^*(UTS3).
```

Because every bundle over an interval is trivial,

```text
W_gamma ~= S2 x I.
```

Its oriented endpoint boundary is

```text
partial W_gamma
=
S(T_palpha S3) disjoint_union (-S(T_pbeta S3)).
```

This reproduces the Genesis Chirality Corridor topology

```text
S2 x [0,1]
```

without inserting a portal tube by hand.

## Direction transport

Let `nabla^3` be an admitted connection on `TS3`. A unit direction `v_alpha in S(T_palpha S3)` can be transported along `gamma` by

```text
nabla^3_{gamma_dot} v = 0,
h3(v,v)=1.
```

This defines a map

```text
P_gamma^dir : S(T_palpha S3) -> S(T_pbeta S3).
```

A chirality/Helicon connection may refine this transport by carrying additional internal orientation/history data.

## Corridor identity

The corridor is therefore not a tunnel added to Time-Space. It is the five-dimensional direction-state family lying over an admissible path in the `S3` continuity domain.

```text
path in S3
   -> pullback of Time-Space
   -> S2 x I corridor.
```
