# R10 — Derivation Ledger
## Fusion of Fusion / Recursive Composition

### P10-01 — Existence of the finite recursive carrier
For any finite static interface registry, the disjoint union of all source carriers exists. The smallest equivalence relation containing the finite set of declared seam pairs also exists. Therefore

\[
Q_G=(\bigsqcup_v X_v)/\!\sim_G
\]

exists as a finite set. If every generating pair has matching label, the label descends to each equivalence class. Thus the structural recursive gluing problem is constructively solvable for every statically label-compatible registry.

This proves structural existence; calling the result **Fusion** additionally requires the edge witnesses/chirality-domain conditions.

### P10-02 — Fixed-generator order theorem
Let the same finite set of edge identifications be executed in two different orders. Both procedures generate the smallest equivalence relation containing exactly the same generator set. Therefore the final equivalence relation is identical:

\[
\sim_{G,h_1}=\sim_{G,h_2}=\sim_G.
\]

Hence execution order cannot change the bare finite quotient when the edge registry is fixed in advance and no dynamic admissibility rule changes the generator set.

### P10-03 — Three-seed associativity theorem
Take a compatible chain

\[
A_L\xleftrightarrow{e_{AB}}B_R\xleftrightarrow{e_{BC}}C_L
\]

using two distinct null ports on `B`. The two iterative carriers

\[
(A\sqcup_{J_1}B)\sqcup_{J_2}C
\]

and

\[
A\sqcup_{J_1}(B\sqcup_{J_2}C)
\]

are both canonically isomorphic to

\[
(A\sqcup B\sqcup C)/
\langle a_1\sim b_1,\ b_2\sim c_1\rangle.
\]

The verifier obtains ten quotient classes in either order:

\[
4+4+4-2=10.
\]

Therefore the current null-interface construction is **structurally associative up to canonical isomorphism on this compatible fixed diagram**.

### P10-04 — Associativity is conditional, not global
The theorem above requires that the second interface survives the first gluing and that the complete interface family is jointly compatible. If an operation consumes, relabels, identifies, or invalidates a later interface, the fixed-generator proof no longer applies.

Thus the correct law is

\[
\boxed{
\text{compatible static diagram}
\Rightarrow
\text{carrier associativity up to canonical isomorphism}
}
\]

not an unrestricted total associativity law.

### P10-05 — History-decorated associativity is not strict
The two three-seed constructions naturally produce different History words:

\[
h_L=e_{BC}e_{AB},
\qquad
h_R=e_{AB}e_{BC}
\]

up to the chosen execution convention. Under R09's conservative History equivalence, different exact words remain distinct unless a reduction is declared.

Therefore

\[
Q_{h_L}\cong Q_{h_R}
\]

can coexist with

\[
[h_L]_H\ne[h_R]_H.
\]

So the **carrier algebra is associative up to isomorphism**, while the full History-decorated record is not strictly associative by default.

### P10-06 — Structural commutativity theorem
The tag-swap bijection on the disjoint union sends the generating interface relation for `(A,B)` to the corresponding relation for `(B,A)`. It descends to

\[
A\sqcup_JB\cong B\sqcup_JA.
\]

Thus the bare current binary carrier is symmetric/commutative up to canonical source-swap isomorphism.

### P10-07 — Decorated Fusion is not strictly commutative
The Fusion witness stores source-side placement/provenance. R02 and R08 already showed that `AB` and `BA` may share a coarse/bare carrier while differing in ordered provenance. Therefore

\[
\mathfrak F_{\rm full}(A,B)
\ne
\mathfrak F_{\rm full}(B,A)
\]

as ordered History/provenance records unless an explicit symmetry quotient is applied.

### P10-08 — Idempotence is not a current Fusion law
The typed expression

\[
\mathfrak F(A,A)
\]

uses a same-handed pair for a primitive seed and is outside the current certified mirror-pair domain. Hence idempotence is **undefined**, not proved.

Even if chirality typing is temporarily forgotten, the current one-point raw gluing of two four-locus copies has

\[
4+4-1=7
\]

loci rather than four, so the present one-point gluing pattern is not idempotent.

Only the different full-overlap construction `A sqcup_A A cong A` is idempotent, and that is not the current Fusion operator.

### P10-09 — Identity candidate exists only at the gluing layer
For the raw pushout layer, using the one-point interface object itself as one source with an identity leg gives

\[
A\sqcup_{J_N}J_N\cong A.
\]

So `J_N` is a **gluing-layer unit candidate** for the interface pushout pattern.

But `J_N` has no certified primitive chirality-seed structure and does not satisfy the current mirror-pair Fusion typing. Therefore R10 does **not** promote it to a Fusion identity object.

### P10-10 — Recursive reversibility theorem
For a port-injective weak network, every declared two-source seam can be retained in a network seam registry. If that registry is kept, each seam class can be split back into its source-side null copies and all source carriers are reconstructed up to label-preserving source isomorphism. If the complete edge witness/provenance family is retained, exact source records can be extracted on the valid image.

If only `Q_G` is retained, source order, seam multiplicity, and execution History are generally non-identifiable.

Therefore R06 generalizes:

\[
\boxed{
\text{bare network carrier: irreversible}
\to
\text{seam graph retained: conditionally reversible}
\to
\text{full witness retained: provenance-reversible}
}
\]

### P10-11 — Network invariants
Under the present weak/source-injective recursive mode, the following survive formally:

1. null-label preservation at each seam;
2. every embedded source carrier and its local chirality class;
3. the tagged chirality roster `X_G`;
4. edge opposition for every admitted binary seam;
5. source provenance when the witness layer is retained;
6. the seam graph/interface registry;
7. the execution History word;
8. R08 Resolution/Bandwidth typing.

A scalar whole-carrier handedness is not among the proved invariants.

### P10-12 — Exact uniform 3×3 lattice has no current Fusion edge
In the exact user-supplied 3×3 sandbox all nine primitive seeds have the same chirality class. Current binary Fusion requires a mirror pair.

Therefore every horizontal, vertical, and diagonal candidate is same-handed:

\[
E_{\rm adm}^{\rm uniform}=\varnothing.
\]

The verifier confirms:

- admissible nearest-neighbor edges: `0` of `12`;
- admissible cell-diagonal edges: `0` of `8`.

Thus the exact uniform 3×3 sandbox is a **nine-isolated-vertex Fusion graph** under the present operator. This is a valid negative result, not a reason to alter the input lattice.

### P10-13 — The exact uniform sandbox does not reach recursive closure
Because no first binary edge is admitted, no row closure, column closure, competing Fusion path, or network-level Fusion carrier exists for the exact uniform sandbox under `F_0^{NN}`.

This is **domain failure**, not Bandwidth saturation and not Resolution blindness.

### P10-14 — Checkerboard diagnostic separates chirality compatibility from full interface admissibility
For the derived checkerboard diagnostic, all 12 horizontal/vertical nearest-neighbor pairs are mirror-opposite, while all eight cell-diagonal pairs are same-handed.

The verifier confirms:

\[
|E_{NN}^{\chi\text{-compatible}}|=12,
\qquad
|E_{diag}^{\chi\text{-compatible}}|=0.
\]

However, chirality compatibility alone still does not prove a valid null/contact interface. R10 must explicitly assign interface ports.

### P10-15 — Distinct-port capacity bound
Each primitive seed has two null ports. Under the conservative port-injective recursive rule, every simultaneously declared binary seam consumes one distinct port incidence. Hence

\[
\deg_G(v)\le2.
\]

The full 3×3 nearest-neighbor checkerboard graph has degree 3 at edge-middle vertices and degree 4 at the center. Therefore its full 12-edge network is **not certified** without a new rule allowing port reuse or higher-valence/multiway Fusion.

This is the first explicit recursive-interface capacity bound.

### P10-16 — Maximal connected port-injective 3×3 test
A connected graph on nine vertices with maximum degree at most two is a path or a cycle. The checkerboard nearest-neighbor graph is bipartite, so every cycle has even length; a 9-vertex connected cycle is impossible. Therefore any connected port-injective spanning subgraph has at most

\[
9-1=8
\]

edges.

A Hamiltonian snake path realizes all eight:

\[
(1,1)\to(1,2)\to(1,3)\to(2,3)\to(2,2)\to(2,1)\to(3,1)\to(3,2)\to(3,3).
\]

Its chirality sequence is

\[
L,R,L,R,L,R,L,R,L.
\]

Thus the snake is **maximal connected** under the current distinct-port weak-Fusion discipline.

### P10-17 — 3×3 snake carrier accounting
Assign the two null ports of every interior seed to its predecessor and successor in the snake; endpoints use one port each. Every seam identifies one previously distinct null pair.

Therefore

\[
|Q_{snake}|=9\cdot4-8=28.
\]

The original 18 null loci become

\[
18-8=10
\]

null classes, while all 18 existence-labeled loci remain distinct.

The verifier confirms:

- total classes `28`;
- null classes `10`;
- existence classes `18`;
- degree multiset `1,1,2,2,2,2,2,2,2`.

### P10-18 — Snake execution order changes History, not carrier
The verifier executes the same eight snake seams in four orders:

1. forward snake;
2. reverse snake;
3. all row seams first;
4. the two vertical connectors first.

All four produce the same structural partition `Q_snake`. Their exact edge words are different. Therefore

\[
\boxed{
\text{fixed seam set: structurally confluent, History-distinct}
}
\]

under the current conservative R09 History equivalence.

### P10-19 — Local row/column plaquette closure
A 2×2 checkerboard plaquette has four mirror-compatible nearest-neighbor edges and exactly two null ports per seed. Assigning one port to each incident edge saturates all four seeds and gives

\[
|Q_{\square}|=4\cdot4-4=12.
\]

The verifier confirms four null classes and eight existence classes. Row-first, column-first, and reverse execution orders all produce the same carrier partition but three distinct History words.

Thus even a closed local row/column Fusion pattern demonstrates the same split:

\[
\text{carrier closure}
\neq
\text{History equality}.
\]

### P10-20 — Diagonal Fusion in the checkerboard diagnostic is outside domain
Every cell diagonal connects equal parity and therefore equal handedness in the checkerboard. Hence diagonal Fusion remains undefined for the current mirror-pair operator.

### P10-21 — Competing maximal paths need not be the same full Fusion record
A row-wise Hamiltonian snake and a column-wise Hamiltonian snake can both use eight valid mirror-compatible edges under suitable explicit port assignments. At the finite labeled-set layer they have the same cardinality profile. But their seam graphs and execution histories differ relative to lattice addresses.

Therefore an isomorphism of bare labeled carriers does not imply equality of the decorated recursive Fusion records.

### P10-22 — Macro-chirality is not derived
The checkerboard diagnostic contains five `L` seeds and four `R` seeds. Under a chosen signed coordinate this gives a roster summary of magnitude one. But R07 already established that signed balance is only a summary and that no native `chi(Q)` has been defined.

Therefore the odd-lattice imbalance does **not** prove emergent whole-carrier handedness.

The conserved object remains the sourcewise tagged chirality profile.

### P10-23 — Saturation result
In the maximal snake, seven interior seeds use both null ports; two endpoints use one. Nevertheless no unused nearest-neighbor edge can be added without touching at least one already saturated seed. The snake is therefore **maximal with respect to the declared grid edge set and distinct-port rule**, even though the two endpoint seeds each retain one unused local null port.

The 2×2 plaquette is locally fully saturated: every seed uses both null ports.

Saturation is thus interface-registry-relative rather than a universal property of the seed.

### P10-24 — First Fusion Algebra
The current work layer closes with the partial history-decorated algebra

\[
\mathcal F_{1.0}
=
(\mathcal C,\mathrm{Adm},\mathfrak F,\alpha,\sigma,\mathcal W,\mathcal H,R,B),
\]

where:

- `C` is the class of typed finite chirality carriers/composites;
- `Adm` is the partial interface-domain predicate;
- `F` is binary pushout Fusion and its fixed-diagram recursive colimit extension;
- `alpha` is the structural associator isomorphism on compatible static diagrams;
- `sigma` is the structural source-swap symmetry;
- `W` is witness/provenance data;
- `H` is R09 execution History;
- `R,B` retain Resolution and Bandwidth typing.

This is **not a monoid**: no certified Fusion identity exists, the operation is partial, and full History-decorated records are not strictly associative/commutative under the conservative History equivalence.
