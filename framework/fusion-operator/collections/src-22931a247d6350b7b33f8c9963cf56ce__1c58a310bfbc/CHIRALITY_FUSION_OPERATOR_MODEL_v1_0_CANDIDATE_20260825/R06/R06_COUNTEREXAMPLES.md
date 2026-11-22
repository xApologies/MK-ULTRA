# R06 — Counterexample Ledger
## Reversibility

### CE6-01 — A section is not an unfusion
A section `s:Q->D` satisfying `pi o s=id_Q` chooses one of the two interface antecedents at `q`. It cannot return both. Therefore a right inverse of the quotient projection is not an inverse of the source-merging operation.

### CE6-02 — Source swap defeats bare ordered inversion
The bare symmetric carrier does not distinguish `(A,B)` from `(B,A)` up to carrier isomorphism. Any supposed bare inverse returning an ordered pair must make an unsupported choice.

### CE6-03 — `q` alone does not encode the seam
Knowing which point was fused does not specify how `Q\{q}` decomposes into the A-side and B-side images. Shared-locus recovery is weaker than source decomposition recovery.

### CE6-04 — Local source-image inverse is not a total `Q->A` projection
`j_A^{-1}` is defined on `A_F`, not on `B_F\{q}`. Extending it to all of `Q` requires arbitrary extra choices. The same holds for B.

### CE6-05 — Stored source data can trivialize archival recovery
If a witness literally contains A, B, and their interface maps, extracting them is exact but does not prove that the quotient geometry itself remembered them intrinsically. R06 labels this provenance reversibility, not intrinsic carrier invertibility.

### CE6-06 — Forgetting provenance destroys exact ordered recovery
If `W_G`, `eta_F`, source tags, and seam registry are removed, the remaining carrier is the noninjective bare output. No downstream narrative may claim that the discarded source order can be reconstructed uniquely without new provenance.

### CE6-07 — Quantum record extraction is not unitary reversal
Copying `rho_AB` into and back out of an archival record is not a physical inverse quantum channel. No unitary or isometric Fusion dynamics is currently established.

### CE6-08 — Strong Fusion may behave differently
A future factor-erasing operator could identify more than the interface or encode the source information nonlocally. R06 conclusions about `U_cut` apply to the current weak one-interface quotient Fusion and cannot be silently generalized.
