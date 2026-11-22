# Internal QMO Schema (Draft)

This schema is intentionally descriptive and private to BRANE.

```text
QMO
  identity
    qmo_id
    request_id
    schema_version
  request
    operation
    root_subject
    context
    report_specification
  canonical_structure
    resolved_root
    nodes[]
    typed_edges[]
    layers[]
    provenance[]
  realization
    trunk
    primary_spine
    major_branches[]
    minor_branches[]
    terminal_branches[]
    leaf_clusters[]
    frontier[]
    continuation_handles[]
  library_state
    required_handles[]
    recovered_packages[]
    unresolved[]
  report_state
    section_plan[]
    artifact_state
  validation
    graph_receipt
    coverage_receipt
    artifact_receipt
```
