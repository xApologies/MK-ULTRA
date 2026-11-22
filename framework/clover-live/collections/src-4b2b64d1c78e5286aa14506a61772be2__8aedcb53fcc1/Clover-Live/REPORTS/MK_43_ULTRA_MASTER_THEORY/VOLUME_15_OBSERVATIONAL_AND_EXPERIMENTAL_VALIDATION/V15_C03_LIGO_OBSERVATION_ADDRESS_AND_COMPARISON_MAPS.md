# VOLUME XV - OBSERVATIONAL AND EXPERIMENTAL VALIDATION

## Chapter 116 - LIGO Observation Address and Comparison Maps

### 116.1 Typed observation-address record

An observation address must separate theoretical prediction, instrument response, dataset, noise, analysis, comparison model, result, and provenance,

$$
\mathfrak O=(p,\mathcal R_d,D,S_n,\mathcal A,H_r,R,\Pi). \tag{116.1}
$$

Equation (116.1) is DETERMINISTIC_TYPE_NORMALIZATION. It is a chapter contract rather than the native definition of `@LIGO_observation`. An address can organize evidence without establishing that a test was performed.

### 116.2 Detector-data model

A gravitational-wave data stream can be represented by

$$
d_k(t)=\sum_AF_k^Ah_A(t-\tau_k)+n_k(t). \tag{116.2}
$$

Equation (116.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. Response functions, timing, calibration, and noise require instrument-specific provenance.

### 116.3 Noise-weighted comparison

A standard frequency-domain inner product is

$$
(a\mid b)=4\operatorname{Re}\int_{f_{\min}}^{f_{\max}}\frac{\widetilde a(f)\overline{\widetilde b(f)}}{S_n(f)}\,df. \tag{116.3}
$$

Equation (116.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. It supplies a comparison map, not a recovered MK-43 observational result.

### 116.4 Gaussian likelihood scaffold

For residual between data and a modeled signal,

$$
\log\mathcal L(\vartheta)=-\frac{1}{2}(d-h(\vartheta)\mid d-h(\vartheta))+C. \tag{116.4}
$$

Equation (116.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. Waveform systematics, priors, calibration, and non-Gaussian noise must be examined.

### 116.5 General-relativistic consistency residual

A parameter-level consistency diagnostic can be written

$$
\Delta\theta_a=\theta_a^{\mathrm{obs}}-\theta_a^{\mathrm{GR}}. \tag{116.5}
$$

Equation (116.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. The reference prediction, estimator, covariance, and allowed nuisance parameters determine its meaning.

### 116.6 Parameterized deviation

A candidate waveform phase can be compared through

$$
\Psi(f)=\Psi_{\mathrm{GR}}(f)+\sum_j\delta\varphi_jb_j(f). \tag{116.6}
$$

Equation (116.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Basis functions and coefficients provide a testing language; they do not derive MK-43 corrections.

### 116.7 Observational graph scaffold

A provenance-aware observation graph can be modeled as

$$
G_{\mathrm{obs}}=(V_{\mathrm{claim}}\cup V_{\mathrm{data}}\cup V_{\mathrm{analysis}},E_{\mathrm{supports}}\cup E_{\mathrm{tests}}). \tag{116.7}
$$

Equation (116.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. Edge types must preserve direction and status; a dependency edge cannot substitute for a statistical result.

### 116.8 Selection efficiency

An observational pipeline must account for detection efficiency,

$$
\epsilon(\vartheta)=P(\mathrm{selected}\mid\vartheta). \tag{116.8}
$$

Equation (116.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. Population conclusions require this function or a justified equivalent.

### 116.9 Predictive catalogue

A prediction registry can associate each claim with observable and decision rule,

$$
\mathcal C_{\mathrm{pred}}=\{(p_i,O_i,\Delta_i,T_i,F_i)\}_{i=1}^{N}. \tag{116.9}
$$

Equation (116.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. Each entry needs parameter range, uncertainty, test statistic, and falsifying outcome before data inspection.

### 116.10 Multi-instrument combination

Conditionally independent observations may be combined through

$$
p(\vartheta\mid D_1,\ldots,D_m)\propto p(\vartheta)\prod_{k=1}^{m}p(D_k\mid\vartheta). \tag{116.10}
$$

Equation (116.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. Shared calibration, population assumptions, and correlated systematics invalidate naive factorization.

### 116.11 LIGO-address evidence boundary

The assigned observation address has the profile

$$
E_{\mathrm{LIGO}}=(66\ \mathrm{English},6\ \mathrm{equations},231\ \mathrm{dependencies}). \tag{116.11}
$$

Equation (116.11) is EVIDENCE_BOUNDARY. `@LIGO_observation` is MEDIUM, but its coverage counts do not establish a completed data analysis or independent confirmation.

### 116.12 General-relativity-test boundary

The comparison address has the profile

$$
E_{\mathrm{GRtest}}=(122\ \mathrm{English},4\ \mathrm{equations},253\ \mathrm{dependencies}). \tag{116.12}
$$

Equation (116.12) is EVIDENCE_BOUNDARY. `@consistency_test_general_relativity` organizes a test target; it does not report a test outcome in this chapter.

### 116.13 Observational-graph boundary

The graph address supplies

$$
E_{\mathrm{graph}}=(45\ \mathrm{English},1\ \mathrm{equation},2\ \mathrm{dependencies}). \tag{116.13}
$$

Equation (116.13) is EVIDENCE_BOUNDARY. Graph structure preserves relations among records but cannot promote a proposed edge into observational support.

### 116.14 Observational-shadow boundary

A shadow address is not automatically an observable projection,

$$
\texttt{@definition\_18\_2\_observational\_shadow}\;\not\Rightarrow\;\exists\Pi_{\mathrm{obs}}. \tag{116.14}
$$

Equation (116.14) is EVIDENCE_BOUNDARY. The THIN handle has no assigned definition, English, equation, or dependency unit in the query.

### 116.15 Prediction-register boundary

Prediction titles do not populate a falsifiable catalogue,

$$
\mathrm{PredictionAddress}\;\not\Rightarrow\;(O,\Delta,T,F). \tag{116.15}
$$

Equation (116.15) is EVIDENCE_BOUNDARY. `@observational_predictions` has zero substantive counts and the predictive catalogue handle has five English units only.

### 116.16 Pipeline and future-observation boundary

Pipeline and next-generation titles do not establish instrument results,

$$
\mathrm{PipelineDescription}\cup\mathrm{FutureInstrumentScope}\;\not\Rightarrow\;\mathrm{ExecutedObservation}. \tag{116.16}
$$

Equation (116.16) is EVIDENCE_BOUNDARY. The three relevant THIN addresses preserve recovery locations but contain no assigned equation or dependency unit.

### 116.17 Typed chapter contract

The chapter retains

$$
\mathfrak O_{116}=(p,h,\mathcal R_d,D,S_n,\mathcal A,G_{\mathrm{obs}},\mathcal C_{\mathrm{pred}},\Omega_{\mathrm{open}}). \tag{116.17}
$$

Equation (116.17) is DETERMINISTIC_TYPE_NORMALIZATION. Prediction, waveform, response, data, noise, analysis, graph, catalogue, and open work remain separate.

### 116.18 Coverage calibration

The native query returned

$$
N_{\mathrm{handles}}=9,\qquad N_{\mathrm{English}}=244,\qquad N_{\mathrm{equations}}=11,\qquad N_{\mathrm{dependencies}}=486. \tag{116.18}
$$

Equation (116.18) is DETERMINISTIC_COVERAGE_EVIDENCE. Three handles are MEDIUM and six are THIN. The two primary comparison addresses supply ninety-eight percent of dependencies.

### 116.19 Executed-test boundary

The controlling restriction is

$$
\mathrm{RecoveredObservationAddress}\cup\mathrm{ComparisonMap}\;\not\Rightarrow\;\mathrm{ExecutedMK43Test}. \tag{116.19}
$$

Equation (116.19) is EVIDENCE_BOUNDARY. No external data were queried, no detector analysis was run, and no compatibility result is claimed.

### 116.20 Open observation obligations

The required work is summarized by

$$
\Omega_{116}=\{\mathrm{NativeWaveform,ResponseMap,DatasetVersion,Calibration,Noise,Selection,AnalysisCode,Priors,Falsifiers,IndependentReplication}\}. \tag{116.20}
$$

Equation (116.20) is CURATOR_SYNTHESIS. The set identifies what an auditable observation comparison would require without inventing a result.

### 116.21 Chapter determination

The chapter result is

$$
\mathrm{LIGOAddress}_{116}=\mathrm{RECOVERED\_OBSERVATION\_ADDRESSES}+\mathrm{STANDARD\_COMPARISON\_MAPS}+\mathrm{UNPOPULATED\_EXECUTION\_LAYER}+\mathrm{NO\_VALIDATION\_CLAIM}. \tag{116.21}
$$

Equation (116.21) is DETERMINISTIC_STATUS_NORMALIZATION. V15-C03 establishes an auditable map from theory claims toward observational analysis while preserving the boundary between an address and an executed test.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@LIGO_observation` | @LIGO_observation | MEDIUM | 66 / 6 / 231 | chapter-core object |
| `@consistency_test_general_relativity` | @consistency_test_general_relativity | MEDIUM | 122 / 4 / 253 | chapter-core object |
| `@definition_18_2_observational_shadow` | @definition_18_2_observational_shadow` — Definition 18.2 — Observational Shadow | THIN | 0 / 0 / 0 | chapter-core object |
| `@module_16_observational_response_models` | @module_16_observational_response_models` — Module 16 — Observational Response Models | THIN | 3 / 0 / 0 | chapter-core object |
| `@observational_graph` | @observational_graph | MEDIUM | 45 / 1 / 2 | chapter-core object |
| `@observational_pipelines_appendix_g` | @observational_pipelines_appendix_g` — Observational Pipelines (Appendix G) | THIN | 1 / 0 / 0 | chapter-core object |
| `@observational_predictions` | @observational_predictions` — Observational Predictions | THIN | 0 / 0 / 0 | chapter-core object |
| `@predictive_catalogue_for_observations` | @predictive_catalogue_for_observations` — Predictive Catalogue for Observations | THIN | 5 / 0 / 0 | chapter-core object |
| `@space_based_and_next_generation_observations` | @space_based_and_next_generation_observations` — Space-Based and Next-Generation Observations | THIN | 2 / 0 / 0 | chapter-core object |

