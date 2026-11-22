# A09 — Failure Handling

- Classifier failure → preserve/transparency.
- Policy lookup failure → preserve/transparency.
- Corrupt policy/signature → refuse transformed mode.
- DSP exception → bypass transform if hardware supports safe bypass; otherwise enter manufacturer-defined safe mode.
- Battery/resource pressure → disable nonessential processing before protected-cue handling.
- Clock/timestamp anomaly → continue safe audio path; flag receipt.
- Provenance mismatch → policy not deployable.
