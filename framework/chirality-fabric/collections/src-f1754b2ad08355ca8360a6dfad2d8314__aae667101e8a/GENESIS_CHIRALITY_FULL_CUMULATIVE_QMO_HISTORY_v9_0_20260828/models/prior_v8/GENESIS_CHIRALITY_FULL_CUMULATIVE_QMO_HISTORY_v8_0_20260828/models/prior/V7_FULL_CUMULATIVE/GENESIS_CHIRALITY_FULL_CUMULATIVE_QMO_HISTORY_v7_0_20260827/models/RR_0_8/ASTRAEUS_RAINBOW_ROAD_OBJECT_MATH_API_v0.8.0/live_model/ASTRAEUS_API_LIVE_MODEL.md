# ASTRAEUS API LIVE MODEL

**Release:** 0.5.0  
**Live model revision:** v0.18.0  
**Root QMO:** `@rainbow_road_recursive_domain`  
**Domain:** Rainbow Road / Möbius recursive carrier

## Purpose

The API and the live model are deliberately different surfaces of one mathematical object. The API is operational: it resolves QMO addresses, traverses typed dependencies, executes recursive closure, runs perturbation tests, and maintains certified internal derivations. The live model is semantic: it records what the API is, what each QMO means, how it is related, where it came from, what state it is in, and how its earlier state can be recovered.

## QMO-addressed metadata library

Each canonical QMO handle is its own metadata address. No second numerical identifier is required.

`@qmo_handle -> mathematical object + current semantic metadata + append-only metadata history`

The handle remains stable when status or interpretation changes. Revisions change the metadata attached to the address; they do not silently create a replacement object. Aliases resolve to the canonical QMO address.

## Metadata contract

- definition / meaning
- mathematical type and native branch
- current status and audit state
- aliases
- typed incoming/outgoing dependency relations
- equation/theorem/candidate/frontier membership
- closure certificate and promotion state
- source provenance
- recovery/history policy
- API release and live-model revision

## Runtime synchronization

Any canonical status mutation must update the addressed metadata record and append a metadata-history event. A readout may suppress structure; the live model must not silently erase the upstream semantic/provenance state needed to recover what the QMO meant at an earlier Road state.

## Global state

- QMO addresses: **187**
- typed edges: **149**
- equations: **15**
- theorems: **3**
- current mathematics frontier: `@recovery_history_signature_minimality`
- Road presentation: `WHITE_SUPERPOSE`
- Road History token: `RRH-bc7705935863`

## QMO inventory

| Address | Type | Branch | Status | Meaning |
|---|---|---|---|---|
| `@adjoint_transduction_audit` | audit architecture | transduction_geometry | PROMOTED_CANDIDATE | Unit/counit and defect framework for forward realization vs backward restriction/readback. |
| `@admissibility_relation` | structural relation | transduction_geometry | MAJOR_PROMOTION | Compatibility relation Adm_f(x,y) defining admissible continuation along dependency arrows. |
| `@admissible_lift_family` | lift structure | transduction_geometry | PROMOTED_CANDIDATE | Family LiftSet(f,x) of structurally admissible typed lifts before connection selection. |
| `@analogy_moebius_gluing` | analogy | transduction_geometry | TYPED_ANALOGY | Möbius gluing illustrates locally simple data with globally nontrivial transition structure. |
| `@analogy_moebius_holonomy` | analogy | transduction_geometry | TYPED_ANALOGY | Möbius loop transport illustrates nontrivial holonomy with preserved base identity. |
| `@analogy_moebius_identity_history` | analogy | transduction_geometry | TYPED_ANALOGY | Möbius recurrence illustrates same identity with changed presentation/history. |
| `@bandwidth` | capacity/admissible-morphism structure | transduction_geometry | RECOVERED_PLUS_LIFT | Available organizational freedom; in GTG, the currently supportable morphism/deformation family. |
| `@bandwidth_algebra` | typed partial path/category-like algebra | bandwidth_algebra | FORMAL_LIVE_MODEL_V1 | Closure of Bandwidth-admissible typed transformation generators under admissible composition and identities. |
| `@bandwidth_compose` | bandwidth algebra operator | bandwidth_algebra | SOURCE_BACKED | Native Bandwidth Algebra operator: compose. |
| `@bandwidth_descent_defect` | audit defect | transduction_geometry | PROMOTED_AUDIT_OBJECT | Mismatch between translated available-morphism families across overlap. |
| `@bandwidth_domain_repair` | continuity repair | live_model | DERIVED | Restrict the operative modifier to a subdomain respecting active Resolution equivalence. |
| `@bandwidth_expand` | bandwidth algebra operator | bandwidth_algebra | SOURCE_BACKED | Native Bandwidth Algebra operator: expand. |
| `@bandwidth_identity` | bandwidth algebra operator | bandwidth_algebra | SOURCE_BACKED | Native Bandwidth Algebra operator: identity. |
| `@bandwidth_join` | bandwidth algebra operator | bandwidth_algebra | SOURCE_BACKED | Native Bandwidth Algebra operator: join. |
| `@bandwidth_meet` | bandwidth algebra operator | bandwidth_algebra | SOURCE_BACKED | Native Bandwidth Algebra operator: meet. |
| `@bandwidth_modifier` | typed Bandwidth transformation | live_model | DERIVED | Restriction, expansion, redirection, or mixed Bandwidth transformation M:A_B->A_B'. |
| `@bandwidth_modify` | bandwidth algebra operator | bandwidth_algebra | SOURCE_BACKED | Native Bandwidth Algebra operator: modify. |
| `@bandwidth_resolution_interface_defect` | structural defect set | live_model | DERIVED | Pairs hidden together at source Resolution whose Bandwidth-modified targets become distinguishable. |
| `@bandwidth_resolution_quotient` | bandwidth algebra operator | bandwidth_algebra | SOURCE_BACKED | Native Bandwidth Algebra operator: resolution_quotient. |
| `@bandwidth_restrict` | bandwidth algebra operator | bandwidth_algebra | SOURCE_BACKED | Native Bandwidth Algebra operator: restrict. |
| `@blast_radius` | impact metric | transduction_geometry | MAJOR_PROMOTION | Typed downstream impact distribution for revision/rejection of a handle. |
| `@bottleneck` | resilience concept | transduction_geometry | MAJOR_PROMOTION | Scope-relative high-path-participation dependency with low bypass redundancy. |
| `@bridge_point` | resilience concept | transduction_geometry | MAJOR_PROMOTION | Architectural connector whose removal fragments graph regions. |
| `@chirality` | admissibility/orientation structure | transduction_geometry | RECOVERED_PLUS_LIFT | Organizational chirality and transported chirality class used in identity and local admissibility. |
| `@chirality_fabric` | distributed admissibility/gluing candidate | transduction_geometry | STRONG_CANDIDATE | Candidate: local admissibility objects + overlap transition maps + descent compatibility. |
| `@chirality_localization_action` | binary localization action | identity_through_history | ATLAS_CANDIDATE | Lambda_chi |
| `@chirality_state` | holonomy/chirality record | holonomy_chirality | SOURCE_BACKED | Record fields: domain, state, chirality_class, provenance |
| `@choke_point` | resilience concept | transduction_geometry | MAJOR_PROMOTION | Bottleneck with high blast radius and low alternative support. |
| `@circularity_audit` | audit engine | transduction_geometry | MAJOR_PROMOTION | Rejects promotion-bearing evidentiary cycles while permitting non-evidentiary graph cycles. |
| `@classifier_scope` | classification scope contract | transduction_geometry | MAJOR_PROMOTION | Declares object class, equivalence relation, base, structure group/groupoid, Resolution, regularity and operative conditions for a classifier claim. |
| `@closed_domain_unity` | whole-domain closure object | rainbow_runtime | ACTIVE_DOMAIN_CONSTRAINT | Identity of one closed whole-domain under the declared closure/identity rule; glyph 1 remains a symbolic label. |
| `@closure` | stabilization/identity-formation candidate | transduction_geometry | STRENGTHENED_CANDIDATE | Stabilization/retraction candidate; may preserve or form/select identity. |
| `@closure_certificate` | derivation certificate | rainbow_runtime | DOMAIN_ACTIVE | Machine-auditable witness that an output is an internal consequence of admitted objects and licensed transformations with intact provenance/recovery and no d... |
| `@closure_equivariance_defect` | structural defect | rainbow_runtime | DERIVED_DOMAIN_RULE | Mismatch between closing a structure before versus after an admitted Möbius/readout handoff, after accounting for the typed transformed presentation. |
| `@compatibility` | allowed relation structure | live_model | STORY_PROBE_SOURCE | Structure of which possibilities can meaningfully connect; retained as probe guidance, not a numerical object. |
| `@component_salvage_protocol` | method | transduction_geometry | MAJOR_PROMOTION | Decompose legacy mathematics into independently reusable components without whole-object lock-in. |
| `@connection_selection` | holonomy/chirality record | holonomy_chirality | SOURCE_BACKED | Record fields: arrow, state, R, B, H, E, chi, selected_lift, selection_witness, status |
| `@constraint_perturbation` | perturbation class | rainbow_runtime | DOMAIN_ACTIVE | Change to an upstream admissibility/constraint object; may propagate through all dependent structures during sandbox reclosure. |
| `@core_witness_collision` | recovery counterexample defect | self_build | DERIVED_CLOSED_INTERNAL | A merge-fiber collision in which distinct fine lineages have the same unqualified core witness projection (provenance root, Identity-Witness class, invariant... |
| `@counit_defect` | audit defect | transduction_geometry | PROMOTED_AUDIT_OBJECT | Typed discrepancy between f! f* y and y. |
| `@cross_resolution_section` | compatible family | live_model | SOURCE_BACKED_SYNTHESIS | Family s_a(R)=rho_R(a) compatible under declared Resolution handoffs. |
| `@dependency_category` | typed category | transduction_geometry | PROMOTED_CANDIDATE | Base category of dependency contexts and typed composable arrows. |
| `@dependency_cone` | dependency object | transduction_geometry | MAJOR_PROMOTION | Typed upstream/downstream dependency cone for a QMO handle. |
| `@dependency_cone_snapshot` | snapshot object | transduction_geometry | MAJOR_PROMOTION | Versioned dependency-cone snapshot for historical recoverability. |
| `@dependency_criticality` | dependency taxonomy | transduction_geometry | MAJOR_PROMOTION | Classifies dependency edges by invalidation significance. |
| `@dependency_cut_set` | resilience diagnostic | transduction_geometry | MAJOR_PROMOTION | Candidate minimal upstream cut whose removal destroys all valid routes. |
| `@derivation_error_taxonomy` | error taxonomy | transduction_geometry | MAJOR_PROMOTION | Typed error classes for malformed or unresolved derivations. |
| `@derivation_macro` | higher-order derivation operator | transduction_geometry | MAJOR_PROMOTION | Reusable typed abstraction of a compiler-valid derivation path. |
| `@derivation_metadata_package` | metadata package | transduction_geometry | MAJOR_PROMOTION | Automatically extracted typed metadata for a derivation path. |
| `@derivation_path` | derivation object | transduction_geometry | MAJOR_PROMOTION | Ordered compiler-witnessed path through QMO objects/operators. |
| `@derivation_provenance_chain` | provenance object | transduction_geometry | MAJOR_PROMOTION | Step-level ordered provenance chain for a derivation. |
| `@derivation_salvage` | salvage method | transduction_geometry | MAJOR_PROMOTION | Preserves valid prefixes/fragments of failed derivations. |
| `@descent_defect` | audit defect | transduction_geometry | PROMOTED_AUDIT_OBJECT | Triple-overlap failure D_ijk = g_ij g_jk g_ki. |
| `@domain_extension_proposal` | boundary-change proposal | rainbow_runtime | AUDIT_REQUIRED | Any proposed primitive, axiom, transformation, or closure-rule change not derivable within the current domain; cannot self-promote. |
| `@dual_impact_status` | impact object | transduction_geometry | MAJOR_PROMOTION | Separates mathematical-validity impact from trust/evidence impact. |
| `@dynamic_recursive_closure` | closure operator | rainbow_runtime | DERIVED_DOMAIN_RULE | Cl_RR closes admitted internal derivations back into the current Rainbow Road domain; reopens when Bandwidth, Resolution, source corpus, licensed rules, or a... |
| `@eventual_recoverability` | access/recovery predicate | live_model | CANDIDATE | A structure need not be readable now if retained provenance permits recovery in some admissible resolving regime. |
| `@evolution_descent_defect` | audit defect | transduction_geometry | PROMOTED_AUDIT_OBJECT | Mismatch between evolve-then-translate and translate-then-evolve. |
| `@fabric_equivalence_test` | classification audit | transduction_geometry | PROMOTED_CANDIDATE | Scope-aware test determining whether two fabric signatures represent equivalent global fabrics under the declared classifier scope. |
| `@fabric_signature` | scope-aware classifier signature | transduction_geometry | MAJOR_PROMOTION | Composite global-fabric classification signature containing local type, gluing, connection, holonomy, curvature, descent, topology and stratum metadata. |
| `@failed_derivation` | research metadata type | transduction_geometry | MAJOR_PROMOTION | Recoverable rejected derivation with failing rule and provenance. |
| `@fine_lineage_selector` | self-build candidate object | self_build | CANDIDATE | A witness-mediated selector over a handoff merge fiber; it is not an inverse to q_ji and may be partial/context-dependent. |
| `@formal_identity` | identity layer | live_model | ACTIVE | Underlying identity class retained across presentation changes. |
| `@formal_lift_family` | lift structure | transduction_geometry | MAJOR_PROMOTION | Formal family LiftSet(f,x) of all structurally admissible lifts. |
| `@formal_object` | formal mathematical object | live_model | ACTIVE | Recoverable mathematical object with Formal Identity, presentations, admissible transformations, Resolution views, and provenance. |
| `@fragility_vector` | resilience vector | transduction_geometry | MAJOR_PROMOTION | Single-point, unresolved, candidate, semantic, trust and blast-radius fragility profile. |
| `@genesis` | organizational field | transduction_geometry | RECOVERED | Recursive self-inheriting organizational field. |
| `@global_fabric_classifier` | classifier | transduction_geometry | MAJOR_PROMOTION | Current classifier using local type, gluing class, and holonomy conjugacy data. |
| `@global_transduction_object` | total category | transduction_geometry | MAJOR_PROMOTION | Grothendieck-construction-like total category assembling dependency contexts and indexed state geometries. |
| `@gluing_class` | equivalence class | transduction_geometry | PROMOTED_CANDIDATE | Transition-data equivalence class under local reparameterization. |
| `@gluing_data` | transition data | transduction_geometry | PROMOTED_CANDIDATE | Representative local transition maps plus their equivalence/gauge class for reconstruction and descent auditing. |
| `@handoff_merge_fiber` | non-injective fiber | live_model | DERIVED | Fine presentations identified by one coarse Resolution handoff. |
| `@high_recall_metadata` | metadata policy | transduction_geometry | MAJOR_PROMOTION | Capture formal and exploratory research metadata at high recall, preserving type/status/provenance. |
| `@history` | path/provenance ledger | transduction_geometry | PROMOTED_CANDIDATE | Path through the total transduction object; layered projections recover fiber/orbit/stratum histories. |
| `@history_bearing_return` | continuity result | rainbow_runtime | DERIVED_CLOSED_INTERNAL | Return to a prior local presentation after recursive traversal while retaining a distinct recoverable History state. |
| `@history_holonomy` | closed-path witness transformation | identity_through_history | SOURCE_BACKED | closed-path witness transformation |
| `@history_path` | composable_path | identity_through_history | SOURCE_BACKED | composable_path |
| `@history_trace` | ordered traversal record | live_model | ACTIVE | Ordered structurally relevant traversal/provenance retained upstream. |
| `@history_trace_counterexample_sufficiency` | derived recovery result | self_build | DERIVED_CLOSED_INTERNAL | For CE-RW-001, adjoining the distinct ordered History token to the colliding core witness separates the two fine lineages. This proves sufficiency for the co... |
| `@history_transport` | witness transport | identity_through_history | BRACED | witness transport |
| `@holonomy_class` | conjugacy invariant | transduction_geometry | PROMOTED_CANDIDATE | Conjugacy class of loop holonomy induced by gluing/connection transport. |
| `@holonomy_history_signature` | history/holonomy signature scaffold | holonomy_chirality | SOURCE_BACKED_SCAFFOLD | Source-backed D57 scaffold for a History-sensitive signature carried by holonomy/transport structure; exact minimal sufficient signature remains open. |
| `@holonomy_record` | holonomy/chirality record | holonomy_chirality | SOURCE_BACKED | Record fields: loop, type, transport_action, equivalence_scope, defect, visibility_by_resolution, provenance |
| `@identity_base` | stratified moduli-like orbit space | transduction_geometry | MAJOR_PROMOTION | Coarse global base of identity classes/strata. |
| `@identity_groupoid` | higher identity quotient | transduction_geometry | PROMOTED_CANDIDATE | Full identity geometry retaining equivalence arrows and isotropy. |
| `@identity_holonomy_defect` | identity-return defect | identity_through_history | SOURCE_BACKED | identity-return defect |
| `@identity_invariant` | identity tuple | transduction_geometry | MAJOR_RESULT | Continuation ancestry class + transported chirality class + invariant residue. |
| `@identity_orbit` | orbit | transduction_geometry | PROMOTED_CANDIDATE | Admissible identity-preserving orbit of developmental/presentation states. |
| `@identity_sensitivity` | holonomy/chirality record | holonomy_chirality | SOURCE_BACKED | Record fields: identity_classifier, chirality_defect_class, sensitive, witness |
| `@identity_stratum` | orbit-type stratum | transduction_geometry | PROMOTED_CANDIDATE | Structural class containing identity orbits with common isotropy/invariant type. |
| `@identity_witness` | recoverable witness relation | identity_through_history | SOURCE_BACKED | recoverable witness relation |
| `@impact_ledger` | change ledger | transduction_geometry | MAJOR_PROMOTION | Records propagation and revalidation effects of significant revisions. |
| `@internal_self_promotion` | closure transition | rainbow_runtime | DOMAIN_ACTIVE | Automatic transition from generated/candidate to internally closed derived mathematics when a complete Closure Certificate validates inside the current domain. |
| `@invariant_residue` | preserved structural residue | live_model | ACTIVE | Declared recoverable organizational content preserved under admissible projection/transport. |
| `@language_missing` | coverage status | transduction_geometry | PROMOTED_RULE | Marker for QMO objects lacking curated language entries. |
| `@language_orphan` | coverage status | transduction_geometry | PROMOTED_RULE | Marker for language terms lacking QMO mathematical handles unless explicitly exempted. |
| `@language_sync_engine` | synchronization engine | transduction_geometry | MAJOR_PROMOTION | Generates/checks semantic language entries against the live QMO object and edge graph. |
| `@lift_coherence_audit` | lift audit | transduction_geometry | PROMOTED_CANDIDATE | Compares composite lift with sequential lift up to declared equivalence. |
| `@lift_composition_coherence` | coherence audit | transduction_geometry | MAJOR_PROMOTION | Compares sequential and composite structural lifting. |
| `@lift_defect` | lift audit | transduction_geometry | PROMOTED_CANDIDATE | Typed failure/nonuniqueness/coherence disposition for lift existence. |
| `@lift_family` | holonomy/chirality record | holonomy_chirality | SOURCE_BACKED | Record fields: arrow, source_state, formal_lifts, bandwidth_available_lifts, status |
| `@macro_connection_to_holonomy` | derivation macro | transduction_geometry | MAJOR_PROMOTION | Connection-selected closed-path transport to holonomy diagnostic. |
| `@macro_dependency_graph` | dependency graph | transduction_geometry | MAJOR_PROMOTION | Tracks macro expansion, use, composition, specialization and invalidation. |
| `@macro_descent_audit` | derivation macro | transduction_geometry | MAJOR_PROMOTION | Overlap-transition composition to descent/global-gluing disposition. |
| `@macro_path_curvature_audit` | derivation macro | transduction_geometry | MAJOR_PROMOTION | Same-endpoint transport comparison to typed curvature defect. |
| `@minimal_fabric_signature` | classifier core | transduction_geometry | MAJOR_PROMOTION | Minimal current fabric signature: LocalType + GluingData + ConnectionClass + ClassifierScope. |
| `@mobius_orientation_handoff` | presentation handoff | rainbow_runtime | DERIVED_DOMAIN_RULE | Local readout handoff H between White/superpose and Black/neon presentations of the same Rainbow Road whole-domain carrier. |
| `@mobius_probe` | test instrument | live_model | PARKED_PROBE | Topology probe retained only when an object/continuity question requires it. |
| `@mobius_recursive_carrier` | recursive presentation carrier | rainbow_runtime | DOMAIN_ACTIVE | Möbius carrier used as the local presentation/return geometry of Rainbow Road: one traversal changes local orientation; a second returns local orientation wi... |
| `@moebius_monodromy` | holonomy special case | transduction_geometry | STRENGTHENED_CANDIDATE | Closed-loop transport example preserving base identity while presentation/history may change. |
| `@number_ontology` | downstream interpretation | live_model | PARKED | Classification of objects as numbers is not required by the active object-first program. |
| `@object_mathematics` | program root | live_model | ACTIVE | Mathematical objects are studied without requiring prior classification as numbers. |
| `@object_resolution_recovery_witness_minimality` | research frontier | live_model | ACTIVE_FRONTIER | Find the smallest witness/provenance structure selecting the correct fine lineage from a non-injective Resolution handoff. |
| `@objectivity` | objectivity/readability condition | live_model | CANDIDATE | Objectivity supplies a domain in which structure can become distinguishable without requiring number ontology. |
| `@observational_identity` | resolution/readout object | resolution_readout | SOURCE_BACKED | Obs_R |
| `@occupancy` | realized state | transduction_geometry | PROMOTED_CANDIDATE | The actually realized object/section among supportable possibilities. |
| `@operative_lift_family` | lift structure | transduction_geometry | MAJOR_PROMOTION | Bandwidth-restricted subset of the formal lift family. |
| `@operator_signature` | operator type contract | transduction_geometry | MAJOR_PROMOTION | Input/output/preservation/change/requirement contract for mathematical operators. |
| `@persistence` | identity-preservation criterion | transduction_geometry | PROMOTED_CANDIDATE | Preservation/recovery of organizational identity under admissible development and transport. |
| `@persistence_closure_native` | identity-stable algebraic closure | identity_through_history | ATLAS_CANDIDATE | Cl_P |
| `@perturbation_probe` | sandbox consistency probe | rainbow_runtime | DOMAIN_ACTIVE | Noncanonical sandbox that injects an alternative object/relation/constraint and recursively propagates dependency consequences to test reclosure or defect fo... |
| `@primitive_structural_zero` | boundary/localization object | rainbow_runtime | SOURCE_BACKED_LIVE_GUARD | Structural boundary object 𝔃 := 0_L \| 0_R; glyph 0 is not presumed numerical. |
| `@provenance` | lineage structure | live_model | ACTIVE | Recoverable ancestry/source/derivation trace. |
| `@provenance_repair` | continuity repair | live_model | DERIVED | Carry the Identity/History witness selecting the correct formal representative. |
| `@qmo_review_graph` | review graph | transduction_geometry | MAJOR_PROMOTION | Quarantine graph for unresolved or uncertain candidate derivations. |
| `@quotient` | resolution/readout object | resolution_readout | SOURCE_BACKED | A_B/K_R |
| `@rainbow_road_probe` | test instrument | live_model | PARKED_PROBE | Bounded-domain probe for presentation, History, Resolution, and continuity; not the research endpoint. |
| `@rainbow_road_recursive_domain` | dynamic recursive closure domain | rainbow_runtime | DOMAIN_ACTIVE | Bounded working domain whose mathematical objects, derivations, readouts, Bandwidth states, Resolution states, and History recursively re-enter one recoverab... |
| `@readable_geometry` | resolution/readout object | resolution_readout | SOURCE_BACKED | Geo_R(B)=Spec_T(A_B/K_R) |
| `@readout_perturbation` | perturbation class | rainbow_runtime | DOMAIN_ACTIVE | Change to a downstream label/readout only; does not by itself license rewriting unrelated upstream structure. |
| `@reclosure_branch` | sandbox branch | rainbow_runtime | DOMAIN_ACTIVE | Isolated alternative closure branch created by a perturbation. It never overwrites canonical state merely because it reaches a fixed point. |
| `@recovery_discriminator` | derived recovery witness component | self_build | DERIVED_CLOSED_INTERNAL | Any retained witness component d such that augmenting a colliding witness map by d separates the recovery-relevant lineages in the handoff merge fiber. |
| `@recovery_history_signature_minimality` | self-build research frontier | self_build | ACTIVE_FRONTIER | Determine whether full ordered History can be replaced by a smaller retained History/holonomy signature that remains separating on every recovery-relevant ha... |
| `@recovery_provenance_bundle` | witness bundle | live_model | OPEN | Unknown minimal retained structure sufficient to recover the correct fine lineage after a non-injective handoff. |
| `@recovery_witness_counterexample_crawl` | self-build research frontier | self_build | ACTIVE_FRONTIER | Can the smallest candidate witness bundle fail to distinguish two fine-resolution lineages in the same non-injective handoff fiber, and if so, exactly which ... |
| `@recursive_dependency_grammar` | generative grammar | transduction_geometry | MAJOR_PROMOTION | Object + typed arrow + composition + identity + quotient/refinement across abstraction levels. |
| `@recursive_impact_cone` | dependency impact structure | rainbow_runtime | DERIVED_DOMAIN_RULE | Dependency descendants whose derivation or validity may require recomputation after a perturbation. This is a structural cone, not a foundational numerical m... |
| `@redundancy_vector` | resilience vector | transduction_geometry | MAJOR_PROMOTION | Route, alternative-dependency, provenance and macro redundancy profile. |
| `@research_pareto_frontier` | priority structure | transduction_geometry | PROMOTED_CANDIDATE | Non-dominated research targets under declared priority dimensions. |
| `@research_priority_operator` | research scheduler | transduction_geometry | PROMOTED_CANDIDATE | Multi-objective operator selecting high-value unresolved mathematical targets. |
| `@research_priority_vector` | priority vector | transduction_geometry | PROMOTED_CANDIDATE | Impact/fragility/discharge/redundancy/scope/recoverability/cost/circularity/novelty profile. |
| `@research_queue` | research queue | transduction_geometry | PROMOTED_CANDIDATE | Typed generated research actions. |
| `@resolution` | readout/refinement structure | transduction_geometry | RECOVERED_PLUS_LIFT | Distinguishable organization; in GTG, a readout that preserves or forgets distinctions. |
| `@resolution_blind_core` | resolution kernel intersection | live_model | SOURCE_BACKED | Structure invisible at every Resolution in the currently modeled family. |
| `@resolution_congruence` | resolution/readout object | resolution_readout | SOURCE_BACKED | K_R |
| `@resolution_descent_defect` | audit defect | transduction_geometry | PROMOTED_AUDIT_OBJECT | Mismatch between Resolution readout and overlap translation. |
| `@resolution_domain` | resolution/readout object | resolution_readout | SOURCE_BACKED | Dom_R([x]_R)=q_R^{-1}([x]_R) |
| `@resolution_equivalence` | resolution/readout object | resolution_readout | SOURCE_BACKED | x ~_R y iff q_R(x)=q_R(y) |
| `@resolution_handoff` | cross-resolution map | live_model | DERIVED | Compatible handoff q_ji between fine and coarse Resolution presentations. |
| `@resolution_index` | resolution/readout object | resolution_readout | SOURCE_BACKED | Res |
| `@resolution_landscape` | resolution/readout object | resolution_readout | SOURCE_BACKED | L_R(B)={Geo_R(B),q_ji} |
| `@resolution_quotiented_lift_family` | lift structure | transduction_geometry | MAJOR_PROMOTION | Lift family modulo current Resolution/readout equivalence. |
| `@resolution_repair` | continuity repair | live_model | DERIVED | Refine Resolution until the needed representatives are distinguishable. |
| `@return_not_reset` | continuity theorem object | rainbow_runtime | DERIVED_CLOSED_INTERNAL | A recurrence of local presentation does not identify the current structural-History state with the earlier state when traversal History is retained. |
| `@robustness_map` | resilience map | transduction_geometry | MAJOR_PROMOTION | Layered map of mathematical, trust, semantic, recovery and reasoning robustness. |
| `@robustness_signature` | resilience signature | transduction_geometry | MAJOR_PROMOTION | Multi-dimensional robustness profile combining redundancy, fragility, dependency cones and impact profile. |
| `@semantic_closure_fixed_point` | closure state | rainbow_runtime | DERIVED_DOMAIN_RULE | A mathematical state X* with Cl_RR(X*) structurally equivalent to X* under the current domain contract. History may still grow while semantic closure remains... |
| `@semantic_contradiction_audit` | audit engine | transduction_geometry | MAJOR_PROMOTION | Detects QMO relations or metadata that violate semantic type/conflation constraints. |
| `@semantic_type_system` | semantic type system | transduction_geometry | MAJOR_PROMOTION | Weak type system constraining terminology, relations, status modality and forbidden conflations. |
| `@square_curvature` | holonomy/chirality record | holonomy_chirality | SOURCE_BACKED | Record fields: U, V, W, Z, path_1, path_2, defect, scope, status |
| `@state_fiber` | indexed state groupoid/category | transduction_geometry | PROMOTED_CANDIDATE | Admissible state geometry F(U) over dependency context U. |
| `@status_monotonicity` | status rule | transduction_geometry | MAJOR_PROMOTION | Prevents conclusions from exceeding unresolved/candidate premise status without independent discharge. |
| `@stratum_graph` | directed typed graph | transduction_geometry | PROMOTED_CANDIDATE | Graph of admissible identity-stratum transition classes. |
| `@strong_resolution_handoff_continuity` | recoverability condition | live_model | DERIVED_CANDIDATE | Weak coherence plus common Formal Identity, valid witness, retained essential distinctions, and recoverable lineage. |
| `@structural_discontinuity` | failure predicate | live_model | CANDIDATE | Failure when a structurally essential prior distinction is neither readable nor recoverable. |
| `@support_multiplicity` | support structure | transduction_geometry | MAJOR_PROMOTION | Tracks independent/alternative support routes. |
| `@theory_chirality_fabric_as_admissibility_descent` | theory candidate | transduction_geometry | STRONG_CANDIDATE | Chirality Fabric may be modeled as local admissibility structures plus transition/gluing data. |
| `@time_shell_history_address` | history-bearing persistent boundary address | identity_through_history | ATLAS_CANDIDATE | history-bearing persistent boundary address |
| `@transduction` | typed transformation | transduction_geometry | STRENGTHENED_CANDIDATE | Inheritance-preserving change of realization; globally a morphism with base and fiber components. |
| `@transduction_compiler` | derivation compiler | transduction_geometry | MAJOR_PROMOTION | Semantic/operator type checker and QMO admission gate. |
| `@transduction_connection` | connection-like structure | transduction_geometry | MAJOR_PROMOTION | Typed admissibility-aware horizontal-lift selection rule. |
| `@transduction_curvature` | typed path-dependence defect | transduction_geometry | MAJOR_PROMOTION | Coherence defect between same-endpoint connection-selected transports. |
| `@transduction_descent` | descent architecture | transduction_geometry | MAJOR_PROMOTION | Local-to-global gluing architecture for connections/admissibility data. |
| `@transduction_language` | semantic language system | transduction_geometry | MAJOR_PROMOTION | Queryable controlled vocabulary and semantic contract for the Transduction theory. |
| `@transduction_reasoning_grammar` | reasoning grammar | transduction_geometry | MAJOR_PROMOTION | Grammar of admissible reusable derivation procedures over QMO objects. |
| `@transport_path` | holonomy/chirality record | holonomy_chirality | SOURCE_BACKED | Record fields: path, selected_lifts, source, target, history_record |
| `@trust_graph` | trust graph | transduction_geometry | MAJOR_PROMOTION | Typed graph of evidentiary, dependency, descriptive, validation and discharge relations. |
| `@trust_strata` | trust architecture | transduction_geometry | MAJOR_PROMOTION | Classifies evidentiary role/ancestry strata without conflating them with truth ranking. |
| `@trust_witness` | trust object | transduction_geometry | MAJOR_PROMOTION | Explains trust stratum, evidence edges, unresolved/discharged dependencies, independence and provenance. |
| `@typed_analogy_record` | metadata schema | transduction_geometry | MAJOR_PROMOTION | Typed analogy object preserving mapping, utility, break conditions, status and provenance. |
| `@typed_lift_architecture` | lift architecture | transduction_geometry | PROMOTED_CANDIDATE | Cartesian-style restriction lifts and cocartesian-style realization lifts by operator family. |
| `@unit_defect` | audit defect | transduction_geometry | PROMOTED_AUDIT_OBJECT | Typed discrepancy between x and f* f! x. |
| `@weak_resolution_handoff_coherence` | commutation condition | live_model | DERIVED | q_ji(rho_Rj(a)) = rho_Ri(a); presentation consistency only. |
| `@witness_bundle_core` | self-build candidate object | self_build | CANDIDATE | Candidate recovery witness containing formal address/provenance pointer + Identity Witness + transition token + invariant residue. |
| `@witness_bundle_full_state_fallback` | self-build candidate object | self_build | FALLBACK_CANDIDATE | Retain the fuller predecessor structural state when compressed provenance cannot guarantee unique lineage recovery. |
| `@witness_bundle_history_augmented` | self-build candidate object | self_build | CANDIDATE | Core candidate plus explicit ordered History trace. |
| `@witness_fiber_separation_criterion` | recovery theorem object | self_build | DERIVED_CLOSED_INTERNAL | A recovery witness uniquely selects a fine lineage from a non-injective handoff merge fiber exactly when the witness map separates distinct lineages on that ... |


## Dependency Landscape QMO layer

`@dependency_landscape` is now a first-class constructor. It maps one or more QMO/landscape inputs into a typed dependency-network object and, when registered in a freeze, that network itself becomes a QMO.

Current registered landscapes: **3**.

Composition modes:
- QMO ↔ QMO
- QMO ↔ Dependency Landscape
- Dependency Landscape ↔ Dependency Landscape

Each landscape carries its own append-only History, Resolution context, Bandwidth context, roots, member QMO addresses, member edge IDs, and provenance. Landscape membership preserves the current status of the member QMO; it does not promote it.

Use `@help dependency_landscape` for the executable surface.

## Structural Command Namespace — v0.6.0

Canonical discovery is now `@help`. Structural API commands live in `api/COMMAND_REGISTRY.json` and are **not** QMOs by default. The first invocation token resolves against the command registry; later `@...` arguments resolve as QMO/landscape addresses according to the command contract.

This preserves a typed separation:

`@command` = executable structural implementation when used in command position.

`@QMO` = queryable mathematical object when used in object/address position.

`@help` has no QMO record. `@dependency_landscape` is intentionally dual-role: the constructor is a structural command and its mathematical constructor semantics are also represented by a QMO backing object.



## Superseding Dependency Graph / Dependency Chain Layer — 0.7.0

The v0.7 runtime adds three distinct recursive graph objects:

1. `@dependency_graph` — focused registered graph QMO (`path`, `induced`, `ego`).
2. `@dependency_landscape` — recursive/merged network; inputs may now be QMO, Dependency Graph, or Dependency Landscape.
3. `@dependency_chain` — ordered History of repeated crawl -> graph -> landscape -> resolved-QMO steps.

A Dependency Chain stops at one of: `CLOSED_FIXED_POINT`, `OPEN_FRONTIER`, `OPEN_FORK`, `FORK`, `CYCLE_DETECTED`, or `MAX_STEPS`.

A chain is **not** a domain merely because it exists. The same QMO address becomes a closed subdomain only if terminal fixed-point closure and the declared subdomain obligations validate. Open/forked chains remain recoverable queryable objects.

Current example chain:

`@dc_recovery_witness_to_signature`

`@object_resolution_recovery_witness_minimality`
` -> @recovery_witness_counterexample_crawl`
` -> @recovery_history_signature_minimality`

It terminates `OPEN_FORK` on the registered targets `@history_holonomy`, `@holonomy_history_signature`, and `@recovery_discriminator`; therefore it is **not** promoted to a domain.

Current inventory: **199 QMO addresses, 190 typed edges, 2 Dependency Graph QMOs, 6 Dependency Landscape QMOs, 1 Dependency Chain QMO, 37 structural commands.**

Canonical command discovery remains `@help`.


## Black Rainbow / Bounded Iteration Layer — v0.8.0

The closure envelope is now typed separately from the recursive carrier:

- `@black_rainbow_closed_landscape` — closed mathematical landscape / domain envelope.
- `@rainbow_road_recursive_domain` — recursive runtime.
- `@mobius_recursive_carrier` — recursive presentation carrier.

The native mathematical functional `@bounded_recursive_iteration` has recurrence:

`X_(i+1) = Cl_BR(Phi_(B,R)(X_i))`, for `i < N`.

`N` is a maximum iteration/search horizon. Canonical early termination includes target recovery, fixed-point closure, fork, cycle, no-new-structure, hard defect, Bandwidth exhaustion, and domain boundary.

The specialization `@bounded_dependency_crawl` performs bounded dependency exploration over registered QMO structure. Registered runs become History-bearing iteration-run QMOs.

Smoke test `@it_recovery_witness_1m_ceiling` requested a bound of 1,000,000 iterations but executed only 2 before reaching the genuine `OPEN_FORK` at `@recovery_history_signature_minimality`. This confirms that the horizon is a ceiling rather than a forced count.

**Consistency guard:** closed landscape bounds admissible derivation but does not by itself prove consistency. Hard guards, typed transformations, provenance, recovery witnesses, and Closure Certificates remain mandatory.
