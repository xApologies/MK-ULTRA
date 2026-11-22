# VOLUME VII - GRAVITY

## Chapter 61 - Weak-Field Metric and Curvature

### 61.1 From projected metric to curvature

The weak-field regime begins with a background metric and a small symmetric perturbation,

$$
g_{\mu\nu}=\bar g_{\mu\nu}+h_{\mu\nu},
\qquad |h_{\mu\nu}|_{\bar g}\ll 1. \tag{61.1}
$$

Equation (61.1) is EXTERNAL_ESTABLISHED_MATHEMATICS. In the TOME sequence, the prior Time-Shell projection chapter supplies the candidate perturbative output \(h_{\mu\nu}\); this chapter asks what geometric structures follow once that output is admitted as a metric perturbation. It does not identify the Time Shell, the projection operator, the perturbation, and curvature.

### 61.2 Perturbative order

Introduce a bookkeeping parameter \(\varepsilon\):

$$
g_{\mu\nu}(\varepsilon)=\bar g_{\mu\nu}+\varepsilon h_{\mu\nu}+O(\varepsilon^2),
\qquad
\delta X=\left.\frac{dX(\varepsilon)}{d\varepsilon}\right|_{\varepsilon=0}. \tag{61.2}
$$

Equation (61.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. Linearized quantities are first variations at a fixed background. A result valid at \(O(\varepsilon)\) is not silently promoted to a nonlinear curvature law.

### 61.3 Inverse-metric variation

The first inverse-metric variation is

$$
g^{\mu\nu}=\bar g^{\mu\nu}-\varepsilon h^{\mu\nu}+O(\varepsilon^2),
\qquad
h^{\mu\nu}=\bar g^{\mu\alpha}\bar g^{\nu\beta}h_{\alpha\beta}. \tag{61.3}
$$

Equation (61.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. Raising an index with the background metric is part of the perturbative convention and must not be confused with using the unknown full inverse metric.

### 61.4 Connection perturbation

For the Levi-Civita connection of the background,

$$
\delta\Gamma^{\rho}{}_{\mu\nu}
=\frac12\bar g^{\rho\sigma}
\left(\bar\nabla_\mu h_{\nu\sigma}
+\bar\nabla_\nu h_{\mu\sigma}
-\bar\nabla_\sigma h_{\mu\nu}\right). \tag{61.4}
$$

Equation (61.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. It supplies the exact linear bridge from a metric perturbation to a connection perturbation. The Library keeps @connection_and_curvature and @connection_to_formal_curvature_bundle distinct because a conceptual pairing is not itself a typed bundle construction.

### 61.5 Linearized Riemann curvature

The corresponding first variation of the Riemann tensor is

$$
\delta R^{\rho}{}_{\sigma\mu\nu}
=\bar\nabla_\mu\delta\Gamma^{\rho}{}_{\nu\sigma}
-\bar\nabla_\nu\delta\Gamma^{\rho}{}_{\mu\sigma}. \tag{61.5}
$$

Equation (61.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. Curvature is therefore second order in derivatives of the metric perturbation at linear order. It is not an additional independent field once the metric connection is fixed.

### 61.6 Linearized Ricci tensor

Contraction gives

$$
\delta R_{\mu\nu}
=\frac12\left(
\bar\nabla_\rho\bar\nabla_\mu h^{\rho}{}_{\nu}
+\bar\nabla_\rho\bar\nabla_\nu h^{\rho}{}_{\mu}
-\bar\Box h_{\mu\nu}
-\bar\nabla_\mu\bar\nabla_\nu h
\right), \tag{61.6}
$$

where \(h=\bar g^{\mu\nu}h_{\mu\nu}\) and curvature-commutator terms must be retained when the background is not flat. Equation (61.6) is EXTERNAL_ESTABLISHED_MATHEMATICS in the displayed derivative ordering.

### 61.7 Linearized scalar curvature

The scalar variation is

$$
\delta R
=\bar\nabla_\mu\bar\nabla_\nu h^{\mu\nu}
-\bar\Box h
-h^{\mu\nu}\bar R_{\mu\nu}. \tag{61.7}
$$

Equation (61.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. The background-curvature term shows why a flat-background formula cannot be copied unchanged into an arbitrary geometry.

### 61.8 Linearized Einstein tensor

The geometric response is

$$
\delta G_{\mu\nu}
=\delta R_{\mu\nu}
-\frac12\bar g_{\mu\nu}\delta R
-\frac12 h_{\mu\nu}\bar R. \tag{61.8}
$$

Equation (61.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. It prepares the next chapter's Einstein sector but does not yet specify a stress-energy source or an MK-43 constitutive law.

### 61.9 Curvature two-form

In an orthonormal-frame description, a connection one-form \(\omega^{a}{}_{b}\) has curvature two-form

$$
\Omega^{a}{}_{b}
=d\omega^{a}{}_{b}
+\omega^{a}{}_{c}\wedge\omega^{c}{}_{b}. \tag{61.9}
$$

Equation (61.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. @curvature_two_form is an independent address because the differential-form representation retains frame and bundle structure not visible in an untyped use of the word curvature.

### 61.10 Bianchi identity

The curvature two-form obeys

$$
D\Omega^{a}{}_{b}=0,
\qquad
\nabla_{[\lambda}R^{\rho}{}_{|\sigma|\mu\nu]}=0. \tag{61.10}
$$

Equation (61.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. This identity constrains any candidate curvature binding. A proposed binding that violates it cannot represent the curvature of a compatible connection without additional structure.

### 61.11 Extrinsic curvature

For a hypersurface with induced metric \(\gamma_{ab}\), unit normal \(n^\mu\), and projected derivative \(D_a\),

$$
K_{ab}=\gamma_a{}^{\mu}\gamma_b{}^{\nu}\nabla_\mu n_\nu
=\frac12\mathcal L_n\gamma_{ab} \tag{61.11}
$$

up to the declared sign convention. Equation (61.11) is EXTERNAL_ESTABLISHED_MATHEMATICS. @extrinsic_curvature measures embedding, not the intrinsic curvature of the hypersurface.

### 61.12 Gauss relation

Intrinsic and ambient curvature are related by

$$
{}^{(\Sigma)}R_{abcd}
=\gamma_a{}^{\mu}\gamma_b{}^{\nu}\gamma_c{}^{\rho}\gamma_d{}^{\sigma}
R_{\mu\nu\rho\sigma}
+K_{ac}K_{bd}-K_{ad}K_{bc}. \tag{61.12}
$$

Equation (61.12) is EXTERNAL_ESTABLISHED_MATHEMATICS for the sign convention of Equation (61.11). It is the disciplined way to compare a shell's intrinsic geometry with bulk-readable curvature.

### 61.13 Sectional curvature

For a nondegenerate two-plane spanned by \(u\) and \(v\),

$$
K(u,v)
=\frac{g(R(u,v)v,u)}
{g(u,u)g(v,v)-g(u,v)^2}. \tag{61.13}
$$

Equation (61.13) is EXTERNAL_ESTABLISHED_MATHEMATICS. @sectional_curvature is a plane-dependent scalar, not a synonym for the full Riemann tensor.

### 61.14 Spatial curvature parameter

For a homogeneous and isotropic spatial slice,

$$
{}^{(3)}R=\frac{6k}{a^2},
\qquad k\in\{-1,0,+1\} \tag{61.14}
$$

under the normalized FLRW convention. Equation (61.14) is EXTERNAL_ESTABLISHED_MATHEMATICS. @spatial_curvature_parameter is a specialization parameter and must not be identified with arbitrary spacetime curvature.

### 61.15 Curvature singularity criterion

A coordinate divergence is not sufficient evidence of a curvature singularity. An invariant diagnostic is the Kretschmann scalar,

$$
\mathcal K=R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}. \tag{61.15}
$$

Equation (61.15) is EXTERNAL_ESTABLISHED_MATHEMATICS. Divergence of \(\mathcal K\) can certify invariant curvature blow-up in a given solution, while finiteness alone need not prove global regularity.

### 61.16 Einstein-field boundary

The established dynamical relation is

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}
=\frac{8\pi G}{c^4}T_{\mu\nu}. \tag{61.16}
$$

Equation (61.16) is EXTERNAL_ESTABLISHED_MATHEMATICS. @einstein_field_equation has the largest evidence population in this chapter, but dependency density is not a recovered proof that a particular MK-43 projection supplies \(T_{\mu\nu}\), \(\Lambda\), or the complete nonlinear metric.

### 61.17 Typed curvature handoff

The minimal deterministic type normalization is

$$
h\in\Gamma(S^2T^*M)
\longmapsto\delta\Gamma
\longmapsto\delta\mathrm{Riem}
\longmapsto(\delta\mathrm{Ric},\delta R,\delta G). \tag{61.17}
$$

Equation (61.17) is DETERMINISTIC_TYPE_NORMALIZATION. It summarizes established differential-geometric constructions. It does not supply a native MK-43 source functional for \(h\), a nonlinear completion, or a proof that any named shell realization satisfies the required regularity assumptions.

### 61.18 Coverage calibration

The Library assignment contains

$$
N_{\mathrm{assigned}}=16,
\qquad N_{\mathrm{MEDIUM}}=10,
\qquad N_{\mathrm{THIN}}=6. \tag{61.18}
$$

Equation (61.18) is DETERMINISTIC_COVERAGE_EVIDENCE. The handles contain 4,024 English units, 42 indexed equation units, zero exact-definition units, and 2,714 registered dependencies. @einstein_field_equation contributes 2,902 English units, eight equations, and 982 dependencies; @weak_field_metric_perturbation contributes 575 English units, eight equations, and 567 dependencies.

### 61.19 API evidence register

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@axiom_a13` | @axiom_a13` — Axiom A13 — Connection and Curvature | THIN | 12 / 0 / 0 | chapter-core object |
| `@connection_and_curvature` | @connection_and_curvature` — Connection and Curvature | THIN | 5 / 0 / 0 | chapter-core object |
| `@connection_to_formal_curvature_bundle` | @connection_to_formal_curvature_bundle | MEDIUM | 36 / 1 / 1 | chapter-core object |
| `@curvature` | @curvature` — Curvature | MEDIUM | 36 / 3 / 52 | chapter-core object |
| `@curvature_binding` | @curvature_binding | MEDIUM | 154 / 5 / 193 | chapter-core object |
| `@curvature_singularity` | @curvature_singularity | MEDIUM | 49 / 4 / 139 | chapter-core object |
| `@curvature_two_form` | @curvature_two_form | MEDIUM | 39 / 4 / 184 | chapter-core object |
| `@einstein_field_equation` | @einstein_field_equation | MEDIUM | 2902 / 8 / 982 | chapter-core object |
| `@einstein_field_relation` | @einstein_field_relation` — Einstein Field Relation | THIN | 11 / 0 / 0 | chapter-core object |
| `@entanglement_curvature_ansatz` | @entanglement_curvature_ansatz` — Entanglement-curvature ansatz | THIN | 6 / 0 / 0 | chapter-core object |
| `@extrinsic_curvature` | @extrinsic_curvature | MEDIUM | 65 / 3 / 212 | chapter-core object |
| `@primitive_p15` | @primitive_p15` — Primitive P15 — Curvature | THIN | 8 / 0 / 0 | chapter-core object |
| `@sectional_curvature` | @sectional_curvature | MEDIUM | 39 / 3 / 181 | chapter-core object |
| `@spatial_curvature_parameter` | @spatial_curvature_parameter | MEDIUM | 72 / 3 / 203 | chapter-core object |
| `@weak_field_metric_perturbation` | @weak_field_metric_perturbation` — Weak-Field Metric Perturbation | MEDIUM | 575 / 8 / 567 | chapter-core object |
| `@white_core_curvature` | @white_core_curvature` — White-core curvature | THIN | 15 / 0 / 0 | chapter-core object |

The register preserves connection, curvature, weak-field perturbation, intrinsic and extrinsic specializations, Einstein relations, singularity language, and historically scoped curvature candidates. Co-occurring equation IDs are not treated as independent derivations.

### 61.20 Identity and scope boundary

The required distinctions are

$$
\begin{aligned}
\mathrm{MetricPerturbation}&\ne\mathrm{Curvature},\\
\mathrm{CurvatureTwoForm}&\ne\mathrm{SectionalCurvature},\\
\mathrm{IntrinsicCurvature}&\ne\mathrm{ExtrinsicCurvature},\\
\mathrm{EinsteinEquation}&\ne\mathrm{EntanglementCurvatureAnsatz}.
\end{aligned} \tag{61.19}
$$

Equation (61.19) is EVIDENCE_BOUNDARY. @entanglement_curvature_ansatz, @white_core_curvature, @axiom_a13, and @primitive_p15 remain preserved addresses, but their THIN coverage does not establish universal equations, equivalences, or proof status.

### 61.21 Open curvature obligations

The unresolved requirements are

$$
\begin{aligned}
\mathfrak U_{\mathrm{curv}}=\{&
\mathrm{NativeSourceFor}\ h,
\mathrm{ProjectionRegularity},
\mathrm{GaugeFixing},
\mathrm{BackgroundChoice},
\mathrm{NonlinearCompletion},\\
&\mathrm{CurvatureBindingMap},
\mathrm{FormalBundleTyping},
\mathrm{EntanglementCurvatureLaw},
\mathrm{WhiteCoreDefinition},\\
&\mathrm{SingularityResolution},
\mathrm{DimensionsAndNormalization},
\mathrm{Stability},
\mathrm{ObservationalValidation}\}.
\end{aligned} \tag{61.20}
$$

Equation (61.20) is CURATOR_SYNTHESIS. It records missing mathematics without manufacturing it. In particular, a graph dependency or a shared source equation does not prove a curvature-binding mechanism.

### 61.22 Chapter determination

The result is

$$
\begin{aligned}
\mathrm{WeakFieldCurvature}_{\mathrm{V07C05}}
={}&\mathrm{ESTABLISHED\_PERTURBATIVE\_GEOMETRY}\\
&+\mathrm{RECOVERED\_CURVATURE\_ADDRESS\_SPACE}\\
&+\mathrm{OPEN\_NATIVE\_BINDING\_AND\_DYNAMICS}.
\end{aligned} \tag{61.21}
$$

Equation (61.21) is DETERMINISTIC_STATUS_NORMALIZATION. The chapter recovers a coherent route from the projected weak-field metric to connection and curvature objects while retaining every API address. The standard differential geometry is mature; the MK-43-specific source, binding, nonlinear, and validation layers remain open where exact evidence does not close them.
