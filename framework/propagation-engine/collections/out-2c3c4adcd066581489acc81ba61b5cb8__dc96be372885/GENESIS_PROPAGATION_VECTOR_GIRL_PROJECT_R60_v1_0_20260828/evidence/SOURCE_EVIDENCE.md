# R60 — Source Evidence Ledger

## Prime / first fold
`_PRIME.md`

- `|` is Primitive P2, Boundary.
- Boundary action is localization.
- The same identity may have distinct boundary addresses:
  `0_L ≡ 0_R` but `0_L !=pos 0_R`.
- The boundary does not create a second identity; it creates a second address.
- Selecting traversal orientation yields:
  `0_L -> 0_R`
  or the reflected orientation.
- `x -> y` means the realization of `y` depends on information inherited from `x`.

This is the first source-native directed relation.

## TOME / Tiger-Cub
`1.8.pdf`, extracted text

The Tiger-Cub walks a circle and then the same circle in reverse.
The two History traces coexist on the same geometry.
The movement is read as organization rather than pressure/place.
The text states, in substance:
- History is ordered traversal.
- The first fold changed relation, therefore traversed.
- If relation is not preserved there is no History, only replacement.

`1.11.pdf`, extracted text

- The room records occupancy without an external witness.
- Internal relation can carry persistence.
- A visible shape depends on the relation from which it is read while the object preserves something across views.
- History becomes navigable without being clock time.
- Two otherwise identical locations can be distinguished by the path by which they were reached.
- Position plus inherited traversal exceeds plain XYZ.

## Transduction Geometry
`Transduction_Definitions_v0.9.md`

D0: admissibility relation.
D1: formal lift family.
D2: Bandwidth-restricted operative lift family.
D3: Resolution equivalence.
D4: Resolution-quotiented lift family.
D5: Connection selection.
D6:
`Transport = connection-selected state motion along a dependency arrow under a fixed declared dependency/base context.`
D7:
`Transduction = admissible typed transformation that may change dependency/base context.`

This is an essential split for the house toy model:
- moving within a fixed relational/base context can be Transport;
- changing the operative dependency/base context can require Transduction.

## Holonomy & Chirality
`05_PARALLEL_TRANSPORT.md`

For a composable path `gamma = f_n o ... o f_1` with selected lifts:
`P_gamma^Conn = lambda_f_n o ... o lambda_f_1`.

A full event may separately carry:
- state transport;
- chirality transport;
- Identity-Witness transport;
- History append;
- provenance append;
- holonomy update.

These records must not be conflated.

## Identity Through History
`02_IDENTITY_WITNESS_TRANSPORT.md`

Identity Witness:
`W_Id(x,y;h)` certifies endpoint realizations connected by History `h`
belong to the same declared Identity class.

History acts on witness data:
`T_Id(h2 o h1) = T_Id(h2) o T_Id(h1)`.

Thus propagation can alter presentation/occupancy while Identity persists,
provided the witness chain survives.

## Chirality Corridor source
`corridor.md`

The source already defines a transport operator:

`P_W : dXi_alpha -> dXi_beta`

as inherited chirality transport induced by an admissible corridor `W_alpha_beta^3`.

Complete corridor operator:

`C_alpha_beta = Pi_beta o P_W o L_alpha`.

For internal traversal in one localized domain:
`C_alpha_alpha : Sigma_alpha -> Sigma_alpha`.

The source preservation conditions include:
- continuation compatibility;
- chirality compatibility;
- persistent identity;
- invariant residue;
- Resolution threshold;
- Bandwidth threshold;
- recursive closure;
- target closure.

This is the strongest pre-existing candidate for the sought propagation operator.

## Rainbow Road
The Rainbow Road source provides a local History-bearing transaction token:
`p := (id_p, x, ell, y, h_p)`,
with selected lift `ell`, source `x`, target `y`, and History/provenance `h_p`.

It is a useful discrete/local carrier of an admissible propagation event,
not itself the entire propagation law.
