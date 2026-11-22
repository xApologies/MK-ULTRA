# CRD Genesis-Field Model v1.0 Candidate

**Status:** PHASE A CLOSED / FROZEN WORK-LAYER MATHEMATICS  
**Physical status:** no black-hole, QFT, GR, Hawking, or energy identification is built into CRD.

## 1. Container and state space

The Genesis Field is the sandbox. CRD introduces no new field.

Let `C_G` denote an admissible finite local restriction of Genesis-Field configuration space. A CRD instance uses a finite connected adjacency graph `G=(V,E)`.

The canonical verifier fixture remains the 2×2×2-indexed chirality-byte block, whose byte graph is `Q3` with 8 byte nodes and 12 byte interfaces. Each byte is itself a 2×2×2 chirality object, so the fixture contains 64 primitive loci.

The 3+1+1 configuration-space ontology is **not** replaced by a 3-D Euclidean cube. `Q3` is only a finite local adjacency fixture. If a future Genesis-Field recovery supplies additional adjacency, the general CRD theorem below still applies; Q3-specific counts must then be recomputed.

## 2. Typed CRD state

A local CRD state is:

`X=(G, C, x, f, beta, R, B, Inv, P, H, Pi_read)`

where:

- `G=(V,E)` — finite connected Genesis-Field adjacency restriction;
- `C` — chirality-byte payload/representation registry at vertices;
- `x in C^0(G;Z2)` — current byte reorientation relative to a declared baseline;
- `f in C^1(G;Z2)` — seam/backreaction constraint sector;
- `beta:E->{R,O,Y,G,B,V}` — optional basin routing index;
- `R,B` — Resolution/Bandwidth admissibility data;
- `Inv` — recoverable invariant residue;
- `P` — persistence/closure status;
- `H` — append-only Portal/Rainbow-Road History;
- `Pi_read` — optional downstream/readout projection, not configuration-space identity.

The API ordering remains untouched:

`Genesis Field -> Resolution -> Bandwidth -> Persistence -> Chirality`.

CRD is a dynamics on admissible Genesis-Field configurations; it does not rewrite that dependency ordering.

## 3. Constraint residual and frustration

For edge `e=(u,v)` define:

`r_e(x;f) = f_e XOR x_u XOR x_v`.

Choose positive admissible edge costs:

`c_e = c(beta_e,R_e,B_e) > 0`.

No physical-energy meaning is implied.

Define:

`Phi_f(x) = sum_e c_e r_e(x;f)`.

A Fusion/unbinding event does not silently reorient neighbors. It changes the constraint sector only through a declared CRD Backreaction Lift:

`E_g : f -> f XOR g`

with the event witness appended to `H`. This preserves Fusion v1 as a separate operator.

## 4. Relaxation Portal

For a nonempty connected vertex set `S`, define:

`P_S(x) = x XOR 1_S`.

It is a spontaneous relaxation Portal only when:
1. its Resolution/Bandwidth contract passes;
2. state and provenance remain in `C_G`;
3. `Phi_f(P_S x) < Phi_f(x)`.

## 5. Cluster-descent theorem

**Theorem CRD-1.** For every finite graph `G`, every fixed seam sector `f`, and every positive edge-cost assignment `c`, if `x` is not a global minimizer of `Phi_f`, then at least one connected Cluster Portal strictly lowers `Phi_f`.

**Proof sketch.** Let `x*` be a global minimizer and let `S` be the support of `x XOR x*`. Decompose `S` into connected components `S_i`. No graph edge joins distinct components, so the total potential difference decomposes into component differences. Global minimality of `x*` makes each component contribution nonpositive from `x` toward `x*`; if `x` is not minimal, at least one is strictly negative.

**Corollary.** Repeated strict connected-cluster descent terminates at a global minimum on every finite CRD graph.

**Persistence criterion.** At fixed `f`, a state is persistent iff no admitted connected cluster lowers `Phi_f`, equivalently iff it is a global minimum under the declared admissibility scope.

Efficient discovery of the best cluster on very large graphs remains an algorithmic problem, not a mathematical closure gap.

## 6. Defect sector

During relaxation `f` is fixed.

`[f] in H^1(G;Z2) = C^1(G;Z2) / im(delta)`.

If `[f]=0`, zero frustration is possible. If `[f]!=0`, nonzero residual frustration is unavoidable.

For Q3:

`H^1(Q3;Z2) ~= Z2^5`.

This is a test-graph invariant, not automatically the topology of full 3+1+1 Genesis-Field configuration space.

## 7. Roads and History

A Rainbow Road is an ordered sequence of admitted Portals, optionally preceded by a declared constraint-sector event:

`Road = E_g ; P_S1 ; ... ; P_Sn`.

A strict relaxation Road is acyclic because `Phi` decreases at every relaxation segment. Multiple Roads may reach the same persistent endpoint while retaining different `H`.

## 8. Multiscale closure

On the byte-coherent fine subspace:
- fine orientation is constant within each byte;
- intra-byte seam residual is zero;
- each coarse inter-byte seam lifts to four primitive crossing edges;
- Cluster Portals are restricted to unions of whole bytes.

With unit primitive edge weights:

`Phi_fine = 4 Phi_coarse`.

Therefore coarse relaxation commutes with the lifted fine relaxation on this declared subspace. Arbitrary fine states omitted by the coarse map are Resolution loss; fine-only Portal choices unavailable at coarse scale are Bandwidth loss. Append-only History can retain route information not readable in the coarse state.

## 9. Frozen scope

Closed:
- finite Genesis-Field CRD state type;
- positive-cost cluster relaxation;
- global-minimum persistence criterion;
- Portal/Road admissibility;
- defect-class preservation under relaxation;
- History-sensitive route multiplicity;
- byte-coherent multiscale closure;
- Q3 exhaustive verifier.

Open by design:
- source-authoritative physical Backreaction Lift from Fusion to seam constraints;
- complete native Genesis-Field adjacency beyond finite local restrictions;
- physical calibration of basin/cost values;
- efficient large-graph optimization;
- QFT/GR/black-hole interpretation.

No downstream failure may rewrite this frozen CRD branch.
