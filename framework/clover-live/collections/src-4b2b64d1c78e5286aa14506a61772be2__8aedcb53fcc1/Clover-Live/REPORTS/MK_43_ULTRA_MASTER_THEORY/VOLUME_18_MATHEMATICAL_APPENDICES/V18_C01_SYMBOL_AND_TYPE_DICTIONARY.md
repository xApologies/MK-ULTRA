# VOLUME XVIII - MATHEMATICAL APPENDICES

## Chapter 135 - Symbol and Type Dictionary

### 135.1 Dictionary entry

A mathematical dictionary entry must separate the API identity, displayed symbol, type, domain, codomain, scope, status, and provenance,

$$
\mathfrak S=(h,u,s,\tau,D,C,\Omega,\sigma,p). \tag{135.1}
$$

Equation (135.1) is DETERMINISTIC_TYPE_NORMALIZATION. A familiar glyph is not a complete definition because its namespace, scope, and type determine how it may be used.

### 135.2 Handle identity

Canonical identity is controlled by the handle and URI pair,

$$
\operatorname{ID}(x)=(h_x,u_x). \tag{135.2}
$$

Equation (135.2) is DETERMINISTIC_API_NORMALIZATION. Titles and local symbols may vary, while the exact address pair prevents distinct records from being merged accidentally.

### 135.3 Symbol assignment

A symbol assignment is a scoped map,

$$
\alpha_{\Omega}:h\longmapsto(s,\tau). \tag{135.3}
$$

Equation (135.3) is DETERMINISTIC_TYPE_NORMALIZATION. The same glyph may be reused in another source or formal system only if its scope remains explicit.

### 135.4 Typed maps

Every operator or construction requires a signature,

$$
f:D_f\longrightarrow C_f. \tag{135.4}
$$

Equation (135.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. Without domain and codomain, composition, equality, inversion, and dimensional checks remain underdetermined.

### 135.5 Composition rule

Two maps compose only when their intermediate types agree,

$$
f:A\to B,quad g:B\to C\quad\Rightarrow\quad g\circ f:A\to C. \tag{135.5}
$$

Equation (135.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. A graph path does not supply this mathematical compatibility by itself.

### 135.6 Equality boundary

Symbol equality requires compatible type and scope,

$$
x=y\quad\Rightarrow\quad \tau(x)=\tau(y)\ \land\ \Omega(x)=\Omega(y). \tag{135.6}
$$

Equation (135.6) is DETERMINISTIC_TYPE_NORMALIZATION. Matching labels or suffixes are insufficient evidence of identity.

### 135.7 Alias boundary

An alias resolves to an address without creating a new object,

$$
a\xrightarrow{\mathrm{alias}}h,\qquad \operatorname{ID}(a)=\operatorname{ID}(h). \tag{135.7}
$$

Equation (135.7) is DETERMINISTIC_API_NORMALIZATION. No undeclared alias is introduced by this chapter.

### 135.8 Overload record

An overloaded glyph requires an explicit branch by scope,

$$
s\mapsto\{(h_1,\tau_1,\Omega_1),\ldots,(h_n,\tau_n,\Omega_n)\}. \tag{135.8}
$$

Equation (135.8) is DETERMINISTIC_TYPE_NORMALIZATION. Overload is preserved rather than normalized into a false universal meaning.

### 135.9 Primitive P3 collision

The API resolves two distinct P3-labeled records,

$$
\operatorname{ID}(@\mathrm{primitive\_p3})\ne\operatorname{ID}(@\mathrm{prime\_primitive\_p3}). \tag{135.9}
$$

Equation (135.9) is DETERMINISTIC_API_EVIDENCE. The first is titled Inherited State Bundle and the second Boundary Reflection; no equivalence edge is recovered.

### 135.10 Lemma L7 collision

The L7 labels are also namespace-distinct,

$$
\operatorname{ID}(@\mathrm{lemma\_l7})\ne\operatorname{ID}(@\mathrm{prime\_lemma\_l7}). \tag{135.10}
$$

Equation (135.10) is DETERMINISTIC_API_EVIDENCE. Residue Invariance and Quotient Identification remain separate lemma titles, and neither is promoted to a proved theorem by its name.

### 135.11 Equation-record type

An equation reference should retain expression, environment, evidence class, source unit, and status,

$$
\mathfrak E=(e,\eta,\kappa,u_s,\sigma_e). \tag{135.11}
$$

Equation (135.11) is DETERMINISTIC_TYPE_NORMALIZATION. Equation presence and proof status are distinct fields.

### 135.12 Definition-record type

A definition record requires term, defining text, scope, source, and status,

$$
\mathfrak F=(t,d,\Omega,u_s,\sigma_d). \tag{135.12}
$$

Equation (135.12) is DETERMINISTIC_TYPE_NORMALIZATION. The address `@definition_2_3_er_network` has one coherent definition unit, but this chapter does not replace that exact source with a new definition.

### 135.13 Theorem-record boundary

A theorem title does not itself supply hypotheses, conclusion, or proof,

$$
\operatorname{Title}(T)\not\Rightarrow(H_T,C_T,\pi_T). \tag{135.13}
$$

Equation (135.13) is EVIDENCE_BOUNDARY. Area Theorem and Penrose Singularity Theorem records retain equation and dependency metadata without an inferred proof record.

### 135.14 Status lattice

Evidence state and API declaration state are orthogonal coordinates,

$$
\sigma(x)=(\sigma_{\mathrm{API}}(x),\sigma_{\mathrm{coverage}}(x),\sigma_{\mathrm{proof}}(x)). \tag{135.14}
$$

Equation (135.14) is DETERMINISTIC_STATUS_NORMALIZATION. DECLARED, REUSED, THIN, MEDIUM, and NOT_PROVED answer different questions.

### 135.15 Graph-edge record

A dependency entry must retain source, relation type, target, audit status, and provenance,

$$
\mathfrak G=(h_s,r,h_t,\sigma_r,p_r). \tag{135.15}
$$

Equation (135.15) is DETERMINISTIC_API_NORMALIZATION. Graph relations organize navigation and do not become mathematical proofs through repetition.

### 135.16 Aggregate native profile

The eighteen assigned addresses supply

$$
E_{135}=(1086\ \mathrm{English},10\ \mathrm{equations},1\ \mathrm{definition},887\ \mathrm{dependencies}). \tag{135.16}
$$

Equation (135.16) is DETERMINISTIC_COVERAGE_EVIDENCE. Most content is concentrated in the two established-theorem addresses rather than distributed evenly across the dictionary set.

### 135.17 Coverage profile

The coverage states are

$$
N_{\mathrm{MEDIUM}}=3,qquad N_{\mathrm{THIN}}=15,qquad N_H=18. \tag{135.17}
$$

Equation (135.17) is DETERMINISTIC_COVERAGE_EVIDENCE. The medium records are Area Theorem, ER Network Definition 2.3, and Penrose Singularity Theorem.

### 135.18 API-status profile

The imported status split is

$$
N_{\mathrm{DECLARED}}=17,qquad N_{\mathrm{REUSED}}=1. \tag{135.18}
$$

Equation (135.18) is DETERMINISTIC_COVERAGE_EVIDENCE. Penrose Singularity Theorem is the single REUSED address in this chapter assignment.

### 135.19 Sparse appendix profile

The eight generic appendix handles contribute only two English units and no equations or dependencies,

$$
E_{\mathrm{appendix}}=(2,0,0). \tag{135.19}
$$

Equation (135.19) is DETERMINISTIC_COVERAGE_EVIDENCE. Their labels remain addressable placeholders, not reconstructed appendix contents.

### 135.20 Open typing obligations

The unresolved dictionary work is

$$
\begin{aligned}
\Omega_{135}=\{&\mathrm{ExactSymbolTables,Domains,Codomains,Units,Dimensions,Scopes},\\
&\mathrm{AliasDeclarations,OverloadRules,EquationTyping,ProofTyping,VersionLinks}\}. \tag{135.20}
\end{aligned}
$$

Equation (135.20) is CURATOR_SYNTHESIS. These fields must be filled from exact sources or explicit rulings, never from lexical resemblance alone.

### 135.21 Chapter determination

The appendix result is

$$
\begin{aligned}
\mathrm{Dictionary}_{135}={}&\mathrm{EIGHTEEN\_ADDRESSED\_RECORDS}\\
&+\mathrm{SCOPED\_SYMBOL\_TYPES}+\mathrm{COLLISIONS\_PRESERVED}+\mathrm{NO\_SILENT\_IDENTITY}. \tag{135.21}
\end{aligned}
$$

Equation (135.21) is DETERMINISTIC_STATUS_NORMALIZATION. V18-C01 establishes the type discipline required to read subsequent mathematical appendices without collapsing handles, glyphs, titles, graph relations, or proof states.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@appendix_16` | @appendix_16` — Appendix 16 | THIN | 2 / 0 / 0 | chapter-core object |
| `@appendix_20` | @appendix_20` — Appendix 20 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_50` | @appendix_50` — Appendix 50 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_51` | @appendix_51` — Appendix 51 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_aa` | @appendix_aa` — Appendix AA | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_ak` | @appendix_ak` — Appendix AK | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_bm` | @appendix_bm` — Appendix BM | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_bw` | @appendix_bw` — Appendix BW | THIN | 0 / 0 / 0 | chapter-core object |
| `@area_theorem` | @area_theorem | MEDIUM | 51 / 4 / 152 | chapter-core object |
| `@definition_2_3_er_network` | @definition_2_3_er_network` — Definition 2.3 — ER Network | MEDIUM | 2 / 0 / 0 | chapter-core object |
| `@lattice_calculus_appendix_a` | @lattice_calculus_appendix_a` — Lattice Calculus (Appendix A) | THIN | 1 / 0 / 0 | chapter-core object |
| `@lemma_l7` | @lemma_l7` — Lemma L7 — Residue Invariance | THIN | 6 / 0 / 0 | chapter-core object |
| `@lemma_l8` | @lemma_l8` — Lemma L8 — Complexification | THIN | 6 / 0 / 0 | chapter-core object |
| `@penrose_singularity_theorem` | @penrose_singularity_theorem | MEDIUM | 1002 / 6 / 735 | chapter-core object |
| `@prime_lemma_l6` | Lemma L6 — Branch Generation Lemma | THIN | 2 / 0 / 0 | chapter-core object |
| `@prime_lemma_l7` | Lemma L7 — Quotient Identification Lemma | THIN | 2 / 0 / 0 | chapter-core object |
| `@prime_primitive_p3` | Primitive P3 — Boundary Reflection | THIN | 4 / 0 / 0 | chapter-core object |
| `@primitive_p3` | @primitive_p3` — Primitive P3 — Inherited State Bundle | THIN | 8 / 0 / 0 | chapter-core object |
