# Milestone 001 — Language-First Architecture

**Decision date:** 2026-08-03  
**Status:** Active architectural direction

## Decision

The Genesis Mainframe will be designed outward from the Genesis programming language.

The language defines:

```text
what counts as state
what counts as a Geometric
what relationships may exist
what transformations are admissible
what must be preserved
what counts as closure
how portals are created
how failure and recovery are expressed
what hardware must physically realize
```

The hardware, operating topology, portal network, and Guardian Intelligence are therefore required to conform to the language.

## First mandatory language feature

The first architecture-defining language construct is:

```text
portal
```

A Genesis implementation is not conformant unless the language can define, validate, open, execute, close, and recover a portal transaction over a Geometric.

## Language-to-machine direction

```text
Genesis ontology
  -> Genesis programming semantics
  -> Geometric object model
  -> admissibility/type system
  -> operator lowering
  -> portal transaction
  -> operating topology
  -> Guardian execution
  -> hardware realization contract
```

## Engineering consequence

The project roadmap must not begin by assuming a CPU, RAM model, instruction set, or conventional operating system.

Those mechanisms may be used during research, but the native architecture is derived from Genesis semantics.
