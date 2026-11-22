# VOLUME XVIII - MATHEMATICAL APPENDICES

## Chapter 144 - API-Native Derivation Trees

### 144.1 Derivation-tree record

A derivation record must declare nodes, parent relation, root, premises, rule labels, conclusions, typing, status, and provenance,

$$
\mathfrak D=(N,\prec,r,P,\lambda,C,\tau,\sigma,p). \tag{144.1}
$$

Equation (144.1) is DETERMINISTIC_TYPE_NORMALIZATION. An API neighborhood becomes a derivation tree only when its edges carry valid inferential roles.

### 144.2 Rooted tree

A finite rooted tree has a distinguished root and a unique path from that root to every node,

$$
T=(N,E,r),\qquad \forall n\in N\;\exists!\,p:r\leadsto n. \tag{144.2}
$$

Equation (144.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. A dependency graph with cycles or multiple ancestry paths is not a tree without an explicit unfolding convention.

### 144.3 Parent map

For every nonroot node, a parent map may be written

$$
\pi:N\setminus\{r\}\longrightarrow N,\qquad (\pi(n),n)\in E. \tag{144.3}
$$

Equation (144.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. The symbol is local to this appendix and is not a recovered MK-43 projection operator.

### 144.4 Labeled inference node

If premises $P_1,\ldots,P_k$ support a conclusion $C$ under rule $R$, the node is displayed as

$$
\frac{P_1\quad\cdots\quad P_k}{C}\;R. \tag{144.4}
$$

Equation (144.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. The rule must be named and its admissibility established in the applicable formal system.

### 144.5 Derivation depth

The depth of a rooted derivation tree is

$$
\operatorname{depth}(T)=\max_{n\in N}\operatorname{dist}(r,n). \tag{144.5}
$$

Equation (144.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. Recursion depth and logical proof depth remain different quantities unless a source types their relation.

### 144.6 Dependency closure

For a directed dependency relation $R$, the transitive closure is

$$
R^{+}=\bigcup_{k\ge1}R^k. \tag{144.6}
$$

Equation (144.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Reachability does not establish logical consequence, physical causation, or object identity.

### 144.7 Topological order

A finite directed acyclic graph admits an ordering in which every edge points forward,

$$
(u,v)\in E\Longrightarrow \operatorname{ord}(u)<\operatorname{ord}(v). \tag{144.7}
$$

Equation (144.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. Such an order is not generally unique and does not by itself determine chronology.

### 144.8 Proof-obligation predicate

A candidate conclusion is closed only if all premise, rule, typing, and provenance obligations pass,

$$
\operatorname{Closed}(C)=P_{\mathrm{premise}}\wedge P_{\mathrm{rule}}\wedge P_{\mathrm{type}}\wedge P_{\mathrm{provenance}}. \tag{144.8}
$$

Equation (144.8) is CURATOR_SYNTHESIS. It is an audit predicate for the TOME, not a recovered framework axiom.

### 144.9 Tree-to-DAG distinction

When a conclusion has multiple immediate derivations, its shared representation is a directed acyclic graph rather than a duplicated tree,

$$
\deg^{-}(n)>1\Longrightarrow \text{shared derivation node in a DAG representation}. \tag{144.9}
$$

Equation (144.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. Tree unfoldings may duplicate nodes but may not multiply substantive evidence.

### 144.10 API-native tree boundary

For an API address $h$, a valid derivation tree requires more than its queried neighborhood,

$$
\mathcal T_h=\operatorname{Unfold}(h,E_{\mathrm{typed}},R_{\mathrm{inference}},P_{\mathrm{source}}). \tag{144.10}
$$

Equation (144.10) is DETERMINISTIC_TYPE_NORMALIZATION. In this chapter the required inference rules and native equations are absent, so no completed object-level derivation tree is asserted.

### 144.11 Native evidence profile

The seventeen assigned API addresses collectively contribute

$$
E_{\mathrm{native}}=(24\ \mathrm{English},0\ \mathrm{equations},1\ \mathrm{definition},0\ \mathrm{theorem/proof},0\ \mathrm{dependencies}). \tag{144.11}
$$

Equation (144.11) is DETERMINISTIC_COVERAGE_EVIDENCE. Equations (144.2)-(144.9) remain explicit external conventions.

### 144.12 Coverage distribution

The coverage split is

$$
N_{\mathrm{THIN}}=16,\qquad N_{\mathrm{MEDIUM}}=1,\qquad N_{\mathrm{total}}=17. \tag{144.12}
$$

Equation (144.12) is DETERMINISTIC_COVERAGE_EVIDENCE. Only the Pre-Genesis Manifold definition address reaches MEDIUM.

### 144.13 Pre-Genesis definition profile

The Definition 18.1 address contributes

$$
E_{\mathrm{pre\text{-}genesis\ manifold}}=(3,0,1,0,0). \tag{144.13}
$$

Equation (144.13) is DETERMINISTIC_COVERAGE_EVIDENCE. One exact definition does not supply a derivation of the manifold's later representations.

### 144.14 Observable-algebra profile

The Observable Algebra address contributes

$$
E_{\mathrm{observable\ algebra}}=(9,0,0,0,0). \tag{144.14}
$$

Equation (144.14) is DETERMINISTIC_COVERAGE_EVIDENCE. No exact algebra, product, involution, representation, or derivation rule is present in this assigned slice.

### 144.15 Named-derivation appendix profile

Quadratic Expansion and TT Derivation, TT Derivations, Bead Hamiltonian Derivation, and Continuum Limit to GR collectively contribute

$$
E_{\mathrm{named\ derivation\ appendices}}=(1,0,0,0,0). \tag{144.15}
$$

Equation (144.15) is DETERMINISTIC_COVERAGE_EVIDENCE. Their canonical titles are navigational evidence, not recovered derivation steps.

### 144.16 Generic appendix profile

The remaining eleven appendix addresses contribute

$$
E_{\mathrm{generic\ appendices}}=(11,0,0,0,0). \tag{144.16}
$$

Equation (144.16) is DETERMINISTIC_COVERAGE_EVIDENCE. No hidden proof content is inferred from appendix numbering.

### 144.17 Equation boundary

The native equation ledger for this assigned slice is empty,

$$
N_{\mathrm{native\ equations}}=0. \tag{144.17}
$$

Equation (144.17) is DETERMINISTIC_COVERAGE_EVIDENCE. Consequently no quadratic, transverse-traceless, Hamiltonian, or continuum-limit equation is reconstructed here.

### 144.18 Proof boundary

No coherent theorem-or-proof unit is attached,

$$
N_{\mathrm{theorem/proof}}=0. \tag{144.18}
$$

Equation (144.18) is DETERMINISTIC_COVERAGE_EVIDENCE. A derivation-themed title cannot elevate proof status.

### 144.19 API-status profile

All assigned handles are declared,

$$
N_{\mathrm{DECLARED}}=17. \tag{144.19}
$$

Equation (144.19) is DETERMINISTIC_COVERAGE_EVIDENCE. DECLARED means addressable through API 4.3, not mathematically derived.

### 144.20 Open derivation obligations

The unresolved derivation set is

$$
\Omega_{144}=\{\text{premises},\text{rules},\text{typed edges},\text{equations},\text{boundary conditions},\text{proofs},\text{status}\}. \tag{144.20}
$$

Equation (144.20) is CURATOR_SYNTHESIS. Each item must resolve to exact provenance before an API-native derivation tree can be treated as complete.

### 144.21 Chapter determination

The appendix result is

$$
\begin{aligned}
\mathrm{DerivationTrees}_{144}
&=17\ \mathrm{DECLARED\ ADDRESSES}\\
&\quad+\mathrm{TREE/DAG\ AUDIT\ GRAMMAR}\\
&\quad+\mathrm{NO\ TITLE\text{-}TO\text{-}DERIVATION\ PROMOTION}.
\end{aligned} \tag{144.21}
$$

Equation (144.21) is DETERMINISTIC_STATUS_NORMALIZATION. V18-C10 preserves the address space while exposing the exact mathematics still needed for derivation-tree completion.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@appendix_14` | @appendix_14` — Appendix 14 | THIN | 4 / 0 / 0 | chapter-core object |
| `@appendix_15` | @appendix_15` — Appendix 15 | THIN | 3 / 0 / 0 | chapter-core object |
| `@appendix_17` | @appendix_17` — Appendix 17 | THIN | 1 / 0 / 0 | chapter-core object |
| `@appendix_36` | @appendix_36` — Appendix 36 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_42` | @appendix_42` — Appendix 42 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_a_quadratic_expansion_and_tt_derivation` | @appendix_a_quadratic_expansion_and_tt_derivation` — Appendix A: Quadratic Expansion and TT Derivation | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_a_tt_derivations` | @appendix_a_tt_derivations` — Appendix A: TT Derivations | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_ac` | @appendix_ac` — Appendix AC | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_ay` | @appendix_ay` — Appendix AY | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_b` | @appendix_b` — Appendix B | THIN | 2 / 0 / 0 | chapter-core object |
| `@appendix_b_bead_hamiltonian_derivation` | @appendix_b_bead_hamiltonian_derivation` — Appendix B: Bead Hamiltonian Derivation | THIN | 1 / 0 / 0 | chapter-core object |
| `@appendix_bh` | @appendix_bh` — Appendix BH | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_bv` | @appendix_bv` — Appendix BV | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_c_continuum_limit_to_gr` | @appendix_c_continuum_limit_to_gr` — Appendix C: Continuum Limit to GR | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_o` | @appendix_o` — Appendix O | THIN | 1 / 0 / 0 | chapter-core object |
| `@definition_18_1_pre_genesis_manifold` | @definition_18_1_pre_genesis_manifold` — Definition 18.1 — Pre-Genesis Manifold | MEDIUM | 3 / 0 / 0 | chapter-core object |
| `@observable_algebra` | @observable_algebra` — Observable Algebra | THIN | 9 / 0 / 0 | chapter-core object |
