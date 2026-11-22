# Portal Interconnect Architecture

## Definition

A Portal is a chirality-admissible transaction that transfers a Geometric between relational addresses while preserving a declared identity and closure contract.

```text
Corridor = route
Portal   = transaction over route
```

## Transaction contract

```text
PortalRequest {
  source_address
  target_address
  geometric_identity
  occupancy
  chirality
  basin_distribution
  persistence_contract
  invariant_residue
  ancestry
  provenance
  resolution_required
  bandwidth_required
  closure_target
}
```

## Successful transaction

A portal succeeds only when:

```text
target address resolves
chirality transport is admissible
required residue is preserved
identity remains recoverable
persistence contract holds
route Resolution is sufficient
route Bandwidth is sufficient
destination closes
provenance is complete
```

## Portal layers

### Semantic layer

Defines what must be preserved.

### Routing layer

Chooses an admissible corridor.

### Fabric layer

Moves or re-realizes the organized state.

### Guardian layer

Validates, observes, and recovers the transaction.

### Physical layer

Future hardware mechanism.

## Current evidence

The hydrogen round-trip supports a reversible computational transport layer.

It establishes the architecture of:

```text
encode
transform
recover
verify
```

It does not yet establish a physical interconnect device.
