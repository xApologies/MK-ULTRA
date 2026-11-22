# Physical Substrate Requirements

## Requirement class

This document defines what the hardware must achieve. It does not yet choose a material.

## Six-state persistent device requirement

A candidate device must reliably support six structurally distinguishable states associated with the six basin identities.

Required characterization:

```text
state separability
write energy
read energy
latency
retention
endurance
noise margin
temperature response
process variation
cross-talk
refresh requirement
failure signature
manufacturability
```

## Open implementation forms

Potential device families may include, but are not selected as canon:

```text
multi-level charge storage
resistive memory
phase-change memory
ferroelectric devices
magnetic/multiferroic devices
coupled-cell basin emergence
new materials
```

The six basin states may be:

1. six states in one device; or
2. an emergent distribution across several lower-level devices.

Both remain open.

## Chirality requirement

A single multi-state cell is insufficient.

The hardware must support spatial or relational arrangement so that chirality is a property of organized occupancy.

The first candidate tile is:

```text
2 x 2 x 2 cell arrangement
```

The design must preserve:

```text
orientation
adjacency
layer relation
mirror state
local identity
readable provenance or error state
```

## Persistent-store role

The storage device defines the initial chirality configuration space available to the operating topology.

The system cannot treat chirality solely as software metadata if the goal is a native Genesis architecture.
