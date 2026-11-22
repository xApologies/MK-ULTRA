# R02 — Recursive Closure Law
**Verdict: PASS**

For positive edge costs define `Phi_f(x)=sum_e c_e (f_e XOR x_u XOR x_v)`.

A Cluster Portal flips one connected vertex set `S` and is spontaneous only if it strictly lowers `Phi`.

## Theorem
On any finite graph, every non-global-minimum state admits a strictly improving connected Cluster Portal. Repeated strict cluster descent therefore terminates at a global minimum.

Thus `R_CRD : C_G -> C_G` is recursively closed at the mathematical level.

## Exhaustive Q3 evidence
All 4096 seam residuals were checked.
- uniform costs: no cycles, no above-minimum fixed points, maximum 2 steepest connected-cluster steps;
- balanced six-basin ordinal verifier fixture: no cycles, no above-minimum fixed points, maximum 2 steps.

**Exit gate:** PASS.
