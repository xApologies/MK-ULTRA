# VOLUME VIII - MATTER AND ENERGY

## Chapter 73 - Matter-Energy Conservation and Transport

### 73.1 Local energy-momentum conservation

For a closed covariant matter system,

$$
\nabla_\mu T^{\mu\nu}=0. \tag{73.1}
$$

Equation (73.1) is EXTERNAL_ESTABLISHED_MATHEMATICS. `@local_energy_momentum_conservation` is MEDIUM and densely connected, but application to motes requires a recovered or defined stress-energy tensor.

### 73.2 Observer energy current

Given a time-flow vector \(\xi^\nu\), define the current

$$
J^\mu_{(\xi)}=T^{\mu}{}_{\nu}\xi^\nu. \tag{73.2}
$$

Equation (73.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. Its divergence vanishes when \(T^{\mu\nu}\) is conserved and \(\xi\) is an appropriate symmetry generator.

### 73.3 Regional balance law

For a spacetime region \(\mathcal V\), the divergence theorem gives

$$
\int_{\mathcal V}\nabla_\mu J^\mu\,dV
=\int_{\partial\mathcal V}J^\mu n_\mu\,d\Sigma. \tag{73.3}
$$

Equation (73.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. Change inside a region and transport across its boundary are complementary parts of one balance statement.

### 73.4 Continuity equation

In a nonrelativistic decomposition,

$$
\partial_t\rho_E+\nabla\cdot\mathbf j_E=s_E. \tag{73.4}
$$

Equation (73.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. The source \(s_E\) vanishes for a closed local energy sector; nonzero \(s_E\) must be matched by exchange with another sector.

### 73.5 Lattice continuity

On a mote lattice with site energies \(E_s\) and directed currents \(j_{s\to t}\), a discrete balance is

$$
\frac{dE_s}{dt}
+\sum_{t\sim s}j_{s\to t}
=s_s. \tag{73.5}
$$

Equation (73.5) is EXTERNAL_ESTABLISHED_MATHEMATICS as a graph-continuity schema. `@mote_lattice` is MEDIUM, but the native adjacency, energy assignment, and current law remain required.

### 73.6 Antisymmetric transport

If internal transport obeys

$$
j_{s\to t}=-j_{t\to s}, \tag{73.6}
$$

then summing (73.5) over a closed finite lattice cancels internal flows. Equation (73.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Boundary edges and sources remain visible.

### 73.7 Global lattice energy

Define

$$
E_{\mathrm{lat}}=\sum_sE_s. \tag{73.7}
$$

For a closed lattice with antisymmetric internal currents and \(s_s=0\), \(dE_{\mathrm{lat}}/dt=0\). Equation (73.7) is EXTERNAL_ESTABLISHED_MATHEMATICS.

### 73.8 Mote Hilbert space

Let \(\mathcal H_{\mathrm{mote}}\) be a Hilbert space with normalized state \(|\Psi\rangle\),

$$
\langle\Psi|\Psi\rangle=1. \tag{73.8}
$$

Equation (73.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. The API title “Definition 14.1 — Mote Hilbert Space” and one definition unit are recovered, but the exact native inner product and basis remain authoritative.

### 73.9 Creation and annihilation operators

For a bosonic mode as a generic comparison,

$$
[a_s,a_t^\dagger]=\delta_{st},
\qquad
[a_s,a_t]=[a_s^\dagger,a_t^\dagger]=0. \tag{73.9}
$$

Equation (73.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. `@mote_creation_operator` is MEDIUM, but no bosonic, fermionic, or other native algebra is inferred without exact evidence.

### 73.10 Number operator

In that comparison model,

$$
N=\sum_s a_s^\dagger a_s. \tag{73.10}
$$

Equation (73.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. A mote-creation event changes number only if the native state space and operator algebra give \([N,a_s^\dagger]=a_s^\dagger\).

### 73.11 Energy cost of creation

For Hamiltonian \(H\), the energy change induced in a normalized state is

$$
\Delta E_s
=\frac{\langle\Psi|a_s H a_s^\dagger|\Psi\rangle}
{\langle\Psi|a_s a_s^\dagger|\Psi\rangle}
-\langle\Psi|H|\Psi\rangle. \tag{73.11}
$$

Equation (73.11) is EXTERNAL_ESTABLISHED_MATHEMATICS as a conditional operator expression. It does not supply the native creation energy.

### 73.12 Creation event as a transition

A creation event can be typed abstractly as

$$
\mathfrak C_s:
\mathcal H_N\longrightarrow\mathcal H_{N+1}. \tag{73.12}
$$

Equation (73.12) is EXTERNAL_ESTABLISHED_MATHEMATICS as a graded-space schema. The title “Definition 11.2 — Mote Creation Event” and one definition unit are recovered, but the native map and admissibility conditions are not invented.

### 73.13 Matter identity

A mote definition and a creation operator answer different questions:

$$
\mathrm{ObjectType}(m)
\quad\text{versus}\quad
\mathfrak C_s(|\Psi\rangle). \tag{73.13}
$$

Equation (73.13) is EXTERNAL_ESTABLISHED_MATHEMATICS as a type distinction. The title “Definition 12.1 — Mote” and its definition unit do not specify how creation proceeds.

### 73.14 Unitary transport

For a closed quantum system,

$$
i\hbar\frac{d}{dt}|\Psi(t)\rangle
=H|\Psi(t)\rangle,
\qquad H=H^\dagger. \tag{73.14}
$$

Equation (73.14) is EXTERNAL_ESTABLISHED_MATHEMATICS. If \(H\) is time independent, \(\langle H\rangle\) is conserved under this evolution.

### 73.15 Exchange between matter and field sectors

For coupled subsystems,

$$
\nabla_\mu T^{\mu\nu}_{\mathrm{mote}}=Q^\nu,
\qquad
\nabla_\mu T^{\mu\nu}_{\mathrm{field}}=-Q^\nu. \tag{73.15}
$$

Equation (73.15) is EXTERNAL_ESTABLISHED_MATHEMATICS. Local mote energy may change while total stress-energy remains conserved; the exchange current must be derived, not assumed.

### 73.16 Typed conservation-and-transport contract

The disciplined chain is

$$
(\mathcal H_{\mathrm{mote}},H,\mathfrak C)
\longmapsto
T^{\mu\nu}_{\mathrm{mote}}
\longmapsto
J_E^\mu
\longmapsto
\big(\mathrm{local\ balance},\mathrm{boundary\ flux}\big). \tag{73.16}
$$

Equation (73.16) is DETERMINISTIC_TYPE_NORMALIZATION. It separates state space, dynamics, creation, stress-energy, current, and transport.

### 73.17 Coverage calibration

The chapter assignment contains

$$
N_{\mathrm{assigned}}=6,
\qquad
N_{\mathrm{MEDIUM}}=6,
\qquad
N_{\mathrm{THIN}}=0. \tag{73.17}
$$

Equation (73.17) is DETERMINISTIC_COVERAGE_EVIDENCE. The handles contain 254 English units, 16 indexed equation units, three definition units, and 226 registered dependencies. `@local_energy_momentum_conservation` contributes 116 English units, five equations, and 218 dependencies.

### 73.18 API evidence register

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@definition_11_2_mote_creation_event` | @definition_11_2_mote_creation_event` — Definition 11.2 — Mote Creation Event | MEDIUM | 4 / 0 / 0 | chapter-core object |
| `@definition_12_1_mote` | @definition_12_1_mote` — Definition 12.1 — Mote | MEDIUM | 4 / 0 / 0 | chapter-core object |
| `@definition_14_1_mote_hilbert_space` | @definition_14_1_mote_hilbert_space` — Definition 14.1 — Mote Hilbert Space | MEDIUM | 3 / 0 / 0 | chapter-core object |
| `@local_energy_momentum_conservation` | @local_energy_momentum_conservation | MEDIUM | 116 / 5 / 218 | chapter-core object |
| `@mote_creation_operator` | Thickened Handle — @mote_creation_operator | MEDIUM | 49 / 4 / 4 | chapter-core object |
| `@mote_lattice` | New Handle — @mote_lattice | MEDIUM | 78 / 7 / 4 | chapter-core object |

The register preserves the three numbered definition addresses, local conservation, the creation operator, and the lattice independently. All are MEDIUM, but their combination is not itself a recovered theorem.

### 73.19 Evidence boundary

The operative distinctions are

$$
\begin{aligned}
\mathrm{MoteDefinition}&\ne\mathrm{CreationEvent},\\
\mathrm{CreationEvent}&\ne\mathrm{CreationOperator},\\
\mathrm{LocalConservation}&\ne\mathrm{ZeroRegionalChange},\\
\mathrm{LatticeTransport}&\ne\mathrm{ContinuumStressTensor}.
\end{aligned} \tag{73.18}
$$

Equation (73.18) is EVIDENCE_BOUNDARY. Transport across a boundary, exchange between sectors, and object creation remain compatible with total conservation only when the full balance is explicit.

### 73.20 Open conservation obligations

The unresolved requirements are

$$
\begin{aligned}
\mathfrak U_{\mathrm{transport}}=\{&
\mathrm{ExactMoteDefinition},
\mathrm{NativeHilbertSpace},
\mathrm{CreationAlgebra},
\mathrm{Hamiltonian},
\mathrm{LatticeAdjacency},\\
&\mathrm{SiteEnergy},
\mathrm{CurrentLaw},
\mathrm{ExchangeCurrent},
\mathrm{StressTensorMap},
\mathrm{BoundaryConditions},\\
&\mathrm{CreationEnergy},
\mathrm{ContinuumLimit},
\mathrm{StabilityProof},
\mathrm{MeasurementProtocol},
\mathrm{ExperimentalValidation}\}.
\end{aligned} \tag{73.19}
$$

Equation (73.19) is CURATOR_SYNTHESIS. It records what remains before mote creation and lattice transport become a closed conservation theory.

### 73.21 Chapter determination

The result is

$$
\begin{aligned}
\mathrm{Transport}_{\mathrm{V08C07}}
={}&\mathrm{RECOVERED\_MOTE\_LATTICE\_AND\_CONSERVATION\_ADDRESSES}\\
&+\mathrm{ESTABLISHED\_LOCAL\_AND\_DISCRETE\_BALANCE\_SCHEMAS}\\
&+\mathrm{OPEN\_NATIVE\_CREATION\_DYNAMICS\_AND\_CONTINUUM\_MAP}.
\end{aligned} \tag{73.20}
$$

Equation (73.20) is DETERMINISTIC_STATUS_NORMALIZATION. The chapter makes conservation compatible with transport and creation through explicit source and flux bookkeeping while preserving the missing native operator algebra, Hamiltonian, stress tensor, continuum limit, and validation.
