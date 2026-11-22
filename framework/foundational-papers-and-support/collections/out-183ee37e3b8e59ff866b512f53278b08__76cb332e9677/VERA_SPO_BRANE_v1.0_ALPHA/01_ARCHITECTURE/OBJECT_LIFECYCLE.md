# Object Lifecycle

```text
SPO_API^5                 CANONICAL / READ_ONLY
    ↓ recover
CanonicalGraph            REQUEST-LOCAL DERIVED VIEW
    ↓ collapse
TraversalRealization      REQUEST-LOCAL DERIVED VIEW
    ↓ compose
QMO^6                     PRIVATE / EPHEMERAL
    ↓ π_SPO
SPO_instance              INDEPENDENT / VERSIONED DERIVED OBJECT
    ↓ compile
DevicePolicy              SIGNED / BOUNDED / DEPLOYABLE
    ↓ run
RuntimeDecision           EPHEMERAL + AUDIT RECEIPT
    ↓ feedback
RevisionProposal          DOES NOT MUTATE CANON
```

Canonical promotion requires a separate review/promotion operation.
