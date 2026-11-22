# VOLUME VIII - MATTER AND ENERGY

## Chapter 68 - Motes, Occupancy, and Organized Matter

### 68.1 A discrete organizational substrate

Let \(\mathcal S\) denote a set of distinguishable sites. A minimal binary occupancy assignment is a function

$$
o:\mathcal S\longrightarrow\{0,1\},
\qquad
o(s)=
\begin{cases}
1,&s\text{ occupied},\\
0,&s\text{ unoccupied}.
\end{cases} \tag{68.1}
$$

Equation (68.1) is EXTERNAL_ESTABLISHED_MATHEMATICS as a discrete-state schema. It supplies a typed reading of occupancy without claiming that the recovered MK-43 sources have fixed the codomain of `@mote_occupancy_function` universally.

### 68.2 Sites, states, and identities

A site label and an occupant identity are different data. If \(\mathcal M\) is a set of mote identities, a partial configuration may be typed as

$$
\mu:\mathcal S\rightharpoonup\mathcal M,
\qquad
o(s)=1\iff s\in\operatorname{dom}(\mu). \tag{68.2}
$$

Equation (68.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. A mote is not identified with the location at which it is represented, and relocation need not destroy identity.

### 68.3 Configuration space

For a finite site set, the binary occupancy space is

$$
\Omega_{\mathcal S}=\{0,1\}^{\mathcal S}. \tag{68.3}
$$

Equation (68.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. Each point of \(\Omega_{\mathcal S}\) is a complete occupancy pattern; it is not yet a dynamical history, a particle theory, or a matter realization.

### 68.4 Occupancy number

The total occupation of a finite configuration is

$$
N[o]=\sum_{s\in\mathcal S}o(s). \tag{68.4}
$$

Equation (68.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. Whether \(N\) is conserved depends on the allowed transitions, not on the definition of occupancy alone.

### 68.5 Complement rule

A binary complement may be defined pointwise by

$$
\bar o(s)=1-o(s),
\qquad
\bar{\bar o}=o. \tag{68.5}
$$

Equation (68.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. It is a candidate typing for the address `@mote_complement_rule`; because that handle is THIN and has no indexed equation unit, it is not represented as a recovered native formula.

### 68.6 The vacant configuration

The empty occupancy state is

$$
o_{\varnothing}(s)=0
\quad\text{for every }s\in\mathcal S. \tag{68.6}
$$

Equation (68.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. The API title “Definition 14.2 — Mote Vacuum” is recovered, and its handle has one definition unit, but the present query does not justify equating every physical vacuum concept with the all-zero configuration.

### 68.7 Layer decomposition

If sites are organized into disjoint layers \(\mathcal S_\ell\), then

$$
\mathcal S=\bigsqcup_{\ell\in L}\mathcal S_\ell,
\qquad
N_\ell[o]=\sum_{s\in\mathcal S_\ell}o(s). \tag{68.7}
$$

Equation (68.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. It gives a precise generic meaning to “layer” while leaving the native layer index, adjacency, and inter-layer maps unresolved for `@mote_layer`.

### 68.8 Chirality and occupancy

With chirality labels \(\chi\in\{-1,+1\}\), a chirality-occupancy state can be represented in

$$
\mathcal C_{\mathrm{occ}}
=\mathcal S\times\{-1,+1\}\times\{0,1\}. \tag{68.8}
$$

Equation (68.8) is EXTERNAL_ESTABLISHED_MATHEMATICS as a product-type schema. It does not prove that `@chirality_occupancy_cube` is literally this Cartesian product; that handle is MEDIUM and contains two indexed equation units whose exact native typing remains authoritative.

### 68.9 Chiral population balance

For an occupied state with chirality field \(\chi_s\), define

$$
N_\pm[o,\chi]
=\sum_{s\in\mathcal S}
o(s)\,\mathbf 1_{\{\chi_s=\pm1\}},
\qquad
\Delta_\chi=N_+-N_-. \tag{68.9}
$$

Equation (68.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. It distinguishes population imbalance from the chirality label itself.

### 68.10 Local exclusion

Binary occupancy enforces the algebraic relation

$$
o(s)^2=o(s). \tag{68.10}
$$

Equation (68.10) is EXTERNAL_ESTABLISHED_MATHEMATICS for \(o(s)\in\{0,1\}\). It states idempotence of a binary variable, not a recovered fermionic anticommutation law.

### 68.11 Adjacency and organized patterns

Let \(A_{st}\) be an adjacency matrix on \(\mathcal S\). A generic local organization functional is

$$
E[o]
=\sum_{s\in\mathcal S}\epsilon_s o(s)
+\frac12\sum_{s,t\in\mathcal S}J_{st}o(s)o(t). \tag{68.11}
$$

Equation (68.11) is EXTERNAL_ESTABLISHED_MATHEMATICS as a finite-state model. The coefficients are not recovered MK-43 constants, and no native energy interpretation is inferred from the occupancy address.

### 68.12 Allowed transitions

A discrete evolution is specified by a transition kernel

$$
K:\Omega_{\mathcal S}\times\Omega_{\mathcal S}\longrightarrow[0,1],
\qquad
\sum_{o'\in\Omega_{\mathcal S}}K(o,o')=1. \tag{68.12}
$$

Equation (68.12) is EXTERNAL_ESTABLISHED_MATHEMATICS for a stochastic model. A deterministic rule is the special case in which each row has a single unit entry.

### 68.13 Conservation under transport

For number-preserving transitions,

$$
K(o,o')>0
\quad\Longrightarrow\quad
N[o']=N[o]. \tag{68.13}
$$

Equation (68.13) is EXTERNAL_ESTABLISHED_MATHEMATICS. Creation, annihilation, or exchange with an environment requires a different rule and must be declared explicitly.

### 68.14 Coarse-grained density

For a region \(R\subseteq\mathcal S\), define

$$
\rho_R[o]=\frac{1}{|R|}\sum_{s\in R}o(s),
\qquad
0\le\rho_R\le1. \tag{68.14}
$$

Equation (68.14) is EXTERNAL_ESTABLISHED_MATHEMATICS. It maps a microscopic occupancy pattern to a regional statistic but does not by itself establish organized matter.

### 68.15 Realization criterion

A matter interpretation requires a declared realization map

$$
\mathfrak M:
\Omega_{\mathcal S}^{\mathrm{adm}}
\longrightarrow
\mathcal F_{\mathrm{matter}},
\qquad
o\longmapsto\mathfrak M[o]. \tag{68.15}
$$

Equation (68.15) is EXTERNAL_ESTABLISHED_MATHEMATICS as a typing requirement. Occupancy data become organized matter only after admissibility, dynamics, observable content, and the realization map are defined.

### 68.16 Typed mote-occupancy contract

The disciplined separation is

$$
\mathcal S
\xrightarrow{\ o\ }
\Omega_{\mathcal S}
\xrightarrow{\ \mathrm{constraints}\ }
\Omega_{\mathcal S}^{\mathrm{adm}}
\xrightarrow{\ \mathfrak M\ }
\mathcal F_{\mathrm{matter}}
\xrightarrow{\ \mathrm{observables}\ }
\mathcal O. \tag{68.16}
$$

Equation (68.16) is DETERMINISTIC_TYPE_NORMALIZATION. It prevents a site, a mote identity, an occupancy bit, an admissible pattern, and a realized matter object from being silently collapsed.

### 68.17 Coverage calibration

The chapter assignment contains

$$
N_{\mathrm{assigned}}=9,
\qquad
N_{\mathrm{MEDIUM}}=5,
\qquad
N_{\mathrm{THIN}}=4. \tag{68.17}
$$

Equation (68.17) is DETERMINISTIC_COVERAGE_EVIDENCE. The handles contain 423 English units, 19 indexed equation units, one definition unit, and 214 registered dependencies. `@occupancy` alone supplies 260 English units, seven equations, and 208 dependencies.

### 68.18 API evidence register

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@chirality_occupancy_cube` | New Handle — @chirality_occupancy_cube | MEDIUM | 79 / 2 / 3 | chapter-core object |
| `@definition_14_2_mote_vacuum` | @definition_14_2_mote_vacuum` — Definition 14.2 — Mote Vacuum | MEDIUM | 3 / 0 / 0 | chapter-core object |
| `@genesis_algebra_and_the_mote` | @genesis_algebra_and_the_mote` — Genesis Algebra and the Mote | THIN | 12 / 0 / 0 | chapter-core object |
| `@genesis_occupancy` | @genesis_occupancy | THIN | 1 / 0 / 0 | chapter-core object |
| `@mote_complement_rule` | @mote_complement_rule | THIN | 1 / 0 / 0 | chapter-core object |
| `@mote_identity` | @mote_identity | MEDIUM | 29 / 3 / 1 | chapter-core object |
| `@mote_layer` | @mote_layer | THIN | 1 / 0 / 0 | chapter-core object |
| `@mote_occupancy_function` | New Handle — @mote_occupancy_function | MEDIUM | 37 / 7 / 2 | chapter-core object |
| `@occupancy` | @occupancy` — Occupancy | MEDIUM | 260 / 7 / 208 | chapter-core object |

The register preserves the API address space and its recovered evidence counts. Dependency abundance for `@occupancy` does not substitute for a complete native definition or realization theorem.

### 68.19 Evidence boundary

The operative distinctions are

$$
\begin{aligned}
\mathrm{MoteIdentity}&\ne\mathrm{SiteIdentity},\\
\mathrm{OccupancyBit}&\ne\mathrm{MatterObject},\\
\mathrm{VacantConfiguration}&\ne\mathrm{PhysicalVacuum},\\
\mathrm{GraphDependency}&\ne\mathrm{DynamicalLaw}.
\end{aligned} \tag{68.18}
$$

Equation (68.18) is EVIDENCE_BOUNDARY. Native titles, linked equations, and dependency edges are retained without importing unstated ontology or dynamics.

### 68.20 Open organizational obligations

The unresolved requirements are

$$
\begin{aligned}
\mathfrak U_{\mathrm{mote}}=\{&
\mathrm{NativeMoteDefinition},
\mathrm{SiteSpace},
\mathrm{OccupancyCodomain},
\mathrm{ComplementTyping},
\mathrm{LayerStructure},\\
&\mathrm{ChiralityCoupling},
\mathrm{TransitionLaw},
\mathrm{ConservationRules},
\mathrm{VacuumInterpretation},
\mathrm{AdmissibilityPredicate},\\
&\mathrm{MatterRealizationMap},
\mathrm{ObservableDictionary},
\mathrm{StabilityProof},
\mathrm{ExperimentalValidation}\}.
\end{aligned} \tag{68.19}
$$

Equation (68.19) is CURATOR_SYNTHESIS. It enumerates missing mathematical and empirical work without completing it.

### 68.21 Chapter determination

The result is

$$
\begin{aligned}
\mathrm{MoteOccupancy}_{\mathrm{V08C02}}
={}&\mathrm{RECOVERED\_API\_ADDRESS\_SPACE}\\
&+\mathrm{QUALIFIED\_DISCRETE\_STATE\_SCHEMAS}\\
&+\mathrm{OPEN\_NATIVE\_DYNAMICS\_AND\_REALIZATION}.
\end{aligned} \tag{68.20}
$$

Equation (68.20) is DETERMINISTIC_STATUS_NORMALIZATION. The chapter supplies a coherent typed framework for discussing motes and occupancy while leaving native mote ontology, exact dynamics, matter realization, proof, and experimental status open where the recovered evidence does not settle them.
