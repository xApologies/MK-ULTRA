# R09 — Derivation Ledger
## Holonomy

### P9-01 — Same endpoint does not imply same History
Take two composable admissible route words

\[
p_1:U\to V,
\qquad
p_2:U\to V,
\]

with

\[
[p_1]_H\ne[p_2]_H.
\]

Under the minimal provenance connection,

\[
P_{p_1}^{\rm prov}(F,h)
=(F,h[p_1]_H),
\]

\[
P_{p_2}^{\rm prov}(F,h)
=(F,h[p_2]_H).
\]

The structural endpoint is the same `F`, but the History-augmented outcomes differ. Hence

\[
K_{\rm prov}(p_1,p_2;F,h)\ne0.
\]

Therefore:

\[
\boxed{
\text{same structural endpoint}
\not\Rightarrow
\text{same route provenance}
}
\]

without requiring any path inverse.

### P9-02 — Existing Fusion source-swap pair is a concrete endpoint-alias example
R02/R08 already provide two decorated Fusion records `F_AB` and `F_BA` whose bare quotient carriers are isomorphic while ordered provenance differs.

Treat the two construction histories as route words

\[
p_{AB}=\texttt{FUSE}(A,B),
\]

\[
p_{BA}=\texttt{SWAP}\cdot\texttt{FUSE}(B,A).
\]

At the bare-carrier equivalence level,

\[
Q_{AB}\cong Q_{BA},
\]

while at the provenance level,

\[
F_{AB}\ne F_{BA}.
\]

Thus an already-established Fusion comparison realizes the same logical pattern as P9-01: endpoint/carrier agreement is strictly weaker than path/provenance agreement.

R09 does not claim `SWAP` is a physical route transaction; it uses the closed constructional symmetry as a same-endpoint provenance test.

### P9-03 — Provenance loop holonomy is a monoid action
Let `gamma:U->U` be a closed route word. Then

\[
\mathrm{Hol}_{\rm prov}(\gamma)(F,h)
=(F,h[\gamma]_H).
\]

For closed route words `gamma_1,gamma_2`,

\[
\mathrm{Hol}_{\rm prov}(\gamma_2\gamma_1)
=
\mathrm{Hol}_{\rm prov}(\gamma_2)
\circ
\mathrm{Hol}_{\rm prov}(\gamma_1).
\]

The empty path acts as identity. Therefore the closed route actions form a monoid representation on the History component.

No inverse is required.

### P9-04 — A closed nonempty History loop can be formally nontrivial while structural transport is identity
In the minimal provenance connection set

\[
\mathrm{Hol}_{\rm struct}(\gamma)=\mathrm{id}_F.
\]

If

\[
[\gamma]_H\ne[\epsilon]_H,
\]

then

\[
\mathrm{Hol}_{\rm prov}(\gamma)(F,h)
\ne
(F,h)
\]

under the exact-word History equivalence.

Hence the full typed holonomy signature is nontrivial even though the carrier endpoint and structural state return exactly.

This is the first R09 component actually **proved nontrivial** for the Fusion work layer.

### P9-05 — Double mirror is chirality-trivial but can be History-nontrivial
By R07,

\[
m^2=\mathrm{id}_\chi.
\]

Therefore for

\[
\gamma_{mm}=m\,m,
\]

\[
\mathrm{Hol}_\chi(\gamma_{mm})=\mathrm{id}_\chi.
\]

But under the conservative History equivalence,

\[
[mm]_H\ne[\epsilon]_H.
\]

Thus

\[
\mathrm{Hol}_{\rm prov}(\gamma_{mm})\ne\mathrm{id}_{\rm prov}
\]

while

\[
\mathrm{Hol}_\chi(\gamma_{mm})=\mathrm{id}_\chi.
\]

So:

\[
\boxed{
\text{same endpoint chirality}
\not\Rightarrow
\text{trivial full holonomy signature}
}
\]

This is a formal route-word result. It does not assert that an actual physical two-mirror loop has been instantiated.

### P9-06 — Endpoint chirality cannot encode route parity beyond its returned action
Suppose two routes have the same final chirality action but different words:

\[
\mathrm{Hol}_\chi(p_1)
=
\mathrm{Hol}_\chi(p_2),
\qquad
[p_1]_H\ne[p_2]_H.
\]

Any endpoint chirality classifier sees only the common returned chirality. It therefore cannot reconstruct the path distinction unless History/provenance is part of the readout.

This is not a failure of chirality. It is a type boundary: endpoint chirality and route History answer different questions.

### P9-07 — Current orientation/chirality holonomy is not proved nontrivial
The source Holonomy book allows nontrivial chirality holonomy in general, and R07 provides a nontrivial mirror automorphism `widehat M` of the bare carrier. But R09 lacks a source-licensed actual Fusion route `gamma_M` satisfying

\[
P_{\gamma_M}^{\rm Conn}=\widehat M.
\]

Therefore R09 cannot promote

\[
\mathrm{Hol}_\chi(\gamma_M)=m
\]

from a conditional test to a fact about the current Fusion operator.

The correct status is:

\[
\boxed{
\text{chirality-valued Fusion holonomy: CONDITIONAL / NOT INSTANTIATED}
}
\]

### P9-08 — Conditional mirror-loop visibility theorem
If a future admissible loop has selected action `widehat M`, then R07 implies:

- bare carrier `Q` returns to the same carrier class;
- seam `q` is fixed;
- source images are exchanged;
- unordered local chirality multiset `{L,R}` is unchanged;
- ordered source/chirality provenance is transformed.

Consequently a readout such as `R1_chi` can be loop-trivial while an ordered provenance readout can be nontrivial.

This is a **conditional theorem**, not current loop existence.

### P9-09 — Phase accumulation requires an independently typed connection
A path-dependent quantum phase would require edge maps

\[
u_e\in U(1)
\]

or an equivalent phase transport law. Without those data, the expression

\[
\prod_e u_e
\]

is undefined.

The R04 parameter `phi` belongs to a state vector; it is not an edge transport record. Therefore

\[
\boxed{
\phi\ne\text{Holonomy by definition}
}
\]

and current Fusion phase holonomy is unestablished.

### P9-10 — Provenance holonomy is not a quantum coherence witness
Consider two quantum decorations on the same structural Fusion record and same route History:

\[
\rho_{\rm coh}=|\Psi_\phi\rangle\langle\Psi_\phi|,
\]

\[
\rho_{\rm mix}
=\tfrac12|LR\rangle\langle LR|
+\tfrac12|RL\rangle\langle RL|.
\]

The provenance transport acts on `(F,h)` identically for both. Therefore the proven provenance holonomy cannot distinguish `rho_coh` from `rho_mix`.

Hence:

\[
\boxed{
\text{provenance holonomy}
\not\Rightarrow
\text{quantum coherence witness}
}
\]

A future phase-sensitive connection plus interference-sensitive readout would be a separate structure.

### P9-11 — Resolution can hide the proved provenance residual
Let two route outcomes be

\[
\widetilde F_1=(F,h[p_1]),
\qquad
\widetilde F_2=(F,h[p_2]),
\]

with distinct History classes.

Any R08 readout that acts only on `F` and discards route History satisfies

\[
\mathrm{Read}_{R}(\widetilde F_1)
=
\mathrm{Read}_{R}(\widetilde F_2).
\]

The new history-sensitive refinement gives

\[
\mathrm{Read}_{R_H}(\widetilde F_1)
\ne
\mathrm{Read}_{R_H}(\widetilde F_2).
\]

Thus the formal provenance holonomy may be observationally trivial at coarse Resolution and visible at `R_H`.

### P9-12 — R09 does not redefine R08 full provenance
R08 `R3_full` is sufficient for the Fusion construction's ordered source/witness provenance. It did not require subsequent transport-route History.

Therefore R09 introduces `R_H` rather than silently asserting that all route words were already visible at `R3_full`.

This preserves source/roadmap chronology.

### P9-13 — Bandwidth can remove replay without deleting History
Suppose route `gamma` was previously traversed and recorded. If a later Bandwidth restriction removes a required lift, `gamma` may no longer be executable.

The existing History record remains

\[
[\gamma]_H
\]

in provenance. Therefore:

\[
\boxed{
\text{currently unexecutable route}
\not\Rightarrow
\text{historically nonexistent route}
}
\]

which preserves the R08 Resolution/Bandwidth distinction.

### P9-14 — Same endpoint and same invariant residue do not force route equivalence
The current corridor discipline can preserve `Inv_F` along multiple admissible routes. Let

\[
P_{p_1}(F),P_{p_2}(F)
\]

have the same carrier endpoint and the same declared invariant residue, but distinct History classes.

Then the invariant record agrees while

\[
K_{\rm prov}(p_1,p_2)\ne0.
\]

So invariant residue is a preservation constraint, not a complete History hash.

### P9-15 — Route difference alone is not enough
If the declared History equivalence identifies two route words, or if every tracked component including History/provenance returns to its identity class, then route syntax alone does not justify calling the loop nontrivial.

Thus the R09 criterion is not

\[
p_1\ne p_2
\Rightarrow
\text{holonomy},
\]

but rather

\[
\boxed{
\text{nontriviality requires a typed residual under the declared equivalence.}
}
\]

### P9-16 — R09 primary classification
The current work layer proves a nontrivial History/provenance action while deliberately leaving the specific chirality and phase actions uninstantiated.

Therefore the exit classification is:

\[
\boxed{
\textbf{PRIMARY: PROVENANCE-VALUED HOLONOMY}
}
\]

with qualifiers:

\[
\text{chirality-valued: conditional/unresolved},
\]

\[
\text{phase-valued: unestablished},
\]

\[
\text{visibility: Resolution-dependent}.
\]
