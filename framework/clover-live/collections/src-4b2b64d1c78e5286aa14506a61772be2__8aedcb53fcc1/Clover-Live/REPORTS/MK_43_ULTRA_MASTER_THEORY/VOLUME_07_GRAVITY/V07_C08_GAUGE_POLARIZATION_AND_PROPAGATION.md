# VOLUME VII - GRAVITY

## Chapter 64 - Gauge, Polarization, and Propagation

### 64.1 Gauge equivalence

A linearized metric perturbation is defined only up to an infinitesimal diffeomorphism:

$$
h_{\mu\nu}
\sim
h_{\mu\nu}
+2\nabla_{(\mu}\xi_{\nu)}. \tag{64.1}
$$

Equation (64.1) is EXTERNAL_ESTABLISHED_MATHEMATICS, with sign fixed by the convention for the coordinate change. Physical wave information belongs to a gauge-equivalence class rather than to arbitrary components of \(h_{\mu\nu}\).

### 64.2 Degree-of-freedom count

In four dimensions, the linearized symmetric tensor begins with ten components. Four coordinate conditions and four constraint or residual-gauge removals leave

$$
10-4-4=2 \tag{64.2}
$$

radiative degrees of freedom in general relativity. Equation (64.2) is EXTERNAL_ESTABLISHED_MATHEMATICS as the standard massless spin-2 count. It is not a count for every modified-gravity or native MK-43 propagation model.

### 64.3 Trace-reversed transformation

For \(\bar h_{\mu\nu}=h_{\mu\nu}-\frac12\eta_{\mu\nu}h\), the gauge transformation is

$$
\bar h'_{\mu\nu}
=\bar h_{\mu\nu}
+\partial_\mu\xi_\nu
+\partial_\nu\xi_\mu
-\eta_{\mu\nu}\partial_\rho\xi^\rho. \tag{64.3}
$$

Equation (64.3) is EXTERNAL_ESTABLISHED_MATHEMATICS for the sign convention of Equation (64.1). Trace reversal changes the algebraic representation, not the physical equivalence class.

### 64.4 Harmonic gauge and residual freedom

The harmonic condition and its residual transformation law are

$$
\partial^\mu\bar h_{\mu\nu}=0,
\qquad
\partial^\mu\bar h'_{\mu\nu}
=\partial^\mu\bar h_{\mu\nu}+\Box\xi_\nu. \tag{64.4}
$$

Equation (64.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. Residual vectors satisfying \(\Box\xi_\nu=0\) preserve the gauge, so harmonic gauge alone does not uniquely specify the perturbation.

### 64.5 Spatial transverse projector

For a unit propagation vector \(n^i\), define

$$
P_{ij}=\delta_{ij}-n_i n_j,
\qquad
P_i{}^kP_{kj}=P_{ij},
\qquad
P_{ij}n^j=0. \tag{64.5}
$$

Equation (64.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. The projector removes the longitudinal spatial component relative to the chosen propagation direction.

### 64.6 TT projector

The symmetric transverse-traceless projector is

$$
\Lambda_{ij,kl}
=P_{i(k}P_{l)j}
-\frac12P_{ij}P_{kl},
\qquad
h^{\mathrm{TT}}_{ij}
=\Lambda_{ij,kl}h_{kl}. \tag{64.6}
$$

Equation (64.6) is EXTERNAL_ESTABLISHED_MATHEMATICS in three spatial dimensions. It exposes the actual projection operation that must not be confused with simply labeling a field TT.

### 64.7 Polarization basis

For orthonormal transverse vectors \(p^i\) and \(q^i\),

$$
e^+_{ij}=p_i p_j-q_i q_j,
\qquad
e^\times_{ij}=p_i q_j+q_i p_j. \tag{64.7}
$$

Equation (64.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. Both tensors are transverse and traceless, and their normalization depends on the declared inner-product convention.

### 64.8 Spin-2 basis rotation

Under a rotation of the transverse basis by angle \(\psi\),

$$
h_+\pm i h_\times
\longmapsto
e^{\mp2i\psi}
\left(h_+\pm i h_\times\right). \tag{64.8}
$$

Equation (64.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. The factor of two encodes spin-2 transformation behavior. A change of polarization basis is not a physical conversion between independent wave species.

### 64.9 Polarization observables

For complex amplitudes \(h_+\) and \(h_\times\), polarization can be summarized by

$$
\begin{aligned}
I&=|h_+|^2+|h_\times|^2,
&Q&=|h_+|^2-|h_\times|^2,\\
U&=2\operatorname{Re}(h_+h_\times^*),
&V&=2\operatorname{Im}(h_+h_\times^*).
\end{aligned} \tag{64.9}
$$

Equation (64.9) is EXTERNAL_ESTABLISHED_MATHEMATICS as a Stokes-like characterization. These quantities describe polarization content after a wave solution and measurement convention have been fixed.

### 64.10 Principal propagation law

The high-frequency phase \(\theta\) defines \(k_\mu=\nabla_\mu\theta\), with leading equations

$$
k^\mu k_\mu=0,
\qquad
k^\nu\nabla_\nu k^\mu=0. \tag{64.10}
$$

Equation (64.10) is EXTERNAL_ESTABLISHED_MATHEMATICS in general-relativistic geometric optics. The principal symbol fixes null characteristics; lower-order curvature terms control amplitude and polarization transport.

### 64.11 Amplitude transport

For scalar amplitude \(A\) along a null congruence,

$$
\nabla_\mu(A^2k^\mu)=0,
\qquad
k^\mu\nabla_\mu\ln A=-\frac12\nabla_\mu k^\mu. \tag{64.11}
$$

Equation (64.11) is EXTERNAL_ESTABLISHED_MATHEMATICS. Focusing or defocusing of the congruence changes amplitude without altering the leading null dispersion relation.

### 64.12 Polarization transport

At geometric-optics order, a normalized polarization tensor \(e_{\mu\nu}\) is parallel transported:

$$
k^\rho\nabla_\rho e_{\mu\nu}=0,
\qquad
k^\mu e_{\mu\nu}=0,
\qquad
g^{\mu\nu}e_{\mu\nu}=0. \tag{64.12}
$$

Equation (64.12) is EXTERNAL_ESTABLISHED_MATHEMATICS under the standard high-frequency expansion. Curvature can rotate the observed basis through transport even when the local polarization tensor remains parallel along the ray.

### 64.13 Retarded solution

For a linear sourced operator \(\mathcal D\), a causal solution has the form

$$
h_{\mu\nu}(x)
=\int_M
G^{\mathrm{ret}}_{\mu\nu}{}^{\rho\sigma}(x,x')
S_{\rho\sigma}(x')\,dV_{x'}. \tag{64.13}
$$

Equation (64.13) is EXTERNAL_ESTABLISHED_MATHEMATICS as a Green-function representation. It separates the wave operator, causal propagator, and source. A native theory must specify all three.

### 64.14 Direct and tail propagation

Locally on a curved spacetime, a retarded Green function can have Hadamard form

$$
G_{\mathrm{ret}}(x,x')
=U(x,x')\delta_+(\sigma)
+V(x,x')\Theta_+(-\sigma). \tag{64.14}
$$

Equation (64.14) is EXTERNAL_ESTABLISHED_MATHEMATICS schematically for a normally hyperbolic operator. The direct term propagates on the null cone, while the tail term records curvature-mediated support inside it.

### 64.15 Gauge-invariant detector curvature

In linearized gravity on a flat background,

$$
R^{(1)}_{0i0j}
=-\frac12\ddot h^{\mathrm{TT}}_{ij}. \tag{64.15}
$$

Equation (64.15) is EXTERNAL_ESTABLISHED_MATHEMATICS in the detector frame. The linearized Riemann tensor supplies a gauge-invariant observable even though the individual components of \(h_{\mu\nu}\) are gauge-dependent.

### 64.16 Typed gauge-to-observation contract

The disciplined chain is

$$
[h]_{\mathrm{gauge}}
\longmapsto
h^{\mathrm{TT}}
\longmapsto
\big(e_+,e_\times\big)
\longmapsto
\mathrm{PropagatedCurvature}
\longmapsto
\mathrm{DetectorResponse}. \tag{64.16}
$$

Equation (64.16) is DETERMINISTIC_TYPE_NORMALIZATION. It keeps equivalence class, gauge representative, polarization basis, propagation, curvature, and observation distinct.

### 64.17 Coverage calibration

The initialized chapter assignment is

$$
N_{\mathrm{assigned}}=0,
\qquad
N_{\mathrm{native\ queries}}=0,
\qquad
N_{\mathrm{native\ evidence\ units}}=0. \tag{64.17}
$$

Equation (64.17) is DETERMINISTIC_COVERAGE_EVIDENCE. Library 4.1 was opened and validated through Runtime to BRANE to API/QMO, but the authoritative chapter ledger assigns no API handles to V07-C08. This chapter therefore claims no native object population.

### 64.18 API evidence register

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|

The empty register is intentional. All mathematical formulas in this chapter are classified as external established mathematics or explicit curatorial boundary statements, not as recovered MK-43 equations.

### 64.19 Evidence boundary

The central distinctions are

$$
\begin{aligned}
\mathrm{GaugeChoice}&\ne\mathrm{PhysicalPolarization},\\
\mathrm{TTProjection}&\ne\mathrm{SourceGeneration},\\
\mathrm{NullCharacteristic}&\ne\mathrm{CompletePropagator},\\
\mathrm{MetricComponent}&\ne\mathrm{DetectorObservable}.
\end{aligned} \tag{64.18}
$$

Equation (64.18) is EVIDENCE_BOUNDARY. These distinctions prevent a convenient representation from being promoted into a native derivation.

### 64.20 Open gauge and propagation obligations

The unresolved requirements are

$$
\begin{aligned}
\mathfrak U_{\mathrm{prop}}=\{&
\mathrm{NativeGaugeGroup},
\mathrm{NativeConstraintAlgebra},
\mathrm{NativeTTProjector},
\mathrm{PolarizationSpectrum},\\
&\mathrm{CharacteristicCone},
\mathrm{DispersionCorrections},
\mathrm{RetardedKernel},
\mathrm{TailStructure},
\mathrm{BackgroundDependence},\\
&\mathrm{ModeConversion},
\mathrm{DetectorCoupling},
\mathrm{Uniqueness},
\mathrm{Stability},
\mathrm{ObservationalBounds}\}.
\end{aligned} \tag{64.19}
$$

Equation (64.19) is CURATOR_SYNTHESIS. It identifies future mathematical and empirical work without creating a native theory in the absence of assigned evidence.

### 64.21 Chapter determination

The result is

$$
\begin{aligned}
\mathrm{GaugePolarizationPropagation}_{\mathrm{V07C08}}
={}&\mathrm{ESTABLISHED\_RELATIVISTIC\_FORMALISM}\\
&+\mathrm{ZERO\_ASSIGNED\_NATIVE\_HANDLES}\\
&+\mathrm{EXPLICIT\_RECOVERY\_BOUNDARY}.
\end{aligned} \tag{64.20}
$$

Equation (64.20) is DETERMINISTIC_STATUS_NORMALIZATION. The chapter supplies the mathematical grammar needed to test future native claims while making the empty QMO assignment visible. It does not infer MK-43 gauge, polarization, or propagation laws from neighboring chapters.
