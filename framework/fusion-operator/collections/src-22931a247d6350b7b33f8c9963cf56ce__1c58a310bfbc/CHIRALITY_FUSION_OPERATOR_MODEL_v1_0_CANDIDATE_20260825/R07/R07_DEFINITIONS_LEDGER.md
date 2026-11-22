# R07 — Definitions Ledger
## Chirality Conservation

### D7-01 — Chirality orientation set
Let

\[
\mathcal O_\chi=\{L,R\}
\]

be the two mirror seed-orientation classes supplied by the current seed diagram.

### D7-02 — Mirror involution
Define

\[
m:\mathcal O_\chi\to\mathcal O_\chi
\]

by

\[
m(L)=R,
\qquad
m(R)=L,
\qquad
m^2=\mathrm{id}.
\]

### D7-03 — Conventional signed coordinate
For algebraic summaries only, choose a coordinate

\[
\epsilon:\mathcal O_\chi\to\{+1,-1\}
\]

with

\[
\epsilon(R)=-\epsilon(L).
\]

Which handed class receives `+1` is conventional. R07 never uses that convention to identify an external 4.3 sign label.

### D7-04 — Pair opposition parity
For a two-seed pair define

\[
\Pi_\chi(A,B)=\epsilon(\chi_A)\epsilon(\chi_B)\in\{+1,-1\}.
\]

Then

\[
\Pi_\chi=-1
\]

means opposite mirror orientation and

\[
\Pi_\chi=+1
\]

means same handedness.

`Pi_chi` is invariant under a global reversal of the `+/-` naming convention.

### D7-05 — Signed chirality balance
Define

\[
S_\chi(A,B)=\epsilon(\chi_A)+\epsilon(\chi_B).
\]

For an opposite pair,

\[
S_\chi=0.
\]

This is a **summary**, not a complete chirality state.

### D7-06 — Chirality content count
Define the unsigned local chirality content

\[
C_\chi(A,B)=|\epsilon(\chi_A)|+|\epsilon(\chi_B)|.
\]

For two resolved seed orientations,

\[
C_\chi=2.
\]

Thus an opposite pair can satisfy simultaneously

\[
S_\chi=0,
\qquad
C_\chi=2.
\]

### D7-07 — Tagged chirality profile
The strong source/provenance object is

\[
\mathbf X_{AB}
=
\big(
(A,\chi_A),
(B,\chi_B),
\Pi_\chi,
S_\chi,
\rho
\big),
\]

where `rho` is the declared relative placement/orientation record used by the current Fusion mode.

### D7-08 — Fused chirality residue/profile
For a full decorated Fusion output define

\[
\mathbf X_F
=
\big(
(A_F,\chi_A),
(B_F,\chi_B),
q,
\Pi_\chi,
S_\chi,
\eta_F
\big).
\]

The interface locus `q` is **not** assigned a third local handedness by this definition. It is the shared carrier locus at which both source ancestries meet.

### D7-09 — Sourcewise chirality conservation
The current Fusion satisfies sourcewise chirality conservation iff

\[
\chi(A_F)=\chi(A)
\]

and

\[
\chi(B_F)=\chi(B)
\]

under the canonical source embeddings, with the chirality ancestry retained by the seam/witness record.

### D7-10 — Chirality balance, cancellation, annihilation
R07 uses three distinct terms:

- **balance:** signed summary `S_chi=0`;
- **cancellation in a scalar summary:** opposite signs sum to zero;
- **annihilation:** the local chirality structures/ancestries cease to exist.

The first two do not imply the third.

### D7-11 — Mirror-compatible Fusion pair
The current certified R01 Fusion mode is evaluated on a mirror/null/contact pair. R07 therefore treats

\[
\Pi_\chi=-1
\]

as part of the certified **current mode**, not as a universal law for every future Fusion operator.

### D7-12 — Induced mirror on the fused carrier
Suppose there is a label-preserving mirror isomorphism

\[
M:A\xrightarrow{\cong}B
\]

with

\[
M(a_\star)=b_\star
\]

and inverse mirror `M^{-1}:B->A`. If the interface span is mirror-compatible, define the induced map

\[
\widehat M:Q\to Q
\]

by swapping the source images through those mirror maps.

The run will prove that this is a well-defined involutive automorphism of the bare pushout carrier.
