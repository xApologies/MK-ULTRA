# VOLUME VIII - MATTER AND ENERGY

## Chapter 70 - Native Unit of Energy

### 70.1 What an energy unit must do

An energy quantity \(E\) has physical dimension

$$
[E]=M L^2 T^{-2}. \tag{70.1}
$$

Equation (70.1) is EXTERNAL_ESTABLISHED_MATHEMATICS. A “native unit of energy” must therefore supply a reference magnitude, dimensions, and a conversion rule; a name or API address is not yet a metrological definition.

### 70.2 Reference-scale decomposition

Given a positive reference energy \(E_*\), any energy may be written

$$
E=\varepsilon E_*,
\qquad
\varepsilon=\frac{E}{E_*}\in\mathbb R. \tag{70.2}
$$

Equation (70.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. The dimensionless coordinate \(\varepsilon\) and the dimensional unit \(E_*\) are distinct mathematical roles.

### 70.3 Unit conversion

If \(E_*'=\alpha E_*\) with \(\alpha>0\), then

$$
\varepsilon' = \frac{E}{E_*'}=\alpha^{-1}\varepsilon. \tag{70.3}
$$

Equation (70.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. A physically meaningful prediction must remain invariant under this change of numerical representation.

### 70.4 Dimensional Hamiltonian

For a dimensionless Hamiltonian \(\widehat H\), a dimensional Hamiltonian is

$$
H=E_*\widehat H. \tag{70.4}
$$

Equation (70.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. The spectrum of \(\widehat H\) becomes an energy spectrum only after \(E_*\) is fixed.

### 70.5 Frequency calibration

Quantum frequency and energy are related by

$$
E=\hbar\omega. \tag{70.5}
$$

Equation (70.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. A native frequency \(\omega_*\) would induce \(E_*=\hbar\omega_*\), but the recovered address `@native_unit_of_energy` does not by itself establish such a frequency.

### 70.6 Mass calibration

Rest mass provides another energy scale,

$$
E=mc^2. \tag{70.6}
$$

Equation (70.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Inferring a native mass from an energy unit requires a stated relativistic regime and does not follow merely from mote terminology.

### 70.7 Thermal calibration

A temperature scale can be converted by

$$
E=k_{\mathrm B}T. \tag{70.7}
$$

Equation (70.7) is EXTERNAL_ESTABLISHED_MATHEMATICS as a characteristic thermal scale. It does not assert equilibrium, a temperature field, or a specific statistical ensemble.

### 70.8 Action and time scale

If a characteristic action \(S_*\) and time \(t_*\) are fundamental, then

$$
E_* = \frac{S_*}{t_*}. \tag{70.8}
$$

Equation (70.8) is EXTERNAL_ESTABLISHED_MATHEMATICS dimensionally. A native theory must identify the source and invariance properties of both scales.

### 70.9 Chirality-labelled motes

Let \(\mathcal M\) be a mote state space and let

$$
\chi:\mathcal M\longrightarrow\{-1,+1\}. \tag{70.9}
$$

Equation (70.9) is EXTERNAL_ESTABLISHED_MATHEMATICS as a binary-label schema. `@chirality_labelled_mote` and `@mote_chirality` are MEDIUM, but their recovered metadata do not establish that chirality alone determines a mote’s energy.

### 70.10 Chiral energy sectors

A chirality-sensitive energy function may be decomposed as

$$
E(m)=E_0(m)+\chi(m)\,\Delta E(m). \tag{70.10}
$$

Equation (70.10) is EXTERNAL_ESTABLISHED_MATHEMATICS as a generic even/odd decomposition. It is not a recovered native energy law and leaves \(E_0\) and \(\Delta E\) unspecified.

### 70.11 Positive chirality is not positive energy

The logical distinction is

$$
\chi(m)=+1
\centernot\Longrightarrow
E(m)>0. \tag{70.11}
$$

Equation (70.11) is EXTERNAL_ESTABLISHED_MATHEMATICS as a type statement. `@mote_positive_chirality` is THIN; the sign of a chirality label and the sign of an energy eigenvalue belong to different codomains.

### 70.12 Diagonal energy rule

If a preferred basis \(\{|m_a\rangle\}\) diagonalizes a Hamiltonian, then

$$
\langle m_a|H|m_b\rangle
=E_a\delta_{ab}. \tag{70.12}
$$

Equation (70.12) is EXTERNAL_ESTABLISHED_MATHEMATICS. It is a candidate generic reading of a diagonal rule, not a claim that the seven indexed equations linked to `@mote_diagonal_rule` all assert this particular formula.

### 70.13 Off-diagonal coupling

In a non-eigenbasis, interaction or mixing appears through

$$
H_{ab}=E_a\delta_{ab}+V_{ab},
\qquad a\ne b\Rightarrow V_{ab}\text{ may be nonzero}. \tag{70.13}
$$

Equation (70.13) is EXTERNAL_ESTABLISHED_MATHEMATICS. A native diagonal rule must state the basis, operator, domain, and conditions under which off-diagonal terms vanish.

### 70.14 Ensemble energy

For occupation numbers \(n_a\), the noninteracting ensemble energy is

$$
E_{\mathrm{ens}}=\sum_a n_a E_a. \tag{70.14}
$$

Equation (70.14) is EXTERNAL_ESTABLISHED_MATHEMATICS. Interactions, constraints, and collective terms generally require additions and can prevent simple additivity.

### 70.15 Source consistency

Two proposed calibrations \(E_*^{(1)}\) and \(E_*^{(2)}\) are compatible only if a declared conversion exists,

$$
E_*^{(2)}=\alpha E_*^{(1)},
\qquad
\alpha>0
\text{ fixed and dimensionless}. \tag{70.15}
$$

Equation (70.15) is EXTERNAL_ESTABLISHED_MATHEMATICS as a consistency criterion. `@mote_source_conflict` is THIN, so conflict language is preserved without inventing which historical source should control.

### 70.16 Native-unit contract

A complete declaration must have the form

$$
\mathcal U_E
=\big(E_*,[E_*],\mathcal D_E,\mathcal C_E,\mathcal I_E\big), \tag{70.16}
$$

where \(\mathcal D_E\) is the domain of quantities measured, \(\mathcal C_E\) the conversion rule, and \(\mathcal I_E\) the invariance convention. Equation (70.16) is DETERMINISTIC_TYPE_NORMALIZATION.

### 70.17 Coverage calibration

The chapter assignment contains

$$
N_{\mathrm{assigned}}=7,
\qquad
N_{\mathrm{MEDIUM}}=5,
\qquad
N_{\mathrm{THIN}}=2. \tag{70.17}
$$

Equation (70.17) is DETERMINISTIC_COVERAGE_EVIDENCE. The assigned handles contain 324 English units, 20 indexed equation units, zero definition units, and 31 registered dependencies. `@native_unit_of_energy` contributes 42 English units, five equations, and six dependencies.

### 70.18 API evidence register

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@chirality_labelled_mote` | @chirality_labelled_mote` — Chirality-Labelled Mote | MEDIUM | 133 / 4 / 14 | chapter-core object |
| `@mote_chirality` | New Handle — @mote_chirality | MEDIUM | 102 / 3 / 7 | chapter-core object |
| `@mote_diagonal_rule` | @mote_diagonal_rule | MEDIUM | 37 / 7 / 2 | chapter-core object |
| `@mote_positive_chirality` | @mote_positive_chirality | THIN | 2 / 0 / 0 | chapter-core object |
| `@mote_source_conflict` | @mote_source_conflict | THIN | 4 / 0 / 0 | chapter-core object |
| `@native_unit_of_energy` | @native_unit_of_energy | MEDIUM | 42 / 5 / 6 | chapter-core object |
| `@unit_of_energy` | @unit_of_energy | MEDIUM | 4 / 1 / 2 | chapter-core object |

The register preserves the native-unit, generic-unit, chirality-labelled mote, mote chirality, diagonal rule, positive chirality, and source-conflict addresses separately. Their proximity does not establish one shared equation or one native numerical constant.

### 70.19 Evidence boundary

The operative distinctions are

$$
\begin{aligned}
\mathrm{UnitSymbol}&\ne\mathrm{UnitMagnitude},\\
\mathrm{ChiralitySign}&\ne\mathrm{EnergySign},\\
\mathrm{DiagonalRule}&\ne\mathrm{InteractionDynamics},\\
\mathrm{SourceConflict}&\ne\mathrm{ResolvedConvention}.
\end{aligned} \tag{70.18}
$$

Equation (70.18) is EVIDENCE_BOUNDARY. No Planck, mote, frequency, mass, or thermal scale is selected as the MK-43 native unit without an exact recovered declaration.

### 70.20 Open unit obligations

The unresolved requirements are

$$
\begin{aligned}
\mathfrak U_{E_*}=\{&
\mathrm{ExactNativeMagnitude},
\mathrm{Dimensions},
\mathrm{DefiningObservable},
\mathrm{ReferenceFrame},
\mathrm{ConversionRules},\\
&\mathrm{MoteEnergyMap},
\mathrm{ChiralityCoupling},
\mathrm{DiagonalBasis},
\mathrm{HamiltonianDomain},
\mathrm{InteractionTerms},\\
&\mathrm{SourceReconciliation},
\mathrm{UncertaintyBudget},
\mathrm{MeasurementProtocol},
\mathrm{ExperimentalCalibration}\}.
\end{aligned} \tag{70.19}
$$

Equation (70.19) is CURATOR_SYNTHESIS. It identifies what must be supplied before the native-unit address becomes a complete physical standard.

### 70.21 Chapter determination

The result is

$$
\begin{aligned}
\mathrm{NativeEnergyUnit}_{\mathrm{V08C04}}
={}&\mathrm{RECOVERED\_UNIT\_AND\_MOTE\_ADDRESS\_SPACE}\\
&+\mathrm{ESTABLISHED\_DIMENSIONAL\_AND\_CONVERSION\_RULES}\\
&+\mathrm{OPEN\_NATIVE\_SCALE\_CALIBRATION\_AND\_PROOF}.
\end{aligned} \tag{70.20}
$$

Equation (70.20) is DETERMINISTIC_STATUS_NORMALIZATION. The chapter defines the obligations of a native energy unit while preserving the fact that no exact magnitude, complete mote-energy law, resolved source convention, or empirical calibration was recovered here.
