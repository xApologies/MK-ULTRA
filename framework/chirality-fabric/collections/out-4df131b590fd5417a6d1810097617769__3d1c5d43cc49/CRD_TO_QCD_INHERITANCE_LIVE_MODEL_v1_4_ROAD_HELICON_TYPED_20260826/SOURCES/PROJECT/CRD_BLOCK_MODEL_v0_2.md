# CHIRALITY RELAXATION DYNAMICS — BLOCK MODEL v0.2 CANDIDATE

**Status:** ROADMAP COMPLETE / 6 OF 6 CLOSED / WORK-LAYER MATHEMATICS / NOT PHYSICAL CANON

**Progress:** `[■■■■■■] 6/6`

## Frozen object

One CRD block is a `2 x 2 x 2` cube of chirality bytes. One byte is `2 x 2 x 2` primitive loci. The block therefore has 8 bytes, 64 primitive loci, 12 byte interfaces and 144 primitive nearest-neighbor relations.

Diagnostic serialized byte pair:

`A=10010110`

`B=01101001`

with A/B bitwise complementary. Under the declared lexicographic local coordinate convention, A is the even-parity byte and B the odd-parity byte. The block alternates A/B by byte-coordinate parity.

## CRD state

Let the byte graph be `G=(V,E)=Q3`. Let

- `x in C0(G;Z2)` be byte reorientation relative to baseline;
- `f in C1(G;Z2)` be the declared seam/backreaction pattern;
- `beta_e in {R,O,Y,G,B,V}` be a basin routing index;
- `R_e,B_e` be Resolution/Bandwidth data;
- `H` be append-only Portal/Road History.

Exact closure is

`delta x = f`.

## R01 baseline theorem

The control block is connected and has `beta1=5` at byte Resolution and `beta1=81` at primitive Resolution. The declared serialization gives 24 null/null cross-byte primitive contacts, providing a finite contact-site sandbox without pretending every contact is physically Fusion-admissible.

## R02 backreaction result

Fusion v1 alone still causes no neighbor reorientation. CRD therefore keeps a separate Backreaction Lift. Under a hard changed byte seam, the equal-capacity minimum soft cut is 2 for every byte edge. At primitive null/null contacts the minimum cut is 3 (12 cases) or 5 (12 cases).

## R03 relaxation theorem and failure

A one-byte cellular relaxation law does **not** close CRD:

- asynchronous strict descent: 25/128 exact seam patterns always close, 100/128 are route-dependent with metastable traps, 3/128 have no descending one-byte road to closure;
- naive synchronous update: 100/128 exact patterns form 2-cycles, 3/128 freeze at `Phi=4`, 25/128 close.

The obstruction is cooperative: the three coordinate-plane coboundaries require a four-byte collective move.

Define a **Cluster Portal** as an admissible transaction that flips a connected byte subset as one Geometric payload. For exact `f`, recover canonical `x*`, decompose its support into connected components, and flip those components. Every step strictly lowers `Phi`, so all 128/128 exact seam patterns close.

Therefore:

`exact/coboundary sector => state-confluent modulo global Z2`

while Road History is generally nonconfluent.

## R04 defect/knot algebra

`H1(Q3;Z2) ~= Z2^5`.

A complete invariant is the five-bit parity signature on five independent cube faces. Define

`Hol_f(gamma) = XOR_(e in gamma) f_e`.

This defect holonomy is invariant under `f -> f + delta x`.

Classification:

- ordinary fluctuation: `f=0`;
- relaxable defect: `f != 0`, `[f]=0`;
- persistent chirality-knot candidate: `[f] != 0`.

The last phrase means persistent **CRD topological frustration** only. It is not yet a physical singularity theorem.

## R05 basin/Rainbow law

A basin-aware Portal cost is

`c_e = w_(beta_e) q(R_e,B_e) > 0`,

with no physical-energy interpretation implied. Color is a coarse route index; full chirality/invariant/provenance remains the payload. Strictly decreasing `Phi` makes spontaneous CRD relaxation Roads acyclic.

## R06 scaling theorem

CRD tiles by dyadic blocks with no change of adjacency rule. A `2 x 2 x 2` superblock has a `4 x 4 x 4` **byte** graph, exactly isomorphic to the `4 x 4 x 4` **primitive-locus** graph inside one block:

`(V,E,beta1) = (64,144,81)` at both descriptions.

This establishes a reusable multiscale lattice architecture for CRD and STONEWAKE.

## Solver boundary

Closed:

- exact/coboundary test and target recovery in `O(V+E)`;
- cluster-Road construction for exact patterns;
- single hard seam weighted min-cut;
- basin-aware routing;
- multiblock gluing and defect detection.

Open by design:

- a general exact optimizer for arbitrary large nontrivial frustrated seam sets;
- any physical energy calibration;
- QFT/GR/black-hole/Hawking interpretation.

## Downstream gate

The supplied QFT/GR bridge remains untouched until CRD is deliberately handed downstream. Its chirality -> ER foam -> Helicon -> gravitational Helicon mode -> Graviton -> continuity perturbation -> Time-Shell -> metric/curvature route is a **comparison/representation gate**, not a premise of this model.
