# Faithful embedding audit: original Genesis / MK43 into GRC-1

**Version:** 0.1, 31 October 2026.  
**Question:** Does the entire original microscopic Genesis theory embed faithfully into the new GR-equivalent GRC-1 model?  
**Determination:** A faithful embedding of the full original theory is **not established**. The GR encoding remains valid on its stated domain. The natural metric/matter-preserving attachment does not become faithful merely by applying that encoding. Explicit recovered-interface collisions survive it, and a source-action specialization has a coordinate-invariant kinetic obstruction to an ordinary same-metric, regular scalar-field embedding into GRC-1's explicit free-scalar branch.

This is an audit, not a replacement of either model. The old source archive and the GRC-1 package are unchanged. The eight-scalar target used here is the **explicit matter branch** of GRC-1 v0.1, not its more general theorem schema allowing any separately specified matched matter action.

## 1. What has actually been inspected and rerun

The audit reads GRC-1's complete theorem, change ledger, executable encoder and 43-check suite; the original canonical API's metric, scalar action, ER graph operator and recurrence; the previous action-reconciliation record; and the Atlas's attainable-evidence recovery proposition. The canonical API text is preserved byte-for-byte in evidence/API43_CANONICAL_UNCHANGED.md. Its SHA-256 is `0071c1d9d6a89c283f57a9c225857fa8f49a63f8caff86d83cca4a66896b0259`.

The GRC-1 archive integrity check passed before its extracted copy was used. All 43 GRC-1 tests passed again. Their new execution record is retained under results/. Separately, this audit runs 32 new exact checks. A successful audit check can mean that a counterexample was correctly detected; it does **not** mean that an embedding passed.

This is a focused comparison of specified mathematical interfaces and action branches. It is not a complete re-audit of every original microscopic state, source archive, latest repository revision, constraint, or quantum claim. In particular, an interface fixture below is not silently promoted to a complete microscopic on-shell state.

### Source map

- **S1:** GRC-1 THEOREM.md, sections 4–11: canonical positive-pair encoding, global recharting, regular Jacobian, complete action and explicit scalar branch.
- **S2:** GRC-1 MODEL_CHANGES.md: finite versus local graph, covector choices, old reference, independent graph action, completed-square scalar action, and original History/Bandwidth exclusions.
- **S3:** API43_ACTION_SOURCE.md, S2–S5: original phase and chromatic actions and mixed interaction. The action/equation variants are retained, not reconciled silently.
- **S4:** API43_ACTION_SOURCE.md, S8–S10: symmetric nonnegative weights, metric sum, ER Laplacian and recursive-depth recurrence.
- **S5:** API43_ACTION_SOURCE.md, S4 and S6: deferred ER action, covector choice, chromatic metric, and coarse-graining obligations in this source.
- **S6:** The Atlas of Becoming, Appendix A.3, supplied PDF page 54 (printed page 49): recovery is relative to attainable evidence and an explicitly chosen equivalence relation. The supplied page image was inspected.

Source choices are described as such. A literature reference supports the use of field-space invariants; it does not determine the original Genesis field-space metric.

## 2. What “faithful embedding” means in this audit

Let N be a specified set of original complete configurations or solution histories, with independently justified native physical equivalence. Let C be GRC-1 configurations or solutions, respectively, with its corresponding physical equivalence. Fix the intended observable interpretation, spacetime region, matter fields, couplings and boundary data.

For a physical embedding, a map i:N→C must:

1. be defined on the stated native domain and carry native solutions to target solutions;
2. distinguish all native physical classes that the comparison retains;
3. preserve the intended geometry, sources, observables and boundary data;
4. intertwine the compared operations/evolution, with their domains of admissibility.

An embedding need not cover every target solution. Equivalence onto the **whole** GRC-1 theory requires that additional coverage statement. This distinction is important when interpreting the target-solution test in section 7.

A fully general embedding involving nonlocal or derivative-dependent maps is a different, broader problem. The kinetic no-go result below is specifically for regular local derivative-free scalar-field maps preserving the spacetime metric and the specified matter action/kinetic structure. No conclusion about all imaginable embeddings is inferred from that result.

## 3. A precise transfer theorem: re-encoding cannot repair information loss

Write

    D : C → Y,          E : Y → C,

for GRC-1 decoding and encoding, where Y is its matched GR metric-plus-matter configuration space. The existing GRC-1 proof gives

    D∘E = id_Y,         E∘D = id_C.

Let P:N→Y be the original theory's complete proposed GR readout. A readout-preserving embedding must obey

    D∘i = P.

Apply E to obtain the unique possible compatible map:

    i = E∘P.                                                   (3.1)

Thus, for any n1,n2,

    i(n1)=i(n2)  iff  P(n1)=P(n2).                              (3.2)

**Proof.** The forward implication follows by applying D. The reverse follows by applying E. Equation (3.1) follows from E∘D=id. This proof needs no linearity.

Consequently i has an inverse on native physical classes exactly when P separates those classes (and is invariant on genuinely redundant representatives). GRC-1 adds a lossless encoding of its inputs, not new evidence about a microscopic input that P erased. It cannot reconstruct an original graph or History label from a canonical code unless the retained target data already determine it.

For differentiable maps on an admitted local model,

    D i_n = D E_{P(n)} ∘ D P_n,
    ker(D i_n) = ker(D P_n),                                  (3.3)

because DE is invertible. A singular original readout is not regularized by applying asinh to its metric components.

### Dynamics also transfer without improvement

Suppose U_Y is a target update and U_C=E∘U_Y∘D its GRC-1 expression. Then

    i∘U_N = U_C∘i  iff  P∘U_N = U_Y∘P,                        (3.4)

on matching domains. Apply D for one direction, E for the other. For partial maps, enabledness must also match. Thus GRC-1 is a convenient target for testing the old theory, but it does not by itself establish the old dynamics-to-GR theorem.

Equations (3.1)–(3.4) also apply on previously justified physical quotients. They are not a license to define native physical equivalence as “anything P forgets.” The Atlas's A.3 states exactly the necessary recovery condition on the attainable image.

## 4. A source-defined graph ambiguity survives canonical GRC-1 encoding

The recovered law is

    g_ER = λ Xi W Xiᵀ,     W=Wᵀ,     W_ij≥0,

with graph operator

    (L_W f)_i = Σ_j W_ij(f_i−f_j).

Take five channels and the SAME fixed covector matrix for both states:

    Xi = [ I_4 | e_0 ],
    v = (−1,0,0,0,1)ᵀ,
    K = vvᵀ,
    W1 = 2 I_5 + Ones_5,
    W2 = W1 + K/2.                                            (4.1)

Both networks are symmetric and strictly entrywise positive. Xi v=0, so

    Xi(W2−W1)Xiᵀ = 0.                                        (4.2)

No change of covectors is needed for this collision.

For a concrete regular readable metric set λ=1/10 and fix the shared background

    g0 = η − λ Xi W1 Xiᵀ,

with identical zero phase/chromatic increments in this interface fixture. Both readouts are exactly η. Their GRC-1 canonical Z, P and Q encodings are therefore identical. The constant background used here is itself Lorentzian, but its microscopic generation and joint source constraints are not established by this test.

The graph spectra differ:

    spec L_W1 = {0,5,5,5,5},
    spec L_W2 = {0,4,5,5,5}.                                  (4.3)

They cannot be related by a node permutation or a similarity preserving this operator. Under the recovered recurrence

    H[n+1] = (2I−c_A² L_W)H[n]−H[n−1],

identical initial amplitude vectors give different next native amplitudes for suitable data. The tests use c_A²=1/2, so the nonzero spectral parameters remain inside the stable 0< c_A² λ <4 branch. The index n is kept as recursive update depth; no interpretation as GR coordinate time is imposed.

**Established failure:** the proposed target consisting of this metric and identical retained scalar data cannot also recover the original graph operator for every input in this source-interface family. Canonicalization does not make the collision disappear.

**Not established:** both fixtures are solutions of the complete original microscopic action and constraints, or that the COMPLETE physical GR history of the full theory would fail to distinguish them. The ER stress may distinguish them; admissibility may remove one; additional fields might retain the distinction. Those possibilities have not been evaluated. Hence this is a definite interface-level nonfaithfulness result, not a universal no-go theorem for the full theory.

An old white-reference tuple mapped to the canonical code of η likewise need not have the same W matrix: differing numerical representations do not themselves constitute an obstruction. What matters is preserving the old graph's physical content when it is claimed to be part of the embedding.

## 5. A new invariant test: the scalar kinetic geometries differ

The displayed old scalar action, specialized explicitly to the real constant chromatic coefficient G^{ab}=δ^{ab}, has kinetic part

    L_old = −β/2 (dτ)² −1/2 Σ_a(dχ_a)²
            −γ Σ_a χ_a dτ·dχ_a,                             (5.1)

with β>0. Potentials are set to zero to isolate the kinetic comparison. This is an allowed algebraic specialization of the displayed source coefficient, not a claim that G=I is the uniquely selected physical law of the entire old theory. No unprovided S_ER term is assumed to cancel or modify (5.1).

Interpret the eight scalar values (τ,χ_1,...,χ_7) as coordinates of their kinetic field space. The associated metric is

    K_old = [ β          γχᵀ ]
            [ γχ         I_7 ].                               (5.2)

For GRC-1's explicit completed-square branch,

    K_new = [ β          γχᵀ                  ]
            [ γχ         I_7+(γ²/β)χχᵀ       ].              (5.3)

This is a geometry of possible FIELD VALUES, not the physical spacetime metric. Curvature here compares scalar interactions and is not a claim about spacetime curvature.

### 5.1 Complete the square without changing the original action

Set a=γ²/β and make the same globally defined circle shift used by GRC-1:

    Θ = τ + γ|χ|²/(2β) mod 2π.

For the OLD action, this gives

    ds²_old = β dΘ² + dχ·dχ − a(χ·dχ)².                     (5.4)

For the NEW action, the final subtraction is exactly canceled by its added completion term:

    ds²_new = β dΘ² + dχ·dχ.                                (5.5)

The new kinetic geometry is flat. The original reduced chromatic metric is I−aχχᵀ. It is positive definite in the open ball a|χ|²<1, degenerate at a|χ|²=1, and has one negative radial eigenvalue outside that ball. The old full determinant is β−γ²|χ|²; the new determinant is β.

The obstruction below occurs INSIDE the positive, regular region, including the origin. It does not rely on extrapolating to a degenerate or negative-kinetic branch.

### 5.2 Curvature calculation

Let m be the number of real chromatic components (m=7 for the tested source branch), r²=|χ|². In polar coordinates on the chromatic field space,

    ds²_chi = (1−ar²)dr² + r² dΩ²_(m−1).

Define proper radial distance s by ds/dr=√(1−ar²). Then

    dr/ds = (1−ar²)^(−1/2),
    d²r/ds² = ar/(1−ar²)².

With the curvature convention R(X,Y)Z=∇_X∇_Y Z−∇_Y∇_X Z−∇_[X,Y]Z, the warped radial geometry gives

    K_radial = −a/(1−ar²)²,
    K_tangential = −a/(1−ar²).

There are m−1 independent radial planes and (m−1)(m−2)/2 independent tangential planes. The scalar curvature is twice their sum:

    R_field,old = −a(m−1)[m−(m−2)ar²]/(1−ar²)².             (5.6)

The phase direction is an independent flat line locally, so it adds zero to this scalar. At the origin,

    R_field,old(0) = −m(m−1)γ²/β.

For seven chromatic components:

    R_field,old(0) = −42γ²/β,     R_field,new = 0.             (5.7)

The implementation independently calculates the FULL eight-dimensional Riemann tensor from exact first and second metric jets at the origin. It does not infer an ambient curvature from a curved two-dimensional slice. It also calculates full jets at nonzero interior points for m=2 and m=7, verifying (5.6), and checks that the new full Riemann tensor vanishes there. A negative control verifies that m=1 has no such curvature obstruction; a single active χ can indeed be flattened on a regular interval.

### 5.3 The precise exclusion theorem

Assume a regular derivative-free local map of all eight independent scalar fields, preservation of the physical spacetime metric, and preservation of the scalar kinetic action/stress structure, with no extra compensating interaction. If the old sector embedded into the new eight-scalar sector in this way, its kinetic metric would be the pullback of K_new under a full-rank 8→8 map. The inverse function theorem makes that map a local diffeomorphism. Curvature tensors are natural under metric pullback, so its pullback of a flat metric must be flat. Equation (5.7) contradicts flatness when γ≠0.

Therefore there is NO such regular same-metric point-field embedding of the source specialization (5.1) into GRC-1's explicit free-scalar branch near χ=0 when at least two chromatic fields vary independently.

This argument is stronger than detecting a missing term under one chosen substitution: it rules out every regular local scalar-coordinate repair in that declared class. Standard nonlinear-sigma-model literature explains why scalar-field redefinitions are coordinate changes of kinetic field space and why its curvature is invariant [R1]. The present curvature computation is supplied here rather than borrowed from that paper.

### Limits of this theorem

- G^{ab}=I is a specified specialization, not the unknown unique original G^{ab}(χ).
- The result concerns the displayed scalar kinetic sector with independent scalar variations at fixed spacetime metric. Original native constraints might admit only a smaller sector.
- An additional S_ER or another kinetic sector might change the TOTAL kinetic geometry. Its form has not been supplied here.
- Derivative-dependent maps, transformations changing the physical metric, nonlocal constructions, extra target fields, or a different target matter action are outside this exclusion theorem.
- Preserving a selected set of solutions is weaker than a full local action/stress embedding and is not ruled out by a failure of an off-shell action isometry alone.
- Curved source manifolds can have isometric embeddings into higher-dimensional flat manifolds; that is not the same eight-independent-field problem, and it would not automatically preserve unconstrained wave-map dynamics.

For a general original G(χ), the object to test is

    K_original = [ β             γ(Gχ)ᵀ ]
                 [ γGχ          G       ],

including every additional kinetic contribution in the fully specified action. Its curvature, signature, allowed variations, potentials and global circle structure must be compared; setting G=I without declaring it would be an error.

## 6. Matching metric readouts does not match stress tensors

The difference between the completed and original kinetic Lagrangians is

    L_new−L_old = −γ²/(2β) (χ·dχ)².                          (6.1)

This term contributes to metric variation. It cannot be treated as a harmless relabeling merely because the phase change has a triangular Jacobian. The field-space argument shows that for m≥2 its effect cannot be removed by another ordinary scalar-coordinate choice while preserving the metric and all scalar kinetic directions.

A literal equality of the two kinetic matrices with unchanged τ,χ would require both G=I+aχχᵀ and Gχ=χ if the same old G is used in the original mixed term. These requirements are incompatible at generic nonzero χ for a≠0. This simple coefficient check is secondary; the invariant proof gives the more robust result for the constant-G specialization.

## 7. An on-shell GRC-1 solution fails the direct old-action return

Rerun the exact GRC-1 solution with t>0, κ=β=1, γ=2, Λ=0:

    g = diag(−1,t^(2/3),t^(2/3),t^(2/3)),
    Θ = χ_1 = ln(t)/√3,     χ_2=...=χ_7=0,
    τ = ln(t)/√3 − (ln t)²/3.

Its eight-scalar action-derived source solves the GRC-1 Einstein equations. Evaluate instead the original displayed scalar action (5.1) with these τ,χ values, still with G=I and zero potentials. The metric residual against that original source is

    (Einstein−T_old)_00 = 2(ln t)²/(9t²),                    (7.1)

and the chromatic Euler–Lagrange residual, using δS=∫√−g EL δχ, is

    EL_chi_1,old = 4 ln t/(3√3 t²).                          (7.2)

The new chromatic residual is zero. The old phase equation also vanishes on this fixture, which localizes the failure rather than merely reporting a generic discrepancy. The spatial stress differences are g_ii times (7.1).

These formulas are obtained from independent action/stress variations and direct curvature, not by defining a source to fit Einstein's tensor. They confirm that the direct identification does not preserve this full target solution under the old displayed action.

**Important logical limitation:** an embedding need not be onto all target solutions. The failure of one target solution to be an old solution does not by itself disprove the existence of some smaller source→target embedding. Equations (7.1)–(7.2) reject the direct full identification; section 5 supplies the separate local kinetic obstruction. Neither result assumes an unknown ER term vanishes in the entire old theory.

## 8. A constructive compatible route retains the original matter rather than replacing it

The positive-pair GRAVITY encoder does not depend on choosing free scalar matter. GRC-1's theorem itself allows any separately specified matched matter action. Therefore the eight-free-scalar target is not the only useful continuation.

For the explicit original-action specialization (5.1), retain it unchanged and define a DIFFERENT matched-matter version:

    S_matched[Z,τ,χ] = S_EH[h(Z)] + S_old,scalar[h(Z),τ,χ].    (8.1)

The inverse is simply

    (Z,τ,χ) ↔ (g=h(Z),τ,χ),
    Z=asinh(g/σ),

with identical matter fields, couplings, sources, potentials if specified, and boundary conditions. The field Jacobian gives

    EL_Z,I = σ cosh Z_I EL_g,I,
    EL_tau,new = EL_tau,old,
    EL_chi,new = EL_chi,old.                                  (8.2)

All multiplier factors are nonzero. Consequently this changed target has exact classical equivalence to GR coupled to THAT original scalar action on the stated regular domain. It keeps the curved kinetic geometry instead of flattening it through an additional interaction.

This is a constructive and exact repair for the specified action sector. It is NOT an embedding into the unchanged eight-free-scalar GRC-1 branch, NOT an adoption of the conflicting printed scalar equations, and NOT a completion of the original microscopic model. An independent ER graph or other native fields must be retained with their actual equations or reconstructed by a separate proof. Simply appending their names does not supply their dynamics.

A metric-only encoder may also accompany an auxiliary native record, as the Atlas permits. That gives recovery from GR PLUS that record. It must not be advertised as recovery from the unchanged GRC-1 physical state alone. The size and physical necessity of such data have not been determined for the full original model.

## 9. Audit verdict by claim

| Claim | Result | Exact scope |
|---|---|---|
| GRC-1's new model is a regular GR reformulation | Rechecked; 43 prior tests pass | New defined classical branch, not microscopic inheritance |
| An evaluated old Lorentzian metric can be canonically encoded | Yes | Metric representation only; old metric must be supplied/generated |
| Canonicalization repairs old readout information loss | No | Transfer theorem (3.2); same complete input readout gives same code |
| The inspected old metric interface determines its graph operator | No for the exhibited family | Same fixed Xi, distinct positive W, same metric, different graph spectra |
| Old constant-G mixed kinetic sector is a free eight-scalar sector in unusual coordinates | No for γ≠0 | Regular same-metric derivative-free action/stress embedding of eight independent fields |
| The GRC-1 target fixture satisfies the old displayed scalar action | No | Residuals (7.1)–(7.2); unknown other sectors not added |
| The positive gravity encoding can retain curved original scalar matter | Yes | Different matched-matter target (8.1); does not solve missing microscopic laws |
| The entire original microscopic theory embeds faithfully into GRC-1 | Unestablished | Full original constraints, complete readout, total action and physical redundancy remain unclassified |

The first result is not invalidated by the later failures. Conversely, the first result is not evidence that the entire old theory has been captured. The useful consequence is a concrete design boundary: keep the regular gravitational representation, but do not replace original matter/graph content and then claim it was preserved.

## 10. Reproducibility and boundaries

Run `python code/checks.py` with Python, SymPy and NumPy available. It produces results/CHECK_RESULTS.json. The field-space module computes Christoffel symbols and the full Riemann tensor from exact metric jets. The old and completed metrics are assembled separately. The graph comparison uses exact rational matrices and exact spectra.

The new 32 checks include a positive general encoding check, graph collision and spectrum checks, original/completed kinetic matrices, full 8D curvature at the origin, nonzero-point curvature, a one-chromatic-field negative control, zero-coupling agreement, sourced GRC-1 versus original-action residuals, and the regular matched-matter chain-rule identity. These checks are not a proof assistant, empirical validation, or exhaustive classification of all possible embeddings.

All source copies have hashes in SOURCE_MANIFEST.json. The original GRC-1 ZIP is included unchanged under prior/. That archive already contains the preceding source/action checkpoint. The full cumulative 404 MiB recovery is not duplicated; this is an incremental audited result.

## References

**R1.** R. Alonso, E. E. Jenkins, A. V. Manohar, *Geometry of the Scalar Sector*, JHEP 08 (2016) 101, arXiv:1605.03602. Sections 1 and 4 explain field redefinitions as coordinate changes and invariant kinetic field-space geometry. The source-dependent curvature (5.6)–(5.7) is calculated in this audit. `https://arxiv.org/abs/1605.03602`

**R2.** D. Tong, *General Relativity*, section 3, *Introducing Riemannian Geometry*: metric, Levi-Civita connection, curvature and invariance. `https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S3.html`

**R3.** D. Tong, *General Relativity*, section 4, *The Einstein Equations*: action variation and scalar stress. `https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S4.html`

The external references support standard comparison methods, not claims about which unspecified native Genesis functions are physically correct. The new conclusions are mathematical results about the explicitly displayed formulas and scopes.
