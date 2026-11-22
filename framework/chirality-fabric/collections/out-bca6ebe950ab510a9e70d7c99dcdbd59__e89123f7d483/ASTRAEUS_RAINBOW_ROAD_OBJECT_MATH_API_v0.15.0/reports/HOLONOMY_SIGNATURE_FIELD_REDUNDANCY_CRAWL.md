# Holonomy Signature Field Redundancy Crawl

**API release:** 0.10.0  
**Live-model revision:** v0.23.0  
**Status:** OPEN / BOUNDED CRAWL COMPLETED  
**Active frontier:** `@holonomy_signature_field_redundancy_crawl`

## Purpose

Test the source scaffold

`Sig_Hol = (src, tgt, [h], Hol_Conn, Hol_chi, Hol_Id, scope, provenance)`

against the already-closed recovery-signature realization criterion. The objective is to determine which typed projection, if any, has kernel exactly equal to Recovery Context Equivalence.

## Registered Dependency Landscape

`@dl_holonomy_field_redundancy`

Roots:

- `@holonomy_signature_field_redundancy_crawl`
- `@holonomy_history_signature`
- `@signature_underresolution_defect`
- `@signature_overresolution_defect`

The registered landscape contains 16 QMOs and 22 preserved typed edges.

## Bounded Crawl

Registered iteration QMO:

`@it_holonomy_field_redundancy_3`

Requested horizon: 3.  
Executed iterations: 3.  
Terminal state: `MAX_ITERATIONS`.

The materialized landscape `@it_holonomy_field_redundancy_3_landscape` contains the resolved local dependency shell. The crawl did not derive a licensed field projection with proven kernel equality.

## Audit disposition

No concrete subtuple is promoted. The source field `[h]` remains semantically under-typed for the intended compression test. Removing it without a separating counterexample test is unlicensed.

The frontier therefore remains open and counterexample-driven.

## Next required work

1. Define typed projection candidates over the source signature fields.
2. Search first for underresolution counterexamples for each projection.
3. Reject any projection that merges distinct Recovery Context Equivalence classes.
4. Test survivors for overresolution/redundancy.
5. Audit compatibility with History composition.
6. Retain full History/provenance as the safe fallback whenever no smaller projection is certified.
