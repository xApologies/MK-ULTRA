# VOLUME VIII - MATTER AND ENERGY

## Chapter 71 - Stress-Energy and Field Energy

### 71.1 Metric definition of stress-energy

For a matter action \(S_{\mathrm m}[g,\psi]\), the Hilbert stress-energy tensor is

$$
T_{\mu\nu}
=-\frac{2}{\sqrt{-g}}
\frac{\delta S_{\mathrm m}}{\delta g^{\mu\nu}}. \tag{71.1}
$$

Equation (71.1) is EXTERNAL_ESTABLISHED_MATHEMATICS for the displayed sign convention. It ties stress-energy to metric response and prevents an energy-density label from standing in for a complete tensor.

### 71.2 Covariant balance

For diffeomorphism-invariant matter satisfying its field equations,

$$
\nabla^\mu T_{\mu\nu}=0. \tag{71.2}
$$

Equation (71.2) is EXTERNAL_ESTABLISHED_MATHEMATICS under the stated hypotheses. A proposed chromatic or phase sector must satisfy the same balance or explicitly state its exchange current with other sectors.

### 71.3 Observer decomposition

Relative to a unit timelike field \(u^\mu\), define

$$
\rho=T_{\mu\nu}u^\mu u^\nu,
\qquad
q_\alpha=-h_\alpha{}^\mu T_{\mu\nu}u^\nu,
\qquad
h_{\mu\nu}=g_{\mu\nu}+u_\mu u_\nu. \tag{71.3}
$$

Equation (71.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. Energy density \(\rho\), spatial energy flux \(q_\alpha\), and the full tensor have different information content.

### 71.4 Pressure and anisotropic stress

The spatial stress decomposes as

$$
T_{\mu\nu}
=\rho u_\mu u_\nu
+2u_{(\mu}q_{\nu)}
+p h_{\mu\nu}
+\pi_{\mu\nu}, \tag{71.4}
$$

where \(\pi_{\mu\nu}u^\nu=0\) and \(\pi^\mu{}_{\mu}=0\). Equation (71.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. A scalar “field energy” does not determine pressure, flux, or anisotropic stress.

### 71.5 Scalar-field tensor

For a real scalar field with

$$
\mathcal L_\phi
=-\frac12g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi
-V(\phi), \tag{71.5}
$$

the stress tensor is

$$
T^{(\phi)}_{\mu\nu}
=\partial_\mu\phi\partial_\nu\phi
-g_{\mu\nu}
\left(\frac12\partial_\alpha\phi\partial^\alpha\phi+V(\phi)\right). \tag{71.6}
$$

Equations (71.5) and (71.6) are EXTERNAL_ESTABLISHED_MATHEMATICS. They illustrate that a field definition, Lagrangian, and tensor output must be supplied together.

### 71.6 Gauge-field energy

For an electromagnetic-type field strength \(F_{\mu\nu}\),

$$
T^{(F)}_{\mu\nu}
=F_{\mu\alpha}F_\nu{}^\alpha
-\frac14g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}. \tag{71.7}
$$

Equation (71.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. A “chromatic field” cannot inherit this tensor solely by analogy; its representation, curvature, action, and normalization must be recovered or defined.

### 71.7 Phase-field sector

For a phase variable \(\theta\), a generic effective action may be written

$$
S_\theta
=\int_M
\left[-\frac{f^2}{2}
g^{\mu\nu}\partial_\mu\theta\partial_\nu\theta
-U(\theta)\right]
\sqrt{-g}\,d^4x. \tag{71.8}
$$

Equation (71.8) is EXTERNAL_ESTABLISHED_MATHEMATICS as an effective-field schema. `@phase_stress_energy` is MEDIUM, but the recovered metadata do not fix \(f\), \(U\), or the physical domain of \(\theta\).

### 71.8 Multi-component chromatic field

Let \(\Phi^a\) be components in an internal vector space with metric \(K_{ab}\). A generic kinetic model is

$$
\mathcal L_{\mathrm{chr}}
=-\frac12K_{ab}
g^{\mu\nu}D_\mu\Phi^aD_\nu\Phi^b
-V(\Phi). \tag{71.9}
$$

Equation (71.9) is EXTERNAL_ESTABLISHED_MATHEMATICS as a model class, not a recovered chromatic Lagrangian. `@definition_2_2_chromatic_field` supplies one definition unit, while `@chromatic_lagrangian` remains THIN.

### 71.9 Chromatic stress-energy output

If (71.9) were adopted, metric variation would give

$$
T^{(\mathrm{chr})}_{\mu\nu}
=K_{ab}D_\mu\Phi^aD_\nu\Phi^b
+g_{\mu\nu}\mathcal L_{\mathrm{chr}}. \tag{71.10}
$$

Equation (71.10) is EXTERNAL_ESTABLISHED_MATHEMATICS conditional on (71.9) and its conventions. It is not asserted as the exact equation indexed by `@chromatic_stress_energy`.

### 71.10 Sector composition

For interacting sectors, a bookkeeping decomposition is

$$
T_{\mu\nu}^{\mathrm{tot}}
=T_{\mu\nu}^{(\mathrm m)}
+T_{\mu\nu}^{(\theta)}
+T_{\mu\nu}^{(\mathrm{chr})}
+T_{\mu\nu}^{(\mathrm{int})}. \tag{71.11}
$$

Equation (71.11) is EXTERNAL_ESTABLISHED_MATHEMATICS. Interaction energy must not be double-counted, and the individual tensors need not be conserved separately.

### 71.11 Exchange currents

A consistent exchange among sectors has the form

$$
\nabla^\mu T^{(A)}_{\mu\nu}=Q^{(A)}_\nu,
\qquad
\sum_A Q^{(A)}_\nu=0. \tag{71.12}
$$

Equation (71.12) is EXTERNAL_ESTABLISHED_MATHEMATICS. It makes “contribution” and “output” quantitative only after the exchange currents are defined.

### 71.12 Projected stress-energy

Given a linear projector \(P\) on tensor fields, a projected sector may be typed as

$$
T^{\mathrm{proj}}=P[T],
\qquad
P^2=P. \tag{71.13}
$$

Equation (71.13) is EXTERNAL_ESTABLISHED_MATHEMATICS as a projector schema. `@projected_stress_energy_sector` is MEDIUM, but the native projector’s domain, image, kernel, and covariance remain required.

### 71.13 Renormalized expectation value

In semiclassical gravity, the source may be a renormalized expectation value,

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}
=\frac{8\pi G}{c^4}
\langle T_{\mu\nu}\rangle_{\mathrm{ren}}. \tag{71.14}
$$

Equation (71.14) is EXTERNAL_ESTABLISHED_MATHEMATICS as a semiclassical equation. `@renormalized_stress_energy_tensor` is MEDIUM and densely connected; a renormalization prescription and state dependence are still indispensable.

### 71.14 Mote configuration and Hilbert spaces

For a finite mote configuration set \(\Omega\), a generic Hilbert space is

$$
\mathcal H_{\mathrm{mote}}
=\ell^2(\Omega),
\qquad
\langle\psi,\varphi\rangle
=\sum_{\omega\in\Omega}
\overline{\psi(\omega)}\varphi(\omega). \tag{71.15}
$$

Equation (71.15) is EXTERNAL_ESTABLISHED_MATHEMATICS. `@mote_configuration_space` and `@mote_hilbert_space` are MEDIUM, but this schema does not select the native configuration set or physical inner product.

### 71.15 Mote closure and admissibility

If \(C_a\) are closure constraints, the admissible state space is

$$
\mathcal H_{\mathrm{phys}}
=\{\psi\in\mathcal H_{\mathrm{mote}}:
\widehat C_a\psi=0\ \text{for all }a\}. \tag{71.16}
$$

Equation (71.16) is EXTERNAL_ESTABLISHED_MATHEMATICS as a constraint schema. The three indexed equation units at `@mote_closure` do not authorize invented operators \(\widehat C_a\).

### 71.16 Typed field-to-gravity contract

The disciplined chain is

$$
(\mathcal F,S,\mathrm{state})
\longmapsto
T_{\mu\nu}
\longmapsto
\big(\rho,q_\mu,p,\pi_{\mu\nu}\big)
\longmapsto
\mathrm{GeometryResponse}. \tag{71.17}
$$

Equation (71.17) is DETERMINISTIC_TYPE_NORMALIZATION. It separates field content, action, state, stress tensor, observer decomposition, and gravitational response.

### 71.17 Coverage calibration

The chapter assignment contains

$$
N_{\mathrm{assigned}}=31,
\qquad
N_{\mathrm{MEDIUM}}=10,
\qquad
N_{\mathrm{THIN}}=21. \tag{71.18}
$$

Equation (71.18) is DETERMINISTIC_COVERAGE_EVIDENCE. The handles contain 1,223 English units, 32 indexed equation units, one definition unit, and 1,108 registered dependencies. `@stress_energy_tensor` contributes 743 English units, six equations, and 858 dependencies.

### 71.18 API evidence register

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@appendix_c_chromatic_solitons` | @appendix_c_chromatic_solitons` — Appendix C: Chromatic Solitons | THIN | 0 / 0 / 0 | chapter-core object |
| `@chromatic_bio_signatures` | @chromatic_bio_signatures` — Chromatic Bio-Signatures | THIN | 5 / 0 / 0 | chapter-core object |
| `@chromatic_charge_of_molecular_clouds` | @chromatic_charge_of_molecular_clouds` — Chromatic Charge of Molecular Clouds | THIN | 5 / 0 / 0 | chapter-core object |
| `@chromatic_contributions` | @chromatic_contributions` — Chromatic Contributions | THIN | 5 / 0 / 0 | chapter-core object |
| `@chromatic_distributions_and_structure_formation` | @chromatic_distributions_and_structure_formation` — Chromatic Distributions and Structure Formation | THIN | 5 / 0 / 0 | chapter-core object |
| `@chromatic_energy_densities` | @chromatic_energy_densities` — Chromatic Energy Densities | THIN | 6 / 0 / 0 | chapter-core object |
| `@chromatic_era_transitions` | @chromatic_era_transitions` — Chromatic Era Transitions | THIN | 4 / 0 / 0 | chapter-core object |
| `@chromatic_field` | @chromatic_field` — Chromatic Field | THIN | 5 / 0 / 0 | chapter-core object |
| `@chromatic_fields` | @chromatic_fields` — Chromatic fields | THIN | 3 / 0 / 0 | chapter-core object |
| `@chromatic_fields_and_energy_bands` | @chromatic_fields_and_energy_bands` — Chromatic Fields and Energy Bands | THIN | 2 / 0 / 0 | chapter-core object |
| `@chromatic_fields_energy_bands` | @chromatic_fields_energy_bands` — Chromatic Fields (Energy Bands) | THIN | 2 / 0 / 0 | chapter-core object |
| `@chromatic_lagrangian` | @chromatic_lagrangian` — Chromatic Lagrangian | THIN | 2 / 0 / 0 | chapter-core object |
| `@chromatic_modulated_alloys` | @chromatic_modulated_alloys` — Chromatic Modulated Alloys | THIN | 0 / 0 / 0 | chapter-core object |
| `@chromatic_recoil_mechanics` | @chromatic_recoil_mechanics` — Chromatic Recoil Mechanics | THIN | 0 / 0 / 0 | chapter-core object |
| `@chromatic_seeds_for_density_perturbations` | @chromatic_seeds_for_density_perturbations` — Chromatic Seeds for Density Perturbations | THIN | 1 / 0 / 0 | chapter-core object |
| `@chromatic_stress_energy` | @chromatic_stress_energy` — Chromatic stress-energy | MEDIUM | 4 / 1 / 2 | chapter-core object |
| `@chromatic_stress_energy_output` | @chromatic_stress_energy_output` — Chromatic Stress-Energy Output | THIN | 2 / 0 / 0 | chapter-core object |
| `@chromaticfield` | @chromaticfield` — ChromaticField | MEDIUM | 70 / 2 / 6 | chapter-core object |
| `@cmb_signatures_from_phase_and_chromatic_structure` | @cmb_signatures_from_phase_and_chromatic_structure` — CMB Signatures from Phase and Chromatic Structure | THIN | 6 / 0 / 0 | chapter-core object |
| `@definition_2_2_chromatic_field` | @definition_2_2_chromatic_field` — Definition 2.2 — Chromatic Field | MEDIUM | 2 / 0 / 0 | chapter-core object |
| `@mote_closure` | @mote_closure | MEDIUM | 66 / 3 / 3 | chapter-core object |
| `@mote_configuration_space` | New Handle — @mote_configuration_space | MEDIUM | 92 / 6 / 6 | chapter-core object |
| `@mote_hilbert_space` | Thickened Handle — @mote_hilbert_space | MEDIUM | 67 / 5 / 4 | chapter-core object |
| `@phase_shell_chromatic_fields_and_er_foam` | @phase_shell_chromatic_fields_and_er_foam` — Phase shell, chromatic fields, and ER foam | THIN | 1 / 0 / 0 | chapter-core object |
| `@phase_stress_energy` | @phase_stress_energy` — Phase stress-energy | MEDIUM | 55 / 3 / 11 | chapter-core object |
| `@phase_stress_energy_output` | @phase_stress_energy_output` — Phase Stress-Energy Output | THIN | 3 / 0 / 0 | chapter-core object |
| `@projected_stress_energy_sector` | @projected_stress_energy_sector` — Projected Stress-Energy Sector | MEDIUM | 14 / 1 / 4 | chapter-core object |
| `@renormalized_stress_energy_tensor` | @renormalized_stress_energy_tensor | MEDIUM | 47 / 5 / 214 | chapter-core object |
| `@signatures_of_chromatic_and_phase_dynamics` | @signatures_of_chromatic_and_phase_dynamics` — Signatures of Chromatic and Phase Dynamics | THIN | 6 / 0 / 0 | chapter-core object |
| `@stress_energy_contribution` | @stress_energy_contribution` — Stress-Energy Contribution | THIN | 0 / 0 / 0 | chapter-core object |
| `@stress_energy_tensor` | @stress_energy_tensor` — Stress-Energy Tensor | MEDIUM | 743 / 6 / 858 | chapter-core object |

The register keeps the central stress tensor, phase, chromatic, projected, renormalized, mote-space, cosmological, material, biological, and observational addresses distinct. Most specialized chromatic applications are THIN and are not upgraded by proximity to the stress-energy core.

### 71.19 Evidence boundary

The operative distinctions are

$$
\begin{aligned}
\mathrm{FieldName}&\ne\mathrm{FieldAction},\\
\mathrm{EnergyDensity}&\ne\mathrm{StressTensor},\\
\mathrm{ProjectedSector}&\ne\mathrm{FullSource},\\
\mathrm{ProposedSignature}&\ne\mathrm{ObservedSignal}.
\end{aligned} \tag{71.19}
$$

Equation (71.19) is EVIDENCE_BOUNDARY. Chromatic solitons, bio-signatures, molecular-cloud charge, alloys, recoil, structure formation, era transitions, CMB signatures, and ER-foam associations remain candidate subjects until equations and observations are supplied.

### 71.20 Open stress-energy obligations

The unresolved requirements are

$$
\begin{aligned}
\mathfrak U_T=\{&
\mathrm{ExactChromaticFieldDefinition},
\mathrm{NativeLagrangian},
\mathrm{RepresentationSpace},
\mathrm{CouplingConstants},
\mathrm{PhaseAction},\\
&\mathrm{MetricVariation},
\mathrm{ExchangeCurrents},
\mathrm{ProjectionOperator},
\mathrm{RenormalizationScheme},
\mathrm{QuantumState},\\
&\mathrm{MoteConfigurationSpace},
\mathrm{PhysicalInnerProduct},
\mathrm{ClosureConstraints},
\mathrm{EnergyConditions},
\mathrm{ObservationalTests}\}.
\end{aligned} \tag{71.20}
$$

Equation (71.20) is CURATOR_SYNTHESIS. It identifies the work required to connect recovered addresses to a conserved, covariant, and testable source tensor.

### 71.21 Chapter determination

The result is

$$
\begin{aligned}
\mathrm{StressEnergy}_{\mathrm{V08C05}}
={}&\mathrm{ESTABLISHED\_COVARIANT\_SOURCE\_FRAMEWORK}\\
&+\mathrm{RECOVERED\_PHASE\_CHROMATIC\_AND\_MOTE\_ADDRESSES}\\
&+\mathrm{OPEN\_NATIVE\_ACTIONS\_PROJECTIONS\_AND\_TESTS}.
\end{aligned} \tag{71.21}
$$

Equation (71.21) is DETERMINISTIC_STATUS_NORMALIZATION. The tensorial requirements for field energy are explicit, while the exact chromatic and phase actions, mote Hilbert structure, projection, renormalization, specialized applications, and observational validation remain open where evidence is thin.
