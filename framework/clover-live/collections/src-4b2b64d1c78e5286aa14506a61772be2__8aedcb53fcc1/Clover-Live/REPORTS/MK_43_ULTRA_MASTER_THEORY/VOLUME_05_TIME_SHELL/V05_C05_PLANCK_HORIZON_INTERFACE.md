# VOLUME V - TIME SHELL

## Chapter 45 - Planck-Horizon Interface

### 45.1 API association

API 4.3 declares “Planck horizon translator” as an alias of `@time_shell`. This provides a deterministic address association:

\[
\mathrm{Planck\ horizon\ translator}
\in
\operatorname{Alias}(\mathtt{@time\_shell}).
\tag{45.1}
\]

Equation (45.1) is DETERMINISTIC_API_EVIDENCE. An alias supports invocation and retrieval. It does not, by itself, assert whole-object identity between a Planck Horizon QMO and the Time Shell QMO.

### 45.2 Missing typed identity

Recovery Pass 06D classified the exact relation between Planck Horizon and Time Shell as PARTIALLY_RECOVERED. The missing assertion is

\[
\mathtt{@PlanckHorizon}
\not\equiv_{\mathrm{recovered}}
\mathtt{@time\_shell}.
\tag{45.2}
\]

Equation (45.2) is an EVIDENCE_BOUNDARY statement. The corpus supports translator role, interface, restriction, and correspondence; it does not contain an exact typed identity edge proving equivalence.

### 45.3 Exact horizon pullback

The recovered Time Shell equation ledger contains the exact source equation

\[
\tau_H(y)=\tau(x(y)).
\tag{45.3}
\]

Equation (45.3) is EXACT_SOURCE, equation `ts-eq-09`, from coherent source unit `unit_532a5e48d62d21676f03b4d1cdc0d17efc4ed6b87e37eab7d19520dcdd59cf4d`. It expresses a bulk quantity \(\tau\) evaluated along the embedding or coordinate assignment \(x(y)\) to obtain horizon data \(\tau_H\).

### 45.4 Exact bulk-horizon correspondence

The same source unit gives

\[
\{\tau,\chi,W\}_{\mathrm{bulk}}
\longleftrightarrow
\{\tau_H,\chi_H,W_H\}_{\mathrm{horizon}}.
\tag{45.4}
\]

Equation (45.4) is EXACT_SOURCE, equation `ts-eq-10`. It preserves a correspondence among the temporal or phase quantity \(\tau\), chirality \(\chi\), and the source quantity \(W\). The double arrow does not specify bijectivity, invertibility, or dynamics.

### 45.5 Restriction interpretation

Equations (45.3) and (45.4) support a restriction picture

\[
\operatorname{res}_{H}:
(\tau,\chi,W)_{\mathrm{bulk}}
\dashrightarrow
(\tau_H,\chi_H,W_H).
\tag{45.5}
\]

Equation (45.5) is DETERMINISTIC_NORMALIZATION of the exact source equations. The dashed arrow marks incomplete typing: the source does not provide the bulk space, horizon space, regularity class, or proof that all three fields share one restriction operator.

### 45.6 Interface rather than identity

The evidence supports the scoped relation

\[
\mathfrak{T}_{\mathrm{S}}
\supset
\mathfrak{I}_{H},
\qquad
\mathfrak{I}_{H}
\sim
\operatorname{PlanckHorizonInterface},
\tag{45.6}
\]

where \(\mathfrak{I}_{H}\) denotes the candidate horizon-facing sector of the Time Shell. Equation (45.6) is CLOVER_SYNTHESIS. Neither inclusion nor similarity is claimed as a recovered set-theoretic or categorical theorem.

### 45.7 Horizon readability

The broader Genesis ruling places the Time Shell at the boundary through which Planck-Landscape organization becomes readable. A type-neutral publication decomposition is

\[
\mathcal{O}_{\mathrm{PL}}
\xrightarrow{\ \operatorname{res}_{H}\ }
\mathcal{O}_{H}
\dashrightarrow
\mathcal{O}_{\mathrm{readable}}.
\tag{45.7}
\]

Equation (45.7) is CURATOR_SYNTHESIS. The first arrow is motivated by exact restriction evidence; the second remains the broader candidate translation problem.

### 45.8 Proto-locality at the interface

The assigned address `@factorisation_and_proto_locality` is THIN and carries no equation or dependency units. It nevertheless names the exact conceptual issue at the horizon boundary: whether upstream organization factors into locally readable sectors. The missing map is

\[
\mathcal{F}_{H}:
\mathcal{O}_{H}
\dashrightarrow
\bigotimes_{i}\mathcal{O}_{H,i}.
\tag{45.8}
\]

Equation (45.8) is CLOVER_SYNTHESIS. No factorization theorem is inferred from the handle title.

### 45.9 Continuum locality

`@emergence_of_continuum_locality` is also THIN, with one English unit and no native equations. The candidate downstream limit is

\[
\bigotimes_i\mathcal{O}_{H,i}
\dashrightarrow
\mathcal{O}_{\mathrm{continuum\ local}}.
\tag{45.9}
\]

Equation (45.9) is CLOVER_SYNTHESIS. A continuum limit, scaling law, topology, and convergence proof remain absent from the assigned address.

### 45.10 Inheritance across the interface

The `@inheritance` address is MEDIUM, with 6,259 unique substantive units, seven equation units, and 214 dependencies. The interface problem asks whether inherited structure is preserved under restriction:

\[
\operatorname{res}_{H}\circ\mathcal{I}_{\mathrm{bulk}}
\overset{?}{=}
\mathcal{I}_{H}\circ\operatorname{res}_{H}.
\tag{45.10}
\]

Equation (45.10) is CLOVER_SYNTHESIS naming a commutation obligation. The coverage record has zero theorem/proof units, so no compatibility theorem is claimed.

### 45.11 Oriented inheritance

The MEDIUM handle `@oriented_inheritance` has 413 unique units, two equation units, an incoming ORIENTS_TO edge, and an outgoing COMPOSES_BY edge. Its candidate role at the interface is

\[
\mathcal{I}_{H}^{\mathrm{oriented}}
=
\mathcal{O}_{\chi,H}\circ\mathcal{I}_{H}.
\tag{45.11}
\]

Equation (45.11) is CLOVER_SYNTHESIS. The API neighborhood supports orientation and composition as distinct relation types, not this exact formula.

### 45.12 API evidence register

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@emergence_of_continuum_locality` | @emergence_of_continuum_locality` — Emergence of Continuum Locality | THIN | 1 / 0 / 0 | chapter-core object |
| `@factorisation_and_proto_locality` | @factorisation_and_proto_locality` — Factorisation and Proto--Locality | THIN | 2 / 0 / 0 | chapter-core object |
| `@inheritance` | @inheritance` — Inheritance | MEDIUM | 317 / 7 / 214 | chapter-core object |
| `@oriented_inheritance` | Oriented Inheritance | MEDIUM | 60 / 2 / 2 | chapter-core object |

All four assigned addresses are represented. Inheritance and oriented inheritance carry substantive metadata; continuum locality and proto-locality remain thin navigation addresses.

### 45.13 Evidence calibration

The two substantive assigned vectors are

\[
\mathbf{E}(\mathtt{@inheritance})
=(6259,347,317,7,0,214),
\tag{45.12}
\]

\[
\mathbf{E}(\mathtt{@oriented\_inheritance})
=(413,109,60,2,0,2).
\tag{45.13}
\]

Equations (45.12) and (45.13) are CLOVER_SYNTHESIS reporting \(U/S/E/Q/T/D\). Both theorem/proof counts are zero.

### 45.14 Interface obligations

The Planck-horizon interface remains incomplete in precisely delimited ways:

\[
\mathfrak{O}_{H}
=
(\operatorname{Type}H,
\operatorname{Dom}\operatorname{res}_{H},
\operatorname{Cod}\operatorname{res}_{H},
\mathcal{F}_{H},
\operatorname{ContinuumLimit},
\operatorname{InheritanceCompatibility},
\operatorname{TypedIdentity}).
\tag{45.14}
\]

Equation (45.14) is CLOVER_SYNTHESIS. The final TypedIdentity entry remains missing and must not be backfilled from the alias.

### 45.15 Chapter result

The evidence-aware interface is

\[
\boxed{
(\tau,\chi,W)_{\mathrm{bulk}}
\longleftrightarrow
(\tau_H,\chi_H,W_H)_{\mathrm{horizon}}
\quad\text{without recovered whole-object identity}
}.
\tag{45.15}
\]

Equation (45.15) is CURATOR_SYNTHESIS anchored to exact equations (45.3) and (45.4). Chapter 46 next examines the projection and intertwining requirements that would be needed to turn interface data into a dynamical bridge.

