# A01 — Release Bootstrap and Integrity Verification

```text
INPUT: package_root, integrity_policy
OUTPUT: CanonicalSnapshot or BootstrapFailure

1. Locate current release manifest.
2. Verify required files are present.
3. Verify PACKAGE_CHECKSUMS.sha256.
4. Verify canonical Markdown digest against manifest.
5. Verify dependency-index canonical digest matches canonical Markdown.
6. Parse registries using strict schemas.
7. Load handle set and typed edge index into immutable structures.
8. Confirm declared counts against observed counts.
9. Validate admission policy exists.
10. Compute canonical fingerprint over ordered file digests and policy version.
11. Freeze all canonical structures.
12. Return CanonicalSnapshot.

FAIL CLOSED on any mismatch.
```
