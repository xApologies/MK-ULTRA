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
