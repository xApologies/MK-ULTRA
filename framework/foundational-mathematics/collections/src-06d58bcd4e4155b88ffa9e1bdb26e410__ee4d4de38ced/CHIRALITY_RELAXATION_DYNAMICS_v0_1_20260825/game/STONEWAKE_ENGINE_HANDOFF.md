# C04 — Downstream Tests and STONEWAKE Physics-Engine Handoff

**Verdict:** CLOSED — `ENGINE-READY DISCRETE CORE; PHYSICAL IDENTIFICATIONS REMAIN OPEN BRIDGES`

## STONEWAKE engine object

A runtime domain can store:

`DomainState = (nodes, edges, chirality, basin, resolution, bandwidth, fusionSeams, persistence, history)`.

An event is:

`FUSE(edge)` or `UNBIND(edge)`.

The update pipeline is:

`event -> validate Fusion domain/ports -> update seam registry -> apply backreaction rule if enabled -> relaxation queue / local cut solver -> persistence test -> readout/effects -> append History`.

The engine can use six basin labels as configurable edge/vertex capacities. A low-capacity corridor can carry a large reorientation farther around the map; a high-capacity boundary can confine it. No fixed monotone mapping from Red..Violet to physical energy is assumed until supplied.

## Why this is useful for gameplay

One local shaping/Fusion event can deterministically alter a larger neighborhood while preserving a compact invariant. The engine therefore gets:

- local-to-domain ripple without arbitrary random propagation;
- persistent knots/defects that survive microscopic reshuffling;
- reversible or partially reversible unbinding events;
- natural closure/saturation conditions;
- provenance/history for replay, save-state, debugging, and deterministic regeneration;
- a clean hook for Metal visuals: render changed edges/nodes from the returned relaxation set rather than simulate decorative noise first.

## QCD comparison target

The present diagnostic is `Z2` and therefore Abelian. It is **not** QCD. The useful resemblance is constrained local reconfiguration. A true non-Abelian comparison requires a group, connection, representation, curvature/self-coupling, constraints, and observable map. That is a future upgrade, not a premise.

## Black-hole / Hawking comparison target

Repeated `UNBIND` events can reduce a nontrivial seam class until `[f]=0`, at which point the domain can fully relax. This gives a precise upstream meaning to "the chirality knot unravels." To call the resulting release Hawking radiation requires a new realization map from organizational release / state change to the semiclassical radiation and mass-loss sector.

## S2 / S3 residue target

The internal mapping gives localized readable S2 fibers and an S3 continuity domain with chirality transport. If a local knot ceases to persist in one readable domain, a future bridge may ask whether its History/invariant residue remains encoded in the wider continuity layer or hidden S3 network. No cycle-memory or Mode-0 transfer law is asserted here.

## Final architecture

`Fusion seam -> candidate backreaction -> chirality relaxation -> persistence class -> readout`

This preserves the API dependency spine and gives STONEWAKE a runnable discrete physics abstraction without pretending the game engine is a validated cosmological model.
