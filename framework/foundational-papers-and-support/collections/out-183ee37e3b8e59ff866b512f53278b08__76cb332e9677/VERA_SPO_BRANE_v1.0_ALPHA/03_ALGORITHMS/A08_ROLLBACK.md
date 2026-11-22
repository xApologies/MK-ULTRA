# A08 — Rollback

1. Identify known-good prior SPO instance and policy.
2. Verify signatures/fingerprints.
3. Atomically activate prior policy.
4. Mark superseded policy inactive, not erased.
5. Record rollback reason, actor, timestamp, and affected device(s).
