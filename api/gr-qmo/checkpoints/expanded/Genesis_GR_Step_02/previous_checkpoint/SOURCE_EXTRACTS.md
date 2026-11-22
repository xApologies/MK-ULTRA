# Genesis–GR: exact source excerpts

This file preserves the source material used in the accompanying derivation. It is not a replacement canonical source and contains no silent corrections. The raw mathematical markup is retained here for fidelity; DERIVATION.md uses readable Unicode notation.

The source archive is the user-uploaded `3 | .zip`. E1–E11 come from the embedded API 4.3 canonical Markdown. E12–E14 come from the manuscript text already indexed inside the archived unified QMO database. The PDF binary was not available for page rendering in this run; no visual PDF audit is claimed. E15 records equation provenance.

## E1. Phase action, equation, and stress-energy

Source: API 4.3 canonical Markdown; lines 480–539. Original text follows unchanged.

## Phase Action

\[
S_{\tau}
=
-\frac{1}{2}
\int d^4x\sqrt{-g}
\left(
\beta g^{\mu\nu}\partial_\mu\tau\partial_\nu\tau
+V(\tau)
\right).
\]

```text
function phaseAction(
    τ: PhaseField,
    g: EffectiveMetric,
    β: PhaseKineticCoupling,
    V: PhasePotential
) -> Action
```

## Phase Evolution Equation

\[
\beta\Box\tau-V'(\tau)=0.
\]

```text
contract PhaseEvolution {
    input: τ, g, β, V
    output: admissible phase trajectory
    condition: β□τ = V′(τ)
}
```

## Phase Stress-Energy Output

\[
T^{(\tau)}_{\mu\nu}
=
\beta\partial_\mu\tau\partial_\nu\tau
-
\frac{1}{2}g_{\mu\nu}
\left(
\beta g^{\rho\sigma}\partial_\rho\tau\partial_\sigma\tau
+V(\tau)
\right).
\]

```text
function phaseStressEnergy(
    τ: PhaseField,
    g: EffectiveMetric
) -> StressEnergyTensor
```

---



## E2. Chromatic Lagrangian and stress-energy

Source: API 4.3 canonical Markdown; lines 539–583. Original text follows unchanged.

# 7. Recovered Chromatic Dynamics

## Chromatic Lagrangian

\[
\mathcal{L}_{\chi}
=
-\frac{1}{2}
G^{ab}(\boldsymbol{\chi})
 g^{\mu\nu}
\partial_\mu\chi_a
\partial_\nu\chi_b
-U(\boldsymbol{\chi}).
\]

```text
function chromaticLagrangian(
    χ: ChromaticField,
    Gχ: ChromaticFieldSpaceMetric,
    g: EffectiveMetric,
    U: ChromaticPotential
) -> LagrangianDensity
```

## Chromatic Stress-Energy Output

\[
T^{(\chi)}_{\mu\nu}
=
G^{ab}(\boldsymbol{\chi})
\partial_\mu\chi_a
\partial_\nu\chi_b
-g_{\mu\nu}\mathcal{L}_{\chi}.
\]

```text
function chromaticStressEnergy(
    χ: ChromaticField,
    g: EffectiveMetric
) -> StressEnergyTensor
```

---



## E3. Total action and integrated Einstein equation

Source: API 4.3 canonical Markdown; lines 583–646. Original text follows unchanged.

# 8. Recovered Integration Layer

## Total Action

\[
S_{\mathrm{tot}}
=
\frac{1}{16\pi G}
\int d^4x\sqrt{-g}\,R
+S_{\tau}
+S_{\chi}
+S_{ER}
+S_{\mathrm{matter}}.
\]

### API interpretation

```text
function totalAction(
    geometry: EinsteinHilbertSector,
    phase: PhaseSector,
    chromatic: ChromaticSector,
    er: ERSector,
    matter: MatterSector
) -> UnifiedAction
```

## Integrated Field Equation

\[
G_{\mu\nu}
=
8\pi G
\left(
T^{(\tau)}_{\mu\nu}
+T^{(\chi)}_{\mu\nu}
+T^{(ER)}_{\mu\nu}
+T^{(\mathrm{matter})}_{\mu\nu}
\right).
\]

### API interpretation

```text
function solveGeometry(
    phaseStress: StressEnergyTensor,
    chromaticStress: StressEnergyTensor,
    erStress: StressEnergyTensor,
    matterStress: StressEnergyTensor
) -> GeometricResponse
```

### Initial recovered dependency chain

```text
PhaseField ───────→ PhaseMetric ───────→ PhaseStressEnergy ────┐
ChromaticField ───→ ChromaticDynamics ─→ ChromaticStressEnergy ─┤
ERNetwork ────────→ ERGeometry ─────────→ ERStressEnergy ────────┼→ EffectiveGeometry
MatterSector ───────────────────────────→ MatterStressEnergy ────┘
```

---



## E4. Nonlinear self-coupling

Source: API 4.3 canonical Markdown; lines 53665–53772. Original text follows unchanged.

# 3. Gravitational Self-Coupling and Nonlinear Closure

## Handle

```text
@gravitational_self_coupling
```

## Type

```text
Type: NativeFixedPointClosure
Domain: continuity perturbations and gravitational helicon responses
Codomain: self-consistent nonlinear gravitational state
DependsOn:
    @continuity_perturbation
    @continuity_redistribution
    @gravitational_helicon_mode
    @time_shell
UsedBy:
    @gravity
    @einstein_limit
    @black_hole
    @cosmology
```

Matter and gravity contribute to the total native continuity perturbation:

\[
\delta C_{\mathrm{tot}}
=
\delta C_{\mathrm{m}}
+
\delta C_{\mathrm{g}}.
\]

The gravitational contribution is geometry-dependent:

\[
\delta C_{\mathrm{g}}
=
\mathcal{F}_g[\delta C].
\]

Let \(\mathcal{R}_C\) be the continuity-redistribution operator.
The closed gravitational state is the fixed point

\[
\delta C_\star
=
\mathcal{R}_C
\left[
\delta C_{\mathrm{m}}
+
\mathcal{F}_g[\delta C_\star]
\right].
\]

Its constructive iteration is

\[
\delta C^{(0)}
=
\mathcal{R}_C[\delta C_{\mathrm{m}}],
\]

\[
\delta C^{(n+1)}
=
\mathcal{R}_C
\left[
\delta C_{\mathrm{m}}
+
\mathcal{F}_g[\delta C^{(n)}]
\right].
\]

The readable metric sequence is

\[
g_{\mu\nu}^{(n)}
=
\bar g_{\mu\nu}
+
\Pi_T\!\left(\delta C^{(n)}\right).
\]

When the admissible iteration converges,

\[
g_{\mu\nu}
=
\lim_{n\to\infty}g_{\mu\nu}^{(n)}.
\]

The readable nonlinear closure is

\[
G_{\mu\nu}[g]
=
8\pi G\,
T_{\mu\nu}[g,\mathrm{matter}],
\]

where the gravitational organization contributes through the phase,
chirality, ER, and geometry-dependent source sectors.



## E5. Conditional projected-GR inheritance

Source: API 4.3 canonical Markdown; lines 53772–53849. Original text follows unchanged.

# 4. Projected-GR Inheritance

## Handle

```text
@projected_gr_inheritance
```

## Theorem

Let

\[
\Pi_T:
\mathrm{NativeGravity}
\longrightarrow
\mathrm{ReadableGeometry}
\]

be the Time-Shell projection. In a readable domain \(D\), suppose

\[
G_{\mu\nu}[g]
+
\Lambda g_{\mu\nu}
=
8\pi G T_{\mu\nu},
\]

\[
\nabla_\mu T^{\mu\nu}=0,
\]

and the MK43 correction operator obeys

\[
\Delta_{\mathrm{MK43}}[g,T]=0
\quad\text{throughout }D.
\]

Then every General Relativity solution with the same initial and boundary data
is a readable MK43 solution:

\[
\mathrm{Sol}_{\mathrm{GR}}(D)
\subseteq
\mathrm{Sol}_{\mathrm{MK43}}^{\mathrm{readable}}(D).
\]

If the projected correction vanishes identically on \(D\),

\[
\mathrm{Sol}_{\mathrm{GR}}(D)
=
\mathrm{Sol}_{\mathrm{MK43}}^{\mathrm{readable}}(D).
\]

## Inherited Descendants

Within an exact projected-GR domain, the API inherits:

```text
Newtonian gravity
post-Newtonian gravity
solar-system tests
binary-pulsar dynamics
ordinary black-hole exteriors
standard gravitational-wave generation
standard cosmological solutions
```

Distinctive MK43 effects are confined to domains where

\[
\Delta_{\mathrm{MK43}}[g,T]\neq 0.
\]



## E6. Native constraints

Source: API 4.3 canonical Markdown; lines 54115–54191. Original text follows unchanged.

# 8. Native Transduction-Constraint Closure

## Handle

```text
@native_constraint_closure
```

## Type

```text
Type: TransductionConstraintAlgebra
Domain: admissible native states and projection maps
Codomain: preserved physical-state subspaces
DependsOn:
    @admissibility
    @continuity_conservation
    @chirality
    @persistent_topology
    @time_shell
UsedBy:
    @gauge_consistency
    @anomaly_freedom
    @readable_graviton_projection
```

Define native constraints

\[
\mathcal{C}_A,\quad
\mathcal{C}_C,\quad
\mathcal{C}_{\chi},\quad
\mathcal{C}_W,\quad
\mathcal{C}_T
\]

for admissibility, continuity, chirality orbit, topology class, and Time-Shell
projection.

Physical native states satisfy

\[
\mathcal{C}_a|\Psi_{\mathrm{phys}}\rangle=0.
\]

Closure under native update is

\[
[\mathcal{C}_a,\mathcal{C}_b]_U
=
\sum_c f_{ab}{}^c\mathcal{C}_c.
\]

The update operator preserves the physical kernel:

\[
U\,\ker(\mathcal{C})
\subseteq
\ker(\mathcal{C}).
\]

Transduction preserves constraints when

\[
\mathcal{C}_{\mathrm{read}}
\Pi_T
=
\Pi_T
\mathcal{C}_{\mathrm{native}}
\]

on admissible states.

This is the native replacement for imposing a conventional fundamental quantum
constraint algebra on a pre-quantum transduction framework.



## E7. Native dimensional projection

Source: API 4.3 canonical Markdown; lines 54275–54361. Original text follows unchanged.

# 10. Configuration-Space Dimensional Projection

## Handle

```text
@configuration_space_3_1_1
```

## Type

```text
Type: GeometricConfigurationSpace
Native form: 3 + 1 + 1
Readable projection: 1 + 3
DependsOn:
    @geometric
    @chirality_history
    @artifact_coordinate
    @time_shell
UsedBy:
    @readable_spacetime
    @lorentz_signature
    @dimensionality_audit
```

The native geometric is represented as

\[
\mathcal{G}_{\mathrm{geo}}
=
(X,Y,Z;A;\chi),
\]

with

\[
\mathcal{G}_{\mathrm{geo}}
\in
\mathbb{R}^3
\times
\mathcal{A}
\times
\Chi.
\]

The three coordinates \(X,Y,Z\) are readable orientation axes,
\(A\) is the artifact or admissible-expression coordinate, and
\(\chi\) is chirality history.

The Time-Shell projection is

\[
\Pi_T:
\mathbb{R}^3\times\mathcal{A}\times\Chi
\longrightarrow
\mathcal{M}_{1,3},
\]

\[
\Pi_T(X,Y,Z;A;\chi)
=
(T,X,Y,Z).
\]

Finite expression-capacity accounting yields

\[
\Delta\Sigma^2
=
c_A^2\Delta T^2
-
\Delta X^2
-
\Delta Y^2
-
\Delta Z^2.
\]

The readable metric signature is therefore

\[
(+,-,-,-)
\]

up to sign convention.



## E8. Correspondence registry

Source: API 4.3 canonical Markdown; lines 54361–54453. Original text follows unchanged.

# 11. Controlled Correspondence Registry

## Handle

```text
@correspondence_registry
```

## Schema

```text
CorrespondenceRecord {
    source_space
    target_space
    map
    validity_domain
    retained_objects
    discarded_objects
    error_bound
    failure_condition
    downstream_sensitivity
}
```

## Canonical Maps

```text
Pi_Q:
    NativeHeliconSpectrum
    -> ReadableQuantumHarmonics

Pi_T:
    NativeContinuityPerturbation
    -> ReadableMetricPerturbation

Pi_GR:
    ProjectedMetricGeometry
    -> EinsteinGravity

Pi_WF:
    EinsteinGravity
    -> WeakFieldGravity

Pi_PN:
    EinsteinGravity
    -> PostNewtonianGravity

Pi_N:
    WeakFieldGravity
    -> NewtonianPotential

Pi_O:
    ReadableGravitationalSolution
    -> DetectorObservable
```

The composed observable map is

\[
\Pi_{\mathrm{total}}
=
\Pi_O
\circ
\Pi_N
\circ
\Pi_{\mathrm{PN}}
\circ
\Pi_{\mathrm{WF}}
\circ
\Pi_{\mathrm{GR}}
\circ
\Pi_T.
\]

If

\[
\|\Pi_i(x)-x_i^{\mathrm{ideal}}\|
\le
\epsilon_i,
\]

then the first-order propagated error satisfies

\[
\epsilon_{\mathrm{total}}
\le
\sum_i L_i\epsilon_i,
\]

where \(L_i\) is the downstream sensitivity factor.



## E9. Accepted stress-energy convention and Einstein equation

Source: API 4.3 canonical Markdown; lines 61356–61392. Original text follows unchanged.

### EQ-RP43-GR-011 — Einstein-Hilbert action

- Handle: `@einstein_hilbert_action`
- Provenance class: `ACCEPTED_MATHEMATICS`

```text
S_g=(c³/16πG)∫(R-2Λ)√(-g)d⁴x
```

### EQ-RP43-GR-012 — Stress-energy definition

- Handle: `@stress_energy_tensor`
- Provenance class: `ACCEPTED_MATHEMATICS`

```text
T_{μν}=-(2/√(-g)) δS_m/δg^{μν}
```

### EQ-RP43-GR-013 — Einstein field equation

- Handle: `@einstein_field_equation`
- Provenance class: `ACCEPTED_MATHEMATICS`

```text
G_{μν}+Λg_{μν}=(8πG/c⁴)T_{μν}
```

### EQ-RP43-GR-014 — Covariant conservation

- Handle: `@local_energy_momentum_conservation`
- Provenance class: `ACCEPTED_MATHEMATICS`

```text
∇_μT^{μν}=0
```



## E10. Unlinked projection operator entry

Source: API 4.3 canonical Markdown; lines 43967–43977. Original text follows unchanged.

### `@time_shell_projection_operator` — Time-Shell Projection Operator

```text
uri: mk43://recover/dependency/time-shell-projection-operator
status: indexed-unlinked
upstream: none
downstream: none
source_occurrences: 7
```



## E11. Numbered source equation records

Source: API 4.3 canonical Markdown; lines 12228–12327. Original text follows unchanged.

### MATH-0288 `313cc5190b21`

**Kinds:** `display`  
**Sources:** `chapters_1_5/chapters_1_5.tex`

```latex
\beta \Box \tau - V'(\tau) = 0.
```

### MATH-0289 `41cac5e70b58`

**Kinds:** `display`  
**Sources:** `chapters_1_5/chapters_1_5.tex`

```latex
T^{(\chi)}_{\mu\nu}
=
G^{ab}\partial_\mu\chi_a\partial_\nu\chi_b
- g_{\mu\nu}\mathcal{L}_\chi.
```

### MATH-0290 `540d5906dacc`

**Kinds:** `display`  
**Sources:** `chapters_1_5/chapters_1_5.tex`

```latex
S_\tau
=
-\frac{1}{2}\int d^4x \sqrt{-g}\left(
\beta\, g^{\mu\nu}\partial_\mu\tau\partial_\nu\tau
+ V(\tau)
\right).
```

### MATH-0291 `5857a13fc189`

**Kinds:** `display`  
**Sources:** `chapters_1_5/chapters_1_5.tex`; `tome_mk43_skeleton/tome_mk43.tex`

```latex
\mathcal{H} = \mathcal{H}_\tau \otimes \mathcal{H}_\chi \otimes \mathcal{H}_{ER} \otimes \mathcal{H}_g.
```

### MATH-0292 `98cd4dc50cda`

**Kinds:** `display`  
**Sources:** `chapters_1_5/chapters_1_5.tex`

```latex
\bm{\chi}(x) = (\chi_1, \dots, \chi_7),
```

### MATH-0293 `9a0d0d6e4a25`

**Kinds:** `display`  
**Sources:** `chapters_1_5/chapters_1_5.tex`

```latex
\mathcal{L}_\chi
=
-\frac{1}{2}G^{ab}(\bm{\chi})\, g^{\mu\nu}\partial_\mu\chi_a\partial_\nu\chi_b
- U(\bm{\chi}),
```

### MATH-0294 `a1dd9d54f23c`

**Kinds:** `display`  
**Sources:** `chapters_1_5/chapters_1_5.tex`

```latex
\bm{\chi} \to 0,
```

### MATH-0295 `aad183a2a9b5`

**Kinds:** `display`  
**Sources:** `chapters_1_5/chapters_1_5.tex`

```latex
W_{ij} \in \mathbb{R}_{\ge 0}
```

### MATH-0296 `b3950c5d7e1e`

**Kinds:** `display`  
**Sources:** `chapters_1_5/chapters_1_5.tex`

```latex
T^{(\tau)}_{\mu\nu}
=
\beta\, \partial_\mu\tau\partial_\nu\tau
-\frac{1}{2}g_{\mu\nu}
\left(
\beta g^{\rho\sigma}\partial_\rho\tau\partial_\sigma\tau
+ V(\tau)
\right).
```



## E12. Indexed manuscript: weak-field projection limit

Source: the existing `source_files.text` database record for `MK Ultra.pdf`, record `FILE-cca59f71a28079fb6fc511df`. This is archived indexed text, not a new PDF rendering; extracted page furniture is retained.

```text
46.9 The exact downstream projection equation
A separate recovered gravity path contains

                                                                     ΠT (δC) = hμν .
                                                                        ​                   ​                                      (46.9)


Equation (46.9) is EXACT_SOURCE with its original proof boundary retained. It maps a continuity perturbation to a weak-field
metric perturbation in the recovered path. It does not identify ΠT with ΠTS in (46.1), and it does not prove their equivalence.
                                                                                    ​               ​




The distinction between a source-specific perturbation projection and a universal Time-Shell-to-quantum projection is essential.
```


## E13. Indexed manuscript: native continuity-space type boundary

Source: the existing `source_files.text` database record for `MK Ultra.pdf`, record `FILE-cca59f71a28079fb6fc511df`. This is archived indexed text, not a new PDF rendering; extracted page furniture is retained.

```text
59.13 Typed continuity-projection contract
A minimal contract is

                                                                                               δC ∈ TC0 Cadmissible ,
                                                                                                                ​
                                                                                                                    ​          ​




                                                                        ΠT : TC0 Cadmissible ⟶ Γ(S 2 T ∗ M )/G,
                                                                              ​

                                                                                      ​
                                                                                          ​         ​

                                                                                                        ​                                ​
                                                                                                                                                                                          (59.13)
                                                                                               δC ⟼ [hμν ].              ​




Equation (59.13) is DETERMINISTIC_TYPE_NORMALIZATION, not a recovered definition. It states the missing domain,
symmetric-tensor codomain, and gauge quotient. The actual native continuity space remains a critical open construction.
```


## E14. Indexed manuscript: Einstein-sector open obligations

Source: the existing `source_files.text` database record for `MK Ultra.pdf`, record `FILE-cca59f71a28079fb6fc511df`. This is archived indexed text, not a new PDF rendering; extracted page furniture is retained.

```text
62.17 Typed Einstein-sector contract
The minimal type flow is

                                 (g, ψ) ⟼ (SEH [g], Sm [g, ψ]) ⟼ (Gμν [g], Tμν [g, ψ]) ⟼ Gμν + Λgμν − κTμν = 0.
                                                ​         ​                                       ​                 ​                           ​   ​   ​   (62.17)


Equation (62.17) is DETERMINISTIC_TYPE_NORMALIZATION. It records the mathematical obligations of an action-based
Einstein sector. It does not assert that the recovered MK-43 corpus supplies every map or functional in the chain.

62.18 Coverage calibration
The chapter assignment contains

                                                    Nassigned = 5,​                 NMEDIUM = 4,            ​                     NTHIN = 1.​               (62.18)




                                                                                                                                                                Page 5
                                                                                     Page
                                                                                     Page463
                                                                                          40
MK Ultra TOME - Volume VII




Equation (62.18) is DETERMINISTIC_COVERAGE_EVIDENCE. The handles contain 2,055 English units, 22 indexed equation
units, zero exact-definition units, and 2,425 registered dependencies. Shared equation IDs are preserved as co-occurrences
and do not multiply substantive proof.

62.19 API evidence register
 API handle                              Native title                               Coverage   Evidence counts (English / equations / dependencies)       Chapter role
 @einstein_hilbert_action                @einstein_hilbert_action                   MEDIUM     581 / 6 / 840                                              chapter-core object

 @einstein_limit                         @einstein_limit                            MEDIUM     29 / 3 / 1                                                 chapter-core object
 @linearized_einstein_tensor             @linearized_einstein_tensor                MEDIUM     628 / 6 / 657                                              chapter-core object

 @riemann_tensor                         @riemann_tensor                            MEDIUM     813 / 7 / 921                                              chapter-core object
 @semiclassical_einstein_equation        @semiclassical_einstein_equation           THIN       4/0/6                                                      chapter-core object


The register preserves action, curvature tensor, linearized field response, limiting behavior, and semiclassical sourcing as
separate mathematical addresses.

62.20 Evidence boundary
The operative distinctions are

                                                                                  Action =
                                                                                          FieldEquation,
                                                                        RiemannTensor =
                                                                                       EinsteinTensor,
                                                                                                                                                                     (62.19)
                                                              LinearizedEquation = NonlinearDynamics,
                                                                                           ​                          ​




                                                              SemiclassicalSource =
                                                                                   NativeQuantumGravity.


Equation (62.19) is EVIDENCE_BOUNDARY. Exact dependency relations organize the address space but do not prove
equivalence across these roles.

62.21 Open Einstein-sector obligations
The unresolved requirements are

                               UE = {NativeAction, NativeMatterFields, SourceFunctional, BoundaryConditions, GaugeCompletion,
                                 ​




                                     NonlinearProjection, ConservationProof, RenormalizedExpectationValue, EinsteinLimitProof,
                                     ​                                                                                                                ​              (62.20)
                                     DimensionsAndCouplings, WellPosedness, Stability, ExperimentalValidation}.


Equation (62.20) is CURATOR_SYNTHESIS. It records what a complete MK-43 Einstein sector must still establish. No missing
source, operator, proof, or coupling is invented here.

62.22 Chapter determination
The result is

                                         EinsteinSectorV07C06 = ESTABLISHED_ACTION_AND_FIELD_STRUCTURE
                                                                    ​




                                                                           ​
                                                                               + RECOVERED_API_ADDRESS_SPACE                             ​                           (62.21)
                                                                               + OPEN_NATIVE_SOURCE_AND_CLOSURE.


Equation (62.21) is DETERMINISTIC_STATUS_NORMALIZATION. The chapter supplies a coherent bridge from curvature to
action, field equations, sources, conservation, and weak-field limits while preserving the recovered object boundaries. The
native MK-43 action, stress-energy construction, semiclassical closure, and empirical validation remain open where exact
evidence is absent.




                                                                                                                                                                          Page 6
                                                                                       Page
                                                                                       Page464
                                                                                            41
MK Ultra TOME - Volume VII
```


## E15. Indexed proof-status records

Exact selected database records, serialized as JSON. `UNSPECIFIED` records provenance status; it is not itself proof of falsehood.

```json
[
  {
    "eq_id": "SW-SWP:API43:DISPLAY-0121",
    "owner_handle": "@projected_gr_inheritance",
    "namespace": "STONEWAKE::API43",
    "expression": "\\Pi_T:\n\\mathrm{NativeGravity}\n\\longrightarrow\n\\mathrm{ReadableGeometry}",
    "proof_status": "UNSPECIFIED",
    "source_path": "STONEWAKE_UNIFIED_PHYSICS_API_v1_1_20260823/02_MACHINE/STONEWAKE_PHYSICS_QMO.sqlite"
  },
  {
    "eq_id": "SW-SWP:API43:DISPLAY-0122",
    "owner_handle": "@projected_gr_inheritance",
    "namespace": "STONEWAKE::API43",
    "expression": "G_{\\mu\\nu}[g]\n+\n\\Lambda g_{\\mu\\nu}\n=\n8\\pi G T_{\\mu\\nu},",
    "proof_status": "UNSPECIFIED",
    "source_path": "STONEWAKE_UNIFIED_PHYSICS_API_v1_1_20260823/02_MACHINE/STONEWAKE_PHYSICS_QMO.sqlite"
  },
  {
    "eq_id": "SW-SWP:API43:DISPLAY-0123",
    "owner_handle": "@projected_gr_inheritance",
    "namespace": "STONEWAKE::API43",
    "expression": "\\nabla_\\mu T^{\\mu\\nu}=0,",
    "proof_status": "UNSPECIFIED",
    "source_path": "STONEWAKE_UNIFIED_PHYSICS_API_v1_1_20260823/02_MACHINE/STONEWAKE_PHYSICS_QMO.sqlite"
  },
  {
    "eq_id": "SW-SWP:API43:DISPLAY-0124",
    "owner_handle": "@projected_gr_inheritance",
    "namespace": "STONEWAKE::API43",
    "expression": "\\Delta_{\\mathrm{MK43}}[g,T]=0\n\\quad\\text{throughout }D.",
    "proof_status": "UNSPECIFIED",
    "source_path": "STONEWAKE_UNIFIED_PHYSICS_API_v1_1_20260823/02_MACHINE/STONEWAKE_PHYSICS_QMO.sqlite"
  },
  {
    "eq_id": "SW-SWP:API43:DISPLAY-0125",
    "owner_handle": "@projected_gr_inheritance",
    "namespace": "STONEWAKE::API43",
    "expression": "\\mathrm{Sol}_{\\mathrm{GR}}(D)\n\\subseteq\n\\mathrm{Sol}_{\\mathrm{MK43}}^{\\mathrm{readable}}(D).",
    "proof_status": "UNSPECIFIED",
    "source_path": "STONEWAKE_UNIFIED_PHYSICS_API_v1_1_20260823/02_MACHINE/STONEWAKE_PHYSICS_QMO.sqlite"
  },
  {
    "eq_id": "SW-SWP:API43:DISPLAY-0126",
    "owner_handle": "@projected_gr_inheritance",
    "namespace": "STONEWAKE::API43",
    "expression": "\\mathrm{Sol}_{\\mathrm{GR}}(D)\n=\n\\mathrm{Sol}_{\\mathrm{MK43}}^{\\mathrm{readable}}(D).",
    "proof_status": "UNSPECIFIED",
    "source_path": "STONEWAKE_UNIFIED_PHYSICS_API_v1_1_20260823/02_MACHINE/STONEWAKE_PHYSICS_QMO.sqlite"
  }
]
```
