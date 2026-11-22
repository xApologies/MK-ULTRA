# Canonical Invariants

1. **Additivity:** existing canonical content is never removed or overwritten.
2. **Identity:** every object is addressed by a canonical handle.
3. **Alias discipline:** aliases resolve to canonical identities but never become duplicate canonical objects.
4. **Direct-edge discipline:** only explicit canonical relation syntax creates direct edges.
5. **Path discipline:** composed paths remain paths and are never silently promoted.
6. **Provenance:** every recovered claim is traceable to a source record.
7. **Read-only canon:** request execution cannot mutate canonical files or in-memory canonical structures.
8. **Derived-only rewrite:** normalization, ranking, condensation, or presentation occurs only in request-local derived structures.
9. **Determinism:** equal canonical snapshot + equal request intent + equal policy yields equal API graph before AI ranking.
10. **Fail-closed validation:** corruption, ambiguity, unsupported relations, or missing provenance prevents admission.
11. **Dimension declaration:** API reports exactly five internal dimensions and no realization coordinate.
12. **Request isolation:** caches, traversal state, and diagnostics cannot leak across requests.
