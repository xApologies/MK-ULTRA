# VOLUME XVIII - MATHEMATICAL APPENDICES

## Chapter 139 - Lemmas and Propositions

### 139.1 Result record

A lemma or proposition record must preserve its address, statement, hypotheses, conclusion, proof object, scope, status, and provenance,

$$
\mathfrak R=(h,S,H,C,\pi,\Omega,\sigma,p). \tag{139.1}
$$

Equation (139.1) is DETERMINISTIC_TYPE_NORMALIZATION. A named result is not complete unless its exact statement and proof obligations are recoverable.

### 139.2 Lemma role

A lemma is a proved intermediate result within a declared argument,

$$
H_L\vdash_{\pi_L}C_L. \tag{139.2}
$$

Equation (139.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. The label records intended formal role; proof status must still be established independently.

### 139.3 Proposition role

A proposition is a typed assertion with stated hypotheses and conclusion,

$$
P=(H_P\Rightarrow C_P). \tag{139.3}
$$

Equation (139.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. Neither terminology nor placement determines whether a proof has been recovered.

### 139.4 Proof object

A proof object records ordered justified steps,

$$
\pi=(s_0\xrightarrow{r_1}s_1\xrightarrow{r_2}\cdots\xrightarrow{r_n}s_n=C). \tag{139.4}
$$

Equation (139.4) is DETERMINISTIC_TYPE_NORMALIZATION. Source citations and dependency edges do not substitute for the inference rules $r_i$.

### 139.5 Hypothesis closure

A result may be applied only when all hypotheses have been discharged,

$$
\Gamma\vdash H_1,\ldots,H_n\quad\land\quad(H_1\land\cdots\land H_n\Rightarrow C)\quad\Rightarrow\quad\Gamma\vdash C. \tag{139.5}
$$

Equation (139.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. Omitted hypotheses prevent a valid downstream application.

### 139.6 Type preservation

Every inferential step must preserve well-formed types,

$$
\Gamma\vdash s_i:\tau_i\quad\land\quad r_{i+1}:\tau_i\to\tau_{i+1}. \tag{139.6}
$$

Equation (139.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. A visually plausible transition is not a typed derivation.

### 139.7 Dependency boundary

Graph dependency and logical implication remain distinct,

$$
h_a\xrightarrow{\mathrm{DEPENDS\_ON}}h_b\not\Rightarrow S_b\vdash S_a. \tag{139.7}
$$

Equation (139.7) is EVIDENCE_BOUNDARY. Each API edge retains its recovered relation class and audit status.

### 139.8 Corollary boundary

A corollary requires an explicit derivation from an established result,

$$
T\vdash C\quad\Rightarrow\quad C\ \text{may be recorded as a corollary of }T. \tag{139.8}
$$

Equation (139.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. No corollary status is inferred from proximity in a source or graph.

### 139.9 Equivalence boundary

Two propositions are equivalent only under a bidirectional derivation,

$$
P\equiv Q\quad\Rightarrow\quad(P\vdash Q)\land(Q\vdash P). \tag{139.9}
$$

Equation (139.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. Similar terminology is insufficient.

### 139.10 Spectral Measurement Projection address

The assigned lemma address is

$$
h_L=@\mathrm{lemma\_l12}. \tag{139.10}
$$

Equation (139.10) is DETERMINISTIC_API_EVIDENCE. Its title is Lemma L12 - Spectral Measurement Projection, with six English units and no coherent theorem-proof unit.

### 139.11 Hypercoherent proposition boundary

The proposition-titled address has no substantive coherent unit in this query,

$$
E_{@\mathrm{hypercoherent\_propositions}}=(0,0,0). \tag{139.11}
$$

Equation (139.11) is DETERMINISTIC_COVERAGE_EVIDENCE. Its declared title is preserved without invented proposition statements.

### 139.12 Definition and invariants profile

The definition-shaped address contributes

$$
E_{@\mathrm{definition\_and\_basic\_invariants}}=(1,0,1,0). \tag{139.12}
$$

Equation (139.12) is DETERMINISTIC_COVERAGE_EVIDENCE. The tuple records English, equation, definition, and dependency units; it is not reclassified as a lemma.

### 139.13 Persistent Boundary profile

The primitive address contributes

$$
E_{@\mathrm{primitive\_p9}}=(8,0,0). \tag{139.13}
$$

Equation (139.13) is DETERMINISTIC_COVERAGE_EVIDENCE. Primitive P9 - Persistent Boundary remains a primitive address rather than a proposition.

### 139.14 Singularity Theorem profile

The dominant address contributes

$$
E_{@\mathrm{singularity\_theorem}}=(97,4,232). \tag{139.14}
$$

Equation (139.14) is DETERMINISTIC_COVERAGE_EVIDENCE. Four equation units and 232 dependencies do not supply a coherent theorem-proof unit.

### 139.15 Aggregate native profile

The fifteen assigned addresses supply

$$
E_{139}=(118\ \mathrm{English},4\ \mathrm{equations},1\ \mathrm{definition},232\ \mathrm{dependencies}). \tag{139.15}
$$

Equation (139.15) is DETERMINISTIC_COVERAGE_EVIDENCE. Evidence is concentrated in the Singularity Theorem address.

### 139.16 Coverage distribution

The coverage-state split is

$$
N_{\mathrm{MEDIUM}}=2,qquad N_{\mathrm{THIN}}=13,qquad N_H=15. \tag{139.16}
$$

Equation (139.16) is DETERMINISTIC_COVERAGE_EVIDENCE. Definition and Basic Invariants and Singularity Theorem are MEDIUM.

### 139.17 Proof-unit profile

No assigned handle has a coherent theorem-proof unit,

$$
N_{\mathrm{theorem/proof}}=0. \tag{139.17}
$$

Equation (139.17) is DETERMINISTIC_COVERAGE_EVIDENCE. This absence controls the chapter's proof-status language.

### 139.18 API-status distribution

All assigned addresses are declared,

$$
N_{\mathrm{DECLARED}}=15. \tag{139.18}
$$

Equation (139.18) is DETERMINISTIC_COVERAGE_EVIDENCE. Declaration establishes addressability, not theoremhood or proof.

### 139.19 Zero-evidence appendix profile

Seven generic appendix handles have zero English, equation, definition, and dependency units,

$$
N_{\mathrm{zero\ appendix}}=7. \tag{139.19}
$$

Equation (139.19) is DETERMINISTIC_COVERAGE_EVIDENCE. Appendix Q, R, and V retain small textual profiles; none supplies theorem-proof material.

### 139.20 Open result obligations

The unresolved work is

$$
\begin{aligned}
\Omega_{139}=\{&\mathrm{ExactStatements,Hypotheses,Conclusions,Types,InferenceRules},\\
&\mathrm{ProofObjects,Dependencies,Counterexamples,VersionStatus,ExternalValidation}\}. \tag{139.20}
\end{aligned}
$$

Equation (139.20) is CURATOR_SYNTHESIS. These obligations must be met before any assigned lemma or proposition can be treated as proved.

### 139.21 Chapter determination

The appendix result is

$$
\begin{aligned}
\mathrm{Results}_{139}={}&\mathrm{FIFTEEN\_DECLARED\_ADDRESSES}\\
&+\mathrm{LEMMA\_PROPOSITION\_TYPE\_SEPARATION}\\
&+\mathrm{ZERO\_PROOF\_UNITS}+\mathrm{NO\_PROOF\_PROMOTION}. \tag{139.21}
\end{aligned}
$$

Equation (139.21) is DETERMINISTIC_STATUS_NORMALIZATION. V18-C05 preserves each formal-role distinction and exposes the exact proof boundary.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@appendix_19` | @appendix_19` — Appendix 19 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_49` | @appendix_49` — Appendix 49 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_8` | @appendix_8` — Appendix 8 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_ag` | @appendix_ag` — Appendix AG | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_ao` | @appendix_ao` — Appendix AO | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_bn` | @appendix_bn` — Appendix BN | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_bz` | @appendix_bz` — Appendix BZ | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_q` | @appendix_q` — Appendix Q | THIN | 1 / 0 / 0 | chapter-core object |
| `@appendix_r` | @appendix_r` — Appendix R | THIN | 1 / 0 / 0 | chapter-core object |
| `@appendix_v` | @appendix_v` — Appendix V | THIN | 4 / 0 / 0 | chapter-core object |
| `@definition_and_basic_invariants` | @definition_and_basic_invariants` — Definition and Basic Invariants | MEDIUM | 1 / 0 / 0 | chapter-core object |
| `@hypercoherent_propositions` | @hypercoherent_propositions` — Hypercoherent Propositions | THIN | 0 / 0 / 0 | chapter-core object |
| `@lemma_l12` | @lemma_l12` — Lemma L12 — Spectral Measurement Projection | THIN | 6 / 0 / 0 | chapter-core object |
| `@primitive_p9` | @primitive_p9` — Primitive P9 — Persistent Boundary | THIN | 8 / 0 / 0 | chapter-core object |
| `@singularity_theorem` | @singularity_theorem | MEDIUM | 97 / 4 / 232 | chapter-core object |
