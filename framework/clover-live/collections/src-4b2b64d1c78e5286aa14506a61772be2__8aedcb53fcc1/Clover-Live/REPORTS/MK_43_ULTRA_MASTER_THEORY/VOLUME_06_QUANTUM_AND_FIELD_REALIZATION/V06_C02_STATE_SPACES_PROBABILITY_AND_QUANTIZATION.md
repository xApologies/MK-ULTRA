# VOLUME VI - QUANTUM AND FIELD REALIZATION

## Chapter 50 - State Spaces, Probability, and Quantization

### 50.1 The state-space layer

Chapter 49 established the Canonical Quantum-Field Handoff Object as a structured bundle, observable, spectral, and action package. The next layer asks how states are represented, how probabilities arise, and how a field description is quantized. The standard mathematical setting is a complex Hilbert space

$$
\mathcal{H}\ \text{complete},\qquad
\langle\psi,\phi\rangle\in\mathbb{C},\qquad
\|\psi\|^2=\langle\psi,\psi\rangle. \tag{50.1}
$$

Equation (50.1) is EXTERNAL_ESTABLISHED_MATHEMATICS. Library 4.1 contains the declared addresses @hilbert_spaces and @hilbert_spaces_and_density_operators, but their coherent coverage is THIN and contains no recovered equation record. The conventional definition is therefore supplied as mathematical context, not misrepresented as an exact MK-43 source equation.

Completeness matters because state limits must remain inside the state space. The inner product supplies both geometry and probability amplitudes. A Hilbert space is not automatically the configuration space of the upstream framework, the bundle total space \(F\), or the projective target \(M\). A bridge among those spaces requires an explicit construction.

### 50.2 Pure states are rays

A normalized vector represents a pure state, but its physically irrelevant global phase means that the state is the ray

$$
[\psi]=\{e^{i\alpha}\psi:\alpha\in\mathbb{R}\},\qquad
\langle\psi,\psi\rangle=1. \tag{50.2}
$$

Equation (50.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. This quotient is conceptually compatible with projective geometry, yet compatibility is not identity. The Projective Target Manifold \(M\) in the handoff object arises from a boundary quotient by \(G_{\Pi}\). The projective Hilbert space arises from quotienting nonzero state vectors by nonzero complex scaling. A source-level map between them must specify which bundle or section data produces a quantum ray.

The distinction prevents a common overreach: a projective manifold in the upstream construction does not, by its name alone, become the space of quantum pure states. The source must establish the representation.

### 50.3 Born probability

For an orthogonal projector \(P\), the Born probability in the pure state \(\psi\) is

$$
\Pr(P\mid\psi)=\langle\psi,P\psi\rangle,\qquad
0\leq\Pr(P\mid\psi)\leq1. \tag{50.3}
$$

Equation (50.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. It connects the Hilbert-space inner product with the spectral projection family \(\mathbb{P}\) recovered as a constituent of \(Q\). The equation supplies the standard probability rule once a state representation and projector are known; it does not derive those ingredients from the Time Shell or from an upstream organizational state.

Normalization and positivity are not optional conventions. They are the conditions that make the measure probabilistic. Any MK-43 translation into this language must therefore preserve norm, positivity, and the total probability of the identity projector.

### 50.4 Observables and spectral measures

A bounded observable is represented by a self-adjoint operator \(A=A^{\dagger}\). Its spectral theorem representation is

$$
A=\int_{\sigma(A)}\lambda\,dP_A(\lambda),\qquad
\langle A\rangle_{\psi}=\langle\psi,A\psi\rangle. \tag{50.4}
$$

Equation (50.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. In the discrete case the integral becomes a sum. Unbounded operators require a dense domain and additional care. The handoff tuple's observable algebra and spectral projection family provide the right structural locations, but a complete correspondence must identify the admissible operators, their domains, and the relation between the source algebra \(\mathcal{A}\) and its representation on \(\mathcal{H}\).

This is also where operator names must be separated from operator proofs. The presence of an API handle does not establish self-adjointness, essential self-adjointness, spectral resolution, or a measurement interpretation.

### 50.5 Density operators

Mixed states and reduced states are represented by positive trace-class operators

$$
\rho\geq0,\qquad \operatorname{Tr}\rho=1,\qquad
\langle A\rangle_{\rho}=\operatorname{Tr}(\rho A). \tag{50.5}
$$

Equation (50.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. This is the natural formal expansion of the Library address @hilbert_spaces_and_density_operators. The API title marks the topic, while the formula supplies conventional mathematics whose provenance is external to the thin recovered record.

A density operator is not simply uncertainty about a pure vector. It also represents reduced states obtained by discarding access to a subsystem. Consequently, density-operator language is required whenever the upstream-to-readable projection leaves inaccessible degrees of freedom or whenever a bundle is partitioned into observed and unobserved sectors.

### 50.6 Ensembles and nonunique decompositions

An ensemble \(\{p_i,\psi_i\}\) produces

$$
\rho=\sum_i p_i|\psi_i\rangle\langle\psi_i|,\qquad
p_i\geq0,\qquad \sum_i p_i=1. \tag{50.6}
$$

Equation (50.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Different ensembles can yield the same density operator, so an ensemble decomposition is not generally an intrinsic physical label. The operator \(\rho\), rather than one preferred decomposition, controls all expectation values.

This fact matters for MK-43 interpretation. If several upstream configurations project to one readable quantum state, the distinction among those configurations cannot be recovered from \(\rho\) unless additional observables or provenance data survive. A many-to-one projection should therefore not be mistaken for a unique inverse dictionary.

### 50.7 Subsystems and partial trace

For a composite state on \(\mathcal{H}_A\otimes\mathcal{H}_B\), the reduced state of subsystem \(A\) is

$$
\rho_A=\operatorname{Tr}_B(\rho_{AB}),\qquad
\operatorname{Tr}_{A}(\rho_A A)
=\operatorname{Tr}_{AB}\!\left(\rho_{AB}(A\otimes I_B)\right). \tag{50.7}
$$

Equation (50.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. It separates loss of access from stochastic ignorance and provides the standard basis for entanglement and open-system descriptions.

An upstream projection could resemble a partial trace only after the factorization, traced subsystem, and equality of expectation values are established. Neither the name boundary projection nor a graph edge is enough. The exact mathematical test is whether the proposed map has the trace-preserving and positivity properties required of the relevant state transformation.

### 50.8 Quantum channels

A general physical state transformation is a completely positive trace-preserving map

$$
\mathcal{E}(\rho)=\sum_a K_a\rho K_a^{\dagger},\qquad
\sum_a K_a^{\dagger}K_a=I. \tag{50.8}
$$

Equation (50.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. Unitary evolution is the special case with one Kraus operator. This formulation provides a precise target for any proposed translation, coarse-graining, or projection mechanism that acts on quantum states.

The framework must distinguish three possibilities: a reversible unitary map, an irreversible channel, and a map into a state space that is not yet quantum. Their domains and codomains differ. Calling all three projection would conceal the central typing question.

### 50.9 Fock space for variable particle number

Quantum fields require states with variable excitation number. For a one-particle Hilbert space \(\mathfrak{h}\), the bosonic or fermionic Fock space is

$$
\mathcal{F}_{\pm}(\mathfrak{h})
=\bigoplus_{n=0}^{\infty}\operatorname{Sym}_{\pm}\!\left(\mathfrak{h}^{\otimes n}\right). \tag{50.9}
$$

Equation (50.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. The plus sign denotes symmetric bosonic sectors and the minus sign antisymmetric fermionic sectors. The vacuum is the \(n=0\) sector.

Fock space is not required for every interacting or curved-background formulation, but it is the cleanest setting for the recovered outgoing-mode number operator. It also clarifies the ontological boundary: particle number labels excitations of a mode representation; it need not define a fundamental particle ontology.

### 50.10 Creation and annihilation algebra

For bosonic modes,

$$
[a_k,a_{\ell}^{\dagger}]=\delta_{k\ell},\qquad
[a_k,a_{\ell}]=[a_k^{\dagger},a_{\ell}^{\dagger}]=0. \tag{50.10}
$$

Equation (50.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. Fermionic modes use anticommutators. These relations encode the statistics and normalization of the mode operators; they do not follow merely from the existence of a field bundle or an action functional.

To derive them within the MK-43 handoff, one would need a symplectic or canonical structure, a mode decomposition, a positive-frequency choice where relevant, and a representation of the resulting algebra. Those ingredients form the mathematical bridge between a classical field section and quantum excitations.

### 50.11 Particle number operator

Library 4.1 preserves one exact definition for @particle_number_operator: “Number operator for an outgoing mode.” The standard operator realizing that role is

$$
N_k=a_k^{\dagger}a_k,\qquad
N_k|n_k\rangle=n_k|n_k\rangle,\qquad n_k\in\mathbb{N}_0. \tag{50.11}
$$

Equation (50.11) combines EXACT_SOURCE role evidence with EXTERNAL_ESTABLISHED_MATHEMATICS for the formula. The API classifies the object as an observable and records incoming MEASURED_BY, BLACK_HOLE_MODEL_REACHES, and BLACK_HOLE_GLOBAL_REACHES relations. Those typed graph relations locate use; they do not prove a unique outgoing-mode basis or a black-hole particle-production calculation.

The distinction between exact definition and conventional realization is deliberate. The source supplies the role. The standard formula supplies a mathematically compatible operator once the mode algebra is fixed.

### 50.12 Canonical quantization

For a classical field \(\phi\) with conjugate momentum \(\pi\), canonical quantization seeks operators satisfying equal-time commutation relations

$$
[\widehat{\phi}(t,\mathbf{x}),\widehat{\pi}(t,\mathbf{y})]
=i\hbar\,\delta(\mathbf{x}-\mathbf{y}),\qquad
[\widehat{\phi},\widehat{\phi}]=[\widehat{\pi},\widehat{\pi}]=0. \tag{50.12}
$$

Equation (50.12) is EXTERNAL_ESTABLISHED_MATHEMATICS. It requires a time slicing or equivalent canonical framework and is not automatically available on every background. Gauge systems introduce constraints; interacting theories can require renormalization; curved backgrounds can lack a preferred vacuum.

The MK-43 handoff therefore reaches a quantum input interface before it reaches a unique quantization. A field bundle, connection, section, algebra, and action supply much of the required structure, but the choice of representation and the construction of physical states remain additional operations.

### 50.13 Action and path-integral representation

A formal path-integral expression is

$$
Z=\int\mathcal{D}\phi\,
\exp\!\left(\frac{i}{\hbar}S[\phi]\right),\qquad
\langle\mathcal{O}\rangle
=Z^{-1}\int\mathcal{D}\phi\,\mathcal{O}[\phi]\,
\exp\!\left(\frac{i}{\hbar}S[\phi]\right). \tag{50.13}
$$

Equation (50.13) is EXTERNAL_ESTABLISHED_MATHEMATICS in formal notation. The assigned API address @bulk_action is DECLARED but THIN, with five English units, no equation units, and no registered dependencies. Its title cannot determine that the action component \(\mathcal{S}\) of \(Q\) is a bulk action, nor can it select a measure, boundary conditions, gauge fixing, or regularization.

Path integrals are useful because they connect action data to amplitudes, but their mathematical definition is model dependent. No claim of a complete MK-43 path-integral construction is made here.

### 50.14 Backreaction on geometry

The conventional semiclassical coupling between quantum matter and a classical geometry is represented schematically by

$$
G_{\mu\nu}[g]+\Lambda g_{\mu\nu}
=8\pi G\,\langle T_{\mu\nu}\rangle_{\rho,g}. \tag{50.14}
$$

Equation (50.14) is EXTERNAL_ESTABLISHED_MATHEMATICS, not a recovered equation for @backreaction_on_geometry. It shows the typing challenge: the state and background determine a renormalized stress-energy expectation value, while that expectation value modifies the geometry on which the state was defined.

Backreaction is therefore a self-consistency problem, not a one-way annotation. A complete treatment needs a state prescription, renormalization scheme, field equations, boundary data, conservation, and a controlled approximation. Quantum gravity would require more than the semiclassical equation.

### 50.15 The recovered backreaction address

The API declares @backreaction_on_geometry and records six incoming typed relations but no outgoing relation in its immediate neighborhood. coverage_v2 rates it MEDIUM, yet its two indexed equation units are contaminated by broad canonical source windows and cannot be treated as clean topic-defining formulas. The correct evidence statement is

$$
@\mathrm{backreaction\_on\_geometry}\ \mathrm{is\ addressable}
\quad\not\Rightarrow\quad
\mathrm{a\ complete\ backreaction\ equation\ is\ recovered}. \tag{50.15}
$$

Equation (50.15) is EVIDENCE_BOUNDARY. It preserves the API identity, graph placement, and coherent evidence without laundering unrelated mathematical blocks into the object. Future recovery must isolate exact source units that explicitly type the geometry, quantum state, stress tensor, approximation order, and feedback map.

### 50.16 Evidence calibration

The five assigned handles have the calibrated distribution

$$
N_{\mathrm{assigned}}=5,\qquad
N_{\mathrm{THIN}}=4,\qquad
N_{\mathrm{MEDIUM}}=1. \tag{50.16}
$$

Equation (50.16) is DETERMINISTIC_COVERAGE_EVIDENCE from Library 4.1. Together the handles contain 104 English units, two indexed equation units, and nine registered dependencies. Only @particle_number_operator has a clean exact definition in the compiled semantic records. The chapter therefore uses the API records for address, scope, status, and provenance while labeling conventional state-space formulas separately.

This prevents both underuse and overuse of the corpus. Thin coverage does not make a topic irrelevant, but it limits what can be attributed to recovered MK-43 mathematics.

### 50.17 API evidence register

The register below is generated from the exact Library 4.1 assignment and native query digest.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@backreaction_on_geometry` | @backreaction_on_geometry` — Backreaction on geometry | MEDIUM | 71 / 2 / 6 | chapter-core object |
| `@bulk_action` | @bulk_action` — Bulk Action | THIN | 5 / 0 / 0 | chapter-core object |
| `@hilbert_spaces` | @hilbert_spaces` — Hilbert Spaces | THIN | 12 / 0 / 0 | chapter-core object |
| `@hilbert_spaces_and_density_operators` | @hilbert_spaces_and_density_operators` — Hilbert spaces and density operators | THIN | 11 / 0 / 0 | chapter-core object |
| `@particle_number_operator` | @particle_number_operator | THIN | 5 / 0 / 3 | chapter-core object |

### 50.18 Open bridge obligations

The outstanding bridge from the handoff object to a complete quantum state theory is

$$
\begin{aligned}
\mathfrak{U}_{\mathrm{quant}}=\{&
\mathrm{HilbertRepresentationOf}\ \mathcal{A},
\mathrm{StateMapFrom}\ Q,
\mathrm{BornRuleDerivation},
\mathrm{PositiveFrequencyChoice},\\
&\mathrm{CanonicalOrCovariantQuantization},
\mathrm{ConstraintAndGaugeTreatment},
\mathrm{VacuumSelection},
\mathrm{Renormalization},\\
&\mathrm{ProbabilityPreservation},
\mathrm{GeometryBackreactionMap},
\mathrm{IntertwiningWithUpstreamDynamics},
\mathrm{ExternalValidation}\}.
\end{aligned} \tag{50.18}
$$

Equation (50.18) is CURATOR_SYNTHESIS of the mathematical gaps exposed by the exact handoff structure and the assigned API evidence. It does not invent a missing quantization. It records the definitions, maps, and proofs that a future chapter or recovery pass must supply.

### 50.19 Chapter result

The state and quantization boundary can now be stated precisely:

$$
\boxed{
\begin{aligned}
&\mathrm{STANDARD\ QUANTUM\ STATE\ MATHEMATICS\ SUPPLIED};\\
&\mathrm{MK43\ ADDRESSES\ RETAINED};\\
&\mathrm{UPSTREAM\ QUANTIZATION\ BRIDGE\ OPEN}
\end{aligned}
}. \tag{50.19}
$$

Equation (50.19) is DETERMINISTIC_STATUS_NORMALIZATION. The chapter supplies the conventional Hilbert, density-operator, channel, Fock-space, mode, and quantization structures required to interpret the field-level handoff. It preserves the exact outgoing-mode role of the particle number operator and the recovered backreaction address. It does not claim that thin API titles contain the conventional formulas, that a unique quantization has been derived, or that backreaction and probability preservation have been proved inside the current MK-43 source spine.
