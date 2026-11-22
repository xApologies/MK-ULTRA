# VOLUME XVIII - MATHEMATICAL APPENDICES

## Chapter 138 - Definitions

### 138.1 Definition record

A definition entry must preserve the canonical address, term, exact defining text, formal signature, scope, status, and provenance,

$$
\mathfrak D=(h,t,d,\tau,\Omega,\sigma,p). \tag{138.1}
$$

Equation (138.1) is DETERMINISTIC_TYPE_NORMALIZATION. A declared title may identify a definition-shaped address while the exact defining text remains absent from the coherent evidence layer.

### 138.2 Definitional equality

Definitional introduction is represented separately from proved equality,

$$
t:=d. \tag{138.2}
$$

Equation (138.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. The notation records a stipulated meaning within a scope; it does not assert empirical identity.

### 138.3 Scope rule

A definition binds only inside its declared scope,

$$
(t:=d)_{\Omega_1}\not\Rightarrow(t:=d)_{\Omega_2}. \tag{138.3}
$$

Equation (138.3) is DETERMINISTIC_TYPE_NORMALIZATION. Historical versions, namespaces, and source-local conventions therefore remain distinct.

### 138.4 Conservative extension

A conservative definition should not add new consequences in the old vocabulary,

$$
T' = T\cup\{t:=d\},\quad \varphi\in\mathcal L(T),\quad T'\vdash\varphi\Rightarrow T\vdash\varphi. \tag{138.4}
$$

Equation (138.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. Whether a recovered MK-43 definition is conservative requires a specified theory and proof.

### 138.5 Well-formedness

A typed definition requires its definiens to inhabit the declared type,

$$
d\in\tau\quad\Rightarrow\quad t:\tau. \tag{138.5}
$$

Equation (138.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. Missing domains, codomains, units, or index conventions prevent a fully typed reconstruction.

### 138.6 Circularity boundary

A direct circular definition does not determine independent content,

$$
t:=F(t)\quad\not\Rightarrow\quad\exists!t. \tag{138.6}
$$

Equation (138.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Fixed-point existence and uniqueness require additional hypotheses.

### 138.7 Equivalent descriptions

Two definitions are interchangeable only under an explicit equivalence result,

$$
T\vdash(d_1\leftrightarrow d_2)\quad\Rightarrow\quad(t:=d_1)\sim_T(t:=d_2). \tag{138.7}
$$

Equation (138.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. Lexical similarity does not supply the required derivation.

### 138.8 Definition-versus-axiom boundary

A definition and an axiom have different formal roles,

$$
(t:=d)\not\equiv A\in\mathcal A. \tag{138.8}
$$

Equation (138.8) is DETERMINISTIC_TYPE_NORMALIZATION. This chapter therefore does not reclassify axiom-titled addresses as definitions.

### 138.9 Definition-versus-primitive boundary

A defined term and a primitive term are likewise distinct,

$$
t\in\mathcal D\quad\Rightarrow\quad t\notin\mathcal P\ \text{within the same presentation}. \tag{138.9}
$$

Equation (138.9) is DETERMINISTIC_TYPE_NORMALIZATION. Later versions may reorganize a theory, but such changes require explicit chronology and scope.

### 138.10 Dependency Path address

The sole explicitly definition-titled address in the assignment is

$$
h_D=@\mathrm{prime\_definition\_d5}. \tag{138.10}
$$

Equation (138.10) is DETERMINISTIC_API_EVIDENCE. Its exact API title is Definition D5 - Dependency Path, while coherent coverage contains four English units and zero definition units.

### 138.11 Missing-definition rule

A definition title with zero definition units remains unpopulated as a formal definition,

$$
N_{\mathrm{definition}}(h)=0\quad\Rightarrow\quad\operatorname{FormalDefinitionRecovered}(h)=\mathrm{false}. \tag{138.11}
$$

Equation (138.11) is DETERMINISTIC_STATUS_NORMALIZATION. This negative result prevents title-driven reconstruction.

### 138.12 Projective Target Manifold boundary

The Projective Target Manifold address contributes contextual prose only,

$$
E_{@\mathrm{projective\_target\_manifold}}=(10,0,0). \tag{138.12}
$$

Equation (138.12) is DETERMINISTIC_COVERAGE_EVIDENCE. No exact definition, equation, or dependency is claimed from this query.

### 138.13 Axiom-title profile

The five axiom-titled addresses contribute

$$
E_{\mathrm{axiom\ titles}}=(10+10+9+9+12,0,0)=(50,0,0). \tag{138.13}
$$

Equation (138.13) is DETERMINISTIC_COVERAGE_EVIDENCE. Infinity Spectrum Ordering, Phase Invariance, Inherited State Bundle, Superposition Closure, and Boundary Projection retain axiom status rather than being converted into definitions.

### 138.14 Primitive-title profile

The two primitive addresses contribute

$$
E_{\mathrm{primitive\ titles}}=(5,0,0)+(4,0,0)=(9,0,0). \tag{138.14}
$$

Equation (138.14) is DETERMINISTIC_COVERAGE_EVIDENCE. Structural Zero and Structural Distinction remain namespace-distinct primitive records.

### 138.15 Aggregate native profile

The eighteen assigned addresses supply

$$
E_{138}=(77\ \mathrm{English},0\ \mathrm{equations},0\ \mathrm{definitions},0\ \mathrm{dependencies}). \tag{138.15}
$$

Equation (138.15) is DETERMINISTIC_COVERAGE_EVIDENCE. The chapter assignment contains no exact coherent definition unit despite its appendix title.

### 138.16 Coverage distribution

Every assigned handle is THIN,

$$
N_{\mathrm{THIN}}=18,qquad N_{\mathrm{MEDIUM}}=N_{\mathrm{THICK}}=0. \tag{138.16}
$$

Equation (138.16) is DETERMINISTIC_COVERAGE_EVIDENCE. Repetition in raw fragments does not increase substantive coverage.

### 138.17 API-status distribution

All assigned records are declared,

$$
N_{\mathrm{DECLARED}}=18. \tag{138.17}
$$

Equation (138.17) is DETERMINISTIC_COVERAGE_EVIDENCE. Address declaration is not exact definition recovery.

### 138.18 Zero-evidence appendix set

Six of the seven generic appendix addresses have zero English, equation, definition, and dependency units,

$$
N_{\mathrm{zero\ appendix}}=6. \tag{138.18}
$$

Equation (138.18) is DETERMINISTIC_COVERAGE_EVIDENCE. Appendix D alone contributes two English units; none contributes a coherent definition.

### 138.19 Publication boundary

A normalized glossary statement cannot replace an absent source definition,

$$
\operatorname{CuratorGloss}(t)\not\Rightarrow\operatorname{ExactDefinition}(t). \tag{138.19}
$$

Equation (138.19) is EVIDENCE_BOUNDARY. This appendix records the gap rather than filling it with invented formal content.

### 138.20 Open definition obligations

The unresolved work is

$$
\begin{aligned}
\Omega_{138}=\{&\mathrm{ExactDefiningText,Definienda,Definientia,Types,Scopes},\\
&\mathrm{Domains,Codomains,Units,Noncircularity,EquivalenceProofs,VersionLinks}\}. \tag{138.20}
\end{aligned}
$$

Equation (138.20) is CURATOR_SYNTHESIS. Exact source recovery or explicit mathematical development is required before these entries can become a complete formal dictionary.

### 138.21 Chapter determination

The appendix result is

$$
\begin{aligned}
\mathrm{Definitions}_{138}={}&\mathrm{EIGHTEEN\_THIN\_DECLARED\_ADDRESSES}\\
&+\mathrm{ZERO\_EXACT\_DEFINITION\_UNITS}\\
&+\mathrm{TITLE\_TYPE\_SEPARATION}+\mathrm{NO\_INVENTED\_DEFINITIONS}. \tag{138.21}
\end{aligned}
$$

Equation (138.21) is DETERMINISTIC_STATUS_NORMALIZATION. V18-C04 establishes a definition-recovery boundary and leaves every missing formal statement explicitly open.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@appendix_40` | @appendix_40` — Appendix 40 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_9` | @appendix_9` — Appendix 9 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_an` | @appendix_an` — Appendix AN | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_az` | @appendix_az` — Appendix AZ | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_bi` | @appendix_bi` — Appendix BI | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_d` | @appendix_d` — Appendix D | THIN | 2 / 0 / 0 | chapter-core object |
| `@appendix_l` | @appendix_l` — Appendix L | THIN | 0 / 0 / 0 | chapter-core object |
| `@axiom_15_2_infinity_spectrum_ordering` | @axiom_15_2_infinity_spectrum_ordering` — Axiom 15.2 — Infinity Spectrum Ordering | THIN | 10 / 0 / 0 | chapter-core object |
| `@axiom_3_5_phase_invariance` | @axiom_3_5_phase_invariance` — Axiom 3.5 — Phase Invariance | THIN | 10 / 0 / 0 | chapter-core object |
| `@axiom_a1` | @axiom_a1` — Axiom A1 — Inherited State Bundle | THIN | 9 / 0 / 0 | chapter-core object |
| `@axiom_a10` | @axiom_a10` — Axiom A10 — Superposition Closure | THIN | 9 / 0 / 0 | chapter-core object |
| `@axiom_a5` | @axiom_a5` — Axiom A5 — Boundary Projection | THIN | 12 / 0 / 0 | chapter-core object |
| `@prime_axiom_a2` | Axiom A2 — Boundary Distinguishability | THIN | 0 / 0 / 0 | chapter-core object |
| `@prime_definition_d5` | Definition D5 — Dependency Path | THIN | 4 / 0 / 0 | chapter-core object |
| `@prime_lemma_l4` | Lemma L4 — First Node Lemma | THIN | 2 / 0 / 0 | chapter-core object |
| `@prime_prime_primitive_p0` | Prime Primitive P0 — Structural Zero | THIN | 5 / 0 / 0 | chapter-core object |
| `@prime_primitive_p4` | Primitive P4 — Structural Distinction | THIN | 4 / 0 / 0 | chapter-core object |
| `@projective_target_manifold` | @projective_target_manifold` — Projective Target Manifold | THIN | 10 / 0 / 0 | chapter-core object |
