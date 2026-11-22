# R03 — Definitions Ledger
## Entanglement Boundary

### D3-01 — Work-layer two-seed quantum lift
For the purpose of R03 only, attach one copy of the two-state chirality Hilbert space to each source seed:

\[
\mathcal H_A=\operatorname{span}\{|L\rangle_A,|R\rangle_A\},
\qquad
\mathcal H_B=\operatorname{span}\{|L\rangle_B,|R\rangle_B\}.
\]

The bipartite diagnostic space is

\[
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B.
\]

This tensor product is a **quantum lift of the two source degrees of freedom**, not a theorem that the quotient carrier `Q` itself factorizes.

### D3-02 — Product chirality basis
Use ordered basis

\[
\mathcal B_{AB}=(|LL\rangle,|LR\rangle,|RL\rangle,|RR\rangle).
\]

### D3-03 — Classical correlation
A classical joint chirality distribution `P_AB` is correlated when

\[
P_{AB}\neq P_A P_B.
\]

The anti-correlated reference distribution is

\[
P(L,R)=P(R,L)=\tfrac12,
\qquad
P(L,L)=P(R,R)=0.
\]

### D3-04 — Quantum separability
A mixed state `rho_AB` is separable when it can be written

\[
\rho_{AB}=\sum_k p_k\,\rho_A^{(k)}\otimes\rho_B^{(k)},
\qquad p_k\ge0,\quad\sum_kp_k=1.
\]

A pure state is separable exactly when

\[
|\psi\rangle=|a\rangle\otimes|b\rangle.
\]

### D3-05 — Entanglement
A state on the explicitly declared bipartite factorization

\[
\mathcal H_A\otimes\mathcal H_B
\]

is entangled when it is not separable. Entanglement is therefore **factorization-relative**: without a declared A|B subsystem structure (or equivalent commuting-subalgebra structure), the predicate is not typed.

### D3-06 — Coherence in the chirality product basis
For a density state `rho`, chirality-basis coherence between `|LR>` and `|RL>` is represented by nonzero matrix elements

\[
\langle LR|\rho|RL\rangle
\quad\text{or}\quad
\langle RL|\rho|LR\rangle.
\]

This is basis-dependent and is not, by itself, an entanglement criterion.

### D3-07 — Current Fusion predicate
Let

\[
\mathrm{Fus}(A,B;\rho_G)=1
\]

when the R01 geometric/interface admissibility data `rho_G` exists and the partial quotient Fusion operator is defined. Otherwise it is zero/undefined.

This predicate belongs to the **carrier/interface layer**, not the quantum-state layer.

### D3-08 — Entanglement predicate
Let

\[
\mathrm{Ent}(\rho_{AB}\mid A|B)=1
\]

when `rho_AB` is nonseparable relative to the declared A|B quantum factorization.

### D3-09 — Hybrid fused quantum object
When both a quotient Fusion witness and a quantum factor registry are intentionally retained, define the work-layer hybrid object

\[
\widehat F
=
(Q,\eta_F,\mathrm{Inv}_F,W_{AB},\rho_{AB}),
\]

where `W_AB` records the auxiliary A|B Hilbert factors and their provenance. Entanglement, if present, is a property of `rho_AB` relative to `W_AB`; it is **not a property of bare `Q` alone**.

### D3-10 — Forgetful map
Define

\[
U(\widehat F)=Q
\]

as the operation that discards the quantum factor registry and quantum state while retaining only the bare fused carrier.

### D3-11 — Strong-fusion entanglement boundary
If a future strong Fusion produces a state space `H_F` with no canonical A|B factorization and no retained factor registry, then the proposition “A is entangled with B after Fusion” is **undefined**, not false and not automatically maximal.
