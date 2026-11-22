# Failure and Fallback

Failures return structured error receipts rather than fabricated completions.

Fallback order:

1. retry deterministic operation within remaining budget;
2. reduce traversal breadth while preserving continuation accounting;
3. return partial realization explicitly marked incomplete;
4. return ambiguity or invalid-root result;
5. abort and preserve canonical state.

A learned strategy failure must fall back to the deterministic baseline.
