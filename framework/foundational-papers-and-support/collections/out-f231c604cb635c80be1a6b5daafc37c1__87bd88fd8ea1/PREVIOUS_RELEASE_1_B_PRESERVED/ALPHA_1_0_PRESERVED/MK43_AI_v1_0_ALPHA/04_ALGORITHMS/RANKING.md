# Stable Branch Ranking

Each candidate receives a score from declared factors only:

```text
score = relevance
      + dependency centrality
      + request alignment
      + explanatory continuity
      + provenance quality
      + admissibility confidence
      - redundancy
      - cycle risk
      - budget cost
```

Weights are policy data. Ties are resolved by canonical stable key, never nondeterministic collection order. Every candidate remains present in the returned ranking record.
