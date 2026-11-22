# Alpha 2.0 Closure in BRANE 2.1

This document records the executable closure of the independent 2.B-1 audit.

| Remaining 2.B-1 finding | 2.1 implementation |
|---|---|
| Chirality placeholder | API-mediated `resolve_chirality` and `admissible` fail-closed lift |
| Root-wide provenance | Per-handle provenance recovered before every lift |
| Cooperative canonical mutation | Canonical mounted modules remain untouched; each request executes against an isolated fork, with independent fingerprints retained as an audit control |
| Derived-only declaration only | Module declarations are explicit and request work occurs only in derived fork contexts |
| In-process opacity | `IsolatedBrane` hosts the entire BRANE behind IPC in a separate process |
| Weak module replacement | Candidate is staged, operationally probed, atomically mounted, and retained under a rollback window |
| Artifact-format disagreement | Markdown is enforced at ingress and again at artifact validation |
| Caller IDs ignored | Caller ID is preserved; a private execution ID is recorded separately |
| Schemas not reflected in code | Manual parser now enforces the shipped schema rules; equivalence is tested |
| Fabricated in-memory declarations | Explicit policies and dimension methods are required |
| Optional integrity | ZIP module loading requires detached SHA-256 by default; detached signatures are policy-selectable |
| AI domain unchecked | AI/API compatibility is enforced unless the AI declares `generic` |
| Unstable realization identity | Identity is derived from root, full path, relation path, chirality, depth, and provenance digest |
| Minimum-only report completeness | Expected chunk families are carried by library packages and enforced in complete mode |
| Shared module concurrency | Request execution is serialized and performed on request-local module forks |
