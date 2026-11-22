# VOLUME XII - DARK MATTER AND RELATIONAL STRUCTURE

## Chapter 96 - Dark-Matter Transport and Bridges

### 96.1 Conserved transport

A transported density rho with current J satisfies

$$
\partial_t\rho+\nabla\cdot\mathbf J=0. \tag{96.1}
$$

Equation (96.1) is EXTERNAL_ESTABLISHED_MATHEMATICS. A bridge model must first identify what quantity is conserved and on which space it lives.

### 96.2 Advective current

For bulk velocity v,

$$
\mathbf J_{\mathrm{adv}}=\rho\mathbf v. \tag{96.2}
$$

Equation (96.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. It describes ordinary spatial flow, not nonlocal bridge transfer.

### 96.3 Diffusive current

Fick transport is represented by

$$
\mathbf J_{\mathrm{diff}}=-D\nabla\rho. \tag{96.3}
$$

Equation (96.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. Positivity and dimensions of D are required for a physical interpretation.

### 96.4 Advection-diffusion equation

Combining the standard currents gives

$$
\partial_t\rho+\nabla\cdot(\rho\mathbf v)
=\nabla\cdot(D\nabla\rho). \tag{96.4}
$$

Equation (96.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. It supplies a comparison model for local transport.

### 96.5 Transport on an expanding background

For a homogeneous nonrelativistic density,

$$
\dot{\bar\rho}+3H\bar\rho=0. \tag{96.5}
$$

Equation (96.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. Any bridge exchange must preserve or explicitly modify the cosmological conservation law.

### 96.6 Collisionless phase-space flow

A collisionless distribution f obeys

$$
\frac{\partial f}{\partial t}
+\dot{\mathbf x}\cdot\nabla_{\mathbf x}f
+\dot{\mathbf p}\cdot\nabla_{\mathbf p}f=0. \tag{96.6}
$$

Equation (96.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. It is the conventional transport baseline for cold dark matter.

### 96.7 Graph-edge current

On a weighted network, an antisymmetric edge current may be written

$$
J_{ij}=\gamma_{ij}(u_i-u_j),
\qquad J_{ij}=-J_{ji}. \tag{96.7}
$$

Equation (96.7) is EXTERNAL_ESTABLISHED_MATHEMATICS as a network-flow schema.

### 96.8 Vertex conservation

Local conservation on the network requires

$$
\dot q_i+\sum_jJ_{ij}=s_i. \tag{96.8}
$$

Equation (96.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. Sources and sinks must sum consistently with any claimed global conservation.

### 96.9 Laplacian transport

With linear edge currents, network evolution becomes

$$
\dot{\mathbf q}=-L_\gamma\mathbf q+\mathbf s. \tag{96.9}
$$

Equation (96.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. A native bridge theory must derive the weighted Laplacian and state its units.

### 96.10 Propagator

For time-independent linear transport without sources,

$$
\mathbf q(t)=e^{-tL_\gamma}\mathbf q(0). \tag{96.10}
$$

Equation (96.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. It is a diffusive propagator and does not establish superluminal or topology-changing motion.

### 96.11 Bridge-transfer operator

A genuine bridge mechanism would require

$$
\mathcal B_{ij}:\mathcal H_i\longrightarrow\mathcal H_j. \tag{96.11}
$$

Equation (96.11) is EVIDENCE_BOUNDARY. The assigned Library handle does not recover endpoint state spaces, an operator kernel, or a physical transfer law.

### 96.12 Endpoint contract

A bridge instance can be typed as

$$
b=(i,j,\mathcal D_i,\mathcal D_j,K_b,\tau_b,c_b). \tag{96.12}
$$

Equation (96.12) is DETERMINISTIC_TYPE_NORMALIZATION. Endpoints, domains, kernel, characteristic time, and capacity are kept distinct; the tuple is not exact native source notation.

### 96.13 Causality boundary

Any continuum realization must establish a causal condition such as

$$
\operatorname{supp}G_{\mathrm{ret}}(x,x')
\subseteq J^+(x'). \tag{96.13}
$$

Equation (96.13) is EVIDENCE_BOUNDARY. A nonlocal graph edge does not automatically define a causal spacetime channel.

### 96.14 Global conservation

For a closed bridge network,

$$
\frac{d}{dt}\sum_i q_i=0 \tag{96.14}
$$

requires antisymmetric internal currents and zero net source. Equation (96.14) is EVIDENCE_BOUNDARY in the native context because no assigned action or conservation proof is recovered.

### 96.15 Gravitational backreaction

Load-bearing transport requires a source map

$$
(q_i,J_{ij},\mathcal B_{ij})
\longrightarrow T_{\mu\nu}^{\mathrm{bridge}}. \tag{96.15}
$$

Equation (96.15) is EVIDENCE_BOUNDARY. Without this map, transport cannot be connected consistently to lensing, dynamics, or cosmological growth.

### 96.16 Discriminating signal

A bridge-specific observable must separate from standard transport,

$$
\Delta\mathcal O_{\mathrm{bridge}}
=\mathcal O_{\mathrm{network}}-\mathcal O_{\mathrm{collisionless}}. \tag{96.16}
$$

Equation (96.16) is EVIDENCE_BOUNDARY. No assigned prediction specifies the sign, scale, or uncertainty of this difference.

### 96.17 Typed chapter contract

The chapter therefore records

$$
\mathfrak M_{96}=(\rho,\mathbf J,f,q_i,J_{ij},L_\gamma,
\mathcal B_{ij},T_{\mu\nu}^{\mathrm{bridge}},\Delta\mathcal O,\Omega_{96}). \tag{96.17}
$$

Equation (96.17) is DETERMINISTIC_TYPE_NORMALIZATION. Local flow, network flow, bridge operator, gravitational source, observation, and open requirements remain distinct.

### 96.18 Coverage calibration

The native query returned

$$
N_{\mathrm{assigned}}=1,
\quad N_{\mathrm{English}}=4,
\quad N_{\mathrm{equation}}=0,
\quad N_{\mathrm{dependency}}=0. \tag{96.18}
$$

Equation (96.18) is DETERMINISTIC_COVERAGE_EVIDENCE. The sole assigned handle is THIN and has no exact definition or equation unit.

### 96.19 API evidence register

| API handle | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---:|---:|---|
| `@dark_matter_bridges_and_transport` | THIN | 4 / 0 / 0 | native title boundary |

The register supplies an exact mathematical address and minimal prose context, but not a transport model.

### 96.20 Evidence boundary

The controlling distinction is

$$
\mathrm{BridgeVocabulary}
\ne
\mathrm{TransferOperator},
\qquad
\mathrm{NetworkFlow}
\ne
\mathrm{DarkMatterTransportLaw}. \tag{96.19}
$$

Equation (96.19) is EVIDENCE_BOUNDARY. The native title cannot inherit standard diffusion or graph equations as though they were recovered framework claims.

### 96.21 Open transport obligations

The unresolved work is

$$
\begin{aligned}
\Omega_{96}=\{&\mathrm{TransportedQuantity},\mathrm{EndpointTypes},
\mathrm{BridgeKernel},\mathrm{RateLaw},\\
&\mathrm{CapacityUnits},\mathrm{CausalityProof},
\mathrm{ConservationProof},\mathrm{CosmologicalEmbedding},\\
&\mathrm{StressEnergyMap},\mathrm{DiscriminatingPrediction},
\mathrm{ExternalValidation}\}.
\end{aligned} \tag{96.20}
$$

Equation (96.20) is CURATOR_SYNTHESIS. It records the minimum mathematical and empirical completion needed for bridge transport.

### 96.22 Chapter determination

The chapter result is

$$
\begin{aligned}
\mathrm{Transport}_{96}={}&\mathrm{ESTABLISHED\_LOCAL\_AND\_GRAPH\_SCAFFOLD}
+\mathrm{ONE\_THIN\_NATIVE\_ADDRESS}\\
&+\mathrm{EXPLICIT\_BRIDGE\_OPERATOR\_BOUNDARY}
+\mathrm{OPEN\_PHYSICAL\_TRANSPORT\_LAW}.
\end{aligned} \tag{96.21}
$$

Equation (96.21) is DETERMINISTIC_STATUS_NORMALIZATION. Dark-matter bridges and transport remain a formal research target rather than a recovered mechanism.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@dark_matter_bridges_and_transport` | @dark_matter_bridges_and_transport` — Dark Matter Bridges and Transport | THIN | 4 / 0 / 0 | chapter-core object |
