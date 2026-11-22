# VOLUME X - BLACK HOLES AND STRONG GRAVITY

## Chapter 86 - Strong-Gravity Signatures and Open Problems

### 86.1 Thermal signature

The stationary semiclassical temperature is

$$
T_H=\frac{\hbar\kappa_H}{2\pi}. \tag{86.1}
$$

Equation (86.1) is EXTERNAL_ESTABLISHED_MATHEMATICS. A temperature address does not by itself specify detector response, backreaction, or an evaporation endpoint.

### 86.2 Isolated horizon

An isolated-horizon cross-section has vanishing outgoing expansion,

$$
\theta_{(\ell)}\big|_{\mathcal H_{\mathrm{iso}}}=0. \tag{86.2}
$$

Equation (86.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. The complete definition also requires causal, field-equation, and invariance conditions.

### 86.3 No local area flux

For an equilibrium isolated horizon,

$$
\mathcal L_{\ell}A_H=0. \tag{86.3}
$$

Equation (86.3) is EXTERNAL_ESTABLISHED_MATHEMATICS under the isolated-horizon assumptions. It differs from a dynamical horizon with nonzero flux.

### 86.4 Horizon first law

A local equilibrium variation is organized as

$$
\delta E_H
=\frac{\kappa_H}{8\pi G}\delta A_H
+\Omega_H\delta J_H+\Phi_H\delta Q_H. \tag{86.4}
$$

Equation (86.4) is EXTERNAL_ESTABLISHED_MATHEMATICS with its horizon normalization and boundary conditions specified.

### 86.5 Horizon restriction

A bulk phase field restricts to a horizon by pullback,

$$
\phi_H=\iota_H^{*}\phi,
\qquad
\iota_H:\mathcal H\hookrightarrow M. \tag{86.5}
$$

Equation (86.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. The THIN `@horizon_restricted_phase` handle supplies no recovered native phase evolution law.

### 86.6 Restricted evolution

A native horizon dynamics would require an operator

$$
U_H(t):\mathcal X_H\longrightarrow\mathcal X_H. \tag{86.6}
$$

Equation (86.6) is EXTERNAL_ESTABLISHED_MATHEMATICS as a typing schema. Domain, generator, boundary conditions, and conservation properties remain absent.

### 86.7 White-horizon survival map

The historical survival question can only be formalized after specifying

$$
\mathcal S_W:\mathcal X_{\mathrm{in}}
\longrightarrow\mathcal X_{\mathrm{surv}}. \tag{86.7}
$$

Equation (86.7) is EXTERNAL_ESTABLISHED_MATHEMATICS as a map schema. It is not a recovered transition law or proof that a white horizon exists.

### 86.8 Ringdown signal

A linear ringdown model is

$$
h(t)=\sum_nA_ne^{-t/\tau_n}\cos(\omega_nt+\varphi_n). \tag{86.8}
$$

Equation (86.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. Mode content and amplitudes depend on the background and excitation.

### 86.9 Quasinormal frequencies

The complex frequencies are written

$$
\Omega_n=\omega_n-\frac{i}{\tau_n}. \tag{86.9}
$$

Equation (86.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. Stability convention requires positive damping time.

### 86.10 Shadow scale

A geometric angular scale is

$$
\theta_{\mathrm{sh}}\simeq\frac{b_c}{D}. \tag{86.10}
$$

Equation (86.10) is EXTERNAL_ESTABLISHED_MATHEMATICS in a small-angle approximation. Astrophysical transfer and instrument response are additional layers.

### 86.11 Gravitational redshift

For static observers in a static metric,

$$
1+z=\sqrt{\frac{-g_{tt}(r_{\mathrm{obs}})}{-g_{tt}(r_{\mathrm{em}})}}. \tag{86.11}
$$

Equation (86.11) is EXTERNAL_ESTABLISHED_MATHEMATICS. Observer motion and nonstationarity require a more general frequency ratio.

### 86.12 Tidal signature

Geodesic deviation obeys

$$
\frac{D^2\xi^{\mu}}{D\tau^2}
=-R^{\mu}{}_{\nu\rho\sigma}
u^{\nu}\xi^{\rho}u^{\sigma}. \tag{86.12}
$$

Equation (86.12) is EXTERNAL_ESTABLISHED_MATHEMATICS. It connects curvature to measurable relative acceleration.

### 86.13 Curvature invariant

For Schwarzschild geometry,

$$
K=R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
=\frac{48G^2M^2}{r^6}. \tag{86.13}
$$

Equation (86.13) is EXTERNAL_ESTABLISHED_MATHEMATICS. It distinguishes the curvature singularity from the regular horizon.

### 86.14 Echo-delay template

A near-horizon reflecting structure may produce a delay scaling as

$$
\Delta t_{\mathrm{echo}}
\sim2\left|r_*(r_{\mathrm{barrier}})-r_*(r_0)\right|. \tag{86.14}
$$

Equation (86.14) is EXTERNAL_ESTABLISHED_MATHEMATICS as a phenomenological template. It is not evidence that echoes or a reflecting surface were observed.

### 86.15 Parameter residual

A strong-gravity test may use

$$
r_i=d_i-m_i(\vartheta). \tag{86.15}
$$

Equation (86.15) is EXTERNAL_ESTABLISHED_MATHEMATICS. Data, covariance, calibration, and model systematics must accompany the residual.

### 86.16 Likelihood audit

For Gaussian residuals,

$$
-2\log\mathcal L(\vartheta)
=r^{\mathsf T}C^{-1}r+\mathrm{constant}. \tag{86.16}
$$

Equation (86.16) is EXTERNAL_ESTABLISHED_MATHEMATICS. It supplies an inference form, not an experiment or result.

### 86.17 Typed signature contract

The chapter normalizes a strong-gravity test record as

$$
\mathfrak O_{\mathrm{SG}}
=\big(\mathrm{object},\mathrm{channel},\mathrm{model},
\mathrm{data},\mathrm{transfer},\mathrm{likelihood},
\mathcal A,\mathcal P,\mathcal U\big). \tag{86.17}
$$

Equation (86.17) is DETERMINISTIC_TYPE_NORMALIZATION. It keeps theory, observation, assumptions, provenance, and unresolved requirements separate.

### 86.18 Coverage calibration

The native query returned

$$
N_{\mathrm{assigned}}=4,
\quad N_{\mathrm{queried}}=4,
\quad N_{\mathrm{English}}=334,
\quad N_{\mathrm{equations}}=9. \tag{86.18}
$$

Equation (86.18) is DETERMINISTIC_COVERAGE_EVIDENCE. Hawking temperature and isolated horizon are MEDIUM; the phase restriction and white-horizon survival addresses are THIN.

### 86.19 API evidence register

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@hawking_temperature` | @hawking_temperature | MEDIUM | 216 / 5 / 279 | chapter-core object |
| `@horizon_restricted_phase` | @horizon_restricted_phase` — Horizon-restricted phase | THIN | 6 / 0 / 0 | chapter-core object |
| `@isolated_horizon` | @isolated_horizon | MEDIUM | 96 / 4 / 211 | chapter-core object |
| `@what_survives_the_white_horizon` | @what_survives_the_white_horizon` — What Survives the White Horizon | THIN | 16 / 0 / 0 | chapter-core object |

The register preserves equilibrium-horizon mathematics, semiclassical temperature, a sparse phase-restriction address, and a historical white-horizon question at their separate evidence levels.

### 86.20 Evidence boundary

The operative distinctions are

$$
\begin{aligned}
\mathrm{TheoreticalSignature}&\ne\mathrm{Detection},\\
\mathrm{IsolatedHorizon}&\ne\mathrm{EvaporatingHorizon},\\
\mathrm{FieldRestriction}&\ne\mathrm{HorizonDynamics},\\
\mathrm{HistoricalQuestion}&\ne\mathrm{TransitionLaw}.
\end{aligned} \tag{86.19}
$$

Equation (86.19) is EVIDENCE_BOUNDARY. It prevents sparse native addresses from being promoted through nearby established mathematics.

### 86.21 Open strong-gravity obligations

The remaining program is

$$
\begin{aligned}
\mathfrak U_{\mathrm{SG}}=\{&
\mathrm{NativeDeviationParameters},
\mathrm{ExactWaveforms},
\mathrm{HorizonTransfer},
\mathrm{PhaseRestrictionType},
\mathrm{PhaseEvolution},\\
&\mathrm{WhiteHorizonDefinition},
\mathrm{SurvivalDomain},
\mathrm{SurvivalCodomain},
\mathrm{TransitionProof},
\mathrm{InstrumentResponse},\\
&\mathrm{NoiseModel},
\mathrm{PopulationModel},
\mathrm{SystematicErrors},
\mathrm{ExecutedExperiments},
\mathrm{IndependentValidation}\}.
\end{aligned} \tag{86.20}
$$

Equation (86.20) is CURATOR_SYNTHESIS. It records the research frontier without creating new strong-gravity claims.

### 86.22 Volume determination

The Volume X result is

$$
\begin{aligned}
\mathrm{StrongGravity}_{\mathrm{V10}}
={}&\mathrm{GEOMETRIC\_THERMODYNAMIC\_INFORMATION\_ARCHITECTURE}\\
&+\mathrm{FOUR\_FINAL\_NATIVE\_ADDRESSES}\\
&+\mathrm{ESTABLISHED\_SIGNATURE\_AND\_INFERENCE\_TEMPLATES}\\
&+\mathrm{OPEN\_NATIVE\_MAPS\_EXPERIMENTS\_AND\_VALIDATION}.
\end{aligned} \tag{86.21}
$$

Equation (86.21) is DETERMINISTIC_STATUS_NORMALIZATION. Volume X closes with a rigorous separation between established strong-gravity mathematics, native address coverage, historical horizon concepts, and unresolved validation.
