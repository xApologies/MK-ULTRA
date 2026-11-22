# VOLUME XVIII - MATHEMATICAL APPENDICES

## Chapter 142 - Quantum and Field-Theory Conventions

### 142.1 Quantum convention record

A quantum convention must declare its state space, scalar field, inner-product order, observable class, time parameter, units, measurement rule, field domain, action sign, and provenance,

$$
\mathfrak Q=(\mathcal H,\mathbb K,\langle\cdot,\cdot\rangle,\mathcal O,t,\hbar,\mathsf M,X,S,p). \tag{142.1}
$$

Equation (142.1) is DETERMINISTIC_TYPE_NORMALIZATION. It is a comparison record, not an assertion that every MK-43 object already possesses all ten coordinates.

### 142.2 State and normalization

In the standard complex-Hilbert-space convention, a pure state is a ray represented by a unit vector,

$$
|\psi\rangle\in\mathcal H,\qquad \langle\psi|\psi\rangle=1. \tag{142.2}
$$

Equation (142.2) is EXTERNAL_ESTABLISHED_MATHEMATICS. A source-specific state space cannot inherit Hilbert structure merely from quantum terminology.

### 142.3 Observables and expectation

For a self-adjoint observable $A$ on its declared domain,

$$
\langle A\rangle_\psi=\langle\psi|A|\psi\rangle. \tag{142.3}
$$

Equation (142.3) is EXTERNAL_ESTABLISHED_MATHEMATICS. Operator domains remain part of the statement.

### 142.4 Commutator convention

The commutator is ordered as

$$
[A,B]=AB-BA. \tag{142.4}
$$

Equation (142.4) is EXTERNAL_ESTABLISHED_MATHEMATICS. Reversing the order reverses its sign.

### 142.5 Unitary evolution

For a time-independent self-adjoint Hamiltonian,

$$
U(t)=\exp\!\left(-\frac{i}{\hbar}Ht\right),\qquad |\psi(t)\rangle=U(t)|\psi(0)\rangle. \tag{142.5}
$$

Equation (142.5) is EXTERNAL_ESTABLISHED_MATHEMATICS. It does not type any recovered MK-43 evolution operator by analogy.

### 142.6 Density operator

A statistical state may be represented by

$$
\rho\succeq0,\qquad \operatorname{tr}\rho=1,\qquad \langle A\rangle_\rho=\operatorname{tr}(\rho A). \tag{142.6}
$$

Equation (142.6) is EXTERNAL_ESTABLISHED_MATHEMATICS. Positivity, trace class, and normalization are required conditions.

### 142.7 Spectral measurement convention

For a projection-valued measure $E_A$, the probability assigned to a Borel set $\Delta$ is

$$
\Pr_\rho(A\in\Delta)=\operatorname{tr}\!\left(\rho E_A(\Delta)\right). \tag{142.7}
$$

Equation (142.7) is EXTERNAL_ESTABLISHED_MATHEMATICS. The API title Spectral Measurement Projection does not, by itself, establish this formula as its recovered definition.

### 142.8 Field action convention

For fields $\phi^a$ on a spacetime domain $X$,

$$
S[\phi]=\int_X\mathcal L(\phi^a,\partial_\mu\phi^a,x)\,d^n x. \tag{142.8}
$$

Equation (142.8) is EXTERNAL_ESTABLISHED_MATHEMATICS. Measure, signature, boundary terms, and admissible variations must be declared.

### 142.9 Euler-Lagrange equation

Stationarity under compactly supported variations gives

$$
\frac{\partial\mathcal L}{\partial\phi^a}-\partial_\mu\!\left(\frac{\partial\mathcal L}{\partial(\partial_\mu\phi^a)}\right)=0. \tag{142.9}
$$

Equation (142.9) is EXTERNAL_ESTABLISHED_MATHEMATICS. It cannot be applied to a named framework quantity until its action and variation class are recovered.

### 142.10 Canonical field momentum

With a selected time coordinate,

$$
\pi_a=\frac{\partial\mathcal L}{\partial(\partial_0\phi^a)}. \tag{142.10}
$$

Equation (142.10) is EXTERNAL_ESTABLISHED_MATHEMATICS. Constraint systems require a separate canonical analysis.

### 142.11 Native evidence profile

The sixteen assigned API addresses collectively contribute

$$
E_{\mathrm{native}}=(49\ \mathrm{English},0\ \mathrm{equations},1\ \mathrm{definition},0\ \mathrm{theorem/proof},0\ \mathrm{dependencies}). \tag{142.11}
$$

Equation (142.11) is DETERMINISTIC_COVERAGE_EVIDENCE. It prevents conventional equations (142.2)-(142.10) from being misreported as recovered equations from this chapter's native handle slice.

### 142.12 Coverage distribution

The coverage split is

$$
N_{\mathrm{THIN}}=15,\qquad N_{\mathrm{MEDIUM}}=1,\qquad N_{\mathrm{total}}=16. \tag{142.12}
$$

Equation (142.12) is DETERMINISTIC_COVERAGE_EVIDENCE. The sole MEDIUM address is the Definition of the Universal Triadic Law.

### 142.13 Axiom-language profile

Axiom A0, Axiom A4, Axiom System, and Boundary Formation contribute

$$
E_{\mathrm{axiom\ slice}}=(38,0,0,0,0). \tag{142.13}
$$

Equation (142.13) is DETERMINISTIC_COVERAGE_EVIDENCE. Their titles and English units do not supply a quantum axiom system, operator algebra, or field action here.

### 142.14 Triadic-definition profile

The Definition of the Universal Triadic Law contributes

$$
E_{\mathrm{triadic\ definition}}=(1,0,1,0,0). \tag{142.14}
$$

Equation (142.14) is DETERMINISTIC_COVERAGE_EVIDENCE. The chapter preserves the address without inventing a field-theoretic representation of that definition.

### 142.15 Projection and persistence profile

Persistence Locus and Spectral Measurement Projection jointly contribute

$$
E_{\mathrm{projection/persistence}}=(7,0,0,0,0). \tag{142.15}
$$

Equation (142.15) is DETERMINISTIC_COVERAGE_EVIDENCE. No exact projector, spectrum, persistence map, domain, codomain, or proof unit is present in the queried metadata.

### 142.16 Appendix-address profile

The nine appendix addresses contribute only three English units in aggregate,

$$
E_{\mathrm{appendices}}=(3,0,0,0,0). \tag{142.16}
$$

Equation (142.16) is DETERMINISTIC_COVERAGE_EVIDENCE. Appendix titles are navigational addresses, not substantive convention records.

### 142.17 Dependency boundary

No registered dependency is exposed by this assigned slice,

$$
N_{\mathrm{registered\ dependencies}}=0. \tag{142.17}
$$

Equation (142.17) is DETERMINISTIC_COVERAGE_EVIDENCE. A zero in this field does not prove physical independence; it records the queried API graph result.

### 142.18 Proof boundary

No coherent theorem-or-proof unit is attached,

$$
N_{\mathrm{theorem/proof}}=0. \tag{142.18}
$$

Equation (142.18) is DETERMINISTIC_COVERAGE_EVIDENCE. Axiom, lemma, and definition words inside canonical titles do not elevate proof status.

### 142.19 API-status profile

Every assigned handle is declared,

$$
N_{\mathrm{DECLARED}}=16. \tag{142.19}
$$

Equation (142.19) is DETERMINISTIC_COVERAGE_EVIDENCE. DECLARED means addressable in API 4.3; it does not mean fully defined, typed, proved, or experimentally validated.

### 142.20 Open quantum and field-theory obligations

The unresolved convention set is

$$
\Omega_{142}=\{\mathcal H,\operatorname{Dom},\hbar,\mathsf M,H,S,\mathcal L,\text{units},\text{boundary terms},\text{proofs}\}. \tag{142.20}
$$

Equation (142.20) is CURATOR_SYNTHESIS. Each item must be recovered or explicitly introduced before framework objects can be given a common quantum or field-theoretic type.

### 142.21 Chapter determination

The appendix result is

$$
\begin{aligned}
\mathrm{QFTConventions}_{142}
&=16\ \mathrm{DECLARED\ ADDRESSES}\\
&\quad+\mathrm{EXPLICIT\ EXTERNAL\ CONVENTIONS}\\
&\quad+\mathrm{NO\ SILENT\ QUANTIZATION}.
\end{aligned} \tag{142.21}
$$

Equation (142.21) is DETERMINISTIC_STATUS_NORMALIZATION. V18-C08 supplies a disciplined comparison grammar while preserving the absence of native quantum equations in its assigned evidence slice.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@appendix_26` | @appendix_26` — Appendix 26 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_3` | @appendix_3` — Appendix 3 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_45` | @appendix_45` — Appendix 45 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_7` | @appendix_7` — Appendix 7 | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_bk` | @appendix_bk` — Appendix BK | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_c_continuum_limit` | @appendix_c_continuum_limit` — Appendix C: Continuum Limit | THIN | 0 / 0 / 0 | chapter-core object |
| `@appendix_g` | @appendix_g` — Appendix G | THIN | 1 / 0 / 0 | chapter-core object |
| `@appendix_n` | @appendix_n` — Appendix N | THIN | 1 / 0 / 0 | chapter-core object |
| `@appendix_p` | @appendix_p` — Appendix P | THIN | 1 / 0 / 0 | chapter-core object |
| `@axiom_a0` | @axiom_a0` — Axiom A0 — Admissible Continuation | THIN | 10 / 0 / 0 | chapter-core object |
| `@axiom_a4` | @axiom_a4` — Axiom A4 — Boundary Formation | THIN | 12 / 0 / 0 | chapter-core object |
| `@axiom_system` | @axiom_system` — Axiom System | THIN | 9 / 0 / 0 | chapter-core object |
| `@boundary_formation` | @boundary_formation` — Boundary Formation | THIN | 7 / 0 / 0 | chapter-core object |
| `@definition_of_the_universal_triadic_law` | @definition_of_the_universal_triadic_law` — Definition of the Universal Triadic Law | MEDIUM | 1 / 0 / 0 | chapter-core object |
| `@persistence_locus` | @persistence_locus` — Persistence Locus | THIN | 4 / 0 / 0 | chapter-core object |
| `@spectral_measurement_projection` | @spectral_measurement_projection` — Spectral Measurement Projection | THIN | 3 / 0 / 0 | chapter-core object |
