# VOLUME VI - QUANTUM AND FIELD REALIZATION

## Chapter 55 - Field Actions, Operators, and Conservation

### 55.1 Action as the dynamical organizer

For fields \(\phi^A\) on a spacetime region \(M\), a local action has the conventional form

$$
S[\phi]=\int_M d^d x\,\sqrt{|g|}\,\mathcal{L}(\phi^A,\nabla_\mu\phi^A,g_{\mu\nu}). \tag{55.1}
$$

Equation (55.1) is EXTERNAL_ESTABLISHED_MATHEMATICS. An action is more than a list of allowed terms: it fixes the variational problem, boundary data, equations of motion, and—when symmetries are present—the corresponding conservation identities. The field content, dimensions, couplings, and admissible variations must therefore be stated before a native MK-43 action can be considered complete.

The ten Library 4.1 addresses assigned to this chapter organize operator-related evidence. They do not independently supply a single recovered action functional.

### 55.2 Euler-Lagrange equations

Stationarity under compactly supported variations gives

$$
\frac{\partial\mathcal{L}}{\partial\phi^A}
-\nabla_\mu\!\left(\frac{\partial\mathcal{L}}
{\partial(\nabla_\mu\phi^A)}\right)=0. \tag{55.2}
$$

Equation (55.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. Its use requires differentiability of the action and controlled boundary terms. Constraints, gauge freedom, higher derivatives, and nonlocal kernels change the precise variational analysis.

An API object called an operator becomes dynamical only after its domain, codomain, action on fields, and relation to \(S\) are supplied. A registry address alone does not establish Equation (55.2) for its entries.

### 55.3 Noether current

For a continuous transformation \(\delta\phi^A=\epsilon\,\Delta\phi^A\) under which the Lagrangian changes by a divergence, a Noether current may be written schematically as

$$
j^\mu
=\frac{\partial\mathcal{L}}{\partial(\nabla_\mu\phi^A)}
\Delta\phi^A-K^\mu,
\qquad \nabla_\mu j^\mu=0. \tag{55.3}
$$

Equation (55.3) is EXTERNAL_ESTABLISHED_MATHEMATICS on shell. Global charges require appropriate hypersurfaces and boundary falloff. Gauge symmetries also generate constraints and identities, so their conserved quantities must be treated more carefully than ordinary global charges.

Conservation in this chapter means a demonstrated consequence of a stated symmetry and action, not merely persistence suggested by an operator's name.

### 55.4 Charge and generator

Given a conserved current and Cauchy surface \(\Sigma\), the charge is

$$
Q=\int_\Sigma d\Sigma_\mu\,j^\mu,
\qquad \frac{dQ}{dt}=0, \tag{55.4}
$$

subject to the equations of motion and vanishing boundary flux. In quantum theory a self-adjoint generator acts through

$$
U(\alpha)=e^{-i\alpha\widehat Q},
\qquad \delta\widehat O=i\alpha[\widehat Q,\widehat O]. \tag{55.5}
$$

Equations (55.4) and (55.5) are EXTERNAL_ESTABLISHED_MATHEMATICS for the displayed conventions. They distinguish a conserved generator from a generic transformation map. A transformation-expansion operator is not automatically a Noether generator.

### 55.5 Operator domains and adjoints

A quantum operator is specified at minimum by

$$
\widehat A:D(\widehat A)\subset\mathcal{H}\longrightarrow\mathcal{H},
\qquad
\langle\psi,\widehat A\varphi\rangle
=\langle\widehat A^\dagger\psi,\varphi\rangle. \tag{55.6}
$$

Equation (55.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. For unbounded operators, the domain is part of the object. Symmetry on a dense domain does not by itself prove self-adjointness, and self-adjoint extensions may encode physical boundary conditions.

This domain discipline is the minimum standard for interpreting @observable_operators or the observable-operator claim named by @lemma_l11.

### 55.6 Observables and expectation values

For a density operator \(\rho\), an observable \(\widehat A\) has expectation

$$
\langle A\rangle_\rho=\operatorname{Tr}(\rho\widehat A),
\qquad \rho\ge0,
\qquad \operatorname{Tr}\rho=1. \tag{55.7}
$$

Equation (55.7) is EXTERNAL_ESTABLISHED_MATHEMATICS when the products are trace class. Superselection sectors restrict which coherent combinations and observable matrix elements are physically available. The address @density_operators_and_sectors therefore points toward a necessary structural boundary, but its THIN evidence does not fix a native sector decomposition.

### 55.7 Time evolution of operators

In the Heisenberg picture,

$$
\frac{d\widehat A}{dt}
=\frac{i}{\hbar}[\widehat H,\widehat A]
+\left(\frac{\partial\widehat A}{\partial t}\right)_{\mathrm{explicit}}. \tag{55.8}
$$

Equation (55.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. If \(\widehat A\) has no explicit time dependence, its conservation follows from \([\widehat H,\widehat A]=0\). This is a testable algebraic statement; it cannot be inferred from an operator label or graph proximity.

### 55.8 Creation and annihilation algebra

For bosonic modes one convention is

$$
[a_r,a_s^\dagger]=\delta_{rs},
\qquad [a_r,a_s]=[a_r^\dagger,a_s^\dagger]=0, \tag{55.9}
$$

while fermionic modes use anticommutators. The number operator obeys

$$
\widehat N_r=a_r^\dagger a_r,
\qquad [\widehat N_r,a_r^\dagger]=a_r^\dagger,
\qquad [\widehat N_r,a_r]=-a_r. \tag{55.10}
$$

Equations (55.9) and (55.10) are EXTERNAL_ESTABLISHED_MATHEMATICS. The address @annihilation_operator is a CREATED operator with THIN coverage, seven English units, no indexed equation units, and six dependencies. @hilbert_space_and_creation_operator is also THIN. Neither record alone fixes statistics, vacuum, mode normalization, or a native canonical algebra.

### 55.9 Normalization maps

For a nonzero Hilbert-space vector, normalization is

$$
\mathcal N(\psi)=\frac{\psi}{\sqrt{\langle\psi,\psi\rangle}},
\qquad \psi\ne0. \tag{55.11}
$$

Equation (55.11) is EXTERNAL_ESTABLISHED_MATHEMATICS. It is nonlinear, undefined at zero, and different from unitary evolution, probability conservation, renormalization, or normalization of a measure.

Library 4.1 gives @normalization_operator MEDIUM coverage with 104 English units, three indexed equation units, and four dependencies. Those counts warrant targeted source review, but they do not justify silently selecting Equation (55.11) as the API object's recovered definition.

### 55.10 Transformations and composition

For operators with compatible domains, composition is associative:

$$
(\mathcal O_3\circ\mathcal O_2)\circ\mathcal O_1
=\mathcal O_3\circ(\mathcal O_2\circ\mathcal O_1). \tag{55.12}
$$

Equation (55.12) is EXTERNAL_ESTABLISHED_MATHEMATICS. Commutativity, invertibility, and conservation do not follow from associativity. A transformation expansion needs its input space, output space, expansion parameter, convergence criterion, and relationship to the unexpanded transformation.

@transformation_expansion_operator has only three English units, no indexed equation units, and one dependency. Its present address is therefore a recovery target rather than a complete operator construction.

### 55.11 Stress-energy conservation

For a diffeomorphism-invariant matter action, the metric stress tensor is conventionally

$$
T_{\mu\nu}=-\frac{2}{\sqrt{|g|}}
\frac{\delta S_{\mathrm m}}{\delta g^{\mu\nu}},
\qquad \nabla_\mu T^{\mu\nu}=0. \tag{55.13}
$$

Equation (55.13) is EXTERNAL_ESTABLISHED_MATHEMATICS on shell under the relevant symmetry and boundary assumptions. In interacting theories, individual sectors may exchange energy and momentum even when the total tensor is conserved. A native MK-43 handoff must specify which upstream contributions enter the field action and how exchange terms close.

### 55.12 Typed registry requirement

A mathematically usable operator registry requires a structure such as

$$
\mathfrak R_{\mathrm{op}}
=\{(O_i,D_i,C_i,\circ_i,\dagger_i,\mathrm{status}_i,
\mathrm{provenance}_i)\}_{i\in I}. \tag{55.14}
$$

Equation (55.14) is DETERMINISTIC_TYPE_NORMALIZATION. It is not a recovered definition of @architect_operator_registry. The tuple records an operator, domain, codomain, composition rules, adjoint data, status, and provenance. Additional fields are needed for grading, constraints, dimensions, and equivalence relations.

The Library registry address is MEDIUM with 36 English units, three indexed equation units, and one dependency. Source isolation is required before any of those equations can be adopted as a registry axiom.

### 55.13 Coverage calibration

The assignment has

$$
N_{\mathrm{assigned}}=10,
\qquad N_{\mathrm{THIN}}=8,
\qquad N_{\mathrm{MEDIUM}}=2. \tag{55.15}
$$

Equation (55.15) is DETERMINISTIC_COVERAGE_EVIDENCE. Across the ten handles, Library 4.1 reports 175 English units, six indexed equation units, and twelve registered dependencies. @normalization_operator dominates the English evidence; it and @architect_operator_registry contain all six indexed equation units.

### 55.14 API evidence register

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@annihilation_operator` | @annihilation_operator | THIN | 7 / 0 / 6 | chapter-core object |
| `@architect_operator_registry` | @architect_operator_registry | MEDIUM | 36 / 3 / 1 | chapter-core object |
| `@collapse_operators_and_the_infinity_vector_field` | @collapse_operators_and_the_infinity_vector_field` — Collapse Operators and the Infinity Vector Field | THIN | 3 / 0 / 0 | chapter-core object |
| `@density_operators_and_sectors` | @density_operators_and_sectors` — Density operators and sectors | THIN | 1 / 0 / 0 | chapter-core object |
| `@hilbert_space_and_creation_operator` | @hilbert_space_and_creation_operator` — Hilbert space and creation operator | THIN | 13 / 0 / 0 | chapter-core object |
| `@lemma_l11` | @lemma_l11` — Lemma L11 — Observable Operators | THIN | 6 / 0 / 0 | chapter-core object |
| `@normalization_operator` | @normalization_operator | MEDIUM | 104 / 3 / 4 | chapter-core object |
| `@observable_operators` | @observable_operators` — Observable Operators | THIN | 1 / 0 / 0 | chapter-core object |
| `@transformation_expansion_operator` | @transformation_expansion_operator | THIN | 3 / 0 / 1 | chapter-core object |
| `@twin_prime_search_operators` | @twin_prime_search_operators` — Twin-Prime Search Operators | THIN | 1 / 0 / 0 | chapter-core object |

The distinct addresses must not be collapsed merely because each contains the word “operator.” In particular, arithmetic search, state normalization, mode annihilation, observation, and collapse belong to different domains unless an exact typed bridge is recovered.

### 55.15 Conservation boundary

The evidentiary implication is

$$
\mathrm{OperatorAddress}
\not\Rightarrow
\mathrm{TypedOperator}
\not\Rightarrow
\mathrm{SymmetryGenerator}
\not\Rightarrow
\mathrm{ConservedCharge}. \tag{55.17}
$$

Equation (55.17) is EVIDENCE_BOUNDARY. Each arrow requires additional mathematics: domains and actions, an invariant action, a Noether construction, and boundary conditions. This prevents graph organization from being reported as a recovered conservation theorem.

### 55.16 Open operator obligations

The remaining work can be organized as

$$
\begin{aligned}
\mathfrak U_{\mathrm{op}}=\{&
\mathrm{NativeFieldAction},\mathrm{BoundaryConditions},
\mathrm{OperatorDomains},\mathrm{AdjointsAndSpectra},
\mathrm{ConstraintAlgebra},\\
&\mathrm{CreationAnnihilationAlgebra},\mathrm{ObservableAlgebra},
\mathrm{SectorDecomposition},\mathrm{NormalizationTyping},
\mathrm{RegistrySemantics},\\
&\mathrm{SymmetryAction},\mathrm{NoetherCurrents},
\mathrm{ConservationProofs},\mathrm{CrossSectorExchange},
\mathrm{PhysicalValidation}\}.
\end{aligned} \tag{55.18}
$$

Equation (55.18) is CURATOR_SYNTHESIS. The list states proof obligations; it does not fill them. The collapse and infinity-vector-field topic, twin-prime search operators, and Lemma L11 require source-specific review before their roles can enter a unified field-operator algebra.

### 55.17 Chapter determination

The chapter status is

$$
\begin{aligned}
\mathrm{FieldActionsOperatorsConservation}_{\mathrm{V06C07}}
={}&\mathrm{RECOVERED\_ADDRESS\_MAP}\\
&+\mathrm{EXTERNAL\_MATHEMATICAL\_FRAME}\\
&+\mathrm{OPEN\_NATIVE\_TYPING}.
\end{aligned} \tag{55.19}
$$

Equation (55.19) is DETERMINISTIC_STATUS_NORMALIZATION. Library 4.1 supplies a verified ten-address evidence map, not a completed native field action or conservation theory. The conventional mathematics in this chapter provides explicit tests for future recovery: operators must be typed, observables represented on a physical state space, transformations tied to the action, and conservation established from symmetry rather than terminology.

The result is therefore a disciplined handoff. It preserves the recovered API address space, separates heterogeneous operator roles, and states exactly what remains before those addresses can become a native MK-43 dynamical and conservation structure.
