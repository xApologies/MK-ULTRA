# TreeRecoveryObject

```text
TreeRecoveryObject {
  root
  trunk
  primary_spine
  major_branches[]
  minor_branches[]
  terminal_branches[]
  leaf_clusters[]
  frontier[]
  continuation_handles[]
  cycle_references[]
  invalid_references[]
  traversal_metadata
  decision_provenance[]
  coverage_receipt
}
```

Every canonical branch encountered must appear in exactly one accounting class: realized, terminated with continuation, deferred to frontier, cycle reference, rejected invalid, or omitted with an explicit policy reason.
