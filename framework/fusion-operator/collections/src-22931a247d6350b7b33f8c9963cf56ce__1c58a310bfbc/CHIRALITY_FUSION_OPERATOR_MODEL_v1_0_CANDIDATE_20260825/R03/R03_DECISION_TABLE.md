# R03 — Decision Table
## Correlation vs separability vs entanglement vs Fusion

| Class | Native object | A|B factorization required? | Coherence required? | Nonseparable? | Shared quotient locus? | Reduced purity diagnostic | Fusion implied? |
|---|---|---:|---:|---:|---:|---|---:|
| Classical anti-correlated pair | probability distribution / diagonal density embedding | for comparison only | no | no | no | can be 1/2 | no |
| Separable coherent quantum state | `rho_A tensor rho_B` or pure product | yes | may be yes | no | no | pure product gives 1 | no |
| Entangled chirality pair | density/pure state on `H_A tensor H_B` | yes | joint coherence for the Bell-like candidate | yes | no | Bell-like pure state gives 1/2 | no |
| Bare fused composite | quotient carrier `Q` | no native Hilbert factor supplied | no | not a typed question | yes | not applicable | yes, by construction |
| Hybrid fused + separable state | `(Q,W_AB,rho_sep)` | retained auxiliary registry | optional | no | yes | depends on state | already fused |
| Hybrid fused + entangled state | `(Q,W_AB,rho_ent)` | retained auxiliary registry | yes for current candidate | yes | yes | Bell-like gives 1/2 | already fused |

## Necessary / sufficient table

| Proposition | R03 verdict | Witness |
|---|---|---|
| Entanglement is necessary for Fusion | **FALSE** | fused carrier + product state |
| Entanglement is sufficient for Fusion | **FALSE** | entangled state + no Fusion interface |
| Fusion is necessary for entanglement | **FALSE** | entangled unfused pair |
| Fusion is sufficient for entanglement | **FALSE** | fused separable pair |
| Perfect anti-correlation is sufficient for entanglement | **FALSE** | classical mixture `rho_cl` |
| Coherence is sufficient for entanglement | **FALSE** | coherent product `|Sigma>` |
| Bare `Q` determines entanglement | **FALSE** | same `Q`, different `rho_AB` |
| A|B entanglement remains meaningful after factor erasure | **FALSE / ILL-TYPED** | A|B factorization is required by definition |

## Compact boundary

\[
\boxed{
\text{correlation} \neq
\text{coherence} \neq
\text{entanglement} \neq
\text{Fusion}
}
\]

The predicates may coexist, but none may be substituted for another.
