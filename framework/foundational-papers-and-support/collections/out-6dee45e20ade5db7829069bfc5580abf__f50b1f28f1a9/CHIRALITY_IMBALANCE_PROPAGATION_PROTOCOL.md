# Chirality Imbalance Propagation Protocol

## Purpose

This protocol tests how chirality imbalance propagates through the locked Pipeline 2 architecture.

Chirality remains read-only.

The pipeline may respond to chirality readout, but no domain may write chirality directly.

## Test Placement

Chirality imbalance readout stress may be applied at:

- R3: awareness response
- R4: corridor candidate formation
- R5: ordered topology resolution
- R6: survivability stabilization
- R7: oscillatory persistence

## Expected Behavior

The pipeline should reveal whether chirality imbalance:

- damps locally,
- migrates through corridor candidates,
- locks into a selected corridor,
- destabilizes an overoccupied topology,
- creates recoverability strain,
- propagates into oscillatory instability,
- or remains inert.

## Required Metrics

- chirality imbalance amplitude
- chirality imbalance locality
- corridor response delta
- bandwidth occupancy delta
- recoverability score delta
- ancestry score delta
- R7 persistence delta
- failure domain if any

## Prohibited Behavior

No test may:
- write chirality,
- force a chirality state,
- hardcode a topology outcome,
- introduce a new domain.

## Closure Condition

Pipeline 2 passes chirality imbalance testing when imbalance propagation is explainable, bounded, and ancestry-preserving unless the test intentionally exceeds the failure threshold.
