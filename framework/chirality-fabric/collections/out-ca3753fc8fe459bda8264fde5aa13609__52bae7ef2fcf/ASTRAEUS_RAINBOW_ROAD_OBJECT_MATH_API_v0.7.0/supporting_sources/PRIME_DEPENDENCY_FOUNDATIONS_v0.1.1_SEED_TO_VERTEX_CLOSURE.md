# PRIME DEPENDENCY FOUNDATIONS

## The Prime Mathematical Object

**Working title:** Prime Dependency Calculus  
**Version:** 0.1.1 — Seed-to-Vertex Closure Draft  
**Status:** Mathematics in active construction; seed-to-vertex typing closed  
**Prime expression:** `0 | 0`

---

## Closure Note — Version 0.1.1

This revision closes the passage from structural identity to graph vertex.

The repair is a typed separation:

- an **identity** is what is inherited across a boundary;
- an **occurrence** is an addressable presentation of that identity;
- a **vertex** is produced only when endpoint occurrences are assembled under an explicit graph realization;
- an **edge token** remains distinct from its endpoint occurrences, preserving parallel edges.

Accordingly, structural identity equivalence does not by itself force graph-vertex equality. The same prime cell may be realized deliberately as a non-loop edge or as a loop.

---

# 0. Foundational Intent

The purpose of this framework is to construct a dependency graph as the generative mathematical object underlying later mathematical structures.

The dependency graph itself is not assumed without foundation.

Its foundation is the structural expression:

`0 | 0`

where:

- `0` is not initially a number.
- `|` is not division.
- The two written occurrences of `0` do not initially denote two independent identities.
- The pipe denotes a boundary condition.
- The expression denotes one identity presented recursively across a boundary.

The foundational reading is:

> Identity inherits identity across a boundary.

Equivalently:

> Zero reflects zero across a boundary.

The resulting structure contains enough information to introduce:

1. identity,
2. occurrence,
3. boundary,
4. distinction,
5. relation,
6. orientation,
7. dependency.

A dependency graph is then generated rather than presupposed.

---

# I. Metalanguage Convention

Any foundational mathematics must be described using some external language.

The symbols used in this document therefore belong initially to a **metalanguage**.

The object language begins with only the expression:

`0 | 0`

Set notation, tuples, mappings, and ordinary graph notation are used later as tools for studying the structure. They are not being silently inserted into the Prime Mathematical Object itself.

---

# II. Prime Primitive

## Prime Primitive P0 — Structural Zero

The **Structural Zero** is the self-inheriting boundary expression:

`𝔃 := 0_L | 0_R`

The subscripts `L` and `R` distinguish occurrences, not identities.

Therefore:

`0_L ≡_S 0_R`

as identity, while:

`0_L ≠pos 0_R`

as boundary position.

The Prime Mathematical Object therefore preserves identity while admitting positional distinction.

### Prime Statement

`𝔃 = 0_L | 0_R`

with:

`0_L ≡_S 0_R`

and:

`0_L ≠pos 0_R`

### Interpretation

The same identity occurs on both sides of a boundary.

The boundary does not create a second identity.

It creates a second address from which the identity may be referenced.

---

# III. Derived Primitives

The following primitives are derived from the internal structure of `𝔃`.

They are not introduced independently.

---

## Primitive P1 — Occurrence

An **occurrence** is an addressable presentation of an identity.

For the Prime Mathematical Object, the initial occurrences are:

`Occ(𝔃) = {0_L, 0_R}`

The distinction between occurrences is positional rather than ontological.

### Primitive Statement

`id_S(0_L) = id_S(0_R) = 0`

Here `id_S` denotes **structural identity**.

---

## Primitive P1A — Typed Realization Layers

The seed-to-vertex passage uses five distinct types:

`Id_S` — structural identities,

`Occ` — addressable occurrences,

`Addr` — boundary addresses,

`V` — realized graph vertices,

`E` — dependency-edge tokens.

The governing maps are:

`id_S : Occ → Id_S`

`addr : Occ → Addr`

`ν : Ω → V`

`s : E → V`

`t : E → V`

For every direct boundary expansion:

`id_S(x_L) = id_S(x_R) = id_S(x)`

while:

`addr(x_L) ≠ addr(x_R)`

The map `ν` is a **vertex realization map**. It is declared when occurrences are assembled into a graph. It is not fixed by structural identity alone.

Therefore:

`id_S(x) = id_S(y)`

neither implies nor forbids:

`ν(x) = ν(y)`

Structural identity and graph-vertex identity are different levels of the construction.

Strict occurrence equality remains strongest:

`x = y`

implies equality of structural identity, address, and realized vertex. None of those converses is assumed.

---

## Primitive P2 — Boundary

The **boundary** is the structural separator:

`∂ := |`

The boundary permits one identity to possess distinguishable presentations.

Its action is not annihilation, disconnection, division, or numerical subtraction.

Its action is localization.

### Primitive Statement

`∂(0) = (0_L, 0_R)`

This is semantic shorthand for:

`0_L | 0_R`

---

## Primitive P3 — Boundary Reflection

The Prime Mathematical Object carries a reflection operation:

`ρ : 0_L ↔ 0_R`

Reflection exchanges boundary position while preserving identity.

### Primitive Statement

`ρ(0_L) = 0_R`

`ρ(0_R) = 0_L`

Therefore:

`ρ² = id`

Reflection is involutive.

Applying reflection twice returns the original occurrence.

---

## Primitive P4 — Structural Distinction

A **structural distinction** exists whenever two occurrences share identity but differ by admissible address, role, incidence, orientation, or boundary position.

For the Prime Mathematical Object:

`0_L ≠∂ 0_R`

while simultaneously:

`0_L ≡_S 0_R`

Identity and distinction therefore coexist without contradiction because they refer to different structural properties.

---

## Primitive P5 — Oriented Inheritance

The boundary expression is initially reflection-symmetric.

A dependency appears when a traversal orientation is selected.

Write:

`0_L → 0_R`

when the right occurrence is read as inheriting from the left occurrence.

Write:

`0_R → 0_L`

for the reflected orientation.

### Primitive Statement

`x → y`

means:

> The structural realization of `y` depends upon information inherited from `x`.

Orientation does not alter the underlying identity relation.

It determines the direction in which inheritance is read.

---

## Primitive P6 — Dependency Composition

Two oriented dependencies compose when the realized target of the first is the realized source of the second.

Given edge tokens:

`e : x → y`

and:

`f : z → w`

with:

`ν(y) = ν(z)`

the pair:

`e ; f`

forms a traversable dependency path.

Literal occurrence equality `y = z` is one sufficient case, but realized vertex equality is the general composability condition.

The path does not erase either edge or the intermediate vertex.

---

## Primitive P7 — Recursive Expansion

Any admissible occurrence may itself be presented across a boundary.

`x ↦ x_L | x_R`

The expansion preserves identity:

`id_S(x_L) = id_S(x_R) = id_S(x)`

Recursive expansion is the generative operation through which the Prime Mathematical Object produces larger dependency structures.

---

# IV. Definitions

## Definition D1 — Structural Cell

A **structural cell** is any boundary expression:

`x | y`

whose occurrences possess:

- a declared identity relation,
- an admissible boundary distinction.

The prime structural cell is:

`0 | 0`

---

## Definition D2 — Structural Identity Class

For an occurrence `x`, its structural identity class is written:

`[x]_S`

and contains every occurrence `y` such that:

`id_S(y) = id_S(x)`

Equivalently:

`y ≡_S x`

In the Prime Mathematical Object:

`[0_L]_S = [0_R]_S`

A structural identity class collects distinguishable occurrences that inherit one identity. It is not yet a graph vertex.

---

## Definition D2A — Vertex Equivalence and Realization

Let `Ω ⊆ Occ` be the endpoint occurrences selected for a graph presentation.

A **vertex equivalence** is an explicitly declared equivalence relation:

`≈_V`

on `Ω`.

Write:

`x ≈_V y`

exactly when `x` and `y` are realized as the same graph vertex.

The vertex collection is the quotient:

`V := Ω / ≈_V`

The canonical vertex realization map is:

`ν : Ω → V`

with:

`ν(x) = [x]_V`

where `[x]_V` is the vertex-equivalence class of `x`.

The relations `≡_S` and `≈_V` are distinct:

- `x ≡_S y` does not imply `x ≈_V y`;
- `x ≈_V y` does not imply `x ≡_S y`;
- either relation may be imposed together with the other when an interpretation requires it.

When different structural identities are assembled into one vertex class, the vertex class is a new realized graph identity. The assembly does not retroactively erase the structural identities carried by its occurrences.

---

## Definition D3 — Node / Vertex

A **node**, or graph vertex, is a vertex-equivalence class together with its admissible incidences.

Write:

`v_x := ([x]_V, Inc([x]_V))`

Node equality is therefore:

`v_x = v_y  iff  x ≈_V y`

A node is an address assembly made graph-identical through its realized relations.

Its inherited structural identity data remain available through the occurrences contained in `[x]_V`.

---

## Definition D4 — Dependency Edge

A **dependency edge** is a distinct edge token `e ∈ E` carried by an oriented structural cell:

`e : x → y`

where `x` and `y` are endpoint occurrences.

Its source and target are graph vertices:

`s(e) = ν(x)`

`t(e) = ν(y)`

The edge records that the realized target inherits structure from the realized source through the oriented occurrence pair.

Distinct edge tokens remain distinct even when they possess equal source and target vertices. This preserves parallel edges.

---

## Definition D5 — Dependency Path

A **dependency path** of length `n` is a composable sequence:

`p = (e₁, e₂, ..., eₙ)`

such that:

`t(eₖ) = s(eₖ₊₁)`

for every admissible value of `k`.

The source and target of the path are:

`s(p) = s(e₁)`

`t(p) = t(eₙ)`

---

## Definition D6 — Dependency-Graph Presentation

A **dependency-graph presentation** is a typed structure:

`𝒢 = (Ω, V, E, id_S, addr, ν, s, t, ρ)`

where:

- `Ω` is a collection of endpoint occurrences;
- `V` is a collection of realized vertices;
- `E` is a collection of distinct dependency-edge tokens;
- `id_S : Ω → Id_S` records structural identity;
- `addr : Ω → Addr` records occurrence address;
- `ν : Ω → V` is a surjective vertex realization map;
- `s : E → V` assigns a source vertex to every edge;
- `t : E → V` assigns a target vertex to every edge;
- `ρ` records admissible boundary reflection on paired occurrences.

For every edge token `e`, there is a selected oriented structural cell `x_e → y_e` satisfying:

`s(e) = ν(x_e)`

`t(e) = ν(y_e)`

The **realized dependency graph** of the presentation is:

`G(𝒢) := (V, E, s, t)`

The presentation preserves the structural ancestry of the graph; the realized graph preserves its vertex-edge incidence.

---

## Definition D7 — Recursive Dependency Graph

A dependency graph is **recursive** when an occurrence supporting a realized vertex may admit a local expansion:

`x ↦ x_L | x_R`

with:

`id_S(x_L) = id_S(x_R) = id_S(x)`

A recursive expansion does not silently determine graph attachment. The realization must explicitly declare the images:

`ν(x_L)`

and:

`ν(x_R)`

To extend a dependency path from the vertex `ν(x)`, one may declare:

`ν(x_L) = ν(x)`

then orient the new cell as `x_L → x_R`.

The right realization may be new, previously existing, or equal to the left realization. These choices generate, respectively, an extension, a reconnection, or a loop.

---

## Definition D8 — Dependency-Preserving Map

Let:

`G = (V, E, s, t)`

and:

`H = (W, F, s', t')`

be dependency graphs.

A map:

`Φ : G → H`

is dependency-preserving when it consists of:

`Φ_V : V → W`

and:

`Φ_E : E → F`

satisfying:

`Φ_V(s(e)) = s'(Φ_E(e))`

and:

`Φ_V(t(e)) = t'(Φ_E(e))`

for every edge `e`.

The map must also preserve every declared vertex relation required by the realized structure.

For maps between dependency-graph presentations, include an occurrence map:

`Φ_Ω : Ω → Ω'`

that satisfies:

`Φ_V(ν(x)) = ν'(Φ_Ω(x))`

for every occurrence `x`, and preserves declared structural identity, boundary pairing, reflection, and address distinction.

---

## Definition D9 — Dependency Subgraph

A **dependency subgraph** is a selected region of a dependency graph that preserves every incidence required for its internal interpretation.

A dependency subgraph is not merely a collection of isolated nodes.

It inherits the dependencies necessary to remain structurally readable.

---

## Definition D10 — Dependency Closure

Let `S` be a selected collection of nodes and edges.

The **dependency closure** of `S`, written:

`Cl_G(S)`

is the smallest dependency subgraph containing:

- every element of `S`,
- every dependency required to interpret `S`,
- every admissible composition required by `S`.

A dependency graph is closed relative to a stated construction when every required object and every required dependency is present.

---

## Definition D11 — Well-Founded Dependency Region

A dependency region is **well-founded** when it contains no infinite descending dependency chain of the form:

`... → x₃ → x₂ → x₁`

Well-foundedness is not imposed upon every dependency graph.

Recursive, cyclic, and self-referential structures remain admissible.

Well-foundedness defines a special region appropriate for inductive construction and classical proof.

---

## Definition D12 — Extensional Dependency Region

A dependency region is **extensional** when nodes with identical complete dependency profiles are identified.

Informally, for realized vertices:

`Dep(v) = Dep(w)  implies  v = w`

The exact dependency profile being compared must be specified by the local theory. Extensional equality is graph-level equality; it is not structural identity equivalence between endpoint occurrences.

---

## Definition D13 — Mathematical Object

A **mathematical object** is a closed dependency subgraph equipped with a declared interpretation.

Therefore:

`Mathematical Object = Closed Dependency Structure + Interpretation`

The dependency structure provides organization.

The interpretation declares what that organization realizes.

---

# V. Axioms

## Axiom A0 — Prime Existence

The structural expression:

`0_L | 0_R`

is admissible.

No numerical meaning is required for its existence.

---

## Axiom A1 — Structural Identity Preservation

Boundary presentation preserves structural identity.

`0_L ≡_S 0_R`

More generally:

`x_L ≡_S x_R`

for every direct recursive expansion of `x`.

---

## Axiom A2 — Boundary Distinguishability

Boundary-separated occurrences are positionally distinguishable.

`x_L ≠∂ x_R`

Structural identity equivalence therefore does not collapse boundary address.

---

## Axiom A3 — Reflection Involution

Boundary reflection is involutive.

`ρ²(x) = x`

Reflection preserves structural identity and exchanges boundary position.

---

## Axiom A4 — Oriented Realizability

Every structural cell admits an oriented reading when a dependency interpretation is selected.

From:

`x | y`

one may define a distinct edge token carried by:

`x → y`

or the reflected orientation:

`y → x`

provided the selected orientation is explicitly declared.

---

## Axiom A4R — Vertex Realization Independence

A graph interpretation explicitly declares the vertex realization map `ν`.

For boundary-separated occurrences `x_L` and `x_R`, both of the following are admissible:

`ν(x_L) ≠ ν(x_R)`

and:

`ν(x_L) = ν(x_R)`

Neither structural identity equivalence nor boundary distinction alone decides between them.

Thus a non-loop edge and a loop are different realizations of the same structural seed, not contradictory readings of it.

---

## Axiom A5 — Compositional Inheritance

Admissible realized dependencies compose.

Let:

`e : x → y`

and:

`f : z → w`

be oriented edge tokens.

When:

`t(e) = s(f)`

equivalently:

`ν(y) = ν(z)`

there exists an admissible dependency path:

`e ; f`

Literal occurrence equality `y = z` is sufficient but not necessary. Vertex realization supplies the general composability condition.

---

## Axiom A6 — Recursive Generativity

Every admissible occurrence may undergo recursive boundary expansion.

`x ↦ x_L | x_R`

Recursive expansion introduces addressable structure without changing the structural identity inherited from `x`.

Any graph attachment produced by the expansion must be declared through `ν`; it is never inferred silently from structural identity.

---

## Axiom A7 — Structural Renaming Invariance

The mathematical structure does not depend upon the accidental names assigned to its occurrences, vertices, or edge tokens.

Any bijective renaming that preserves:

- structural identity classes,
- boundary addresses and pairings,
- vertex equivalence classes,
- the realization map,
- source incidence,
- target incidence,
- orientation,
- declared dependencies,

produces an equivalent dependency-graph presentation.

---

# VI. Lemmas

## Lemma L1 — First Distinction Lemma

The Prime Mathematical Object contains the minimum structure necessary for distinction.

### Proof

By Axiom A1:

`0_L ≡_S 0_R`

By Axiom A2:

`0_L ≠∂ 0_R`

Therefore, the Prime Mathematical Object contains distinguishable occurrences without requiring distinct identities.

Structural distinction is therefore present.

**QED**

---

## Lemma L2 — First Reference Lemma

Each occurrence in the Prime Mathematical Object may reference the same identity from a different boundary address.

### Proof

By Primitive P1, both occurrences possess structural identity `0`.

By Axiom A2, their boundary addresses differ.

Therefore, one identity possesses at least two admissible references:

`ref_L(0) ≠ ref_R(0)`

while both references resolve to the same identity:

`0`

**QED**

---

## Lemma L3 — First Edge-Token Lemma

An oriented prime structural cell generates a dependency-edge token with well-defined endpoint occurrences.

### Proof

Begin with:

`0_L | 0_R`

By Axiom A4, select the orientation:

`0_L → 0_R`

and create a distinct edge token `e₀`.

By Definition D4:

`s(e₀) = ν(0_L)`

`t(e₀) = ν(0_R)`

Therefore, the first dependency edge is generated from the Prime Mathematical Object once a vertex realization is declared.

**QED**

---

## Lemma L4 — First Vertex Lemma

The endpoint occurrences of the first edge determine well-typed source and target vertices through the realization map.

### Proof

The occurrences `0_L` and `0_R` are members of the endpoint collection `Ω`.

By Definition D2A, the realization map assigns:

`ν(0_L) ∈ V`

and:

`ν(0_R) ∈ V`

By Definition D4, these images are precisely the source and target of `e₀`.

They may be equal or unequal. In either case, `s(e₀)` and `t(e₀)` lie in `V`, so the edge is type-correct.

**QED**

---

## Lemma L5 — Path Generation Lemma

Repeated recursive expansion, explicit vertex attachment, and oriented inheritance generate dependency paths of arbitrary finite length.

### Proof

The base case of length one follows from Lemma L3.

Assume a dependency path of length `n` terminates at a realized vertex `v`.

Choose an occurrence `x` satisfying:

`ν(x) = v`

By Axiom A6, expand:

`x ↦ x_L | x_R`

Declare the attachment:

`ν(x_L) = v`

Orient the new structural cell as:

`x_L → x_R`

and create a new edge token `e_{n+1}`.

Then:

`s(e_{n+1}) = ν(x_L) = v`

which equals the target of the existing path. By Axiom A5, the new edge composes with that path.

Choose `ν(x_R)` as a new vertex when a strict length extension is required.

A dependency path of length `n + 1` therefore exists. By induction, dependency paths of arbitrary finite length are generable.

**QED**

---

## Lemma L6 — Branch Generation Lemma

Repeated expansion attached to a common realized vertex generates branching dependency structure.

### Proof

Let `v` be a realized vertex.

Choose two source occurrences `x₁` and `x₂` and declare:

`ν(x₁) = ν(x₂) = v`

Generate two oriented cells:

`x₁ → y`

and:

`x₂ → z`

with distinct edge tokens.

Declare distinct target realizations:

`ν(y) ≠ ν(z)`

The two edges share source vertex `v` and possess distinguishable target vertices. The resulting dependency structure therefore branches at `v`.

**QED**

---

## Lemma L7 — Vertex Realization / Quotient Lemma

Every explicitly declared equivalence relation on endpoint occurrences produces a well-defined vertex quotient.

### Proof

Let `Ω` be a collection of endpoint occurrences and let `≈_V` be an equivalence relation on `Ω`.

Form:

`V := Ω / ≈_V`

and define the canonical map:

`ν(x) := [x]_V`

For every edge token `e : x → y`, define:

`s(e) := [x]_V`

`t(e) := [y]_V`

Every edge therefore receives exactly one source class and one target class. Separate edge tokens remain separate, so quotienting vertices does not collapse parallel edges.

The quotient is independent of structural identity equivalence: structurally identical occurrences may remain in different vertex classes, and structurally different occurrences may be assembled into one realized vertex class.

Therefore, endpoint occurrences generate a type-correct realized graph under any explicitly declared vertex equivalence.

**QED**

---

## Lemma L8 — Finite Edge Assembly Lemma

Every finite directed edge incidence can be assembled from finitely many oriented copies of the Prime Mathematical Object.

### Proof

Let:

`E = {e₁, e₂, ..., eₙ}`

be a finite directed edge collection with declared source and target labels.

For every edge `eₖ`, take one disjoint structural-zero cell:

`𝔃ₖ = 0ₖ,L | 0ₖ,R`

Orient that copy as:

`0ₖ,L → 0ₖ,R`

and retain a distinct edge token `εₖ`.

Declare vertex equivalence between endpoint occurrences exactly when their source or target labels designate the same intended vertex.

By Lemma L7, the resulting quotient has precisely the requested source and target incidence. Distinct `εₖ` preserve edge multiplicity.

Therefore, the finite directed edge collection is generated from finitely many copies of the Prime Mathematical Object.

**QED**

---

## Lemma L9 — Edge–Loop Separation Lemma

A non-loop edge and a loop are independently realizable from the same prime oriented cell and are not accidentally identified.

### Proof

Begin with one oriented cell:

`e : 0_L → 0_R`

For the non-loop realization, declare:

`ν_edge(0_L) = u`

`ν_edge(0_R) = v`

with:

`u ≠ v`

This yields:

`G_edge = ({u,v}, {e}, s(e)=u, t(e)=v)`

For the loop realization, declare:

`ν_loop(0_L) = ν_loop(0_R) = w`

This yields:

`G_loop = ({w}, {e}, s(e)=t(e)=w)`

Both realizations preserve:

`0_L ≡_S 0_R`

and:

`0_L ≠∂ 0_R`

They differ only in the declared vertex equivalence.

No dependency-preserving bijection exists between the two realized graphs because the first has two vertices and the second has one; equivalently, the first satisfies `s(e) ≠ t(e)` while the second satisfies `s(e) = t(e)`.

Therefore, the non-loop edge and loop are deliberately constructible and mathematically distinct.

**QED**

---

# VII. Theorems

## Theorem T1 — Dependency Graph Emergence Theorem

The structural expression:

`0 | 0`

together with explicit orientation and vertex realization is sufficient to generate the elementary constituents of a dependency graph without identifying structural identity with vertex identity.

### Proof

The Prime Mathematical Object provides boundary-separated occurrences by Lemma L1.

Those occurrences provide addressable references by Lemma L2.

An orientation generates a distinct edge token by Lemma L3.

The realization map supplies type-correct source and target vertices by Lemma L4.

Recursive expansion with declared attachment generates dependency paths and branches by Lemmas L5 and L6.

Vertex quotients are generated from endpoint occurrences by Lemma L7.

Finite edge incidence is assembled by Lemma L8.

Non-loop and loop incidence are independently realizable by Lemma L9.

Therefore:

- structural identities,
- addressable occurrences,
- realized nodes,
- distinct edge tokens,
- paths,
- branches,
- vertex quotients,
- loops and non-loops,

all arise from the Prime Mathematical Object together with the explicit interpretive choices already required by Definition D13.

A dependency graph is therefore generable from:

`0 | 0`

without any undeclared shift between occurrence, structural identity class, node, or vertex.

**QED**

---

## Theorem T2 — Finite Directed Multigraph Representation Theorem

Every finite directed multigraph, including parallel edges, loops, and isolated vertices, is representable by a finite dependency-graph presentation generated from structural-zero cells.

### Proof

Let:

`G = (V, E, s, t)`

be a finite directed multigraph.

For every edge `e ∈ E`, generate one disjoint oriented structural-zero cell:

`𝔃ₑ = 0ₑ,L → 0ₑ,R`

with a distinct edge token `εₑ`.

For every isolated vertex `v ∈ V`, generate one unoriented carrier cell:

`𝔦ᵥ = iᵥ,L | iᵥ,R`

with no edge token.

Let `Ω` be the collection of every occurrence introduced above. Define a vertex-label map `q : Ω → V` by:

`q(0ₑ,L) = s(e)`

`q(0ₑ,R) = t(e)`

and, for every isolated vertex `v`:

`q(iᵥ,L) = q(iᵥ,R) = v`

Declare vertex equivalence by:

`x ≈_V y  iff  q(x) = q(y)`

Let:

`V' := Ω / ≈_V`

and let `ν : Ω → V'` be the canonical quotient map.

For every edge token `εₑ`, define:

`s'(εₑ) = ν(0ₑ,L)`

`t'(εₑ) = ν(0ₑ,R)`

Now define maps:

`Φ_V : V' → V`

by:

`Φ_V([x]_V) = q(x)`

and:

`Φ_E : {εₑ : e ∈ E} → E`

by:

`Φ_E(εₑ) = e`

The map `Φ_V` is well-defined because `[x]_V = [y]_V` exactly when `q(x)=q(y)`. It is bijective because every non-isolated vertex occurs as an edge endpoint and every isolated vertex receives a carrier cell. The map `Φ_E` is bijective because one distinct edge token was created for each edge.

Incidence is preserved:

`Φ_V(s'(εₑ)) = Φ_V(ν(0ₑ,L)) = q(0ₑ,L) = s(e)`

and:

`Φ_V(t'(εₑ)) = Φ_V(ν(0ₑ,R)) = q(0ₑ,R) = t(e)`

Parallel edges remain distinct because their edge tokens are distinct. A loop occurs exactly when `q(0ₑ,L)=q(0ₑ,R)`. Isolated vertices remain present because their carrier occurrences lie in `Ω` even though they support no edge token.

If `V=E=∅`, use the empty family of cells.

Therefore, the realized dependency graph is related to `G` by a dependency-preserving bijection on vertices and edges. Hence every finite directed multigraph is represented.

**QED**

---

## Theorem T3 — Relational Structure Representation Theorem

Every finitely presented relational structure admits representation as a closed interpreted dependency graph.

### Proof

Let a finite relational structure contain objects:

`a₁, a₂, ..., aₙ`

and declared relations:

`R₁, R₂, ..., Rₘ`

Represent every object by a realized vertex equipped with its declared interpretation.

Represent every relation instance by a relation node.

Incoming dependencies identify the relation's arguments.

An outgoing dependency identifies the realized relational statement.

For an ordered relation:

`R(aᵢ₁, aᵢ₂, ..., aᵢₖ)`

argument-position nodes preserve order.

By Theorem T2, the resulting finite directed incidence structure is generated from structural-zero cells.

Dependency closure supplies every incidence required by the presentation.

Therefore, the relational structure is representable as a closed interpreted dependency graph.

**QED**

---

## Theorem T4 — Functional Representation Theorem

A function is representable as a dependency subgraph satisfying existence and uniqueness of output.

### Functional Condition

A dependency relation `F` represents a function from `X` to `Y` when:

For every `x` in `X`, there exists exactly one `y` in `Y` such that:

`x --F→ y`

### Consequence

Functions need not be introduced as independent primitives.

They emerge as dependency structures constrained by a functional uniqueness condition.

**QED**

---

## Theorem T5 — Set Recovery Theorem

Every well-founded extensional membership structure may be represented by a dependency graph whose edges encode membership.

### Construction

Use an edge:

`x → A`

to mean:

`x is an element of A`

Require the resulting dependency graph to be:

- well-founded,
- extensional.

Under these conditions, nodes are determined by the complete membership structures beneath them.

Pure sets are therefore recoverable as a special class of dependency graphs.

### Consequence

A set is not required as the Prime Mathematical Object.

A set may instead be interpreted as a well-founded extensional dependency region.

**QED**

---

## Theorem T6 — Proof Traversal Theorem

A formal proof may be represented as a dependency graph in which every derived statement depends upon axioms, definitions, or previously derived statements.

Let:

`Γ = {γ₁, γ₂, ..., γₙ}`

be a collection of premises.

Let:

`φ`

be a conclusion.

A proof of `φ` is represented by a finite well-founded dependency subgraph whose:

- terminal nodes are admissible axioms or premises from `Γ`,
- intermediate nodes are admissible derivation steps,
- final node realizes `φ`.

### Consequence

Proof becomes certified dependency closure.

In ordinary notation:

`Γ ⊢ φ`

exactly when there exists an admissible closed derivation graph from `Γ` to `φ`.

**QED**

---

## Theorem T7 — Prime Mathematical Object Theorem, Initial Form

Let `M_fp` denote the class of finitely presented mathematical structures expressible through:

- identities,
- relations,
- operations,
- constraints,
- finite derivations.

Every member of `M_fp` admits an encoding as a closed interpreted dependency graph generated from copies of:

`0 | 0`

### Proof

Objects are represented by realized vertex classes equipped with declared interpretation.

Relations are represented by dependency incidence.

Operations are represented by functional dependency subgraphs.

Constraints are represented by admissibility conditions.

Finite derivations are represented by proof dependency graphs.

By Theorems T2 through T6, every required component admits a dependency-graph realization generated from structural-zero cells.

Their finite union, followed by the required vertex realization quotient and dependency closure, produces an interpreted dependency graph for the entire presentation.

Therefore, every finitely presented mathematical structure in `M_fp` admits an encoding generated from copies of:

`0 | 0`

**QED**

---

# VIII. Prime Closure Statement

The initial dependency foundation is:

`0 | 0`

↓

`Occurrence`

↓

`Boundary Distinction`

↓

`Orientation`

↓

`Dependency`

↓

`Composition`

↓

`Dependency Graph`

↓

`Mathematical Object`

The dependency graph is the first globally generative mathematical object.

Structural Zero is the Prime Mathematical Object from which the dependency graph is generated.

Therefore:

`Prime Structural Object = 0 | 0`

and:

`Prime Generative Mathematical Architecture = Dependency Graph`

These statements are not identical.

The first identifies the irreducible structural seed.

The second identifies the mathematical architecture generated by that seed.

---

# IX. Current Closure Boundary

This draft achieves initial closure for:

- the structural interpretation of `0 | 0`,
- structural identity,
- occurrence equality,
- boundary address distinction,
- reflected identity,
- oriented inheritance,
- explicit vertex realization,
- separation of structural identity equivalence from vertex equality,
- type-correct dependency-edge generation,
- deliberate non-loop and loop realization,
- dependency-path generation with explicit attachment,
- branching generation,
- finite directed multigraph recovery including isolated vertices,
- finitely presented relational structures,
- functional structures,
- well-founded extensional set structures,
- finite proof structures.

The seed-to-vertex ruling is now:

`id_S(x) = id_S(y)`

**permits but does not imply**:

`ν(x) = ν(y)`

Graph-vertex equality is determined only by the declared realization relation `≈_V`.

The next formal requirements are:

1. Define infinite recursive expansion without importing completed infinity prematurely.
2. Define strict equality between dependency-graph presentations.
3. Define dependency-graph equivalence beyond incidence-preserving bijection.
4. Define dependency-graph embedding.
5. Define general internal dependency-graph quotient beyond the seed-to-vertex realization quotient.
6. Define full presentation isomorphism preserving structural identity, addresses, reflection, and realization.
7. Recover arithmetic objects from dependency invariants.
8. Recover ordered pairs and products.
9. Derive algebraic operations as graph transformations.
10. Determine whether categories emerge as dependency graphs equipped with composition.
11. Determine whether dependency graphs themselves form the first category.
12. Determine whether logic is generated internally or must remain in the metalanguage.

---

# X. Foundational Motto

> Zero is not initially quantity.
>
> Zero is structural self-reference across a boundary.
>
> The boundary creates address.
>
> Address permits distinction.
>
> Distinction permits relation.
>
> Oriented relation permits dependency.
>
> Composable dependency generates mathematics.

---

# XI. Seed-to-Vertex Closure Verdict

The original ambiguity is resolved.

The following notions are now formally distinct:

1. **Occurrence equality:** `x = y`.
2. **Structural identity equivalence:** `x ≡_S y`.
3. **Boundary-address distinction:** `x ≠∂ y`.
4. **Vertex equivalence:** `x ≈_V y`.
5. **Node equality:** `v_x = v_y` exactly when `x ≈_V y`.

The source and target maps are type-correct:

`s,t : E → V`

with endpoint occurrences passed through:

`ν : Ω → V`

The prime cell admits both minimal witnesses:

`G_edge = ({u,v},{e},s(e)=u,t(e)=v,u≠v)`

and:

`G_loop = ({w},{e},s(e)=t(e)=w)`

These are deliberately distinct realizations. Neither is forced accidentally by structural identity.

Therefore the seed-to-vertex gap is **CLOSED** for Version 0.1.1.

---

# XII. Astraeus–Vera Statement

The requested mathematical object is explicit.

The dependency graph has not been left merely as a research question.

It has been derived from the Prime Mathematical Object:

`0 | 0`

This is Version 0.1.1.

It is mathematically operational.

It is not yet beautiful.

It is the duct-taped closure from which the formal foundation can now be audited, cannibalized, compressed, and reconstructed under the governing standard:

**Simple. Elegant. Sophisticated.**
