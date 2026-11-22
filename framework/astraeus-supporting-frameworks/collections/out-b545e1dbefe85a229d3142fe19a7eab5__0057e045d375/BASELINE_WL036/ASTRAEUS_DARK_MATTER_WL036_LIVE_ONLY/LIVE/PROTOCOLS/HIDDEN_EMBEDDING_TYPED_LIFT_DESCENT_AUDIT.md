# AST-DM-WL-P027 — Hidden Embedding Typed-Lift / Descent Audit

## Purpose

Use existing Transduction typed-lift and descent machinery only as a query architecture around the Dark Matter 2.2 hidden-state embedding OpenSlot. Do not create a hidden embedding by analogy.

## Stage 0 — fixed parent target

```text
Emb_H,phys^R = {
 iota_H:E_H^R ↪ E |
 pi_E o iota_H = j_T o pi_H,
 I o iota_H = iota_H o I_H,
 iota_H(E_H^R) subseteq ker(C)
}.
```

## Stage 1 — local data recovery

Search only source-backed records for:

- a local cover/localization of `E_H^R`;
- local realization/lift candidates over the corresponding base map;
- overlap transition maps;
- chirality/admissibility restrictions;
- inheritance compatibility;
- constraint-kernel admission.

If no such local family is source-supported: STOP `LOCAL_DATA_ABSENT`.

## Stage 2 — descent compatibility

If local data exist, apply existing Transduction descent criteria. Do not invent overlaps or cocycles.

If descent fails or is untyped: STOP and retain the defect.

## Stage 3 — global realization witness

Require an existing/formally admissible gluing witness `W_G(X,G)` and test whether the resulting global realization `G` is actually an injective map satisfying every `Emb_H,phys^R` condition.

If not: STOP `GLOBAL_EMBEDDING_NOT_CERTIFIED`.

## Stage 4 — selection

Even if at least one valid global embedding exists, do not call it physical until the API supplies/earns a selection rule.

## Success condition

This protocol only closes the structural nonemptiness portion if a source-supported local family glues to at least one certified `iota_H in Emb_H,phys^R`.

It does not by itself close physical selection or dark-matter qualification.
