# STATUS NOTICE — PROVISIONAL SKETCH

This file predates the language-discovery reset. It is retained for provenance only. It is **not** current Genesis canon and must not be treated as a finalized syntax or language design.

# Genesis Programming Language Specification v0.1

**Status:** First working language architecture  
**Architecture role:** Native language of the Genesis Mainframe  
**Primary executable object:** Geometric  
**First mandatory system primitive:** Portal

---

## 1. Language identity

Genesis is an architecture-native programming language.

It is not:

```text
a colored version of an existing language
a JVM language
a conventional machine language
a scripting layer over an ordinary operating system
```

It is the grammar through which the Genesis Mainframe defines, instantiates, transforms, transports, observes, and recovers organized state.

---

## 2. Semantic construction order

Every executable Genesis statement is resolved through:

```text
Environment
  -> Boundary
  -> Occupancy
  -> Relationship
  -> Identity
  -> Persistence
  -> Resolution
```

The language is relationship-first.

An identity cannot be considered executable until its boundary, occupancy, and relationships are sufficiently resolved.

---

## 3. Core language objects

### 3.1 Geometric

A Geometric is the primitive operational object.

```genesis
geometric Name {
    environment: ...
    boundary: ...
    occupancy: ...
    relationships: ...
    chirality: ...
    basin: ...
    identity: ...
    persistence: ...
    closure: ...
}
```

### 3.2 Boundary

A Boundary defines distinction, containment, locality, and addressability.

```genesis
boundary A {
    environment: root
    locality: local
}
```

### 3.3 Relationship

A Relationship connects boundaries or Geometrics under explicit admissibility conditions.

```genesis
relationship A_to_B {
    from: A
    to: B
    admissibility: chirality
}
```

### 3.4 Identity

Identity defines what must remain recoverable through transformation.

```genesis
identity PayloadIdentity {
    preserve: [structure, chirality, ancestry]
}
```

### 3.5 Persistence

Persistence defines continuity requirements.

```genesis
persistence Stable {
    checkpoint: closure
    recoverable: true
}
```

### 3.6 Basin expression

The six structural basins are first-class expressions:

```genesis
red
orange
yellow
green
blue
violet
```

They are not RGB values.

A basin may be applied as an expression:

```genesis
express red in Payload
```

### 3.7 Chirality

Chirality is an admissibility and organizational type.

Working forms:

```genesis
chirality right
chirality left
chirality inherited
chirality constrained(...)
```

---

## 4. Core verbs

The first canonical transformation verbs are:

```text
inherit
propagate
stabilize
redistribute
destabilize
close
normalize
```

Working syntax:

```genesis
inherit Payload from Parent
propagate Payload through Route
stabilize Payload
redistribute Payload within Region
destabilize Payload under Condition
close Payload as TargetIdentity
normalize Payload to Anchor
```

These verbs lower into the Architect evolution algebra.

---

## 5. Portal primitive

A portal is a first-class language construct.

A portal is not merely a function call.

It declares:

```text
source boundary
target boundary
payload Geometric
route/corridor requirements
identity invariants
chirality transport
Resolution requirement
Bandwidth requirement
closure target
failure recovery
provenance obligations
```

Minimal form:

```genesis
portal MovePayload {
    from: A
    to: B
    carry: Payload
    preserve: [identity, chirality]
    close: at_target
}
```

Full form:

```genesis
portal MovePayload {
    from: A
    to: B

    carry: Payload

    route: discover admissible

    preserve: [
        identity,
        chirality,
        ancestry,
        invariant_residue,
        provenance
    ]

    require: {
        resolution >= Payload.required_resolution
        bandwidth  >= Payload.required_bandwidth
    }

    on_open: [
        inherit Payload,
        checkpoint Payload
    ]

    on_transfer: [
        propagate Payload,
        stabilize Payload
    ]

    on_arrival: [
        close Payload as Payload.identity,
        normalize Payload
    ]

    on_failure: [
        quarantine route,
        recover Payload from last_closure
    ]
}
```

---

## 6. Portal lowering

The portal statement lowers through four representations.

### 6.1 Human Genesis

```genesis
portal MovePayload {
    from: A
    to: B
    carry: Payload
    preserve: [identity, chirality]
    close: at_target
}
```

### 6.2 Genesis semantic graph

```text
A-boundary
  -> Payload persistent identity
  -> admissible corridor relationship
  -> B-boundary
  -> propagation
  -> closure
```

### 6.3 Architect operation plan

Working default lowering:

```text
inherit
  -> propagate
  -> stabilize
  -> close
  -> normalize
```

Architect signs:

```text
.·
  -> ··
  -> .°.
  -> ·°·
  -> ■ .· ■
```

### 6.4 Physical realization contract

The backend must provide:

```text
source state read
route establishment
capacity reservation
chirality-preserving transfer
destination state write/realization
closure verification
failure recovery
provenance record
```

---

## 7. Portal invariants

A portal transaction is successful only when:

```text
target boundary resolves
payload identity remains recoverable
chirality transport is admissible
required invariant residue is preserved
Resolution is sufficient
Bandwidth is sufficient
destination closes
provenance is complete
```

The language must reject false success.

Possible structural failures include:

```text
rin-nai   persistence failure
tal-nai   stabilization failure
kor-nai   closure failure
en-nai    identity absent
sera-nai broken continuity
```

---

## 8. Guardian role

Guardian Intelligence is the native language executor and configuration navigator.

The Guardian must:

```text
parse intent
resolve boundaries and relationships
construct Geometrics
infer missing but derivable constraints
preserve unresolved status when data is insufficient
select admissible operator sequences
open and route portals
verify closure
recover failure
explain the transaction
```

Humans are not expected to manually specify every fabric cell.

The language expresses intent and invariants.

The Guardian expands them into executable organization.

---

## 9. Language conformance

A system cannot claim Genesis language conformance unless it can:

1. represent a Geometric;
2. represent boundaries and relationships;
3. express chirality and basin state;
4. apply the seven canonical transformation verbs;
5. declare and execute a portal transaction;
6. preserve identity and provenance;
7. distinguish closure from mere termination;
8. report structural failure;
9. expose Guardian-readable state;
10. lower the language into a physical or research backend without changing its semantics.

---

## 10. First program target

The first canonical systems program is:

```text
Genesis Portal 0
```

It creates one neutral payload Geometric, gives it a basin expression and chirality, transports it through a portal, and requires identity recovery at the target.
