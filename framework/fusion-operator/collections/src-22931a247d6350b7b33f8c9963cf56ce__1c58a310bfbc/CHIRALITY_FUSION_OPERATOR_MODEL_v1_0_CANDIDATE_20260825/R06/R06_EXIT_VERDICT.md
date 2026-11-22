# R06 — Exit Verdict
## Reversibility

**Run:** R06 / 10  
**Verdict:** **CLOSED**

## Classification

\[
\boxed{
\textbf{PROVENANCE-REVERSIBLE / SEAM-CONDITIONALLY REVERSIBLE / BARE-CARRIER IRREVERSIBLE}
}
\]

The classification is data-regime dependent:

| Retained output | Reversibility result |
|---|---|
| Bare `(Q,lambda_Q)` | **IRREVERSIBLE / NON-IDENTIFIABLE** for exact ordered source recovery |
| `(Q,q)` only | **IRREVERSIBLE** in general; fused point known but seam not known |
| `(Q,S_F)` with source-image seam | **CONDITIONALLY REVERSIBLE UP TO ISOMORPHISM** via `U_cut` |
| Full `(Q,W_G,eta_F,Inv_F)` | **PROVENANCE-REVERSIBLE ON THE IMAGE OF FUSION** |
| Hybrid record with retained `rho_AB` | state record recoverable; **quantum dynamical reversibility UNRESOLVED** |
| Physical process | **NOT ESTABLISHED** |

## Required roadmap exit tests

- left inverse: **resolved** — none exists for the noninjective quotient projection; witness-decorated Fusion has a provenance-extraction left inverse;
- right inverse: **resolved** — quotient sections exist but are not unfusion; witness right inversion is image-restricted;
- local inverse: **resolved** — source-image inverses exist;
- provenance inverse: **resolved** — exact source-record recovery exists when full witness is retained;
- side-information inverse: **resolved** — seam cut reconstructs sources up to isomorphism;
- many-to-one behavior: **resolved** — interface identification and source-swap nonidentifiability demonstrated;
- destroyed/retained information: **resolved** — carrier loses interface multiplicity, full witness externalizes and preserves it.

## Central law

> **Fusion can be irreversible as a carrier quotient while remaining reversible as a fully witnessed provenance record. Reversibility belongs to the operator together with the retained information boundary.**

**Next:** R07 — Chirality Conservation.
