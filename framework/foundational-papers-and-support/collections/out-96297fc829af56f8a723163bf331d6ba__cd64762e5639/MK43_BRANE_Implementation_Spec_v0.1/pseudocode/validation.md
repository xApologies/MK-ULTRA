# Validation Pseudocode

```text
FUNCTION CHECK_LIBRARY_COVERAGE(qmo):
    expected ← SET(qmo.recovery_requirements.handles)
    returned ← SET(qmo.recovered_chunks.handles)
    unresolved ← expected - returned
    duplicate ← FIND_DUPLICATE_PACKAGES(qmo.recovered_chunks)
    invalid ← FIND_INVALID_PROVENANCE(qmo.recovered_chunks)

    RETURN {
        expected_count: SIZE(expected),
        recovered_count: SIZE(returned),
        unresolved: unresolved,
        duplicates: duplicate,
        invalid_provenance: invalid,
        complete: EMPTY(unresolved, duplicate, invalid)
    }

FUNCTION VALIDATE_ARTIFACT(artifact, qmo):
    ASSERT artifact EXISTS
    ASSERT artifact.size > 0
    ASSERT artifact.encoding == UTF_8
    ASSERT EVERY_REQUIRED_HANDLE_IS_RENDERED_OR_DECLARED_UNRESOLVED(artifact, qmo)
    ASSERT NO_UNCONTROLLED_RECURSIVE_DUPLICATION(artifact)
    RETURN SIGNED_OR_CHECKSUM_RECEIPT(artifact)
```
