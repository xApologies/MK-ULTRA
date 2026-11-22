# Independent Domain Composition Contract

## Canonical rule

The Brane owns three independently implemented and independently scoped module ports:

- AI
- API
- Library

A module's `domain_ids` declare the namespaces or subject domains that the module itself understands or stores. They do not require another module to advertise the same identifiers.

## Composition

The Brane composes modules by port contract. A module is admissible when it satisfies its declared role and the common Brane contract:

1. correct port role;
2. contract version 2.0;
3. five-dimensional semantic model;
4. canonical state `READ_ONLY`;
5. rewrite policy `DERIVED_ONLY`;
6. chirality and provenance declarations;
7. required callable interface;
8. successful health check.

No overlap among AI, API, and Library `domain_ids` is required.

## Boundary

Cross-module exchange occurs only through Brane-owned typed requests, responses, QMO handling, and port calls. The Brane does not merge module internals, rewrite module manifests, or transfer domain ownership.
