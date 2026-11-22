# R08 — Readout Decision Table
## Resolution / Readout

| Readout | Retains | Hides / aliases | Current Fusion output | What it may establish |
|---|---|---|---|---|
| `R0_balance` | `S_chi` | local L/R, seam, source order, witness, provenance | `0` | net signed balance only |
| `R1_chi` | unordered `{L,R}`, `Pi_chi`, `S_chi`, `C_chi` | ordered ancestry, witness, seam | `{L,R}, -1, 0, 2` | two opposite local chiralities remain represented |
| `R2_seam` | R1 data + `q` | ordered source/witness provenance | chirality profile + shared seam | seam and local opposition are distinguishable |
| `R3_full` | ordered source images, chirality, seam, witness, provenance | nothing intentionally dropped by this work-layer contract | full decorated record | current formal reconstruction/provenance questions |
| `R_occ` branch | label populations | arrangement, handedness, seam semantics, provenance | `(3 null, 4 existence)` | population only |
| bare carrier projection | quotient carrier | historical source order/witness | `Q` | carrier structure only |
| display permutation | declared reindexing | none if bijective and inverse retained | may render diagonal as row | presentation change, not source change |
| identity-display contract | same coordinates expected | n/a | row output mismatches source | contract failure unless another declared map exists |

## Same source / different projection

For fixed formal `F_AB`:

\[
\mathrm{Read}_{R0}(F_{AB})
\neq
\mathrm{Read}_{R1}(F_{AB})
\neq
\mathrm{Read}_{R2}(F_{AB})
\neq
\mathrm{Read}_{R3}(F_{AB})
\]

in the sense that they inhabit different typed readable codomains and expose different distinctions.

## Different source / same projection

For ordered provenance records `F_AB != F_BA`:

| Resolution | Equal output? | Reason |
|---|---:|---|
| `R0_balance` | yes | source order discarded |
| `R1_chi` | yes | chirality multiset unordered |
| `R2_seam` | yes | seam retained but source order still discarded |
| `R3_full` | no | ordered provenance/witness retained |
| `R_occ` | yes | only populations retained |

Therefore observational equality is readout-relative.
