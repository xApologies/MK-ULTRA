# BRANE 2.3.2 — Live Collapse-Constrained Crawl

## Corrected pipeline

```text
request -> BRANE private QMO workspace
        -> API root resolution
        -> API local route proposals
        -> Collapse Intelligence restriction per proposal
        -> BRANE admits continuation or records leaf/frontier/cycle
        -> bounded QMO
        -> Library handoff
        -> report
        -> QMO destruction
```

BRANE no longer asks the API to materialize a complete closure before AI participation. It also no longer asks the AI to deconstruct a completed graph. The API remains the canonical route authority. The Collapse Intelligence remains the domain and leaf authority. BRANE conducts the crawl, enforces the declared policy envelope, owns the transient QMO, and performs the Library handoff.

Recursive re-entry and duplicate canonical-domain expansion are represented as finite continuation leaves rather than recursively reopening the dependency landscape.

No AI, API, or Library package is embedded in this release.
