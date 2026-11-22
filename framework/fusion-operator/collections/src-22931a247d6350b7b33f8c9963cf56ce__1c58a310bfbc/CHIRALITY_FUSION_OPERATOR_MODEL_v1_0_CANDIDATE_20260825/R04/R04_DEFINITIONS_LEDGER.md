# R04 — Definitions Ledger
## Superposition Structure

### D4-01 — Chirality basis
For one seed, use the orthonormal mirror-chirality basis

\[
\mathcal B_\chi=(|L\rangle,|R\rangle).
\]

`L/R` denote the two mirror orientation classes without fixing the unresolved numeric-sign convention.

### D4-02 — Single-seed state

\[
|\psi\rangle=\alpha|L\rangle+\beta e^{i\phi}|R\rangle,
\qquad |\alpha|^2+|\beta|^2=1.
\]

A state is superposed **in the chirality basis** when both amplitudes are nonzero and coherence is retained.

### D4-03 — Joint chirality basis

\[
\mathcal B_{AB}=(|LL\rangle,|LR\rangle,|RL\rangle,|RR\rangle).
\]

A general pure two-seed state is

\[
|\psi_{AB}\rangle=
\sum_{x,y\in\{L,R\}}c_{xy}|xy\rangle,
\qquad
\sum_{x,y}|c_{xy}|^2=1.
\]

### D4-04 — Relative phase
For nonzero amplitudes `c_j,c_k`, their physically relevant relative phase is

\[
\phi_{jk}=\arg(c_k)-\arg(c_j).
\]

A common global phase multiplying every amplitude is not an observable distinction in the Hilbert model.

### D4-05 — Coherent superposition versus mixture
For two alternatives `|u>,|v>`, the coherent pure state

\[
|\psi\rangle=\alpha|u\rangle+\beta e^{i\phi}|v\rangle
\]

has density operator containing off-diagonal terms

\[
\alpha\beta^*e^{-i\phi}|u\rangle\langle v|+
\alpha^*\beta e^{i\phi}|v\rangle\langle u|.
\]

The corresponding incoherent mixture

\[
\rho_{\rm mix}=|\alpha|^2|u\rangle\langle u|+|\beta|^2|v\rangle\langle v|
\]

contains no such coherence terms in that basis.

### D4-06 — Structural Fusion map

\[
\mathfrak F_G(A,B;\rho_G)=(Q,\eta_F,\mathrm{Inv}_F)
\]

acts on carrier/interface data. It is not, by itself, a linear operator on `H_AB`.

### D4-07 — Quantum-decoration lift of Fusion
Define the **minimal typed lift**

\[
\mathfrak F_{\rm dec}:
(A,B,\rho_G,W_{AB},\rho_{AB})
\mapsto
(Q,\eta_F,\mathrm{Inv}_F,W_{AB},\rho_{AB}).
\]

This packages the pre-existing quantum state with the fused carrier while leaving `rho_AB` unchanged. It does **not** claim a physical dynamical map has acted on the quantum state.

### D4-08 — Conditional native fused Hilbert lift
A native fused quantum state is typed only if additional structure supplies a Hilbert space `H_F` and an isometric encoding

\[
V_F:\mathcal H_{AB}\to\mathcal H_F,
\qquad V_F^\dagger V_F=I_{AB}.
\]

Then

\[
|F_{xy}\rangle:=V_F|xy\rangle
\]

and

\[
|\Phi_F\rangle
=\sum_{xy}c_{xy}|F_{xy}\rangle
\]

is a valid fused-output superposition. `V_F` is a **candidate extra structure**, not derived from the quotient alone.

### D4-09 — Measurement/readout
For quantum POVM `{E_m}` and structural readout/projection `P_r`, define

\[
\Pr(m)=\operatorname{Tr}(\rho E_m),
\]

and the combined observable report

\[
\mathcal R_{r,E}(\widehat F)
=\bigl(P_r(Q),\{\operatorname{Tr}(\rho E_m)\}_m\bigr).
\]

The carrier, quantum state, and readout are distinct typed objects.

### D4-10 — Superposition support
For basis `B={|b_k>}`, define

\[
\mathrm{Supp}_B(|\psi\rangle)=\{k:c_k\neq0\}.
\]

Support size greater than one is necessary for basis-superposition of a pure state, but coherent phase information is carried by the amplitudes, not by support alone.
