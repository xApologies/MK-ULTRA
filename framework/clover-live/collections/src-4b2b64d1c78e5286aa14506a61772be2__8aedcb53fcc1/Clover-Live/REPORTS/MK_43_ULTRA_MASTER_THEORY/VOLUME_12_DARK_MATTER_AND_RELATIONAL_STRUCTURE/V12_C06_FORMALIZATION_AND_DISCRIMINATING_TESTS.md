# VOLUME XII - DARK MATTER AND RELATIONAL STRUCTURE

## Chapter 99 - Formalization and Discriminating Tests

### 99.1 Formal theory tuple

A testable relational dark-sector theory must distinguish its ingredients,

$$
\mathfrak T=(\mathcal X,\Theta,\mathcal D,\mathcal B,
\mathcal O,\mathcal P,\mathcal H,\mathcal V). \tag{99.1}
$$

Equation (99.1) is DETERMINISTIC_TYPE_NORMALIZATION. State space, parameters, dynamics, boundary data, observation map, probability model, hypotheses, and validation protocol are different record classes; the tuple is not a recovered native definition.

### 99.2 State space

Mathematical states occupy a declared space,

$$
x\in\mathcal X,
\qquad
\mathcal X=\{x\mid C_a[x]=0,\ a=1,\ldots,m\}. \tag{99.2}
$$

Equation (99.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. The constraints must state admissibility, regularity, gauge equivalence, topology, dimensions, and boundary conditions.

### 99.3 Dynamics

A deterministic evolution law can be expressed as

$$
\dot x=F(x,\theta;t),
\qquad
x(t_0)=x_0. \tag{99.3}
$$

Equation (99.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. A stochastic or discrete theory requires a correspondingly explicit transition rule instead of this template.

### 99.4 Well-posedness

For a dynamical initial-value problem, formal viability requires

$$
\exists!\,x(t),
\qquad
\|x(t;x_0)-x(t;y_0)\|\le K(t)\|x_0-y_0\|. \tag{99.4}
$$

Equation (99.4) is EXTERNAL_ESTABLISHED_MATHEMATICS as an existence, uniqueness, and continuous-dependence objective. The appropriate norm and hypotheses depend on the actual native equations.

### 99.5 Observation map

Theory variables meet measurements through

$$
\mathbf y=\mathcal O[x,\theta]+\boldsymbol\varepsilon,
\qquad
\boldsymbol\varepsilon\sim p_\varepsilon. \tag{99.5}
$$

Equation (99.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. Instrument response, selection, calibration, and nuisance parameters belong in the map rather than being hidden in qualitative comparison.

### 99.6 Dimensional consistency

Every valid equation must satisfy

$$
[\mathrm{LHS}]=[\mathrm{RHS}],
\qquad
[F_i(x,\theta;t)]=[x_i]T^{-1}. \tag{99.6}
$$

Equation (99.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Undefined units prevent comparison across scales and make numerical parameter values uninterpretable.

### 99.7 Conservation test

If the continuum interface is covariant, a candidate effective source must obey

$$
\nabla_\mu T_{\mathrm{eff}}^{\mu\nu}=0. \tag{99.7}
$$

Equation (99.7) is EXTERNAL_ESTABLISHED_MATHEMATICS as a compatibility requirement. A complete derivation should obtain it from symmetry or field equations rather than impose it after the fact.

### 99.8 Identifiability

Local parameter identifiability can be diagnosed with the Fisher matrix

$$
I_{ab}(\theta)=
\left(\frac{\partial\boldsymbol\mu}{\partial\theta_a}\right)^T
C^{-1}
\left(\frac{\partial\boldsymbol\mu}{\partial\theta_b}\right). \tag{99.8}
$$

Equation (99.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. Rank deficiency signals parameter combinations that the selected observables cannot distinguish.

### 99.9 Null and relational hypotheses

A test requires mutually inspectable models,

$$
H_0=(\mathfrak T_0,\Theta_0),
\qquad
H_1=(\mathfrak T_{\mathrm{rel}},\Theta_{\mathrm{rel}}). \tag{99.9}
$$

Equation (99.9) is EXTERNAL_ESTABLISHED_MATHEMATICS as a comparison schema. Neither hypothesis may be left elastic enough to reproduce arbitrary outcomes.

### 99.10 Likelihood-ratio statistic

One frequentist discriminator is

$$
\Lambda=2\left[
\ln\mathcal L(\widehat\theta_1\mid H_1)
-\ln\mathcal L(\widehat\theta_0\mid H_0)
\right]. \tag{99.10}
$$

Equation (99.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. Its reference distribution depends on nesting, regularity, boundary parameters, and the sampling design.

### 99.11 Bayesian evidence

Model evidence and its ratio are

$$
Z_i=\int\mathcal L(\mathbf d\mid\theta_i,H_i)
\pi(\theta_i\mid H_i)d\theta_i,
\qquad
B_{10}=\frac{Z_1}{Z_0}. \tag{99.11}
$$

Equation (99.11) is EXTERNAL_ESTABLISHED_MATHEMATICS. Prior dependence and parameter volume must be reported rather than suppressed.

### 99.12 Out-of-sample prediction

Training and validation data remain separate,

$$
\widehat\theta=\arg\max_\theta p(D_{\mathrm{train}}\mid\theta),
\qquad
S_{\mathrm{test}}=-\ln p(D_{\mathrm{test}}\mid\widehat\theta). \tag{99.12}
$$

Equation (99.12) is EXTERNAL_ESTABLISHED_MATHEMATICS. A model that is revised after seeing its test set has not passed an independent prediction test.

### 99.13 Cross-domain constraint

One relational parameterization must lie in the common acceptable region,

$$
\Theta_{\mathrm{joint}}=
\Theta_{\mathrm{rotation}}
\cap\Theta_{\mathrm{lensing}}
\cap\Theta_{\mathrm{growth}}
\cap\Theta_{\mathrm{background}}. \tag{99.13}
$$

Equation (99.13) is EXTERNAL_ESTABLISHED_MATHEMATICS as a consistency requirement. Channel-specific retuning weakens claims of a unified consequence.

### 99.14 Preregistered decision rule

A clean test fixes its statistic and threshold in advance,

$$
\mathcal R(D)=
\begin{cases}
\mathrm{REJECT}\ H_1,&S(D)>S_\star,\\
\mathrm{RETAIN\ FOR\ FURTHER\ TEST},&S(D)\le S_\star.
\end{cases} \tag{99.14}
$$

Equation (99.14) is EXTERNAL_ESTABLISHED_MATHEMATICS as a decision schema. The actual direction of the inequality depends on the registered statistic.

### 99.15 Replication criterion

Independent validation can be represented by

$$
\operatorname{sign}(\widehat\Delta_1)=
\operatorname{sign}(\widehat\Delta_2),
\qquad
|\widehat\Delta_1-\widehat\Delta_2|
\le z_\alpha\sqrt{\sigma_1^2+\sigma_2^2}. \tag{99.15}
$$

Equation (99.15) is EXTERNAL_ESTABLISHED_MATHEMATICS as a simple compatibility test. Replication must use independent data, preserved analysis rules, and documented provenance.

### 99.16 Native formalization boundary

The missing end-to-end native construction is

$$
\mathrm{API/QMO\ Address}
\longrightarrow
(\mathcal X,F,\Theta,\mathcal B)
\longrightarrow
\mathcal O
\longrightarrow
p(D\mid\theta,H)
\longrightarrow
\mathcal R(D). \tag{99.16}
$$

Equation (99.16) is EVIDENCE_BOUNDARY. V12-C06 has no assigned Library 4.1 handle or evidence record establishing the typed chain.

### 99.17 Typed chapter contract

The formalization ledger is

$$
\mathfrak M_{99}=(\mathfrak T,\mathcal W,\mathcal U,
\mathcal I,\mathcal H,\mathcal Q,\mathcal R,\Omega_{99}). \tag{99.17}
$$

Equation (99.17) is DETERMINISTIC_TYPE_NORMALIZATION. Theory, well-posedness, units, identifiability, hypotheses, quantitative tests, decision rule, and open obligations remain separate.

### 99.18 Coverage calibration

The native Runtime to BRANE to API/QMO query returned

$$
N_{\mathrm{assigned}}=0,
\quad N_{\mathrm{English}}=0,
\quad N_{\mathrm{equation}}=0,
\quad N_{\mathrm{dependency}}=0. \tag{99.18}
$$

Equation (99.18) is DETERMINISTIC_COVERAGE_EVIDENCE. The chapter ledger intentionally assigns no canonical Library 4.1 handle to V12-C06.

### 99.19 API evidence register

The assigned-handle register is empty. No native state space, dynamics, test statistic, proof, or experiment is imported from neighboring addresses. The formal mathematics above is explicitly external and establishes evaluation criteria, not MK-43 Ultra results.

### 99.20 Evidence boundary

The controlling distinction is

$$
\mathrm{FormalScaffold}\ne\mathrm{RecoveredTheory},
\qquad
\mathrm{PossibleTest}\ne\mathrm{ExecutedValidation}. \tag{99.19}
$$

Equation (99.19) is EVIDENCE_BOUNDARY. A rigorous theory report must preserve this separation even when a proposed structure is conceptually compelling.

### 99.21 Open formalization obligations

The unresolved work is

$$
\begin{aligned}
\Omega_{99}=\{&\mathrm{CanonicalNativeAddress},\mathrm{StateSpace},
\mathrm{VariableTypes},\mathrm{Units},\mathrm{Dynamics},\\
&\mathrm{BoundaryData},\mathrm{GaugeAndSymmetry},\mathrm{WellPosedness},
\mathrm{ConservationProof},\\
&\mathrm{ObservationMap},\mathrm{ParameterIdentification},
\mathrm{RegisteredNull},\mathrm{DecisionRule},\\
&\mathrm{IndependentDataset},\mathrm{Replication},
\mathrm{ExternalExperimentalValidation}\}.
\end{aligned} \tag{99.20}
$$

Equation (99.20) is CURATOR_SYNTHESIS. It is a development and validation ledger, not a claim that these requirements have been satisfied.

### 99.22 Chapter determination

The chapter result is

$$
\begin{aligned}
\mathrm{Formalization}_{99}={}&
\mathrm{ESTABLISHED\_TESTING\_SCAFFOLD}
+\mathrm{ZERO\_ASSIGNED\_NATIVE\_HANDLES}\\
&+\mathrm{EXPLICIT\_END\_TO\_END\_CONTRACT}
+\mathrm{OPEN\_MATHEMATICAL\_AND\_EMPIRICAL\_VALIDATION}.
\end{aligned} \tag{99.21}
$$

Equation (99.21) is DETERMINISTIC_STATUS_NORMALIZATION. V12-C06 closes Volume XII at a disciplined boundary: relational dark structure remains a program requiring typed equations, discriminating predictions, and independent tests rather than a validated physical result.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
