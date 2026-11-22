# System Overview

## Three-plane architecture

```text
┌──────────────────────── AUTHORING / CLINICAL PLANE ────────────────────────┐
│ user / caregiver / clinician / support staff                              │
│                     ↓                                                     │
│             external authoring AI                                         │
│                     ↓                                                     │
│          candidate profile package                                        │
└─────────────────────┬──────────────────────────────────────────────────────┘
                      ↓
┌──────────────────────── BRANE COMPOSITION PLANE ──────────────────────────┐
│                 ┌─────────┬─────────┬─────────┐                            │
│                 │  AI^5   │ API^5   │ LIB^5   │                           │
│                 │         │         │         │                            │
│                 │ intent  │SPO_API^5│ content │                            │
│                 │collapse │canonical│history  │                            │
│                 └────┬────┴────┬────┴────┬────┘                            │
│                      └───────── BRANE ─────┘                               │
│                                ↓                                          │
│                         private QMO^6(q)                                  │
│                                ↓ π_SPO                                    │
│                      independent SPO_instance                             │
│                                ↓ compile                                  │
│                       signed DevicePolicy                                 │
└─────────────────────┬──────────────────────────────────────────────────────┘
                      ↓
┌──────────────────────── REALTIME DEVICE PLANE ────────────────────────────┐
│ microphones → event front-end → policy lookup → Vera gate → DSP → output  │
│                                         ↑                                 │
│                            direct user override                           │
└────────────────────────────────────────────────────────────────────────────┘
```

## Architectural objective

The system does not maximize silence. It attempts to preserve the information needed for environmental awareness and agency while permitting bounded transformations of representations that a validated profile marks as disruptive.

## Core boundary

```text
classification ≠ profile authority ≠ safety authority ≠ DSP
```

A classifier reports an event hypothesis. The independent SPO supplies the user's allowed policy. Vera's gate enforces non-negotiable safety invariants. DSP realizes the already-approved transformation.
