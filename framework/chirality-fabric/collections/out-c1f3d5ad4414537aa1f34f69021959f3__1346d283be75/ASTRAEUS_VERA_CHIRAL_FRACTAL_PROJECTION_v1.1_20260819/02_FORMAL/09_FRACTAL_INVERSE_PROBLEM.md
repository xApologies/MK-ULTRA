# 09 - Fractal Inverse Problem

## Forward model

A source object x is mapped through a family of projections

`y_i = Pi_i(x)`.

The forward problem is to predict the profiles y_i.

## Inverse family

Given observed profiles y_i, the admissible source family is

`A(y_1,...,y_m) = intersection_i Pi_i^{-1}(y_i) intersect X_admissible`.

Adding a probe is useful only if it reduces this intersection.

## Identifiability score

For linearized finite models, define

`rank_m = rank(O_m)` and `nullity_m = n-rank_m`.

For nonlinear models, candidate diagnostics include local Jacobian rank, fiber diameter, posterior volume under a declared prior, or equivalence-class cardinality in a finite state space.

## Probe design

A rational next probe maximizes reduction of the current uncertainty fiber subject to cost/safety/availability constraints. In the linear toy, choose P_new so its row space intersects the current kernel nontrivially.

This provides a clean interpretation of a 'transverse probe': it is a measurement whose sensitivity points into directions discarded by the dominant readout.
