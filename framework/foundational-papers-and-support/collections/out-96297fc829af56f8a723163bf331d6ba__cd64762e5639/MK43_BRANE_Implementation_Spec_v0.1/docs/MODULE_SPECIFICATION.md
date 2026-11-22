# Current API companion mapping

> Current API: [GR/QMO](../../../../../../api/gr-qmo/00_START_HERE.md). Its supplied [definitions](../../../../../../api/gr-qmo/INTEGRATION_SPEC.md) and [object dictionary](../../../../../../api/gr-qmo/INSTALLED_OBJECTS.md) govern current API use. The superseded instructions in this block are retired; no equivalence of old runtime behavior or unprovided mathematics is implied. [Original guide and provenance](provenance://unavailable/content-sha256/4b6f800695d3a833a594b23e950fd75f239c9eaae70abb27d0f554fe01c7076b/MODULE_SPECIFICATION.md).

The following retained sections describe this source collection. Historical implementation examples and domain-specific results are not a claim that GR/QMO implements those older interfaces.

# Module Specification

## BRANE package

A BRANE package is a versioned deployment bundle containing a manifest and three required pluggable modules.

```text
brane/
├── manifest
├── collapse_intelligence/
├── api/
├── library/
├── policies/
└── optional language/report resources
```

## Required module capabilities

### Collapse Intelligence module

Must expose conceptual operations equivalent to:

- `compile_request(request)`
- `plan_recovery(api_capabilities, request)`
- `realize_tree(canonical_graph, policy)`
- `evaluate_coverage(qmo, library_receipt)`
- `request_continuation(qmo, unresolved_state)`

### API module

Must expose conceptual operations equivalent to:

- `describe_capabilities()`
- `resolve_handle(handle_or_phrase)`
- `recover_graph(root, traversal_request)`
- `build_qmo(graph, metadata)`
- `validate_qmo(qmo)`

### Library module

Must expose conceptual operations equivalent to:

- `describe_capabilities()`
- `recover_handle(handle, context)`
- `recover_batch(ordered_handles, context)`
- `validate_coverage(qmo, recovered_chunks)`
- `render_language(chunks, language)`

## Compatibility rules

Every module declares:

- semantic version;
- contract version;
- supported schema versions;
- domain identifiers;
- required dependencies;
- checksums;
- migration requirements.

BRANE loading fails closed when contracts are incompatible. The runtime receives a failure receipt; it never receives partially loaded internals.

## Hot-swappable upgrades

The following upgrades are independent when contracts remain compatible:

> Current API: [GR/QMO](../../../../../../api/gr-qmo/00_START_HERE.md). Its supplied [definitions](../../../../../../api/gr-qmo/INTEGRATION_SPEC.md) and [object dictionary](../../../../../../api/gr-qmo/INSTALLED_OBJECTS.md) govern current API use. The superseded instructions in this block are retired; no equivalence of old runtime behavior or unprovided mathematics is implied. [Original guide and provenance](provenance://unavailable/content-sha256/4b6f800695d3a833a594b23e950fd75f239c9eaae70abb27d0f554fe01c7076b/MODULE_SPECIFICATION.md).

An API update may require a library coverage update if it introduces new handles. It does not automatically require an intelligence update.
