# R08 — Definitions Ledger
## Resolution / Readout

### D8-01 — Full formal Fusion record
Let the current full structural record be

\[
\mathfrak F_{\mathrm{full}}
=
(Q,\lambda_Q,A_F,B_F,q,\mathbf X_F,W_G,\eta_F,\mathrm{Inv}_F).
\]

This is the formal object read by R08. A readout need not expose every component.

### D8-02 — Resolution quotient
For each modeled Resolution `R`, let `K_R` be a congruence on the relevant formal algebra/record class. Define

\[
q_R:\mathcal A_B\to\mathcal A_B/K_R.
\]

Two formal records are observationally equivalent at `R` when

\[
F\sim_R G
\iff
q_R(F)=q_R(G).
\]

### D8-03 — Readout map
A complete readout is

\[
\mathrm{Read}_R
=
\mathrm{Realize}_R\circ q_R.
\]

The quotient determines which distinctions survive. `Realize_R` determines how the surviving quotient is represented.

### D8-04 — Feature readout / mask model
For the finite Fusion work layer, a useful implementation is a typed feature projection. Let

\[
\mathcal D_F=
\{
\text{carrier},
\text{labels},
\text{seam},
\text{local chirality},
\text{pair opposition},
\text{signed balance},
\text{source order},
\text{witness},
\text{provenance}
\}.
\]

A Resolution mask `M_R subseteq D_F` defines a projection `P_R` retaining exactly the declared features. Its kernel is a finite realization of `K_R`:

\[
F\sim_R G
\iff
P_R(F)=P_R(G).
\]

This is a work-layer model of the source quotient rule, not a claim that every Resolution system is literally a coordinate mask.

### D8-05 — Observational fiber
For output `o` at Resolution `R`, define

\[
\mathrm{Fib}_R(o)
=
\{F\mid\mathrm{Read}_R(F)=o\}.
\]

If the fiber has more than one formal member, the readout is non-identifying at that output.

### D8-06 — Feature visibility
For a formal feature `d in D_F`, define

\[
\mathrm{Vis}_R(d;F)=1
\]

when changing `d` within the admissible comparison class can change the `R`-readout, and `0` otherwise.

This is stronger than merely printing a field name: a feature is visible only if the readout can distinguish alternatives that differ in that feature.

### D8-07 — Persistence profile of a feature

\[
\mathrm{Pers}(d;F)
=
\{R\in\mathrm{Res}\mid\mathrm{Vis}_R(d;F)=1\}.
\]

If the Resolution family admits a first visible level, call it

\[
R_{\mathrm{emerge}}(d;F).
\]

### D8-08 — Observational death
A formal distinction `d` is observationally dead at `R` when it remains part of the formal record but lies in the kernel of the readout:

\[
\mathrm{Vis}_R(d;F)=0.
\]

This is not formal erasure.

### D8-09 — Nested illustrative Resolution chain
Define the following **declared work-layer chain** for the current Fusion record:

- `R0_balance`: retain only signed balance `S_chi`;
- `R1_chi`: retain unordered local chirality multiset, opposition parity, signed balance, and chirality content;
- `R2_seam`: retain all `R1` information plus the existence/identity of the shared seam `q`;
- `R3_full`: retain ordered source images, seam, chirality profile, witness, and provenance.

The chain is ordered

\[
R0\le R1\le R2\le R3.
\]

Each coarsening map simply forgets the extra finer information.

The source allows non-monotone Resolution graphs. Therefore an independent occupancy branch is also permitted:

- `R_occ`: retain only occupancy/null-state population information.

`R_occ` is not silently inserted into the total chain.

### D8-10 — Occupancy readout
For the exact seven-locus fused carrier define

\[
\mathrm{Read}_{\mathrm{occ}}(F)
=(n_N,n_E),
\]

where `n_N` is the number of null-labeled loci and `n_E` the number of singleton-empty/existence-labeled loci.

For the current exact pair,

\[
(n_N,n_E)=(3,4).
\]

Because chirality is arrangement-sensitive, this count is not a chirality classifier.

### D8-11 — Unordered chirality readout

\[
\mathrm{Read}_{\chi}(F)
=
(\{\!\{\chi_A,\chi_B\}\!\},\Pi_\chi,S_\chi,C_\chi).
\]

For the current mirror pair:

\[
\mathrm{Read}_{\chi}(F)
=(\{\!\{L,R\}\!\},-1,0,2).
\]

This preserves local chirality content/opposition but discards ordered provenance.

### D8-12 — Seam readout

\[
\mathrm{Read}_{\mathrm{seam}}(F)
=
(\mathrm{Read}_{\chi}(F),q).
\]

This can distinguish a shared Fusion locus but still need not recover which historical source was first/second.

### D8-13 — Full provenance readout

\[
\mathrm{Read}_{\mathrm{full}}(F)
=
(A_F,\chi_A,B_F,\chi_B,q,W_G,\eta_F,\mathrm{Inv}_F).
\]

This is the current readout level sufficient for ordered source/provenance recovery, subject to the validity of the retained witness.

### D8-14 — Bandwidth availability predicate
Let

\[
\mathrm{Avail}_B(\mathfrak F)
\]

mean that the formal Bandwidth Algebra has enough available organizational freedom to support the relevant Fusion/transport operation. This is distinct from `Vis_R`.

### D8-15 — Resolution/Bandwidth state pair
The operative/readable condition is represented by the pair

\[
(B,R).
\]

`B` answers **can the transformation/configuration be supported?**  
`R` answers **which formal distinctions can be distinguished/read?**

### D8-16 — Representation contract
A readout contract is a tuple

\[
\mathcal C_R=(q_R,\mathrm{Realize}_R,\mathrm{codomain},\mathrm{invariants}).
\]

An output mismatch is assessed relative to this declared contract, not by visual comparison alone.

### D8-17 — Representation-only variation
Suppose `x` is a formal seed occupancy state and `sigma` is a bijection of display coordinates. Define

\[
\mathrm{Realize}_\sigma(x)=\sigma_*x.
\]

If `sigma` is part of the declared contract, then

\[
y=\mathrm{Realize}_\sigma(x)
\]

may look different from `x` while preserving all information recoverable through `sigma^{-1}`.

### D8-18 — Readout-contract corruption
For a deterministic declared readout contract `C_R`, an output `y` is contract-inconsistent for input `x` when

\[
y\ne\mathrm{Read}_R(x)
\]

and no declared admissible representation degree of freedom accounts for the discrepancy.

This is a **readout-contract failure**. It is not inferred merely from a different-looking matrix.

### D8-19 — Readout equivalence profile
For two formal records `F,G`, define

\[
\mathcal E(F,G)
=
\{R\mid F\sim_R G\}.
\]

This records the set of readouts under which the two formal records alias.

### D8-20 — Cross-Resolution Fusion section
A compatible family

\[
s_F=\{s_R\}
\]

is a Cross-Resolution Fusion section when each `s_R` is the readout class of the same formal Fusion record and the declared coarsening maps satisfy

\[
q_{ji}(s_{R_j})=s_{R_i}.
\]

This is the correct object for saying that one Fusion event is followed through multiple Resolution levels.
