# Current API companion mapping

> Current API: [GR/QMO](../../../../../../../api/gr-qmo/00_START_HERE.md). Its supplied [definitions](../../../../../../../api/gr-qmo/INTEGRATION_SPEC.md) and [object dictionary](../../../../../../../api/gr-qmo/INSTALLED_OBJECTS.md) govern current API use. The superseded instructions in this block are retired; no equivalence of old runtime behavior or unprovided mathematics is implied. [Original guide and provenance](provenance://unavailable/content-sha256/131ce093184ac57e691c7ede92218ec829fadade9bf875ef001fd6cd980f895e/DARK_MATTER_2_2_CURRENT_CANONICAL.md).

The following retained sections describe this source collection. Historical implementation examples and domain-specific results are not a claim that GR/QMO implements those older interfaces.

# MK43 DARK MATTER API

> Current API: [GR/QMO](../../../../../../../api/gr-qmo/00_START_HERE.md). Its supplied [definitions](../../../../../../../api/gr-qmo/INTEGRATION_SPEC.md) and [object dictionary](../../../../../../../api/gr-qmo/INSTALLED_OBJECTS.md) govern current API use. The superseded instructions in this block are retired; no equivalence of old runtime behavior or unprovided mathematics is implied. [Original guide and provenance](provenance://unavailable/content-sha256/131ce093184ac57e691c7ede92218ec829fadade9bf875ef001fd6cd980f895e/DARK_MATTER_2_2_CURRENT_CANONICAL.md).

---

# 0. RELEASE RESULT

Dark Matter API 2.1 is the first brute-force-mined formalization in
which the child API contains an explicit mathematical qualification
definition for dark matter.

It does **not** prove that the qualification locus is nonempty.

Status:

```text
qualification definition: CLOSED
source realization: PARTIAL
existence witness: OPEN
empirical identification: OPEN
```

Primary blockers:

```text
@dm_hidden_state_embedding
@dm_metric_action_selection
@dm_dark_matter_qualification_nonempty
```

---

# 1. CURRENT CRITICAL PATH

```text
@dm_mode0_access_interface
@dm_mode0_network_selection_rule
@dm_hidden_s3_network
@dm_hidden_state_bundle
@dm_hidden_state_embedding
@inherited_state_bundle
@dm_formal_persistence_qualification
@persistent_locus
@dm_hidden_persistent_subset
@dm_hidden_boundary_contact
@persistent_boundary
@boundary_projection
@projective_target_manifold
@residue_quantum_field_bundle
@dm_projection_residue_survival
@dm_q_completion_family
@dm_q_survival
@dm_metric_action_selection
@dm_stress_energy_realization_family
@stress_energy_tensor
@dm_hidden_sector_conservation
@dm_stress_energy_separation_gate
@dm_energy_gravity_consistency_filter
@dm_dark_matter_qualification_locus
@dm_dark_matter_qualification_nonempty
```

---

# 2. MAJOR 2.1 CLOSURES

```text
@dm_hidden_boundary_contact
@dm_q_completion_family
@dm_q_survival
@dm_stress_energy_realization_family
@dm_hidden_sector_conservation
@dm_dark_matter_qualification_locus
```

The former broad/open handles have been superseded where appropriate.

---

# 3. OBJECT REGISTRY

## `@dm_chromatic_optional_branch` — Optional Chromatic/Basin Representation Branch

```text
type: OptionalRepresentationBranch
status: OPTIONAL_NOT_CRITICAL_PATH
criticality: optional
```

Historical/downstream chromatic or basin representation route. It is not required for the current persistent-boundary / residue-bundle critical path.

```text
E --chi--> Omega --R_{OmegaC}^R--> X_C^R; R_{OmegaC}^R remains open.
```

## `@dm_continuity_laplacian` — Selected Continuity Graph Laplacian

```text
type: FiniteWeightedLaplacian
status: ATLAS_DERIVED_ACTIVE
criticality: critical
```

Finite algebraic realization of continuity redistribution on a selected network support.

```text
L_N=B_N W_N B_N^T; deltaC=-L_N c.
```

## `@dm_dark_matter_qualification_locus` — Dark-Matter Qualification Locus

```text
type: MatchedFullVisibleQualificationRelation
status: ATLAS_DERIVED_CLOSED
criticality: critical
```

Precise internal definition of what a dark-matter realization would have to be in the current architecture. It does not assert that such a pair exists in nature.

```text
DM_R:={(u_f,u_v): matched external data; u_f contains admissible hidden S3 organization; M_R(u_f)=M_R(u_v); T_H:=T_f−T_v≠0; g_f≠g_v; Ein(g_f)=κT_f; Ein(g_v)=κT_v; persistence/boundary/Q gates pass}.
```

## `@dm_dark_matter_qualification_nonempty` — Dark-Matter Qualification Nonemptiness

```text
type: OpenExistenceTheorem
status: OPEN_PRIMARY_HANDLE
criticality: critical
```

Final internal existence target after the source map is typed: prove that the Dark-Matter Qualification Locus contains at least one admissible full/visible comparison state.

```text
Goal: DM_R ≠ ∅ for at least one declared Resolution R and matched comparison class.
```

## `@dm_dark_readout_defect` — Dark Readout Factorization Defect

```text
type: ReadoutFactorizationDefect
status: ATLAS_DERIVED_ACTIVE
criticality: critical
```

Pairs of formal states identified by ordinary matter readout but distinguished by gravitational readout.

```text
D_R={(x,y): M_R(x)=M_R(y), G_R(x)!=G_R(y)}.
```

## `@dm_direct_cycle_gravity_no_go` — Direct Cycle-Gravity Kernel No-Go

```text
type: NoGoTheorem
status: ATLAS_DERIVED_CLOSED
criticality: constraint
```

A pure divergence-free circulation is killed by the direct deltaC gravitational channel; cycle organization can matter only through network/operator dependence or another typed route.

```text
z in ker(D_C) => G_direct(z)=0.
```

## `@dm_energy_gravity_consistency_filter` — Energy-Gravity Consistency Filter

```text
type: CompatibilityFilter
status: ATLAS_DERIVED_ACTIVE
criticality: supporting
```

Admits only native continuity/gravity flows whose readable metric and energy/stress-energy route agree.

```text
Flow_EG(N)={Phi in Flow(N): Ein(g_Phi)=kappa T_E(N)}.
```

## `@dm_formal_persistence_qualification` — Hidden-State Formal Persistence Qualification

```text
type: PredicateOnEmbeddedHiddenStates
status: ATLAS_DERIVED_ACTIVE
criticality: critical
```

Exact formal Persistence test applied only after a hidden S3 network state has been embedded in the Time-Space Inherited State Bundle.

```text
P_Xi(x) := [exists n>=1 such that I^n(iota_HE^R(x)) ~ iota_HE^R(x)]. If true, iota_HE^R(x) in Xi.
```

## `@dm_hidden_boundary_contact` — Hidden Persistent-Boundary Contact Set

```text
type: CanonicalBoundaryContactSet
status: ATLAS_DERIVED_CLOSED
criticality: critical
```

Canonical boundary-incidence object replacing the arbitrary open incidence relation. It detects whether the closure of the hidden persistent subset reaches the already-existing Persistent Boundary.

```text
B_H^R := cl_E(Xi_H^R) ∩ ∂Xi. B_H^R=∅ kills the residue route at Resolution R; B_H^R≠∅ supplies the relevant boundary support.
```

## `@dm_hidden_boundary_response_form` — Hidden Boundary-Response Form

```text
type: PositiveQuotientBilinearForm
status: ATLAS_DERIVED_ACTIVE
criticality: supporting
```

Positive response geometry on relative S2 port states after quotienting the kernel of the hidden response operator.

```text
B_H([x],[y])=x^T Lambda_H y on R^P/ker(Lambda_H).
```

## `@dm_hidden_persistent_subset` — Hidden Persistent Subset

```text
type: ConditionalSubsetOfPersistentLocus
status: ATLAS_DERIVED_CLOSED
criticality: critical
```

Once a hidden-state embedding exists, this object selects the embedded hidden states that satisfy the exact Time-Space Persistence criterion.

```text
Xi_H^R := { iota_H(x) | x∈Dom(iota_H), iota_H(x)∈Xi } ⊆ Xi.
```

## `@dm_hidden_relational_load` — Hidden Relational-Capacity Load

```text
type: FiniteNetworkLoadFunctional
status: ATLAS_DERIVED_ACTIVE
criticality: critical
```

Static supported load assigned to hidden relationships using relationship valuation and runtime transition capacity. It is not endpoint history energy and is not automatically mass.

```text
L_H(U)=sum_{e in E_H(U)} r(e) T_run(e); rho_H(U)=L_H(U)/V(U).
```

## `@dm_hidden_response_operator` — Hidden S3 to S2 Response Operator

```text
type: SchurReducedBoundaryOperator
status: ATLAS_DERIVED_ACTIVE
criticality: critical
```

Effective S2-port operator obtained by eliminating hidden S3 interior coordinates from the continuity Laplacian.

```text
Lambda_N=L_PP-L_PI L_II^{-1} L_IP; DeltaLambda_H=Lambda_full-Lambda_vis.
```

## `@dm_hidden_s3_network` — Hidden S3 Multi-Port Continuity Network

```text
type: DerivedNetworkCandidate
status: ATLAS_DERIVED_ACTIVE
criticality: critical
```

Candidate Mode-0-selected hidden continuity organization joining multiple localized S2 / black-hole ports within the established S3 continuity level. It is a derived subnetwork candidate, not a new dimension and not yet identified with dark matter.

```text
G_H^R=(V_H,E_H,w), with multi-port hidden connectivity; active geometry remains S4 -> S3 -> S2.
```

## `@dm_hidden_sector_conservation` — Hidden-Sector Conservation / Exchange Law

```text
type: StressEnergyExchangeBalanceIdentity
status: ATLAS_DERIVED_CLOSED
criticality: critical
```

Covariant hidden/visible exchange identity implied by total stress-energy conservation after a full/visible source decomposition is defined.

```text
T_full=T_vis+T_H, ∇_μ T_full^{μν}=0. Define J^ν:=∇_μ T_vis^{μν}; then ∇_μ T_H^{μν}=-J^ν. If J^ν=0, the hidden sector is separately conserved.
```

## `@dm_hidden_state_bundle` — Hidden S3 Relational-State Bundle

```text
type: ConditionalRelationalStateBundle
status: ATLAS_DERIVED_ACTIVE
criticality: critical
```

Type-normalized bundle candidate for the time-indexed hidden S3 network organization. Its existence as a smooth admissible bundle is conditional on the declared hidden relational history.

```text
π_H:E_H^R→T_H, with fiber state R_H(t)=(V_t,E_t,w_t,χ_t,H_t)_R. This types the domain of iota_H; it does not itself prove iota_H exists.
```

## `@dm_hidden_state_embedding` — Hidden S3 State Embedding into Inherited State Bundle

```text
type: OpenBundleMonomorphism
status: OPEN_PRIMARY_HANDLE
criticality: critical
```

Current primary open map: embed the hidden relational-state bundle into the Time-Space Inherited State Bundle while preserving base continuation and inherited evolution.

```text
π_H:E_H^R→T_H; iota_H:E_H^R↪E; π_E∘iota_H=j_T∘π_H; I∘iota_H=iota_H∘I_H. Existence/injectivity for the physical hidden network remain open.
```

## `@dm_history_support_preorder` — History-Support Preorder

```text
type: PreorderOnRelationships
status: ATLAS_DERIVED_ACTIVE
criticality: supporting
```

Orders relationships by inclusion of invariant-preserving admissible history support.

```text
e <=_H f iff S_R(e) subseteq S_R(f).
```

## `@dm_history_to_continuity_strength` — History Support to Continuity-Strength Transduction

```text
type: OpenMonotoneFunctional
status: OPEN_HANDLE
criticality: supporting
```

Typed unresolved object promoted from the Master Dark-Matter QMO. It remains mathematically open; promotion makes the unknown queryable rather than solved.

```text
K_R : HistorySupport_R -> ContinuityStrength | requirements: Respect history-support preorder where all other local conditions are equal.; Do not identify raw history count with physical continuity strength.; Allow source-authoritative decay/forgetting if present.
```

## `@dm_local_capacity_envelope` — Local Constitutive Capacity Envelope

```text
type: LocalCapacityBound
status: ATLAS_DERIVED_ACTIVE
criticality: supporting
```

Local upper envelope on runtime transition capacity induced by the recovered continuity-flow relation and admissible endpoint-state range.

```text
U_ij^+=kappa_ij A_ij DeltaC_ij^+; T_run(e_ij)<=U_ij^+.
```

## `@dm_local_continuity_response_coefficient` — Local Continuity Response Coefficient

```text
type: LocalEdgeResponseCoefficient
status: ATLAS_DERIVED_ACTIVE
criticality: critical
```

Local unsaturated edge-response coefficient used by the finite continuity Laplacian. It is definitionally distinct from runtime transition capacity.

```text
w_e = kappa_ij A_ij >= 0; W_N=diag(w_e); L_N=B_N W_N B_N^T.
```

## `@dm_metric_action_selection` — Metric-Coupled Hidden Action Selection

```text
type: OpenActionSelection
status: OPEN_PRIMARY_HANDLE
criticality: critical
```

Narrow remaining source-map problem: select or derive the admissible hidden-sector action/constitutive functional with explicit metric dependence needed for readable stress-energy.

```text
S_H ∈ S_adm(Q_H,g). Required: differentiability in g, declared field variables/couplings, compatibility with Q-handoff data, and conservation/exchange consistency.
```

## `@dm_mode0_access_interface` — Mode-0 / White-State Access Interface

```text
type: CuratorialAccessInterface
status: USER_CURATORIAL_RULING_ACTIVE
criticality: critical
```

Mode 0 routes through the White-State Core and is treated in the current dark-matter landscape as an access interface to the inter-black-hole hidden continuity network. The White-State Core is not identified with the network or with dark matter.

```text
Mode1 -> local GR/Penrose singularity branch; Mode0 -> White-State Core -> hidden inter-black-hole network (current curatorial ruling).
```

## `@dm_mode0_network_selection_rule` — Mode-0 Hidden-Network Selection Rule

```text
type: OpenSelectionMap
status: OPEN_HANDLE
criticality: supporting
```

Typed unresolved object promoted from the Master Dark-Matter QMO. It remains mathematically open; promotion makes the unknown queryable rather than solved.

```text
Sel_0 : Mode0AccessState -> P(X_H^R) | requirements: Preserve current White-State-Core access-interface distinction.; Select hidden S3 support without identifying White-State Core with dark matter.; Remain inside S4 -> S3 -> S2.
```

## `@dm_native_density_to_readable_source` — Native Density Profile to Readable Source

```text
type: OpenTransduction
status: OPEN_HANDLE
criticality: supporting
```

Typed unresolved object promoted from the Master Dark-Matter QMO. It remains mathematically open; promotion makes the unknown queryable rather than solved.

```text
T_rho,R : DensityProfile_R -> ReadableSource_R | requirements: Cannot use one regional scalar as a universal spatial profile inverse.; Must preserve any claimed nonzero distinction through an explicitly typed translation/calibration.; Must not reconstruct a full stress-energy tensor from scalar density alone.
```

## `@dm_native_hidden_witness` — Native Hidden-Network Witness

```text
type: TypedWitnessTuple
status: ATLAS_DERIVED_ACTIVE
criticality: critical
```

Current finite diagnostic package keeping static supported-load profile and hidden inter-port response distinct.

```text
W_H^R=(Delta boldrho_H^R, Lambda_H) with separately typed history/chirality/persistence data when required.
```

## `@dm_omega_to_chromatic_representation` — Chirality-Space to Chromatic/Basin Representation

```text
type: OpenRepresentationRelation
status: OPTIONAL_OPEN_HANDLE
criticality: optional
```

Typed unresolved object promoted from the Master Dark-Matter QMO. It remains mathematically open; promotion makes the unknown queryable rather than solved.

```text
R_OmegaC^R subseteq Omega x X_C^R | requirements: Do not identify chirality-space elements with chromatic components by shared notation.; Any transported representation must satisfy the appropriate equivariance/commutation condition.; Not required by the primary residue-bundle branch.
```

## `@dm_one_port_no_go` — Free One-Port Hidden Appendage No-Go

```text
type: NoGoTheorem
status: ATLAS_DERIVED_CLOSED
criticality: constraint
```

A free hidden connected component attached to only one readable port contributes zero effective Schur/Kron port operator.

```text
one readable port => Lambda_H=0 for a free hidden component.
```

## `@dm_projection_residue_survival` — Projection-Residue Survival Test

```text
type: FullVsVisibleSurvivalTest
status: ATLAS_DERIVED_ACTIVE
criticality: critical
```

Tests whether matched full and visible-only constructions remain distinguishable after boundary projection and invariant-residue bundle construction.

```text
B_full^R not ~=_F B_vis^R is a sufficient field-bundle survival witness.
```

## `@dm_q_completion_family` — Residue-Bundle Q-Completion Family

```text
type: ConditionalCompletionFamily
status: ATLAS_DERIVED_CLOSED
criticality: critical
```

Set of complete QFT handoff objects extending an admissible residue bundle under the current Time-Space field axioms/theorems. It replaces the open arbitrary residue→Q map.

```text
C_Q(B):={ Q=(M,F,π_F,h,∇,R_∇,Γ,A,P,S) | Q extends B=(M,F,π_F) and satisfies the admitted field axioms }. For a residue bundle produced under the full current Time-Space assumptions, C_Q(B)≠∅ by T1–T4.
```

## `@dm_q_survival` — Q-Handoff Survival Theorem

```text
type: StructuredTupleSurvivalTheorem
status: ATLAS_DERIVED_CLOSED
criticality: critical
```

A hidden full-vs-visible distinction that survives as a non-isomorphic residue bundle cannot disappear by merely appending the standard Q-handoff structure, because the residue bundle is a constituent of Q.

```text
B_full≄B_vis ⇒ no Q-isomorphism preserving the residue-bundle constituent can identify Q_full with Q_vis. Thus bundle-level survival implies Q-structured survival under the declared morphism category.
```

## `@dm_resolution_density_profile` — Resolution-Level Hidden Density Profile

```text
type: ResolutionIndexedDensityProfile
status: ATLAS_DERIVED_ACTIVE
criticality: critical
```

Resolution-level profile of hidden supported relational-capacity load. The scalar regional density is only its weighted compression.

```text
rho_{H,a}^R=L_H(U_a)/V_a; Delta boldrho_H^R=(Delta rho_{H,a}^R)_a.
```

## `@dm_runtime_transition_capacity` — Runtime Transition Capacity

```text
type: EdgeCapacityFunctional
status: ATLAS_DERIVED_ACTIVE
criticality: critical
```

Maximum globally feasible continuity flow supported by an already-persistent relationship under the active Time-Space constraints.

```text
T_run(e)=sup_{Phi in F_run(G_*)} Phi(e).
```

## `@dm_stress_energy_realization_family` — Hidden Stress-Energy Realization Family

```text
type: ConditionalStressEnergyFamily
status: ATLAS_DERIVED_CLOSED
criticality: critical
```

Set-valued readable stress-energy construction conditional on a metric-coupled hidden action. It replaces the arbitrary open residue→stress-energy map.

```text
T_H(Q,g):={ -(2/√(-g)) δS_H/δg^{μν} | S_H∈S_adm(Q_H,g) }. The family is typed; selecting the physically relevant member remains the metric-action-selection problem.
```

## `@dm_stress_energy_separation_gate` — Stress-Energy Separation Gate

```text
type: SufficientTensorSeparationWitness
status: ATLAS_DERIVED_ACTIVE
criticality: critical
```

A nonzero readable density difference for the same observer is sufficient to prove the full and visible stress-energy tensors are unequal; it does not reconstruct the full tensor.

```text
Delta rho_read[u]=Delta T_mn u^m u^n != 0 => Delta T_mn != 0.
```



# 4. SELF-CLOSURE

```text
composable nodes: 214
primitive dependency pairs: 307
fixed-point dependency pairs: 5447
closure growth: 17.74x
child nontrivial SCCs: 1
```

Recursive consequences are kept in:

```text
registry/DM_COMPOSED_DEPENDENCY_INDEX.json
```

rather than bloating the direct graph.

---

# 5. DARK-MATTER QUALIFICATION

The canonical internal qualification object is:

```text
@dm_dark_matter_qualification_locus
```

Its nonemptiness theorem target is:

```text
@dm_dark_matter_qualification_nonempty
```

The child API therefore separates:

```text
definition
from
existence
from
empirical identification.
```

---

# 6. OPEN HANDLES

- `@dm_dark_matter_qualification_nonempty` — OPEN_PRIMARY_HANDLE — Dark-Matter Qualification Nonemptiness
- `@dm_hidden_state_embedding` — OPEN_PRIMARY_HANDLE — Hidden S3 State Embedding into Inherited State Bundle
- `@dm_metric_action_selection` — OPEN_PRIMARY_HANDLE — Metric-Coupled Hidden Action Selection
- `@dm_history_to_continuity_strength` — OPEN_HANDLE — History Support to Continuity-Strength Transduction
- `@dm_mode0_network_selection_rule` — OPEN_HANDLE — Mode-0 Hidden-Network Selection Rule
- `@dm_native_density_to_readable_source` — OPEN_HANDLE — Native Density Profile to Readable Source
- `@dm_omega_to_chromatic_representation` — OPTIONAL_OPEN_HANDLE — Chirality-Space to Chromatic/Basin Representation


---

# 7. DESIGN RULE

Direct graph:

```text
small, typed, source-aware
```

Recursive closure:

```text
dense, derived, queryable
```

A closure edge is not promoted to a physical mechanism until a targeted
proof/recovery pass survives.

Dark matter remains physically unresolved.


---

# 12. BIDIRECTIONAL CROSS-API CLOSURE — 2.2

Dark Matter API 2.2 adds a directional cross-crawl layer:

```text
Time-Space 4.3 -> Dark Matter
Dark Matter -> Time-Space 4.3
```

The source/type-audited promotions are:

```text
@native_constraint_closure
@total_action
@diffeomorphism_invariance
@particle_readable_organization

@dm_constraint_preserving_embedding_family
@dm_covariant_hidden_action_family
@dm_er_branch_readout_separation
```

The current primary questions remain open but are narrower:

```text
@dm_hidden_state_embedding
  -> select from Emb_H,phys^R

@dm_metric_action_selection
  -> select from S_H^cov(Q_H,g)

@dm_dark_matter_qualification_nonempty
  -> construct one witness in DM_R
```

Cross-crawl statistics:

```text
direct TS/DM interface: 27

DM objects reached from Time-Space: 35/38

novel full-Time-Space handles exposed by reverse crawl:
  depth 1: 17
  depth 2: 101
  depth 3: 279

strict fixed-point dependency pairs after promotion:
  5769

Dark Matter child SCCs:
  0
```

Dense cross-links remain in the mining overlay unless a targeted
source/type audit earns promotion.
