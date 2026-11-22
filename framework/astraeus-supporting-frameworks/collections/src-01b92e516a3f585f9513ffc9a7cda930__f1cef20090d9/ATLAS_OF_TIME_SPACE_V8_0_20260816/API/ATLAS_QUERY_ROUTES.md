# Atlas Query Routes

These are conceptual recovery routes for the API layer.

## Query: local QFT/GR bridge

```text
@chirality
 -> local chirality restriction
 -> @qft realization
 -> @stress_energy

@chirality
 -> @er_foam
 -> @helicon
 -> @gravitational_helicon_mode
 -> @graviton
 -> @time_shell_projection_operator
 -> @projected_spacetime_metric
 -> @gravity
```

The Atlas adds the requirement that both routes be scoped to the same localized `S2` projection address.

## Query: corridor

```text
source S2 address
 -> Time-Shell lift
 -> S3 continuity path gamma
 -> chirality transport P_gamma^chi
 -> target Time-Shell projection
 -> target S2 address
```

## Query: image label

Each image label should resolve to a formal object/status through `CARTOGRAPHY/PLATE_I_SEMANTICS.md`.

## v5 Direction-Sphere routes

```text
@time_space
 -> candidate @unit_tangent_bundle_S3
 -> @S2_local_projection

@helicon
 -> @S3_helicon_connection
 -> @helicon_curvature
 -> @directional_S2_readout
 -> @transient_ER_ensemble
 -> @dark_geometric_load
```

These are Atlas live-model routes. Handles not present in the canonical API are local Atlas candidate addresses and must not be misreported as recovered API-native handles.
