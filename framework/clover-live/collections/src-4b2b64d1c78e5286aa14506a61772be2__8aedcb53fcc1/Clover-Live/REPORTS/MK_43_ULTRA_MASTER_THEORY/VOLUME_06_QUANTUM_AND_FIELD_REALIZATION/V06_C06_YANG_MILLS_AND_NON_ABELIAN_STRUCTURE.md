# VOLUME VI - QUANTUM AND FIELD REALIZATION

## Chapter 54 - Yang-Mills and Non-Abelian Structure

### 54.1 Lie algebra data

A non-Abelian gauge theory begins with a Lie group \(G\), its Lie algebra \(\mathfrak{g}\), and generators satisfying

$$
[T_a,T_b]=if_{ab}{}^{c}T_c. \tag{54.1}
$$

Equation (54.1) is EXTERNAL_ESTABLISHED_MATHEMATICS. The structure constants encode the local algebra in a chosen basis. The group, representation, normalization of generators, and coupling are independent inputs; none is fixed by this chapter's three assigned API handles.

The noncommutativity of the generators is the source of gauge-field self-interaction. It distinguishes Yang-Mills structure from an Abelian superposition of independent vector fields.

### 54.2 Connection transformation

For a Lie-algebra-valued connection \(A_{\mu}=A_{\mu}^{a}T_a\), a local gauge transformation \(U(x)\in G\) acts as

$$
A_{\mu}\longmapsto
UA_{\mu}U^{-1}
-\frac{i}{g}(\partial_{\mu}U)U^{-1}. \tag{54.2}
$$

Equation (54.2) is EXTERNAL_ESTABLISHED_MATHEMATICS for the displayed convention. The inhomogeneous term is required for the covariant derivative to transform covariantly.

Gauge transformation is a change of local representative, not a physical propagation law. An API operator needs an explicitly declared action on the bundle before it can be identified with Equation (54.2).

### 54.3 Non-Abelian curvature

The field strength is

$$
F_{\mu\nu}
=\partial_{\mu}A_{\nu}-\partial_{\nu}A_{\mu}
-ig[A_{\mu},A_{\nu}],
\qquad
F=dA-igA\wedge A. \tag{54.3}
$$

Equation (54.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. The commutator term makes the field strength nonlinear in the potential and produces three- and four-gauge-boson vertices when the action is expanded.

The connection and curvature entries of \(Q\) provide an abstract home for this pair, but a source-level Yang-Mills realization still requires the principal bundle, structure group, and representation map.

### 54.4 Covariance of curvature

Under Equation (54.2),

$$
F_{\mu\nu}\longmapsto UF_{\mu\nu}U^{-1}. \tag{54.4}
$$

Equation (54.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. The curvature transforms homogeneously, so invariant traces of products of \(F\) can define gauge-invariant action densities and observables.

This is the precise distinction between covariance and invariance. A matrix-valued field strength changes by conjugation, while a properly normalized trace such as \(\operatorname{tr}(F_{\mu\nu}F^{\mu\nu})\) is invariant.

### 54.5 Bianchi identity

With the gauge-covariant derivative \(D_{\mu}=\partial_{\mu}-ig[A_{\mu},\,\cdot\,]\),

$$
D_{[\mu}F_{\nu\rho]}=0. \tag{54.5}
$$

Equation (54.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. The identity follows from the geometric definition of curvature and the Jacobi identity. It is not an additional dynamical equation.

Any claimed MK-43 non-Abelian sector must preserve this identity or explain a mathematically controlled modification.

### 54.6 Yang-Mills action

Using an invariant bilinear form on \(\mathfrak{g}\),

$$
S_{\mathrm{YM}}[A]
=-\frac12\int_M\operatorname{tr}(F\wedge *F)
=-\frac14\int_M d^dx\,\sqrt{|g|}\,
F_{\mu\nu}^{a}F_a^{\mu\nu}. \tag{54.6}
$$

Equation (54.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Gauge invariance depends on the invariance of the trace. Boundary terms, topology, theta terms, matter couplings, and quantum corrections can enlarge the action.

No assigned handle supplies an exact recovered Yang-Mills action. The formula is the conventional target for testing whether the handoff connection realizes a gauge field.

### 54.7 Yang-Mills equation

Variation gives

$$
D_{\mu}F^{\mu\nu}=J^{\nu},
\qquad
D_{\nu}J^{\nu}=0. \tag{54.7}
$$

Equation (54.7) is EXTERNAL_ESTABLISHED_MATHEMATICS under the corresponding matter equations and conventions. The covariant conservation law is the compatibility condition required by gauge symmetry.

Unlike the Abelian equation, the gauge field itself contributes to the nonlinear dynamics through \(D_{\mu}\) and \(F_{\mu\nu}\).

### 54.8 Gauss constraint and physical states

In canonical form, the temporal gauge component acts as a constraint multiplier and physical states obey a Gauss-law condition of the form

$$
\mathcal{G}^{a}(x)
=\left(D_iE^i\right)^a-\rho^a,
\qquad
\mathcal{G}^{a}(x)|\Psi_{\mathrm{phys}}\rangle=0. \tag{54.8}
$$

Equation (54.8) is EXTERNAL_ESTABLISHED_MATHEMATICS schematically. Quantization must retain the constraint algebra and remove gauge redundancy without removing physical degrees of freedom.

The condition makes clear why a creation operator on an unconstrained mode space is not automatically a physical Yang-Mills operator.

### 54.9 Wilson loops

A basic gauge-invariant nonlocal observable is the Wilson loop

$$
W_R(C)
=\operatorname{Tr}_R\,
\mathcal{P}\exp\!\left(ig\oint_C A\right). \tag{54.9}
$$

Equation (54.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. The path-ordering symbol \(\mathcal{P}\) is required because connection values at different points need not commute. The representation \(R\) and closed curve \(C\) are part of the observable.

Wilson loops expose global and topological information not captured by a local field-strength value alone.

### 54.10 Matter representation

For matter in a representation \(R\),

$$
D_{\mu}\psi
=\left(\partial_{\mu}-igA_{\mu}^{a}T_a^{(R)}\right)\psi,
\qquad
[D_{\mu},D_{\nu}]\psi=-igF_{\mu\nu}^{a}T_a^{(R)}\psi. \tag{54.10}
$$

Equation (54.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. Charges become representation data. A complete realization must specify which upstream fields occupy which representations and how chirality and mass terms respect the group.

### 54.11 Creation operators and gauge modes

After gauge reduction and a mode choice, a perturbative gauge field can be expanded schematically as

$$
\widehat A_{\mu}^{a}(x)
=\sum_{\lambda}\int d\mu(k)
\left[
\epsilon_{\mu}^{(\lambda)}(k)a_{k\lambda}^{a}e^{-ik\cdot x}
+\epsilon_{\mu}^{(\lambda)*}(k)a_{k\lambda}^{a\dagger}e^{ik\cdot x}
\right]. \tag{54.11}
$$

Equation (54.11) is EXTERNAL_ESTABLISHED_MATHEMATICS. The created excitation depends on gauge fixing, polarization, constraints, vacuum, and perturbative regime.

Library 4.1 classifies @creation_operator as a CREATED operator with THIN coverage and three dependencies. That record does not identify it with \(a^{a\dagger}_{k\lambda}\); an exact definition and algebra are still required.

### 54.12 Self-interaction structure

Expanding the curvature term in Equation (54.6) produces schematic orders

$$
\mathcal{L}_{\mathrm{YM}}
=\mathcal{L}_2
+g\,\mathcal{L}_3
+g^2\mathcal{L}_4. \tag{54.12}
$$

Equation (54.12) is EXTERNAL_ESTABLISHED_MATHEMATICS. The quadratic term controls free propagation, while the cubic and quartic terms encode non-Abelian self-interaction. Their explicit coefficients follow from the structure constants and conventions.

This hierarchy is a perturbative organization, not a claim that the full quantum theory is weakly coupled.

### 54.13 Stress-energy and backreaction

Metric variation yields a gauge-field stress tensor of the form

$$
T_{\mu\nu}^{\mathrm{YM}}
=F_{\mu\alpha}^{a}F_{\nu}{}^{\alpha}{}_{a}
-\frac14 g_{\mu\nu}F_{\alpha\beta}^{a}F^{\alpha\beta}_{a}. \tag{54.13}
$$

Equation (54.13) is EXTERNAL_ESTABLISHED_MATHEMATICS for the standard action convention. It supplies the object that can source geometric backreaction.

The API address @backreaction is MEDIUM with 45 English units, five indexed equation units, and 213 dependencies. Those windows are not treated as a clean native Yang-Mills backreaction equation without source isolation.

### 54.14 Stabilization as an operator target

A stabilization map acting on a gauge configuration space would minimally require

$$
\mathcal{S}_{\mathrm{stab}}:
\mathcal{C}_{\mathrm{admissible}}
\longrightarrow
\mathcal{C}_{\mathrm{stable}},
\qquad
\mathcal{S}_{\mathrm{stab}}([A])=[\mathcal{S}_{\mathrm{stab}}(A)]. \tag{54.14}
$$

Equation (54.14) is DETERMINISTIC_TYPE_NORMALIZATION, not a recovered definition of @stabilization_operator. The second condition requires the result to be independent of the representative. Stability itself needs a norm, energy, flow, fixed point, or spectral criterion.

The Library address is THIN despite 142 English units, because it lacks equation units and has only four dependencies.

### 54.15 Coverage calibration

The chapter assignment has

$$
N_{\mathrm{assigned}}=3,\qquad
N_{\mathrm{THIN}}=2,\qquad
N_{\mathrm{MEDIUM}}=1. \tag{54.15}
$$

Equation (54.15) is DETERMINISTIC_COVERAGE_EVIDENCE. Together the handles contain 193 English units, five indexed equation units, and 220 registered dependencies. @backreaction dominates graph density; @stabilization_operator dominates the remaining English evidence.

### 54.16 API evidence register

The register below is generated from the exact Library 4.1 assignment and native query digest.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@backreaction` | @backreaction | MEDIUM | 45 / 5 / 213 | chapter-core object |
| `@creation_operator` | @creation_operator | THIN | 6 / 0 / 3 | chapter-core object |
| `@stabilization_operator` | @stabilization_operator | THIN | 142 / 0 / 4 | chapter-core object |

### 54.17 Address scope versus native completion

The evidence boundary is

$$
\{\mathrm{@backreaction,@creation\_operator,@stabilization\_operator}\}
\not\Rightarrow
\mathrm{a\ recovered\ native\ Yang\!-\!Mills\ theory}. \tag{54.17}
$$

Equation (54.17) is EVIDENCE_BOUNDARY. The addresses organize relevant operations but do not supply the group, bundle, action, constraint algebra, gauge fixing, or quantum representation.

### 54.18 Open non-Abelian obligations

The missing bridge is

$$
\begin{aligned}
\mathfrak{U}_{\mathrm{YM}}=\{&
\mathrm{ExactGaugeGroup},
\mathrm{PrincipalBundle},
\mathrm{RepresentationsAndCharges},
\mathrm{NativeConnectionMap},\\
&\mathrm{RecoveredAction},
\mathrm{ConstraintAlgebra},
\mathrm{GaugeReduction},
\mathrm{PhysicalStateSpace},\\
&\mathrm{CreationOperatorAlgebra},
\mathrm{StabilizationCriterion},
\mathrm{BackreactionClosure},
\mathrm{QuantumValidation}\}.
\end{aligned} \tag{54.18}
$$

Equation (54.18) is CURATOR_SYNTHESIS. It records the exact data and proofs required for a complete MK-43 non-Abelian sector without creating them.

### 54.19 Chapter result

The non-Abelian realization boundary is

$$
\boxed{
\begin{aligned}
&\mathrm{LIE,\ CONNECTION,\ CURVATURE,\ ACTION,\ AND\ CONSTRAINT\ TARGETS\ EXPLICIT};\\
&\mathrm{CREATION,\ STABILIZATION,\ AND\ BACKREACTION\ ADDRESSES\ PRESERVED};\\
&\mathrm{NATIVE\ MK43\ YANG\!-\!MILLS\ COMPLETION\ REMAINS\ OPEN}.
\end{aligned}
} \tag{54.19}
$$

Equation (54.19) is DETERMINISTIC_STATUS_NORMALIZATION. The chapter supplies the established non-Abelian mathematics needed to test a Yang-Mills realization. It does not promote graph density into a recovered action, identify the generic creation operator with a gauge-boson mode, or claim a typed stabilization and backreaction closure.
