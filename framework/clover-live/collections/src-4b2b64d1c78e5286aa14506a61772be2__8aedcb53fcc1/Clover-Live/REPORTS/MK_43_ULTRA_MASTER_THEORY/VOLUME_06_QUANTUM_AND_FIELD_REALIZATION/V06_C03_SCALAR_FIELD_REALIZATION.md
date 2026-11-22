# VOLUME VI - QUANTUM AND FIELD REALIZATION

## Chapter 51 - Scalar-Field Realization

### 51.1 From a bundle section to a scalar field

The handoff object supplies a bundle \(F\to M\), a connection, curvature, a section, and an action. The simplest field realization occurs when the relevant fiber is one-dimensional and the section is represented locally by a scalar function

$$
\phi:M\longrightarrow\mathbb{R}
\quad\text{or}\quad
\phi:M\longrightarrow\mathbb{C}. \tag{51.1}
$$

Equation (51.1) is EXTERNAL_ESTABLISHED_MATHEMATICS. It is a realization choice, not an exact recovered definition attached to one of this chapter's eleven API handles. A real scalar has one real component; a complex scalar has two real components and can carry a continuous phase symmetry.

The distinction between field and realization remains important. The abstract section \(\Gamma\) in \(Q\) need not be scalar. Choosing a scalar target fixes a representation sector and makes the variational and propagation structures explicit enough to test.

### 51.2 Covariant scalar action

On a Lorentzian manifold \((M,g)\), a standard minimally coupled real scalar action is

$$
S[\phi;g]
=\int_M d^dx\,\sqrt{|g|}
\left[
-\frac12 g^{\mu\nu}\nabla_{\mu}\phi\,\nabla_{\nu}\phi
-V(\phi)
\right]. \tag{51.2}
$$

Equation (51.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. The action specifies the kinetic pairing, background geometry, volume form, and potential. The API addresses @shell_action, @interaction_action, and @action_and_variation do not contain a recovered exact formula establishing that any one of them equals Equation (51.2).

The formula instead supplies the conventional mathematical target against which an MK-43 scalar realization can be typed. A source-level identification would have to specify the field, metric, dimension, sign convention, potential, units, and boundary terms.

### 51.3 Variation and equation of motion

For compactly supported variations or boundary conditions that cancel the surface term,

$$
\delta S
=\int_M d^dx\,\sqrt{|g|}
\left(\nabla_{\mu}\nabla^{\mu}\phi-V'(\phi)\right)\delta\phi,
\qquad
\square_g\phi-V'(\phi)=0. \tag{51.3}
$$

Equation (51.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. It makes the title @action_and_variation mathematically concrete without attributing the equation to that thin source record. The boundary qualification is essential: the Euler-Lagrange equation follows only after the variational problem is well posed.

This also defines what an action address must eventually provide. A name alone does not determine the varied variables, admissible variations, boundary conditions, or whether the field equation is classical, effective, or operator-valued.

### 51.4 Mass and interaction terms

A common potential expansion is

$$
V(\phi)
=\frac12 m^2\phi^2
+\frac{\lambda_3}{3!}\phi^3
+\frac{\lambda_4}{4!}\phi^4+\cdots . \tag{51.4}
$$

Equation (51.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. The quadratic term fixes the free mass parameter, while higher powers introduce local self-interactions. Stability, symmetry, dimension, and renormalizability constrain the admissible coefficients.

The assigned addresses @interaction_action and @origin_fractal_interaction are both THIN and contain no coherent equation units. Their titles can direct later recovery, but they cannot select \(\lambda_3\), \(\lambda_4\), a nonlocal kernel, or a fractal interaction law. No such identification is made.

### 51.5 Stress-energy and geometric response

Metric variation defines the scalar stress-energy tensor,

$$
T_{\mu\nu}
=-\frac{2}{\sqrt{|g|}}\frac{\delta S}{\delta g^{\mu\nu}}
=\nabla_{\mu}\phi\,\nabla_{\nu}\phi
-g_{\mu\nu}
\left[
\frac12\nabla_{\alpha}\phi\,\nabla^{\alpha}\phi+V(\phi)
\right]. \tag{51.5}
$$

Equation (51.5) is EXTERNAL_ESTABLISHED_MATHEMATICS for the convention used in Equation (51.2). It supplies the object that can participate in the backreaction problem introduced in Chapter 50. Conservation \(\nabla^{\mu}T_{\mu\nu}=0\) follows on shell under the corresponding covariance assumptions.

The result does not prove that a Time-Shell or Helicon variable is a scalar matter field. It shows what must be recovered if one is to claim that such a variable sources readable geometry through a scalar realization.

### 51.6 Free-field mode expansion

In a stationary flat-background example, a free real field may be expanded as

$$
\widehat{\phi}(x)
=\int\frac{d^{d-1}\mathbf{k}}{(2\pi)^{d-1}\sqrt{2\omega_{\mathbf{k}}}}
\left[
a_{\mathbf{k}}e^{-ik\cdot x}
+a_{\mathbf{k}}^{\dagger}e^{ik\cdot x}
\right],
\qquad
\omega_{\mathbf{k}}^2=\mathbf{k}^2+m^2. \tag{51.6}
$$

Equation (51.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. It connects a scalar field to the Fock-space and particle-number structures of Chapter 50. The expansion depends on a positive-frequency split and is not globally canonical on a general time-dependent geometry.

This limitation is directly relevant to realization. A propagation operator does not by itself choose a vacuum, a mode basis, or a particle interpretation. Those require additional geometric and state data.

### 51.7 Green functions and propagation

For the linear operator \(L=\square_g-m^2\), a Green function satisfies

$$
L_xG(x,y)=\frac{\delta^{(d)}(x-y)}{\sqrt{|g(x)|}},
\qquad
\phi(x)=\phi_{\mathrm{hom}}(x)+\int_M d^dy\,\sqrt{|g(y)|}\,G(x,y)J(y). \tag{51.7}
$$

Equation (51.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. Retarded, advanced, Feynman, and other Green functions differ through boundary or state prescriptions. Their shared differential equation does not make them interchangeable.

The Library address @propagation_operator is highly connected and evidence-rich relative to the other assigned handles. Yet its six indexed equation windows are broad canonical blocks, not clean scalar-propagation definitions. Equation (51.7) is therefore a conventional model of what a propagation structure can do, not a recovered formula for that handle.

### 51.8 Abstract propagation operator

An abstract evolution family can be typed as

$$
U(t_2,t_1):\mathcal{S}_{t_1}\longrightarrow\mathcal{S}_{t_2},
\qquad
U(t_3,t_2)U(t_2,t_1)=U(t_3,t_1). \tag{51.8}
$$

Equation (51.8) is DETERMINISTIC_TYPE_NORMALIZATION. It identifies the minimum domain, codomain, and composition data needed for an object to act as a propagation operator. It does not assert that @propagation_operator already has this exact typing.

If the dynamics is unitary on a Hilbert space, \(U^{\dagger}U=I\). If it evolves classical Cauchy data, its state spaces are solution-data spaces rather than Hilbert rays. If it transports bundle sections, compatibility with the connection must be stated. These cases cannot be merged by terminology.

### 51.9 Initial-value formulation

For a globally hyperbolic background with Cauchy surface \(\Sigma\), a second-order scalar equation is determined by data

$$
\phi|_{\Sigma}=\phi_0,\qquad
n^{\mu}\nabla_{\mu}\phi|_{\Sigma}=\pi_0. \tag{51.9}
$$

Equation (51.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. Well-posedness requires existence, uniqueness, and continuous dependence in specified function spaces. These conditions turn a formal differential equation into a propagation law.

Primitive P2 is declared as the Continuation Operator. That title is structurally adjacent to an evolution map, but no exact source record in this chapter establishes that P2 is the Cauchy propagator of Equation (51.9). The relation remains one of possible representation, not identity.

### 51.10 Chirality mirror as a candidate field operation

The API records a direct arrow from @boundary_reflection to @chirality_mirror_operator. A scalar-field model could represent a reflection by

$$
(\mathcal{M}_{\chi}\phi)(x)=\eta_{\chi}\,\phi(r x),
\qquad
\eta_{\chi}\in\{+1,-1\}. \tag{51.10}
$$

Equation (51.10) is PROPOSED_INTERPRETATION. It is not a recovered equation. The sign could distinguish scalar from pseudoscalar behavior under a specified reflection \(r\), but the API does not presently supply the domain, reflection map, parity assignment, involution law, or relation to the framework's broader chirality object.

The candidate is included to expose the missing typing, not to complete it. A valid source-level mirror operator should state whether \(\mathcal{M}_{\chi}^2=I\), which inner product it preserves, and how it acts on boundary conditions and interactions.

### 51.11 Bulk, shell, and boundary action

For a region \(M\) with boundary \(\partial M\), a well-posed variational principle may require

$$
S_{\mathrm{total}}
=S_{\mathrm{bulk}}+S_{\mathrm{boundary}},
\qquad
\delta S_{\mathrm{total}}\big|_{\mathrm{admissible\ data}}=0. \tag{51.11}
$$

Equation (51.11) is EXTERNAL_ESTABLISHED_MATHEMATICS. It gives a conventional scope distinction for @shell_action and the bulk-action material encountered in Chapter 50. It does not establish that shell means Time Shell, that a shell action is a boundary term, or that either source address has this decomposition.

Those claims require exact field content, integration domain, induced geometry, orientation, matching conditions, and a derivation of the surface term. Until then, bulk, shell, and boundary remain separate labels.

### 51.12 Expansion operators and provenance

The API declares @provenance_expansion_operator and @realization_expansion_operator with one registered dependency each. Their minimum typed distinction can be expressed as

$$
\mathcal{E}_{\mathrm{prov}}:\mathcal{R}\to\mathcal{R}^{+},
\qquad
\mathcal{E}_{\mathrm{real}}:\mathcal{O}\to\operatorname{Rep}(\mathcal{O}). \tag{51.12}
$$

Equation (51.12) is DETERMINISTIC_TYPE_NORMALIZATION, not recovered operator mathematics. The first arrow expands a record with provenance context; the second expands an object into realization records. Neither is automatically a physical field evolution.

This distinction protects the theory from confusing metadata operations with dynamics. Provenance expansion can expose more evidence without changing a physical state. Realization expansion can enumerate representations without evolving the represented object.

### 51.13 Evidence and domain guardrails

The chapter's assigned set also includes a market-network adapter chapter, a Genesis Creation Operator, and an Origin-Fractal Interaction. Their assignment does not make them scalar-field constituents:

$$
\mathrm{chapter\ assignment}
\not\Rightarrow
\mathrm{scalar\ field\ definition,\ action,\ or\ propagator}. \tag{51.13}
$$

Equation (51.13) is EVIDENCE_BOUNDARY. Narrative, economic, adapter, Genesis-language, and physical-field domains may share structural analogies, but a scalar-field import needs an explicit variable, state space, action, and typed map. No analogy is promoted into mathematical identity.

### 51.14 Coverage calibration

The Library 4.1 evidence distribution is

$$
N_{\mathrm{assigned}}=11,\qquad
N_{\mathrm{THIN}}=9,\qquad
N_{\mathrm{MEDIUM}}=2. \tag{51.14}
$$

Equation (51.14) is DETERMINISTIC_COVERAGE_EVIDENCE. The assigned handles contain 696 English units, nine indexed equation units, and 433 registered dependencies. Of those, @propagation_operator alone contributes 609 English units, six equation units, and 430 dependencies.

This concentration is not a proof of scalar dynamics. It makes propagation the strongest recovery address while requiring more stringent filtering of broad graph and source-window material.

### 51.15 API evidence register

The register below is generated from the exact Library 4.1 assignment and native query digest.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@action_and_variation` | @action_and_variation` — Action and variation | THIN | 18 / 0 / 0 | chapter-core object |
| `@chapter_77_adapter_market_er_networks_and_transaction_connectivity` | @chapter_77_adapter_market_er_networks_and_transaction_connectivity` — Chapter 77 Adapter — Market ER Networks and Transaction Connectivity | THIN | 11 / 0 / 0 | chapter-core object |
| `@chirality_mirror_operator` | New Handle — @chirality_mirror_operator | MEDIUM | 34 / 3 / 1 | chapter-core object |
| `@interaction_action` | @interaction_action` — Interaction Action | THIN | 0 / 0 / 0 | chapter-core object |
| `@operator_14_3_genesis_creation_operator` | @operator_14_3_genesis_creation_operator` — Operator 14.3 — Genesis Creation Operator | THIN | 3 / 0 / 0 | chapter-core object |
| `@origin_fractal_interaction` | @origin_fractal_interaction` — Origin-Fractal Interaction | THIN | 0 / 0 / 0 | chapter-core object |
| `@primitive_p2` | @primitive_p2` — Primitive P2 — Continuation Operator | THIN | 8 / 0 / 0 | chapter-core object |
| `@propagation_operator` | @propagation_operator` — Propagation Operator | MEDIUM | 609 / 6 / 430 | chapter-core object |
| `@provenance_expansion_operator` | @provenance_expansion_operator | THIN | 3 / 0 / 1 | chapter-core object |
| `@realization_expansion_operator` | @realization_expansion_operator | THIN | 3 / 0 / 1 | chapter-core object |
| `@shell_action` | @shell_action` — Shell Action | THIN | 7 / 0 / 0 | chapter-core object |

### 51.16 Open scalar-realization obligations

The remaining work can be stated as

$$
\begin{aligned}
\mathfrak{U}_{\phi}=\{&
\mathrm{ExactMK43ScalarVariable},
\mathrm{FiberAndRepresentationMap},
\mathrm{RecoveredPotential},
\mathrm{UnitsAndNormalization},\\
&\mathrm{ExactPropagationOperator},
\mathrm{InitialOrBoundaryData},
\mathrm{QuantizationPrescription},
\mathrm{VacuumAndModeChoice},\\
&\mathrm{TypedChiralityMirror},
\mathrm{ShellBulkRelation},
\mathrm{BackreactionClosure},
\mathrm{StabilityAndValidation}\}.
\end{aligned} \tag{51.16}
$$

Equation (51.16) is CURATOR_SYNTHESIS of explicit bridge requirements. It does not fill them. Each item needs exact source evidence, a declared mathematical construction, or later mathematical development with its status clearly labeled.

### 51.17 Chapter result

The scalar-field realization boundary is

$$
\boxed{
\begin{aligned}
&\mathrm{SCALAR\ ACTION,\ VARIATION,\ AND\ PROPAGATION\ TARGETS\ EXPLICIT};\\
&\mathrm{LIBRARY\ OPERATOR\ ADDRESSES\ PRESERVED};\\
&\mathrm{MK43\ SCALAR\ IDENTIFICATION\ NOT\ YET\ RECOVERED}.
\end{aligned}
} \tag{51.17}
$$

Equation (51.17) is DETERMINISTIC_STATUS_NORMALIZATION. The chapter supplies the conventional mathematical realization needed to test an MK-43 scalar sector, organizes the action and propagation addresses, and preserves the boundary-reflection-to-chirality-mirror graph relation. It does not claim a recovered scalar identity, an exact potential, a proven shell action, or a fully typed propagation operator.
