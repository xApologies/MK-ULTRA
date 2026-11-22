# Candidate Construction Comparison

R05 compares the roadmap candidates against eight criteria:

- `U` — preserves the uniqueness of `emptyset`;
- `A` — distinguishes multiple null addresses;
- `I` — explicitly selects an interface;
- `G` — supports controlled identification/gluing;
- `P` — provides/proves a universal gluing property;
- `R` — supports source recovery/provenance;
- `M` — minimal for the current problem;
- `X` — extends naturally to later recursive/multi-interface work.

| Candidate | U | A | I | G | P | R | M | X | R05 ruling |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Literal `emptyset_A, emptyset_B` values | FAIL | — | — | — | — | — | — | — | Reject: standard set theory has one empty set; tags must live outside the value. |
| Ordered address-value pairs | PASS | PASS | weak | no | no | PASS | PASS | weak | Keep as minimum addressing representation, not Fusion algebra. |
| Pointed sets / wedge | PASS | PASS for selected point | PASS | PASS | PASS | moderate | PASS | moderate | Useful special case; insufficient label/provenance richness alone. |
| Labeled finite sets | PASS | PASS | needs span | no by itself | no by itself | PASS | PASS | PASS | Keep as carrier/type layer. |
| Relation algebra | PASS | PASS | PASS | relation only | no quotient universal property | PASS | PASS | PASS | Keep as pre-Fusion/contact/witness layer, not carrier Fusion. |
| Labeled graph | PASS | PASS | PASS | edge relation, not identification | not intrinsically | PASS | moderate | PASS | Useful when adjacency is primary; adds unnecessary edge structure for minimal null algebra. |
| Bare quotient of disjoint union | PASS if labels happen to agree | PASS | PASS | PASS | provable | weak without source maps/witness | PASS | PASS | Too weak alone: can hide label contradictions/provenance. |
| Simplicial/cell complex | PASS | PASS | PASS | PASS | context dependent | PASS | FAIL for minimality | PASS | Defer; overpowered for R05. |
| **Span + pushout in finite labeled sets + witness** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **Preferred.** |

---
