# R04 — Superposition Structure
## Closed work-layer report

**Run:** R04 / 10  
**Verdict:** CLOSED  
**Classification:** SUPERPOSITION IS A QUANTUM-STATE-LAYER PROPERTY; CURRENT QUOTIENT FUSION DOES NOT ITSELF GENERATE IT  
**Next:** R05 — Null-Interface Algebra

# Executive result

R04 answers the roadmap question **"what exactly is superposed after Fusion?"** with a type-separated result.

The current R01/R02 Fusion Operator creates a structural quotient carrier `Q`. It does not itself create Hilbert linearity, complex amplitudes, normalization, or phase. Therefore **Fusion is not the superposition operation**.

The supplied 4.3 source independently supports a one-chirality-degree Hilbert space and an equal chirality creation superposition. R03 supplied an explicit two-copy diagnostic lift. On that lift, the object that may be superposed is the **quantum chirality state**: for example the joint alternatives `LR` and `RL` in

\[
|\Psi_\phi\rangle=(|LR\rangle+e^{i\phi}|RL\rangle)/\sqrt2.
\]

After structural Fusion, the minimum type-safe construction is a hybrid record

\[
\widehat F=(Q,\eta_F,\mathrm{Inv}_F,W_{AB},\rho_{AB}),
\]

which retains the quantum state and its factor registry beside the fused carrier. This bookkeeping lift preserves the stored amplitudes and relative phase because it leaves `rho_AB` unchanged; it does **not** prove a physical coherence-preserving Fusion dynamics.

A genuine native fused state

\[
|\Phi_F\rangle=\alpha|F_1\rangle+\beta e^{i\phi}|F_2\rangle
\]

is mathematically valid only if a later derivation supplies a fused Hilbert space `H_F` and an isometric encoding `V_F:H_AB->H_F`. The current quotient does not supply them.

The recovered old sketch is therefore classified at R04 as a **carrier/gluing diagram with an interface marker**, not a complete quantum-state diagram. It can host or motivate a quantum lift, but the amplitudes, phase, inner product, and measurement rule are additional typed structure.

Finally, R04 proves that a simple chirality-basis readout can hide coherence: the Bell-like coherent state and the incoherent anti-correlated mixture both give 50/50 `LR/RL` populations. An interference-sensitive basis reveals the relative phase through

\[
P(B_+)=(1+\cos\phi)/2,\qquad
P(B_-)=(1-\cos\phi)/2.
\]

Thus state, carrier, and readout are now explicitly separated before R05 attacks the null-interface algebra.

---

# R04 — Input Ledger
## Superposition Structure

**Run:** R04 / 10  
**Dependency:** R03 CLOSED  
**Question:** What exactly is superposed after Fusion?

## Authorized inherited premises

### I4-01 — R01/R02 carrier Fusion [DERIVED / CLOSED]
The active structural operator forms the decorated quotient carrier

\[
Q=(A\sqcup B)/(a_\star\sim b_\star),
\]

with one shared interface locus `q`, injective source images `A_F` and `B_F`, tagged Fusion relation/provenance `eta_F`, and fused invariant/provenance record `Inv_F`.

### I4-02 — R02 subsystem result [DERIVED / CLOSED]
The current operator is weak quotient Fusion: source images remain recoverable and overlap at `q`, but the quotient itself supplies no native independent product/tensor decomposition.

### I4-03 — R03 quantum diagnostic lift [DERIVED / CLOSED]
For two chirality degrees of freedom, R03 licensed

\[
\mathcal H_A=\operatorname{span}\{|L\rangle_A,|R\rangle_A\},\qquad
\mathcal H_B=\operatorname{span}\{|L\rangle_B,|R\rangle_B\},
\]

and

\[
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B.
\]

This is an auxiliary quantum factor registry, not a theorem that bare `Q` factorizes.

### I4-04 — MK43 4.3 single-mote superposition [SOURCE]
The supplied 4.3 canonical source defines

\[
\mathcal H_{\mathrm{mote}}=\operatorname{span}\{|+\rangle,|-\rangle\}
\]

and the Genesis creation relation

\[
\hat G^\dagger|\Omega\rangle
=\frac{|+\rangle+|-\rangle}{\sqrt2}.
\]

Thus a normalized single-chirality superposition is source-licensed. R04 keeps abstract `L/R` basis names to avoid silently resolving the known sign/orientation naming conflict.

### I4-05 — R03 entanglement boundary [DERIVED / CLOSED]
Entanglement and Fusion are logically independent. The same carrier `Q` may support separable or entangled quantum decorations. Quantum phase belongs to the state layer unless independently related to route holonomy in R09.

### I4-06 — Projection/readout discipline [SOURCE]
The corridor source distinguishes inherited organization, chirality, invariant residue, Resolution, Bandwidth, closure, and projected expression. R04 therefore separates underlying quantum state from structural carrier and from readout.

## Prohibited assumptions

R04 may not assume:
- a native fused Hilbert space `H_F` already exists;
- structural quotient/gluing generates quantum coherence;
- the old sketch encodes amplitudes or phase;
- matrix/occupancy overlay is coherent superposition;
- entanglement is required for superposition;
- a density mixture is a coherent superposition merely because it has the same chirality populations;
- the relative phase `phi` is holonomy;
- a measurement/readout result is the state itself;
- the fusion carrier `Q` uniquely fixes a quantum state.

---
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

---
# R04 — Derivation Ledger
## Superposition Structure

# 1. Superposition is basis-relative

The phrase "the object is superposed" is incomplete unless a basis/decomposition is specified. Any normalized pure state can itself be chosen as one vector of some orthonormal basis, so superposition is not an intrinsic binary label detached from representation.

R04 therefore fixes the **chirality eigenbasis** as the physically relevant basis inherited from the source two-state chirality sector. This makes `L/R` superposition typed rather than rhetorical.

# 2. Single-seed superposition is already source-supported

The supplied 4.3 source provides a two-dimensional chirality Hilbert space and an equal creation superposition. Abstracting only the unresolved sign/name mapping gives

\[
|s\rangle=\frac{|L\rangle+|R\rangle}{\sqrt2}.
\]

This is a superposition of two **chirality eigenstates of one seed/mote degree of freedom**.

It is not a fusion of two carrier objects.

# 3. Two-seed superposition belongs to the joint quantum state

On

\[
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B,
\]

a general joint state is

\[
|\psi_{AB}\rangle=
 c_{LL}|LL\rangle+c_{LR}|LR\rangle+c_{RL}|RL\rangle+c_{RR}|RR\rangle.
\]

This immediately separates three questions:

1. **What are the alternatives?** The product-basis states with nonzero coefficients.
2. **Are the alternatives coherent?** Inspect relative amplitudes/off-diagonal density terms.
3. **Is the state entangled?** Apply the R03 factorability criterion.

Therefore superposition and entanglement are not synonyms. A product state such as

\[
|s\rangle_A\otimes|s\rangle_B
=\frac12(|LL\rangle+|LR\rangle+|RL\rangle+|RR\rangle)
\]

is highly superposed in the joint chirality basis but separable.

# 4. The Bell-like state is a superposition of JOINT alternatives

R03's reference state

\[
|\Psi_\phi\rangle
=\frac{|LR\rangle+e^{i\phi}|RL\rangle}{\sqrt2}
\]

is precisely a coherent superposition of the **two joint alternatives** `LR` and `RL`. Its entanglement follows from nonfactorizability, not merely from the fact that two terms appear.

Its density operator is

\[
\rho_\phi=\frac12\Bigl(
|LR\rangle\langle LR|+|RL\rangle\langle RL|
+e^{-i\phi}|LR\rangle\langle RL|
+e^{i\phi}|RL\rangle\langle LR|
\Bigr).
\]

The off-diagonal terms are the chirality-basis coherence terms.

# 5. Same populations do not establish superposition

The incoherent anti-correlated mixture

\[
\rho_{\rm cl}=\frac12|LR\rangle\langle LR|+\frac12|RL\rangle\langle RL|
\]

has exactly the same chirality-basis outcome probabilities as `rho_phi`:

\[
P(LR)=P(RL)=\frac12.
\]

Yet it lacks the coherence terms. Therefore a readout that only reports `LR/RL` populations cannot distinguish coherent superposition from a classical mixture.

# 6. Interference-sensitive readout exposes relative phase

Define

\[
|B_+\rangle=\frac{|LR\rangle+|RL\rangle}{\sqrt2},\qquad
|B_-\rangle=\frac{|LR\rangle-|RL\rangle}{\sqrt2}.
\]

For `|Psi_phi>`:

\[
P(B_+)=|\langle B_+|\Psi_\phi\rangle|^2
=\frac{1+\cos\phi}{2},
\]

\[
P(B_-)=\frac{1-\cos\phi}{2}.
\]

So relative phase can be hidden from a chirality-population readout yet visible in an interference-sensitive basis. This is why R04 must keep **state** and **readout** separate.

Nothing in this derivation identifies `phi` with route holonomy. R09 retains that obligation.

# 7. Structural Fusion does not generate quantum superposition

The R01/R02 map

\[
(A,B)\mapsto Q
\]

is a quotient/gluing construction. It has no addition law, complex scalar multiplication, inner product, normalization rule, or phase structure. Therefore the quotient operation alone cannot establish a Hilbert superposition.

A simple proof by countermodel is enough: take the same admissible carrier pair and decorate it with the product basis state `|LR>`. Fusion produces the same structural `Q`, yet the quantum decoration contains no superposition in the joint chirality basis. Hence

\[
\mathrm{Fusion}\not\Rightarrow\mathrm{Superposition}.
\]

Conversely a single seed can already be in the 4.3 source superposition without any two-carrier Fusion, so

\[
\mathrm{Superposition}\not\Rightarrow\mathrm{Fusion}.
\]

# 8. What survives the current Fusion operation

The minimal type-safe construction is not a new fused Hilbert space. It is the hybrid object

\[
\widehat F
=(Q,\eta_F,\mathrm{Inv}_F,W_{AB},\rho_{AB}),
\]

where `rho_AB` is carried alongside the newly fused structural carrier.

Under the minimal decoration lift

\[
\mathfrak F_{\rm dec},
\]

the state is unchanged. Therefore every pre-existing amplitude and relative phase in `rho_AB` is preserved **by definition of the bookkeeping lift**, not because the quotient has dynamically protected coherence.

This distinction prevents an accounting identity from being mistaken for a physical coherence theorem.

# 9. Can we define a genuine fused-output superposition?

Conditionally, yes.

If later mathematics supplies a native fused Hilbert space and an isometry

\[
V_F:\mathcal H_{AB}\to\mathcal H_F,
\]
then the joint basis pushes forward to

\[
|F_{LL}\rangle,|F_{LR}\rangle,|F_{RL}\rangle,|F_{RR}\rangle,
\]

and

\[
|\Phi_F\rangle=\sum_{xy}c_{xy}|F_{xy}\rangle
\]

is normalized because

\[
\langle\Phi_F|\Phi_F\rangle
=\langle\psi_{AB}|V_F^\dagger V_F|\psi_{AB}\rangle=1.
\]

For the two-term case required by the roadmap,

\[
|\Phi_F\rangle
=\alpha|F_1\rangle+\beta e^{i\phi}|F_2\rangle,
\qquad |\alpha|^2+|\beta|^2=1
\]

when `|F_1>,|F_2>` are orthonormal.

But the quotient construction does **not** supply `H_F` or `V_F`. Therefore R04 licenses this only as a **conditional fused-Hilbert lift**, not as an established property of the current Fusion Operator.

# 10. The old diagram is not a complete quantum-state diagram

The recovered sketch supplies visible structural information: two chirality-seed-like organizations, an interface, and a marked central relation/locus. It does not visibly provide:

- complex amplitudes;
- normalization;
- relative phase;
- an inner product;
- a declared Hilbert basis;
- a density operator;
- a measurement rule.

Therefore the sketch cannot, by itself, uniquely specify a coherent quantum state.

The best-supported classification at R04 is:

\[
\boxed{\text{carrier/gluing diagram with an interface marker}}
\]

possibly accompanied by a **readout/annotation convention** whose original semantics remain partly unrecovered.

It may serve as the geometric carrier on which a quantum state is later placed, but the quantum state is extra typed data.

# 11. Fusion-channel superposition is a separate unlicensed object

One might write

\[
\alpha|\text{fuse at }q_1\rangle+\beta|\text{fuse at }q_2\rangle.
\]

This would be a superposition of **operator channels or structural outcomes**, not of chirality eigenstates. It requires a Hilbert space whose basis consists of Fusion channels/outcomes and a quantum operation mapping into it. No such structure has yet been derived.

R04 therefore records Fusion-channel superposition as **UNRESOLVED / NOT CURRENTLY TYPED**.

# 12. Complete typed map

The current closed map is:

```text
chirality basis
    |
    v
single-seed or joint Hilbert state
    |    amplitudes + normalization + relative phase live here
    v
structural Fusion admissibility witness
    |
    v
quotient carrier Q + Fusion provenance eta_F
    |
    +---- retain W_AB and rho_AB ----> hybrid fused quantum object
    |                                    (no native H_F implied)
    v
structural projection P_r          quantum POVM {E_m}
    \                                  /
     \                                /
      ---------- readout ------------
```

Symbolically:

\[
\mathcal B_{AB}
\longrightarrow
\rho_{AB}
\xrightarrow{\;\mathfrak F_{\rm dec}\;}
(Q,\eta_F,\mathrm{Inv}_F,W_{AB},\rho_{AB})
\xrightarrow{\;\mathcal R_{r,E}\;}
\bigl(P_r(Q),\{\operatorname{Tr}(\rho E_m)\}_m\bigr).
\]

This satisfies the roadmap's required basis → joint state → Fusion → fused state → readout chain without pretending that the quotient itself is a Hilbert-space superposition operator.

---
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

---
# R04 — Superposition / Readout Decision Table

| Object / operation | Has Hilbert linearity? | Can contain chirality-basis superposition? | Does it prove entanglement? | Does it prove Fusion? | R04 status |
|---|---:|---:|---:|---:|---|
| One-seed state `alpha|L>+beta|R>` | yes | yes | no | no | SOURCE-LICENSED TYPE |
| Joint product state `|s>_A⊗|s>_B` | yes | yes | no | no | DERIVED |
| Bell-like `(|LR>+e^{iphi}|RL>)/sqrt2` | yes | yes | yes, by R03 nonfactorability | no | DERIVED |
| Classical `LR/RL` mixture | density-state formalism, but incoherent in this basis | no coherent superposition | no | no | DERIVED |
| Bare quotient carrier `Q` | no | not typed | no | yes, structurally | CLOSED STRUCTURAL |
| Hybrid `(Q,...,W_AB,rho_AB)` | quantum state retained as decoration | according to `rho_AB` | according to `rho_AB` | yes | CLOSED HYBRID TYPE |
| Native fused Hilbert state `V_F|psi>` | conditionally yes | conditionally yes | depends on retained factorization | yes | CANDIDATE / EXTRA STRUCTURE |
| Fusion-channel superposition | not yet supplied | untyped | untyped | untyped | UNRESOLVED |
| Old hand sketch | no explicit Hilbert data | cannot establish it alone | no | supports structural hypothesis only | CARRIER/GLUING DIAGRAM |

---
# R04 — Vera Audit
## Superposition Structure

**Audit verdict:** PASS / CLOSED.

### 1. Conclusion-as-premise check
PASS. R04 did not assume a fused Hilbert space in order to prove a fused Hilbert state. It explicitly left `H_F,V_F` conditional.

### 2. Terminology check
PASS. "Superposition" is used only after a basis, complex amplitudes, normalization, and coherence structure are declared.

### 3. Overlay check
PASS. Geometric/occupancy overlay is explicitly rejected as proof of coherent superposition.

### 4. Mixture/coherence check
PASS. The Bell-like pure state and the anti-correlated mixture are separated by off-diagonal coherence and interference-sensitive readout.

### 5. Entanglement firewall
PASS. Superposition is not equated with entanglement; the separable four-term product state is an explicit counterexample.

### 6. Fusion firewall
PASS. Structural Fusion and quantum superposition are logically independent; the same `Q` can carry multiple quantum states.

### 7. State/readout firewall
PASS. `rho` and measurement probabilities are separate typed objects. Chirality-basis readout is shown to hide relative phase that an interference basis can reveal.

### 8. Holonomy firewall
PASS. `phi` remains a quantum relative-phase parameter only. R09 retains the question whether a route can generate/encode such a phase.

### 9. Old-sketch provenance check
PASS. The recovered drawing is classified as a carrier/gluing diagram with interface marker, not retroactively labeled a complete Hilbert-state diagram.

### 10. Anti-recursion check
PASS. Each section contributes a distinct object, proof, counterexample, or type boundary; no conclusion is obtained by repeated restatement.

### 11. Falsifiability
The current R04 classification would need revision if an authenticated source or later derivation provides a canonical native `H_F` and quantum Fusion operator from the quotient construction itself. In that case the conditional `V_F` layer could be promoted and tested directly.

---
# R04 — Exit Verdict

**Run:** R04 — Superposition Structure  
**Verdict:** **CLOSED**  
**Classification:** **SUPERPOSITION IS A QUANTUM-STATE-LAYER PROPERTY; CURRENT QUOTIENT FUSION DOES NOT ITSELF GENERATE IT**

R04 closes with the following licensed results:

1. Single-seed chirality superposition is source-supported by the 4.3 two-state mote Hilbert sector.
2. On the R03 two-seed lift, superposition is defined relative to the joint chirality basis `LL,LR,RL,RR` with complex amplitudes and normalization.
3. The Bell-like entangled state is a coherent superposition of the **joint alternatives** `LR` and `RL`; its entanglement is a separate R03 property.
4. The current structural Fusion map does not supply Hilbert linearity and therefore does not itself establish quantum superposition.
5. The minimal type-safe post-Fusion object retains `rho_AB` and factor registry `W_AB` alongside the quotient carrier. Under this bookkeeping lift, amplitudes and phase are carried forward but not dynamically proved protected.
6. A native fused-output superposition `|Phi_F>` is valid only conditionally on additional `H_F` and isometric encoding `V_F`; those are not derived from the quotient.
7. The old sketch is best classified as a carrier/gluing diagram with interface marker, not a complete quantum-state diagram.
8. Readout is distinct from state. Chirality populations can hide coherence/relative phase; an interference-sensitive basis can reveal it.
9. Fusion-channel superposition remains untyped/unresolved.

**Next:** R05 — Null-Interface Algebra.

---
# R04 — Carry-Forward Packet
## Licensed inputs for R05

R05 may inherit:

- `Q=(A disjoint_union B)/(a*~b*)` as the current closed quotient Fusion carrier.
- `A_F,B_F` as recoverable overlapping source images, with `A_F cap B_F={q}`.
- the hybrid object `(Q,eta_F,Inv_F,W_AB,rho_AB)` as a type-safe way to retain an auxiliary quantum state without claiming a native fused Hilbert space.
- superposition as basis-relative Hilbert-state structure with complex amplitudes, normalization, and relative phase.
- the source-supported single-seed chirality superposition.
- the derived joint chirality basis and Bell-like reference state.
- `Fusion !-> Superposition` and `Superposition !-> Fusion` for the current operator.
- the old sketch as structural carrier/gluing evidence only, not as proof of amplitudes/phase.

R05 may **not** inherit as proved:

- a native fused Hilbert space `H_F`;
- a quantum Fusion dynamics;
- Fusion-channel superposition;
- factor erasure;
- chirality conservation;
- reversibility;
- a phase-holonomy identity;
- physical realization.

### R05 active question
What minimum algebraic structure distinguishes two addressable null loci while preserving the uniqueness and emptiness of `∅`, and what is the preferred null-interface construction for Fusion?
