# VOLUME VI - QUANTUM AND FIELD REALIZATION

## Chapter 52 - Gauge-Field Realization

### 52.1 Gauge potential as a connection

A gauge field is most naturally represented by a connection on a principal or associated bundle. For an Abelian \(U(1)\) realization, the local connection one-form is

$$
A=A_{\mu}dx^{\mu}. \tag{52.1}
$$

Equation (52.1) is EXTERNAL_ESTABLISHED_MATHEMATICS. It gives a conventional realization of the connection component already present in the handoff object \(Q\), but it is not an exact formula recovered from this chapter's API handles.

The potential depends on a local trivialization. The field strength and gauge-invariant observables, rather than one chosen potential, carry physical content. This difference between representation and invariant object is the organizing principle of gauge theory.

### 52.2 Abelian gauge transformation

For a scalar gauge parameter \(\alpha\),

$$
A_{\mu}\longmapsto A_{\mu}+\partial_{\mu}\alpha,
\qquad
\psi\longmapsto e^{iq\alpha}\psi. \tag{52.2}
$$

Equation (52.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. The transformation changes the local representative while preserving the gauge-equivalence class. A charged matter field transforms in a representation with charge \(q\).

This is internal gauge symmetry. It must not be identified with a change of spacetime coordinates or the linearized metric transformation discussed later. Both use redundant descriptions, but their objects, groups, and representations differ.

### 52.3 Curvature or field strength

The Abelian curvature is

$$
F=dA,\qquad
F_{\mu\nu}=\partial_{\mu}A_{\nu}-\partial_{\nu}A_{\mu},
\qquad
dF=0. \tag{52.3}
$$

Equation (52.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. The Bianchi identity \(dF=0\) follows directly from \(d^2=0\). Under Equation (52.2), \(F\) is invariant.

Within the handoff tuple, the connection \(\nabla\) and curvature \(R_{\nabla}\) provide the abstract locations for this structure. An exact \(U(1)\) identification still requires the structure group, representation, coupling, and relation between \(R_{\nabla}\) and \(F\).

### 52.4 Maxwell action

The standard Abelian action with current \(J^{\mu}\) is

$$
S[A]
=\int_M d^dx\,\sqrt{|g|}
\left(
-\frac14 F_{\mu\nu}F^{\mu\nu}
-J^{\mu}A_{\mu}
\right). \tag{52.4}
$$

Equation (52.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. Gauge invariance of the source coupling requires current conservation under the usual boundary assumptions.

The action converts the geometric connection into dynamics. It still leaves sign conventions, units, boundary terms, background geometry, and admissible field space to be specified. No API title alone fixes these choices.

### 52.5 Field equation and constraint

Variation of Equation (52.4) yields

$$
\nabla_{\mu}F^{\mu\nu}=J^{\nu},
\qquad
\nabla_{\nu}J^{\nu}=0. \tag{52.5}
$$

Equation (52.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. The second relation is a compatibility condition. It illustrates what gauge consistency means in a concrete field model: sources, constraints, and symmetry must fit together.

A gauge condition is not the field equation. It selects representatives or simplifies evolution, while Equation (52.5) governs gauge-equivalence classes of solutions.

### 52.6 Non-Abelian connection and curvature

For a Lie-algebra-valued connection \(A=A_{\mu}^aT_a\,dx^{\mu}\),

$$
F=dA+gA\wedge A,\qquad
F_{\mu\nu}^a
=\partial_{\mu}A_{\nu}^a-\partial_{\nu}A_{\mu}^a
+g f^{a}{}_{bc}A_{\mu}^bA_{\nu}^c. \tag{52.6}
$$

Equation (52.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. The nonlinear term distinguishes Yang-Mills curvature from the Abelian case. Gauge transformations act by
\(A\mapsto UAU^{-1}-g^{-1}(dU)U^{-1}\).

The group, representation, coupling, and invariant bilinear form are indispensable data. A general connection in \(Q\) does not determine them without a recovered structure-group declaration.

### 52.7 Yang-Mills action

The conventional gauge action is

$$
S_{\mathrm{YM}}[A]
=-\frac14\int_M d^dx\,\sqrt{|g|}\,
F_{\mu\nu}^{a}F^{\mu\nu}_{a},
\qquad
D_{\mu}F^{\mu\nu}=J^{\nu}. \tag{52.7}
$$

Equation (52.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. The covariant derivative \(D_{\mu}\) acts in the adjoint representation on the curvature. Quantization additionally requires gauge fixing or a gauge-invariant construction, constraints, and, in perturbative formulations, ghost and renormalization machinery.

Nothing in the current assignment recovers a unique MK-43 gauge group or proves that a particular upstream field realizes Equation (52.7).

### 52.8 Gauge-covariant matter coupling

For a matter field \(\psi\), the ordinary derivative is replaced by

$$
D_{\mu}\psi
=\left(\nabla_{\mu}+igA_{\mu}^{a}T_a\right)\psi,
\qquad
[D_{\mu},D_{\nu}]\psi
=igF_{\mu\nu}^{a}T_a\psi. \tag{52.8}
$$

Equation (52.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. It links representation data, connection, and curvature. This is the type of exact bridge required to turn the abstract handoff connection into an interaction-carrying gauge field.

The commutator relation is representation dependent. It must not be generalized to every propagation or continuation operator without specifying how the operator acts on sections.

### 52.9 Lorenz gauge

For an Abelian potential, the Lorenz condition is

$$
\nabla_{\mu}A^{\mu}=0,
\qquad
\square_g A^{\nu}-R^{\nu}{}_{\mu}A^{\mu}=J^{\nu}
\ \text{under this condition}. \tag{52.9}
$$

Equation (52.9) is EXTERNAL_ESTABLISHED_MATHEMATICS for the displayed curvature convention. Library 4.1 contains the declared address @lorenz_gauge with MEDIUM coherent coverage, but this formula is presented as conventional mathematics rather than an exact-source import.

Lorenz gauge does not remove all gauge freedom. Residual parameters satisfy the homogeneous equation compatible with the background and boundary conditions.

### 52.10 Gauge fixing and physical modes

The physical configuration space is a quotient,

$$
\mathcal{C}_{\mathrm{phys}}
=\mathcal{C}_{\mathrm{fields}}/\mathcal{G}_{\mathrm{gauge}},
\qquad
\mathcal{O}[A]=\mathcal{O}[A^{g}]. \tag{52.10}
$$

Equation (52.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. A gauge choice selects representatives, while observables descend to the quotient. This conventional distinction supplies the mathematical scope for @gauge_choices_and_physical_modes.

A successful gauge condition should intersect admissible orbits appropriately and preserve the constraints. Global obstructions, residual symmetry, and Gribov-type ambiguities can prevent a single gauge choice from defining a global section of configuration space.

### 52.11 Linearized spacetime gauge transformation

For a perturbation \(g_{\mu\nu}=\bar g_{\mu\nu}+h_{\mu\nu}\), an infinitesimal diffeomorphism generated by \(\xi_{\mu}\) acts as

$$
h_{\mu\nu}
\longmapsto
h_{\mu\nu}
+\bar\nabla_{\mu}\xi_{\nu}
+\bar\nabla_{\nu}\xi_{\mu}. \tag{52.11}
$$

Equation (52.11) is EXTERNAL_ESTABLISHED_MATHEMATICS. It provides the standard target for @gauge_transformation_linearized. It is a spacetime-gauge transformation of a metric perturbation, not the internal \(U(1)\) transformation of Equation (52.2).

The two transformation laws may coexist in a theory with matter and gravity. Their parameters and constraints remain separate unless a larger unified structure is explicitly constructed.

### 52.12 Transverse-traceless gauge

For radiative perturbations on a suitable background, the TT conditions are

$$
\bar\nabla^{\mu}h_{\mu\nu}^{\mathrm{TT}}=0,
\qquad
\bar g^{\mu\nu}h_{\mu\nu}^{\mathrm{TT}}=0. \tag{52.12}
$$

Equation (52.12) is EXTERNAL_ESTABLISHED_MATHEMATICS. The address @transverse_traceless_gauge is MEDIUM and strongly connected in Library 4.1. The conventional conditions isolate radiative degrees of freedom only under appropriate background, field-equation, and boundary assumptions.

TT projection is therefore not a universal replacement for gauge reduction. It applies to a specified perturbative sector and must preserve the upstream provenance of the perturbation being projected.

### 52.13 Gauge consistency is a typed condition

The recovered addresses are substantial, but address density cannot merge internal gauge theory, linearized diffeomorphisms, and gauge fixing:

$$
\mathcal{G}_{\mathrm{internal}}
\neq
\mathcal{G}_{\mathrm{linearized\ diffeomorphism}}
\neq
\mathrm{GaugeCondition}. \tag{52.13}
$$

Equation (52.13) is EVIDENCE_AND_TYPE_BOUNDARY. The first two are transformation groups or their infinitesimal actions; the last is a condition on representatives. Gauge consistency requires that the action, field equations, constraints, observables, and quantization respect the relevant symmetry.

The API handle @gauge_consistency has MEDIUM coverage and two registered dependencies. Its indexed equation units remain source windows to audit, not permission to assert a completed universal consistency theorem.

### 52.14 Continuation and gauge transport

An abstract continuation operator acting on gauge classes should satisfy

$$
C_{t_2,t_1}:\mathcal{C}_{\mathrm{phys}}(t_1)
\longrightarrow
\mathcal{C}_{\mathrm{phys}}(t_2),
\qquad
C[A^{g}]=[C(A)]. \tag{52.14}
$$

Equation (52.14) is DETERMINISTIC_TYPE_NORMALIZATION, not a recovered formula for @continuation_operator. It displays the compatibility needed for physical evolution to be independent of a representative.

If continuation acts before quotienting, equivariance with gauge transformations must be stated. If it acts after quotienting, existence and well-posedness on the quotient must be proved. The Library address alone does not select one construction.

### 52.15 Coverage calibration

The chapter's Library 4.1 assignment has

$$
N_{\mathrm{assigned}}=7,\qquad
N_{\mathrm{THIN}}=1,\qquad
N_{\mathrm{MEDIUM}}=6. \tag{52.15}
$$

Equation (52.15) is DETERMINISTIC_COVERAGE_EVIDENCE. The seven handles contain 1,974 English units, 36 indexed equation units, and 2,255 registered dependencies. @gauge_transformation_linearized, @lorenz_gauge, and @transverse_traceless_gauge dominate the dependency landscape.

This is strong navigational evidence. It does not by itself prove a gauge-field realization or a complete constraint analysis.

### 52.16 API evidence register

The register below is generated from the exact Library 4.1 assignment and native query digest.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@continuation_operator` | @continuation_operator` — Continuation Operator | MEDIUM | 239 / 6 / 187 | chapter-core object |
| `@gauge_choices_and_physical_modes` | @gauge_choices_and_physical_modes` — Gauge Choices and Physical Modes | THIN | 12 / 0 / 0 | chapter-core object |
| `@gauge_condition` | @gauge_condition | MEDIUM | 33 / 3 / 151 | chapter-core object |
| `@gauge_consistency` | @gauge_consistency | MEDIUM | 48 / 11 / 2 | chapter-core object |
| `@gauge_transformation_linearized` | @gauge_transformation_linearized | MEDIUM | 519 / 5 / 593 | chapter-core object |
| `@lorenz_gauge` | @lorenz_gauge | MEDIUM | 535 / 5 / 656 | chapter-core object |
| `@transverse_traceless_gauge` | @transverse_traceless_gauge | MEDIUM | 588 / 6 / 666 | chapter-core object |

### 52.17 Open gauge-realization obligations

The unresolved mathematical bridge is

$$
\begin{aligned}
\mathfrak{U}_{\mathrm{gauge}}=\{&
\mathrm{ExactStructureGroup},
\mathrm{RepresentationAndCharges},
\mathrm{MK43ConnectionMap},
\mathrm{RecoveredGaugeAction},\\
&\mathrm{ConstraintAlgebra},
\mathrm{GaugeFixingDomain},
\mathrm{ResidualGauge},
\mathrm{PhysicalObservableAlgebra},\\
&\mathrm{QuantizationAndGhostSector},
\mathrm{InternalVsSpacetimeGaugeMap},
\mathrm{ContinuationEquivariance},
\mathrm{Validation}\}.
\end{aligned} \tag{52.17}
$$

Equation (52.17) is CURATOR_SYNTHESIS. It records the data and proofs needed to claim a complete MK-43 gauge sector. It does not invent them.

### 52.18 Chapter result

The gauge-field realization boundary is

$$
\boxed{
\begin{aligned}
&\mathrm{CONNECTION,\ CURVATURE,\ ACTION,\ AND\ GAUGE\ TARGETS\ EXPLICIT};\\
&\mathrm{INTERNAL\ AND\ SPACETIME\ GAUGE\ KEPT\ DISTINCT};\\
&\mathrm{MK43\ GAUGE\ GROUP\ AND\ COMPLETE\ QUANTIZATION\ OPEN}.
\end{aligned}
} \tag{52.18}
$$

Equation (52.18) is DETERMINISTIC_STATUS_NORMALIZATION. The chapter supplies the established mathematics needed to test a gauge-field realization and organizes the well-populated Library addresses for Lorenz, TT, linearized transformation, condition, consistency, and continuation. It does not claim an exact recovered gauge group, a universal gauge-fixing theorem, or a completed quantum gauge theory.
