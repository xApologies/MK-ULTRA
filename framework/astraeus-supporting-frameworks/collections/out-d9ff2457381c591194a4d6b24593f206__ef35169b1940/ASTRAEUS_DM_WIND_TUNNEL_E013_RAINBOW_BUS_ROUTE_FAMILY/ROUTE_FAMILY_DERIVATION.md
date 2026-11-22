# E013 — Rainbow Bus Route-Family Object

The mounted Rainbow Road source defines:

- `Rainbow Bus = available color-indexed transport fabric`
- `Portal = one transaction on that fabric`
- `Rainbow Road = one persistent navigable route through a sequence of portal transactions`

E012 found no single connected B=2 route that is invariant under every tested condition.
Therefore the robust object should not be forced into the form of one frozen road.

For each state `x` and tested environment/selection condition `theta`, define:

`Gamma_theta(x) = { connected B=2 routes optimal at both p=0 and p=1 }`.

If `Gamma_theta(x)` is nonempty for every `theta`, the state passes strict T5 route persistence.

Define the **persistent route family**:

`F_route(x) = union_theta Gamma_theta(x)`.

This is a work-layer route-family object.
It is not automatically:
- an Invariant Residue;
- a completed Portal transaction;
- an ER throat network;
- a physical Rainbow Road.

Its useful role is to encode which persistent routes the Rainbow Bus can make
available to the same state as local admissibility/selection context varies.

A pair with the same coarse readout but:

`F_route(x) != F_route(y)`

has a route-level hidden distinction that survives the T5 persistence boundary.
