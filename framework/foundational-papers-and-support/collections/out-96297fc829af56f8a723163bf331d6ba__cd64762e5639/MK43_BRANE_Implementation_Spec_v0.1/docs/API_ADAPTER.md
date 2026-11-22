# API Adapter Specification

## Objective

Allow BRANE to load historical or future API packages without embedding assumptions about one release.

## Adapter duties

- inspect package manifest;
- verify checksums;
- locate canonical handle and edge registries;
- expose normalized handle resolution;
- expose typed-neighbor queries;
- expose recursive recovery;
- normalize aliases and provenance;
- return graph objects without rewriting mathematics.

## Adapter restrictions

The adapter may normalize file formats and field names. It may not infer missing canonical edges, repair mathematical definitions, or silently remove malformed records. Such conditions become validation errors or explicit unresolved records.

## Reverse reconstruction mode

For older API packages, a reconstruction adapter may derive a normalized index from canonical source files. The derived index must retain provenance to original line, section, or registry location and must be marked as reconstructed rather than native.

## Capability declaration

Each loaded API must report at least:

- API identifier and version;
- canonical root or domain set;
- handle count;
- edge relation vocabulary;
- alias support;
- provenance support;
- upstream/downstream recovery support;
- QMO schema compatibility.
