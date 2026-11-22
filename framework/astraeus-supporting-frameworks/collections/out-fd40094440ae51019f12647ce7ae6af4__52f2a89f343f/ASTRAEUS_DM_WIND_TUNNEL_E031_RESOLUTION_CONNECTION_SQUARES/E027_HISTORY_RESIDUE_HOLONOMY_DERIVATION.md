# E027 — Source-Derived History / Residue / Holonomy Structure

## 1. The source answers the History -> Residue question differently than expected

For a source-valid Chirality Corridor history

`H_W = (xi_0, xi_1, ..., xi_N)`

the corridor source requires, for every stage:

`Inv(xi_n) = Inv(xi_0)`.

Therefore define the derived corridor-residue label:

`Res_corr(H_W) := Inv(xi_0)`.

Then:

`Inv(xi_n) = Res_corr(H_W)` for every `n`.

So an admissible History does **not** generally encode itself by changing the invariant
residue. The residue is a preserved label carried through the History.

Corridor composition reinforces this: two corridors may compose only when the arrival
residue of the first matches the departure residue of the second.

## 2. Where does History live, then?

The Version-1 Unified Transduction Object answers this directly.

A successful:

`TRANSPORT(T,path)`

must:
- append the path to `History`;
- update the relevant `Holonomy` records;
- preserve or explicitly revise Identity Witness status;
- preserve provenance.

The UTO explicitly keeps:

`History != Identity`

and:

`Connection != Curvature`.

Therefore the source-aligned map is not:

`History -> new residue value`.

It is structurally:

`History`
-> `transport path`
-> `connection/transport action`
-> `holonomy record`

while invariant residue may remain fixed.

## 3. Bundle interpretation

The canonical Residue / Quantum Field Bundle carries a Hermitian connection.

Field Transport states that curvature measures the obstruction to path-independent
parallel transport.

Thus two different admissible paths with the same endpoints can act differently on
fiber data even when:
- endpoint projection is the same;
- invariant residue class is preserved.

This is exactly the mathematical role of holonomy/path dependence.

## 4. Rainbow Road consequence

Rainbow Road / History should therefore be treated as a candidate **transport history**
through a residue-bearing bundle, not as the residue itself.

A better target is:

`History -> Holonomy acting on/within residue fibers`.

This preserves the firewall:

`route family != invariant residue`.

## 5. Vertical-fiber consequence

E026's fixed Hydrogen quantum-anchor fiber does not need distinct states to be encoded
as different residue labels.

They may instead be different lifted histories/transport states over one readout, with
gravity responding to the path-dependent transport/holonomy organization.

This is a new source-aligned route to the dark pair.

## 6. Möbius connection

A Möbius strip is a useful geometric analogy because a closed traversal can return to
the same base location with reversed local orientation.

Do not promote the Rainbow Road to a literal Möbius bundle from this analogy alone.

But the correct mathematical question is now recognizably holonomic:
what transport transformation is accumulated after traversing the route?
