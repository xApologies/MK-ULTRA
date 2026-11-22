# VOLUME XV - OBSERVATIONAL AND EXPERIMENTAL VALIDATION

## Chapter 115 - Gravitational-Wave Compatibility Program

### 115.1 Typed waveform-test record

A gravitational-wave compatibility test must distinguish source parameters, propagation, polarizations, detector response, noise, waveform family, statistic, and status,

$$
\mathfrak W=(\vartheta_s,\mathcal P,h_A,\mathcal R_d,S_n,\mathcal H,T,\sigma). \tag{115.1}
$$

Equation (115.1) is DETERMINISTIC_TYPE_NORMALIZATION. It is a testing contract, not a recovered MK-43 waveform model. Every physics-bearing slot must be populated before comparison with data.

### 115.2 Polarization decomposition

A metric strain observed along a line of sight may be decomposed into polarization tensors,

$$
h_{ij}(t,\mathbf n)=\sum_Ah_A(t,\mathbf n)e^A_{ij}(\mathbf n). \tag{115.2}
$$

Equation (115.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. The allowed polarization set depends on the theory and must not be assumed for an untyped candidate model.

### 115.3 Detector response

For a detector with antenna responses, the measured strain is modeled by

$$
h_d(t)=\sum_AF_d^A(\mathbf n,\psi)h_A(t-\tau_d). \tag{115.3}
$$

Equation (115.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. Calibration, timing, orientation, duty cycle, and data-quality choices are part of the observational map.

### 115.4 Noise-weighted inner product

Waveform comparisons commonly use

$$
(a\mid b)=4\operatorname{Re}\int_{f_{\min}}^{f_{\max}}\frac{\widetilde a(f)\overline{\widetilde b(f)}}{S_n(f)}\,df. \tag{115.4}
$$

Equation (115.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. Frequency range, windowing, noise estimation, and nonstationarity affect the result.

### 115.5 Matched-filter signal-to-noise ratio

For a template waveform, the optimal statistic is

$$
\rho=\frac{(d\mid h)}{\sqrt{(h\mid h)}}. \tag{115.5}
$$

Equation (115.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. A high score supports compatibility with the template under the noise model; it does not establish unique theory identity.

### 115.6 Waveform mismatch

Normalized mismatch can be defined by

$$
\mathcal M=1-\max_{t_c,\phi_c}\frac{(h_1\mid h_2)}{\sqrt{(h_1\mid h_1)(h_2\mid h_2)}}. \tag{115.6}
$$

Equation (115.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Maximized nuisance parameters and the chosen noise spectrum must be stated.

### 115.7 Phase residual

A frequency-dependent phase deviation may be parameterized as

$$
\delta\Psi(f)=\Psi_{\mathrm{candidate}}(f)-\Psi_{\mathrm{reference}}(f). \tag{115.7}
$$

Equation (115.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. A candidate program must derive this quantity from its dynamics rather than fit an arbitrary residual after inspection.

### 115.8 Propagation modification

A model-independent dispersion scaffold can be written

$$
\omega^2=k^2+\sum_{n}a_n\frac{k^n}{\Lambda^{n-2}}. \tag{115.8}
$$

Equation (115.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. Coefficients, dimensions, stability, causality, and applicable regime require a theory-specific derivation.

### 115.9 Ringdown comparison

A damped-mode waveform may be represented by

$$
h(t)=\sum_nA_ne^{-(t-t_0)/\tau_n}\cos\!\left(\omega_n(t-t_0)+\phi_n\right). \tag{115.9}
$$

Equation (115.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. Mode frequencies and damping times must be predicted, not selected solely to improve fit.

### 115.10 Model comparison

Posterior odds between candidate and reference models obey

$$
\frac{p(H_c\mid d)}{p(H_r\mid d)}=\frac{p(d\mid H_c)}{p(d\mid H_r)}\frac{p(H_c)}{p(H_r)}. \tag{115.10}
$$

Equation (115.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. Prior volume, selection effects, waveform systematics, and calibration uncertainty must be audited.

### 115.11 Assigned-address absence

The chapter ledger assigns no QMO handles,

$$
N_{\mathrm{assigned\ handles}}=0. \tag{115.11}
$$

Equation (115.11) is EVIDENCE_BOUNDARY. No native equation, waveform, detector relation, or observational dependency is imported into this chapter.

### 115.12 Compatibility boundary

Agreement with gravitational-wave data would not uniquely confirm MK-43,

$$
\mathrm{DataCompatibility}\;\not\Rightarrow\;\mathrm{UniqueTheoryConfirmation}. \tag{115.12}
$$

Equation (115.12) is EVIDENCE_BOUNDARY. Standard general-relativistic behavior and competing modifications can occupy overlapping observational regions.

### 115.13 Generation boundary

The program lacks an assigned native waveform generator,

$$
\nexists\,\mathcal G_{\mathrm{MK43}}:\vartheta_s\longmapsto\{h_A(t)\}_A. \tag{115.13}
$$

Equation (115.13) is EVIDENCE_BOUNDARY. A future generator must connect the framework's equations to source dynamics, initial data, gauge choices, and asymptotic radiation.

### 115.14 Propagation boundary

No assigned content defines a theory-specific propagation map,

$$
\nexists\,\mathcal P_{\mathrm{MK43}}:h_A^{\mathrm{source}}\longmapsto h_A^{\mathrm{detector}}. \tag{115.14}
$$

Equation (115.14) is EVIDENCE_BOUNDARY. Cosmological distance, dispersion, attenuation, lensing, and polarization transport remain unpopulated.

### 115.15 Detector boundary

Detector response is external instrumentation, not a framework identity,

$$
\mathrm{TheoryWaveform}\;\not\equiv\;\mathrm{DetectorData}. \tag{115.15}
$$

Equation (115.15) is EVIDENCE_BOUNDARY. Calibration and analysis pipelines mediate the comparison and require independent provenance.

### 115.16 Observation-address boundary

The specific LIGO address belongs to the next chapter's assigned set,

$$
\texttt{@LIGO\_observation}\notin\mathcal H_{115}. \tag{115.16}
$$

Equation (115.16) is EVIDENCE_BOUNDARY. This chapter does not borrow or preempt V15-C03 evidence.

### 115.17 Typed program contract

The program retains

$$
\mathfrak W_{115}=(\vartheta_s,\mathcal G,\mathcal P,\mathcal R_d,S_n,\mathcal T,\mathcal F,\Omega_{\mathrm{open}}). \tag{115.17}
$$

Equation (115.17) is DETERMINISTIC_TYPE_NORMALIZATION. Generation, propagation, response, noise, statistic, falsifier, and open work remain distinct.

### 115.18 Coverage calibration

The native query returned

$$
N_{\mathrm{handles}}=0,\qquad N_{\mathrm{English}}=0,\qquad N_{\mathrm{equations}}=0,\qquad N_{\mathrm{dependencies}}=0. \tag{115.18}
$$

Equation (115.18) is DETERMINISTIC_COVERAGE_EVIDENCE. Library 4.1 remained unchanged and no neighboring address was used to disguise the absence.

### 115.19 Scientific boundary

The controlling restriction is

$$
\mathrm{CompatibilityProgram}\;\not\Rightarrow\;\mathrm{ExecutedTest}\;\not\Rightarrow\;\mathrm{Validation}. \tag{115.19}
$$

Equation (115.19) is EVIDENCE_BOUNDARY. No gravitational-wave dataset was analyzed and no experimental result is claimed.

### 115.20 Open gravitational-wave obligations

The required work is summarized by

$$
\Omega_{115}=\{\mathrm{SourceDynamics,WaveformGenerator,Propagation,Polarizations,DetectorResponse,Noise,Systematics,Priors,Falsifiers,IndependentReplication}\}. \tag{115.20}
$$

Equation (115.20) is CURATOR_SYNTHESIS. These obligations define a future compatibility program without creating missing framework physics.

### 115.21 Chapter determination

The chapter result is

$$
\mathrm{GWProgram}_{115}=\mathrm{STANDARD\_COMPARISON\_ARCHITECTURE}+\mathrm{EXPLICIT\_MISSING\_MAPS}+\mathrm{ZERO\_ASSIGNED\_QMO\_CONTENT}+\mathrm{NO\_EXECUTED\_TEST}. \tag{115.21}
$$

Equation (115.21) is DETERMINISTIC_STATUS_NORMALIZATION. V15-C02 establishes a disciplined gravitational-wave testing interface and does not present a native waveform or observational confirmation.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|

