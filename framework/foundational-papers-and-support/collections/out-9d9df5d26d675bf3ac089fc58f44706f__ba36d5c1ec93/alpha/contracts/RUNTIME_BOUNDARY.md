# Runtime Boundary Contract

The runtime sees one callable object: BRANE.

## Request

```text
BraneRequest {
  request_id,
  operation,
  subject,
  scope,
  language,
  artifact_format,
  presentation_requirements,
  integrity_requirements
}
```

## Response

```text
BraneResponse {
  request_id,
  status,
  artifact_reference,
  artifact_size,
  artifact_sha256,
  recovery_receipt,
  errors
}
```

## Forbidden leakage

The response must not expose:

- raw API object
- raw Library storage
- AI internal chain state
- raw QMO⁶
- internal module filesystem paths
- secret keys or module credentials

## Runtime ignorance invariant

```text
RuntimeKnowledge = {BRANE public contract only}
```
