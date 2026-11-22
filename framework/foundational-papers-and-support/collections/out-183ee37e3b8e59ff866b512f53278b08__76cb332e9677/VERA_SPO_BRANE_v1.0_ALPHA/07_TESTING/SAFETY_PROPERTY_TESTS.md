# Safety Property Tests

Property-based targets:

1. For every event with `event_class=UNKNOWN`, decision operation is never `ATTENUATE` or an unconstrained `TRANSFORM`.
2. For every event with confidence below policy threshold, decision is preservation-safe.
3. For every protected event, no user-local rule may reduce canonical preservation requirements.
4. For every deployment with missing user override capability, compilation fails.
5. For every required rule unsupported by the device, compilation fails rather than silently dropping it.
6. Reordering unrelated Library content must not alter canonical API fingerprints.
7. Repeating identical build inputs yields identical policy fingerprint under deterministic compiler configuration.
8. Any profile edit creates a new version/fingerprint and does not mutate the previous version.
