# SPO API Formalism

The supplied API formalism defines:

```text
API^5 = (Identity, Dependency, Chirality, RecursiveDepth, Provenance)
```

For the auditory domain, define the canonical mapped object:

```text
SPO_API^5 := (I, D, χ, R, P ; A)
```

where:
- `I` = identity handles for event classes, transforms, policy classes, profile fields, device constraints;
- `D` = typed dependency graph among those objects;
- `χ` = BRANE-required chirality/admissibility state and branch orientation metadata;
- `R` = recursive/context depth, ancestry, and closure horizon;
- `P` = provenance, source, status, audit, and revision lineage;
- `A` = auditory-domain payload attached to canonical records.

`A` does not add a sixth BRANE dimension. It is domain content represented by the canonical records. BRANE supplies realization as the sixth coordinate.

The API-level object is immutable during ordinary requests:

```text
Mutate(SPO_API^5 | ordinary_request) = FORBIDDEN
```

All user/context outputs are derived.
