# VOLUME VII - GRAVITY

## Chapter 59 - Continuity Perturbation

### 59.1 Position in the gravity spine

The API dependency architecture places continuity perturbation between the graviton and Time-Shell projection:

$$
@\mathrm{graviton}
\longrightarrow @\mathrm{continuity\_perturbation}
\longrightarrow @\mathrm{time\_shell\_projection\_operator}
\longrightarrow @\mathrm{weak\_field\_metric\_perturbation}. \tag{59.1}
$$

Equation (59.1) is DETERMINISTIC_API_EVIDENCE. The intermediate node prevents a silent identification of the graviton with a metric tensor. It also states the central mathematical-development requirement: an independently defined continuity perturbation must exist before projection.

### 59.2 Exact projection handoff

The recovered equation is

$$
\Pi_T(\delta C)=h_{\mu\nu}. \tag{59.2}
$$

Equation (59.2) is EXACT_SOURCE. It identifies the output of a Time-Shell projection while leaving the type of \(C\), admissible perturbation space, kernel of \(\Pi_T\), and uniqueness of \(h_{\mu\nu}\) unresolved. This equation is the current exact bridge, not a proof of the missing upstream construction of \(\delta C\).

### 59.3 Perturbation as a tangent vector

For a one-parameter family \(C(\epsilon)\), the perturbation is conventionally

$$
\delta C
=\left.\frac{d}{d\epsilon}C(\epsilon)\right|_{\epsilon=0}
\in T_{C_0}\mathcal C. \tag{59.3}
$$

Equation (59.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. It supplies a typing target: \(\mathcal C\) must be a configuration space and \(C_0\) a background configuration. Without these objects, \(\delta C\) is suggestive notation rather than a complete perturbative variable.

### 59.4 Linearization of a nonlinear map

For a differentiable map \(F:\mathcal C\to\mathcal Y\),

$$
F(C_0+\epsilon\delta C)
=F(C_0)+\epsilon\,DF_{C_0}[\delta C]+O(\epsilon^2). \tag{59.4}
$$

Equation (59.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. A projection law is genuinely linear only when its Fréchet derivative, background, and remainder control are specified. The symbol \(\Pi_T\) may instead be nonlinear before perturbative restriction.

### 59.5 Continuity equation target

For a conserved current,

$$
\nabla_\mu J^\mu=0. \tag{59.5}
$$

Equation (59.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. If “continuity” refers to current conservation, \(C\) must be linked to a current, density, or flux. If it refers to topological or geometric continuity, the governing object and invariant must be stated separately.

### 59.6 Linearized conservation

Varying a conserved current around a background gives

$$
\delta(\nabla_\mu J^\mu)
=\bar\nabla_\mu\delta J^\mu
+\delta\Gamma^\mu_{\mu\nu}\,\bar J^\nu=0. \tag{59.6}
$$

Equation (59.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. It shows that perturbing continuity generally couples the current perturbation to the connection perturbation. A native continuity tensor cannot be assumed independent of the background geometry.

### 59.7 Metric perturbation

The readable metric is decomposed as

$$
g_{\mu\nu}=\bar g_{\mu\nu}+h_{\mu\nu},
\qquad |h_{\mu\nu}|\ll1. \tag{59.7}
$$

Equation (59.7) is EXTERNAL_ESTABLISHED_MATHEMATICS as a weak-field expansion. @linear_metric_perturbation is MEDIUM and dominates the chapter evidence. Equation (59.2) supplies a candidate origin for \(h_{\mu\nu}\), but the background and norm defining smallness remain realization-specific.

### 59.8 Inverse metric variation

To first order,

$$
\delta g^{\mu\nu}=-h^{\mu\nu},
\qquad
h^{\mu\nu}=\bar g^{\mu\alpha}\bar g^{\nu\beta}h_{\alpha\beta}. \tag{59.8}
$$

Equation (59.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. Index raising is performed with the background at linear order. A phase perturbation and a metric perturbation cannot be exchanged without an explicit map preserving tensor type.

### 59.9 Connection perturbation

For the Levi-Civita connection,

$$
\delta\Gamma^{\rho}_{\mu\nu}
=\frac12\bar g^{\rho\sigma}
\left(
\bar\nabla_\mu h_{\nu\sigma}
+\bar\nabla_\nu h_{\mu\sigma}
-\bar\nabla_\sigma h_{\mu\nu}
\right). \tag{59.9}
$$

Equation (59.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. It makes the downstream consequence of Equation (59.2) explicit: the projected field changes parallel transport and therefore curvature.

### 59.10 Linearized curvature

The first variation of the Riemann tensor is

$$
\delta R^{\rho}{}_{\sigma\mu\nu}
=\bar\nabla_\mu\delta\Gamma^{\rho}_{\nu\sigma}
-\bar\nabla_\nu\delta\Gamma^{\rho}_{\mu\sigma}. \tag{59.10}
$$

Equation (59.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. The resulting curvature is a derivative consequence of the projected metric perturbation, not an additional identity assigned to \(\delta C\).

### 59.11 Gauge transformation

An infinitesimal coordinate change gives

$$
h_{\mu\nu}\mapsto
h_{\mu\nu}+\bar\nabla_\mu\xi_\nu+\bar\nabla_\nu\xi_\mu. \tag{59.11}
$$

Equation (59.11) is EXTERNAL_ESTABLISHED_MATHEMATICS. A valid projection must either descend to gauge-equivalence classes or specify a gauge. Otherwise different representatives of the same geometry could be mistaken for distinct physical perturbations.

### 59.12 Linearized Einstein compatibility

The standard weak-field requirement is

$$
\delta G_{\mu\nu}[h]
=8\pi G_{\!N}\,\delta T_{\mu\nu},
\qquad
\bar\nabla^\mu\delta G_{\mu\nu}=0. \tag{59.12}
$$

Equation (59.12) is EXTERNAL_ESTABLISHED_MATHEMATICS. The linearized Bianchi identity imposes conservation compatibility. A projected \(h_{\mu\nu}\) that violates it cannot serve as an unconstrained gravitational perturbation without additional source or correction terms.

### 59.13 Typed continuity-projection contract

A minimal contract is

$$
\begin{aligned}
\delta C&\in T_{C_0}\mathcal C_{\mathrm{admissible}},\\
\Pi_T:T_{C_0}\mathcal C_{\mathrm{admissible}}
&\longrightarrow
\Gamma(S^2T^*M)/\mathcal G,\\
\delta C&\longmapsto[h_{\mu\nu}].
\end{aligned} \tag{59.13}
$$

Equation (59.13) is DETERMINISTIC_TYPE_NORMALIZATION, not a recovered definition. It states the missing domain, symmetric-tensor codomain, and gauge quotient. The actual native continuity space remains a critical open construction.

### 59.14 Coverage calibration

The Library assignment has

$$
N_{\mathrm{assigned}}=2,
\qquad N_{\mathrm{MEDIUM}}=1,
\qquad N_{\mathrm{THIN}}=1. \tag{59.14}
$$

Equation (59.14) is DETERMINISTIC_COVERAGE_EVIDENCE. Together the handles contain 1,263 English units, seven indexed equation units, and 697 dependencies. @linear_metric_perturbation supplies all indexed equations and dependencies; @metric_and_phase_perturbations has seven English units and no equation units.

### 59.15 API evidence register

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@linear_metric_perturbation` | @linear_metric_perturbation | MEDIUM | 1256 / 7 / 697 | chapter-core object |
| `@metric_and_phase_perturbations` | @metric_and_phase_perturbations` — Metric and phase perturbations | THIN | 7 / 0 / 0 | chapter-core object |

Neither handle has coverage_v2 definition or theorem/proof units. The dense graph around linear metric perturbation must not be mistaken for an exact construction of the upstream continuity perturbation.

### 59.16 Scope boundary

The evidentiary distinction is

$$
\mathrm{PhasePerturbation}
\not\equiv
\mathrm{ContinuityPerturbation}
\not\equiv
\mathrm{MetricPerturbation}. \tag{59.16}
$$

Equation (59.16) is EVIDENCE_BOUNDARY. Exact maps may relate the objects, but their domains and tensor roles remain distinct. Equation (59.2) supports the second map only at the stated projection boundary.

### 59.17 Open continuity obligations

The remaining requirements are

$$
\begin{aligned}
\mathfrak U_{\delta C}=\{&
\mathrm{NativeConfigurationSpace},\mathrm{BackgroundState},
\mathrm{IndependentGenerationLaw},\mathrm{TensorType},
\mathrm{Dimensions},\\
&\mathrm{ConstraintAndConservationLaw},\mathrm{ProjectionKernel},
\mathrm{GaugeCompatibility},\mathrm{Uniqueness},
\mathrm{Stability},\\
&\mathrm{EinsteinCompatibility},\mathrm{SourceCoupling},
\mathrm{NonlinearExtension},\mathrm{Validation}\}.
\end{aligned} \tag{59.17}
$$

Equation (59.17) is CURATOR_SYNTHESIS. It preserves the critical development lane: continuity-tensor generation must be established independently before TT or readable-metric projection.

### 59.18 Chapter determination

The result is

$$
\begin{aligned}
\mathrm{ContinuityPerturbation}_{\mathrm{V07C03}}
={}&\mathrm{EXACT\_PROJECTION\_OUTPUT}\\
&+\mathrm{DENSE\_METRIC\_EVIDENCE}\\
&+\mathrm{UPSTREAM\_GENERATION\_OPEN}.
\end{aligned} \tag{59.18}
$$

Equation (59.18) is DETERMINISTIC_STATUS_NORMALIZATION. Continuity perturbation is a required and nonredundant bridge in the recovered gravity architecture. Its projection to metric perturbation is exact source evidence; its independent native definition, generation, constraints, typing, and proofs remain unresolved.
