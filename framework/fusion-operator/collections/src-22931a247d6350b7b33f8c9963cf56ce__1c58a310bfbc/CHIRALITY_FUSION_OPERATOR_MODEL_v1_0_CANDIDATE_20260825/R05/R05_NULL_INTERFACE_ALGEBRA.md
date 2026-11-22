# R05 — Null-Interface Algebra
## Closed work-layer report

**Run:** R05 / 10  
**Verdict:** CLOSED  
**Classification:** LABELED NULL-LOCUS SPAN + FINITE PUSHOUT + EXTERNAL GLUING/FUSION WITNESS  
**Preferred construction:** a one-interface pushout in a finite labeled-set category, equivalently a labeled wedge after selecting the null interface point  
**Next:** R06 — Reversibility

# Executive result

R05 closes the algebraic question at the center of the recovered Fusion sketch:

> How can two addressable loci each carrying the empty-set state participate in a relation that exists, and then become one shared interface locus, without inventing multiple empty sets or placing content inside the empty set?

The answer is that **value and address are different types**.

There is one empty-set value,

\[
\varnothing,
\]

but a seed carrier may contain many distinct loci whose label map takes the value `N`, with interpretation

\[
\mu(N)=\varnothing.
\]

Thus two interface sites are not two empty sets. They are two different carrier points,

\[
a_\star\in A,
\qquad
b_\star\in B,
\qquad
\lambda_A(a_\star)=N=\lambda_B(b_\star),
\]

whose common state value is the unique empty set.

The minimum address-preserving carrier is therefore a finite labeled set. The preferred Fusion interface is the span

\[
J_N\xrightarrow{i_A}A,
\qquad
J_N\xrightarrow{i_B}B,
\]

where `J_N={j}` and `lambda_J(j)=N`. The shared carrier is its finite pushout

\[
Q=A\sqcup_{J_N}B
\cong
(A\sqcup B)/(i_A(j)\sim i_B(j)).
\]

Because both interface maps preserve the same label, the quotient has a unique descended label map

\[
\lambda_Q:Q\to\Sigma_0
\]

with

\[
\lambda_Q(q)=N,
\qquad
q=[i_A(j)]=[i_B(j)].
\]

Therefore the shared locus stays null:

\[
\mu(\lambda_Q(q))=\varnothing.
\]

The **new existence** is not inside `emptyset`. It is carried by nonempty relational/gluing data such as

\[
R_{AB}=\{(i_A(j),i_B(j))\}\neq\varnothing
\]

and by the Fusion witness/decorated provenance record

\[
\eta_F\neq\varnothing.
\]

R05 proves the finite pushout universal property directly, so the gluing is not accepted merely by naming it a pushout. It also compares pointed sets, labeled sets, relation algebra, graphs, bare quotients, and cell/simplicial descriptions. The preferred algebra is the **labeled pushout with an external witness**, because it is the smallest construction in the tested family that simultaneously:

- preserves the uniqueness of the empty set;
- distinguishes multiple null-labeled addresses;
- selects an interface explicitly;
- makes the shared locus mathematically canonical for the selected span;
- proves a universal gluing property;
- retains source maps/recovery structure;
- keeps Fusion provenance outside the null value;
- scales to later multi-interface and recursive composition work.

This result also sharpens the old sketch. R05 does **not** declare that its green center historically meant `q`, `eta_F`, `{emptyset}`, entanglement, or superposition. The mathematically preferred modern reading separates two layers:

1. `q` — the shared null-labeled carrier locus;
2. `eta_F` — the nonempty Fusion/gluing witness or relation marker.

That separation is a derived work-layer interpretation, not a retroactive claim about the historical drawing.

---

# R05 — Input Ledger

## I5-01 — R01 finite Fusion carrier [DERIVED / CLOSED]

The first work-layer Fusion mode uses finite chirality seeds with addressed loci and state labels `N` and `E`, with

\[
N\equiv\varnothing,
\qquad
E\equiv\{\varnothing\}.
\]

The active interface selects one `N`-labeled boundary locus in each seed and forms

\[
Q=(A\sqcup B)/(a_\star\sim b_\star).
\]

R01 also introduced a nonempty witness/provenance record `eta_F` and explicitly required that the shared state label remain `N`.

## I5-02 — R02 source-image recovery [DERIVED / CLOSED]

For the one-point interface quotient, the canonical source maps into `Q` are injective on the current seed carriers. Their images overlap only at the shared class `q`. This licenses R05 to retain source injections as part of the interface algebra without treating the source images as independent product factors.

## I5-03 — R03/R04 type firewall [DERIVED / CLOSED]

Entanglement and superposition belong to an auxiliary quantum-state layer and are logically independent of the structural Fusion quotient. R05 therefore performs no Hilbert-space operation and uses no phase/coherence premise.

## I5-04 — Chirality address discipline [SOURCE]

The supplied corridor formalization treats an address as an ordered object carrying domain/location, inherited state, chirality, invariant residue, Resolution, Bandwidth, and recursive order. It also distinguishes projected coordinates from persistent-boundary representatives. R05 inherits the principle that a state value does not exhaust the identity of an addressed locus.

## I5-05 — Transduction Geometry gluing vocabulary [SOURCE]

The supplied Transduction Geometry v1.0 package defines, among other items:

- `D23 — Gluing / Realization Operator`: `Glue` is a partial operator from descent-compatible local families to global realizations;
- `D25 — Gluing Witness`;
- `D31 — Quotient-Constructible Local Family`;
- `D32 — Recovery-Compatible Quotient`;
- `D35 — Canonical Quotient Class`;
- `D36 — Quotient-Universal Realization`, whose full universal-property formalism is explicitly deferred in that source.

R05 does **not** silently promote a pushout universal property into that source canon. Instead, it proves a finite standard pushout result for the present null-interface work layer.

## I5-06 — Recovered sketch [SOURCE ARTIFACT]

The old drawing supplies the motivation for a shared central interface between mirror chirality structures. Its exact historical semantic labels are not independently recoverable from the image alone.

## Prohibited assumptions

R05 may not assume:

- that there are two distinct empty sets;
- that `{emptyset,emptyset}` is a quantum or Fusion operation;
- that a nonempty relation changes `emptyset` internally;
- that the green sketch mark has a uniquely known historical semantics;
- that an adjacency edge is the same operation as quotient identification;
- that quotient identification is automatically full Fusion without witness/provenance;
- that the bare quotient is reversible;
- that the interface relation is entanglement;
- that Fusion generates superposition;
- that chirality is conserved by the interface;
- that a universal property from the supplied Transduction Geometry source was already canonically closed.

---

# R05 — Definitions Ledger

## D5-01 — State-value alphabet

Use the abstract state alphabet

\[
\Sigma_0=\{N,E\}
\]

with interpretation map

\[
\mu:\Sigma_0\to\mathcal V,
\qquad
\mu(N)=\varnothing,
\qquad
\mu(E)=\{\varnothing\}.
\]

The abstract labels prevent type confusion between a carrier point and the set-valued state it expresses.

## D5-02 — Labeled finite carrier

A null-interface carrier is a pair

\[
(X,\lambda_X),
\qquad
\lambda_X:X\to\Sigma_0,
\]

where `X` is a finite set of **addresses/loci** and `lambda_X` assigns a state label.

A null locus is an element `x in X` such that

\[
\lambda_X(x)=N.
\]

The locus `x` is not the empty set. Its interpreted state is the empty set:

\[
\mu(\lambda_X(x))=\varnothing.
\]

## D5-03 — Label-preserving map

A map

\[
f:(X,\lambda_X)\to(Y,\lambda_Y)
\]

is label-preserving when

\[
\lambda_Y\circ f=\lambda_X.
\]

The finite labeled carriers and label-preserving maps form the working category `FinSet/Sigma_0` (the finite slice over the state alphabet).

## D5-04 — Null interface template

Define

\[
J_N=(\{j\},\lambda_J),
\qquad
\lambda_J(j)=N.
\]

An interface selection is a pair of injective label-preserving maps

\[
i_A:J_N\hookrightarrow A,
\qquad
i_B:J_N\hookrightarrow B.
\]

Write

\[
a_\star=i_A(j),
\qquad
b_\star=i_B(j).
\]

## D5-05 — Pre-fusion contact relation

Before quotient identification, the tagged disjoint union keeps the selected loci distinct. Define the one-interface contact relation

\[
R_{AB}=\{(\iota_A(a_\star),\iota_B(b_\star))\}.
\]

Then

\[
|R_{AB}|=1,
\]

so

\[
R_{AB}\neq\varnothing.
\]

This is the first rigorous sense in which a relation between two null-labeled positions can exist without modifying their state value.

## D5-06 — Null-interface pushout

The **null-interface pushout carrier** is

\[
Q=A\sqcup_{J_N}B,
\]

constructed concretely as

\[
Q=(A\sqcup B)/\sim,
\]

where `~` is the smallest equivalence relation satisfying

\[
\iota_A(i_A(j))\sim\iota_B(i_B(j)).
\]

Let

\[
j_A:A\to Q,
\qquad
j_B:B\to Q
\]

be the canonical maps.

## D5-07 — Shared null class

The selected interface class is

\[
q=j_A(a_\star)=j_B(b_\star).
\]

Because the interface maps preserve the label `N`, define

\[
\lambda_Q([x])=
\begin{cases}
\lambda_A(x),&x\in A,\\
\lambda_B(x),&x\in B.
\end{cases}
\]

The compatibility condition makes this well-defined at `q`, and

\[
\lambda_Q(q)=N.
\]

## D5-08 — Null-value preservation invariant

Define the null invariant

\[
\mathsf{NullPres}(q)
\iff
\mu(\lambda_Q(q))=\varnothing.
\]

The Fusion interface passes the null-preservation test iff `NullPres(q)` holds.

## D5-09 — Gluing witness / Fusion witness

A **gluing witness** is external data certifying that the quotient realizes the selected interface span. A minimal work-layer witness is

\[
W_G=(J_N,i_A,i_B,Q,j_A,j_B).
\]

The stronger Fusion witness adds the placement/orientation/provenance record:

\[
\eta_F=
(q,(A,a_\star),(B,b_\star),\rho,\mathsf{FUSE}).
\]

The empty set is not a container for `eta_F`. Rather,

\[
\eta_F\in\mathcal W_F
\]

for a separate witness/provenance space `W_F`.

## D5-10 — Labeled wedge special case

When each source has a chosen interface basepoint and `J_N` is one point, the underlying pushout is the pointed-set wedge pattern

\[
A\vee B
\cong
(A\sqcup B)/(a_\star\sim b_\star).
\]

R05 calls it a **labeled null wedge** only as a special-case description. The primary definition remains the labeled pushout because it generalizes cleanly to larger interface templates.

## D5-11 — Preferred Null-Interface Algebra

The preferred algebraic object is

\[
\mathcal N_F(A,B;J_N)
=
\big(
J_N\xrightarrow{i_A}A,
J_N\xrightarrow{i_B}B,
Q,
\lambda_Q,
j_A,j_B,
W_G,
\eta_F
\big).
\]

This is a **labeled span + finite pushout + external witness**.

## D5-12 — Raw gluing versus Fusion

Raw gluing is the pushout square and carrier `Q`.

Fusion remains the decorated object carrying `eta_F` and inherited provenance/invariant data. Thus R05 retains the R01 distinction

\[
\mathsf{gluing}\neq\mathsf{Fusion}.
\]

---

# R05 — Derivation Ledger

## P5-01 — One empty set does not imply one null address

Assume a labeled carrier `(X,lambda_X)` has two distinct points `x != y` with

\[
\lambda_X(x)=N=\lambda_X(y).
\]

Applying the interpretation map gives

\[
\mu(\lambda_X(x))=\varnothing
=\mu(\lambda_X(y)).
\]

The equality occurs in the **value codomain**, not in the carrier domain. Therefore

\[
x\neq y
\]

is consistent with both loci expressing the same unique empty-set value.

This proves that address multiplicity requires no duplication of `emptyset`.

### Concrete representation

One may write the address-state pairs

\[
(x,\varnothing),
\qquad
(y,\varnothing).
\]

These ordered pairs are distinct because their first coordinates differ, even though their second coordinates agree.

---

## P5-02 — Disjoint union protects source distinction before Fusion

For distinct source carriers `A` and `B`, the disjoint union uses tagged injections

\[
\iota_A:A\to A\sqcup B,
\qquad
\iota_B:B\to A\sqcup B.
\]

Therefore, before identification,

\[
\iota_A(a_\star)\neq\iota_B(b_\star)
\]

regardless of the fact that

\[
\lambda_A(a_\star)=N=\lambda_B(b_\star).
\]

Hence the phrase "two null loci" refers to two distinct **addresses with the same null value**, not two empty-set objects.

---

## P5-03 — A relation between null loci is nonempty

Define

\[
R_{AB}=\{(\iota_A(a_\star),\iota_B(b_\star))\}.
\]

It contains one ordered pair, so

\[
|R_{AB}|=1
\]

and therefore

\[
R_{AB}\neq\varnothing.
\]

At the same time,

\[
\mu(\lambda_A(a_\star))
=
\mu(\lambda_B(b_\star))
=
\varnothing.
\]

No contradiction occurs. The relation's existence is a statement about an object in a relation space, not about membership inside the empty set.

This is the precise algebraic version of the exploratory phrase:

> null states can stand in a relation that exists.

It is **not** the statement that nonexistence becomes internally nonempty.

---

## P5-04 — Label descent through the quotient

Construct the equivalence relation on `A disjoint_union B` generated by

\[
\iota_A(a_\star)\sim\iota_B(b_\star).
\]

Define `lambda_Q` on an equivalence class by reading the source label of a representative.

The only nontrivial cross-source equivalence class is

\[
q=[\iota_A(a_\star)]
=[\iota_B(b_\star)].
\]

Since the interface maps are label preserving,

\[
\lambda_A(a_\star)=N=\lambda_B(b_\star).
\]

Thus both representatives give the same value, so `lambda_Q` is well-defined at `q`. All other classes contain representatives from only one source in the current one-point construction, so well-definedness is immediate there.

Hence

\[
\lambda_Q:Q\to\Sigma_0
\]

exists uniquely subject to

\[
\lambda_Q\circ j_A=\lambda_A,
\qquad
\lambda_Q\circ j_B=\lambda_B.
\]

In particular,

\[
\lambda_Q(q)=N.
\]

---

## P5-05 — Empty-set preservation theorem

The interpretation map `mu` is unchanged by Fusion. From P5-04,

\[
\lambda_Q(q)=N.
\]

Therefore

\[
\mu(\lambda_Q(q))=\mu(N)=\varnothing.
\]

No step defines a new member of `emptyset`, no step replaces `emptyset` by a singleton, and no step modifies the interpretation of `N`.

Thus

\[
\boxed{\mathsf{NullPres}(q)}.
\]

The shared locus exists as a carrier point `q`; the state expressed at that point remains the empty set.

This is a type distinction:

\[
q\neq\varnothing,
\qquad
\text{but}\qquad
\text{state}(q)=\varnothing.
\]

---

## P5-06 — Finite pushout universal property

R05 now proves rather than assumes that the quotient is the pushout of the selected interface span in the labeled-set layer.

Let `(Z,lambda_Z)` be any labeled carrier with label-preserving maps

\[
f_A:A\to Z,
\qquad
f_B:B\to Z
\]

satisfying interface compatibility

\[
f_A\circ i_A=f_B\circ i_B.
\]

Define

\[
h:Q\to Z
\]

by

\[
h(j_A(a))=f_A(a),
\qquad
h(j_B(b))=f_B(b).
\]

### Well-definedness

Away from `q`, each class belongs to only one source image. At the shared class,

\[
j_A(a_\star)=j_B(b_\star)=q.
\]

Compatibility gives

\[
f_A(a_\star)
=
f_A(i_A(j))
=
f_B(i_B(j))
=
f_B(b_\star).
\]

Therefore both representatives assign the same value to `h(q)`. So `h` is well-defined.

### Label preservation

For `a in A`,

\[
\lambda_Z(h(j_A(a)))
=\lambda_Z(f_A(a))
=\lambda_A(a)
=\lambda_Q(j_A(a)).
\]

The same holds for the `B` image. Since `j_A(A) union j_B(B)=Q`, `h` is label preserving on all of `Q`.

### Commutativity

By construction,

\[
h\circ j_A=f_A,
\qquad
h\circ j_B=f_B.
\]

### Uniqueness

If `h':Q->Z` also satisfies those two equations, then every point of `Q` lies in the image of `j_A` or `j_B`, so `h'` and `h` agree everywhere. Hence

\[
h'=h.
\]

Therefore the square

\[
\begin{array}{ccc}
J_N & \xrightarrow{i_B} & B\\
\downarrow i_A && \downarrow j_B\\
A & \xrightarrow{j_A} & Q
\end{array}
\]

has the pushout universal property in the finite labeled-set work layer.

This proof is local to R05. It does not claim that the supplied Transduction Geometry source had already closed its deferred general universal-property formalism.

---

## P5-07 — Exact recovered-seed cardinality

For the R01 seed pair,

\[
|A|=4,
\qquad
|B|=4,
\qquad
|J_N|=1.
\]

Because each interface map is injective and only one cross-source point pair is identified,

\[
|Q|=|A|+|B|-|J_N|=4+4-1=7.
\]

The null-label count changes from four addressed null loci in the disjoint source pair to three null-labeled classes in the quotient because exactly two selected null addresses become one shared null address. The set value `emptyset` itself has not been multiplied or reduced; only the count of carrier addresses labeled by `N` changes.

---

## P5-08 — Source recovery remains encoded by the pushout maps

The canonical maps

\[
j_A:A\to Q,
\qquad
j_B:B\to Q
\]

are part of the pushout square. In the present one-interface finite construction they are injective, so the source images remain recoverable as

\[
A_F=j_A(A),
\qquad
B_F=j_B(B),
\]

with

\[
A_F\cap B_F=\{q\}.
\]

R05 does not call this reversibility. It only records the structural information R06 is allowed to test.

---

## P5-09 — Wedge interpretation is valid but secondary

If `a_star` and `b_star` are regarded as chosen basepoints, then the set-level quotient is exactly the wedge-sum pattern

\[
A\vee B=(A\sqcup B)/(a_\star\sim b_\star).
\]

However, a bare pointed-set wedge does not remember that the chosen basepoint carries the `N` state, does not by itself encode other `N/E` labels, and does not carry the Fusion witness. Therefore the wedge is a useful special case, not the preferred full algebra.

---

## P5-10 — Why the green-center interpretation must be split

The modern formalization contains at least two distinct objects at the interface:

\[
q
\quad\text{and}\quad
\eta_F.
\]

`q` is the carrier locus created by identification and remains `N`-labeled.

`eta_F` is a nonempty witness/provenance object recording that `q` descends from two source interface loci under the declared Fusion placement.

A single highlighted glyph in the old drawing cannot, by itself, tell us which of these layers the original drawing intended. Therefore R05 refuses to collapse them. The preferred work-layer diagram is

```text
source A null locus a* ----\\
                              >---- q [state N -> emptyset]
source B null locus b* ----/              |
                                           +---- eta_F [nonempty witness/provenance]
```

This preserves the historical ambiguity while giving the modern mathematics clean types.

---

# Candidate Construction Comparison

R05 compares the roadmap candidates against eight criteria:

- `U` — preserves the uniqueness of `emptyset`;
- `A` — distinguishes multiple null addresses;
- `I` — explicitly selects an interface;
- `G` — supports controlled identification/gluing;
- `P` — provides/proves a universal gluing property;
- `R` — supports source recovery/provenance;
- `M` — minimal for the current problem;
- `X` — extends naturally to later recursive/multi-interface work.

| Candidate | U | A | I | G | P | R | M | X | R05 ruling |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Literal `emptyset_A, emptyset_B` values | FAIL | — | — | — | — | — | — | — | Reject: standard set theory has one empty set; tags must live outside the value. |
| Ordered address-value pairs | PASS | PASS | weak | no | no | PASS | PASS | weak | Keep as minimum addressing representation, not Fusion algebra. |
| Pointed sets / wedge | PASS | PASS for selected point | PASS | PASS | PASS | moderate | PASS | moderate | Useful special case; insufficient label/provenance richness alone. |
| Labeled finite sets | PASS | PASS | needs span | no by itself | no by itself | PASS | PASS | PASS | Keep as carrier/type layer. |
| Relation algebra | PASS | PASS | PASS | relation only | no quotient universal property | PASS | PASS | PASS | Keep as pre-Fusion/contact/witness layer, not carrier Fusion. |
| Labeled graph | PASS | PASS | PASS | edge relation, not identification | not intrinsically | PASS | moderate | PASS | Useful when adjacency is primary; adds unnecessary edge structure for minimal null algebra. |
| Bare quotient of disjoint union | PASS if labels happen to agree | PASS | PASS | PASS | provable | weak without source maps/witness | PASS | PASS | Too weak alone: can hide label contradictions/provenance. |
| Simplicial/cell complex | PASS | PASS | PASS | PASS | context dependent | PASS | FAIL for minimality | PASS | Defer; overpowered for R05. |
| **Span + pushout in finite labeled sets + witness** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **Preferred.** |

---

# R05 — Counterexample Ledger

## C5-01 — Literal duplicate-empty-set model

Suppose one writes two literal set values `emptyset_A` and `emptyset_B` and requires

\[
\varnothing_A\neq\varnothing_B
\]

while both are empty sets. In ordinary extensional set theory, any two sets with no members are equal. Therefore this cannot supply address distinction.

**Ruling:** FAILED. Distinction belongs in address tags, not in the empty-set value.

---

## C5-02 — Singleton-collapse substitution

The expression

\[
\{\varnothing,\varnothing\}=\{\varnothing\}
\]

is true because duplicate elements do not multiply in a set. But it destroys the source-address distinction and supplies no interface maps, no shared carrier, no chirality placement, no gluing witness, and no provenance.

**Ruling:** REJECTED AS FUSION MODEL. It is ordinary extensional set reduction.

---

## C5-03 — Pair without identification

The ordered pair

\[
(a_\star,b_\star)
\]

or singleton relation

\[
\{(a_\star,b_\star)\}
\]

is nonempty and perfectly represents a relation between null addresses. But the two addresses remain distinct.

**Ruling:** VALID PRE-FUSION RELATION; INSUFFICIENT AS FUSED CARRIER.

---

## C5-04 — Graph edge without quotient

A graph edge joining the two null nodes records contact/adjacency, but it does not identify the endpoints. Thus it models the R01 placement condition more naturally than the Fusion result itself.

**Ruling:** VALID CONTACT MODEL; NOT THE CURRENT FUSION OPERATOR.

---

## C5-05 — Incompatible-label pushout attempt

Let the selected source labels be

\[
\lambda_A(a_\star)=N,
\qquad
\lambda_B(b_\star)=E.
\]

Then no label-preserving interface object `J` can map its one point simultaneously to both selected loci while preserving a single state label. Equivalently, a descended `lambda_Q(q)` would be forced to equal both `N` and `E`.

**Ruling:** FAILS IN THE LABELED CATEGORY. This formalizes the R01 typed-interface counterexample.

---

## C5-06 — Bare unlabeled quotient

If labels are erased before quotienting, one may identify the selected points even when their original states were incompatible. The resulting carrier exists as a set, but the operation no longer certifies a state-consistent Fusion interface.

**Ruling:** MATHEMATICAL QUOTIENT EXISTS; TYPED FUSION FAILS.

---

## C5-07 — Quantum vocabulary substituted for interface algebra

Calling the relation "entanglement" or the quotient "superposition" supplies neither the address distinction nor the pushout proof.

**Ruling:** TYPE ERROR under R03/R04.

---

# R05 — Vera Audit

## Audit target
Close the null-interface algebra without allowing the desired Fusion story to define its own premises.

### V5-01 — Did we invent multiple empty sets?
**PASS.** The value layer contains one interpreted `emptyset`; distinct loci are domain points of a label map.

### V5-02 — Did a nonempty relation get inserted into `emptyset`?
**PASS.** `R_AB` and `eta_F` live in relation/witness spaces. `lambda_Q(q)=N` remains unchanged.

### V5-03 — Did we use `{emptyset,emptyset}={emptyset}` as Fusion?
**PASS.** Explicitly rejected as ordinary set reduction.

### V5-04 — Did we merely name the quotient a pushout?
**PASS.** P5-06 proves existence, well-definedness, label preservation, commutativity, and uniqueness of the mediating map.

### V5-05 — Did we overclaim the supplied Transduction Geometry source?
**PASS.** That source provides gluing/quotient/witness vocabulary and explicitly defers full universal-property formalism. R05's finite labeled pushout is labeled as a new work-layer derivation.

### V5-06 — Did we overwrite the old sketch's historical meaning?
**PASS.** The sketch remains semantically underdetermined. The `q`/`eta_F` split is a modern preferred formalization only.

### V5-07 — Did we smuggle entanglement or superposition into R05?
**PASS.** No Hilbert operation is used.

### V5-08 — Did we smuggle reversibility into R05?
**PASS.** R05 retains source maps and witness data but does not claim an inverse Fusion operator. R06 owns that question.

### V5-09 — Did we preserve typed failure?
**PASS.** N/E interface mismatch fails in the labeled category even though an unlabeled set quotient could still be constructed.

### V5-10 — Does each major section perform a distinct job?
**PASS.** Inputs, definitions, derivations, candidate comparison, counterexamples, audit, exit, and carry-forward are nonredundant.

**Vera verdict:** R05 may close.

---

# R05 — Exit Verdict

**Status:** CLOSED

The roadmap required:

> One preferred algebraic construction plus at least two rejected alternatives with reasons.

R05 supplies:

\[
\boxed{
\text{Preferred Null-Interface Algebra}
=
\text{labeled interface span}
+
\text{finite pushout}
+
\text{external gluing/Fusion witness}
}
\]

More concretely,

\[
\boxed{
\mathcal N_F(A,B;J_N)
=
(J_N\to A,\ J_N\to B,\ Q=A\sqcup_{J_N}B,\lambda_Q,j_A,j_B,W_G,\eta_F)
}
\]

with

\[
\lambda_Q(q)=N,
\qquad
\mu(N)=\varnothing,
\qquad
\eta_F\neq\varnothing.
\]

Thus the central result is:

\[
\boxed{
\text{shared relational existence does not require internal content in the null state.}
}
\]

The null state remains null; the carrier address, interface morphisms, quotient class, and witness carry the structure.

### Current classification of the recovered center

- **carrier locus:** `q`, null-labeled;
- **relation/witness:** `eta_F`, nonempty;
- **historical sketch semantics:** unresolved;
- **quantum meaning:** not supplied by R05.

### Not established

R05 does not establish:

- an inverse/unfusion operator;
- losslessness of Fusion under discarded witness data;
- chirality conservation;
- readout equivalence;
- phase/holonomy;
- recursive associativity;
- physical realization.

These remain assigned to R06-R10.

---

# R05 — Carry-Forward Packet
## Licensed inputs for R06

R06 may inherit:

- the one-point null interface template `J_N`;
- the finite labeled carrier model `(X,lambda_X)`;
- one unique empty-set state value represented by `N`;
- distinct null addresses as distinct carrier points with the same label `N`;
- the interface span `J_N -> A`, `J_N -> B`;
- the proven finite labeled pushout
  \[
  Q=A\sqcup_{J_N}B;
  \]
- canonical source maps `j_A,j_B`;
- the current injective source-image result for the exact one-interface seed pair;
- the shared locus `q` with `lambda_Q(q)=N`;
- the nonempty contact relation `R_AB`;
- the external gluing/Fusion witness `W_G,eta_F`;
- the distinction `q != eta_F`;
- the preferred classification: labeled pushout + witness;
- the fact that a bare unlabeled quotient is weaker than typed Fusion.

R06 may **not** inherit as proved:

- that Fusion is reversible;
- that the bare `Q` alone uniquely determines `(A,B)`;
- that witness-assisted source recovery is an inverse Fusion operation;
- that no information is lost;
- that chirality is conserved;
- that a native fused Hilbert space exists;
- that the old sketch uniquely encodes `q` or `eta_F`.

### R06 active question

Given the preferred null-interface algebra, under which retained data does there exist a left inverse, right inverse, partial inverse, provenance-assisted reconstruction, or no inverse at all for the Fusion operation?
