# Vera Safety Invariants

## V1 — Unknown is not permission to suppress

```text
Unknown(E) OR confidence(E) < threshold
    ⇒ operation ∈ {PRESERVE, bounded safe processing}
```

## V2 — Protected events inherit preservation

If an event is protected by canonical policy, a user SPO may not weaken that protection without an explicit higher-authority policy pathway.

## V3 — Device incapability fails closed to transformation

If the hardware cannot realize a transformation while satisfying the required safety constraints, that transformation is unavailable.

## V4 — User override

The user must be able to immediately request transparency/preservation behavior.

## V5 — No hidden profile mutation

Realtime use may emit telemetry/feedback receipts but may not silently rewrite the user's profile.

## V6 — Provenance required

Every deployed policy must identify the API fingerprint, profile revision, compiler version, device target, and approval lineage.

## V7 — Clinical uncertainty is represented as uncertainty

The system does not infer a diagnosis from an acoustic preference or response.
