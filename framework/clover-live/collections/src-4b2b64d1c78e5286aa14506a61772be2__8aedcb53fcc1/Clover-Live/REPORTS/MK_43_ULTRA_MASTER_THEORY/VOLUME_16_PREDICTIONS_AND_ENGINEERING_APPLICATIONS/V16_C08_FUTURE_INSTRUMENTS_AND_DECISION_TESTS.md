# VOLUME XVI - PREDICTIONS AND ENGINEERING APPLICATIONS

## Chapter 128 - Future Instruments and Decision Tests

### 128.1 Typed instrument record

A future-instrument proposal must distinguish target signal, measurand, detector response, noise, calibration, sampling plan, statistic, decision rule, uncertainty, provenance, and status,

$$
\mathfrak I=(s,q,\mathcal R,n,\mathcal C,\Pi,T,D,U,\mathcal P,\sigma). \tag{128.1}
$$

Equation (128.1) is DETERMINISTIC_TYPE_NORMALIZATION. It is an experimental contract rather than a recovered detector design.

### 128.2 Forward measurement model

A measured record may be written

$$
\mathbf y=\mathcal H(\boldsymbol\theta)+\boldsymbol\varepsilon. \tag{128.2}
$$

Equation (128.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. Parameters, response map, disturbances, units, and sampling process must be declared.

### 128.3 Linear response scaffold

Within a justified linear regime,

$$
\mathbf y=\mathbf R\mathbf s+\mathbf n. \tag{128.3}
$$

Equation (128.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. Bandwidth, nonlinearity, drift, cross-talk, and saturation delimit the model.

### 128.4 Noise spectrum

For a stationary noise process, a power spectral density can be defined by

$$
S_n(f)=\int_{-\infty}^{\infty}C_n(\tau)e^{-2\pi i f\tau}\,d\tau. \tag{128.4}
$$

Equation (128.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. Stationarity, windowing, environmental lines, and non-Gaussian tails require validation.

### 128.5 Matched-filter statistic

For a declared template and noise spectrum, an optimal linear statistic under standard assumptions is

$$
\rho^2=4\int_0^{\infty}\frac{|\widetilde h(f)|^2}{S_n(f)}\,df. \tag{128.5}
$$

Equation (128.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. Template error, trials factors, nonstationarity, and background estimation remain part of the decision problem.

### 128.6 Likelihood-ratio test

Two explicit hypotheses may be compared through

$$
\Lambda(\mathbf y)=\frac{p(\mathbf y\mid H_1)}{p(\mathbf y\mid H_0)}. \tag{128.6}
$$

Equation (128.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Both likelihoods and the decision threshold must be fixed independently of the observed preference.

### 128.7 Bayesian model comparison

With declared priors, a Bayes factor is

$$
B_{10}=\frac{\int p(\mathbf y\mid\boldsymbol\theta_1,H_1)\,p(\boldsymbol\theta_1\mid H_1)\,d\boldsymbol\theta_1}{\int p(\mathbf y\mid\boldsymbol\theta_0,H_0)\,p(\boldsymbol\theta_0\mid H_0)\,d\boldsymbol\theta_0}. \tag{128.7}
$$

Equation (128.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. Prior sensitivity, parameter volume, computational error, and model misspecification must be disclosed.

### 128.8 Operating characteristic

A thresholded detector is characterized by

$$
P_{\mathrm D}(\tau)=\Pr(T>\tau\mid H_1),\qquad P_{\mathrm{FA}}(\tau)=\Pr(T>\tau\mid H_0). \tag{128.8}
$$

Equation (128.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. Sensitivity cannot be reported without the corresponding false-alarm behavior.

### 128.9 Calibration traceability

A calibrated estimate may be represented by

$$
\widehat q=\mathcal C(\mathbf y;\boldsymbol\alpha),\qquad U_q^2=\mathbf J_{\alpha}\boldsymbol\Sigma_{\alpha}\mathbf J_{\alpha}^{\mathsf T}+U_{\mathrm{rep}}^2. \tag{128.9}
$$

Equation (128.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. Reference standards, transfer uncertainty, repeatability, and drift belong to the reported result.

### 128.10 Sequential decision boundary

A sequential test can stop at a declared evidence boundary,

$$
\log\Lambda_k\notin(\log A,\log B)\quad\Longrightarrow\quad\mathrm{stop}. \tag{128.10}
$$

Equation (128.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. Stopping rules, error rates, data dependence, and maximum duration must be prespecified.

### 128.11 Assigned-address boundary

The authoritative chapter ledger assigns no native handle,

$$
N_{\mathrm{assigned}}(\mathrm{V16\!-\!C08})=0. \tag{128.11}
$$

Equation (128.11) is DETERMINISTIC_COVERAGE_EVIDENCE. Detector and prediction addresses completed elsewhere are not duplicated as evidence.

### 128.12 Native-query boundary

The Runtime-to-Library operation therefore returns

$$
N_{\mathrm{queries}}=0,\qquad N_{\mathrm{failures}}=0. \tag{128.12}
$$

Equation (128.12) is DETERMINISTIC_COVERAGE_EVIDENCE. The established architecture was validated while the chapter's zero-handle assignment remained intact.

### 128.13 Instrument boundary

A target signal does not imply a realizable instrument,

$$
\mathrm{TargetObservable}\;\not\Rightarrow\;\mathrm{BuildableDetector}. \tag{128.13}
$$

Equation (128.13) is EVIDENCE_BOUNDARY. Coupling, materials, dynamic range, isolation, calibration, and safety require separate engineering evidence.

### 128.14 Sensitivity boundary

A low modeled noise floor is not a detection,

$$
S_n^{1/2}<S_*^{1/2}\;\not\Rightarrow\;\mathrm{SignalObserved}. \tag{128.14}
$$

Equation (128.14) is EVIDENCE_BOUNDARY. Backgrounds, vetoes, blind injections, provenance, and independent review control the observation claim.

### 128.15 Identifiability boundary

A fitted anomaly is not unique evidence for one theory,

$$
p(\mathbf y\mid H_1)>p(\mathbf y\mid H_0)\;\not\Rightarrow\;\mathrm{UniqueMechanism}. \tag{128.15}
$$

Equation (128.15) is EVIDENCE_BOUNDARY. Alternative models, nuisance parameters, degeneracies, and out-of-sample predictions must be compared.

### 128.16 Novelty boundary

Unexpected residual structure does not automatically establish new physics,

$$
\mathrm{ResidualAnomaly}\;\not\Rightarrow\;\mathrm{NewPhysicalLaw}. \tag{128.16}
$$

Equation (128.16) is EVIDENCE_BOUNDARY. Instrumental artifacts, analysis choices, environmental coupling, and known-model incompleteness must be exhausted.

### 128.17 Typed chapter contract

The retained decision chain is

$$
\mathfrak I_{128}=(s,q,\mathcal R,n,\mathcal C,\Pi,T,D,U,\mathcal P,\Omega_{\mathrm{open}}). \tag{128.17}
$$

Equation (128.17) is DETERMINISTIC_TYPE_NORMALIZATION. Signal, measurand, response, noise, calibration, sampling, statistic, decision, uncertainty, provenance, and open work remain distinct.

### 128.18 Coverage calibration

The native evidence totals are

$$
N_H=0,\quad N_{\mathrm{English}}=0,\quad N_{\mathrm{equations}}=0,\quad N_{\mathrm{dependencies}}=0. \tag{128.18}
$$

Equation (128.18) is DETERMINISTIC_COVERAGE_EVIDENCE. The chapter supplies measurement logic, not newly populated native addresses.

### 128.19 Scientific boundary

The controlling restriction is

$$
\mathrm{FutureInstrumentConcept}\cup\mathrm{DecisionStatistic}\;\not\Rightarrow\;\mathrm{ValidatedDiscovery}. \tag{128.19}
$$

Equation (128.19) is EVIDENCE_BOUNDARY. No instrument sensitivity, detected signal, rejected null, or engineering readiness level is claimed.

### 128.20 Open experimental obligations

The future route is

$$
\begin{aligned}
\Omega_{128}=\{&\mathrm{SignalModel,Response,Noise,Calibration,Prototype,Background},\\
&\mathrm{BlindAnalysis,DecisionRule,Replication,DataRelease,Audit,Safety}\}. \tag{128.20}
\end{aligned}
$$

Equation (128.20) is CURATOR_SYNTHESIS. These obligations turn a future instrument concept into an auditable experimental program.

### 128.21 Chapter determination

The chapter result is

$$
\begin{aligned}
\mathrm{FutureTests}_{128}={}&\mathrm{MEASUREMENT\_AND\_DECISION\_CONTRACTS}\\
&+\mathrm{ZERO\_ASSIGNED\_NATIVE\_ADDRESSES}+\mathrm{NO\_DISCOVERY\_CLAIM}. \tag{128.21}
\end{aligned}
$$

Equation (128.21) is DETERMINISTIC_STATUS_NORMALIZATION. V16-C08 closes the volume with explicit instrument and decision boundaries while preserving all unresolved design and validation work.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
