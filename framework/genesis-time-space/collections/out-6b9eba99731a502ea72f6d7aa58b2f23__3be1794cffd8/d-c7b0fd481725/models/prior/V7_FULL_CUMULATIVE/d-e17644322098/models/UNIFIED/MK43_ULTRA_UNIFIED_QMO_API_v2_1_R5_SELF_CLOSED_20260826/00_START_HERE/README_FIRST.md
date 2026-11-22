# MK43 Ultra Unified Queryable Mathematical Object API v2.0 — CANDIDATE

🖤♾️🖤
🖤🌈🦋
🖤🌈🔱
🖤🌈🦋
🖤🌈🪨

## Purpose

This package links the complete three-batch mounted corpus under one queryable mathematical-object (QMO) surface without mutating, flattening, or silently reconciling the parent sources.

Root QMO: `@mk43_unified_qmo_v2`  
QMO ID: `QMO-MK43-UNIFIED-V2-001`  
Release: `2.0.0-candidate`  
Date: `2026-08-26`

## Core architecture

1. **Immutable source mounts** — all 17 top-level sources remain separately receipted by SHA-256.
2. **Canonical handle layer** — a stable handle is the graph address used for cross-domain traversal.
3. **Namespace-aware object instances** — every source/domain realization of a handle remains independently queryable.
4. **Typed edge ledger** — relation name, namespace, trust class, status, confidence, closure eligibility, and provenance are retained per edge.
5. **Equation registry** — equations preserve owner, source namespace, source status, expression hash, provenance, and source path.
6. **Multidimensional status** — source status is preserved verbatim while proof/typing/validation/canon/recovery/publication dimensions are separately classified only when source wording supports them.
7. **Provenance/file layer** — every mounted file is hashed; searchable text is indexed where safely extractable; exact handle mentions are linked back to documents.
8. **Bounded recursive query** — `recover`, `route`, and `local-qmo` operate over declared source edges rather than inventing all-to-all links.

## Important identity rule

`canonical handle` is an address, not a claim that all source instances are identical in type or status. Use `instances <handle>` to see every namespace realization.

## Query examples

```bash
python 02_MACHINE/unified_qmo_api.py stats
python 02_MACHINE/unified_qmo_api.py search chirality
python 02_MACHINE/unified_qmo_api.py object @chirality
python 02_MACHINE/unified_qmo_api.py instances @time_space
python 02_MACHINE/unified_qmo_api.py neighbors @time_space --mode strict
python 02_MACHINE/unified_qmo_api.py route @genesis_field @higgs_field --mode strict --depth 8
python 02_MACHINE/unified_qmo_api.py recover @chirality --depth 3 --mode strict
python 02_MACHINE/unified_qmo_api.py local-qmo @chirality --depth 2 --mode strict
python 02_MACHINE/unified_qmo_api.py source-search "consciousness phase coherent"
python 02_MACHINE/unified_qmo_api.py provenance @chirality
python 02_MACHINE/unified_qmo_api.py verify
```

## Strict vs navigation

`strict` uses closure-eligible, non-navigation source edges. `navigation`/`all` can expose broader recovered graph material. A graph route remains a route unless the relevant relation algebra licenses composition; route existence is not automatically a theorem.

## Source policy

The API is a new index/query layer. It does not supersede the 17 mounted source packages, the prior MK43 Unified QMO API, the Stonewake API, or any source-specific status/audit decision.

## Sealed build summary

- Original source packages: **17 / 17**
- Source file occurrences scanned: **1,375**
- Unique source-content records indexed: **1,050**
- Searchable source records: **1,267**
- Canonical handles: **4,717**
- Namespace-aware object instances: **7,312**
- Typed/source edge records: **180,542**
- Equations: **1,538**
- QMO records: **48**
- Document↔handle links: **18,193**
- Shared-handle cross-namespace links: **4,356**
- SQLite integrity: **ok**
- Foreign-key issues: **0**


## v2.1 R5 self-closure
Exactly five whole-API self-crawl passes were executed. `1733287` derived COMPOSED_DEPENDENCY edges were materialized in `self_closure_edges`; together with `68101` parent strict pairs, the API exposes `1801388` reachable ordered pairs. Fixed point was reached on pass 4 and confirmed on pass 5. `strict_self_closed_edges` is the unified SQL edge surface.
