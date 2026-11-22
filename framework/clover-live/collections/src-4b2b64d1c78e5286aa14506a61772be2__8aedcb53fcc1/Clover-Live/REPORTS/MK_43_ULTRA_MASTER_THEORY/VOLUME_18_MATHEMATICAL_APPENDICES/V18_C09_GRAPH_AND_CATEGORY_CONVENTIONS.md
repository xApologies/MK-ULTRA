# VOLUME XVIII - MATHEMATICAL APPENDICES

## Chapter 143 - Graph and Category Conventions

### 143.1 Graph convention record

A graph-level claim must declare vertices, edges, incidence, direction, labels, multiplicity, path convention, typing, status, and provenance,

$$
\mathfrak G_{\mathrm{graph}}=(V,E,s,t,\lambda,m,\mathsf P,\tau,\sigma,p). \tag{143.1}
$$

Equation (143.1) is DETERMINISTIC_TYPE_NORMALIZATION. It prevents a dependency graph, theorem graph, causal graph, and physical network from being silently identified.

### 143.2 Directed graph

A directed multigraph may be represented by

$$
G=(V,E,s,t),\qquad s,t:E\longrightarrow V. \tag{143.2}
$$

Equation (143.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. Whether loops or parallel edges are allowed must be stated.

### 143.3 Directed path

A path of length $n$ is a composable edge sequence

$$
p=(e_1,\ldots,e_n),\qquad t(e_k)=s(e_{k+1})\quad(1\le k<n). \tag{143.3}
$$

Equation (143.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. A listed sequence of handles is not yet a mathematical derivation unless every edge and composition rule is typed.

### 143.4 Induced subgraph

For $W\subseteq V$, the induced subgraph has

$$
G[W]=\bigl(W,\{e\in E:s(e),t(e)\in W\}\bigr). \tag{143.4}
$$

Equation (143.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. A dependency subgraph retains only the edge semantics explicitly selected.

### 143.5 Graph homomorphism

A directed-graph homomorphism is a pair of maps satisfying

$$
f_V\circ s=s'\circ f_E,\qquad f_V\circ t=t'\circ f_E. \tag{143.5}
$$

Equation (143.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. Preservation of labels, weights, or edge types requires additional conditions.

### 143.6 Category convention

A category records objects, morphisms, composition, and identities,

$$
\mathcal C=(\operatorname{Ob}\mathcal C,\operatorname{Hom}_{\mathcal C},\circ,1). \tag{143.6}
$$

Equation (143.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Associativity and identity laws are required, not optional annotations.

### 143.7 Typed composition

For morphisms $f:A\to B$ and $g:B\to C$,

$$
g\circ f:A\longrightarrow C. \tag{143.7}
$$

Equation (143.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. A domain-codomain mismatch makes the displayed composition undefined.

### 143.8 Functor convention

A functor preserves sources, targets, identities, and composition,

$$
F(g\circ f)=F(g)\circ F(f),\qquad F(1_A)=1_{F(A)}. \tag{143.8}
$$

Equation (143.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. A correspondence between address spaces is not a functor until these obligations are met.

### 143.9 Natural transformation

For functors $F,G$ from category C to category D, a natural transformation $\eta:F\Rightarrow G$ obeys

$$
G(f)\circ\eta_A=\eta_B\circ F(f)\qquad(f:A\to B). \tag{143.9}
$$

Equation (143.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. Naturality is a commuting condition, not merely similarity of diagrams.

### 143.10 API graph relation

The queried theorem-graph neighborhood exposes the typed relation pattern

$$
@\mathrm{theorem\_graph}\xrightarrow{\mathrm{GENERALIZES}}x,
\qquad y\xrightarrow{\mathrm{SPECIALIZES\_AS}}@\mathrm{theorem\_graph}. \tag{143.10}
$$

Equation (143.10) is DETERMINISTIC_API_EVIDENCE. It records relation types without converting either edge into a proof or categorical universal property.

### 143.11 Native evidence profile

The thirty-three assigned addresses collectively contribute

$$
E_{\mathrm{native}}=(124\ \mathrm{English},0\ \mathrm{equations},0\ \mathrm{definitions},0\ \mathrm{theorem/proof},2\ \mathrm{dependencies}). \tag{143.11}
$$

Equation (143.11) is DETERMINISTIC_COVERAGE_EVIDENCE. Standard formulas (143.2)-(143.9) remain external conventions rather than recovered framework equations.

### 143.12 Coverage distribution

Every address in the assigned slice remains THIN,

$$
N_{\mathrm{THIN}}=33,\qquad N_{\mathrm{MEDIUM}}=N_{\mathrm{THICK}}=0. \tag{143.12}
$$

Equation (143.12) is DETERMINISTIC_COVERAGE_EVIDENCE. Canonical naming does not substitute for mathematical population.

### 143.13 Dependency-definition profile

The Identity Class, Dependency Graph, Recursive Dependency Graph, and Dependency Subgraph addresses contribute

$$
E_{\mathrm{dependency\ definitions}}=(15,0,0,0,0). \tag{143.13}
$$

Equation (143.13) is DETERMINISTIC_COVERAGE_EVIDENCE. Their title class is definition-like, but the coherent-unit ledger contains no exact definition unit for this slice.

### 143.14 Theorem-graph profile

The dominant address contributes

$$
E_{@\mathrm{theorem\_graph}}=(48,0,0,0,2). \tag{143.14}
$$

Equation (143.14) is DETERMINISTIC_COVERAGE_EVIDENCE. The two graph dependencies are structural metadata and do not constitute theorem proofs.

### 143.15 Boundary and chirality-map profile

Boundary Projection, Primitive P10, and Primitive P6 jointly contribute

$$
E_{\mathrm{boundary/chirality}}=(26,0,0,0,0). \tag{143.15}
$$

Equation (143.15) is DETERMINISTIC_COVERAGE_EVIDENCE. No typed functor, projection domain, projection codomain, or chirality-map law is recovered here.

### 143.16 Axiom-consistency profile

Axiom Schemes and Consistency contributes

$$
E_{\mathrm{axiom\ schemes}}=(10,0,0,0,0). \tag{143.16}
$$

Equation (143.16) is DETERMINISTIC_COVERAGE_EVIDENCE. Consistency in a title is not a recovered consistency proof.

### 143.17 Named theorem and lemma boundary

The assigned theorem and lemma titles have

$$
N_{\mathrm{named\ theorem/lemma\ addresses}}=8,\qquad N_{\mathrm{proof\ units}}=0. \tag{143.17}
$$

Equation (143.17) is DETERMINISTIC_COVERAGE_EVIDENCE. Dependency Graph Emergence, Finite Directed Graph Representation, Framework Integrity, Superposition, First Distinction, and Path Generation therefore retain NOT_PROVED status in this chapter.

### 143.18 Appendix-address boundary

The fifteen appendix addresses supply only one English unit in aggregate,

$$
E_{\mathrm{appendices}}=(1,0,0,0,0). \tag{143.18}
$$

Equation (143.18) is DETERMINISTIC_COVERAGE_EVIDENCE. Their presence preserves navigation without fabricating categorical content.

### 143.19 API-status profile

All assigned handles are declared,

$$
N_{\mathrm{DECLARED}}=33. \tag{143.19}
$$

Equation (143.19) is DETERMINISTIC_COVERAGE_EVIDENCE. DECLARED supplies a mathematical address; it does not determine object class, universal property, or proof status.

### 143.20 Open graph and category obligations

The unresolved convention set is

$$
\Omega_{143}=\{V,E,s,t,\lambda,\tau,\operatorname{Ob},\operatorname{Hom},\circ,1,\text{functors},\text{proofs}\}. \tag{143.20}
$$

Equation (143.20) is CURATOR_SYNTHESIS. These items must be supplied per construction before API dependency diagrams may be interpreted as categorical mathematics.

### 143.21 Chapter determination

The appendix result is

$$
\begin{aligned}
\mathrm{GraphCategory}_{143}
&=33\ \mathrm{DECLARED\ ADDRESSES}+2\ \mathrm{TYPED\ API\ EDGES}\\
&\quad+\mathrm{EXPLICIT\ EXTERNAL\ CONVENTIONS}\\
&\quad+\mathrm{NO\ GRAPH\text{-}TO\text{-}PROOF\ PROMOTION}.
\end{aligned} \tag{143.21}
$$

Equation (143.21) is DETERMINISTIC_STATUS_NORMALIZATION. V18-C09 establishes a comparison grammar while retaining every typing and proof gap exposed by Library 4.1.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@appendix_25` | @appendix_25` — Appendix 25 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_32` | @appendix_32` — Appendix 32 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_4` | @appendix_4` — Appendix 4 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_5` | @appendix_5` — Appendix 5 | THIN | 1 / 0 / 0 | chapter-core object |
| `@appendix_ab` | @appendix_ab` — Appendix AB | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_af` | @appendix_af` — Appendix AF | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_ah` | @appendix_ah` — Appendix AH | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_al` | @appendix_al` — Appendix AL | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_aw` | @appendix_aw` — Appendix AW | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_ba` | @appendix_ba` — Appendix BA | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_bf` | @appendix_bf` — Appendix BF | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_bs` | @appendix_bs` — Appendix BS | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_bt` | @appendix_bt` — Appendix BT | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_d_er_network_dynamics` | @appendix_d_er_network_dynamics` — Appendix D: ER Network Dynamics | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_e_white_state_limits_and_stability` | @appendix_e_white_state_limits_and_stability` — Appendix E: White--State Limits and Stability | THIN | 0 / 0 / 0 | chapter-core object |
| `@axiom_schemes_and_consistency` | @axiom_schemes_and_consistency` — Axiom Schemes and Consistency | THIN | 10 / 0 / 0 | chapter-core object |
| `@boundary_projection` | @boundary_projection` — Boundary Projection | THIN | 10 / 0 / 0 | chapter-core object |
| `@lemma_l10` | @lemma_l10` — Lemma L10 — Superposition | THIN | 6 / 0 / 0 | chapter-core object |
| `@prime_axiom_a1` | Axiom A1 — Identity Preservation | THIN | 0 / 0 / 0 | chapter-core object |
| `@prime_axiom_a7` | Axiom A7 — Structural Renaming Invariance | THIN | 0 / 0 / 0 | chapter-core object |
| `@prime_definition_d2` | Definition D2 — Identity Class | THIN | 4 / 0 / 0 | chapter-core object |
| `@prime_definition_d6` | Definition D6 — Dependency Graph | THIN | 4 / 0 / 0 | chapter-core object |
| `@prime_definition_d7` | Definition D7 — Recursive Dependency Graph | THIN | 4 / 0 / 0 | chapter-core object |
| `@prime_definition_d9` | Definition D9 — Dependency Subgraph | THIN | 3 / 0 / 0 | chapter-core object |
| `@prime_lemma_l1` | Lemma L1 — First Distinction Lemma | THIN | 0 / 0 / 0 | chapter-core object |
| `@prime_lemma_l5` | Lemma L5 — Path Generation Lemma | THIN | 2 / 0 / 0 | chapter-core object |
| `@prime_primitive_p2` | Primitive P2 — Boundary | THIN | 4 / 0 / 0 | chapter-core object |
| `@prime_theorem_t1` | Theorem T1 — Dependency Graph Emergence Theorem | THIN | 3 / 0 / 0 | chapter-core object |
| `@prime_theorem_t2` | Theorem T2 — Finite Directed Graph Representation Theorem | THIN | 2 / 0 / 0 | chapter-core object |
| `@primitive_p10` | @primitive_p10` — Primitive P10 — Boundary Projection | THIN | 8 / 0 / 0 | chapter-core object |
| `@primitive_p6` | @primitive_p6` — Primitive P6 — Chirality Map | THIN | 8 / 0 / 0 | chapter-core object |
| `@theorem_graph` | @theorem_graph | THIN | 48 / 0 / 2 | chapter-core object |
| `@theorem_t3` | @theorem_t3` — Theorem T3 — Framework Integrity Theorem | THIN | 7 / 0 / 0 | chapter-core object |
