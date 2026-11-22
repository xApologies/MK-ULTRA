# VOLUME IV - HELICON

## Chapter 34 - Structural Tuple and One-Form Representations

### 34.1 The recovered structural tuple

The tuple formulation is preserved exactly as

\[
H=(L,\Omega_H,C_H,W_H).
\tag{34.1}
\]

Equation (34.1) is `EXACT_RECOVERED_EQUATION` `hel-eq-01`, from source unit `unit_11f9b725cc0530b3db72c328c726c02685e4fc30b4fd5d439012d0a9f3470c19`. It presents a Helicon quantity as a four-component structural object. The exact source does not, by this line alone, supply universal types for all four components.

Library 4.1 assigns `@helicon_structural_tuple`. The handle is `DECLARED` with `MEDIUM` calibrated coverage and participates in one `REPRESENTED_BY` and one `REPRESENTS` relation. The edge typing supports a representation relation rather than whole-object identity.

### 34.2 Tuple projections

For a product object, component projections have the conventional form

\[
\pi_L(H)=L,\quad
\pi_\Omega(H)=\Omega_H,\quad
\pi_C(H)=C_H,\quad
\pi_W(H)=W_H.
\tag{34.2}
\]

Equation (34.2) is `EXTERNAL_ESTABLISHED_MATHEMATICS`. It explains how tuple components may be addressed once the product types are supplied. It does not assert that the recovered source explicitly defines these four maps.

### 34.3 The recovered one-form

A distinct exact representation is

\[
\mathcal{H}(x)=H_i(x)\,dx^i.
\tag{34.3}
\]

Equation (34.3) is `EXACT_RECOVERED_EQUATION` `hel-eq-06`, from source unit `unit_e66d83785edbf4be8bed30fccbf347c0d75728c0b53253afe88f4832ef1c851d`. Here \(H_i\) are explicitly one-form components. The calligraphic one-form remains scope-distinct from the tuple \(H\).

### 34.4 Coordinate transformation

For a genuine one-form under a coordinate change \(x^i\mapsto x^{i'}\), components transform as

\[
H_{i'}=\frac{\partial x^i}{\partial x^{i'}}H_i.
\tag{34.4}
\]

Equation (34.4) is `EXTERNAL_ESTABLISHED_MATHEMATICS`. A framework source must identify the underlying manifold and chart structure before this law can be applied as more than a conventional typing criterion.

### 34.5 Recovered curvature

The exact one-form source defines

\[
\mathcal{F}_{ij}=\partial_iH_j-\partial_jH_i.
\tag{34.5}
\]

Equation (34.5) is `EXACT_RECOVERED_EQUATION` `hel-eq-07`. It supplies the antisymmetric derivative associated with the one-form representation. This is a scoped field-strength construction, not a complete identity for every Helicon formulation.

### 34.6 Exterior-derivative identity

Writing \(\mathcal{F}=d\mathcal{H}\), the nilpotence of the exterior derivative gives

\[
d\mathcal{F}=d^2\mathcal{H}=0.
\tag{34.6}
\]

Equation (34.6) is `EXTERNAL_ESTABLISHED_MATHEMATICS`. The identity follows when \(\mathcal{H}\) is a sufficiently regular differential one-form. It is not a recovered Helicon field equation or equation of motion.

### 34.7 Line integration

A one-form naturally pairs with a curve \(\gamma\):

\[
\int_\gamma\mathcal{H}
=\int_a^b H_i(\gamma(t))\,\dot\gamma^i(t)\,dt.
\tag{34.7}
\]

Equation (34.7) is `EXTERNAL_ESTABLISHED_MATHEMATICS`. It shows how a one-form can generate a path-dependent quantity, but the recovered sources must specify whether such an integral has a Helicon interpretation.

### 34.8 Representation map

The relation between tuple and one-form descriptions is recorded conservatively as a candidate map

\[
\rho_{1}:\mathcal{D}_{\rho_1}\subseteq\mathcal{X}_{\mathrm{tuple}}
\longrightarrow\Omega^1(M).
\tag{34.8}
\]

Equation (34.8) is `CLOVER_SYNTHESIS`. Neither the domain, component dictionary, nor inverse is recovered as a universal construction. The map therefore remains a typing requirement rather than a completed equivalence.

### 34.9 No silent identification

The current notation ruling requires

\[
H_{\mathrm{tuple}}\neq
\mathcal{H}_{\mathrm{one\text{-}form}}
\quad\text{as persistent identity records}.
\tag{34.9}
\]

Equation (34.9) is `CLOVER_SYNTHESIS`. The inequality protects record identity. It does not assert that the representations can never be related; it asserts that any relation must be explicit, typed, and provenanced.

### 34.10 Tagged representation space

Until a common state space is constructed, the recovered forms can be held in a tagged sum

\[
\mathcal{X}_{H}=\mathcal{X}_{\mathrm{tuple}}
\sqcup\Omega^1(M)\sqcup
\mathcal{X}_{\mathrm{configuration}}
\sqcup\mathcal{X}_{\mathrm{triadic}}.
\tag{34.10}
\]

Equation (34.10) is `EXTERNAL_ESTABLISHED_MATHEMATICS` as a disjoint-union construction. The tags prevent cross-scope symbol reuse from becoming a false equivalence.

### 34.11 Reconstruction obligation

A reversible correspondence would require maps satisfying

\[
\rho_{1}^{-1}\circ\rho_{1}=I
\quad\text{on }\mathcal{D}_{\rho_1}.
\tag{34.11}
\]

Equation (34.11) is `CLOVER_SYNTHESIS` as an unresolved obligation. No universal inverse has been recovered. The incomplete inverse dictionary remains a separate high-priority mathematical-development lane.

### 34.12 Representation dependencies

Each representation carries its own dependency block:

\[
\operatorname{Deps}(\rho)=
(\operatorname{Carrier},\operatorname{Coordinates},
\operatorname{Operators},\operatorname{Units},\operatorname{Provenance}).
\tag{34.12}
\]

Equation (34.12) is `CLOVER_SYNTHESIS`. A missing carrier or operator type remains visible rather than being supplied from a neighboring source.

### 34.13 Recovered spectral pairing

The one-form formulation continues into the exact pairing

\[
\Gamma_n(x)=\langle\nabla\Psi_n,\mathcal{R}H\rangle.
\tag{34.13}
\]

Equation (34.13) is `EXACT_RECOVERED_EQUATION` `hel-eq-08`. Its use of \(H\) must be read in its own source scope. The expression does not retroactively identify the symbol with every tuple or configuration record.

### 34.14 Recovered wake dynamics

The same source window gives

\[
\frac{dW}{dt}=-\alpha\Gamma_{\mathrm{tot}}
-\beta\nabla\Psi\cdot H.
\tag{34.14}
\]

Equation (34.14) is `EXACT_RECOVERED_EQUATION` `hel-eq-10`. The appearance of \(W\) provides a structural correspondence with the tuple's \(W_H\) only as a candidate until the equality, units, and map are explicitly established.

### 34.15 Version-scoped notation

The live model stores notation with a source and version index:

\[
\operatorname{Meaning}(H)=
\operatorname{Meaning}(H\mid s,\nu,\rho).
\tag{34.15}
\]

Equation (34.15) is `CLOVER_SYNTHESIS`. Historical quasi-particle, one-form, tuple, configuration-space, and triadic uses remain separately recoverable.

### 34.16 Status of the native address

The calibrated handle summary is

\[
\operatorname{Status}(@\mathrm{helicon\_structural\_tuple})
=\mathrm{DECLARED}+\mathrm{MEDIUM}.
\tag{34.16}
\]

Equation (34.16) is `CLOVER_SYNTHESIS`. Library 4.1 reports 2,677 unique substantive units across 88 source hashes, with 31 English units, 6 equation units, 2 registered dependencies, and 4 provenance units. It recovers no exact-definition unit and no theorem/proof unit under this address.

### 34.17 Library 4.1 native evidence register

The generated register records the assigned structural-tuple address and its representation-edge neighborhood.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@helicon_structural_tuple` | @helicon_structural_tuple | MEDIUM | 31 / 6 / 2 | chapter-core object |

### 34.18 Representation validity

A Helicon representation is publication-valid when

\[
\operatorname{Valid}(\rho)=
\operatorname{ScopeTagged}(\rho)\land
\operatorname{CarrierTyped}(\rho)\land
\operatorname{EquationsProvenanced}(\rho)\land
\operatorname{IdentityDistinct}(\rho).
\tag{34.17}
\]

Equation (34.17) is `CLOVER_SYNTHESIS`.

The current relation path is

\[
\text{structural tuple}\to\text{explicit representation edge}
\to\text{one-form candidate map}\to\text{curvature and coupling}.
\tag{34.18}
\]

Equation (34.18) is `CLOVER_SYNTHESIS`. The chapter preserves two mathematically useful representations while refusing to manufacture the common typed state space or inverse dictionary still required to unify them.
