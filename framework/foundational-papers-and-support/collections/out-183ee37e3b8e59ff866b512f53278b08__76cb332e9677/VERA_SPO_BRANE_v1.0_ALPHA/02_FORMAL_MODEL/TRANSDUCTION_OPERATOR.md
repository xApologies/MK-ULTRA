# Transduction Operator

Candidate high-level operations:

```text
Ω = { PRESERVE, ATTENUATE, TRANSFORM, EMPHASIZE }
```

A policy decision is:

```text
T(E, SPO_instance, Context, DeviceCaps) → Decision
```

subject to Vera's safety gate.

## Semantic preservation

The system's objective is not waveform identity. Where a transform is allowed, the output may change carrier representation while preserving required information.

Candidate required information fields include:
- urgency;
- source direction/localization;
- speech content where protected;
- event occurrence;
- user-selected environmental cues.

The exact preservation metric is an open research question and must be validated for the intended use case.
