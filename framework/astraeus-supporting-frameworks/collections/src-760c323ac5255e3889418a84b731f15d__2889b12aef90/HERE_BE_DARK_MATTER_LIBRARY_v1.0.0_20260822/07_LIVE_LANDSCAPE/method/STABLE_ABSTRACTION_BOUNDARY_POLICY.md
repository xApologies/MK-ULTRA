# Stable Abstraction Boundary Policy — Live Landscape

## Purpose

The Live Landscape supports two valid construction modes.

### Foundation mode
Descend through dependency ancestry when the theorem currently being tested actually needs the missing property, a contradiction appears, or a branch has become important enough to justify formal backfill.

### Exploration mode
When an object has a coherent typed interface and is locally consistent with the registered API, it may be admitted provisionally as a **Working Assumption / Working Primitive** and used to explore downstream consequences.

A working assumption is not a promotion. It must carry:

- an explicit type and scope;
- the exact properties being assumed;
- provenance and parent handles;
- a Proof-Debt record;
- all downstream results tagged as conditional on it.

The working rule is:

```text
Foundation when necessary.
Abstraction when sufficient.
Backfill after discovery.
```

This is analogous to ordinary mathematical practice such as “let M be a manifold,” while preserving the deeper PRIME/dependency lineage as separately auditable provenance.

## Promotion rule

No result depending on unresolved working assumptions may be promoted to baseline canon or physical claim solely because the conditional derivation closes.
