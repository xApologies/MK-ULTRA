# 83 — Time-Shell Typed Projection Namespace

The API overloads `Pi_T`. Atlas v10 resolves the collision by typing projection channels explicitly.

## Configuration/History projection

```text
Pi_TS^conf : R^3 x A x Chi_H -> M_(1,3)
```

with the recovered map

```text
Pi_TS^conf(X,Y,Z;A;chi_H) = (T,X,Y,Z).
```

## Gravitational projection

```text
Pi_TS^grav : C_TT -> H_2
```

where `C_TT` is the admissible transverse/tensor continuity-perturbation sector and `H_2` denotes readable symmetric rank-two metric perturbations.

Recovered weak-field statement:

```text
Pi_TS^grav(deltaC) = h_mn.
```

## Persistent-boundary projection

The foundational kernel separately contains a boundary projection

```text
Pi_boundary : dXi -> M
```

from persistent-boundary organization into a projective target manifold.

## Other Pi symbols

Keep separate:

```text
Pi_persist   persistence potential
Pi_occ       recursive occupancy projection
Pi_boundary  persistent-boundary projection
Pi_TS^conf   Time-Shell configuration/History projection
Pi_TS^grav   Time-Shell gravitational projection
```

## Rule

No two `Pi` operators may be identified solely because historical source notation reused the same glyph.
