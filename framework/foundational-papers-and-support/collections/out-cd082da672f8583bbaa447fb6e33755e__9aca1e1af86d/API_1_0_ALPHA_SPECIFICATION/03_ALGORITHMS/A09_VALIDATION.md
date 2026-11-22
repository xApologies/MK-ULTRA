# A09 — Graph Validation

```text
1. Verify root identity.
2. Verify all node handles exist canonically.
3. Verify every direct graph edge matches a canonical edge record.
4. Verify no composed path was stored as a direct edge.
5. Verify node depth equals path length minus one.
6. Verify all paths begin at root and are contiguous.
7. Verify each node has object-specific provenance.
8. Verify equations are exact registry/source recoveries.
9. Verify chirality states belong to the declared domain.
10. Verify all budget counters are within limits.
11. Verify canonical fingerprint equals pre-request fingerprint.
12. Verify graph structures are immutable before return.
13. Raise structured validation failure on first invariant breach,
    while retaining a complete diagnostic list internally.
```
