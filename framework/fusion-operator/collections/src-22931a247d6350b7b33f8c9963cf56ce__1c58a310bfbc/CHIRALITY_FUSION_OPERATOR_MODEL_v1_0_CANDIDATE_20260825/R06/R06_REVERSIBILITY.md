# R06 — Reversibility
## Closed work-layer report

**Run:** R06 / 10  
**Verdict:** CLOSED  
**Classification:** PROVENANCE-REVERSIBLE / SEAM-CONDITIONALLY REVERSIBLE / BARE-CARRIER IRREVERSIBLE  
**Next:** R07 — Chirality Conservation

# Executive result

R06 finds that the question **“Can Fusion be undone?”** has no single answer until the retained output data are specified.

For the current weak one-interface Fusion,

\[
Q=A\sqcup_{J_N}B
\cong
(A\sqcup B)/(a_\star\sim b_\star),
\]

the underlying quotient projection

\[
\pi:A\sqcup B\to Q
\]

is genuinely noninjective. It sends two distinct tagged interface loci to the same fused class `q`. Consequently `pi` has **no functional left inverse**. Bare carrier Fusion therefore loses the distinction between the two interface copies and cannot be globally inverted from `Q` alone.

However, R05 deliberately retained richer structure. When the source-image seam

\[
S_F=(A_F,B_F,q)
\]

is retained, the shared point can be **cut** into two null-labeled copies and the original source carriers are reconstructed up to label-preserving isomorphism. When the full gluing/Fusion witness and tagged provenance are retained, the exact source presentation can be recovered by extraction on the image of Fusion.

Thus the current operator has a layered reversibility profile:

\[
\boxed{
\text{bare quotient: irreversible}
\quad\longrightarrow\quad
\text{seam retained: conditionally reversible}
\quad\longrightarrow\quad
\text{full witness retained: provenance-reversible}
}
\]

This does **not** establish reversible quantum dynamics or a physical unfusion process.

# 1. The map that actually loses the distinction

Before Fusion the two source carriers are kept disjoint by tagging:

\[
D=A\sqcup B.
\]

The selected null interface points are distinct in `D` even though both carry the same null state label:

\[
\iota_A(a_\star)\neq\iota_B(b_\star),
\qquad
\lambda_A(a_\star)=N=\lambda_B(b_\star).
\]

Fusion forms the quotient class

\[
q=[\iota_A(a_\star)]=[\iota_B(b_\star)].
\]

The relevant map is therefore

\[
\pi:D\to Q.
\]

At `q`, the fiber has two elements:

\[
\pi^{-1}(q)
=
\{\iota_A(a_\star),\iota_B(b_\star)\}.
\]

This one fiber is the precise location of carrier-level information collapse in the current operator.

# 2. Why the quotient cannot have a left inverse

Suppose a function `ell:Q->D` could undo `pi` on every pre-Fusion point:

\[
\ell\circ\pi=\mathrm{id}_D.
\]

Applying this to both interface antecedents would force

\[
\ell(q)=\iota_A(a_\star)
\]

and

\[
\ell(q)=\iota_B(b_\star).
\]

A single-valued function cannot return two distinct values at the same input. Hence no such `ell` exists.

This is not merely a vocabulary choice: it is a direct obstruction caused by noninjectivity.

# 3. Why a quotient section is not unfusion

Because `pi` is a finite surjection, a section can choose one representative of each quotient class:

\[
s:Q\to D,
\qquad
\pi\circ s=\mathrm{id}_Q.
\]

For the current one-interface case there are exactly two sections, differing only in whether `s(q)` chooses the A-side or B-side representative.

Neither section recovers the two-element preimage of `q`. Therefore a section is a **representative selector**, not an unfusion operator.

The exact inverse information at `q` is instead relation-valued:

\[
q\mapsto
\{\iota_A(a_\star),\iota_B(b_\star)\}.
\]

But even this preimage relation requires knowledge of the original quotient presentation or witness; it is not inferable from the bare set `Q` alone.

# 4. Why bare `Q` does not determine the ordered source pair

R02 already established a source-swap carrier symmetry:

\[
Q(A,B)\cong Q(B,A).
\]

If source order or provenance matters, `(A,B)` and `(B,A)` are different inputs. Their bare quotient carrier cannot distinguish that order.

Therefore no inverse from bare carrier is allowed to manufacture an ordered source history. The missing order must come from surviving provenance.

This is a second irreversibility mechanism distinct from the two-to-one interface fiber:

- the fiber merger loses local interface multiplicity;
- forgetting source tags loses ordered provenance.

# 5. Three levels of recovery

R06 separates three recovery notions that must not be collapsed.

## 5.1 Local/source-image recovery
Because `j_A,j_B` are injective,

\[
j_A^{-1}:A_F\to A,
\qquad
j_B^{-1}:B_F\to B
\]

exist.

These inverses are exact **on their own images**. They are not total maps from all of `Q` back to a source.

## 5.2 Seam-assisted structural recovery
If `A_F,B_F,q` are marked, split `q` into two new null-labeled points:

\[
q\rightsquigarrow(q_A,q_B).
\]

Then

\[
A^\sharp=(A_F\setminus\{q\})\cup\{q_A\},
\]

\[
B^\sharp=(B_F\setminus\{q\})\cup\{q_B\}.
\]

The R02 injectivity theorem provides

\[
A^\sharp\cong A,
\qquad
B^\sharp\cong B.
\]

This is a real structural **cut** operation, but it depends on side information specifying the seam.

## 5.3 Full provenance recovery
The R05 witness

\[
W_G=(J_N,i_A,i_B,Q,j_A,j_B)
\]

plus

\[
\eta_F=(q,(A,a_\star),(B,b_\star),\rho,\mathsf{FUSE})
\]

stores the exact source-side constructional data.

An extraction operator can therefore return the original source presentation. This is strongest recovery, but its strength comes from retained provenance.

# 6. The cut operator

Define

\[
\mathfrak U_{\mathrm{cut}}(Q;S_F)
=(A^\sharp,B^\sharp,J_N^\sharp).
\]

For the current one-interface Fusion:

\[
\mathfrak U_{\mathrm{cut}}\circ\mathfrak F_S
\cong
\mathrm{id}
\]

on admissible source presentations, and

\[
\mathfrak F_S\circ\mathfrak U_{\mathrm{cut}}
\cong
\mathrm{id}
\]

on valid seam-decorated outputs.

The equivalence is **up to label-preserving source isomorphism**, because `q_A,q_B` are reconstructed copies rather than necessarily the original historical address tokens.

This is why R06 calls the current Fusion **seam-conditionally reversible** rather than intrinsically reversible.

# 7. The witness operator

Let the full decorated output be

\[
\widehat Q_F=(Q,\lambda_Q,W_G,\eta_F,\mathrm{Inv}_F).
\]

Define `U_W` to extract the input span and source records already retained in the witness.

Then

\[
\mathfrak U_W\circ\mathfrak F_W
=
\mathrm{id}
\]

on admissible input records.

Conversely,

\[
\mathfrak F_W\circ\mathfrak U_W
\simeq
\mathrm{id}
\]

only on valid outputs in the image of `F_W`. Arbitrary tuples that merely look like Fusion records need not satisfy the pushout or witness constraints.

This yields the classification **provenance-reversible on the image of Fusion**.

# 8. Where the information went

The most important conceptual result of R06 is that carrier-level information is not necessarily destroyed from the **full system record**.

At the carrier layer:

\[
a_\star,b_\star\mapsto q.
\]

The distinct source-interface address multiplicity is gone.

At the witness layer, however, the source identities and maps remain recorded:

\[
(i_A,i_B,j_A,j_B,\eta_F,\mathrm{tag}_A,\mathrm{tag}_B).
\]

So the correct description is:

\[
\boxed{
\text{Fusion externalizes some source distinction from the carrier into provenance.}
}
\]

If provenance is retained, reconstruction can be lossless at the representation level. If it is discarded, the carrier's many-to-one quotient becomes effective irreversible loss.

# 9. Forgetting is an operation

Introduce the forgetful map

\[
\mathrm{Forget}(Q,W_G,\eta_F,\mathrm{Inv}_F)=Q.
\]

Then

\[
\mathrm{Forget}\circ\mathfrak F_W
=
\mathfrak F_{\mathrm{bare}}.
\]

This matters because the same Fusion event can therefore have different reversibility depending on what the system chooses to retain.

It is incorrect to say simply:

> Fusion is reversible.

It is also incorrect to say simply:

> Fusion is irreversible.

The complete statement is:

> **The current weak Fusion is irreversible from its bare quotient carrier, conditionally reversible from a retained seam, and provenance-reversible from its complete witness record.**

# 10. Exact 2×2 seed accounting

For the current seed pair:

\[
|A|=4,
\qquad
|B|=4,
\qquad
|D|=8,
\qquad
|Q|=7.
\]

The quotient fiber distribution is:

- six singleton fibers;
- one two-element fiber at `q`.

Therefore the exact number of set-theoretic sections of `pi` is

\[
1^6\cdot2=2.
\]

This is useful because it makes the failure of section-based unfusion concrete: both sections necessarily choose only one of the two null-interface antecedents.

The R06 verifier confirms the cardinalities, the two sections, null-label preservation under cutting, and re-Fusion of the cut sources back to an isomorphic seven-locus quotient.

# 11. Reversibility table

| Data retained after Fusion | Can recover source geometry? | Can recover source order/provenance? | Classification |
|---|---:|---:|---|
| `Q` only | no canonical recovery | no | IRREVERSIBLE / NON-IDENTIFIABLE |
| `Q,q` | not generally | no | IRREVERSIBLE |
| `Q,A_F,B_F,q` | yes, up to isomorphism | side labels if marked | CONDITIONALLY REVERSIBLE |
| `Q,W_G,eta_F,Inv_F` | yes | yes | PROVENANCE-REVERSIBLE ON IMAGE |
| plus archived `rho_AB` | state record yes | yes | archival only; quantum dynamics unresolved |
| physical fused system | unknown | unknown | NOT ESTABLISHED |

# 12. Quantum firewall

The hybrid R04 object may retain `rho_AB` as a state record. Extracting that record later does not mean a physical quantum process ran backward.

A future isometric encoding

\[
V_F:\mathcal H_{AB}\to\mathcal H_F
\]

would satisfy

\[
V_F^\dagger V_F=I
\]

and therefore admit a left inverse on its image. But `V_F` is not currently derived.

R06 therefore keeps three concepts separate:

\[
\text{archival recovery}
\neq
\text{structural cut}
\neq
\text{quantum dynamical inverse}.
\]

# 13. Physical firewall

Nothing in R06 establishes a physical Fusion machine, reversible Hamiltonian, thermodynamic process, or time-reversal symmetry. The report concerns formal reconstructability of the present mathematical object.

# 14. Vera synthesis

Vera's anti-recursion audit finds no need to weaken the result. The central distinction is stable:

1. quotienting is noninjective at the carrier level;
2. seams can make the quotient structurally cuttable;
3. witnesses can preserve exact historical/provenance data externally;
4. none of this proves physical or quantum reversibility.

# 15. R06 closure

The current Fusion operator is classified as

\[
\boxed{
\textbf{PROVENANCE-REVERSIBLE / SEAM-CONDITIONALLY REVERSIBLE / BARE-CARRIER IRREVERSIBLE}
}
\]

The next run may therefore ask what happens to **chirality itself** without first having to pretend that the source pair either disappeared completely or remained independently separable.

**Next:** R07 — Chirality Conservation.
