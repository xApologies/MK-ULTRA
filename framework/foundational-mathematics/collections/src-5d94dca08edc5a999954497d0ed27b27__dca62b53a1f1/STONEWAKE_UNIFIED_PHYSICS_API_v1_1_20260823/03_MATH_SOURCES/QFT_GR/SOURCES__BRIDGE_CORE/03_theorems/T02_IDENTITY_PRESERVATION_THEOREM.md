# T02 — Atomic Identity Preservation Under Relational Traversal

## Assumptions

```text
R-domain chirality access is read-only
ancestry deletion is forbidden
component atomic arrays remain immutable
corridor topology is stored separately.
```

## Statement

Under these guards, `U_R` preserves every component atomic chirality
identity while allowing a new molecular relation identity to emerge.

## Proof

`U_R` may read component chirality and write relational corridor,
occupancy, survivability, and ancestry data. It may not replace the
component chirality fields or delete their ancestry. Therefore each atomic
carrier remains recoverable as a component of the output. The molecular
identity is represented by the new persistent relation graph.

QED.

## Status

Formal theorem under the supplied domain guards.
