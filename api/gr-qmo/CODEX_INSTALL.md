# Codex handoff — install the complete GR/QMO

Use this extracted release as the authoritative active QMO. Do not reconstruct
it from a summary and do not reload the API 4.3 graph from the provenance archive.

First run:

```text
python mk43.py verify
python tests/test_installation.py
```

For an additive repository installation:

```text
python install.py --target "." --dry-run
python install.py --target "."
```

The active entrypoints are declared in `registry/ENTRYPOINTS.json`. Load
`registry/GR_QMO.sqlite` or `GR_QMO_DEPENDENCY_INDEX.json`; never select an
RP42 index, historical canonical, or the old integrated SQLite file from the
legacy directory.

Preserve the conditions attached to the 28 integration dependencies. A handle
name retained from API 4.3 does not reactivate its retired routing. Do not stage,
commit, push, or publish unless separately requested.
