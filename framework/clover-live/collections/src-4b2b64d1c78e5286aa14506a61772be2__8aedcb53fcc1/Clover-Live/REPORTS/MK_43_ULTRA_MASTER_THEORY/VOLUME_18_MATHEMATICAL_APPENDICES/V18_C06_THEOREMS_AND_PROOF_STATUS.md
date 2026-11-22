# VOLUME XVIII - MATHEMATICAL APPENDICES

## Chapter 140 - Theorems and Proof Status

### 140.1 Theorem record

A theorem record must preserve the canonical address, exact statement, hypotheses, conclusion, proof, formal system, status, and provenance,

$$
\mathfrak T=(h,S,H,C,\pi,F,\sigma,p). \tag{140.1}
$$

Equation (140.1) is DETERMINISTIC_TYPE_NORMALIZATION. A theorem title is an address-level claim about role, not evidence that all proof fields are populated.

### 140.2 Proof judgment

A proved theorem requires an explicit derivation,

$$
H\vdash_{F,\pi}C. \tag{140.2}
$$

Equation (140.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. The formal system and inference rules must be identified for the judgment to be auditable.

### 140.3 Soundness boundary

Semantic truth follows from syntactic proof only under soundness,

$$
H\vdash_F C\quad\land\quad\operatorname{Sound}(F)\quad\Rightarrow\quad H\models_F C. \tag{140.3}
$$

Equation (140.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. Soundness itself requires justification.

### 140.4 Completeness boundary

Failure to recover a proof is not proof of falsehood,

$$
H\nvdash_F C\not\Rightarrow H\models_F\neg C. \tag{140.4}
$$

Equation (140.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. Missing evidence and refutation remain distinct statuses.

### 140.5 Proof-status coordinates

The status of a theorem-shaped record is multidimensional,

$$
\sigma(T)=(\sigma_{\mathrm{statement}},\sigma_{\mathrm{hypotheses}},\sigma_{\mathrm{typing}},\sigma_{\mathrm{proof}},\sigma_{\mathrm{validation}}). \tag{140.5}
$$

Equation (140.5) is DETERMINISTIC_STATUS_NORMALIZATION. Exact source recovery, mathematical proof, and empirical validation do not collapse into one label.

### 140.6 Candidate boundary

A theorem candidate remains distinct from a proved theorem,

$$
\mathrm{CANDIDATE}(T)\not\Rightarrow\mathrm{PROVED}(T). \tag{140.6}
$$

Equation (140.6) is EVIDENCE_BOUNDARY. Naming elegance or structural convergence cannot complete missing mathematics.

### 140.7 Numerical boundary

Numerical agreement over a finite test set does not constitute a universal proof,

$$
\forall x\in X_N,\ P(x)\quad\not\Rightarrow\quad\forall x\in X,\ P(x). \tag{140.7}
$$

Equation (140.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. Computation may support testing while leaving analytic obligations open.

### 140.8 Graph boundary

A path named Proof Traversal is not itself a proof,

$$
h_0\to h_1\to\cdots\to h_n\not\Rightarrow H\vdash C. \tag{140.8}
$$

Equation (140.8) is EVIDENCE_BOUNDARY. Each transition still requires an inference rule and discharged hypotheses.

### 140.9 Counterexample rule

A universal claim is refuted by one admissible counterexample,

$$
\exists x\in D:\neg P(x)\quad\Rightarrow\quad\neg\forall x\in D:P(x). \tag{140.9}
$$

Equation (140.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. Domain admissibility must be explicit.

### 140.10 Proof Traversal address

The assigned theorem-titled handle is

$$
h_T=@\mathrm{prime\_theorem\_t6}. \tag{140.10}
$$

Equation (140.10) is DETERMINISTIC_API_EVIDENCE. Its API title is Theorem T6 - Proof Traversal Theorem, with four English units and zero theorem-proof units.

### 140.11 Proof-status disposition

The recovered evidence supports

$$
\sigma_{\mathrm{proof}}(h_T)=\mathrm{NOT\_PROVED}. \tag{140.11}
$$

Equation (140.11) is DETERMINISTIC_STATUS_NORMALIZATION. NOT_PROVED records missing proof evidence; it does not assert that the proposed theorem is false.

### 140.12 Definition-address profile

The five definition-titled addresses contribute

$$
E_{\mathrm{definition\ titles}}=(1+4+2+0+4,0,0)=(11,0,0). \tag{140.12}
$$

Equation (140.12) is DETERMINISTIC_COVERAGE_EVIDENCE. None has a coherent definition unit in this query, and none is treated as a theorem.

### 140.13 Numerical appendix profile

The two Appendix 10 addresses each contribute nine English units,

$$
E_{\mathrm{Appendix\ 10}}=(9,0,0)+(9,0,0)=(18,0,0). \tag{140.13}
$$

Equation (140.13) is DETERMINISTIC_COVERAGE_EVIDENCE. Their titles do not establish an implemented or validated numerical scheme.

### 140.14 Geometry appendix profile

The ER-Bridge Topology and Connectivity Measures address contributes

$$
E_{@\mathrm{appendix\_5\_er\_bridge\_topology\_and\_connectivity\_measures}}=(1,0,0). \tag{140.14}
$$

Equation (140.14) is DETERMINISTIC_COVERAGE_EVIDENCE. No topology theorem or proof is reconstructed from the title.

### 140.15 Aggregate native profile

The twenty-three assigned addresses supply

$$
E_{140}=(57\ \mathrm{English},0\ \mathrm{equations},0\ \mathrm{definitions},0\ \mathrm{dependencies}). \tag{140.15}
$$

Equation (140.15) is DETERMINISTIC_COVERAGE_EVIDENCE. The evidence base is entirely sparse textual context.

### 140.16 Coverage distribution

Every assigned handle is THIN,

$$
N_{\mathrm{THIN}}=23,qquad N_{\mathrm{MEDIUM}}=N_{\mathrm{THICK}}=0. \tag{140.16}
$$

Equation (140.16) is DETERMINISTIC_COVERAGE_EVIDENCE. No duplicate raw occurrence increases this substantive rating.

### 140.17 Theorem-proof profile

No coherent theorem-proof unit is present,

$$
N_{\mathrm{theorem/proof}}=0. \tag{140.17}
$$

Equation (140.17) is DETERMINISTIC_COVERAGE_EVIDENCE. This controls every theorem-status determination in the chapter.

### 140.18 Equation profile

No coherent equation unit is present,

$$
N_{\mathrm{equation}}=0. \tag{140.18}
$$

Equation (140.18) is DETERMINISTIC_COVERAGE_EVIDENCE. Proof reconstruction cannot proceed from unnamed equations.

### 140.19 API-status distribution

All assigned records are declared,

$$
N_{\mathrm{DECLARED}}=23. \tag{140.19}
$$

Equation (140.19) is DETERMINISTIC_COVERAGE_EVIDENCE. Addressability is preserved without scientific-status promotion.

### 140.20 Open theorem obligations

The unresolved work is

$$
\begin{aligned}
\Omega_{140}=\{&\mathrm{ExactStatements,Hypotheses,Conclusions,Types,FormalSystems},\\
&\mathrm{InferenceRules,ProofObjects,Counterexamples,NumericalChecks,ExternalValidation}\}. \tag{140.20}
\end{aligned}
$$

Equation (140.20) is CURATOR_SYNTHESIS. These requirements must be met before any theorem-shaped record can receive PROVED status.

### 140.21 Chapter determination

The appendix result is

$$
\begin{aligned}
\mathrm{ProofStatus}_{140}={}&\mathrm{TWENTY\_THREE\_THIN\_DECLARED\_ADDRESSES}\\
&+\mathrm{ZERO\_EQUATION\_AND\_PROOF\_UNITS}\\
&+\mathrm{NOT\_PROVED\_BOUNDARY}+\mathrm{NO\_THEOREM\_PROMOTION}. \tag{140.21}
\end{aligned}
$$

Equation (140.21) is DETERMINISTIC_STATUS_NORMALIZATION. V18-C06 converts sparse theorem vocabulary into an auditable absence finding rather than an invented proof.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@appendix_10` | @appendix_10` — Appendix 10 | THIN | 9 / 0 / 0 | chapter-core object |
| `@appendix_10_numerical_schemes_for_phase_and_er_foam_evolution` | @appendix_10_numerical_schemes_for_phase_and_er_foam_evolution` — Appendix 10: Numerical Schemes for Phase and ER-Foam Evolution | THIN | 9 / 0 / 0 | chapter-core object |
| `@appendix_2` | @appendix_2` — Appendix 2 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_41` | @appendix_41` — Appendix 41 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_52` | @appendix_52` — Appendix 52 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_5_er_bridge_topology_and_connectivity_measures` | @appendix_5_er_bridge_topology_and_connectivity_measures` — Appendix 5: ER-Bridge Topology and Connectivity Measures | THIN | 1 / 0 / 0 | chapter-core object |
| `@appendix_aq` | @appendix_aq` — Appendix AQ | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_ar` | @appendix_ar` — Appendix AR | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_b_discrete_hamiltonian` | @appendix_b_discrete_hamiltonian` — Appendix B: Discrete Hamiltonian | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_bd` | @appendix_bd` — Appendix BD | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_bg` | @appendix_bg` — Appendix BG | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_s` | @appendix_s` — Appendix S | THIN | 2 / 0 / 0 | chapter-core object |
| `@appendix_w` | @appendix_w` — Appendix W | THIN | 4 / 0 / 0 | chapter-core object |
| `@complexification` | @complexification` — Complexification | THIN | 2 / 0 / 0 | chapter-core object |
| `@definition_1` | @definition_1 | THIN | 1 / 0 / 0 | chapter-core object |
| `@prime_definition_d1` | Definition D1 — Structural Cell | THIN | 4 / 0 / 0 | chapter-core object |
| `@prime_definition_d10` | Definition D10 — Dependency Closure | THIN | 2 / 0 / 0 | chapter-core object |
| `@prime_definition_d12` | Definition D12 — Extensional Dependency Region | THIN | 0 / 0 / 0 | chapter-core object |
| `@prime_definition_d4` | Definition D4 — Dependency Edge | THIN | 4 / 0 / 0 | chapter-core object |
| `@prime_theorem_t6` | Theorem T6 — Proof Traversal Theorem | THIN | 4 / 0 / 0 | chapter-core object |
| `@primitive_p17` | @primitive_p17` — Primitive P17 — Observable Algebra | THIN | 8 / 0 / 0 | chapter-core object |
| `@projective_quotient` | @projective_quotient` — Projective Quotient | THIN | 5 / 0 / 0 | chapter-core object |
| `@residue_invariance` | @residue_invariance` — Residue Invariance | THIN | 2 / 0 / 0 | chapter-core object |
