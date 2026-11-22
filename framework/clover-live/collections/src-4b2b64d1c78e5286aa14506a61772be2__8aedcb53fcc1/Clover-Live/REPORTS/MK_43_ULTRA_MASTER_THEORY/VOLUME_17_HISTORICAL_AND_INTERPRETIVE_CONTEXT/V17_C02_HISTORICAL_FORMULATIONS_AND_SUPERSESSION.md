# VOLUME XVII - HISTORICAL AND INTERPRETIVE CONTEXT

## Chapter 130 - Historical Formulations and Supersession

### 130.1 Typed formulation record

A historical formulation must distinguish identity, exact content, source, chronology, object vocabulary, equations, relations, declared status, supersession evidence, and uncertainty,

$$
\mathfrak F=(f,X,S,T,O,Q,R,\sigma,E_{\mathrm{sup}},U). \tag{130.1}
$$

Equation (130.1) is DETERMINISTIC_TYPE_NORMALIZATION. It prevents a historical title from being mistaken for a fully recovered mathematical version.

### 130.2 Exact-content equivalence

Two occurrences belong to one exact formulation when

$$
f_i\sim_{\mathrm{exact}}f_j\quad\Longleftrightarrow\quad h(X_i)=h(X_j). \tag{130.2}
$$

Equation (130.2) is DETERMINISTIC_AUDIT_NORMALIZATION. Occurrence provenance remains distinct even when exact content is shared.

### 130.3 Formulation difference

A comparison record may be decomposed as

$$
\Delta(f_i,f_j)=(\Delta_X,\Delta_O,\Delta_Q,\Delta_R,\Delta_\sigma). \tag{130.3}
$$

Equation (130.3) is DETERMINISTIC_AUDIT_NORMALIZATION. Text, objects, equations, relations, and status are compared independently.

### 130.4 Source precedence

Where dated sources are nonoverlapping,

$$
T_i^+<T_j^-\quad\Longrightarrow\quad f_i\prec_T f_j. \tag{130.4}
$$

Equation (130.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. Temporal precedence does not by itself imply logical or canonical replacement.

### 130.5 Status vocabulary

A controlled historical status set is

$$
\Sigma_{\mathrm{hist}}=\{\mathrm{EARLY,INTERMEDIATE,LATER,SUPERSEDED,CANDIDATE,UNRESOLVED}\}. \tag{130.5}
$$

Equation (130.5) is DETERMINISTIC_STATUS_NORMALIZATION. Each assignment requires exact source or curator provenance.

### 130.6 Explicit supersession predicate

Supersession is admitted only when supported by an identified record,

$$
f_j\succ_{\mathrm{sup}}f_i\quad\Longleftrightarrow\quad \exists e\in E_{\mathrm{sup}}:\ e(f_j,f_i)=\mathrm{explicit}. \tag{130.6}
$$

Equation (130.6) is DETERMINISTIC_AUDIT_NORMALIZATION. The predicate is not inferred from numbering or style.

### 130.7 Convergent replacement candidate

Absent explicit language, a possible replacement remains separately typed,

$$
f_j\succ_{\mathrm{cand}}f_i\quad\Longrightarrow\quad \sigma(f_j,f_i)=\mathrm{UNRESOLVED}. \tag{130.7}
$$

Equation (130.7) is DETERMINISTIC_STATUS_NORMALIZATION. Convergence may motivate review but does not silently supersede a source.

### 130.8 Chapter-number boundary

A larger chapter number is not a version proof,

$$
n_j>n_i\;\not\Rightarrow\;f_j\succ_{\mathrm{sup}}f_i. \tag{130.8}
$$

Equation (130.8) is EVIDENCE_BOUNDARY. Chapter numbering may describe organization rather than developmental sequence.

### 130.9 Later-file boundary

A later modification timestamp is not canonical status,

$$
t_{\mathrm{mtime}}(f_j)>t_{\mathrm{mtime}}(f_i)\;\not\Rightarrow\;\sigma_j=\mathrm{CANON}. \tag{130.9}
$$

Equation (130.9) is EVIDENCE_BOUNDARY. Copying, extraction, export, and metadata repair can alter file times.

### 130.10 Narrative boundary

Historical reconstruction inside a narrative is not automatically documentary history,

$$
\mathrm{NarrativeReconstruction}\;\not\Rightarrow\;\mathrm{SourceAttestedRevision}. \tag{130.10}
$$

Equation (130.10) is EVIDENCE_BOUNDARY. Narrative and scientific formulation layers remain separate.

### 130.11 Aggregate native profile

The eight assigned addresses supply

$$
E_{130}=(30\ \mathrm{English},0\ \mathrm{equations},0\ \mathrm{dependencies}). \tag{130.11}
$$

Equation (130.11) is DETERMINISTIC_COVERAGE_EVIDENCE. No registered supersession structure accompanies the assigned text.

### 130.12 Numbered-chapter profile

The four direct chapter addresses contribute

$$
E_{\mathrm{chapter}}=(11,0,0)+(3,0,0)+(3,0,0)+(4,0,0)=(21,0,0). \tag{130.12}
$$

Equation (130.12) is DETERMINISTIC_COVERAGE_EVIDENCE. Black Rainbow, radial echo, tensor harmony, and anchor titles are preserved as separate historical addresses.

### 130.13 Adapter and narrative profile

The remaining addresses contribute

$$
E_{\mathrm{other}}=(8,0,0)+(1,0,0)+(0,0,0)+(0,0,0)=(9,0,0). \tag{130.13}
$$

Equation (130.13) is DETERMINISTIC_COVERAGE_EVIDENCE. The two zero-unit titles add address provenance but no substantive formulation record.

### 130.14 Relation profile

No source-backed supersession, revision, or replacement edge is registered,

$$
N_{\mathrm{supersedes}}=N_{\mathrm{revises}}=N_{\mathrm{replaces}}=0. \tag{130.14}
$$

Equation (130.14) is DETERMINISTIC_COVERAGE_EVIDENCE. The chapter cannot resolve historical succession from API graph structure.

### 130.15 Name-continuity boundary

Shared terminology does not ensure unchanged meaning,

$$
\mathrm{Name}_i=\mathrm{Name}_j\;\not\Rightarrow\;(O_i,Q_i,R_i)=(O_j,Q_j,R_j). \tag{130.15}
$$

Equation (130.15) is EVIDENCE_BOUNDARY. Object types, equations, and relations must be compared directly.

### 130.16 Elegance boundary

A clearer later expression is not proof of canonical replacement,

$$
\mathrm{Clarity}(f_j)>\mathrm{Clarity}(f_i)\;\not\Rightarrow\;f_j\succ_{\mathrm{sup}}f_i. \tag{130.16}
$$

Equation (130.16) is EVIDENCE_BOUNDARY. Editorial quality and evidentiary status answer different questions.

### 130.17 Typed chapter contract

The retained formulation chain is

$$
\mathfrak F_{130}=(f,X,S,T,O,Q,R,\sigma,E_{\mathrm{sup}},\Omega_{\mathrm{open}}). \tag{130.17}
$$

Equation (130.17) is DETERMINISTIC_TYPE_NORMALIZATION. Content, source, time, mathematical structure, status, evidence, and open work remain distinct.

### 130.18 Coverage calibration

The native query returns

$$
N_H=8,\quad N_{\mathrm{English}}=30,\quad N_{\mathrm{equations}}=0,\quad N_{\mathrm{dependencies}}=0. \tag{130.18}
$$

Equation (130.18) is DETERMINISTIC_COVERAGE_EVIDENCE. All eight handles are THIN.

### 130.19 Scientific boundary

The controlling restriction is

$$
\mathrm{HistoricalAddresses}\cup\mathrm{LaterOccurrence}\;\not\Rightarrow\;\mathrm{VerifiedSupersession}. \tag{130.19}
$$

Equation (130.19) is EVIDENCE_BOUNDARY. No complete version tree or canonical replacement sequence is claimed.

### 130.20 Open historical obligations

The future route is

$$
\begin{aligned}
\Omega_{130}=\{&\mathrm{ExactVersionTexts,Dates,ContentDiffs,ObjectDiffs,EquationDiffs},\\
&\mathrm{RelationDiffs,ExplicitStatus,ReplacementEvidence,ConflictReview}\}. \tag{130.20}
\end{aligned}
$$

Equation (130.20) is CURATOR_SYNTHESIS. These obligations preserve historical differences without forcing a false linear canon.

### 130.21 Chapter determination

The chapter result is

$$
\begin{aligned}
\mathrm{FormulationHistory}_{130}={}&\mathrm{EIGHT\_THIN\_HISTORICAL\_ADDRESSES}\\
&+\mathrm{EXPLICIT\_SUPERSESSION\_CONTRACT}+\mathrm{NO\_RECOVERED\_SUPERSESSION\_EDGE}. \tag{130.21}
\end{aligned}
$$

Equation (130.21) is DETERMINISTIC_STATUS_NORMALIZATION. V17-C02 retains each assigned formulation while leaving replacement and current-canon judgments unresolved.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@chapter_0` | @chapter_0` — Chapter 0: The Black Rainbow | THIN | 11 / 0 / 0 | chapter-core object |
| `@chapter_12_the_radial_echo` | @chapter_12_the_radial_echo` — Chapter 12: The Radial Echo | THIN | 3 / 0 / 0 | chapter-core object |
| `@chapter_14_tensor_harmonies` | @chapter_14_tensor_harmonies` — Chapter 14: Tensor Harmonies | THIN | 3 / 0 / 0 | chapter-core object |
| `@chapter_15_abyssal_anchor_theory` | @chapter_15_abyssal_anchor_theory` — Chapter 15: Abyssal Anchor Theory | THIN | 4 / 0 / 0 | chapter-core object |
| `@chapter_71_adapter_phase_coherent_civilizations_and_collective_stability` | @chapter_71_adapter_phase_coherent_civilizations_and_collective_stability` — Chapter 71 Adapter — Phase-Coherent Civilizations and Collective Stability | THIN | 8 / 0 / 0 | chapter-core object |
| `@egress_flow_accepts_the_team` | @egress_flow_accepts_the_team` — Egress: Flow Accepts the Team | THIN | 1 / 0 / 0 | chapter-core object |
| `@overture_arrival_in_the_luminous_realm` | @overture_arrival_in_the_luminous_realm` — Overture: Arrival in the Luminous Realm | THIN | 0 / 0 / 0 | chapter-core object |
| `@the_abyssal_crown_wars_a_historical_reconstruction_of_resonance_conflict` | @the_abyssal_crown_wars_a_historical_reconstruction_of_resonance_conflict` — The Abyssal Crown Wars: A Historical Reconstruction of Resonance Conflict | THIN | 0 / 0 / 0 | chapter-core object |
