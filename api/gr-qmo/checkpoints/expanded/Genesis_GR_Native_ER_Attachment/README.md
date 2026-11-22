# Genesis–GR: native ER metric attachment

This is an incremental research checkpoint, not the complete theory or the exhaustive conversation recovery.

## New result

The archived API contains explicit rules:

    g_tau = alpha d tau tensor d tau
    g_ER  = lambda Xi W Xi^T.

The adapter implements these rules, the reference-calibrated composite metric, an exact four-channel inverse, and a complete finite linear inverse for a constant network using jointly separating metric readouts.

The five-channel example recovers all fifteen symmetric edge weights from three spacetime readouts. A curved metric calculation is sent through the earlier tensor translator and returns the same constant ER network.

## Read

- DERIVATION.md — full derivation, hypotheses, two-sided proofs, image restrictions and the precise remaining boundary.
- evidence/API43_EXACT_EXCERPTS.md — original source passages, not a summary.
- evidence/DATABASE_RECOVERY.json — targeted database lookup and byte-identical source check.
- code/er_attachment.py — recovered-rule evaluator and inverse.
- code/checks.py — reproducible exact checks.
- results/CHECK_RESULTS.json — executed final results.
- code/prior_translator.py — unchanged code from the previous checkpoint.

## Run

    python -m pip install -r requirements.txt
    python code/checks.py
    python verify.py

The checks do not require network access. Python and SymPy versions actually used are recorded in the result JSON.

## Limits that must remain attached

The native construction of Xi and the chromatic metric contribution remains open in the inspected API. The script does not create them from raw History, Bandwidth or chirality. Finite-graph weights are not silently promoted to local fields. The current inverse recovers ER weights in the stated interface, not all upstream physical states, sources or histories.

The total native Genesis–GR endpoint remains unproved. This package is nevertheless more than another conditional frame calculation: it adds and tests a particular metric input rule actually recovered from the source, with an explicit inverse and concrete domain checks.
