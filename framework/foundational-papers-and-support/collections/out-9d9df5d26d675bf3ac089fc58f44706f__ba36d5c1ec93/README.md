# MK43 BRANE 2.3.2 — Brane-Only Host

MK43 BRANE 2.2 is the full Alpha-closure executable realization derived from:

- **2.0 Alpha** — mathematical, architectural, pseudocode, and recovery spine.
- **2.B** — initial executable realization.
- **2.B-1** — hardened reference realization.
- **2.1** — closed realization of the remaining Alpha contracts identified by independent audit.


## Canonical package boundary

This archive is **only the Brane host mechanism**. It contains no AI, API, or Library module archive or canonical payload. The three modules remain independent external packages and are mounted through the `ai`, `api`, and `library` ports at load time—analogous to plugging three USB devices into a computer.

Brane owns the port registry, contract validator, composition mechanism, request isolation, private QMO workspace, and output boundary. It does **not** own or absorb module domain content.

External loading example:

```bash
python plug_in_brane.py --ai /path/AI.zip --api /path/API.zip --library /path/LIBRARY.zip
```

## Boundary

The runtime communicates with one sealed BRANE object. For strict runtime opacity use `IsolatedBrane`, which hosts BRANE in a separate process and exposes only:

- `handle(request)`
- `replace_module(role, candidate)`
- `close()`

Internally BRANE mounts three five-dimensional modules:

- external AI⁵ port
- external API⁵ port
- external Library⁵ port

Their request-relative collaboration creates a private QMO⁶. Only the resulting artifact and receipt cross the boundary.

## Closure features

- exact AI⁵, API⁵, and Library⁵ contracts;
- semantic five-dimensional capability validation;
- explicit READ_ONLY / DERIVED_ONLY declarations;
- request-isolated module forks;
- object-specific provenance;
- API-mediated chirality resolution and admissibility checks;
- stable path/chirality/provenance realization identities;
- strict request ingress validation;
- caller request ID preservation plus private execution IDs;
- context-sensitive QMO accounting;
- expected knowledge-family validation;
- atomic streaming Markdown artifacts;
- staged operational module replacement;
- one-request automatic rollback window;
- detached checksum policy and optional detached Ed25519 signatures;
- archive traversal, symlink, expansion, member-count, and size defenses;
- independent AI/API/Library port-contract validation;
- sanitized public errors;
- process-isolated runtime façade;
- Alpha 2.0 preserved in `alpha/`.

## Quick start

```python
from mk43_brane import IsolatedBrane
from mk43_brane.fixtures import demo_modules

brane = IsolatedBrane(demo_modules(), "./artifacts")
try:
    response = brane.handle({
        "operation": "generate_report",
        "subject": "gravity",
        "request_id": "example-001",
        "artifact_format": "markdown"
    })
    print(response.to_json())
finally:
    brane.close()
```

## Tests

```bash
python -m pytest -q
```

Expected result for this release: **23 passed**.
