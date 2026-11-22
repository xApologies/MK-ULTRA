# A04 — Compile Device Policy

1. Validate independent SPO instance.
2. Load target `DeviceCapabilities`.
3. Intersect allowed transforms with device capabilities.
4. Apply canonical protected-event rules.
5. Reject rules whose latency/output/localization requirements cannot be met.
6. Build deterministic lookup/parameter tables.
7. Run static safety analysis.
8. Produce signed/fingerprinted `DevicePolicy` and compile receipt.
