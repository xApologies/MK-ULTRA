# AI 1.B Component Map

```text
mk43_ai/
├── module.py                 # BRANE entry point
├── contracts.py              # typed models and protocols
├── context.py                # isolated request context
├── interpretation.py         # intent and root resolution
├── ranking.py                # deterministic ranker + strategy interface
├── traversal.py              # Tree realization engine
├── decisions.py              # continue/terminate/defer/reject
├── continuation.py           # resumable continuation records
├── collapse.py               # finite ordered realization
├── validation.py             # collapse and invariant validation
├── policies.py               # immutable policy registry
├── provenance.py             # decision provenance
├── errors.py                 # structured failure model
└── fixtures/                 # deterministic tests only
```
