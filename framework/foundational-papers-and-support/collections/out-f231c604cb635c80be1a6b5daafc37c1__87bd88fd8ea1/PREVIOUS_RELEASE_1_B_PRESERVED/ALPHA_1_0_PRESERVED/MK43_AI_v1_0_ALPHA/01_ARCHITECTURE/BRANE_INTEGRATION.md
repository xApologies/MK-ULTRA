# BRANE Integration

AI 1.B must load as an AI-role BRANE module and expose the exact AI⁵ port contract.

Required declarations:

```text
contract_version = "2.0"
internal_dimension = 5
canonical_state_policy = "READ_ONLY"
rewrite_policy = "DERIVED_ONLY"
```

Required common methods:

```python
dimension_model()
fork_request_context()
canonical_fingerprint()
healthcheck()
```

Required cognitive methods:

```python
interpret()
rank()
continue_or_terminate()
place_continuation()
collapse()
validate_collapse()
```
