# Canonical and Derived Types

## Canonical types

- `CanonicalHandle`
- `AliasRecord`
- `CanonicalObjectRecord`
- `EdgeRecord`
- `EquationRecord`
- `ProvenanceRecord`
- `RecoveryPassRecord`
- `AdmissionPolicy`
- `CanonicalSnapshot`

## Request-local derived types

- `RecoveryIntent`
- `RequestContext`
- `TraversalNode`
- `TraversalPath`
- `ChiralityState`
- `AdmissibilityDecision`
- `CanonicalGraph` (derived view of canonical objects and edges)
- `DiagnosticRecord`

## EdgeRecord schema

```text
source
relation
target
graph_family
confidence
audit_status
recovery_pass
provenance
```

Observed 4.3 fields are preserved exactly. API 5.B may add derived indexes but may not rewrite these records.
