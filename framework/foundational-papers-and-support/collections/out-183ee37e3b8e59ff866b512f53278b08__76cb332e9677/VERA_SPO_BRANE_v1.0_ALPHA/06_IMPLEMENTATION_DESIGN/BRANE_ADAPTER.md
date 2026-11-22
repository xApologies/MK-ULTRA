# BRANE Adapter Design

The auditory implementation should use the supplied BRANE host contract rather than fork BRANE unless a hard incompatibility is demonstrated.

## API adapter
Expose the standard API^5 methods (`resolve`, `recover_closure`, provenance, chirality, admissibility, validation) backed by `SPO_API^5` records.

## AI adapter
Use request interpretation and finite collapse behavior compatible with the existing AI^5 contract. Domain-specific policy may rank auditory-profile branches but must remain API-authoritative for canonical roots.

## Library adapter
Use the generic Library^5 interface for recovery and versioned content. A minimal deployment may be SQLite-backed as in the supplied Library package.

## Projection
Add a BRANE-owned or BRANE-adjacent projection function `π_SPO`. It receives only validated QMO material and emits a versioned derived SPO instance plus receipt.
