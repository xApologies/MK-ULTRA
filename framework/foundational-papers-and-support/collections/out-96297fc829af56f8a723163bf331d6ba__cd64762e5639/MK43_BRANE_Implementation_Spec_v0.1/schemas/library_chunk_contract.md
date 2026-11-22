# Library Chunk Contract

```text
KnowledgePackage
  canonical_handle
  display_name
  package_version
  context
  chunks[]
    chunk_id
    chunk_type
    title
    body
    sequence
    language
    status
    provenance_ids[]
  equations[]
    equation_id
    exact_text
    symbol_definitions
    assumptions
    interpretation
    derivation_chunks[]
  relations[]
  provenance[]
  unresolved_fields[]
```

Required rule: a missing chunk family is represented explicitly; it is not filled with invented content.
