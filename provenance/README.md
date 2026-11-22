# Publication provenance

`file_manifest.jsonl` records the SHA-256 and size of every payload file present when this catalog was generated, excluding this generated `provenance/` catalog to avoid circular hashes. Paths are repository-relative. Git LFS entries describe the actual research file bytes, not the Git pointer text.

`source_occurrences.jsonl` retains independent source occurrences, original source hashes and source-name ancestry. A publication-copy hash may differ from its source hash when documentation paths or packaging were changed. The GR/QMO package's own `PUBLICATION_EDITION.json` records its exact edition changes and exclusions. Its internal manifest remains independently maintained by the GR/QMO publication toolchain.

`domain_index.json` indexes source collections without claiming new mathematical equivalence between them. Historical distinct QMO records remain nonactive research evidence. Local private paths, intake locations and operational audit reports are not included here.

Embedded source manifests describe their historical research packages and can refer to original archives or held containers outside this release. They are source-provenance records, not a claim that all historical package inputs are published. This catalog enumerates the actual publication; the active GR/QMO also has its own verified publication manifest. Unavailable historical references are recorded explicitly rather than replaced with invented files.
