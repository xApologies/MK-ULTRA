# VOLUME XVI - PREDICTIONS AND ENGINEERING APPLICATIONS

## Chapter 121 - Prediction Registry and Freeze Protocol

### 121.1 Typed prediction record

A testable prediction requires a claim, scope, parameter state, observable, measurement map, uncertainty, decision rule, deadline, provenance, and status,

$$
\mathfrak P=(C,S,\boldsymbol\theta,O,M,U,R,t,\mathcal P,\sigma). \tag{121.1}
$$

Equation (121.1) is DETERMINISTIC_TYPE_NORMALIZATION. It is a publication contract rather than a recovered universal definition of a prediction.

### 121.2 Prediction map

For a specified model and parameter state, a predicted observable can be written

$$
\widehat O=F_{\mathcal M}(\boldsymbol\theta,X). \tag{121.2}
$$

Equation (121.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. Inputs, domain, approximation order, units, and nuisance quantities must be declared.

### 121.3 Probabilistic prediction

A predictive distribution has the form

$$
p(O_{\mathrm{new}}\mid D,\mathcal M)=\int p(O_{\mathrm{new}}\mid\boldsymbol\theta,\mathcal M)p(\boldsymbol\theta\mid D,\mathcal M)\,d\boldsymbol\theta. \tag{121.3}
$$

Equation (121.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. The distribution is conditional on the declared model, data, likelihood, prior, and integration procedure.

### 121.4 Prediction interval

An interval forecast may be specified by

$$
\Pr\!\left(O_{\mathrm{new}}\in I_{1-\alpha}\mid\mathcal I\right)=1-\alpha. \tag{121.4}
$$

Equation (121.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. The conditioning information and coverage interpretation must accompany the interval.

### 121.5 Frozen prediction identity

A prediction can be frozen to an immutable content digest,

$$
h_P=\operatorname{SHA256}(C\Vert S\Vert\boldsymbol\theta\Vert F\Vert U\Vert R\Vert t). \tag{121.5}
$$

Equation (121.5) is DETERMINISTIC_AUDIT_NORMALIZATION. The digest establishes byte identity and ordering, not scientific correctness.

### 121.6 Pre-observation condition

To avoid retrospective relabeling, the freeze time must precede the observation time,

$$
t_{\mathrm{freeze}}<t_{\mathrm{observation}}. \tag{121.6}
$$

Equation (121.6) is DETERMINISTIC_AUDIT_NORMALIZATION. Embargoed or blinded data require equivalent provenance controls.

### 121.7 Proper scoring rule

For a predictive density $q$ and observed outcome $o$, the logarithmic score is

$$
S_{\log}(q,o)=-\log q(o). \tag{121.7}
$$

Equation (121.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. The score compares stated distributions; it does not supply missing measurement or selection models.

### 121.8 Calibration condition

For repeated probability forecasts, calibration can be expressed schematically as

$$
\Pr(Y=1\mid\widehat p=p)=p. \tag{121.8}
$$

Equation (121.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. Binning, sample size, dependence, and covariate shift affect empirical assessment.

### 121.9 Decision rule

A registered test maps data to an outcome label,

$$
R(D)=\begin{cases}\mathrm{PASS},&T(D)\in\mathcal A,\\ \mathrm{FAIL},&T(D)\notin\mathcal A.\end{cases} \tag{121.9}
$$

Equation (121.9) is DETERMINISTIC_TYPE_NORMALIZATION. Inconclusive and invalid-data outcomes may be added, but they must be defined before evaluation.

### 121.10 Versioned registry

A registry is an append-only ordered set of records,

$$
\mathcal R_P=(r_1,\ldots,r_n),\qquad r_i=(\mathrm{id}_i,h_i,t_i,\sigma_i). \tag{121.10}
$$

Equation (121.10) is DETERMINISTIC_AUDIT_NORMALIZATION. Revision creates a new record linked to its predecessor rather than overwriting the frozen claim.

### 121.11 Freeze-protocol evidence profile

The native freeze address supplies

$$
E(\texttt{@prediction\_freeze\_protocol})=(15\ \mathrm{English},5\ \mathrm{equations},1\ \mathrm{dependency}). \tag{121.11}
$$

Equation (121.11) is DETERMINISTIC_COVERAGE_EVIDENCE. Its MEDIUM rating supports an addressable protocol layer, while this chapter keeps its exact native records separate from the normalized audit contract.

### 121.12 Prediction-registry evidence profile

The registry address has

$$
E(\texttt{@prediction\_registry})=(1,2,0). \tag{121.12}
$$

Equation (121.12) is DETERMINISTIC_COVERAGE_EVIDENCE. MEDIUM coverage does not imply that a complete executed prediction catalogue is present.

### 121.13 Testable-predictions boundary

The third assigned address has no English, equation, or dependency unit,

$$
E(\texttt{@testable\_predictions})=(0,0,0). \tag{121.13}
$$

Equation (121.13) is EVIDENCE_BOUNDARY. Its THIN status preserves addressability without inventing a claim, observable, or falsifier.

### 121.14 Registry and result boundary

An entry records what was claimed, but

$$
\mathrm{Registered}(C)\;\not\Rightarrow\;\mathrm{Confirmed}(C). \tag{121.14}
$$

Equation (121.14) is EVIDENCE_BOUNDARY. Confirmation requires later observation, a valid measurement chain, and application of the frozen rule.

### 121.15 Prediction and explanation boundary

Predictive agreement does not alone identify a unique mechanism,

$$
\mathrm{PredictiveFit}\;\not\Rightarrow\;\mathrm{UniqueExplanation}. \tag{121.15}
$$

Equation (121.15) is EVIDENCE_BOUNDARY. Competing models and parameter degeneracies must be retained.

### 121.16 Freeze and immutability boundary

A frozen record may be superseded only by lineage,

$$
r_i\longrightarrow r_{i+1},\qquad r_i\ \mathrm{unchanged}. \tag{121.16}
$$

Equation (121.16) is DETERMINISTIC_AUDIT_NORMALIZATION. The later record does not retroactively alter the earlier prediction.

### 121.17 Typed chapter contract

The retained prediction chain is

$$
\mathfrak P_{121}=(C,S,\Theta,O,M,U,F,R,\mathcal R_P,\Omega_{\mathrm{open}}). \tag{121.17}
$$

Equation (121.17) is DETERMINISTIC_TYPE_NORMALIZATION. Claim, scope, parameters, observable, measurement, uncertainty, freeze, rule, registry, and open work remain distinct.

### 121.18 Coverage calibration

The three assigned addresses provide

$$
N_H=3,\qquad N_{\mathrm{English}}=16,\qquad N_{\mathrm{equations}}=7,\qquad N_{\mathrm{dependencies}}=1. \tag{121.18}
$$

Equation (121.18) is DETERMINISTIC_COVERAGE_EVIDENCE. Two handles are MEDIUM and one is THIN; dependency count is not treated as a prediction result.

### 121.19 Scientific boundary

The controlling restriction is

$$
\mathrm{FreezeProtocol}\cup\mathrm{RegistryAddress}\;\not\Rightarrow\;\mathrm{ExecutedPredictionTest}. \tag{121.19}
$$

Equation (121.19) is EVIDENCE_BOUNDARY. No new external data were queried and no prediction was adjudicated in this chapter.

### 121.20 Open prediction obligations

The required path is

$$
\begin{aligned}
\Omega_{121}=\{&\mathrm{ExactClaims,ParameterRanges,ObservableMaps,Units,Uncertainty},\\
&\mathrm{FreezeTimes,DecisionRules,DataProvenance,Alternatives,Replication}\}. \tag{121.20}
\end{aligned}
$$

Equation (121.20) is CURATOR_SYNTHESIS. These obligations convert an addressable prediction program into auditable future tests without manufacturing results.

### 121.21 Chapter determination

The chapter result is

$$
\begin{aligned}
\mathrm{PredictionRegistry}_{121}={}&\mathrm{THREE\_NATIVE\_ADDRESSES}+\mathrm{APPEND\_ONLY\_FREEZE\_CONTRACT}\\
&+\mathrm{EXTERNAL\_SCORING\_SCAFFOLDS}+\mathrm{NO\_EXECUTED\_TEST}. \tag{121.21}
\end{aligned}
$$

Equation (121.21) is DETERMINISTIC_STATUS_NORMALIZATION. V16-C01 establishes the publication's prediction-registration discipline while preserving the difference between a frozen claim and its later outcome.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@prediction_freeze_protocol` | @prediction_freeze_protocol | MEDIUM | 15 / 5 / 1 | chapter-core object |
| `@prediction_registry` | @prediction_registry | MEDIUM | 1 / 2 / 0 | chapter-core object |
| `@testable_predictions` | @testable_predictions` — Testable Predictions | THIN | 0 / 0 / 0 | chapter-core object |
