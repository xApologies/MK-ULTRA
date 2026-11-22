# Provenance and Versioning

Every independent SPO instance must carry:

```text
instance_id
parent_spo_api_fingerprint
source_profile_package_fingerprint
qmo_receipt_fingerprint
compiler_version
device_capability_fingerprint
policy_fingerprint
created_at
approval_receipts[]
previous_instance_id | null
```

Profile updates create a new instance rather than rewriting the previous one.

```text
SPO_v1 → SPO_v2 → SPO_v3
              ↘ rollback target remains recoverable
```

The Library retains active and historical versions according to policy.
