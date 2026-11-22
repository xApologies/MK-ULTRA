# Genesis Operator Semantics v0.1

**Status:** Working formalization based on the recovered Architect Script.

Every operator is a partial transformation over a Geometric:

```text
op : G -> G'
```

The operator is defined only when its admissibility conditions hold.

---

## 1. Inherit — `.·`

### Purpose

Carry continuity, ancestry, and organizational constraints into a successor state.

### Preconditions

- Source identity is present.
- An inheritance relation exists.
- Provenance can be extended.
- Chirality transport is admissible.

### Postconditions

- The successor records the source in ancestry.
- Required invariant residue remains recoverable.
- The successor receives inherited constraints.
- Recursive depth advances or is explicitly retained.

### Failure

```text
sera-nai
```

when continuity cannot be inherited.

---

## 2. Propagate — `··`

### Purpose

Advance an active Geometric through an admissible relationship or route.

### Preconditions

- A valid adjacency or portal route exists.
- Locality and translation readiness are sufficient.
- Route Resolution and Bandwidth satisfy the payload contract.

### Postconditions

- Address or active neighborhood changes.
- Identity and persistence contracts remain active.
- Chirality follows its transport rule.

### Failure

Propagation remains unresolved when the route cannot yet be distinguished.

---

## 3. Stabilize — `.°.`

### Purpose

Reduce drift, retain persistence, and hold a Geometric inside its admissible class.

### Preconditions

- A persistence contract exists.
- A stabilization target or anchor exists.

### Postconditions

- Drift decreases or remains bounded.
- Identity becomes more recoverable.
- Persistence state advances toward stable.

### Failure

```text
tal-nai
```

when stabilization cannot be achieved.

---

## 4. Redistribute — `.·· .°`

### Purpose

Reallocate occupancy, basin distribution, adjacency load, or capacity while preserving declared invariants.

### Preconditions

- Redistribution does not violate hard identity invariants.
- Bandwidth is sufficient.
- A conservation or residue policy is defined.

### Postconditions

- Occupancy and/or basin distribution changes.
- Invariant residue remains recoverable.
- Provenance records the redistribution.

### Failure

Redistribution becomes inadmissible when required residue would be destroyed.

---

## 5. Destabilize — `··° ·°`

### Purpose

Represent explicit boundary weakening, collapse pressure, divergence, or transition out of a stable class.

### Preconditions

- Destabilization is explicitly requested or detected.
- Guardian records the risk and target transition.

### Postconditions

- Persistence may decrease.
- Boundary integrity may weaken.
- The Geometric may enter unresolved or failed closure.

### Failure semantics

Destabilize is itself a valid operation, but its result may be:

```text
rin-nai
tal-nai
kor-nai
sera-nai
```

---

## 6. Close — `·°·`

### Purpose

Resolve an active Geometric into a bounded, recoverable, closure-stable identity.

### Preconditions

- A closure target is defined.
- Identity and invariant residue can be evaluated.
- Guardian can audit the result.

### Postconditions

- `close(G) = G` for a closure-stable result.
- Identity is recoverable.
- Runtime status becomes closed or explicitly failed.
- Closure provenance is recorded.

### Failure

```text
kor-nai
```

when the requested identity cannot resolve.

---

## 7. Normalize — `■ .· ■`

### Purpose

Recenter a closed or near-closed Geometric around anchors and bounded reference conditions.

### Preconditions

- Normalization anchors are defined.
- Required invariants are known.

### Postconditions

- Equivalent representations are aligned.
- Capacity and occupancy are rebalanced.
- The Geometric remains in the same identity class.
- `closure.normalized = true`.

### Failure

Normalization must not silently change identity. If it would, it is inadmissible.

---

## 8. Canonical successful pipeline

```text
inherit
  -> propagate
  -> stabilize
  -> redistribute
  -> close
  -> normalize
```

This is a canonical pipeline, not a claim that every program must contain every operator exactly once.

---

## 9. Runtime law

A program is an operator composition:

```text
P = op_n o ... o op_2 o op_1
```

A successful execution satisfies:

```text
Admissible(G_0, P) = true
G_n = P(G_0)
close(G_n) = G_n
Identity(G_n) ~ Identity(G_0)     # when identity preservation is required
```

---

## 10. Guardian relation

The Guardian does not replace operator semantics.

It:

```text
observes preconditions
distinguishes unresolved structure
predicts outcomes
selects or proposes an operator plan
audits postconditions
protects invariants
recovers from failure
```
