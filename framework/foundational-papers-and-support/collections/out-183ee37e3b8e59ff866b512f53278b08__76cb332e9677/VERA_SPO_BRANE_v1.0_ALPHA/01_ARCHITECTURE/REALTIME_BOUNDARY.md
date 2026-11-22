# Realtime Boundary

BRANE is the construction and validation architecture. It is not required to process every PCM frame.

The realtime path consumes precompiled bounded policy data and a low-latency event-state front end.

```text
OFFLINE / ASYNCHRONOUS                     REALTIME
----------------------                     --------
authoring AI                               microphone input
BRANE composition                           event features
QMO recovery                                event hypothesis
SPO projection                              deterministic policy lookup
policy compilation                          Vera gate
signature / provenance                      DSP transform
```

This separation reduces latency, simplifies failure behavior, and prevents unconstrained generative decisions from entering the earbud audio loop.
