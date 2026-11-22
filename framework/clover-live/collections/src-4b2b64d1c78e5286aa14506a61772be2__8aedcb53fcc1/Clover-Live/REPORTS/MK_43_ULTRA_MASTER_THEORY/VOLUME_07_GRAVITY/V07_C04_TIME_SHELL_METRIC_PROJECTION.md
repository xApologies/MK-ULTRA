# VOLUME VII - GRAVITY

## Chapter 60 - Time-Shell Metric Projection

### 60.1 The projection position

The API gravity spine preserves the metric handoff as

$$
\begin{aligned}
@\mathrm{continuity\_perturbation}
&\longrightarrow @\mathrm{time\_shell\_projection\_operator}\\
&\longrightarrow @\mathrm{weak\_field\_metric\_perturbation}
\longrightarrow @\mathrm{projected\_spacetime\_metric}.
\end{aligned} \tag{60.1}
$$

Equation (60.1) is DETERMINISTIC_API_EVIDENCE. Time-Shell projection is an intermediate construction, not whole-object identity. The projected spacetime metric remains distinct from the broader Time Shell and from its upstream continuity input.

### 60.2 Exact perturbative projection

The recovered source equation is

$$
\Pi_T(\delta C)=h_{\mu\nu}. \tag{60.2}
$$

Equation (60.2) is EXACT_SOURCE. It assigns a symmetric metric perturbation as projection output. The domain, kernel, gauge quotient, and nonlinear extension of \(\Pi_T\) remain unresolved, so the equation is not silently promoted into a complete metric-construction theorem.

### 60.3 Exact readable metric

The second recovered source equation is

$$
g_{\mu\nu}=\bar g_{\mu\nu}+h_{\mu\nu}. \tag{60.3}
$$

Equation (60.3) is EXACT_SOURCE. The background \(\bar g_{\mu\nu}\) and projected perturbation \(h_{\mu\nu}\) are separate inputs to the readable metric. Their sum does not identify the background, perturbation, and full geometry.

### 60.4 Metric axioms

A pseudo-Riemannian metric is a smooth, symmetric, nondegenerate tensor

$$
g\in\Gamma(S^2T^*M),
\qquad g_{\mu\nu}=g_{\nu\mu},
\qquad \det(g_{\mu\nu})\ne0. \tag{60.4}
$$

Equation (60.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. A native projection must land in this admissible space and preserve the chosen signature. An arbitrary tensor output does not yet define readable spacetime geometry.

### 60.5 Signature stability

For a sufficiently small perturbation, signature is preserved if the metric remains nondegenerate:

$$
\det(\bar g+h)\ne0,
\qquad
\operatorname{signature}(\bar g+h)
=\operatorname{signature}(\bar g). \tag{60.5}
$$

Equation (60.5) is EXTERNAL_ESTABLISHED_MATHEMATICS locally under controlled variation. @metric_signature is a distinct address because signature is an admissibility condition, not a decorative convention.

### 60.6 Inverse metric

The inverse is defined by

$$
g^{\mu\alpha}g_{\alpha\nu}=\delta^\mu{}_{\nu},
\qquad
g^{\mu\nu}=\bar g^{\mu\nu}-h^{\mu\nu}+O(h^2). \tag{60.6}
$$

Equation (60.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. @inverse_metric has MEDIUM coverage with 566 English units, six indexed equations, and 654 dependencies. The inverse must be derived from the projected metric rather than introduced as an unrelated field.

### 60.7 Metric-compatible connection

For the Levi-Civita connection,

$$
\nabla_\rho g_{\mu\nu}=0,
\qquad
\Gamma^{\rho}_{\mu\nu}
=\frac12g^{\rho\sigma}
(\partial_\mu g_{\nu\sigma}+\partial_\nu g_{\mu\sigma}-\partial_\sigma g_{\mu\nu}). \tag{60.7}
$$

Equation (60.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. @metric_compatibility and @metric_compatible_connection are preserved separately: the former is a condition; the latter is the connection satisfying it under stated assumptions.

### 60.8 Induced metric

For an embedding \(X:\Sigma\to M\), the induced metric is

$$
\gamma_{ab}
=g_{\mu\nu}(X)\,\partial_aX^\mu\partial_bX^\nu. \tag{60.8}
$$

Equation (60.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. If a Time Shell is treated as a boundary or hypersurface, its intrinsic metric must be distinguished from the bulk metric and from a projection map that produces a bulk-readable perturbation.

### 60.9 Composite metric discipline

A composite metric may be organized schematically as

$$
g_{\mathrm{comp}}
=g_{\mathrm{base}}+\Delta g_{\mathrm{phase}}+\Delta g_{\mathrm{ER}}+Delta g_{\mathrm{other}}, \tag{60.9}
$$

where every term is a symmetric covariant two-tensor on the same manifold. Equation (60.9) is EXTERNAL_ESTABLISHED_MATHEMATICS as a tensor-sum requirement, not a recovered MK-43 formula. The Library addresses @composite_metric, @phase_metric_contribution, and @er_metric_contribution must remain separate until exact source coefficients and maps are isolated.

### 60.10 Phase contribution

For a phase scalar \(\theta\), a candidate geometric contribution could only enter a metric after a typed construction such as

$$
\Delta g^{(\theta)}_{\mu\nu}
=F_{\mu\nu}(\theta,\nabla\theta,\nabla^2\theta;\bar g). \tag{60.10}
$$

Equation (60.10) is EXTERNAL_ESTABLISHED_MATHEMATICS as a general tensor-functional form. It does not choose \(F\) or claim that the recovered @phase_metric equals this expression. Covariance, symmetry, dimensions, and signature preservation constrain any exact realization.

### 60.11 Metric variation

The variation of the volume density is

$$
\delta\sqrt{|g|}
=\frac12\sqrt{|g|}\,g^{\mu\nu}\delta g_{\mu\nu}. \tag{60.11}
$$

Equation (60.11) is EXTERNAL_ESTABLISHED_MATHEMATICS. @metric_variation is MEDIUM with 691 English units, six indexed equations, and 825 dependencies. Variation provides the bridge from a projected metric to dynamics only after an action functional is specified.

### 60.12 Temporal and spatial metrics

In an ADM-type split,

$$
ds^2=-N^2dt^2+\gamma_{ij}(dx^i+N^idt)(dx^j+N^jdt). \tag{60.12}
$$

Equation (60.12) is EXTERNAL_ESTABLISHED_MATHEMATICS. Temporal metric language, spatial geometry, lapse, and shift occupy different roles. A phase-to-time interpretation does not by itself fix this decomposition.

### 60.13 Homogeneous and axisymmetric specializations

A homogeneous-isotropic metric may take the form

$$
ds^2=-dt^2+a(t)^2\left(\frac{dr^2}{1-kr^2}+r^2d\Omega^2\right), \tag{60.13}
$$

while an axisymmetric geometry admits a rotational Killing vector \(\varphi^\mu\) satisfying

$$
\mathcal L_{\varphi}g_{\mu\nu}=0. \tag{60.14}
$$

Equations (60.13) and (60.14) are EXTERNAL_ESTABLISHED_MATHEMATICS. These are specialization targets, not universal forms of the Time-Shell projection. The projection should commute with imposed symmetries only when that property is proved.

### 60.14 Typed projection contract

A minimal metric compilation route is

$$
\begin{aligned}
\Pi_T:T_{C_0}\mathcal C_{\mathrm{admissible}}
&\longrightarrow \Gamma(S^2T^*M)/\mathcal G,\\
\delta C&\longmapsto[h],\\
(\bar g,[h])&\longmapsto[g=\bar g+h].
\end{aligned} \tag{60.15}
$$

Equation (60.15) is DETERMINISTIC_TYPE_NORMALIZATION. It is not a recovered complete definition. It exposes the domain, gauge-reduced tensor codomain, background requirement, and compilation step that must be supplied by native mathematics.

### 60.15 Coverage calibration

The Library assignment contains

$$
N_{\mathrm{assigned}}=36,
\qquad N_{\mathrm{MEDIUM}}=16,
\qquad N_{\mathrm{THIN}}=20. \tag{60.16}
$$

Equation (60.16) is DETERMINISTIC_COVERAGE_EVIDENCE. The handles contain 5,463 English units, 71 indexed equation units, two definition units, and 5,662 dependencies. @metric_tensor dominates with 1,392 English units; @projected_spacetime_metric contributes 571 English units, seven equations, and 565 dependencies.

### 60.16 API evidence register

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@axiom_a9` | @axiom_a9` — Axiom A9 — Hermitian Metric | THIN | 11 / 0 / 0 | chapter-core object |
| `@axisymmetric_spacetime` | @axisymmetric_spacetime | MEDIUM | 38 / 4 / 185 | chapter-core object |
| `@background_metric` | @background_metric | MEDIUM | 493 / 6 / 596 | chapter-core object |
| `@bio_geometric_functional` | @bio_geometric_functional` — Bio-geometric functional | THIN | 13 / 0 / 0 | chapter-core object |
| `@chapter_49_adapter_geometric_infrastructure_and_phase_supported_architecture` | @chapter_49_adapter_geometric_infrastructure_and_phase_supported_architecture` — Chapter 49 Adapter — Geometric Infrastructure and Phase-Supported Architecture | THIN | 16 / 0 / 0 | chapter-core object |
| `@composite_metric` | @composite_metric` — Composite Metric | THIN | 7 / 0 / 0 | chapter-core object |
| `@core_geometric_object` | @core_geometric_object` — Core geometric object | THIN | 11 / 0 / 0 | chapter-core object |
| `@definition_5_1_phase_metric_contribution` | @definition_5_1_phase_metric_contribution` — Definition 5.1 — Phase Metric Contribution | MEDIUM | 5 / 0 / 0 | chapter-core object |
| `@definition_5_2_composite_metric` | @definition_5_2_composite_metric` — Definition 5.2 — Composite Metric | MEDIUM | 5 / 0 / 0 | chapter-core object |
| `@effective_lensing_metric` | @effective_lensing_metric` — Effective lensing metric | THIN | 6 / 0 / 0 | chapter-core object |
| `@er_graph_distance_to_effective_metric` | @er_graph_distance_to_effective_metric` — ER graph distance to effective metric | THIN | 10 / 0 / 0 | chapter-core object |
| `@er_metric_contribution` | @er_metric_contribution` — ER metric contribution | THIN | 10 / 0 / 0 | chapter-core object |
| `@geometric` | @geometric | MEDIUM | 44 / 4 / 3 | chapter-core object |
| `@geometric_compilation_route` | @geometric_compilation_route` — Geometric compilation route | THIN | 12 / 0 / 0 | chapter-core object |
| `@geometric_decoherence_functional` | @geometric_decoherence_functional | THIN | 20 / 0 / 0 | chapter-core object |
| `@hermitian_metric` | @hermitian_metric` — Hermitian Metric | THIN | 10 / 0 / 0 | chapter-core object |
| `@homogeneous_isotropic_metric` | @homogeneous_isotropic_metric` — Homogeneous-isotropic metric | THIN | 5 / 0 / 0 | chapter-core object |
| `@induced_metric` | @induced_metric | MEDIUM | 74 / 4 / 212 | chapter-core object |
| `@inverse_metric` | @inverse_metric | MEDIUM | 566 / 6 / 654 | chapter-core object |
| `@linearized_geometric_equation` | @linearized_geometric_equation` — Linearized geometric equation | THIN | 5 / 0 / 0 | chapter-core object |
| `@linearized_phase_metric_contribution` | @linearized_phase_metric_contribution` — Linearized phase-metric contribution | THIN | 5 / 0 / 0 | chapter-core object |
| `@metric_compatibility` | @metric_compatibility | MEDIUM | 47 / 4 / 185 | chapter-core object |
| `@metric_compatible_connection` | @metric_compatible_connection` — Metric-Compatible Connection | MEDIUM | 561 / 8 / 434 | chapter-core object |
| `@metric_signature` | @metric_signature | MEDIUM | 52 / 4 / 179 | chapter-core object |
| `@metric_tensor` | @metric_tensor | MEDIUM | 1392 / 7 / 964 | chapter-core object |
| `@metric_variation` | @metric_variation | MEDIUM | 691 / 6 / 825 | chapter-core object |
| `@module_3_metric_composition` | @module_3_metric_composition` — Module 3 — Metric Composition | THIN | 8 / 0 / 0 | chapter-core object |
| `@phase_metric` | @phase_metric` — Phase metric | MEDIUM | 73 / 1 / 15 | chapter-core object |
| `@phase_metric_and_time_as_geometry` | @phase_metric_and_time_as_geometry` — Phase Metric and Time as Geometry | THIN | 1 / 0 / 0 | chapter-core object |
| `@phase_metric_contribution` | @phase_metric_contribution` — Phase Metric Contribution | THIN | 3 / 0 / 0 | chapter-core object |
| `@primitive_p1` | @primitive_p1` — Primitive P1 — Temporal Metric | THIN | 8 / 0 / 0 | chapter-core object |
| `@primitive_p13` | @primitive_p13` — Primitive P13 — Hermitian Metric | THIN | 8 / 0 / 0 | chapter-core object |
| `@projected_spacetime_metric` | @projected_spacetime_metric` — Projected Spacetime Metric | MEDIUM | 571 / 7 / 565 | chapter-core object |
| `@recovered_geometric` | @recovered_geometric | THIN | 1 / 0 / 0 | chapter-core object |
| `@temporal_metric` | @temporal_metric` — Temporal Metric | MEDIUM | 127 / 4 / 181 | chapter-core object |
| `@vacuum_wave_equation` | @vacuum_wave_equation | MEDIUM | 554 / 6 / 664 | chapter-core object |

The register preserves general metrics, phase and ER contributions, induced and inverse metrics, symmetry reductions, compilation routes, projection output, and vacuum-wave structure. Co-occurring equation IDs are not counted as independent derivations.

### 60.17 Projection versus composition

The central boundary is

$$
\begin{aligned}
\mathrm{TimeShell}&\ne\mathrm{ProjectedMetric},\\
\mathrm{ProjectionOperator}&\ne\mathrm{MetricPerturbation},\\
\mathrm{PhaseContribution}&\ne\mathrm{CompleteMetric}.
\end{aligned} \tag{60.18}
$$

Equation (60.18) is EVIDENCE_BOUNDARY. Relations among these objects can be exact without collapsing identity, operation, contribution, and result.

### 60.18 Open metric-projection obligations

The unresolved requirements are

$$
\begin{aligned}
\mathfrak U_{\Pi_T}=\{&
\mathrm{ProjectionDomain},\mathrm{KernelAndImage},
\mathrm{BackgroundSelection},\mathrm{GaugeQuotient},
\mathrm{SignaturePreservation},\\
&\mathrm{PhaseMetricFunctional},\mathrm{ERMetricFunctional},
\mathrm{CompositionCoefficients},\mathrm{MetricCompatibility},
\mathrm{SymmetryCompatibility},\\
&\mathrm{NonlinearCompletion},\mathrm{ActionAndVariation},
\mathrm{Uniqueness},\mathrm{Stability},
\mathrm{ObservationalValidation}\}.
\end{aligned} \tag{60.19}
$$

Equation (60.19) is CURATOR_SYNTHESIS. It records missing mathematics rather than supplying it. The still-unresolved Time-Shell intertwining equation is not silently replaced by the narrower exact projection in Equation (60.2).

### 60.19 Chapter determination

The result is

$$
\begin{aligned}
\mathrm{TimeShellMetricProjection}_{\mathrm{V07C04}}
={}&\mathrm{EXACT\_PERTURBATIVE\_HANDOFF}\\
&+\mathrm{RECOVERED\_METRIC\_ADDRESS\_SPACE}\\
&+\mathrm{OPEN\_COMPOSITION\_AND\_TYPING}.
\end{aligned} \tag{60.20}
$$

Equation (60.20) is DETERMINISTIC_STATUS_NORMALIZATION. The corpus recovers a substantive projection boundary from continuity perturbation to readable metric geometry. It does not yet recover the complete phase/ER composite metric, the global projection intertwiner, or proofs of admissibility, uniqueness, and stability.
