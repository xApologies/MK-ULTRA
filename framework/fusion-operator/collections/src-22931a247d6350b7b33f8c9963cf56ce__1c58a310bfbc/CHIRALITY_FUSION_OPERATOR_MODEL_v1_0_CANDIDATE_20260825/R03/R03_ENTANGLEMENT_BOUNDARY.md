# R03 — Entanglement Boundary
## Closed work-layer report

**Run:** R03 / 10  
**Verdict:** CLOSED  
**Classification:** ENTANGLEMENT/FUSION LOGICALLY INDEPENDENT — TYPE-SEPARATED LAYERS  
**Next:** R04 — Superposition Structure

# Executive result

R03 establishes a sharp boundary between the current Fusion Operator and quantum entanglement.

The current Fusion Operator is a **carrier/interface operation**: it forms the R01/R02 quotient carrier

\[
Q=(A\sqcup B)/(a_\star\sim b_\star).
\]

Entanglement is a **quantum state property** that is meaningful only relative to an explicitly declared subsystem factorization

\[
\mathcal H_A\otimes\mathcal H_B.
\]

Using the supplied MK43 4.3 two-state chirality Hilbert structure as a source anchor, R03 constructs a two-copy work-layer quantum lift and compares:

1. classical anti-correlation;
2. separable coherent quantum states;
3. nonseparable Bell-like chirality entanglement;
4. the quotient-Fusion carrier.

The result is:

\[
\boxed{
\mathrm{Fus}\not\Rightarrow\mathrm{Ent},
\qquad
\mathrm{Ent}\not\Rightarrow\mathrm{Fus}
}
\]

so entanglement is **neither necessary nor sufficient** for the current Fusion operation.

The same bare fused carrier `Q` can be decorated with either a separable state or an entangled state. Therefore entanglement is not an invariant of `Q`. Conversely, the same abstract entangled state can be associated with carriers that are Fusion-admissible or Fusion-inadmissible, so the state does not determine Fusion.

The mathematically decisive boundary is:

> **Entanglement preserves a question about two declared subsystems. Fusion is an operation on their carrier/interface structure. If a future stronger Fusion eliminates the subsystem factorization itself, A|B entanglement becomes undefined rather than automatically maximal.**

R03 therefore closes the terminology firewall required before R04 can ask what, if anything, is superposed in the fused structure.

---

# R03 — Input Ledger
## Entanglement Boundary

**Run:** R03 / 10  
**Dependency:** R02 CLOSED  
**Question:** Where does entanglement end and Fusion begin?

## Authorized inherited premises

### I3-01 — R02 quotient-Fusion carrier [DERIVED / CLOSED]
R03 inherits the exact current Fusion carrier

\[
Q=(A\sqcup B)/(a_\star\sim b_\star),
\]

with embedded source images

\[
A_F\cong A,\qquad B_F\cong B,\qquad A_F\cap B_F=\{q\},\qquad Q=A_F\cup B_F.
\]

The source maps remain injective. The carrier is one quotient object, but no native independent product/tensor factorization of `Q` was established.

### I3-02 — R02 factorization firewall [DERIVED / CLOSED]
The words *source image* and *factor* are not interchangeable. R03 may construct an explicit quantum lift, but it may not retroactively claim that R02 had already produced a Hilbert tensor factorization of the quotient carrier.

### I3-03 — MK43 4.3 single-mote chirality Hilbert structure [SOURCE]
The supplied 4.3 archive contains a current Genesis canonical source defining a two-dimensional mote Hilbert space

\[
\mathcal H_{\mathrm{mote}}=\operatorname{span}\{|+\rangle,|-\rangle\},
\]

with basis states corresponding to the two chirality eigenvalues, and a Genesis creation operator that produces an equal single-mote chirality superposition. R03 uses this only to license a **two-copy work-layer quantum lift** for two chirality seeds.

### I3-04 — Chirality naming firewall [SOURCE / UNRESOLVED REPRESENTATION CONFLICT]
The seed artifact visually identifies left- and right-handed mirror orientations. The current 4.3 source also carries a provisional numeric sign/orientation naming layer. R03 therefore uses abstract basis labels `|L>` and `|R>` for the two mirror chirality states without resolving the numeric-sign naming conflict.

### I3-05 — Holonomy representation firewall [SOURCE]
The supplied Holonomy and Chirality source states that a downstream orientation representation may contain phase/spinorial/chirality factors while remaining a **representation** of chirality/orientation rather than the definition of chirality itself. R03 therefore does not identify a holonomy phase with a quantum entanglement phase. R09 owns the route/holonomy test.

### I3-06 — Corridor persistence/readout discipline [SOURCE]
The Chirality Corridor source carries chirality, inherited organization, invariant residue, Resolution, Bandwidth, and recursive closure as distinct conditions. R03 preserves this type separation and does not infer quantum entanglement from continuity or transport alone.

## Prohibited assumptions

R03 may not assume any of the following:

- the shared quotient point `q` is entanglement;
- perfect anti-correlation is entanglement;
- a coherent superposition in either seed is entanglement between seeds;
- off-diagonal density-matrix entries by themselves prove entanglement;
- mixed reduced states by themselves prove entanglement;
- the current Fusion Operator requires entanglement;
- entanglement is sufficient to make Fusion admissible;
- the bare quotient carrier `Q` has a canonical Hilbert tensor factorization;
- strong factor erasure has occurred;
- the phase `phi` in a Bell-like candidate is a holonomy residue;
- the old sketch proves a quantum state.


---

# R03 — Definitions Ledger
## Entanglement Boundary

### D3-01 — Work-layer two-seed quantum lift
For the purpose of R03 only, attach one copy of the two-state chirality Hilbert space to each source seed:

\[
\mathcal H_A=\operatorname{span}\{|L\rangle_A,|R\rangle_A\},
\qquad
\mathcal H_B=\operatorname{span}\{|L\rangle_B,|R\rangle_B\}.
\]

The bipartite diagnostic space is

\[
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B.
\]

This tensor product is a **quantum lift of the two source degrees of freedom**, not a theorem that the quotient carrier `Q` itself factorizes.

### D3-02 — Product chirality basis
Use ordered basis

\[
\mathcal B_{AB}=(|LL\rangle,|LR\rangle,|RL\rangle,|RR\rangle).
\]

### D3-03 — Classical correlation
A classical joint chirality distribution `P_AB` is correlated when

\[
P_{AB}\neq P_A P_B.
\]

The anti-correlated reference distribution is

\[
P(L,R)=P(R,L)=\tfrac12,
\qquad
P(L,L)=P(R,R)=0.
\]

### D3-04 — Quantum separability
A mixed state `rho_AB` is separable when it can be written

\[
\rho_{AB}=\sum_k p_k\,\rho_A^{(k)}\otimes\rho_B^{(k)},
\qquad p_k\ge0,\quad\sum_kp_k=1.
\]

A pure state is separable exactly when

\[
|\psi\rangle=|a\rangle\otimes|b\rangle.
\]

### D3-05 — Entanglement
A state on the explicitly declared bipartite factorization

\[
\mathcal H_A\otimes\mathcal H_B
\]

is entangled when it is not separable. Entanglement is therefore **factorization-relative**: without a declared A|B subsystem structure (or equivalent commuting-subalgebra structure), the predicate is not typed.

### D3-06 — Coherence in the chirality product basis
For a density state `rho`, chirality-basis coherence between `|LR>` and `|RL>` is represented by nonzero matrix elements

\[
\langle LR|\rho|RL\rangle
\quad\text{or}\quad
\langle RL|\rho|LR\rangle.
\]

This is basis-dependent and is not, by itself, an entanglement criterion.

### D3-07 — Current Fusion predicate
Let

\[
\mathrm{Fus}(A,B;\rho_G)=1
\]

when the R01 geometric/interface admissibility data `rho_G` exists and the partial quotient Fusion operator is defined. Otherwise it is zero/undefined.

This predicate belongs to the **carrier/interface layer**, not the quantum-state layer.

### D3-08 — Entanglement predicate
Let

\[
\mathrm{Ent}(\rho_{AB}\mid A|B)=1
\]

when `rho_AB` is nonseparable relative to the declared A|B quantum factorization.

### D3-09 — Hybrid fused quantum object
When both a quotient Fusion witness and a quantum factor registry are intentionally retained, define the work-layer hybrid object

\[
\widehat F
=
(Q,\eta_F,\mathrm{Inv}_F,W_{AB},\rho_{AB}),
\]

where `W_AB` records the auxiliary A|B Hilbert factors and their provenance. Entanglement, if present, is a property of `rho_AB` relative to `W_AB`; it is **not a property of bare `Q` alone**.

### D3-10 — Forgetful map
Define

\[
U(\widehat F)=Q
\]

as the operation that discards the quantum factor registry and quantum state while retaining only the bare fused carrier.

### D3-11 — Strong-fusion entanglement boundary
If a future strong Fusion produces a state space `H_F` with no canonical A|B factorization and no retained factor registry, then the proposition “A is entangled with B after Fusion” is **undefined**, not false and not automatically maximal.


---

# R03 — Derivation Ledger
## Entanglement Boundary

# 1. Why a quantum lift is legitimate but not retroactive

The supplied 4.3 source gives a two-state Hilbert realization for one chirality degree of freedom. R03 therefore takes two labeled copies for two source seeds:

\[
\mathcal H_A\cong\mathbb C^2,
\qquad
\mathcal H_B\cong\mathbb C^2,
\qquad
\mathcal H_{AB}\cong\mathbb C^4.
\]

This is a new typed layer. It does not alter R02's result that the **carrier** `Q` has no native product/tensor decomposition supplied by the quotient construction.

The distinction is:

```text
carrier layer:   A, B  --Fusion-->  Q
state layer:     H_A tensor H_B carrying rho_AB
```

A hybrid object can retain both layers, but neither layer is silently substituted for the other.

# 2. Classical anti-correlation

Consider the classical distribution

\[
P(L,R)=P(R,L)=\frac12,
\qquad
P(L,L)=P(R,R)=0.
\]

It is perfectly anti-correlated because observing A fixes B in the opposite chirality class. Yet it is entirely classical.

Its diagonal density embedding is

\[
\rho_{\mathrm{cl}}
=
\frac12|LR\rangle\langle LR|
+
\frac12|RL\rangle\langle RL|.
\]

In the ordered basis `(LL,LR,RL,RR)`,

\[
\rho_{\mathrm{cl}}=
\begin{bmatrix}
0&0&0&0\\
0&1/2&0&0\\
0&0&1/2&0\\
0&0&0&0
\end{bmatrix}.
\]

This state is separable by construction because it is a convex mixture of two product projectors.

Both reduced states are

\[
\rho_A=\rho_B=\frac12 I,
\]

so

\[
\operatorname{Tr}(\rho_A^2)=\operatorname{Tr}(\rho_B^2)=\frac12.
\]

Therefore **mixed local reduced states do not prove entanglement**.

# 3. Separable coherent quantum state

Let

\[
|s\rangle=\frac{|L\rangle+|R\rangle}{\sqrt2}.
\]

Two independent equal chirality superpositions give

\[
|\Sigma\rangle
=|s\rangle_A\otimes|s\rangle_B
=\frac12(
|LL\rangle+|LR\rangle+|RL\rangle+|RR\rangle
).
\]

This state contains extensive off-diagonal coherence in the chirality product basis but factorizes exactly.

Its reduced states are pure:

\[
\rho_A=|s\rangle\langle s|,
\qquad
\rho_B=|s\rangle\langle s|,
\qquad
\operatorname{Tr}(\rho_A^2)=1.
\]

Thus **coherence does not imply entanglement**.

This example is especially important because the supplied 4.3 source already contains an equal single-mote chirality superposition. Two such independent single-mote states remain separable unless an additional joint operation creates nonseparability.

# 4. Nonseparable entangled reference state

Use the roadmap candidate

\[
|\Psi_\phi\rangle
=
\frac{1}{\sqrt2}
\left(
|LR\rangle+e^{i\phi}|RL\rangle
\right).
\]

The coefficient matrix with rows indexed by A and columns by B is

\[
M_\phi
=
\frac1{\sqrt2}
\begin{bmatrix}
0&1\\
e^{i\phi}&0
\end{bmatrix}.
\]

For a two-qubit pure state, factorization requires coefficient-matrix rank one. But

\[
\det M_\phi=-\frac{e^{i\phi}}2\neq0,
\]

so

\[
\operatorname{rank}M_\phi=2.
\]

Hence the state is nonfactorizable and therefore entangled.

Its density matrix is

\[
\rho_{\mathrm{ent}}
=|\Psi_\phi\rangle\langle\Psi_\phi|
=
\begin{bmatrix}
0&0&0&0\\
0&1/2&e^{-i\phi}/2&0\\
0&e^{i\phi}/2&1/2&0\\
0&0&0&0
\end{bmatrix}.
\]

The off-diagonal `LR <-> RL` elements preserve relative coherence.

The reduced states are again

\[
\rho_A=\rho_B=\frac12I,
\]

but now the **global state is pure**:

\[
\operatorname{Tr}(\rho_{\mathrm{ent}}^2)=1,
\]

whereas

\[
\operatorname{Tr}(\rho_{\mathrm{cl}}^2)=\frac12.
\]

Thus the classical mixture and the entangled pure state can have the same chirality-basis anti-correlation statistics and the same reduced density matrices while remaining mathematically different global states.

# 5. Partial-transpose cross-check in the 2x2 lift

For the Bell-like candidate, partial transposition on B gives eigenvalues

\[
\left\{\frac12,\frac12,\frac12,-\frac12\right\}.
\]

The negative eigenvalue verifies nonseparability in this two-qubit case.

For the classical anti-correlated mixture, the partial transpose remains positive with eigenvalues

\[
\left\{\frac12,\frac12,0,0\right\}.
\]

For the separable coherent product state, the partial transpose is also positive.

This gives R03 a second diagnostic independent of the pure-state coefficient determinant.

# 6. The first boundary theorem: Fusion does not imply entanglement

Take a pair of seed carriers satisfying the R01 mirror/null/contact Fusion domain. Assign them a separable state, for example

\[
|LR\rangle
\]

or the coherent product state `|Sigma>` above.

The geometric/contact premises required by the R01 operator are still satisfied, so

\[
\mathrm{Fus}=1.
\]

But the state factorizes, so

\[
\mathrm{Ent}=0.
\]

Therefore

\[
\boxed{\mathrm{Fus}\not\Rightarrow\mathrm{Ent}}.
\]

Entanglement is **not necessary** for the current Fusion operation.

# 7. The second boundary theorem: entanglement does not imply Fusion

Take two labeled chirality degrees of freedom with the entangled state `|Psi_phi>`, but choose carriers for which the R01 Fusion interface witness is absent: no declared null/contact identification, incompatible interface type, or simply no Fusion adjacency.

The quantum state remains entangled:

\[
\mathrm{Ent}=1,
\]

while the partial Fusion operator is undefined:

\[
\mathrm{Fus}=0/\text{undefined}.
\]

Therefore

\[
\boxed{\mathrm{Ent}\not\Rightarrow\mathrm{Fus}}.
\]

Entanglement is **not sufficient** for the current Fusion operation.

# 8. All four logical combinations exist

The two predicates occupy independent typed axes:

| Fusion | Entanglement | Example |
|---:|---:|---|
| 0 | 0 | separated carriers with a product state |
| 0 | 1 | Bell-like chirality state with no Fusion interface witness |
| 1 | 0 | R01-admissible quotient Fusion carrying a product/separable state |
| 1 | 1 | R01-admissible quotient Fusion plus retained A|B quantum factor registry carrying `rho_ent` |

Thus the current work layer establishes **logical independence** between the two properties.

# 9. Bare quotient `Q` cannot have a well-defined entanglement value

Suppose, for contradiction, that entanglement were a property of the bare carrier alone:

\[
E_Q:Q\mapsto\{0,1\}.
\]

Fix one R01-admissible fused carrier `Q`. Construct two hybrid objects with exactly the same carrier:

\[
\widehat F_{\mathrm{sep}}
=(Q,\eta_F,\mathrm{Inv}_F,W_{AB},\rho_{\mathrm{sep}}),
\]

and

\[
\widehat F_{\mathrm{ent}}
=(Q,\eta_F,\mathrm{Inv}_F,W_{AB},\rho_{\mathrm{ent}}).
\]

The first is separable; the second is entangled. Yet

\[
U(\widehat F_{\mathrm{sep}})
=
U(\widehat F_{\mathrm{ent}})
=Q.
\]

Therefore no function of bare `Q` alone can recover the entanglement distinction.

Hence:

\[
\boxed{\text{entanglement is not an invariant of the current bare Fusion carrier}.}
\]

# 10. Conversely, the quantum state does not determine Fusion

Fix the same entangled density state `rho_ent` on two abstract chirality factors. Realize it once on carriers satisfying the R01 Fusion interface witness and once on carriers that do not.

The quantum state is the same while Fusion admissibility differs. Therefore:

\[
\boxed{\text{Fusion is not an invariant of }\rho_{AB}\text{ alone}.}
\]

# 11. Where entanglement ends and Fusion begins

The sharp boundary is **type-theoretic**.

Entanglement asks:

> Given a declared bipartite quantum factorization, is the joint state separable across it?

Fusion asks:

> Given two carrier structures and an interface witness, does the partial quotient/gluing operation produce one admissible composite carrier?

So:

```text
ENTANGLEMENT
state property
requires subsystem factorization
nonseparability criterion
phase/coherence may matter

FUSION
carrier/interface operation
requires geometric/relational witness
quotient/gluing criterion
quantum coherence not required
```

They can coexist in a richer object, but one cannot be substituted for the other.

# 12. What happens if stronger Fusion erases the factorization?

Entanglement is defined *relative to* A|B. If a future strong Fusion produces a native state space

\[
\mathcal H_F
\]

for which no canonical A|B decomposition survives and no factor registry is retained, then the expression

\[
\mathrm{Ent}(\rho_F\mid A|B)
\]

is not false; it is **undefined** because the required subsystem split has ceased to be part of the typed object.

This gives a mathematically precise version of the verbal distinction:

> Entanglement can bind two subsystems without destroying the fact that there are two subsystems. Strong Fusion, if it exists, may instead remove the very factorization with respect to which their mutual entanglement was defined.

The current R01/R02 operator has **not** established that stronger state-space transformation.

# 13. Relation to the recovered sketch

The old sketch remains a source artifact for the geometric/contact construction. R03 does not treat the central green locus as a Bell state, an interference term, or a phase marker. It can support the Fusion witness at the carrier layer while the quantum state remains independently classified.

This is a feature, not a weakness: the sketch need not encode all modern Hilbert-space data in order to motivate a valid geometric Fusion candidate.

# 14. R03 theorem set

### T3-01 — Entanglement/Fusion independence
For the current work-layer definitions,

\[
\mathrm{Fus}\not\Rightarrow\mathrm{Ent},
\qquad
\mathrm{Ent}\not\Rightarrow\mathrm{Fus}.
\]

### T3-02 — Bare-carrier non-descent
Entanglement classification does not descend through the forgetful map from the hybrid fused object to bare `Q`.

### T3-03 — Factorization requirement
A|B entanglement is defined only when an A|B quantum factorization or equivalent subsystem algebra is retained.

### T3-04 — Strong-Fusion boundary
Loss of the A|B factorization would make post-Fusion A|B entanglement undefined rather than automatically zero or maximal.

### T3-05 — Correlation firewall
Perfect chirality anti-correlation is compatible with both a separable classical mixture and an entangled coherent state; anti-correlation alone cannot classify entanglement.


---

# R03 — Counterexample Ledger
## Entanglement Boundary

### CE3-01 — Perfect anti-correlation without entanglement

\[
\rho_{\mathrm{cl}}
=\tfrac12|LR\rangle\langle LR|
+\tfrac12|RL\rangle\langle RL|
\]

is perfectly anti-correlated but explicitly separable.

**Blocks:** `correlation => entanglement`.

### CE3-02 — Coherence without entanglement

\[
|\Sigma\rangle
=\left(\tfrac{|L\rangle+|R\rangle}{\sqrt2}\right)_A
\otimes
\left(\tfrac{|L\rangle+|R\rangle}{\sqrt2}\right)_B
\]

has off-diagonal coherence but factorizes.

**Blocks:** `coherence => entanglement`.

### CE3-03 — Mixed marginals without entanglement
`rho_cl` has maximally mixed one-seed reduced states but is separable.

**Blocks:** `mixed reduced state => entanglement`.

### CE3-04 — Shared quotient locus without entanglement
An R01-admissible fused carrier carrying product state `|LR>` has shared quotient locus `q` and no entanglement.

**Blocks:** `Fusion overlap => entanglement`.

### CE3-05 — Entanglement without Fusion
The Bell-like state `|Psi_phi>` remains entangled even when the carrier pair lacks the R01 interface witness.

**Blocks:** `entanglement => Fusion admissibility`.

### CE3-06 — Same bare carrier, different entanglement classes
The same `Q` can be decorated with separable or entangled quantum states.

**Blocks:** `entanglement is a property of bare Q`.

### CE3-07 — Same quantum state, different Fusion classes
The same abstract `rho_ent` can be associated with a Fusion-admissible or Fusion-inadmissible carrier pair.

**Blocks:** `Fusion is determined by rho_AB`.

### CE3-08 — Factor erasure is not maximal entanglement
If a future strong Fusion deletes the A|B factorization, A|B entanglement becomes ill-typed rather than “infinite” or “maximal.”

**Blocks:** `no differentiation => maximal entanglement`.

### CE3-09 — Phase symbol laundering
A relative phase `e^{i phi}` in a Bell-like state is not automatically the same object as route holonomy phase/residue.

**Blocks:** `quantum relative phase = holonomy` prior to R09.


---

# R03 — Decision Table
## Correlation vs separability vs entanglement vs Fusion

| Class | Native object | A|B factorization required? | Coherence required? | Nonseparable? | Shared quotient locus? | Reduced purity diagnostic | Fusion implied? |
|---|---|---:|---:|---:|---:|---|---:|
| Classical anti-correlated pair | probability distribution / diagonal density embedding | for comparison only | no | no | no | can be 1/2 | no |
| Separable coherent quantum state | `rho_A tensor rho_B` or pure product | yes | may be yes | no | no | pure product gives 1 | no |
| Entangled chirality pair | density/pure state on `H_A tensor H_B` | yes | joint coherence for the Bell-like candidate | yes | no | Bell-like pure state gives 1/2 | no |
| Bare fused composite | quotient carrier `Q` | no native Hilbert factor supplied | no | not a typed question | yes | not applicable | yes, by construction |
| Hybrid fused + separable state | `(Q,W_AB,rho_sep)` | retained auxiliary registry | optional | no | yes | depends on state | already fused |
| Hybrid fused + entangled state | `(Q,W_AB,rho_ent)` | retained auxiliary registry | yes for current candidate | yes | yes | Bell-like gives 1/2 | already fused |

## Necessary / sufficient table

| Proposition | R03 verdict | Witness |
|---|---|---|
| Entanglement is necessary for Fusion | **FALSE** | fused carrier + product state |
| Entanglement is sufficient for Fusion | **FALSE** | entangled state + no Fusion interface |
| Fusion is necessary for entanglement | **FALSE** | entangled unfused pair |
| Fusion is sufficient for entanglement | **FALSE** | fused separable pair |
| Perfect anti-correlation is sufficient for entanglement | **FALSE** | classical mixture `rho_cl` |
| Coherence is sufficient for entanglement | **FALSE** | coherent product `|Sigma>` |
| Bare `Q` determines entanglement | **FALSE** | same `Q`, different `rho_AB` |
| A|B entanglement remains meaningful after factor erasure | **FALSE / ILL-TYPED** | A|B factorization is required by definition |

## Compact boundary

\[
\boxed{
\text{correlation} \neq
\text{coherence} \neq
\text{entanglement} \neq
\text{Fusion}
}
\]

The predicates may coexist, but none may be substituted for another.


---

# R03 — Vera Audit
## Entanglement Boundary

**Audit verdict:** PASS FOR R03 CLOSURE  
**Promotion verdict:** WORK LAYER ONLY

## 1. Dependency audit — PASS
R03 begins from the exact R02 quotient-Fusion output and does not assume that Fusion erased source differentiation.

## 2. Quantum type audit — PASS
The A|B Hilbert tensor product is introduced explicitly as a **new work-layer quantum lift** licensed by the supplied single-mote chirality Hilbert source. It is not retroactively assigned to bare `Q`.

## 3. Correlation audit — PASS
Perfect LR/RL anti-correlation is exhibited in an explicitly separable classical mixture. Correlation is not used as shorthand for entanglement.

## 4. Coherence audit — PASS
A coherent product state is given as a counterexample to `coherence => entanglement`. Off-diagonal entries are treated as basis-dependent diagnostics, not a universal entanglement test.

## 5. Nonfactorizability audit — PASS
The Bell-like reference state is proved nonfactorizable by coefficient-matrix rank/determinant and cross-checked using partial-transpose negativity in the two-qubit lift.

## 6. Reduced-state audit — PASS
R03 explicitly shows that both an entangled Bell-like state and a separable classical mixture can have maximally mixed one-seed marginals. Reduced mixedness is not accepted as sufficient evidence.

## 7. Fusion audit — PASS
Fusion remains the R01/R02 partial carrier/interface quotient operation. It is not redefined by the quantum state.

## 8. Necessity/sufficiency audit — PASS
R03 constructs all four combinations of Fusion yes/no and entanglement yes/no. This directly proves logical independence for the current typed model.

## 9. Bare-carrier audit — PASS
Entanglement is not assigned to `Q` alone. The same bare carrier can support different quantum decorations, so entanglement does not descend through the forgetful map.

## 10. Factor-erasure audit — PASS
R03 does not equate loss of subsystem factorization with maximal entanglement. If A|B ceases to be a defined split, A|B entanglement becomes undefined.

## 11. Phase-laundering audit — PASS
The Bell-state relative phase `phi` is not equated with chirality holonomy or route residue. R09 remains authoritative for that bridge.

## 12. R04 boundary audit — PASS
R03 uses superposed states only as diagnostic quantum examples. It does not decide what the **fused object itself** superposes. R04 retains that proof obligation.

## 13. Source-artifact audit — PASS
The recovered green-center sketch is not promoted into a quantum-state diagram. It remains carrier-level provenance evidence for the geometric Fusion candidate.

## 14. Anti-recursion audit — PASS
Each major section has a distinct obligation: type lift, classical correlation, separable coherence, entanglement proof, independence proof, carrier non-descent, factor-erasure boundary, and handoff.

## Final Vera ruling

\[
\boxed{\text{R03 may close with Entanglement and Fusion as logically independent typed structures.}}
\]


---

# R03 — Exit Verdict
## Entanglement Boundary

**VERDICT: CLOSED**

## Central classification

\[
\boxed{
\textbf{ENTANGLEMENT/FUSION LOGICALLY INDEPENDENT — TYPE-SEPARATED LAYERS}
}
\]

Refinement:

> Entanglement is a nonseparability property of a quantum state relative to an explicitly declared A|B factorization. The current Fusion Operator is a partial geometric/interface quotient producing one carrier. The two properties can coexist in a decorated hybrid object, but neither is necessary nor sufficient for the other.

## Closed results

1. A two-copy chirality Hilbert lift is licensed for R03 as a work-layer state model.
2. Classical anti-correlation, coherent separability, and entanglement are explicitly separated.
3. The Bell-like reference state is nonfactorizable.
4. The current Fusion operation can act on a separable/non-entangled state.
5. Entanglement can exist when Fusion is undefined.
6. Therefore neither Entanglement nor Fusion implies the other.
7. Entanglement is not a property of bare quotient carrier `Q`.
8. Post-Fusion entanglement can be discussed only when an A|B quantum factor registry is intentionally retained.
9. If a future strong Fusion truly erases the A|B factorization, A|B entanglement becomes undefined rather than maximal.

## Still unresolved

R03 does **not** establish:
- what exactly is superposed in the fused object;
- a native fused Hilbert space `H_F`;
- a quantum Fusion map on amplitudes;
- whether Fusion preserves, consumes, or transforms coherence;
- whether the old sketch encodes a superposed fused state;
- whether `phi` is route/holonomy residue;
- physical realization.

## R04 authorization

R04 may use:
- `H_A`, `H_B`, and the four-state product chirality basis as an auxiliary pre-/co-Fusion quantum registry;
- the classical, separable coherent, and Bell-like diagnostic states;
- the hybrid object `(Q,eta_F,Inv_F,W_AB,rho_AB)`;
- the theorem that entanglement does not descend to bare `Q`.

R04 may **not** assume:
- a native `H_F` already exists;
- the fused state is automatically Bell-like;
- Fusion is a projection/measurement;
- Fusion destroys the A|B registry;
- superposition equals occupancy overlay;
- the green center is a phase amplitude.

**Next:** R04 — Superposition Structure.


---

# R03 — Carry-Forward Packet to R04
## Immutable R03 output

### CF3-01 — Typed quantum lift
R03 licenses a work-layer two-seed quantum diagnostic space

\[
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B,
\]

with abstract mirror chirality basis `|L>`, `|R>` for each seed. This is auxiliary state structure, not a tensor factorization theorem about bare `Q`.

### CF3-02 — Reference state classes
R04 inherits three diagnostic classes:

- classical anti-correlated mixture `rho_cl`;
- separable coherent product `|Sigma>`;
- Bell-like entangled state `|Psi_phi>`.

### CF3-03 — Independence theorem

\[
\mathrm{Fus}\not\Rightarrow\mathrm{Ent},
\qquad
\mathrm{Ent}\not\Rightarrow\mathrm{Fus}.
\]

Entanglement is neither necessary nor sufficient for the current Fusion operator.

### CF3-04 — Bare-carrier firewall
Entanglement is not an invariant of bare quotient carrier `Q`. It requires an explicit subsystem/factor registry.

### CF3-05 — Hybrid fused quantum object
R04 may use

\[
\widehat F=(Q,\eta_F,\mathrm{Inv}_F,W_{AB},\rho_{AB})
\]

as a bookkeeping object when both Fusion geometry and A|B quantum factors are retained.

### CF3-06 — Strong-Fusion boundary
If a future Fusion truly removes A|B factorization, A|B entanglement becomes undefined. This is not yet established for the current weak quotient Fusion.

### CF3-07 — Phase firewall
The relative phase `phi` in quantum state examples is not yet identified with holonomy. R09 owns that bridge.

## R04 mandatory question

Determine **what is actually superposed** in or around the Fusion construction and whether a native fused state space/operator can be defined without confusing:

- single-seed superposition;
- two-seed product superposition;
- entangled joint alternatives;
- Fusion-channel superposition;
- fused-output superposition;
- geometric occupancy overlay.
