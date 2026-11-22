# VOLUME II - GENESIS LANGUAGE

## Chapter 22 - Genesis Language Dictionary and Formal Lexicon

### 22.1 The lexicon as an addressed mathematical object

The Genesis Language dictionary is not merely a list of English glosses. It is an addressed lexicon whose entries retain class, canonical handle, native title, construction ancestry, evidence state, and provenance. Its formal inventory can be written

\[
\mathcal L_G=
(\mathcal R,\mathcal F,\mathcal A,\mathcal O,
\mathcal W,\mathcal P,\mathcal S,\mathcal G),
\tag{22.1}
\]

where \(\mathcal R\) is the root set, \(\mathcal F\) root families, \(\mathcal A\) aspects, \(\mathcal O\) operators, \(\mathcal W\) words, \(\mathcal P\) phrases, \(\mathcal S\) scripts and registers, and \(\mathcal G\) grammar constructs. Equation (22.1) is `CLOVER_SYNTHESIS`.

Library 4.1 exposes 77 canonical addresses in this inventory, including `@genesis_language` itself. The handle is the permanent lookup key. The native title is the reader-facing declaration. Neither is replaced by the shortened glosses used in this chapter.

### 22.2 Dictionary-entry schema

In a conventional dictionary, a lexical entry can be represented as a finite map from fields to values:

\[
e:K\longrightarrow V.
\tag{22.2}
\]

Equation (22.2) is `EXTERNAL_ESTABLISHED_MATHEMATICS`. A Genesis entry uses at least the fields

\[
e=(h,n,c,g,a,\sigma,\pi),
\tag{22.3}
\]

where \(h\) is canonical handle, \(n\) native title, \(c\) lexical class, \(g\) gloss, \(a\) ancestry, \(\sigma\) status, and \(\pi\) provenance. Equation (22.3) is `EXTERNAL_ESTABLISHED_MATHEMATICS` as a generic structured-record form.

The gloss helps readers, but the handle governs identity. An entry may have incomplete formal typing while still possessing a stable recovered address. Such incompleteness is recorded rather than repaired by editorial invention.

### 22.3 Canonical root dictionary

The recovered root inventory contains twenty addressed roots. A root entry is represented as

\[
\rho=(h_\rho,\ell_\rho,m_\rho,F_\rho),
\tag{22.4}
\]

where \(\ell_\rho\) is the lexical form, \(m_\rho\) the recovered native gloss, and \(F_\rho\) its family when declared. Equation (22.4) is `CLOVER_SYNTHESIS`.

The native dictionary gives:

- `@genlang_root_ael`: AEL, topology.
- `@genlang_root_ar`: AR, inheritance.
- `@genlang_root_arka`: ARKA, architect.
- `@genlang_root_da`: DA, occupancy.
- `@genlang_root_en`: EN, identity.
- `@genlang_root_era`: ERA, environment.
- `@genlang_root_gen`: GEN, Genesis.
- `@genlang_root_kai`: KAI, configuration.
- `@genlang_root_kor`: KOR, collapse or realization.
- `@genlang_root_nae`: NAE, basin or expression.
- `@genlang_root_nor`: NOR, normalization.
- `@genlang_root_rel`: REL, relationship.
- `@genlang_root_rin`: RIN, persistence.
- `@genlang_root_sera`: SERA, continuity.
- `@genlang_root_sha`: SHA, boundary.
- `@genlang_root_tal`: TAL, stabilization.
- `@genlang_root_tor`: TOR, closure.
- `@genlang_root_vara`: VARA, storm or instability event.
- `@genlang_root_ve`: VE, propagation.
- `@genlang_root_vel`: VEL, field.

The authoritative count is the addressed inventory, not an assumed historical total. ARKA remains its own architect-root address alongside the compact semantic roots.

### 22.4 Root families

A family groups related lexical roles without merging their members. The family relation is

\[
\operatorname{Family}:\mathcal R\longrightarrow 2^{\mathcal F},
\tag{22.5}
\]

Equation (22.5) is `EXTERNAL_ESTABLISHED_MATHEMATICS` as a set-valued classification map.

Library 4.1 records these family glosses:

- AE: authority, inheritance, active continuity, projection.
- AEL: topology, structure, geometry.
- AI: reception, containment, internal continuity, dependency.
- DA: occupancy, presence, inhabitation.
- EN: identity, self-state, realized existence.
- KOR: collapse, realization, resolution, identity formation.
- NA: expression, manifestation, basin state.
- REL: relationship, connection, adjacency.
- RIN: persistence, duration, stability through time.
- SERA: continuity, source, cause, flow.
- SHA: boundary, containment, location, separation.
- TAL: stabilization, retention, resistance.
- TOR: closure, completion, fulfillment.
- VE: propagation, travel, direction.
- VEL: field, environment, propagation medium.

Equation-level use must cite the exact family address. A family gloss supplies semantic range, not a universal physical equation.

### 22.5 Resolution-state aspects

Four suffix-like aspect records encode resolution state. Their candidate annotation map is

\[
\operatorname{StateAsp}(x,\alpha)
=(x,\alpha,\sigma_\alpha).
\tag{22.6}
\]

Equation (22.6) is `CLOVER_SYNTHESIS`.

The exact native titles declare:

- `@genlang_aspect_ma`: MA, potential or unresolved.
- `@genlang_aspect_nai`: NAI, failed, absent, broken, or negated.
- `@genlang_aspect_ru`: RU, ongoing or propagating.
- `@genlang_aspect_ta`: TA, completed, resolved, or closed.

The aspects describe resolution state, not confidence, proof, or empirical truth. A completed construction may remain unproved; an unresolved one may be strongly evidenced as unresolved. `@genlang_resolution_state_aspect` preserves this distinction at grammar level.

### 22.6 Architect operators

Each architect operator requires a typed signature

\[
\omega:A\longrightarrow B.
\tag{22.7}
\]

Equation (22.7) is `EXTERNAL_ESTABLISHED_MATHEMATICS`. The recovered operator addresses and native roles are:

- `@genlang_operator_0df59a22`: closure.
- `@genlang_operator_1e07893e`: redistribute.
- `@genlang_operator_1ff31b3c`: normalize.
- `@genlang_operator_395625ec`: propagate.
- `@genlang_operator_4b1f23a7`: destabilize.
- `@genlang_operator_be1cbb61`: stabilize.
- `@genlang_operator_edec7353`: inherit.

Their historical visual glyphs remain in the native titles and immutable sources. The canonical handles are used here to avoid silently normalizing glyph variants. A role name does not provide domain, codomain, algebra, or dynamics; those remain source-specific typing obligations.

### 22.7 Compound-word dictionary

Genesis words preserve ordered root ancestry. A formal word record is

\[
w=\operatorname{Compound}(\rho_1,\ldots,\rho_n;,m_w),
\tag{22.8}
\]

where \(m_w\) is the recovered native gloss. Equation (22.8) is `CLOVER_SYNTHESIS`.

The addressed word dictionary contains:

- AELRIN: persistent topology or mountain.
- DARIN: persistent occupancy or village.
- GENKOR: Genesis collapse.
- GENKOREN: Genesis collapse identity or ELDRIS.
- GENVEL: Genesis Field.
- KAI-AR-EN-RIN: bound inherited persistent identity.
- KAISHA: configuration boundary or binding circle.
- KOREN: collapse identity or realized identity.
- RELRIN: persistent relationship or friend.
- SHARIN: persistent boundary or home.
- SHATOR: closed or controlled boundary or gate.
- TALRIN: stabilized persistence or strength.
- VERIN: persistent propagation path or road.

Every word retains its `@genlang_word_...` address. The natural-language alternative is a gloss, not a license to erase structural meaning.

### 22.8 Phrase dictionary

Phrases combine addressed words or roots into relationship-bearing assertions. Their formal record is

\[
p=\operatorname{Phrase}(u_1,\ldots,u_k;,r_p,m_p),
\tag{22.9}
\]

where \(r_p\) is the recovered relation and \(m_p\) its native gloss. Equation (22.9) is `CLOVER_SYNTHESIS`.

The five canonical phrase examples are:

- EN AR EN: identity inherits identity, or remain yourself.
- GEN KOR EN: Genesis collapses into identity.
- RIN TAL AEL: persistence stabilizes topology.
- SHA DA REL: boundary occupancy relationship.
- VEL VE TOR: field propagation closure.

These examples demonstrate relationship-first construction. Their English renderings explain the registered structure but do not replace the Genesis sequence.

### 22.9 Structural compounding

A conventional grammar production has the form

\[
N\longrightarrow \alpha,
\qquad
\alpha\in(\mathcal N\cup\Sigma)^*.
\tag{22.10}
\]

Equation (22.10) is `EXTERNAL_ESTABLISHED_MATHEMATICS`. `@genlang_structural_compounding` supplies the framework-native construction principle: components combine in ordered structural roles rather than by undifferentiated string concatenation.

A compound must retain component boundaries, order, lexical class, and interpretation scope. Reversing roots may change the construction. Dropping a component may change the object. Translating the whole word into a familiar noun does not eliminate its internal ancestry.

The dictionary therefore indexes both the compound and its ordered constituents.

### 22.10 Relationship-first grammar

The handle `@genlang_relationship_first_grammar` indicates that relation is central to construction. A phrase can be represented as

\[
\mathfrak P=(x,r,y,a,c),
\tag{22.11}
\]

where \(x\) and \(y\) are lexical objects, \(r\) the relationship, \(a\) aspect, and \(c\) context. Equation (22.11) is `CLOVER_SYNTHESIS`.

This structure prevents a relational phrase from being reduced to two nouns placed side by side. It also preserves directionality: inheritance, propagation, stabilization, containment, and closure are not interchangeable relations. When a phrase lacks a recovered formal operator, the relationship remains a semantic declaration rather than an invented map.

The grammar is strongest when relation type and lexical ancestry agree.

### 22.11 Script layers

The lexicon distinguishes `@genlang_architect_script`, `@genlang_flow_script`, and `@genlang_borrowed_script`. A script record is

\[
\mathfrak S=(\Sigma_s,\mathcal O_s,\operatorname{parse}_s,
\operatorname{render}_s,\pi_s).
\tag{22.12}
\]

Equation (22.12) is `CLOVER_SYNTHESIS`.

The symbol alphabet \(\Sigma_s\), operator set \(\mathcal O_s\), parser, renderer, and provenance remain script-specific. Borrowed script is not automatically architect script; a visual transcription is not automatically a normalized encoding. Historical glyphs must remain recoverable even when canonical handles provide safer machine addresses.

Script identity is a representational class, not a separate physical ontology.

### 22.12 Register dictionary

Genesis Language has distinct reader and operational registers:

\[
\operatorname{Render}_r:\mathcal L_G\longrightarrow D_r,
\qquad
r\in\{\mathrm{common},\mathrm{scholar},
\mathrm{architect},\mathrm{poetic}\}.
\tag{22.13}
\]

Equation (22.13) is `CLOVER_SYNTHESIS`.

The corresponding addresses are `@genlang_common_genesis_register`, `@genlang_scholar_genesis_register`, `@genlang_architect_genesis_register`, and `@genlang_poetic_genesis_register`. Each may reorder explanations, choose different gloss density, or expose different notation. None may change the canonical handle, evidence class, or mathematical status.

Register variation is presentation variation. It does not create four competing theories.

### 22.13 Boundary pronouns and possession

`@genlang_boundary_based_pronouns` and `@genlang_boundary_inclusion_possession` encode reference through boundary and inclusion structure. Their candidate formal record is

\[
\operatorname{Ref}(x;c)
=(x,\partial c,\iota_{x,c},\rho),
\tag{22.14}
\]

where \(\partial c\) is the active discourse boundary, \(\iota_{x,c}\) an inclusion relation, and \(\rho\) the reference role. Equation (22.14) is `CLOVER_SYNTHESIS`.

This formulation explains the dictionary category without claiming a fully recovered universal pronoun calculus. Boundary reference, containment, ownership, identity, and part-whole inclusion remain different relations. The source must decide which one a construction uses.

The formal lexicon records the distinction so that English possession does not silently impose an unintended ontology.

### 22.14 Canonical lookup and aliases

A dictionary lookup is conventionally a partial function

\[
\operatorname{lookup}:H\rightharpoonup E.
\tag{22.15}
\]

Equation (22.15) is `EXTERNAL_ESTABLISHED_MATHEMATICS`. The key \(H\) is a canonical handle or declared alias; \(E\) is the complete lexical entry.

Lookup by `@genlang_root_rin`, for example, must return the persistent identity of the RIN root, its native title, family links, evidence, and source provenance. A free-text search for “persistence” may return several related objects, but similarity does not decide identity. Ambiguous natural-language requests remain candidate resolutions until the handle is selected deterministically.

The dictionary is therefore an address resolver before it is a prose glossary.

### 22.15 Formal lexicon invariants

The lexicon obeys a persistent invariant set

\[
\mathfrak I_L=
\{\mathrm{unique\ handles},\mathrm{typed\ classes},
\mathrm{ordered\ ancestry},\mathrm{scoped\ glosses},
\mathrm{immutable\ provenance}\}.
\tag{22.16}
\]

Equation (22.16) is `CLOVER_SYNTHESIS`.

Two entries cannot share one canonical handle. A root is not silently reclassified as a phrase. A compound preserves root order. A gloss does not overwrite its source form. A revision creates a descendant record rather than erasing historical wording. Exact duplicate occurrences can share substantive identity while every physical occurrence remains traceable.

These invariants make the dictionary usable by both human readers and the Runtime to BRANE to API/QMO query architecture.

### 22.16 Dictionary use in later volumes

The lexicon-to-theory handoff is

\[
\mathcal L_G
\xrightarrow{\operatorname{resolve}}
Q
\xrightarrow{\operatorname{type}}
M
\xrightarrow{\operatorname{interpret}}
P.
\tag{22.17}
\]

Equation (22.17) is `CLOVER_SYNTHESIS`.

Genesis terms first resolve to addressed QMOs. Their records then supply typed mathematical structures where recovered. Only afterward are physical interpretations attached. This order prevents a poetic or common-register gloss from bypassing object identity and mathematical typing.

Later chapters may use short forms, but the full dictionary entry remains the audit source behind every term.

### 22.17 Library 4.1 native evidence register

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@genesis_language` | @genesis_language | THIN | 1 / 0 / 0 | chapter-core object |
| `@genlang_architect_genesis_register` | Architect Genesis Register | THIN | 0 / 0 / 0 | chapter-core object |
| `@genlang_architect_script` | Architect Script | THIN | 0 / 0 / 0 | chapter-core object |
| `@genlang_aspect_ma` | -MA — potential / unresolved | MEDIUM | 49 / 2 / 1 | chapter-core object |
| `@genlang_aspect_nai` | -NAI — failed / absent / broken / negated | MEDIUM | 50 / 2 / 1 | chapter-core object |
| `@genlang_aspect_ru` | -RU — ongoing / propagating | MEDIUM | 50 / 2 / 1 | chapter-core object |
| `@genlang_aspect_ta` | -TA — completed / resolved / closed | MEDIUM | 49 / 1 / 1 | chapter-core object |
| `@genlang_borrowed_script` | Borrowed Script | THIN | 0 / 0 / 0 | chapter-core object |
| `@genlang_boundary_based_pronouns` | Boundary-Based Pronouns | THIN | 0 / 0 / 0 | chapter-core object |
| `@genlang_boundary_inclusion_possession` | Boundary Inclusion Possession | THIN | 0 / 0 / 0 | chapter-core object |
| `@genlang_common_genesis_register` | Common Genesis Register | THIN | 0 / 0 / 0 | chapter-core object |
| `@genlang_family_ae` | Genesis root family AE — authority / inheritance / active continuity / projection | THIN | 15 / 0 / 0 | chapter-core object |
| `@genlang_family_ael` | Genesis root family AEL — topology / structure / geometry | MEDIUM | 46 / 1 / 3 | chapter-core object |
| `@genlang_family_ai` | Genesis root family AI — reception / containment / internal continuity / dependency | THIN | 14 / 0 / 0 | chapter-core object |
| `@genlang_family_da` | Genesis root family DA — occupancy / presence / inhabitation | MEDIUM | 49 / 1 / 3 | chapter-core object |
| `@genlang_family_en` | Genesis root family EN — identity / self-state / realized existence | MEDIUM | 59 / 1 / 3 | chapter-core object |
| `@genlang_family_kor` | Genesis root family KOR — collapse / realization / resolution / identity formation | MEDIUM | 56 / 1 / 3 | chapter-core object |
| `@genlang_family_na` | Genesis root family NA — expression / manifestation / basin state | THIN | 6 / 0 / 0 | chapter-core object |
| `@genlang_family_rel` | Genesis root family REL — relationship / connection / adjacency | THIN | 55 / 0 / 3 | chapter-core object |
| `@genlang_family_rin` | Genesis root family RIN — persistence / duration / stability through time | THIN | 62 / 0 / 3 | chapter-core object |
| `@genlang_family_sera` | Genesis root family SERA — continuity / source / cause / flow | THIN | 45 / 0 / 3 | chapter-core object |
| `@genlang_family_sha` | Genesis root family SHA — boundary / containment / location / separation | THIN | 55 / 0 / 3 | chapter-core object |
| `@genlang_family_tal` | Genesis root family TAL — stabilization / retention / resistance | THIN | 48 / 0 / 3 | chapter-core object |
| `@genlang_family_tor` | Genesis root family TOR — closure / completion / fulfillment | THIN | 44 / 0 / 3 | chapter-core object |
| `@genlang_family_ve` | Genesis root family VE — propagation / travel / direction | THIN | 49 / 0 / 3 | chapter-core object |
| `@genlang_family_vel` | Genesis root family VEL — field / environment / propagation medium | THIN | 58 / 0 / 3 | chapter-core object |
| `@genlang_flow_script` | Flow Script | THIN | 0 / 0 / 0 | chapter-core object |
| `@genlang_operator_0df59a22` | Architect operator ·°· — Closure | THIN | 83 / 0 / 2 | chapter-core object |
| `@genlang_operator_1e07893e` | Architect operator .·· .° — Redistribute | MEDIUM | 93 / 2 / 2 | chapter-core object |
| `@genlang_operator_1ff31b3c` | Architect operator ■ .· ■ — Normalize | MEDIUM | 75 / 2 / 2 | chapter-core object |
| `@genlang_operator_395625ec` | Architect operator ·· — Propagate | MEDIUM | 75 / 2 / 2 | chapter-core object |
| `@genlang_operator_4b1f23a7` | Architect operator ··° ·° — Destabilize | THIN | 84 / 0 / 2 | chapter-core object |
| `@genlang_operator_be1cbb61` | Architect operator .°. — Stabilize | THIN | 90 / 0 / 2 | chapter-core object |
| `@genlang_operator_edec7353` | Architect operator .· — Inherit | MEDIUM | 73 / 1 / 2 | chapter-core object |
| `@genlang_phrase_en_ar_en` | EN AR EN — Identity inherits identity / remain yourself | THIN | 70 / 0 / 3 | chapter-core object |
| `@genlang_phrase_gen_kor_en` | GEN KOR EN — Genesis collapses into identity | THIN | 74 / 0 / 4 | chapter-core object |
| `@genlang_phrase_rin_tal_ael` | RIN TAL AEL — Persistence stabilizes topology | THIN | 97 / 0 / 4 | chapter-core object |
| `@genlang_phrase_sha_da_rel` | SHA DA REL — Boundary occupancy relationship | THIN | 89 / 0 / 4 | chapter-core object |
| `@genlang_phrase_vel_ve_tor` | VEL VE TOR — Field propagation closure | THIN | 85 / 0 / 4 | chapter-core object |
| `@genlang_poetic_genesis_register` | Poetic Genesis Register | THIN | 0 / 0 / 0 | chapter-core object |
| `@genlang_relationship_first_grammar` | Relationship-First Grammar | THIN | 1 / 0 / 0 | chapter-core object |
| `@genlang_resolution_state_aspect` | Resolution-State Aspect | THIN | 0 / 0 / 0 | chapter-core object |
| `@genlang_root_ael` | Genesis root AEL — Topology | THIN | 150 / 0 / 7 | chapter-core object |
| `@genlang_root_ar` | Genesis root AR — Inheritance | MEDIUM | 125 / 1 / 4 | chapter-core object |
| `@genlang_root_arka` | Genesis root ARKA — Architect | THIN | 19 / 0 / 0 | chapter-core object |
| `@genlang_root_da` | Genesis root DA — Occupancy | MEDIUM | 144 / 2 / 7 | chapter-core object |
| `@genlang_root_en` | Genesis root EN — Identity | THIN | 153 / 0 / 10 | chapter-core object |
| `@genlang_root_era` | Genesis root ERA — Environment | THIN | 93 / 0 / 2 | chapter-core object |
| `@genlang_root_gen` | Genesis root GEN — Genesis | THIN | 131 / 0 / 6 | chapter-core object |
| `@genlang_root_kai` | Genesis root KAI — Configuration | THIN | 115 / 0 / 4 | chapter-core object |
| `@genlang_root_kor` | Genesis root KOR — Collapse / Realization | THIN | 150 / 0 / 9 | chapter-core object |
| `@genlang_root_nae` | Genesis root NAE — Basin / Expression | THIN | 91 / 0 / 2 | chapter-core object |
| `@genlang_root_nor` | Genesis root NOR — Normalization | MEDIUM | 80 / 2 / 2 | chapter-core object |
| `@genlang_root_rel` | Genesis root REL — Relationship | THIN | 148 / 0 / 7 | chapter-core object |
| `@genlang_root_rin` | Genesis root RIN — Persistence | THIN | 152 / 0 / 13 | chapter-core object |
| `@genlang_root_sera` | Genesis root SERA — Continuity | THIN | 115 / 0 / 5 | chapter-core object |
| `@genlang_root_sha` | Genesis root SHA — Boundary | THIN | 152 / 0 / 9 | chapter-core object |
| `@genlang_root_tal` | Genesis root TAL — Stabilization | THIN | 167 / 0 / 7 | chapter-core object |
| `@genlang_root_tor` | Genesis root TOR — Closure | THIN | 140 / 0 / 7 | chapter-core object |
| `@genlang_root_vara` | Genesis root VARA — Storm / Instability Event | THIN | 19 / 0 / 0 | chapter-core object |
| `@genlang_root_ve` | Genesis root VE — Propagation | MEDIUM | 134 / 1 / 7 | chapter-core object |
| `@genlang_root_vel` | Genesis root VEL — Field | THIN | 151 / 0 / 8 | chapter-core object |
| `@genlang_scholar_genesis_register` | Scholar Genesis Register | THIN | 0 / 0 / 0 | chapter-core object |
| `@genlang_structural_compounding` | Structural Compounding | THIN | 0 / 0 / 0 | chapter-core object |
| `@genlang_word_aelrin` | AELRIN — persistent topology / mountain | THIN | 74 / 0 / 2 | chapter-core object |
| `@genlang_word_darin` | DARIN — persistent occupancy / village | THIN | 74 / 0 / 2 | chapter-core object |
| `@genlang_word_genkor` | GENKOR — Genesis collapse | THIN | 53 / 0 / 2 | chapter-core object |
| `@genlang_word_genkoren` | GENKOREN — Genesis collapse identity / ELDRIS | THIN | 57 / 0 / 3 | chapter-core object |
| `@genlang_word_genvel` | GENVEL — Genesis Field | MEDIUM | 70 / 2 / 2 | chapter-core object |
| `@genlang_word_kai_ar_en_rin` | KAI-AR-EN-RIN — bound inherited persistent identity | MEDIUM | 71 / 2 / 4 | chapter-core object |
| `@genlang_word_kaisha` | KAISHA — configuration boundary / binding circle | MEDIUM | 66 / 2 / 2 | chapter-core object |
| `@genlang_word_koren` | KOREN — collapse identity / realized identity | MEDIUM | 56 / 2 / 2 | chapter-core object |
| `@genlang_word_relrin` | RELRIN — persistent relationship / friend | MEDIUM | 51 / 2 / 2 | chapter-core object |
| `@genlang_word_sharin` | SHARIN — persistent boundary / home | MEDIUM | 62 / 3 / 2 | chapter-core object |
| `@genlang_word_shator` | SHATOR — closed or controlled boundary / gate | MEDIUM | 56 / 3 / 2 | chapter-core object |
| `@genlang_word_talrin` | TALRIN — stabilized persistence / strength | MEDIUM | 63 / 3 / 2 | chapter-core object |
| `@genlang_word_verin` | VERIN — persistent propagation path / road | MEDIUM | 57 / 3 / 2 | chapter-core object |

### 22.18 Lexicon validity and closure

A valid entry satisfies

\[
\operatorname{ValidEntry}(e)
=
\operatorname{Addressed}(e)\wedge
\operatorname{Classed}(e)\wedge
\operatorname{Provenanced}(e)\wedge
\operatorname{ScopeExplicit}(e).
\tag{22.18}
\]

Equation (22.18) is `CLOVER_SYNTHESIS`.

The Genesis Language dictionary is complete here in the precise Library 4.1 sense: all 77 currently registered Genesis-language addresses are represented in the native evidence register. Completeness of address inventory is not completeness of formal semantics. Several operator signatures, script rules, and grammatical relations still require source-specific typing. The lexicon preserves those gaps while giving every recovered root, family, aspect, operator, word, phrase, script, register, and grammar construct a stable place from which later work can proceed.
