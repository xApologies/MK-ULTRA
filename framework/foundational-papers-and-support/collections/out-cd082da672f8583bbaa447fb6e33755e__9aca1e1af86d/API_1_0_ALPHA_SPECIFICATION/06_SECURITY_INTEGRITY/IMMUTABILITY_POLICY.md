# Immutability and Rewrite Policy

## Canonical read path

- Files are opened read-only.
- Parsed canonical structures are converted to immutable mappings, tuples, and frozen records.
- A pre-request fingerprint is retained.
- A post-request fingerprint must match.

## Derived rewrite path

Allowed:
- local normalization of a query;
- local ranking or filtering;
- construction of request-specific paths;
- condensation into a derived graph;
- caching inside a disposable request context.

Forbidden:
- changing a canonical handle;
- replacing canonical equations;
- deleting duplicate provenance records;
- promoting inferred paths to canonical edges;
- changing confidence or audit status;
- writing into the preserved 4.3 directory.
