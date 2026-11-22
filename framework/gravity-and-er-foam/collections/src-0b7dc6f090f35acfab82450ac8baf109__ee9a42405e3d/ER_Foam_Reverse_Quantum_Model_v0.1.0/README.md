# ER-Foam Reverse Quantum Model v0.1.0

This package reverses the uploaded ER-foam chirality substrate into a minimal
quantum-state model.

The reverse is exact for the supplied rest tensor:

```text
ER tensor
    -> remove closure projector
    -> divide chirality filter
    -> divide persistence filter
    -> recovered pre-observation quantum state
```

The recovered state is an equal-amplitude constructive superposition over 192
basis states.

It is a pre-particle substrate state, not an atomic model.

See:

```text
model/ER_FOAM_REVERSE_QUANTUM_MODEL.md
model/ER_FOAM_REVERSE_QUANTUM_MODEL.json
validation/VALIDATION.json
```
