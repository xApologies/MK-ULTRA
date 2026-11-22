# VOLUME XVIII - MATHEMATICAL APPENDICES

## Chapter 146 - Provenance, Status, and Citation Ledgers

### 146.1 Provenance record

Every substantive claim must preserve record identity, claim class, source identity, exact locator, content hash, ancestry, status, and recovery pass,

$$
\mathfrak P=(r,c,s,\ell,h,a,\sigma,\rho). \tag{146.1}
$$

Equation (146.1) is DETERMINISTIC_TYPE_NORMALIZATION. Provenance is a typed chain, not a filename or an unqualified citation count.

### 146.2 Content identity

Exact content identity is established by a cryptographic digest,

$$
h=\operatorname{SHA256}(b). \tag{146.2}
$$

Equation (146.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. Equal hashes support byte identity under the stated algorithm; they do not establish semantic equivalence of different bytes.

### 146.3 Occurrence-to-content map

Physical occurrences map many-to-one onto unique content records,

$$
\pi_{\mathrm{content}}:\mathcal O\longrightarrow\mathcal U. \tag{146.3}
$$

Equation (146.3) is DETERMINISTIC_TYPE_NORMALIZATION. Every occurrence retains its path and ancestry while duplicate content counts once substantively.

### 146.4 Citation record

A resolvable citation records source, locator, quoted or attached content hash, claim, and evidence class,

$$
\mathfrak C=(s,\ell,h,c,e). \tag{146.4}
$$

Equation (146.4) is DETERMINISTIC_TYPE_NORMALIZATION. A citation is incomplete when its immutable source location cannot be reopened.

### 146.5 Status partial order

Evidence status must not be upgraded merely by repetition,

$$
\mathrm{candidate}\not\Rightarrow\mathrm{proved},\qquad \mathrm{declared}\not\Rightarrow\mathrm{complete}. \tag{146.5}
$$

Equation (146.5) is DETERMINISTIC_STATUS_NORMALIZATION. Promotion requires the explicit review and proof conditions attached to the target status.

### 146.6 Evidence-class separation

The principal evidence classes remain disjoint at the record level,

$$
\mathcal E=\mathcal E_{\mathrm{exact}}\sqcup\mathcal E_{\mathrm{API}}\sqcup\mathcal E_{\mathrm{normalized}}\sqcup\mathcal E_{\mathrm{curator}}\sqcup\mathcal E_{\mathrm{unresolved}}. \tag{146.6}
$$

Equation (146.6) is CURATOR_SYNTHESIS. A record may have links across classes, but its own class cannot change silently.

### 146.7 Revision relation

Append-only revisioning records a parent without overwriting it,

$$
R_{n+1}\xrightarrow{\mathrm{PARENT\_OF}^{-1}}R_n,\qquad R_n\ \text{immutable}. \tag{146.7}
$$

Equation (146.7) is DETERMINISTIC_STATUS_NORMALIZATION. Supersession, when explicit, remains different from deletion.

### 146.8 Conflict record

A conflict preserves both claims, their evidence, scope, and disposition,

$$
\mathfrak K=(c_1,c_2,E_1,E_2,D_1,D_2,\delta,\sigma). \tag{146.8}
$$

Equation (146.8) is DETERMINISTIC_TYPE_NORMALIZATION. Unresolved conflict is a valid recorded state.

### 146.9 Citation integrity predicate

A citation passes only if its source exists, hash matches, locator resolves, and evidence class is retained,

$$
\operatorname{ValidCitation}=P_{\mathrm{exists}}\wedge P_{\mathrm{hash}}\wedge P_{\mathrm{locator}}\wedge P_{\mathrm{class}}. \tag{146.9}
$$

Equation (146.9) is CURATOR_SYNTHESIS. It defines the TOME audit boundary rather than a recovered physical law.

### 146.10 Completeness boundary

Ledger completeness is relative to an enumerated input set,

$$
\operatorname{Complete}(L\mid I)\Longleftrightarrow \forall i\in I\;\exists\,r_i\in L. \tag{146.10}
$$

Equation (146.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. It does not imply that the underlying theory is mathematically or experimentally complete.

### 146.11 Native evidence profile

The twenty-four assigned API addresses collectively contribute

$$
E_{\mathrm{native}}=(284\ \mathrm{English},6\ \mathrm{equations},2\ \mathrm{definitions},0\ \mathrm{theorem/proof},185\ \mathrm{dependencies}). \tag{146.11}
$$

Equation (146.11) is DETERMINISTIC_COVERAGE_EVIDENCE. Coverage density remains distinct from evidence authority.

### 146.12 Coverage distribution

The coverage split is

$$
N_{\mathrm{THIN}}=22,\qquad N_{\mathrm{MEDIUM}}=2,\qquad N_{\mathrm{total}}=24. \tag{146.12}
$$

Equation (146.12) is DETERMINISTIC_COVERAGE_EVIDENCE. Admissible Continuation and the Formal Infinity Class are MEDIUM.

### 146.13 Admissible-continuation profile

The dominant address contributes

$$
E_{@\mathrm{admissible\_continuation}}=(224,6,0,0,185). \tag{146.13}
$$

Equation (146.13) is DETERMINISTIC_COVERAGE_EVIDENCE. Its high dependency count does not independently prove admissibility claims.

### 146.14 Equation-provenance register

The six native equations resolve to coherent equation IDs

$$
I_{\mathrm{equation}}=\{721,723,732,1798,1799,2203\}. \tag{146.14}
$$

Equation (146.14) is DETERMINISTIC_PROVENANCE_NORMALIZATION. The IDs preserve exact record resolution without reprinting source mathematics out of context.

### 146.15 Definition profile

The two definition attachments are distributed as

$$
N_{\mathrm{Formal\ Infinity\ Class}}=1,\qquad N_{\mathrm{Configuration\ Functional}}=1. \tag{146.15}
$$

Equation (146.15) is DETERMINISTIC_COVERAGE_EVIDENCE. Definition count alone does not close typing, existence, or uniqueness obligations.

### 146.16 Axiom and schema profile

Spectral Projection Rule and Axiom Schema jointly contribute

$$
E_{\mathrm{axiom/schema}}=(20,0,0,0,0). \tag{146.16}
$$

Equation (146.16) is DETERMINISTIC_COVERAGE_EVIDENCE. Their titles do not create a recovered proof system in this slice.

### 146.17 Supporting-object profile

Hermitian Connection, Structured Temporal Manifold, and Projection Residue Bundle jointly contribute

$$
E_{\mathrm{supporting\ objects}}=(24,0,0,0,0). \tag{146.17}
$$

Equation (146.17) is DETERMINISTIC_COVERAGE_EVIDENCE. Exact relationship claims remain governed by typed API edges and source records.

### 146.18 Zero-substantive boundary

Eleven assigned appendix or prime-axiom addresses carry no substantive units in this queried slice,

$$
N_{\mathrm{zero\text{-}substantive}}=11. \tag{146.18}
$$

Equation (146.18) is DETERMINISTIC_COVERAGE_EVIDENCE. Their addresses remain preserved as navigation and provenance.

### 146.19 API-status profile

All assigned handles are declared,

$$
N_{\mathrm{DECLARED}}=24. \tag{146.19}
$$

Equation (146.19) is DETERMINISTIC_COVERAGE_EVIDENCE. Declaration cannot substitute for review, proof, or Library-readiness status.

### 146.20 Open ledger obligations

The unresolved ledger set is

$$
\Omega_{146}=\{\text{exact locators},\text{status authority},\text{conflict review},\text{proof links},\text{external validation}\}. \tag{146.20}
$$

Equation (146.20) is CURATOR_SYNTHESIS. Each open item must remain visible until its own validation path closes.

### 146.21 TOME determination

The completed chapter ledger satisfies

$$
\begin{aligned}
\mathrm{TOME}_{146}
&=146/146\ \mathrm{CHAPTERS\ COMPOSED\ AND\ SEALED}\\
&\quad+\mathrm{PROVENANCE/STATUS/CITATION\ BOUNDARIES}\\
&\quad+\mathrm{NO\ EVIDENCE\text{-}CLASS\ COLLAPSE}.
\end{aligned} \tag{146.21}
$$

Equation (146.21) is DETERMINISTIC_STATUS_NORMALIZATION. It closes the planned chapter sequence while preserving every object-level uncertainty, conflict, and proof obligation recorded inside the TOME.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@admissible_continuation` | @admissible_continuation` — Admissible Continuation | MEDIUM | 224 / 6 / 185 | chapter-core object |
| `@appendix_11` | @appendix_11` — Appendix 11 | THIN | 8 / 0 / 0 | chapter-core object |
| `@appendix_27` | @appendix_27` — Appendix 27 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_30` | @appendix_30` — Appendix 30 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_35` | @appendix_35` — Appendix 35 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_39` | @appendix_39` — Appendix 39 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_ad` | @appendix_ad` — Appendix AD | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_am` | @appendix_am` — Appendix AM | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_at` | @appendix_at` — Appendix AT | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_au` | @appendix_au` — Appendix AU | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_av` | @appendix_av` — Appendix AV | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_bx` | @appendix_bx` — Appendix BX | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_ca` | @appendix_ca` — Appendix CA | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_t` | @appendix_t` — Appendix T | THIN | 2 / 0 / 0 | chapter-core object |
| `@appendix_z` | @appendix_z` — Appendix Z | THIN | 5 / 0 / 0 | chapter-core object |
| `@axiom_a12` | @axiom_a12` — Axiom A12 — Spectral Projection Rule | THIN | 11 / 0 / 0 | chapter-core object |
| `@axiom_schema` | @axiom_schema` — Axiom schema | THIN | 9 / 0 / 0 | chapter-core object |
| `@definition_15_1_formal_infinity_class` | @definition_15_1_formal_infinity_class` — Definition 15.1 — Formal Infinity Class | MEDIUM | 1 / 0 / 0 | chapter-core object |
| `@definition_18_4_configuration_functional` | @definition_18_4_configuration_functional` — Definition 18.4 — Configuration Functional | THIN | 0 / 0 / 0 | chapter-core object |
| `@hermitian_connection` | @hermitian_connection` — Hermitian Connection | THIN | 9 / 0 / 0 | chapter-core object |
| `@prime_axiom_a4` | Axiom A4 — Oriented Realizability | THIN | 0 / 0 / 0 | chapter-core object |
| `@prime_axiom_a6` | Axiom A6 — Recursive Generativity | THIN | 0 / 0 / 0 | chapter-core object |
| `@primitive_p0` | @primitive_p0` — Primitive P0 — Structured Temporal Manifold | THIN | 9 / 0 / 0 | chapter-core object |
| `@projection_residue_bundle` | @projection_residue_bundle` — Projection Residue Bundle | THIN | 6 / 0 / 0 | chapter-core object |
