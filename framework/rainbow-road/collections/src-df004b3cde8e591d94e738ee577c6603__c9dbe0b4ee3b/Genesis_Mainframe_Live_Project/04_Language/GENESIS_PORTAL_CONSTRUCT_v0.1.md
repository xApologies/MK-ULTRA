# STATUS NOTICE — PROVISIONAL SKETCH

This file predates the language-discovery reset. It is retained for provenance only. It is **not** current Genesis canon and must not be treated as a finalized syntax or language design.

# Genesis Portal Construct v0.1

## Canonical classification

```text
Portal = native Genesis bus transaction
Corridor = admissible route used by the transaction
```

## Semantic form

```text
Portal(
    SourceBoundary,
    TargetBoundary,
    PayloadGeometric,
    RoutePolicy,
    PreservationContract,
    CapacityContract,
    ClosureContract,
    RecoveryContract
)
```

## Required fields

| Field | Meaning |
|---|---|
| `from` | Source boundary/address |
| `to` | Target boundary/address |
| `carry` | Payload Geometric |
| `route` | Explicit or Guardian-discovered corridor |
| `preserve` | Identity invariants |
| `require` | Resolution and Bandwidth constraints |
| `on_open` | Pre-transfer inheritance/checkpoint operations |
| `on_transfer` | Propagation/stabilization operations |
| `on_arrival` | Closure and normalization operations |
| `on_failure` | Quarantine and recovery behavior |

## Minimal legal portal

```genesis
portal P {
    from: A
    to: B
    carry: G
    preserve: [identity]
    close: at_target
}
```

## Illegal portal examples

### No payload identity

```genesis
portal Invalid {
    from: A
    to: B
    carry: unresolved
}
```

Reason:

```text
en-nai
```

### Insufficient capacity

```genesis
portal Invalid {
    from: A
    to: B
    carry: G
    require: bandwidth < G.required_bandwidth
}
```

Reason:

```text
inadmissible capacity contract
```

### No closure condition

```genesis
portal Invalid {
    from: A
    to: B
    carry: G
}
```

Reason:

```text
transport may terminate without identity recovery
```

## Compiler obligations

The compiler/Guardian must not silently invent:

```text
target identity
required invariant residue
missing closure target
missing route capacity
```

It may infer only what is derivable from declared Geometric metadata and active architecture canon.

## Portal composition

Two portals may compose:

```genesis
portal P1 { from: A to: B carry: G ... }
portal P2 { from: B to: C carry: G ... }

compose P1 then P2 as A_to_C
```

Composition must preserve the witness route through `B`.

Provenance cannot collapse the composed route into a false direct transfer.

## Portal lifecycle

```text
declared
  -> validated
  -> capacity_reserved
  -> opened
  -> transferring
  -> arrived
  -> closed
  -> normalized
  -> inherited
```

Failure may occur at any phase and must resolve into:

```text
retry
reroute
recover
quarantine
abort_to_checkpoint
```
