# API Query Report — `@chirality`

## Query intent

Recover direct and high-confidence dependencies needed to build the common chirality landscape down into quantum and gravitational realizations.

## Direct recovered edges used in LM-001

From the supplied API dependency index:

```text
@chirality DEPENDS_TO @er_foam
@chirality CONTRIBUTES_TO @helicon_orientation
@chirality VERTICAL_CHAIN @orientation
@chirality VERTICAL_CHAIN @persistence
@chirality VERTICAL_CHAIN @time_shell

@er_foam DEPENDS_TO @helicon
@er_foam DEPENDS_TO @stable_er_foam_knot
@er_foam DEPENDS_TO @time_shell
```

The index also contains derived/composed reachability from chirality into Helicon, gravitational Helicon mode, Graviton, Time Shell, configuration-space/readable-spacetime objects and gravity. LM-001 keeps direct versus composed relations separate in `chirality_bridge_subgraph.json`.

## Relevant recovered gravity chain

```text
@chirality
-> @er_foam
-> @helicon
-> @gravitational_helicon_mode
-> @graviton
-> @continuity_perturbation
-> @time_shell_projection_operator
-> @weak_field_metric_perturbation
-> @projected_spacetime_metric
```

The exact relation type is not assumed uniform across every arrow; inspect the JSON ledger.

## QFT integration

The QFT side is assembled from the canonical Q handoff and the historical Helicon/quantum-wave source equations. The current API dependency index does not expose one single direct `@chirality -> @Q` theorem. The live model therefore uses the typed representation map `rho_Q` as a formal integration target rather than fabricating a direct edge.

## Query discipline

- direct edges are stored as `API_DIRECT`;
- composed reachability is stored as `API_COMPOSED`;
- newly proposed edges are stored separately and are not written back into the source API.
