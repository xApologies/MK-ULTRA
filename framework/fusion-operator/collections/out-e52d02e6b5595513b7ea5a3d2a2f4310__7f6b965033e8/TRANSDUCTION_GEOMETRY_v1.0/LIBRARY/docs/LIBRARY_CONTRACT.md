# Library Contract

## Address contract

An address package contains:

```text
handle
aliases
object_type
canonical_math
content_blocks
relations
provenance
metadata
status
language
```

## Root QMO address

`@global_transduction_object` is the root mathematical address for the live QMO.

The metadata under this address includes:

```text
QMO schema
object registry
typed edge registry
equation/operator registry
ledger registry
alias registry
component-salvage registry
runtime state
release manifest
validation state
query contract
```

## Recovery

Recovery is exhaustive relative to the active package at an address. Summarization is downstream presentation, not storage.

## Safety

- append-only by default;
- provenance required;
- candidate status preserved;
- missing content is returned as unresolved;
- no domain knowledge is invented by the Library.
