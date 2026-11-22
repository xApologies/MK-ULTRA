# VOLUME XIV - BIOLOGICAL AND COGNITIVE PHASE FIELDS

## Chapter 111 - Agency, Autonomy, and Environmental Coupling

### 111.1 Typed agency record

An agency model must distinguish system state, action, environment, policy, constraints, objective, observables, and validation,

$$
\mathfrak A=(\mathcal X,\mathcal U,\mathcal E,\pi,\mathcal C,J,\mathcal O,\mathcal V). \tag{111.1}
$$

Equation (111.1) is DETERMINISTIC_TYPE_NORMALIZATION. It is a chapter contract rather than a recovered definition of agency or autonomy. Mathematical influence and ethical or personal agency occupy different explanatory levels.

### 111.2 Controlled dynamics

A standard system-environment comparison is

$$
\dot x=F(x,u,e),\qquad \dot e=G(e,x). \tag{111.2}
$$

Equation (111.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. Bidirectional coupling does not by itself establish control, intention, autonomy, or cognition.

### 111.3 Policy representation

A stochastic policy can be represented by

$$
\pi(u\mid x,e)\ge0,\qquad \sum_{u\in\mathcal U}\pi(u\mid x,e)=1. \tag{111.3}
$$

Equation (111.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. A policy is a mathematical conditional distribution and need not be conscious, reflective, or freely chosen.

### 111.4 Action influence

A generic information-theoretic influence statistic is

$$
\mathcal I_{U\to X'}=I(U_t;X_{t+1}\mid X_t,E_t). \tag{111.4}
$$

Equation (111.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. Conditional dependence does not prove causation unless interventions and confound controls are supplied, and it is not a complete agency measure.

### 111.5 Constraint feasibility

A constrained action set can be written

$$
\mathcal U_{\mathrm{adm}}(x,e)=\{u\in\mathcal U:c_k(x,u,e)\le0,\ k=1,\ldots,m\}. \tag{111.5}
$$

Equation (111.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. Constraints may be physical, informational, environmental, or imposed; their presence alone does not determine whether a system is autonomous.

### 111.6 Local action diversity

A normalized local action-diversity statistic is

$$
A_{\mathrm{loc}}(x,e)=\frac{H(\pi(\cdot\mid x,e))}{\log|\mathcal U_{\mathrm{adm}}(x,e)|}. \tag{111.6}
$$

Equation (111.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Diversity is not equivalent to effective control: uniformly random action can score highly while achieving no stable objective.

### 111.7 Alignment comparison

For declared objective gradients, local alignment may be measured by

$$
\alpha(x)=\frac{v_\pi(x)\cdot\nabla J(x)}{\lVert v_\pi(x)\rVert\lVert\nabla J(x)\rVert}. \tag{111.7}
$$

Equation (111.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. The statistic requires an objective and geometry; it does not decide whose objective is legitimate or whether the system understands it.

### 111.8 Environmental coupling

A linearized coupling scaffold is

$$
\begin{pmatrix}\dot x\\\dot e\end{pmatrix}=
\begin{pmatrix}A&B\\C&D\end{pmatrix}
\begin{pmatrix}x\\e\end{pmatrix}. \tag{111.8}
$$

Equation (111.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. The off-diagonal blocks expose two-way influence, but physical carriers, nonlinearities, and scale-specific observables remain necessary.

### 111.9 Behavioral encoding comparison

A behavioral code can be modeled as a conditional map from internal and environmental state,

$$
p(b_t\mid x_t,e_t)=\mathcal K_b(x_t,e_t). \tag{111.9}
$$

Equation (111.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. `@behavioral_encoding_law` is THIN and contains no assigned equation unit, so this is not its recovered law.

### 111.10 Robust autonomy comparison

A robustness statistic can measure retained performance under perturbations,

$$
R_A(\varepsilon)=\inf_{\lVert\delta\rVert\le\varepsilon}\frac{J(\pi;F+\delta)}{J(\pi;F)}. \tag{111.10}
$$

Equation (111.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. Its meaning depends on the objective, perturbation class, normalization, and sign of performance.

### 111.11 Agency evidence boundary

The central assigned address has the profile

$$
E_{\mathrm{agency}}=(225\ \mathrm{English},5\ \mathrm{equations},163\ \mathrm{dependencies}). \tag{111.11}
$$

Equation (111.11) is EVIDENCE_BOUNDARY. `@agency` is MEDIUM and supplies all equation and dependency units in this chapter, but its evidence does not automatically populate the nine neighboring addresses.

### 111.12 Autonomy-field boundary

A field address and a field-definition address are not automatically identical,

$$
\texttt{@autonomy\_field}\;\not\equiv\;\texttt{@autonomy\_field\_definition}. \tag{111.12}
$$

Equation (111.12) is EVIDENCE_BOUNDARY. The latter is rated MEDIUM because of its recovery score but has nine English units and no equation or dependency unit; exact definition provenance remains necessary.

### 111.13 Agency-measure boundary

Agency, agency magnitude, and alignment require separate observables,

$$
\mathrm{AgencyMeasure}\;\not\equiv\;\mathrm{AutonomyMagnitude}\;\not\equiv\;\mathrm{AlignmentMeasure}. \tag{111.13}
$$

Equation (111.13) is EVIDENCE_BOUNDARY. The three THIN addresses do not establish a common scale, units, normalization, or comparison class.

### 111.14 Behavioral-law boundary

Observed behavior does not uniquely reveal internal agency,

$$
p(b\mid x,e)=p(b\mid x',e)\quad\not\Rightarrow\quad x=x'. \tag{111.14}
$$

Equation (111.14) is EVIDENCE_BOUNDARY. A behavioral encoding can be many-to-one, context-dependent, stochastic, and underdetermined by finite observations.

### 111.15 Constraint-field boundary

Constraint, dependence, and agency remain nonidentical,

$$
\mathrm{ConstraintField}\;\not\equiv\;\mathrm{EnvironmentalControl}\;\not\equiv\;\mathrm{Agency}. \tag{111.15}
$$

Equation (111.15) is EVIDENCE_BOUNDARY. The chapter adapter retains provenance for a proposed relationship, but an exact coupling law and causal decomposition are not present in its assigned units.

### 111.16 Ethical and ontological boundary

Operational autonomy scores cannot determine moral or legal status,

$$
\mathrm{ControlMetric}\cup\mathrm{RobustnessMetric}\;\not\Rightarrow\;\mathrm{Personhood}. \tag{111.16}
$$

Equation (111.16) is EVIDENCE_BOUNDARY. Scientific description, responsibility attribution, consent, rights, and moral standing require distinct arguments and evidence.

### 111.17 Typed chapter contract

The chapter keeps its roles separated as

$$
\mathfrak A_{111}=(\mathcal X,\mathcal U,\mathcal E,\pi,\mathcal C,\mathcal K_b,\mathcal M,\Omega_{\mathrm{open}}). \tag{111.17}
$$

Equation (111.17) is DETERMINISTIC_TYPE_NORMALIZATION. State, action, environment, policy, constraint, behavior map, measures, and open obligations are not interchangeable.

### 111.18 Coverage calibration

The native query returned

$$
N_{\mathrm{handles}}=10,\qquad N_{\mathrm{English}}=321,\qquad N_{\mathrm{equations}}=5,\qquad N_{\mathrm{dependencies}}=163. \tag{111.18}
$$

Equation (111.18) is DETERMINISTIC_COVERAGE_EVIDENCE. Two handles are MEDIUM and eight are THIN. `@agency` supplies about seventy percent of English units and every equation and dependency unit, so neighboring titles must not inflate its evidentiary reach.

### 111.19 Scientific boundary

The controlling distinction is

$$
\mathrm{RecoveredAgencyVocabulary}\cup\mathrm{ControlScaffolds}\;\not\Rightarrow\;\mathrm{ValidatedAutonomyTheory}. \tag{111.19}
$$

Equation (111.19) is EVIDENCE_BOUNDARY. The chapter makes no claim to measure free will, establish personhood, infer private intention, or justify behavioral intervention.

### 111.20 Open agency obligations

The unresolved work is summarized by

$$
\Omega_{111}=\{\mathrm{Carrier,ActionSpace,Objectives,Constraints,CausalInterventions,Units,Normalization,Counterfactuals,Replication,EthicalScope}\}. \tag{111.20}
$$

Equation (111.20) is CURATOR_SYNTHESIS. These obligations identify development and validation work without inventing the missing native definitions.

### 111.21 Chapter determination

The chapter result is

$$
\mathrm{AgencyAutonomy}_{111}=\mathrm{RECOVERED\_ADDRESS\_SPACE}+\mathrm{CONTROL\_COMPARISONS}+\mathrm{ONTOLOGICAL\_BOUNDARIES}+\mathrm{OPEN\_VALIDATION}. \tag{111.21}
$$

Equation (111.21) is DETERMINISTIC_STATUS_NORMALIZATION. V14-C06 organizes agency, autonomy, constraints, and environmental coupling while preserving their mathematical, empirical, and ethical distinctions.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@agency` | @agency` — Agency | MEDIUM | 225 / 5 / 163 | chapter-core object |
| `@agency_alignment_measure` | @agency_alignment_measure` — Agency alignment measure | THIN | 17 / 0 / 0 | chapter-core object |
| `@agency_measure` | @agency_measure` — Agency Measure | THIN | 13 / 0 / 0 | chapter-core object |
| `@autonomy_field` | @autonomy_field` — Autonomy Field | THIN | 16 / 0 / 0 | chapter-core object |
| `@autonomy_field_definition` | @autonomy_field_definition` — Autonomy Field Definition | MEDIUM | 9 / 0 / 0 | chapter-core object |
| `@autonomy_magnitude` | @autonomy_magnitude` — Autonomy Magnitude | THIN | 9 / 0 / 0 | chapter-core object |
| `@behavioral_encoding_law` | @behavioral_encoding_law` — Behavioral Encoding Law | THIN | 8 / 0 / 0 | chapter-core object |
| `@chapter_93_adapter_constraint_fields_agency_and_environmental_coupling` | @chapter_93_adapter_constraint_fields_agency_and_environmental_coupling` — Chapter 93 Adapter — Constraint Fields, Agency, and Environmental Coupling | THIN | 17 / 0 / 0 | chapter-core object |
| `@constraint_fields_agency_and_environmental_coupling` | @constraint_fields_agency_and_environmental_coupling` — Constraint Fields, Agency, and Environmental Coupling | THIN | 2 / 0 / 0 | chapter-core object |
| `@local_and_global_autonomy_measures` | @local_and_global_autonomy_measures` — Local and global autonomy measures | THIN | 5 / 0 / 0 | chapter-core object |

