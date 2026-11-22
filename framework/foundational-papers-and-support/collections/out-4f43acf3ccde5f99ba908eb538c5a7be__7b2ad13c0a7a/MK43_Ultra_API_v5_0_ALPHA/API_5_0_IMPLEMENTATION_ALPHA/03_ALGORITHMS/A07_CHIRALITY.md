# A07 — Chirality Resolution

Chirality is a request-relative orientation state derived from canonical evidence. API 5.0 does not invent missing chirality.

```text
INPUT: node, intent, provenance
OUTPUT: RIGHT | LEFT | BALANCED | WHITE | BLACK | UNRESOLVED

1. Gather explicit chirality fields from the canonical object.
2. Gather relation-orientation evidence from the incoming path.
3. Gather basin or orientation metadata referenced by provenance.
4. Apply canonical precedence:
   explicit object declaration
   > explicit edge orientation
   > canonical dependency-path orientation
   > request-local derived orientation.
5. Detect contradictory equal-precedence evidence.
6. If contradiction exists, return UNRESOLVED with diagnostic.
7. If no evidence exists, return UNRESOLVED.
8. Otherwise return the highest-precedence stable state.
9. Cache only inside the request context.
```
