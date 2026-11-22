# Implementation Map

## Proposed 1.B components

```text
vera_spo/
├── authoring/
│   ├── normalization.py
│   ├── profile_package.py
│   └── approval.py
├── brane/
│   ├── auditory_api_module.py
│   ├── auditory_ai_module.py
│   ├── auditory_library_module.py
│   ├── spo_projection.py
│   └── receipts.py
├── compile/
│   ├── capability_negotiation.py
│   ├── policy_compiler.py
│   └── static_safety.py
├── runtime/
│   ├── frontend.py
│   ├── classifier.py
│   ├── scene.py
│   ├── vera_gate.py
│   ├── policy_lookup.py
│   ├── dsp_backend.py
│   └── telemetry.py
└── models/
    ├── spo_api.py
    ├── spo_instance.py
    ├── event.py
    ├── policy.py
    └── provenance.py
```

The included scaffold implements only the data/safety control layer. Live audio DSP and classification are intentionally interfaces/placeholders in 1.0 Alpha.
