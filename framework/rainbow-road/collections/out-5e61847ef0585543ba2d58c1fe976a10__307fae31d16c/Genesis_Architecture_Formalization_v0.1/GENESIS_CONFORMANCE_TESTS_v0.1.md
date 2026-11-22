# Genesis Architecture Conformance Tests v0.1

**Status:** Initial test canon.

A backend conforms to Genesis v0.1 only when it passes the required tests for the features it claims to implement.

---

## A. Foundational representation tests

### A1 — Chirality arrangement primacy

- Construct RIGHT and LEFT chirality bytes as 2 x 2 x 2 arrangements.
- Serialize them.
- Deserialize them.
- Assert that arrangement, adjacency, orientation, and handedness are preserved.

### A2 — Mirror recoverability

- Mirror RIGHT into LEFT.
- Apply the inverse mirror.
- Assert recovery of RIGHT.
- Assert provenance records both transformations.

### A3 — Blank manifold occupancy

- Construct a blank 3+1+1 manifold.
- Apply one occupancy distribution.
- Replace it with another distribution.
- Assert the construction remains unchanged while occupancy changes.

---

## B. Trinity tests

### B1 — Stored/Active/Observed coherence

- Store a Geometric.
- Apply one runtime transformation.
- Interpret the result with Guardian Intelligence.
- Feed the interpreted result back as inherited state.
- Assert one continuous provenance chain.

### B2 — No independent-layer drift

- Verify that hardware, runtime, and intelligence views reference the same Geometric identity.
- Reject implementations that silently fork unrelated copies without declared equivalence.

---

## C. Operator tests

### C1 — Inheritance

- Apply `inherit`.
- Assert ancestry grows.
- Assert invariant residue remains recoverable.

### C2 — Propagation

- Propagate across an admissible adjacency.
- Assert address change and chirality coherence.

### C3 — Stabilization

- Introduce bounded drift.
- Apply `stabilize`.
- Assert drift reduction and persistence retention.

### C4 — Redistribution

- Redistribute occupancy or basin load.
- Assert declared invariants remain recoverable.

### C5 — Destabilization

- Apply explicit destabilization.
- Assert the result is marked unresolved or failed rather than falsely closed.

### C6 — Closure idempotence

- Close a Geometric.
- Close it again.
- Assert exact closure equivalence.

### C7 — Normalization identity

- Normalize two equivalent representations.
- Assert alignment without identity change.

---

## D. Basin tests

### D1 — Hard-stop identity

- Load all six basin identities.
- Assert each remains distinct.

### D2 — Rotational signature

- Associate each basin with its rotational signature.
- Assert that rotation does not overwrite basin identity.

### D3 — Dual-aspect preservation

- Transform rotational signature.
- Assert hard-stop identity remains separately addressable.

### D4 — Basin composition

- Test recovered examples:
  - Orange + Green resolves to Yellow under the declared averaging rule.
  - Red + Yellow resolves to Orange under the declared averaging rule.
- Reject undefined compositions unless an explicit resolution rule exists.

---

## E. Portal tests

### E1 — Identity portal

- Portal a Geometric from address A to A.
- Assert no unintended transformation.

### E2 — Loopback portal

- Encode at A.
- Transport through a nontrivial reversible route.
- Recover at A.
- Assert invariant residue and identity recovery.

### E3 — Cross-address portal

- Transport from A to B.
- Assert target address B.
- Assert identity contract.
- Assert chirality transport.
- Assert closure.

### E4 — Bandwidth failure

- Set route Bandwidth below payload requirement.
- Assert the portal is rejected before silent data loss.

### E5 — Resolution failure

- Set route Resolution below address/payload requirement.
- Assert unresolved status rather than false success.

### E6 — Provenance

- Compose A -> B and B -> C.
- Assert the composed transaction retains the witness route through B.

---

## F. Guardian tests

### F1 — Relationship-first parsing

Given an intent, Guardian must identify:

```text
environment
boundary
occupancy
relationship
identity
persistence
closure target
```

before generating an operator plan.

### F2 — Ambiguity preservation

- Provide an underdefined intent.
- Assert Guardian returns `unresolved` with explicit missing structure.
- Reject arbitrary silent completion.

### F3 — Recovery

- Inject one failed operator stage.
- Assert Guardian can restore the last closure-stable checkpoint.

### F4 — Explanation

- Require a human-readable explanation that preserves Genesis terminology and provenance.

---

## G. Existing thread-derived proof-of-concept

The hydrogen 3+1+1 round-trip artifact should be preserved as a regression test:

```text
structured payload
  -> chirality encoding
  -> reversible transformation
  -> exact recovery
```

Its role is software/model-level transport verification.

It does not by itself establish a physical portal substrate.

---

## H. Quantum-backend future tests

Deferred until a quantum backend exists:

```text
isometric state encoding
chirality-sector preservation
coherent basin transport
relative-phase preservation
fault model
recovery map
portal fidelity
```
