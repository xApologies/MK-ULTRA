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
