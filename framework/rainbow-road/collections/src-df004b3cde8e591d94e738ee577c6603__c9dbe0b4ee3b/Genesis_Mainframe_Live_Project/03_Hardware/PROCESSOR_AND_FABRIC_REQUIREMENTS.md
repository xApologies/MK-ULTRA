# Processor and Fabric Requirements

## Fabric model

The processor is expected to be distributed through or closely coupled to the chirality fabric rather than organized solely around a central fetch/decode/execute CPU.

## Native transformations

The hardware or microarchitecture must eventually realize:

```text
inherit
propagate
stabilize
redistribute
destabilize
close
normalize
```

For each operation, engineering must define:

```text
input state class
admissibility precondition
local cell transition
neighbor transition
basin effect
chirality effect
identity invariant
persistence invariant
energy cost
latency
parallel behavior
failure state
recovery path
```

## Addressing

Genesis addresses are expected to be relational and typed.

Working form:

```text
Address = (
  environment,
  boundary,
  locality,
  chirality class,
  identity class,
  persistence state,
  recursive depth,
  provenance
)
```

Numeric physical addresses may exist beneath this, but they are not the full semantic address.

## Capacity

Two architecture-level capacity concepts are required:

```text
Resolution = ability to distinguish organization
Bandwidth  = available organizational freedom/capacity
```

The fabric must expose measurable or computable proxies for both.
