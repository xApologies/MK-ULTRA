# R05 — Multiscale Closure
**Verdict: PASS WITH EXPLICIT SUBSPACE SCOPE**

Fine fixture: 4×4×4 primitive nearest-neighbor lattice, 64 loci, 144 edges. Coarse fixture: Q3 byte graph.

On the byte-coherent subspace, coarse seams lift to four primitive interface edges and whole-byte Portals lift exactly. With unit primitive weights, `Phi_fine = 4 Phi_coarse`.

Exhaustive coherent-state verification passed 524,288 cases.

Outside this subspace, discarded microstate distinctions are Resolution loss; unavailable micro-Portals are Bandwidth loss; append-only History may retain route information.

**Exit gate:** PASS.
