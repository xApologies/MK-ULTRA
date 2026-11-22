# Current API companion mapping

> Current API: [GR/QMO](../../../../api/gr-qmo/00_START_HERE.md). Its supplied [definitions](../../../../api/gr-qmo/INTEGRATION_SPEC.md) and [object dictionary](../../../../api/gr-qmo/INSTALLED_OBJECTS.md) govern current API use. The superseded instructions in this block are retired; no equivalence of old runtime behavior or unprovided mathematics is implied. [Original guide and provenance](provenance://unavailable/content-sha256/23289bd3ee239436aaa5fbb65ada31e26dfaa12bf29352cf5a6bbc713bc98fb1/README.md).

The following retained sections describe this source collection. Historical implementation examples and domain-specific results are not a claim that GR/QMO implements those older interfaces.

# MK43 Ultra API 1.B

> Current API: [GR/QMO](../../../../api/gr-qmo/00_START_HERE.md). Its supplied [definitions](../../../../api/gr-qmo/INTEGRATION_SPEC.md) and [object dictionary](../../../../api/gr-qmo/INSTALLED_OBJECTS.md) govern current API use. The superseded instructions in this block are retired; no equivalence of old runtime behavior or unprovided mathematics is implied. [Original guide and provenance](provenance://unavailable/content-sha256/23289bd3ee239436aaa5fbb65ada31e26dfaa12bf29352cf5a6bbc713bc98fb1/README.md).

## Load with BRANE 2.1

```python
from mk43_brane.loader import PortLoader
from mk43_brane.ports import PortKind

loaded = PortLoader.from_zip(
    "MK43_Ultra_API_v1.B_FULL.zip",
    PortKind.API,
    expected_sha256="<detached zip sha256>",
)
api = loaded.instance
print(api.resolve("gravity"))
```

The module is read-only, request-forkable, provenance-aware, and fails closed on fabricated handles and edges.
