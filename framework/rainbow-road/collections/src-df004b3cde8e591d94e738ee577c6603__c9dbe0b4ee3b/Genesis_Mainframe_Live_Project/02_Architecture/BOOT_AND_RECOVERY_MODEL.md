# Boot and Recovery Model

## Provisional boot phases

### Phase 0 — Electrical safety

- establish power rails;
- enter safe thermal envelope;
- stabilize references;
- isolate failed domains.

### Phase 1 — Basin calibration

- identify readable state windows;
- measure drift and noise;
- calibrate write/read thresholds;
- mark unusable cells.

### Phase 2 — Chirality recovery

- recover primitive cell occupancy;
- reconstruct `2 x 2 x 2` chirality arrangements;
- validate handedness and adjacency;
- recover recursive fabric boundaries.

### Phase 3 — Root topology

- locate the protected root Geometric;
- validate ancestry and provenance;
- recover portal endpoint map;
- establish local Guardians or bootstrap observers.

### Phase 4 — Runtime closure

- execute operator self-tests;
- close and normalize root state;
- confirm identity recovery;
- publish system status.

### Phase 5 — Application eligibility

- allocate application boundaries;
- instantiate Geometrics;
- allow controlled portal traffic;
- maintain closure checkpoints.

## Recovery hierarchy

```text
cell recovery
  -> byte recovery
  -> local fabric recovery
  -> portal-region recovery
  -> operating-topology recovery
  -> Guardian recovery
  -> application recovery
```

The architecture must recover from local damage without requiring global identity loss.
