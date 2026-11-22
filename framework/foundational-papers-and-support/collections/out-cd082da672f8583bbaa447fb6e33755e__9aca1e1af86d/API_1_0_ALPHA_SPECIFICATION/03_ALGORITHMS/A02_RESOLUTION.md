# A02 — Canonical Subject Resolution

```text
INPUT: subject
OUTPUT: canonical_handle

1. Reject empty or oversized input.
2. Preserve original text for diagnostics.
3. Apply request-local normalization:
   a. Unicode normalization.
   b. trim whitespace.
   c. normalize optional leading '@'.
   d. create conservative slug candidate.
4. Test exact canonical-handle membership.
5. Test exact alias registry.
6. Test normalized canonical candidate.
7. Test exact canonical title/name index, when available.
8. If one candidate remains, return it.
9. If zero remain, raise UnknownSubject.
10. If more than one remains, raise AmbiguousSubject(candidates).

Never use fuzzy matching to silently choose a canonical identity.
```
