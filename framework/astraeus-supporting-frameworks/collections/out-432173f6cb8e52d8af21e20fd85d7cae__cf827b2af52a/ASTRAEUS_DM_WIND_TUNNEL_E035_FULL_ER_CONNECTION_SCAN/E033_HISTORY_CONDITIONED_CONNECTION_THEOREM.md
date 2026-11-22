# E033 — History-Conditioned Operative Connection

## 1. Source architecture

The Transduction source explicitly defines:

`D_B(x | E,H)`

and revises the active graph to:

`G_active(R,B,E,chi,H)`.

It also states:

`Lift_f^B(x | H,E)`,

and distinguishes:

`p_static`

from:

`p_oper(H,E,B)`.

A history/environment change can therefore remove an otherwise formally admissible
lift without changing the static dependency skeleton.

In connection language:

`Conn_oper(...|H_n)`

can evolve recursively through a dynamic admissibility mask.

Bandwidth loss is described as:

`loss of horizontal transport directions`.

## 2. Controlled support-gate diagnostic

The source does not provide a numerical map from the E003 environment fields to
`LiftSet_B`.

E033 therefore introduces one explicit **work-layer diagnostic gate**, not a source law:

A contextual Hydrogen Resolution direction is locally operative at the E018 target iff
its corresponding environmental field has nonzero support in the exact `2x2x2` target
patch.

This is deliberately minimal:
- it does not rank lifts;
- it does not weight lifts;
- it only tests support/no-support.

## 3. Target-patch result

At the E018 conditioned-only target patch:

Fresh environment:
- chirality direction: supported;
- adjacency direction: supported;
- corridor direction: **unsupported**;
- persistence direction: supported.

H2-conditioned environment:
- all four directions are supported.

The corridor result is especially strong because fresh corridor memory is identically
zero over the entire `32^3` environment, while conditioned corridor memory is nonzero.

## 4. Operative connection signatures

Formal static skeleton:

`{chi, adjacency, corridor, persistence}`

for both states.

Controlled operative horizontal sets:

Fresh:

`Hor_oper^fresh = {chi, adjacency, persistence}`.

Conditioned:

`Hor_oper^cond = {chi, adjacency, corridor, persistence}`.

Thus:

`Hor_oper^fresh != Hor_oper^cond`

while the Hydrogen quantum anchor remains the same.

This realizes, at controlled work-layer level, the source distinction:

`static fabric signature`
!=
`operative transport signature`.

## 5. Resolution graph consequence

Fresh operative Resolution graph:
- 3 horizontal directions;
- 8 nodes;
- 12 cover edges;
- 3 elementary squares;
- 6 full refinement orders.

Conditioned operative Resolution graph:
- 4 horizontal directions;
- 16 nodes;
- 32 cover edges;
- 6 elementary squares;
- 24 full refinement orders.

The three newly available conditioned squares are precisely the squares containing the
corridor-memory direction.

So History conditioning does not merely change a scalar response.

Under the controlled gate it changes the **available loop/holonomy opportunity space**.

## 6. What is and is not established

Established in the controlled diagnostic:

`same [Q_H]`
+
`different H/E-conditioned operative lift availability`.

Not established:

- the physical Bandwidth law that turns field support into lift availability;
- a numerical connection matrix;
- a physical holonomy value;
- gravitational readout.

The result is therefore an **operative-connection separation**, not yet a physical
holonomy separation.

## 7. Dark-matter significance

E032 showed pure Resolution-order holonomy is common scaffolding and does not explain
the dark pair.

E033 shows the pre-existing environmental History can instead change **which
Resolution/connection directions exist at all**.

This is a much sharper role:

`History`
-> `operative Bandwidth/admissibility mask`
-> `available horizontal lifts`
-> `available loops`
-> `possible holonomy/curvature measurements`.

The next test should avoid inventing weights and ask whether this support-gated
connection separation correlates with the already-established UCM/pre-G response
separation across multiple local patches, not just the selected E018 target.
