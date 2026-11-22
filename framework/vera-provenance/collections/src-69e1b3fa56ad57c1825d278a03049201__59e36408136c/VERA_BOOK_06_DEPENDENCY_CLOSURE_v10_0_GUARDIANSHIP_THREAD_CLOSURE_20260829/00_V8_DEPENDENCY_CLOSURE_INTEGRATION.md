# V8 — Dependency & Closure-specific integration

Dependency analysis now tracks question dependencies and local-primitive admissions.

A downstream object may legitimately depend on a locally admitted primitive while the primitive's deeper provenance remains outside scope. Reopening the foundational question reactivates the dependency crawl rather than invalidating prior scoped work automatically.
