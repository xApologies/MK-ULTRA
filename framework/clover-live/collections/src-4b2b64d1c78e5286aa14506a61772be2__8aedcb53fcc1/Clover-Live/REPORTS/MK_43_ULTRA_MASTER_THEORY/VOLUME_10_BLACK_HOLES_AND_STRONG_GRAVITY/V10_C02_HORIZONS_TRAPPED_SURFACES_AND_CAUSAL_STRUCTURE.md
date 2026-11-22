# VOLUME X - BLACK HOLES AND STRONG GRAVITY

## Chapter 82 - Horizons, Trapped Surfaces, and Causal Structure

### 82.1 Surface geometry

Let S be a compact spacelike codimension-two surface in spacetime,

$$
S\hookrightarrow(M,g). \tag{82.1}
$$

Equation (82.1) is EXTERNAL_ESTABLISHED_MATHEMATICS. Compactness, orientability, regularity, and boundary conditions are part of the surface specification.

### 82.2 Null normals

Choose future-directed null normals satisfying

$$
\ell^a\ell_a=0,
\qquad
n^an_a=0,
\qquad
\ell^an_a=-1. \tag{82.2}
$$

Equation (82.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. Rescaling the null normals changes some representative quantities while preserving appropriately defined signs and invariants.

### 82.3 Induced metric

The surface metric is

$$
q_{ab}=g_{ab}+\ell_an_b+n_a\ell_b. \tag{82.3}
$$

Equation (82.3) is EXTERNAL_ESTABLISHED_MATHEMATICS under the stated normalization.

### 82.4 Null expansions

The outgoing and ingoing expansions are

$$
\theta_{(\ell)}=q^{ab}\nabla_a\ell_b,
\qquad
\theta_{(n)}=q^{ab}\nabla_an_b. \tag{82.4}
$$

Equation (82.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. Expansion signs classify local light-front behavior around the surface.

### 82.5 Closed trapped surface

A future trapped surface obeys

$$
\theta_{(\ell)}<0,
\qquad
\theta_{(n)}<0. \tag{82.5}
$$

Equation (82.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. It is a local geometric condition, not an event-horizon definition.

### 82.6 Marginally trapped surface

A common future marginal condition is

$$
\theta_{(\ell)}=0,
\qquad
\theta_{(n)}<0. \tag{82.6}
$$

Equation (82.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Which null direction is labeled outgoing must be fixed by context.

### 82.7 Marginally outer trapped tube

A hypersurface foliated by marginal leaves is

$$
\mathcal T=\bigcup_{v}S_v,
\qquad
\theta_{(\ell)}\big|_{S_v}=0. \tag{82.7}
$$

Equation (82.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. The causal character of the tube distinguishes different horizon notions.

### 82.8 Raychaudhuri evolution

For an affinely parameterized hypersurface-orthogonal null congruence,

$$
\frac{d\theta}{d\lambda}
=-\frac12\theta^2-\sigma_{ab}\sigma^{ab}-R_{ab}k^ak^b. \tag{82.8}
$$

Equation (82.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. Twist and non-affinity terms must be restored when the stated assumptions do not hold.

### 82.9 Null convergence condition

Classical focusing uses

$$
R_{ab}k^ak^b\ge0. \tag{82.9}
$$

Equation (82.9) is EXTERNAL_ESTABLISHED_MATHEMATICS as a geometric energy-condition form. Quantum or effective violations require separate treatment.

### 82.10 Area variation

Along a null generator,

$$
\frac{d}{d\lambda}\log\sqrt{q}=\theta. \tag{82.10}
$$

Equation (82.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. It relates expansion to local cross-sectional area change.

### 82.11 Dynamical horizon

A standard dynamical-horizon signature is summarized by

$$
\operatorname{sign}(g|_{\mathcal H_D})=(+,+,+),
\qquad
\theta_{(\ell)}=0,
\quad
\theta_{(n)}<0. \tag{82.11}
$$

Equation (82.11) is EXTERNAL_ESTABLISHED_MATHEMATICS for a spacelike foliated horizon. Precise regularity and outer conditions remain part of the definition.

### 82.12 Outer trapping condition

One future-outer condition is

$$
\mathcal L_n\theta_{(\ell)}<0. \tag{82.12}
$$

Equation (82.12) is EXTERNAL_ESTABLISHED_MATHEMATICS. It distinguishes an outer trapping horizon from other marginal tubes.

### 82.13 Cauchy horizon

For initial data on a partial Cauchy surface Sigma, the future Cauchy horizon is

$$
H^{+}(\Sigma)=\overline{D^{+}(\Sigma)}\setminus I^{-}(D^{+}(\Sigma)). \tag{82.13}
$$

Equation (82.13) is EXTERNAL_ESTABLISHED_MATHEMATICS in a standard causal-set convention. It concerns predictability from initial data rather than local trapping.

### 82.14 Event and apparent boundaries

The global and slicing-dependent boundaries are schematically distinct,

$$
\mathcal H^{+}=\partial J^{-}(\mathscr I^{+}),
\qquad
\mathcal A_t=\partial\{S\subset\Sigma_t:\theta_{(\ell)}<0\}. \tag{82.14}
$$

Equation (82.14) is EXTERNAL_ESTABLISHED_MATHEMATICS as a comparison schema. The apparent-horizon expression depends on the chosen foliation.

### 82.15 Cosmological horizon scale

For a Robertson-Walker expansion, the comoving particle-horizon scale is

$$
\chi_p(t)=\int_{t_i}^{t}\frac{dt'}{a(t')}. \tag{82.15}
$$

Equation (82.15) is EXTERNAL_ESTABLISHED_MATHEMATICS. Cosmological, particle, black-hole, and white-horizon terms must not be collapsed into one geometry.

### 82.16 Area-encoding template

A conventional horizon-information relation is

$$
S_H=\frac{A_H}{4G\hbar}. \tag{82.16}
$$

Equation (82.16) is EXTERNAL_ESTABLISHED_MATHEMATICS in semiclassical gravity. It is not a recovered Module 15 encoding law.

### 82.17 Typed horizon contract

The chapter normalizes a horizon record as

$$
\mathfrak H
=\big(S,q,\ell,n,\theta_{(\ell)},\theta_{(n)},
\mathcal T,\mathrm{causal\ type},\mathcal P,\mathcal U\big). \tag{82.17}
$$

Equation (82.17) is DETERMINISTIC_TYPE_NORMALIZATION. It keeps surface data, foliation, causal type, provenance, and unresolved requirements explicit.

### 82.18 Coverage calibration

The native query returned

$$
N_{\mathrm{assigned}}=9,
\quad N_{\mathrm{queried}}=9,
\quad N_{\mathrm{English}}=1209,
\quad N_{\mathrm{equations}}=24. \tag{82.18}
$$

Equation (82.18) is DETERMINISTIC_COVERAGE_EVIDENCE. Five handles are MEDIUM and four are THIN; shared source content prevents raw totals from acting as independent proof counts.

### 82.19 API evidence register

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@cauchy_horizon` | @cauchy_horizon | MEDIUM | 90 / 4 / 197 | chapter-core object |
| `@closed_trapped_surface` | @closed_trapped_surface | MEDIUM | 456 / 6 / 564 | chapter-core object |
| `@dynamical_horizon` | @dynamical_horizon | MEDIUM | 89 / 4 / 185 | chapter-core object |
| `@marginally_trapped_surface` | @marginally_trapped_surface | MEDIUM | 84 / 4 / 186 | chapter-core object |
| `@module_15_horizon_and_large_scale_encoding` | @module_15_horizon_and_large_scale_encoding` — Module 15 — Horizon and Large-Scale Encoding | THIN | 9 / 0 / 0 | chapter-core object |
| `@phase_cosmology_and_holographic_horizons` | @phase_cosmology_and_holographic_horizons` — Phase Cosmology and Holographic Horizons | THIN | 1 / 0 / 0 | chapter-core object |
| `@phase_evolution_on_cosmological_horizons` | @phase_evolution_on_cosmological_horizons` — Phase Evolution on Cosmological Horizons | THIN | 0 / 0 / 0 | chapter-core object |
| `@the_white_horizon_transition` | @the_white_horizon_transition` — The White Horizon Transition | THIN | 1 / 0 / 0 | chapter-core object |
| `@trapped_surface` | @trapped_surface | MEDIUM | 479 / 6 / 571 | chapter-core object |

The register preserves local, global, cosmological, encoding, and historical white-horizon addresses without merging their meanings.

### 82.20 Evidence boundary

The operative distinctions are

$$
\begin{aligned}
\mathrm{EventHorizon}&\ne\mathrm{TrappedSurface},\\
\mathrm{MarginalSurface}&\ne\mathrm{DynamicalHorizon},\\
\mathrm{CauchyHorizon}&\ne\mathrm{CosmologicalHorizon},\\
\mathrm{AreaRelation}&\ne\mathrm{NativeEncodingMap}.
\end{aligned} \tag{82.19}
$$

Equation (82.19) is EVIDENCE_BOUNDARY. Horizon terminology is meaningful only with its geometric scope and causal construction attached.

### 82.21 Open horizon obligations

The remaining native program is

$$
\begin{aligned}
\mathfrak U_{\mathrm{hor}}=\{&
\mathrm{SurfaceRegularity},
\mathrm{NullNormalization},
\mathrm{FoliationChoice},
\mathrm{OuterCondition},
\mathrm{EnergyConditions},\\
&\mathrm{GlobalCompletion},
\mathrm{CauchyStability},
\mathrm{AreaFluxLaw},
\mathrm{Module15Map},
\mathrm{PhaseHorizonDynamics},\\
&\mathrm{HolographicTyping},
\mathrm{WhiteHorizonDefinition},
\mathrm{TransitionLaw},
\mathrm{ObservableMap},
\mathrm{ExternalValidation}\}.
\end{aligned} \tag{82.20}
$$

Equation (82.20) is CURATOR_SYNTHESIS. It records missing constructions without creating them.

### 82.22 Chapter determination

The chapter result is

$$
\begin{aligned}
\mathrm{Horizons}_{\mathrm{V10C02}}
={}&\mathrm{NINE\_NATIVE\_ADDRESSES}\\
&+\mathrm{ESTABLISHED\_SURFACE\_AND\_CAUSAL\_GEOMETRY}\\
&+\mathrm{SCOPE\_PRESERVING\_HORIZON\_TAXONOMY}\\
&+\mathrm{OPEN\_NATIVE\_ENCODING\_AND\_TRANSITION\_LAWS}.
\end{aligned} \tag{82.21}
$$

Equation (82.21) is DETERMINISTIC_STATUS_NORMALIZATION. Library 4.1 makes the principal horizon scopes addressable while their native MK Ultra maps and proofs remain bounded by explicit requirements.
