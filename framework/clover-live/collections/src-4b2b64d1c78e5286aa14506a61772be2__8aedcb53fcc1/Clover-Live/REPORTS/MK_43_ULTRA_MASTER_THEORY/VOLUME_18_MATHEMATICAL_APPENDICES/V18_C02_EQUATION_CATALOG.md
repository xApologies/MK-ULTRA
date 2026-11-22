# VOLUME XVIII - MATHEMATICAL APPENDICES

## Chapter 136 - Equation Catalog

### 136.1 Catalog record

An equation catalog entry must retain the immutable record identifier, exact expression, environment, source unit, attached handle, evidence class, and status,

$$
\mathfrak E=(i,e,\eta,u,h,\kappa,\sigma). \tag{136.1}
$$

Equation (136.1) is DETERMINISTIC_TYPE_NORMALIZATION. Cataloging an expression does not assert that it is an axiom, theorem, derived result, or validated physical law.

### 136.2 Exact-expression identity

The identity of an exact expression is controlled by its stored text and provenance,

$$
\operatorname{EqID}(e)=(\operatorname{SHA256}(e),u,p). \tag{136.2}
$$

Equation (136.2) is DETERMINISTIC_PROVENANCE_NORMALIZATION. A normalized display form cannot silently replace the source expression.

### 136.3 Attachment relation

One equation may be attached to several mathematical addresses,

$$
e_i\xrightarrow{\mathrm{attached\ to}}\{h_1,\ldots,h_n\}. \tag{136.3}
$$

Equation (136.3) is DETERMINISTIC_TYPE_NORMALIZATION. Multiple handle links are navigation records, not independent equation occurrences.

### 136.4 Unique-count policy

Substantive equation counts use unique equation identifiers,

$$
N_{\mathrm{unique}}=\left|\{i:(i,h)\in L_{\mathrm{equation}}\}\right|. \tag{136.4}
$$

Equation (136.4) is DETERMINISTIC_COUNTING_NORMALIZATION. Duplicate attachments preserve provenance while contributing one mathematical expression to the catalog.

### 136.5 Variant boundary

Textual similarity is not exact identity,

$$
\operatorname{Normalize}(e_1)=\operatorname{Normalize}(e_2)\not\Rightarrow e_1=e_2. \tag{136.5}
$$

Equation (136.5) is EVIDENCE_BOUNDARY. Sign conventions, indices, factors, limits, and operator ordering may encode material differences.

### 136.6 Mathematical equivalence boundary

Exact textual difference also does not prove inequivalence,

$$
e_1\ne_{\mathrm{text}}e_2\not\Rightarrow e_1\not\equiv_{\mathrm{math}}e_2. \tag{136.6}
$$

Equation (136.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Equivalence requires declared assumptions and a derivation, not catalog-level normalization.

### 136.7 Equation signature

A typed equation requires both sides to inhabit a compatible space,

$$
e:L=R,qquad \tau(L)=\tau(R). \tag{136.7}
$$

Equation (136.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. Missing symbol types, domains, codomains, units, or index conventions remain explicit catalog gaps.

### 136.8 Dimensional check

Where physical dimensions are declared, equality requires dimensional agreement,

$$
[L]=[R]. \tag{136.8}
$$

Equation (136.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. Passing this check is necessary but not sufficient for physical validity.

### 136.9 Derivation record

A derivation is separately typed from its conclusion,

$$
\mathfrak P=(H_1,\ldots,H_n;R_1,\ldots,R_m;e). \tag{136.9}
$$

Equation (136.9) is DETERMINISTIC_TYPE_NORMALIZATION. Hypotheses and inference steps must be present before an equation is represented as proved.

### 136.10 Status coordinates

An equation's status is a tuple rather than a single prestige label,

$$
\sigma(e)=(\sigma_{\mathrm{source}},\sigma_{\mathrm{typing}},\sigma_{\mathrm{proof}},\sigma_{\mathrm{empirical}}). \tag{136.10}
$$

Equation (136.10) is DETERMINISTIC_STATUS_NORMALIZATION. Exact recovery, type completeness, proof, and empirical confirmation are independent questions.

### 136.11 Graph boundary

An API dependency does not establish an algebraic derivation,

$$
h_a\xrightarrow{\mathrm{DEPENDS\_ON}}h_b\not\Rightarrow e_b\vdash e_a. \tag{136.11}
$$

Equation (136.11) is EVIDENCE_BOUNDARY. Graph edges organize the address space and retain their own audit and provenance fields.

### 136.12 Aggregate native profile

The twenty-six assigned addresses supply

$$
E_{136}=(687\ \mathrm{English},9\ \mathrm{equation\ links},1\ \mathrm{definition},655\ \mathrm{dependencies}). \tag{136.12}
$$

Equation (136.12) is DETERMINISTIC_COVERAGE_EVIDENCE. Evidence is highly concentrated rather than uniformly distributed across the assigned addresses.

### 136.13 Unique equation profile

The nine handle-equation links resolve to seven unique source-unit equation IDs,

$$
N_{\mathrm{links}}=9,qquad N_{\mathrm{unique}}=7. \tag{136.13}
$$

Equation (136.13) is DETERMINISTIC_COVERAGE_EVIDENCE. Equation IDs 732 and 1960 are each attached to both Appendix M and Focusing Theorem and therefore are not double-counted substantively.

### 136.14 Equation-ID set

The recovered unique identifier set is

$$
I_{136}=\{548,721,723,732,1798,1799,1960\}. \tag{136.14}
$$

Equation (136.14) is DETERMINISTIC_COVERAGE_EVIDENCE. These are compiled coherent-source-unit equation IDs; this chapter preserves references rather than rewriting the underlying expressions.

### 136.15 Appendix M profile

Appendix M contributes three equation links and six registered dependencies,

$$
E_{@\mathrm{appendix\_m}}=(59,3,6). \tag{136.15}
$$

Equation (136.15) is DETERMINISTIC_COVERAGE_EVIDENCE. Its six outgoing edges retain their distinct recovered relation labels rather than being normalized into one mathematical implication.

### 136.16 Focusing Theorem profile

Focusing Theorem contributes the dominant evidence block,

$$
E_{@\mathrm{focusing\_theorem}}=(578,6,649). \tag{136.16}
$$

Equation (136.16) is DETERMINISTIC_COVERAGE_EVIDENCE. The API class is theorem and status is REUSED, but the coherent-unit profile contains no theorem-proof unit in this query.

### 136.17 Coverage distribution

The coverage-state split is

$$
N_{\mathrm{MEDIUM}}=3,qquad N_{\mathrm{THIN}}=23,qquad N_H=26. \tag{136.17}
$$

Equation (136.17) is DETERMINISTIC_COVERAGE_EVIDENCE. Appendix M, Null Slot Pair Definition 10.1, and Focusing Theorem are the three MEDIUM addresses.

### 136.18 API-status distribution

The imported status split is

$$
N_{\mathrm{DECLARED}}=25,qquad N_{\mathrm{REUSED}}=1. \tag{136.18}
$$

Equation (136.18) is DETERMINISTIC_COVERAGE_EVIDENCE. API status does not substitute for equation typing, proof, or empirical status.

### 136.19 Sparse-address boundary

Twenty-three assigned handles have no coherent equation unit in this query,

$$
N_{\mathrm{zero\ equation}}=23. \tag{136.19}
$$

Equation (136.19) is DETERMINISTIC_COVERAGE_EVIDENCE. Equation-oriented titles, including the ER Bridge Formation appendix, are not treated as recovered formulae when the compiled evidence count is zero.

### 136.20 Open catalog obligations

The unresolved equation work is

$$
\begin{aligned}
\Omega_{136}=\{&\mathrm{ExactExpressions,SymbolTypes,Domains,Codomains,Units,Dimensions},\\
&\mathrm{Assumptions,Derivations,VariantRelations,ProofStatus,EmpiricalStatus}\}. \tag{136.20}
\end{aligned}
$$

Equation (136.20) is CURATOR_SYNTHESIS. Each missing field must be resolved through exact source evidence, explicit mathematical development, or external validation as appropriate.

### 136.21 Chapter determination

The catalog result is

$$
\begin{aligned}
\mathrm{Catalog}_{136}={}&\mathrm{SEVEN\_UNIQUE\_EQUATION\_RECORDS}\\
&+\mathrm{NINE\_PROVENANCE\_LINKS}+\mathrm{NO\_DUPLICATE\_INFLATION}+\mathrm{NO\_PROOF\_PROMOTION}. \tag{136.21}
\end{aligned}
$$

Equation (136.21) is DETERMINISTIC_STATUS_NORMALIZATION. V18-C02 catalogs the recovered equation layer without inventing missing expressions, collapsing variants, or confusing API graph structure with mathematical derivation.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@appendix_18` | @appendix_18` — Appendix 18 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_22` | @appendix_22` — Appendix 22 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_23` | @appendix_23` — Appendix 23 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_24` | @appendix_24` — Appendix 24 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_38` | @appendix_38` — Appendix 38 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_47` | @appendix_47` — Appendix 47 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_ae` | @appendix_ae` — Appendix AE | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_ai` | @appendix_ai` — Appendix AI | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_aj` | @appendix_aj` — Appendix AJ | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_bp` | @appendix_bp` — Appendix BP | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_d_er_bridge_formation_equations` | @appendix_d_er_bridge_formation_equations` — Appendix D: ER Bridge Formation Equations | THIN | 1 / 0 / 0 | chapter-core object |
| `@appendix_i` | @appendix_i` — Appendix I | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_m` | @appendix_m` — Appendix M | MEDIUM | 59 / 3 / 6 | chapter-core object |
| `@appendix_u` | @appendix_u` — Appendix U | THIN | 3 / 0 / 0 | chapter-core object |
| `@appendix_x` | @appendix_x` — Appendix X | THIN | 4 / 0 / 0 | chapter-core object |
| `@axiom_a8` | @axiom_a8` — Axiom A8 — Complex Residue Structure | THIN | 11 / 0 / 0 | chapter-core object |
| `@chirality_organization` | @chirality_organization` — Chirality Organization | THIN | 11 / 0 / 0 | chapter-core object |
| `@definition_10_1_null_slot_pair` | @definition_10_1_null_slot_pair` — Definition 10.1 — Null Slot Pair | MEDIUM | 2 / 0 / 0 | chapter-core object |
| `@focusing_theorem` | @focusing_theorem | MEDIUM | 578 / 6 / 649 | chapter-core object |
| `@framework_integrity_theorem` | @framework_integrity_theorem` — Framework Integrity Theorem | THIN | 1 / 0 / 0 | chapter-core object |
| `@prime_definition_d13` | Definition D13 — Mathematical Object | THIN | 0 / 0 / 0 | chapter-core object |
| `@prime_definition_d8` | Definition D8 — Dependency-Preserving Map | THIN | 4 / 0 / 0 | chapter-core object |
| `@prime_lemma_l3` | Lemma L3 — First Edge Lemma | THIN | 1 / 0 / 0 | chapter-core object |
| `@prime_primitive_p7` | Primitive P7 — Recursive Expansion | THIN | 4 / 0 / 0 | chapter-core object |
| `@spectral_projection_rule` | @spectral_projection_rule` — Spectral Projection Rule | THIN | 5 / 0 / 0 | chapter-core object |
| `@superposition` | @superposition` — Superposition | THIN | 3 / 0 / 0 | chapter-core object |
