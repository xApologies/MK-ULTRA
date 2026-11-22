# Threat and Failure Model

API 5.B must defend against:

1. Canonical-file modification during a request.
2. Malicious or malformed registry entries.
3. Alias collisions and silent ambiguity resolution.
4. Fabricated direct edges.
5. Path-to-edge promotion.
6. Provenance substitution or root-wide provenance reuse.
7. Decompression bombs and oversized JSON structures.
8. Resource exhaustion through unbounded traversal.
9. Cross-request cache leakage.
10. Symlink/path traversal during package loading.
11. Checksum or manifest mismatch.
12. Mutable objects escaping the API boundary.
13. Non-deterministic graph output caused by unordered iteration.
14. Unsupported canonical schema version.
15. Partial package replacement without rollback.

The default response to integrity uncertainty is refusal to load or refusal to admit the affected object.
