# Latency and Resource Budget

1.0 Alpha intentionally does **not** hard-code a medical/psychoacoustic latency threshold because the supplied sources do not establish one.

Instead, every transform declares a required latency class and every target device declares measured capability. Compilation succeeds only when:

```text
measured_device_path ≤ transform_requirement
```

The implementation plan must measure separately:
- capture buffering;
- feature extraction;
- classification;
- policy lookup / Vera gate;
- DSP;
- output buffering.

Power/resource telemetry should be recorded without allowing resource pressure to disable protected-cue behavior first.
