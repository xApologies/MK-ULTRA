# Genesis Language Architecture
Library 4.1 exposes **82** Genesis Language addresses in the native initialization query. The architecture is representational rather than ornamental: it records roles, scope, projection, persistence, realization, relation direction, and resolution state.
## Structural layers
1. **Roots** provide atomic semantic roles such as genesis, identity, collapse/realization, persistence, topology, boundary, occupancy, relationship, field, propagation, inheritance, continuity, and stabilization.
2. **Root families** group those roles into ontological domains without asserting that every member has the same mathematical type.
3. **Operators** encode transformations such as inherit, propagate, stabilize, destabilize, normalize, redistribute, and close.
4. **Resolution aspects** distinguish potential/unresolved, ongoing/propagating, completed/resolved, and failed/absent states.
5. **Compounds and relation-first phrases** compose roles while preserving direction, including `GEN KOR EN`, `RIN TAL AEL`, `SHA DA REL`, `VEL VE TOR`, and `EN AR EN`.
6. **Registers and scripts** select representational scope and usage without changing the referenced mathematical object.
7. **API/QMO bindings** attach language objects to canonical handles and typed mathematical relations.
## Category census
| Category | Addresses |
|---|---:|
| COMPOUND_WORD | 13 |
| GRAMMAR_OR_LANGUAGE_ROOT | 6 |
| OPERATOR | 7 |
| REGISTER | 4 |
| RELATED_LANGUAGE_OBJECT | 5 |
| RELATION_FIRST_PHRASE | 5 |
| RESOLUTION_ASPECT | 4 |
| ROOT | 20 |
| ROOT_FAMILY | 15 |
| SCRIPT | 3 |

## Complete address inventory

| Handle | Canonical name | Category | Equations | In | Out |
|---|---|---|---:|---:|---:|
| `@genlang_word_aelrin` | AELRIN — persistent topology / mountain | COMPOUND_WORD | 0 | 2 | 0 |
| `@genlang_word_darin` | DARIN — persistent occupancy / village | COMPOUND_WORD | 0 | 2 | 0 |
| `@genlang_word_genkor` | GENKOR — Genesis collapse | COMPOUND_WORD | 0 | 2 | 0 |
| `@genlang_word_genkoren` | GENKOREN — Genesis collapse identity / ELDRIS | COMPOUND_WORD | 0 | 3 | 0 |
| `@genlang_word_genvel` | GENVEL — Genesis Field | COMPOUND_WORD | 2 | 2 | 0 |
| `@genlang_word_kai_ar_en_rin` | KAI-AR-EN-RIN — bound inherited persistent identity | COMPOUND_WORD | 2 | 4 | 0 |
| `@genlang_word_kaisha` | KAISHA — configuration boundary / binding circle | COMPOUND_WORD | 2 | 2 | 0 |
| `@genlang_word_koren` | KOREN — collapse identity / realized identity | COMPOUND_WORD | 2 | 2 | 0 |
| `@genlang_word_relrin` | RELRIN — persistent relationship / friend | COMPOUND_WORD | 2 | 2 | 0 |
| `@genlang_word_sharin` | SHARIN — persistent boundary / home | COMPOUND_WORD | 3 | 2 | 0 |
| `@genlang_word_shator` | SHATOR — closed or controlled boundary / gate | COMPOUND_WORD | 3 | 2 | 0 |
| `@genlang_word_talrin` | TALRIN — stabilized persistence / strength | COMPOUND_WORD | 3 | 2 | 0 |
| `@genlang_word_verin` | VERIN — persistent propagation path / road | COMPOUND_WORD | 3 | 2 | 0 |
| `@genesis_grammar` | @genesis_grammar | GRAMMAR_OR_LANGUAGE_ROOT | 0 | 0 | 0 |
| `@genesis_language` | @genesis_language | GRAMMAR_OR_LANGUAGE_ROOT | 0 | 0 | 0 |
| `@genlang_relationship_first_grammar` | Relationship-First Grammar | GRAMMAR_OR_LANGUAGE_ROOT | 0 | 0 | 0 |
| `@geometry_as_prime_api_language` | `@geometry_as_prime_api_language` — Geometry as Prime API Language | GRAMMAR_OR_LANGUAGE_ROOT | 0 | 0 | 0 |
| `@natural_language_invocation` | `@natural_language_invocation` — Natural-Language Invocation | GRAMMAR_OR_LANGUAGE_ROOT | 0 | 0 | 0 |
| `@source_genesis_grammar_v0_1` | @source_genesis_grammar_v0_1 | GRAMMAR_OR_LANGUAGE_ROOT | 0 | 0 | 0 |
| `@genlang_operator_0df59a22` | Architect operator ·°· — Closure | OPERATOR | 0 | 1 | 1 |
| `@genlang_operator_1e07893e` | Architect operator .·· .° — Redistribute | OPERATOR | 2 | 1 | 1 |
| `@genlang_operator_1ff31b3c` | Architect operator ■ .· ■ — Normalize | OPERATOR | 2 | 1 | 1 |
| `@genlang_operator_395625ec` | Architect operator ·· — Propagate | OPERATOR | 2 | 1 | 1 |
| `@genlang_operator_4b1f23a7` | Architect operator ··° ·° — Destabilize | OPERATOR | 0 | 1 | 1 |
| `@genlang_operator_be1cbb61` | Architect operator .°. — Stabilize | OPERATOR | 0 | 1 | 1 |
| `@genlang_operator_edec7353` | Architect operator .· — Inherit | OPERATOR | 1 | 1 | 1 |
| `@genlang_architect_genesis_register` | Architect Genesis Register | REGISTER | 0 | 0 | 0 |
| `@genlang_common_genesis_register` | Common Genesis Register | REGISTER | 0 | 0 | 0 |
| `@genlang_poetic_genesis_register` | Poetic Genesis Register | REGISTER | 0 | 0 | 0 |
| `@genlang_scholar_genesis_register` | Scholar Genesis Register | REGISTER | 0 | 0 | 0 |
| `@genesis_expression` | @genesis_expression | RELATED_LANGUAGE_OBJECT | 0 | 0 | 0 |
| `@genlang_boundary_based_pronouns` | Boundary-Based Pronouns | RELATED_LANGUAGE_OBJECT | 0 | 0 | 0 |
| `@genlang_boundary_inclusion_possession` | Boundary Inclusion Possession | RELATED_LANGUAGE_OBJECT | 0 | 0 | 0 |
| `@genlang_resolution_state_aspect` | Resolution-State Aspect | RELATED_LANGUAGE_OBJECT | 0 | 0 | 0 |
| `@genlang_structural_compounding` | Structural Compounding | RELATED_LANGUAGE_OBJECT | 0 | 0 | 0 |
| `@genlang_phrase_en_ar_en` | EN AR EN — Identity inherits identity / remain yourself | RELATION_FIRST_PHRASE | 0 | 2 | 1 |
| `@genlang_phrase_gen_kor_en` | GEN KOR EN — Genesis collapses into identity | RELATION_FIRST_PHRASE | 0 | 3 | 1 |
| `@genlang_phrase_rin_tal_ael` | RIN TAL AEL — Persistence stabilizes topology | RELATION_FIRST_PHRASE | 0 | 3 | 1 |
| `@genlang_phrase_sha_da_rel` | SHA DA REL — Boundary occupancy relationship | RELATION_FIRST_PHRASE | 0 | 3 | 1 |
| `@genlang_phrase_vel_ve_tor` | VEL VE TOR — Field propagation closure | RELATION_FIRST_PHRASE | 0 | 3 | 1 |
| `@genlang_aspect_ma` | -MA — potential / unresolved | RESOLUTION_ASPECT | 2 | 0 | 1 |
| `@genlang_aspect_nai` | -NAI — failed / absent / broken / negated | RESOLUTION_ASPECT | 2 | 0 | 1 |
| `@genlang_aspect_ru` | -RU — ongoing / propagating | RESOLUTION_ASPECT | 2 | 0 | 1 |
| `@genlang_aspect_ta` | -TA — completed / resolved / closed | RESOLUTION_ASPECT | 1 | 0 | 1 |
| `@genlang_root_ael` | Genesis root AEL — Topology | ROOT | 0 | 3 | 4 |
| `@genlang_root_ar` | Genesis root AR — Inheritance | ROOT | 1 | 1 | 3 |
| `@genlang_root_arka` | Genesis root ARKA — Architect | ROOT | 0 | 0 | 0 |
| `@genlang_root_da` | Genesis root DA — Occupancy | ROOT | 2 | 3 | 4 |
| `@genlang_root_en` | Genesis root EN — Identity | ROOT | 0 | 3 | 7 |
| `@genlang_root_era` | Genesis root ERA — Environment | ROOT | 0 | 1 | 1 |
| `@genlang_root_gen` | Genesis root GEN — Genesis | ROOT | 0 | 1 | 5 |
| `@genlang_root_kai` | Genesis root KAI — Configuration | ROOT | 0 | 1 | 3 |
| `@genlang_root_kor` | Genesis root KOR — Collapse / Realization | ROOT | 0 | 3 | 6 |
| `@genlang_root_nae` | Genesis root NAE — Basin / Expression | ROOT | 0 | 1 | 1 |
| `@genlang_root_nor` | Genesis root NOR — Normalization | ROOT | 2 | 1 | 1 |
| `@genlang_root_rel` | Genesis root REL — Relationship | ROOT | 0 | 3 | 4 |
| `@genlang_root_rin` | Genesis root RIN — Persistence | ROOT | 0 | 3 | 10 |
| `@genlang_root_sera` | Genesis root SERA — Continuity | ROOT | 0 | 3 | 2 |
| `@genlang_root_sha` | Genesis root SHA — Boundary | ROOT | 0 | 3 | 6 |
| `@genlang_root_tal` | Genesis root TAL — Stabilization | ROOT | 0 | 3 | 4 |
| `@genlang_root_tor` | Genesis root TOR — Closure | ROOT | 0 | 3 | 4 |
| `@genlang_root_vara` | Genesis root VARA — Storm / Instability Event | ROOT | 0 | 0 | 0 |
| `@genlang_root_ve` | Genesis root VE — Propagation | ROOT | 1 | 3 | 4 |
| `@genlang_root_vel` | Genesis root VEL — Field | ROOT | 0 | 3 | 5 |
| `@genlang_family_ae` | Genesis root family AE — authority / inheritance / active continuity / projection | ROOT_FAMILY | 0 | 0 | 0 |
| `@genlang_family_ael` | Genesis root family AEL — topology / structure / geometry | ROOT_FAMILY | 1 | 1 | 2 |
| `@genlang_family_ai` | Genesis root family AI — reception / containment / internal continuity / dependency | ROOT_FAMILY | 0 | 0 | 0 |
| `@genlang_family_da` | Genesis root family DA — occupancy / presence / inhabitation | ROOT_FAMILY | 1 | 1 | 2 |
| `@genlang_family_en` | Genesis root family EN — identity / self-state / realized existence | ROOT_FAMILY | 1 | 1 | 2 |
| `@genlang_family_kor` | Genesis root family KOR — collapse / realization / resolution / identity formation | ROOT_FAMILY | 1 | 1 | 2 |
| `@genlang_family_na` | Genesis root family NA — expression / manifestation / basin state | ROOT_FAMILY | 0 | 0 | 0 |
| `@genlang_family_rel` | Genesis root family REL — relationship / connection / adjacency | ROOT_FAMILY | 0 | 1 | 2 |
| `@genlang_family_rin` | Genesis root family RIN — persistence / duration / stability through time | ROOT_FAMILY | 0 | 1 | 2 |
| `@genlang_family_sera` | Genesis root family SERA — continuity / source / cause / flow | ROOT_FAMILY | 0 | 1 | 2 |
| `@genlang_family_sha` | Genesis root family SHA — boundary / containment / location / separation | ROOT_FAMILY | 0 | 1 | 2 |
| `@genlang_family_tal` | Genesis root family TAL — stabilization / retention / resistance | ROOT_FAMILY | 0 | 1 | 2 |
| `@genlang_family_tor` | Genesis root family TOR — closure / completion / fulfillment | ROOT_FAMILY | 0 | 1 | 2 |
| `@genlang_family_ve` | Genesis root family VE — propagation / travel / direction | ROOT_FAMILY | 0 | 1 | 2 |
| `@genlang_family_vel` | Genesis root family VEL — field / environment / propagation medium | ROOT_FAMILY | 0 | 1 | 2 |
| `@genlang_architect_script` | Architect Script | SCRIPT | 0 | 0 | 0 |
| `@genlang_borrowed_script` | Borrowed Script | SCRIPT | 0 | 0 | 0 |
| `@genlang_flow_script` | Flow Script | SCRIPT | 0 | 0 | 0 |
