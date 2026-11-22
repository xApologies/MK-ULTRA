# Current API companion mapping

> Current API: [GR/QMO](../../../../../api/gr-qmo/00_START_HERE.md). Its supplied [definitions](../../../../../api/gr-qmo/INTEGRATION_SPEC.md) and [object dictionary](../../../../../api/gr-qmo/INSTALLED_OBJECTS.md) govern current API use. The superseded instructions in this block are retired; no equivalence of old runtime behavior or unprovided mathematics is implied. [Original guide and provenance](provenance://unavailable/content-sha256/1b4189b9930b2890e594596f6d5bab234f5df54c472579f3c3950c42ff513ca2/README.md).

The following retained sections describe this source collection. Historical implementation examples and domain-specific results are not a claim that GR/QMO implements those older interfaces.

# Genesis–GR: native ER metric attachment

This is an incremental research checkpoint, not the complete theory or the exhaustive conversation recovery.

## New result

The archived API contains explicit rules:

    g_tau = alpha d tau tensor d tau
    g_ER  = lambda Xi W Xi^T.

The adapter implements these rules, the reference-calibrated composite metric, an exact four-channel inverse, and a complete finite linear inverse for a constant network using jointly separating metric readouts.

The five-channel example recovers all fifteen symmetric edge weights from three spacetime readouts. A curved metric calculation is sent through the earlier tensor translator and returns the same constant ER network.

## Read

> Current API: [GR/QMO](../../../../../api/gr-qmo/00_START_HERE.md). Its supplied [definitions](../../../../../api/gr-qmo/INTEGRATION_SPEC.md) and [object dictionary](../../../../../api/gr-qmo/INSTALLED_OBJECTS.md) govern current API use. The superseded instructions in this block are retired; no equivalence of old runtime behavior or unprovided mathematics is implied. [Original guide and provenance](provenance://unavailable/content-sha256/1b4189b9930b2890e594596f6d5bab234f5df54c472579f3c3950c42ff513ca2/README.md).

## Run

    python -m pip install -r requirements.txt
    python code/checks.py
    python verify.py

The checks do not require network access. Python and SymPy versions actually used are recorded in the result JSON.

## Limits that must remain attached

The native construction of Xi and the chromatic metric contribution remains open in the inspected API. The script does not create them from raw History, Bandwidth or chirality. Finite-graph weights are not silently promoted to local fields. The current inverse recovers ER weights in the stated interface, not all upstream physical states, sources or histories.

The total native Genesis–GR endpoint remains unproved. This package is nevertheless more than another conditional frame calculation: it adds and tests a particular metric input rule actually recovered from the source, with an explicit inverse and concrete domain checks.
