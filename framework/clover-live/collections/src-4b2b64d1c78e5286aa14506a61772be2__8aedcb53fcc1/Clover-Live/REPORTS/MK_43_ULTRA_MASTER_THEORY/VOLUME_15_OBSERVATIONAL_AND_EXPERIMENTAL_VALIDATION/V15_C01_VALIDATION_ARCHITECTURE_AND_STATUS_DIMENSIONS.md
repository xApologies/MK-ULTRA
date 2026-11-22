# VOLUME XV - OBSERVATIONAL AND EXPERIMENTAL VALIDATION

## Chapter 114 - Validation Architecture and Status Dimensions

### 114.1 Typed validation record

A validation claim must distinguish object, proposition, source, derivation, observable, dataset, test, outcome, and status,

$$
\mathfrak V=(q,p,s,d,o,D,T,R,\sigma). \tag{114.1}
$$

Equation (114.1) is DETERMINISTIC_TYPE_NORMALIZATION. It defines the chapter audit contract, not a recovered native validation object. Missing slots remain explicit rather than being filled by confidence language.

### 114.2 Orthogonal status dimensions

The chapter tracks validation as a vector rather than a single scalar,

$$
\sigma=(\sigma_{\mathrm{source}},\sigma_{\mathrm{math}},\sigma_{\mathrm{internal}},\sigma_{\mathrm{empirical}},\sigma_{\mathrm{external}},\sigma_{\mathrm{replication}}). \tag{114.2}
$$

Equation (114.2) is CURATOR_SYNTHESIS. The components prevent exact recovery, formal derivation, internal consistency, empirical fit, outside confirmation, and reproducibility from being silently collapsed.

### 114.3 Measurement model

An observational comparison requires a map from theoretical state to measured data,

$$
y=h(x;\theta)+\epsilon. \tag{114.3}
$$

Equation (114.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. The instrument response, units, calibration, selection function, and noise distribution must accompany the model.

### 114.4 Residual definition

For predicted and observed vectors, the residual is

$$
r=y_{\mathrm{obs}}-y_{\mathrm{pred}}(\theta). \tag{114.4}
$$

Equation (114.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. Residual interpretation depends on covariance, model adequacy, preprocessing, and the construction of the prediction.

### 114.5 Covariance-weighted discrepancy

For nonsingular covariance matrix, a standard quadratic discrepancy is

$$
\chi^2(\theta)=r^{\mathsf T}\Sigma^{-1}r. \tag{114.5}
$$

Equation (114.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. A numerical value is meaningful only when distributional and independence assumptions are examined.

### 114.6 Likelihood comparison

For conditionally Gaussian residuals, the log likelihood contains

$$
\log\mathcal L(\theta)=-\frac{1}{2}r^{\mathsf T}\Sigma^{-1}r-\frac{1}{2}\log|\Sigma|+C. \tag{114.6}
$$

Equation (114.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Likelihood support remains conditional on the observation and error models and is not proof of the underlying ontology.

### 114.7 Held-out predictive risk

Generalization can be assessed on observations excluded from fitting,

$$
R_{\mathrm{test}}=\frac{1}{n_{\mathrm{test}}}\sum_{i\in D_{\mathrm{test}}}\ell(\widehat f(x_i),y_i). \tag{114.7}
$$

Equation (114.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. Split construction, leakage control, hyperparameter selection, and uncertainty must be documented.

### 114.8 Predeclared falsification region

A falsifiable test specifies a rejection region before examining the outcome,

$$
\mathcal R_\alpha=\{y:T(y)\ge c_\alpha\},\qquad P_{H_0}(Y\in\mathcal R_\alpha)\le\alpha. \tag{114.8}
$$

Equation (114.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. A failed threshold is not automatically theory-wide falsification unless auxiliary assumptions and scope are explicit.

### 114.9 Sensitivity analysis

Dependence on parameters can be summarized locally by

$$
S_{ij}=\frac{\partial\log O_i}{\partial\log\theta_j}. \tag{114.9}
$$

Equation (114.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. Structural nonidentifiability and nonlinear regime changes require analyses beyond a local derivative.

### 114.10 Provenance seal

An append-only audit chain can link each record to its predecessor,

$$
H_k=\operatorname{SHA256}(H_{k-1}\Vert\mathrm{id}_k\Vert\mathrm{payload}_k). \tag{114.10}
$$

Equation (114.10) is DETERMINISTIC_AUDIT_NORMALIZATION. Hash continuity detects byte changes; it does not certify scientific truth or the quality of the underlying evidence.

### 114.11 Assigned-address absence

The chapter ledger assigns no QMO handles,

$$
N_{\mathrm{assigned\ handles}}=0. \tag{114.11}
$$

Equation (114.11) is EVIDENCE_BOUNDARY. The validation architecture is therefore an explicit curatorial and external-method scaffold, not a synthesis of native handle content.

### 114.12 Status noncollapse

The principal validation dimensions cannot be substituted for one another,

$$
\sigma_{\mathrm{source}}\not\equiv\sigma_{\mathrm{math}}\not\equiv\sigma_{\mathrm{empirical}}\not\equiv\sigma_{\mathrm{external}}. \tag{114.12}
$$

Equation (114.12) is EVIDENCE_BOUNDARY. Exact quotation may support provenance while leaving equations unproved and predictions untested.

### 114.13 Proof and observation boundary

Formal proof and empirical confirmation answer different questions,

$$
\mathrm{FormalDerivation}\;\not\Rightarrow\;\mathrm{PhysicalRealization},\qquad
\mathrm{EmpiricalFit}\;\not\Rightarrow\;\mathrm{UniqueTheory}. \tag{114.13}
$$

Equation (114.13) is EVIDENCE_BOUNDARY. Mathematical validity concerns consequences of assumptions; empirical validation concerns correspondence with measured systems.

### 114.14 Coverage boundary

Population of a Library address is not a validation score,

$$
\mathrm{CoverageDepth}\;\not\equiv\;\mathrm{EvidenceStrength}. \tag{114.14}
$$

Equation (114.14) is EVIDENCE_BOUNDARY. Repeated content, dependency density, and many source occurrences must not inflate independent support.

### 114.15 Internal and external boundary

Internal consistency is necessary but not sufficient for external confirmation,

$$
\mathrm{InternalConsistency}\;\not\Rightarrow\;\mathrm{ExternalValidation}. \tag{114.15}
$$

Equation (114.15) is EVIDENCE_BOUNDARY. Independent data, instruments, analysts, and replications remain separate requirements.

### 114.16 Canon and validation boundary

Curatorial status cannot determine scientific outcome,

$$
\mathrm{CurrentCanonCandidate}\;\not\Rightarrow\;\mathrm{ValidatedLaw}. \tag{114.16}
$$

Equation (114.16) is EVIDENCE_BOUNDARY. Canon status organizes a framework; it does not override absent proof, measurement, or replication.

### 114.17 Typed chapter contract

The chapter closes its architecture as

$$
\mathfrak V_{114}=(q,p,s,d,h,D,T,R,\sigma,\Omega_{\mathrm{open}}). \tag{114.17}
$$

Equation (114.17) is DETERMINISTIC_TYPE_NORMALIZATION. Claim, source, derivation, observation map, data, test, result, status vector, and open work remain separately addressable.

### 114.18 Coverage calibration

The native query returned

$$
N_{\mathrm{handles}}=0,\qquad N_{\mathrm{English}}=0,\qquad N_{\mathrm{equations}}=0,\qquad N_{\mathrm{dependencies}}=0. \tag{114.18}
$$

Equation (114.18) is DETERMINISTIC_COVERAGE_EVIDENCE. Library 4.1 remained unchanged; zero assigned content is preserved as an evidentiary fact.

### 114.19 Scientific boundary

The controlling restriction is

$$
\mathrm{ValidationArchitecture}\;\not\Rightarrow\;\mathrm{ValidatedResult}. \tag{114.19}
$$

Equation (114.19) is EVIDENCE_BOUNDARY. A protocol becomes informative only when a specific claim, dataset, analysis, result, and decision rule occupy it.

### 114.20 Open validation obligations

The remaining work is summarized by

$$
\Omega_{114}=\{\mathrm{ClaimRegistry,ObservableMaps,Units,Datasets,NullModels,Falsifiers,Uncertainty,IndependentAnalysis,Replication,StatusGovernance}\}. \tag{114.20}
$$

Equation (114.20) is CURATOR_SYNTHESIS. The set defines cross-chapter obligations and does not invent native evidence.

### 114.21 Chapter determination

The chapter result is

$$
\mathrm{ValidationArchitecture}_{114}=\mathrm{ORTHOGONAL\_STATUS\_DIMENSIONS}+\mathrm{STANDARD\_TEST\_SCAFFOLDS}+\mathrm{PROVENANCE\_CONTROL}+\mathrm{ZERO\_ASSIGNED\_QMO\_CONTENT}. \tag{114.21}
$$

Equation (114.21) is DETERMINISTIC_STATUS_NORMALIZATION. V15-C01 establishes an audit vocabulary for later observational chapters while clearly labeling its handle-level evidence absence.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|

