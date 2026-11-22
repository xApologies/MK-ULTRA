# Start here — MK Ultra ER / Time-Shell integration v0.1

This is an incremental research checkpoint, not a full conversation export.

**Main result:** a native-ER-preserving exact memory interface and inverse for the archived linear modal recurrence, together with an explicit proposed nonlinear breathing-foam action and a source-based continuum boundary-kernel calculation.

**Not completed:** the entire microscopic theory, a derived spin-2/clock/metric handoff, all nonlinear Einstein constraints, or a complete physical inverse through GR alone.

Read `REPORT.md` for the mathematical argument and every scope restriction. `MODEL_DECISIONS.md` distinguishes preserved original definitions from new branch choices. `evidence/SOURCE_EXCERPTS.md` includes the original ER/graviton/Time-Shell contracts and original square-root response. The full canonical API is copied unchanged.

## Reproduce

Install Python dependencies listed in `requirements.txt` in a suitable local environment, then run:

    python code/checks.py
    python verify.py

The check script recomputes `results/CHECK_RESULTS.json`; its elapsed time will vary. The frozen manifest records the delivered run. Re-running changes that result file's hash because timing is recorded, so use `verify.py` before re-running to verify the original package, or keep your new result as a separate run. The mathematical check outcomes are deterministic for the supplied random seed.

No repository was modified. No online monitoring or background work was scheduled. The prior faithful-embedding audit ZIP is included unchanged under `prior/`; this does not make it a complete account-level export.

The newest proposed interface is a finite graph-port realization; it is not automatically identical to the native persistent boundary. This distinction is part of the result rather than an omitted implementation detail.
