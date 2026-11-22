# VOLUME VII - GRAVITY

## Chapter 65 - Gravity-Matter Closure

### 65.1 Meaning of closure

In a gravitational initial-value problem, closure requires constraints, evolution equations, sources, and gauge conditions to remain mutually compatible:

$$
\mathcal C[g,K,\psi]=0,
\qquad
\mathcal E[g,K,\psi]=0,
\qquad
\mathcal G[g,K]=\kappa T[g,\psi]. \tag{65.1}
$$

Equation (65.1) is EXTERNAL_ESTABLISHED_MATHEMATICS as a schematic organization. It is not a recovered MK-43 formula. “Closure” means mathematical consistency of a declared system, not merely the presence of a handle named closure.

### 65.2 Spatial projection

Let \(n^\mu\) be the future-directed unit normal to a spacelike slice. Its spatial projector is

$$
\gamma_{\mu\nu}=g_{\mu\nu}+n_\mu n_\nu,
\qquad
\gamma_{\mu\nu}n^\nu=0. \tag{65.2}
$$

Equation (65.2) is EXTERNAL_ESTABLISHED_MATHEMATICS for signature \((-+++)\). The spacetime metric, slice metric, and normal field are separate inputs to the decomposition.

### 65.3 Extrinsic curvature

Choose the convention

$$
K_{ij}
=-\frac12\mathcal L_n\gamma_{ij}. \tag{65.3}
$$

Equation (65.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. Reversing the sign convention changes several subsequent signs but not the closure logic; every calculation must remain internally consistent.

### 65.4 Matter projections

Stress-energy decomposes relative to \(n^\mu\) as

$$
\rho=T_{\mu\nu}n^\mu n^\nu,
\qquad
j_i=-\gamma_i{}^\mu T_{\mu\nu}n^\nu,
\qquad
S_{ij}=\gamma_i{}^\mu\gamma_j{}^\nu T_{\mu\nu}. \tag{65.4}
$$

Equation (65.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. Energy density, momentum density, and spatial stress are projections of one tensor, not independent arbitrary sources.

### 65.5 Hamiltonian constraint

The normal-normal projection of Einstein's equation gives

$$
{}^{(3)}R+K^2-K_{ij}K^{ij}
=16\pi G\rho+2\Lambda \tag{65.5}
$$

in units \(c=1\). Equation (65.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. Initial data that violate this relation do not define an admissible Einstein evolution.

### 65.6 Momentum constraint

The normal-spatial projection gives

$$
D_j\!\left(K^{ij}-\gamma^{ij}K\right)
=8\pi G j^i. \tag{65.6}
$$

Equation (65.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. A proposed native matter handoff must supply both energy and momentum projections consistently.

### 65.7 Metric evolution

With lapse \(N\) and shift \(\beta^i\),

$$
(\partial_t-\mathcal L_\beta)\gamma_{ij}
=-2N K_{ij}. \tag{65.7}
$$

Equation (65.7) is EXTERNAL_ESTABLISHED_MATHEMATICS for the convention of Equation (65.3). Lapse and shift encode foliation freedom; they are not additional physical matter fields.

### 65.8 Curvature evolution

The extrinsic curvature evolves schematically as

$$
\begin{aligned}
(\partial_t-\mathcal L_\beta)K_{ij}
={}&-D_iD_jN
+N\big({}^{(3)}R_{ij}+K K_{ij}-2K_{ik}K^k{}_j\big)\\
&-8\pi G N\left(S_{ij}-\frac12\gamma_{ij}(S-\rho)\right)
-N\Lambda\gamma_{ij}.
\end{aligned} \tag{65.8}
$$

Equation (65.8) is EXTERNAL_ESTABLISHED_MATHEMATICS under the displayed conventions. It shows that source closure requires the spatial stress \(S_{ij}\), not only a scalar density.

### 65.9 Constraint preservation

If \(\mathcal H\) and \(\mathcal M_i\) denote the Hamiltonian and momentum constraints, consistency requires

$$
\mathcal H|_{t_0}=0,
\quad
\mathcal M_i|_{t_0}=0
\quad\Longrightarrow\quad
\mathcal H|_t=0,
\quad
\mathcal M_i|_t=0. \tag{65.9}
$$

Equation (65.9) is EXTERNAL_ESTABLISHED_MATHEMATICS as the closure requirement. Its proof follows from the evolution system, Bianchi identities, and source conservation under suitable regularity assumptions.

### 65.10 Covariant conservation

The Einstein equation and contracted Bianchi identity require

$$
\nabla^\mu G_{\mu\nu}=0
\quad\Longrightarrow\quad
\nabla^\mu T_{\mu\nu}=0. \tag{65.10}
$$

Equation (65.10) is EXTERNAL_ESTABLISHED_MATHEMATICS for constant couplings. A source prescription that fails this condition cannot be attached to an unchanged Einstein tensor without inconsistency.

### 65.11 Riemann symmetry closure

For the Levi-Civita curvature tensor,

$$
R_{\mu\nu\rho\sigma}
=-R_{\nu\mu\rho\sigma}
=-R_{\mu\nu\sigma\rho}
=R_{\rho\sigma\mu\nu},
\qquad
R_{\mu[\nu\rho\sigma]}=0. \tag{65.11}
$$

Equation (65.11) is EXTERNAL_ESTABLISHED_MATHEMATICS. @riemann_symmetries has MEDIUM coverage. These identities are algebraic admissibility conditions, not optional aesthetic properties.

### 65.12 Smeared constraints

Let \(H[N]\) and \(D[\vec N]\) be the Hamiltonian and spatial-diffeomorphism constraints smeared with lapse and shift. Their hypersurface-deformation structure includes

$$
\{D[\vec N],D[\vec M]\}
=D[[\vec N,\vec M]]. \tag{65.12}
$$

Equation (65.12) is EXTERNAL_ESTABLISHED_MATHEMATICS. Closure is an algebraic property of constraint generators; it cannot be inferred from a list of dependencies alone.

### 65.13 Mixed bracket

The mixed bracket is

$$
\{D[\vec N],H[M]\}
=H[\mathcal L_{\vec N}M]. \tag{65.13}
$$

Equation (65.13) is EXTERNAL_ESTABLISHED_MATHEMATICS. It expresses that the Hamiltonian smearing function transforms as a spatial scalar under the diffeomorphism generator.

### 65.14 Hamiltonian bracket

The Hamiltonian constraints satisfy

$$
\{H[N],H[M]\}
=D\!\left[\gamma^{ij}(N\partial_jM-M\partial_jN)\right]. \tag{65.14}
$$

Equation (65.14) is EXTERNAL_ESTABLISHED_MATHEMATICS. The appearance of the inverse spatial metric as a structure function distinguishes this relation from a Lie algebra with constant structure coefficients.

### 65.15 Reduced phase space

Formally, the physical phase space is

$$
\Gamma_{\mathrm{phys}}
=\{\text{constraint-satisfying data}\}/\{\text{gauge orbits}\}. \tag{65.15}
$$

Equation (65.15) is EXTERNAL_ESTABLISHED_MATHEMATICS as a formal quotient description. A complete construction requires functional-analytic control, gauge treatment, and boundary conditions.

### 65.16 Typed closure contract

The minimum consistency chain is

$$
(\gamma,K,\psi)
\longmapsto
(\rho,j,S)
\longmapsto
(\mathcal H,\mathcal M_i,\mathcal E)
\longmapsto
\big(\dot{\mathcal H},\dot{\mathcal M}_i\big)\big|_{\mathcal C=0}=0. \tag{65.16}
$$

Equation (65.16) is DETERMINISTIC_TYPE_NORMALIZATION. It keeps initial data, matter projections, constraints, evolution, and propagation of constraints distinct.

### 65.17 Coverage calibration

The chapter assignment contains

$$
N_{\mathrm{assigned}}=3,
\qquad
N_{\mathrm{MEDIUM}}=3,
\qquad
N_{\mathrm{THIN}}=0. \tag{65.17}
$$

Equation (65.17) is DETERMINISTIC_COVERAGE_EVIDENCE. The handles contain 629 English units, 24 indexed equation units, zero exact-definition units, and 578 registered dependencies. @native_constraint_closure contributes 597 English units, 15 equations, and 440 dependencies; @gravity_closure_v2 has six equations but only one registered dependency.

### 65.18 API evidence register

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@gravity_closure_v2` | @gravity_closure_v2 | MEDIUM | 23 / 6 / 1 | chapter-core object |
| `@native_constraint_closure` | @native_constraint_closure | MEDIUM | 597 / 15 / 440 | chapter-core object |
| `@riemann_symmetries` | @riemann_symmetries | MEDIUM | 9 / 3 / 137 | chapter-core object |

The register preserves native constraint closure, gravity closure versioning, and Riemann symmetry conditions as separate addresses. Coverage does not establish that their complete mathematics is identical.

### 65.19 Evidence boundary

The operative distinctions are

$$
\begin{aligned}
\mathrm{ConstraintClosure}&\ne\mathrm{TheoryCompletion},\\
\mathrm{SourceConservation}&\ne\mathrm{SourceDerivation},\\
\mathrm{RiemannSymmetry}&\ne\mathrm{EinsteinDynamics},\\
\mathrm{GraphDependency}&\ne\mathrm{PoissonBracketProof}.
\end{aligned} \tag{65.18}
$$

Equation (65.18) is EVIDENCE_BOUNDARY. These distinctions prevent a recovered status label from being upgraded into a mathematical closure theorem.

### 65.20 Open gravity-matter obligations

The unresolved requirements are

$$
\begin{aligned}
\mathfrak U_{\mathrm{closure}}=\{&
\mathrm{NativePhaseSpace},
\mathrm{NativeConstraints},
\mathrm{ConstraintAlgebra},
\mathrm{MatterProjections},
\mathrm{SourceConservation},\\
&\mathrm{GaugeGenerators},
\mathrm{BoundaryCharges},
\mathrm{WellPosedEvolution},
\mathrm{ConstraintPropagationProof},\\
&\mathrm{AnomalyFreedom},
\mathrm{QuantumClosure},
\mathrm{Uniqueness},
\mathrm{Stability},
\mathrm{ExperimentalValidation}\}.
\end{aligned} \tag{65.19}
$$

Equation (65.19) is CURATOR_SYNTHESIS. It records the requirements that remain after the standard closure structure has been made explicit.

### 65.21 Chapter determination

The result is

$$
\begin{aligned}
\mathrm{GravityMatterClosure}_{\mathrm{V07C09}}
={}&\mathrm{ESTABLISHED\_CONSTRAINT\_FRAMEWORK}\\
&+\mathrm{RECOVERED\_CLOSURE\_ADDRESSES}\\
&+\mathrm{OPEN\_NATIVE\_ALGEBRA\_AND\_SOURCE}.
\end{aligned} \tag{65.20}
$$

Equation (65.20) is DETERMINISTIC_STATUS_NORMALIZATION. The chapter supplies the standard mathematical meaning of closure and maps it to the recovered API addresses without claiming a native proof. The MK-43 constraint algebra, source derivation, quantum closure, and validation remain open where exact evidence does not close them.
