# VOLUME XVIII - MATHEMATICAL APPENDICES

## Chapter 141 - Differential Geometry Conventions

### 141.1 Geometric convention record

A geometry convention must preserve manifold, dimension, signature, coordinates, metric, connection, curvature sign, orientation, scope, and provenance,

$$
\mathfrak G=(M,n,s,x,g,\nabla,\varepsilon_R,o,\Omega,p). \tag{141.1}
$$

Equation (141.1) is DETERMINISTIC_TYPE_NORMALIZATION. Formulas cannot be compared safely when any of these coordinates is implicit.

### 141.2 Metric convention

The line element is locally

$$
ds^2=g_{\mu\nu}\,dx^\mu dx^\nu. \tag{141.2}
$$

Equation (141.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. The signature and index range must be declared separately.

### 141.3 Inverse metric

Index raising and lowering require

$$
g^{\mu\rho}g_{\rho\nu}=\delta^\mu{}_{\nu}. \tag{141.3}
$$

Equation (141.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. Degenerate structures require a different convention and may not use this identity silently.

### 141.4 Levi-Civita connection

For a nondegenerate metric, the torsion-free metric-compatible connection has coefficients

$$
\Gamma^\rho{}_{\mu\nu}=\frac12g^{\rho\sigma}(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu}). \tag{141.4}
$$

Equation (141.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. It is not assumed for source-specific generalized connections without evidence.

### 141.5 Covariant derivative

For a vector field,

$$
\nabla_\mu V^\nu=\partial_\mu V^\nu+\Gamma^\nu{}_{\mu\rho}V^\rho. \tag{141.5}
$$

Equation (141.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. Tensor type determines every additional connection term.

### 141.6 Curvature convention

One explicit sign convention is

$$
[\nabla_\mu,\nabla_\nu]V^\rho=R^\rho{}_{\sigma\mu\nu}V^\sigma. \tag{141.6}
$$

Equation (141.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. A source using the opposite Riemann sign must remain version-specific.

### 141.7 Ricci contraction

With equation (141.6), define

$$
R_{\mu\nu}=R^\rho{}_{\mu\rho\nu},\qquad R=g^{\mu\nu}R_{\mu\nu}. \tag{141.7}
$$

Equation (141.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. Alternate index placements require an explicit translation.

### 141.8 Geodesic convention

An affinely parameterized geodesic satisfies

$$
\frac{d^2x^\rho}{d\lambda^2}+\Gamma^\rho{}_{\mu\nu}\frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda}=0. \tag{141.8}
$$

Equation (141.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. Non-affine parameters introduce a tangent-proportional term.

### 141.9 Pullback boundary

For a smooth map $f:M\to N$, a covariant tensor may be pulled back,

$$
f^*:T^*N\to T^*M. \tag{141.9}
$$

Equation (141.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. Pullback, restriction, projection, and whole-object identity remain different relations.

### 141.10 Orientation convention

An orientation choice fixes the sign of the volume form,

$$
\mathrm{vol}_g=\sqrt{|\det g|}\,dx^0\wedge\cdots\wedge dx^{n-1}. \tag{141.10}
$$

Equation (141.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. Coordinate ordering and metric signature must remain explicit.

### 141.11 Chirality-definition profile

The Chirality definition address contributes

$$
E_{@\mathrm{definition\_13\_1\_chirality}}=(7,0,1,0). \tag{141.11}
$$

Equation (141.11) is DETERMINISTIC_COVERAGE_EVIDENCE. The tuple records English, equation, definition, and dependency units; it does not identify chirality with geometric orientation.

### 141.12 Structured-nothingness profile

The Structured Nothingness definition contributes

$$
E_{@\mathrm{definition\_10\_2\_structured\_nothingness}}=(2,0,1,0). \tag{141.12}
$$

Equation (141.12) is DETERMINISTIC_COVERAGE_EVIDENCE. Its mathematical type is not supplied by the chapter title.

### 141.13 No-hair profile

The dominant address contributes

$$
E_{@\mathrm{no\_hair\_theorem}}=(49,4,139). \tag{141.13}
$$

Equation (141.13) is DETERMINISTIC_COVERAGE_EVIDENCE. Four equations and 139 dependencies do not yield a coherent theorem-proof unit.

### 141.14 Geometry-title profile

Phase Geometry, Amplitude Geometry, and Shell Differential Geometry contribute

$$
E_{\mathrm{geometry\ titles}}=(14,0,0)+(6,0,0)+(7,0,0)=(27,0,0). \tag{141.14}
$$

Equation (141.14) is DETERMINISTIC_COVERAGE_EVIDENCE. Their titles motivate convention tracking without supplying a shared geometric formalism.

### 141.15 Aggregate native profile

The thirty-two assigned addresses supply

$$
E_{141}=(120\ \mathrm{English},4\ \mathrm{equations},2\ \mathrm{definitions},139\ \mathrm{dependencies}). \tag{141.15}
$$

Equation (141.15) is DETERMINISTIC_COVERAGE_EVIDENCE. The native evidence is unevenly concentrated.

### 141.16 Coverage distribution

The coverage split is

$$
N_{\mathrm{MEDIUM}}=3,qquad N_{\mathrm{THIN}}=29,qquad N_H=32. \tag{141.16}
$$

Equation (141.16) is DETERMINISTIC_COVERAGE_EVIDENCE. The two definition addresses and No-Hair Theorem are MEDIUM.

### 141.17 Proof profile

No coherent theorem-proof unit is present,

$$
N_{\mathrm{theorem/proof}}=0. \tag{141.17}
$$

Equation (141.17) is DETERMINISTIC_COVERAGE_EVIDENCE. The T4, T5, and T7 theorem titles therefore remain NOT_PROVED.

### 141.18 Convention-source boundary

Both notation-and-conventions appendix addresses have zero substantive units,

$$
E_{@\mathrm{appendix\_1\_notation\_and\_conventions}}=E_{@\mathrm{appendix\_a\_notation\_and\_conventions}}=(0,0,0). \tag{141.18}
$$

Equation (141.18) is DETERMINISTIC_COVERAGE_EVIDENCE. This appendix does not attribute its external conventions to those empty records.

### 141.19 API-status profile

All assigned handles are declared,

$$
N_{\mathrm{DECLARED}}=32. \tag{141.19}
$$

Equation (141.19) is DETERMINISTIC_COVERAGE_EVIDENCE. Declaration does not settle sign, signature, dimension, or proof status.

### 141.20 Open geometry obligations

The unresolved work is

$$
\begin{aligned}
\Omega_{141}=\{&\mathrm{Dimensions,Signatures,Coordinates,Metrics,Connections,CurvatureSigns},\\
&\mathrm{Orientations,BundleTypes,ProjectionMaps,Units,BoundaryConditions,Proofs}\}. \tag{141.20}
\end{aligned}
$$

Equation (141.20) is CURATOR_SYNTHESIS. Exact MK-43 conventions must be recovered source by source before formulas are unified.

### 141.21 Chapter determination

The appendix result is

$$
\begin{aligned}
\mathrm{Geometry}_{141}={}&\mathrm{THIRTY\_TWO\_DECLARED\_ADDRESSES}\\
&+\mathrm{EXPLICIT\_EXTERNAL\_CONVENTIONS}+\mathrm{SIGN\_AND\_TYPE\_BOUNDARIES}\\
&+\mathrm{NO\_SILENT\_UNIFICATION}. \tag{141.21}
\end{aligned}
$$

Equation (141.21) is DETERMINISTIC_STATUS_NORMALIZATION. V18-C07 provides a comparison grammar without inventing a single universal MK-43 geometry.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@amplitude_geometry` | @amplitude_geometry` — Amplitude Geometry | THIN | 6 / 0 / 0 | chapter-core object |
| `@appendix_1_notation_and_conventions` | @appendix_1_notation_and_conventions` — Appendix 1: Notation and Conventions | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_21` | @appendix_21` — Appendix 21 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_28` | @appendix_28` — Appendix 28 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_29` | @appendix_29` — Appendix 29 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_43` | @appendix_43` — Appendix 43 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_44` | @appendix_44` — Appendix 44 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_46` | @appendix_46` — Appendix 46 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_6` | @appendix_6` — Appendix 6 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_a_notation_and_conventions` | @appendix_a_notation_and_conventions` — Appendix A: Notation and Conventions | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_ax` | @appendix_ax` — Appendix AX | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_be` | @appendix_be` — Appendix BE | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_bj` | @appendix_bj` — Appendix BJ | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_by` | @appendix_by` — Appendix BY | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_d_er_bridge_geometry` | @appendix_d_er_bridge_geometry` — Appendix D: ER-Bridge Geometry | THIN | 1 / 0 / 0 | chapter-core object |
| `@appendix_e` | @appendix_e` — Appendix E | THIN | 2 / 0 / 0 | chapter-core object |
| `@appendix_j` | @appendix_j` — Appendix J | THIN | 0 / 0 / 0 | chapter-core object |
| `@axiom_3_1_phase_geometry` | @axiom_3_1_phase_geometry` — Axiom 3.1 — Phase Geometry | THIN | 14 / 0 / 0 | chapter-core object |
| `@definition_10_2_structured_nothingness` | @definition_10_2_structured_nothingness` — Definition 10.2 — Structured Nothingness | MEDIUM | 2 / 0 / 0 | chapter-core object |
| `@definition_13_1_chirality` | @definition_13_1_chirality` — Definition 13.1 — Chirality | MEDIUM | 7 / 0 / 0 | chapter-core object |
| `@lemma_l5` | @lemma_l5` — Lemma L5 — Projection Residue Bundle | THIN | 4 / 0 / 0 | chapter-core object |
| `@lemma_l9` | @lemma_l9` — Lemma L9 — Amplitude Geometry | THIN | 6 / 0 / 0 | chapter-core object |
| `@no_hair_theorem` | @no_hair_theorem | MEDIUM | 49 / 4 / 139 | chapter-core object |
| `@prime_axiom_a0` | Axiom A0 — Prime Existence | THIN | 0 / 0 / 0 | chapter-core object |
| `@prime_definition_d11` | Definition D11 — Well-Founded Dependency Region | THIN | 1 / 0 / 0 | chapter-core object |
| `@prime_definition_d3` | Definition D3 — Node | THIN | 4 / 0 / 0 | chapter-core object |
| `@prime_primitive_p6` | Primitive P6 — Dependency Composition | THIN | 4 / 0 / 0 | chapter-core object |
| `@prime_theorem_t4` | Theorem T4 — Functional Representation Theorem | THIN | 2 / 0 / 0 | chapter-core object |
| `@prime_theorem_t5` | Theorem T5 — Set Recovery Theorem | THIN | 3 / 0 / 0 | chapter-core object |
| `@prime_theorem_t7` | Theorem T7 — Prime Mathematical Object Theorem, Initial Form | THIN | 5 / 0 / 0 | chapter-core object |
| `@shell_differential_geometry_appendix_b` | @shell_differential_geometry_appendix_b` — Shell Differential Geometry (Appendix B) | THIN | 7 / 0 / 0 | chapter-core object |
| `@superposition_closure` | @superposition_closure` — Superposition Closure | THIN | 3 / 0 / 0 | chapter-core object |
