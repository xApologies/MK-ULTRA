# R04 — Counterexample Ledger
## Superposition Structure

### C4-01 — Occupancy overlay is not quantum superposition
Take two 2×2 occupancy representatives and add/overlay their marks. The result may be a perfectly meaningful combinatorial picture, but without complex amplitudes, normalization, an inner product, and a phase relation it is not a Hilbert superposition.

**Verdict:** rejects `geometric overlay => coherent superposition`.

### C4-02 — Same chirality populations, different coherence

\[
|\Psi_0\rangle=(|LR\rangle+|RL\rangle)/\sqrt2
\]

and

\[
\rho_{\rm cl}=\tfrac12|LR\rangle\langle LR|+\tfrac12|RL\rangle\langle RL|
\]

both yield 50/50 `LR/RL` in the chirality basis. Only the first has off-diagonal coherence.

**Verdict:** population readout does not prove superposition.

### C4-03 — Fusion without superposition
Take a Fusion-admissible carrier pair and quantum state `|LR>`. The carrier quotient exists but the state has support size one in `B_AB`.

**Verdict:** `Fusion !-> Superposition`.

### C4-04 — Superposition without Fusion
The source single-mote creation state `( |L> + |R> )/sqrt(2)` is already a chirality superposition without two-carrier contact Fusion.

**Verdict:** `Superposition !-> Fusion`.

### C4-05 — Same Q, different quantum states
The same bare quotient carrier `Q` can be packaged with `|LR>`, a separable four-term state, a Bell-like state, or an incoherent mixture.

**Verdict:** `Q` does not determine what is superposed.

### C4-06 — Native fused basis without an encoding map is a type error
Writing `|F_1>,|F_2>` as though they were already defined by the quotient silently invents a Hilbert structure.

**Verdict:** a native fused-output superposition requires additional `H_F,V_F` data.

### C4-07 — Global phase is not a new superposition
`|psi>` and `e^{i theta}|psi>` represent the same ray. Counting this as a distinct coherent alternative would manufacture a false degree of freedom.

**Verdict:** only relative phase among basis amplitudes is relevant here.
