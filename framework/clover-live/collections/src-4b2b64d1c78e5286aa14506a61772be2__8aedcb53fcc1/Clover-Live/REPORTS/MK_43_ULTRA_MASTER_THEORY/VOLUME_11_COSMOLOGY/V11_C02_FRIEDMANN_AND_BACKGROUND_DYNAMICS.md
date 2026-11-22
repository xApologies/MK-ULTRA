# VOLUME XI - COSMOLOGY

## Chapter 88 - Friedmann and Background Dynamics

### 88.1 Background geometry

The homogeneous and isotropic sector is represented by the Friedmann-Lemaitre-Robertson-Walker line element

$$
ds^2=-dt^2+a(t)^2\left[\frac{dr^2}{1-kr^2}+r^2d\Omega^2\right]. \tag{88.1}
$$

Equation (88.1) is EXTERNAL_ESTABLISHED_MATHEMATICS. It fixes the background ansatz; it does not derive that ansatz from the native MK 43 Ultra address space.

### 88.2 Gravitational field equation

For an Einstein background with cosmological constant,

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T_{\mu\nu}. \tag{88.2}
$$

Equation (88.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. Any native correction must specify whether it modifies geometry, stress-energy, coupling, or the reduction map.

### 88.3 Homogeneous source

A perfect-fluid source has

$$
T_{\mu\nu}=(\rho+p)u_\mu u_\nu+p g_{\mu\nu}. \tag{88.3}
$$

Equation (88.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. The variables are effective background quantities unless a microscopic dictionary is supplied.

### 88.4 Expansion variable

The Hubble parameter is

$$
H=\frac{\dot a}{a}. \tag{88.4}
$$

Equation (88.4) is EXTERNAL_ESTABLISHED_MATHEMATICS and provides the central background rate.

### 88.5 Friedmann constraint

The temporal field equation gives

$$
H^2+\frac{k}{a^2}=\frac{8\pi G}{3}\rho+\frac{\Lambda}{3}. \tag{88.5}
$$

Equation (88.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. The Library has substantial coherent evidence around `@friedmann_equation`, but that population does not by itself determine an MK-native correction.

### 88.6 Acceleration equation

The spatial trace yields

$$
\frac{\ddot a}{a}=-\frac{4\pi G}{3}(\rho+3p)+\frac{\Lambda}{3}. \tag{88.6}
$$

Equation (88.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Acceleration requires negative enough effective pressure or a modified dynamical sector.

### 88.7 Continuity equation

Covariant conservation reduces to

$$
\dot\rho+3H(\rho+p)=0. \tag{88.7}
$$

Equation (88.7) is EXTERNAL_ESTABLISHED_MATHEMATICS for a conserved total fluid. The address `@continuity_equation_cosmology` is independently populated in Library 4.1.

### 88.8 Sector decomposition

For separately named background components,

$$
\rho=\sum_A\rho_A,\qquad p=\sum_A p_A. \tag{88.8}
$$

Equation (88.8) is EXTERNAL_ESTABLISHED_MATHEMATICS as bookkeeping. A native sector must earn its place through a defined stress-energy contribution and coupling rule.

### 88.9 Equation of state

A constant barotropic component is parameterized by

$$
p_A=w_A\rho_A. \tag{88.9}
$$

Equation (88.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. It is a phenomenological closure relation, not an explanation of microscopic origin.

### 88.10 Background scaling

For constant equation-of-state parameter and separate conservation,

$$
\rho_A(a)=\rho_{A0}\,a^{-3(1+w_A)}. \tag{88.10}
$$

Equation (88.10) is EXTERNAL_ESTABLISHED_MATHEMATICS and follows from Equations (88.7) and (88.9).

### 88.11 Density parameters

At a selected epoch the normalized Friedmann constraint is

$$
1=\Omega_{\mathrm m}+\Omega_{\mathrm r}+\Omega_{\Lambda}+\Omega_k+\Omega_{\mathrm{native}}. \tag{88.11}
$$

Equation (88.11) is EXTERNAL_ESTABLISHED_MATHEMATICS as an effective decomposition. The final term is only a slot; no value or native content is inferred here.

### 88.12 Deceleration parameter

The dimensionless acceleration diagnostic is

$$
q=-\frac{\ddot a}{aH^2}. \tag{88.12}
$$

Equation (88.12) is EXTERNAL_ESTABLISHED_MATHEMATICS. A complete model must connect it to observables rather than merely assign a sign.

### 88.13 Conformal description

Conformal time is introduced by

$$
d\eta=\frac{dt}{a(t)},\qquad \mathcal H=\frac{a'}{a}=aH. \tag{88.13}
$$

Equation (88.13) is EXTERNAL_ESTABLISHED_MATHEMATICS and is useful when background dynamics are coupled to perturbations.

### 88.14 Effective Friedmann system

A general correction can be isolated without claiming its native form:

$$
H^2+\frac{k}{a^2}=\frac{8\pi G}{3}\rho+\frac{\Lambda}{3}+\Delta_{\mathrm F}[a,\rho,p;\Theta]. \tag{88.14}
$$

Equation (88.14) is EXTERNAL_ESTABLISHED_MATHEMATICS as an effective parameterization. The addresses `@effective_friedmann_equations` and `@effective_friedmann_system` require an explicit derivation of the functional and parameters before the final term becomes native content.

### 88.15 Interacting sectors

If components exchange energy while the total remains conserved, one may write

$$
\dot\rho_A+3H(\rho_A+p_A)=Q_A,
\qquad \sum_A Q_A=0. \tag{88.15}
$$

Equation (88.15) is EXTERNAL_ESTABLISHED_MATHEMATICS. It separates total conservation from component-level exchange and exposes where a native coupling law must enter.

### 88.16 Native reduction obligation

The missing derivational bridge can be represented as the requirement

$$
\mathcal R_{\mathrm{cosmo}}:
\mathfrak X_{\mathrm{native}}
\longrightarrow
\bigl(a,H,\rho,p,k,\Lambda,\Delta_{\mathrm F},Q_A\bigr). \tag{88.16}
$$

Equation (88.16) is EVIDENCE_BOUNDARY. Library evidence names phase cosmology, multiversal dynamics, white-state cores, and effective Friedmann systems, but the assigned set does not supply a single typed reduction map establishing their contribution to every background variable.

### 88.17 Typed chapter contract

The chapter therefore records

$$
\mathfrak M_{88}=
(g_{\mathrm{FLRW}},a,H,\rho,p,\mathcal C,\Delta_{\mathrm F},\mathcal R_{\mathrm{cosmo}},\Omega_{88}). \tag{88.17}
$$

Equation (88.17) is DETERMINISTIC_TYPE_NORMALIZATION. The tuple keeps background geometry, standard dynamics, effective corrections, reduction obligations, and open requirements distinct.

### 88.18 Coverage calibration

The native query returned

$$
N_{\mathrm{assigned}}=11,
\quad N_{\mathrm{English}}=1282,
\quad N_{\mathrm{equation}}=19,
\quad N_{\mathrm{dependency}}=1533. \tag{88.18}
$$

Equation (88.18) is DETERMINISTIC_COVERAGE_EVIDENCE. Three handles are MEDIUM and eight are THIN; none contains a recovered exact definition in the calibrated digest.

### 88.19 API evidence register

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@chapter_61_adapter_multiversal_phase_boundaries_and_cross_cycle_geometry` | Chapter 61 Adapter - Multiversal Phase Boundaries and Cross-Cycle Geometry | THIN | 12 / 0 / 0 | adapter boundary |
| `@continuity_equation_cosmology` | Continuity Equation Cosmology | MEDIUM | 75 / 5 / 214 | conservation law |
| `@effective_friedmann_equations` | Effective Friedmann Equations | THIN | 1 / 0 / 0 | correction address |
| `@effective_friedmann_system` | Effective Friedmann System | THIN | 1 / 0 / 0 | system address |
| `@friedmann_equation` | Friedmann Equation | MEDIUM | 633 / 7 / 683 | background constraint |
| `@friedmann_lemaitre_robertson_walker_spacetime` | Friedmann-Lemaitre-Robertson-Walker Spacetime | MEDIUM | 523 / 7 / 636 | background geometry |
| `@galactic_rotation_potential` | Galactic Rotation Potential | THIN | 12 / 0 / 0 | scale-boundary address |
| `@multiversal_dynamics_and_phase_correlated_cosmoi` | Multiversal Dynamics and Phase-Correlated Cosmoi | THIN | 1 / 0 / 0 | native candidate context |
| `@multiversal_phase_boundaries_and_cross_cycle_geometry` | Multiversal Phase Boundaries and Cross-Cycle Geometry | THIN | 1 / 0 / 0 | cycle-boundary context |
| `@phase_cosmology_and_background_solutions` | Phase Cosmology and Background Solutions | THIN | 1 / 0 / 0 | solution address |
| `@white_state_core_dynamics` | White-State Core Dynamics | THIN | 22 / 0 / 0 | transition candidate |

The register prevents the heavily populated standard background addresses from being conflated with the thin native extension addresses.

### 88.20 Evidence boundary

The operative distinction is

$$
\mathrm{FLRWBackground}
\ne
\mathrm{NativeDerivation},
\qquad
\mathrm{EffectiveSlot}
\ne
\mathrm{RecoveredCorrectionLaw}. \tag{88.19}
$$

Equation (88.19) is EVIDENCE_BOUNDARY. The chapter may organize a Friedmann-facing interface, but it may not fill thin addresses with unproven dynamics.

### 88.21 Open background obligations

The remaining work is

$$
\Omega_{88}=\{
\mathrm{NativeStressEnergy},
\mathrm{ReductionDerivation},
\mathrm{CorrectionFunctional},
\mathrm{ParameterUnits},
\mathrm{InitialData},
\mathrm{CycleBoundaryConditions},
\mathrm{WhiteStateCoupling},
\mathrm{ObservableConstraints}
\}. \tag{88.20}
$$

Equation (88.20) is CURATOR_SYNTHESIS. It records missing deliverables rather than manufacturing a background solution.

### 88.22 Chapter determination

The resulting status is

$$
\mathrm{Background}_{88}
=
\mathrm{ESTABLISHED\_FLRW\_AND\_FRIEDMANN\_SCAFFOLD}
+\mathrm{CALIBRATED\_NATIVE\_ADDRESS\_REGISTER}
+\mathrm{OPEN\_MK\_DERIVATION}. \tag{88.21}
$$

Equation (88.21) is DETERMINISTIC_STATUS_NORMALIZATION. The chapter supplies a rigorous background scaffold and a typed boundary for later native cosmological work; it does not claim that the thin phase, multiversal, or white-state records already determine cosmological dynamics.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@chapter_61_adapter_multiversal_phase_boundaries_and_cross_cycle_geometry` | @chapter_61_adapter_multiversal_phase_boundaries_and_cross_cycle_geometry` — Chapter 61 Adapter — Multiversal Phase Boundaries and Cross-Cycle Geometry | THIN | 12 / 0 / 0 | chapter-core object |
| `@continuity_equation_cosmology` | @continuity_equation_cosmology | MEDIUM | 75 / 5 / 214 | chapter-core object |
| `@effective_friedmann_equations` | @effective_friedmann_equations` — Effective Friedmann Equations | THIN | 1 / 0 / 0 | chapter-core object |
| `@effective_friedmann_system` | @effective_friedmann_system` — Effective Friedmann system | THIN | 1 / 0 / 0 | chapter-core object |
| `@friedmann_equation` | @friedmann_equation | MEDIUM | 633 / 7 / 683 | chapter-core object |
| `@friedmann_lemaitre_robertson_walker_spacetime` | @friedmann_lemaitre_robertson_walker_spacetime | MEDIUM | 523 / 7 / 636 | chapter-core object |
| `@galactic_rotation_potential` | @galactic_rotation_potential` — Galactic Rotation Potential | THIN | 12 / 0 / 0 | chapter-core object |
| `@multiversal_dynamics_and_phase_correlated_cosmoi` | @multiversal_dynamics_and_phase_correlated_cosmoi` — Multiversal Dynamics and Phase-Correlated Cosmoi | THIN | 1 / 0 / 0 | chapter-core object |
| `@multiversal_phase_boundaries_and_cross_cycle_geometry` | @multiversal_phase_boundaries_and_cross_cycle_geometry` — Multiversal Phase Boundaries and Cross-Cycle Geometry | THIN | 1 / 0 / 0 | chapter-core object |
| `@phase_cosmology_and_background_solutions` | @phase_cosmology_and_background_solutions` — Phase Cosmology and Background Solutions | THIN | 1 / 0 / 0 | chapter-core object |
| `@white_state_core_dynamics` | @white_state_core_dynamics` — White-State Core Dynamics | THIN | 22 / 0 / 0 | chapter-core object |
