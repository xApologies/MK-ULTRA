# Genesis–GR native ER attachment: recovered metric law and constructive inverse

**Date:** 31 October 2026  
**Status:** Source-based, implemented ER-weight/phase-to-metric attachment, with exact inverses on explicitly identified image sectors. **Not a proof of total native Genesis–GR equivalence.**  
**Integrity:** Existing sources and prior checkpoints remain unchanged. The new derivations below are distinguished from the recovered formulas. An example is not labeled a generated solution of all native laws.

## 0. What changes in this continuation

The previous operation-translation checkpoint started with evaluated native metric and source tensors. This continuation starts one step earlier for part of the archived field interface: native ER adjacency weights W and the phase field tau. It evaluates metric contributions using formulas actually present in API 4.3, rather than inventing a metric functional or using the final GR metric as the input to its own derivation.

The earlier search for the exact symbol Q_R did not constitute an exhaustive search for metric constructions. API 4.3 contains explicit phase and ER contributions. Saying that no metric-construction rule had been recovered at all would be too broad. The narrower remaining boundary is the complete Q_R attachment, the native construction of ER covectors, chromatic metric generation, and full native source/dynamical closure.

A targeted QMO database lookup led back to the canonical API. The complete source Markdown is included byte-for-byte. Its text agrees byte-for-byte with source_files record FILE-0071c1d9d6a89c283f57a9c2 in the original unified database. Exact line-numbered passages and database provenance are in evidence/.

New results:

1. An explicit inverse of the recovered four-channel ER metric rule, with native sign conditions and target-domain checks retained.
2. A complete constant-network reconstruction from jointly separating spacetime readouts, including an explicit five-channel/three-point decoder.
3. A composition of that attachment with the existing two-way differential translator.
4. Direct evaluation of the recovered phase metric and its stated stress tensor.
5. Exact tests of a curved Einstein endpoint, an off-shell phase configuration, and invalid inverse proposals.

None of these results supplies the missing map from all raw Genesis variables to Xi and g_chi, nor an independent ER stress-energy/dynamics law.

## 1. Source facts, not new definitions

The recovered API declares a phase field

    tau : M -> R / (2 pi Z),

and a nonnegative symmetric ER adjacency matrix

    W_ij >= 0,     W_ij = W_ji.

The weights are entrywise nonnegative. This is NOT the condition that W be a positive-semidefinite quadratic form.

The metric contributions are [S2–S3]:

    g_tau,munu = alpha (partial_mu tau)(partial_nu tau),

    g_ER,munu = lambda sum_(i,j) W_ij xi_mu^(i) xi_nu^(j),

    g = g_0 + g_tau + g_chi + g_ER.                         (1)

The ER expression is also independently indexed as MATH-0390, with original source chapters_6_10/chapters_6_10.tex [S6]. The code does not treat the duplicate appearance as a separate theorem.

The reference-state record includes

    d tau = 0,    chi = 0,    W = I,    g = eta.             (2)

The same API expressly retains these open items [S5]:

- reconcile the phase metric with the explicit Time-Shell projection;
- specify the functional form of g_chi;
- specify the ER basis covectors xi^(i);
- reconcile the white-state adjacency with connectivity semantics;
- type the W_ij -> W_IJ coarse-graining map.

Those qualifications travel with the formulas. In particular, a supplied covector array in a test is not a recovered law producing that array from a raw native state.

The source's phase stress tensor is [S4]

    T_tau = beta u u^T - (1/2) g [beta (u^T g^(-1) u) + V(tau)],
    u = d tau.                                             (3)

It is one contribution, not the total stress tensor. This calculation uses the displayed action-compatible stress expression. The previously identified mismatch between the displayed phase action's V/2 normalization and its separate standalone field equation is not silently repaired here. The off-shell phase test uses V=0, so that discrepancy cannot affect it.

The complete action names S_ER but the inspected passages do not specify its functional dependence sufficiently to derive a total ER stress tensor or complete ER equations. The entropy-style expression involving S_ER elsewhere is not substituted for an action.

## 2. A correctly typed matrix form

Put the supplied ER covectors into columns:

    Xi_(mu i) = xi_mu^(i).

Xi has four spacetime rows and n ER-index columns. The number n is a number of ER channels/sites in this representation; it is NOT the dimension of the upstream 3+1+1 manifold. Nor is Xi the differential anchor A in the previous tensor-translation proof.

Then

    g_ER = lambda Xi W Xi^T.                               (4)

For a direct metric inverse, the non-ER terms, coupling, and Xi must be known and held fixed, or have their dependence separately evaluated. It would be circular to select these terms afresh after seeing each target metric solely to force a lift to exist.

The four-channel theorem assumes Xi is a real invertible 4-by-4 matrix at every point of the declared region and lambda is nonzero. Xi may vary smoothly across spacetime; its variation is retained by the differential translator. It is not assumed to depend on the unknown W. Such dependence would change the inverse problem.

For n greater than four, the single-point map need not be injective. A constant network can nevertheless be recovered from several spacetime readouts. Sections 6–7 prove exactly when this happens.

## 3. Reference calibration: do not add the white-state contribution twice

Equation (2) does not license setting g_0=eta and then adding lambda Xi Xi^T without checking the other terms. At a reference state, the sum of all contributions must be the declared reference metric.

Let W_ref, u_ref, g_chi,ref and g_ref refer to a common reference at the same spacetime point. Subtract the reference instance of (1) from the actual instance. Provided Xi, lambda and the background are the same in the two instances,

    g = g_ref + alpha (u u^T - u_ref u_ref^T)
                  + Delta g_chi
                  + lambda Xi (W - W_ref) Xi^T.            (5)

This is an algebraic consequence of the archived sum, not a replacement physical law. No assumption that g_chi vanishes follows merely from chi=0; the chromatic difference must be supplied or justified separately.

For a white reference W_ref=I and u_ref=0, and a declared zero chromatic increment, (5) reads

    g = eta + alpha u u^T + lambda Xi(W-I)Xi^T.             (6)

This form calibrates the already-existing ER reference contribution. It does not define S_ER or the physical energy of W.

The program uses (5), with Delta g_chi an explicit required argument. It does not implement an implicit chi-to-metric rule.

## 4. Exact four-channel inverse

Define the corrected metric remainder

    Delta = g - g_ref - alpha(u u^T-u_ref u_ref^T)
                         - Delta g_chi.                   (7)

Equation (5) gives Delta=lambda Xi(W-W_ref)Xi^T. Therefore

    W = W_ref + (1/lambda) Xi^(-1) Delta Xi^(-T).           (8)

### Theorem 1: two-sided ER metric correspondence

Fix the reference and all non-ER context above. Let the input set contain symmetric W satisfying the declared native weight conditions and producing Lorentzian, nondegenerate metrics. Let the target set be precisely the metrics for which (8) satisfies those same conditions. Then (5) and (8) are two-sided inverses.

Proof. Substituting (5) in (8) gives

    W_ref + Xi^(-1) [lambda Xi(W-W_ref)Xi^T] Xi^(-T)/lambda
      = W_ref + W-W_ref = W.

Substituting (8) in (5) gives

    g_ref + non_ER_increment
       + lambda Xi[Xi^(-1)Delta Xi^(-T)/lambda]Xi^T
      = g_ref + non_ER_increment + Delta = g.

All cancellations are exact. Inverse congruence preserves symmetry. Native nonnegativity and metric signature are imposed on the actual domain, not inferred from the cancellation. QED.

The target restriction is constructive: compute (8), check symmetry and entrywise nonnegativity, and check any additional native restrictions. The current program reports UNKNOWN when a symbolic sign is not established; it never promotes that status to admitted.

For example, in the context Xi=I, lambda=1, W_ref=I, zero phase/chromatic increment, the Lorentzian target equal to eta except for g_01=g_10=-1/10 produces W_01=-1/10. It has a perfectly good Lorentzian signature but is not in this native weight-image sector. This is a restriction of this fixed context, not a proof that no other native sector can represent that metric.

### Phase and other fields must not be discarded

With the phase retained as a matter field, the corresponding tuple map is

    (W,tau,other retained fields) <-> (g,tau,other retained fields),

with fixed context. A metric alone does not generally recover the separately contributing phase, chromatic field and network. Circle-valued tau may require local real lifts; the source's global phase and winding information is retained rather than inferred from a squared gradient. No new phase-reflection gauge is declared.

### Covariance

Under a coordinate change with covector-component matrix J^T,

    g' = J^T g J,    Xi' = J^T Xi,    u' = J^T u.

The other rank-two terms transform likewise. In (8) the J factors cancel, leaving the same ER-index weights. Changing the internal ER-site basis is a different operation: it can change entrywise positivity and is not automatically gauge.

## 5. One constant network versus a resolved field of networks

A finite graph has one matrix W for its named sites. Its Xi(x) may vary with spacetime in the metric realization. Applying (8) pointwise to a target metric gives a candidate W_hat(x). A target belongs to the image of the SAME constant graph only if W_hat is constant across the connected region, as well as satisfying (5) everywhere.

It is not legitimate to obtain a different graph at every point and call that a reconstruction of the original constant graph. The implementation checks the constancy condition symbolically where it can. Unsupported symbolic constancy stays unresolved.

One may additionally study a smooth resolved-field interpretation W=W(x). In that setting, (8) is a local field redefinition. That is a distinct hypothesis. The source explicitly retains coarse-graining semantics as open; this work does not infer the field interpretation or a continuum limit from a finite adjacency matrix.

For a fixed finite graph, neither the finite number of W parameters nor an inverse at one point establishes coverage of arbitrary smooth metric fields.

## 6. The complete single-point inverse family for more channels

Assume Xi has full row rank four and n>=4. Choose any matrix R with Xi R=I_4. For a corrected Delta, the solutions of

    Xi(W-W_ref)Xi^T = Delta/lambda

are exactly

    W = W_ref + R(Delta/lambda)R^T + K,
    K=K^T,    Xi K Xi^T=0.                                 (9)

Proof. Substitution verifies every displayed candidate. Conversely subtract the selected representative from any solution; its difference is symmetric and annihilated by the metric map. QED.

This is an affine family intersected with entrywise nonnegative weights and all further native conditions. The selected representative is not necessarily nonnegative. A pseudoinverse is not automatically an admissible or physically unique network.

On symmetric matrices, the map W -> Xi W Xi^T has rank ten when Xi has row rank four. It is onto Sym_4 because R D R^T maps to D for any symmetric D. Hence its kernel has dimension

    n(n+1)/2 - 10.                                         (10)

At an interior point of the entrywise-positive cone, sufficiently small symmetric kernel perturbations remain positive. Thus the single-point loss is not merely an artifact of allowing invalid negative weights.

The code checks an actual collision of the recovered formula with n=5:

    Xi = [I_4 | e_0],
    v = (-1,0,0,0,1)^T,    K=v v^T,
    W_1 = 2I_5 + Ones_5,    W_2=W_1+K/2.

Both weight matrices are symmetric and entrywise positive, and Xi K Xi^T=0. This is a collision of this metric formula. It is NOT proof that all native source observables and dynamics also fail to distinguish the networks.

## 7. Recovering a whole constant network from the complete metric field

A pointwise kernel does not by itself establish information loss from an entire field. The same W may be sampled by different Xi(x).

For known Xi at points x_1,...,x_m, define

    L(W) = (Xi(x_a) W Xi(x_a)^T)_(a=1,...,m).

In a basis of symmetric n-by-n matrices, this is an ordinary linear map with n(n+1)/2 unknowns and at most 10m scalar equations.

### Theorem 2: exact constant-network recovery

The metric readouts at those points determine every symmetric W uniquely if and only if

    intersection_a {K=K^T : Xi(x_a) K Xi(x_a)^T=0} = {0}.    (11)

Equivalently, the stacked observation matrix has full column rank n(n+1)/2.

Proof. If two networks give the same observations, their difference lies in the intersection. If the intersection is zero they agree. If it contains a nonzero K, W and W+K have the same linear observations. When considering positive-network uniqueness, a small multiple of K gives distinct positive weights around an interior point. Full column rank gives a left inverse on the image by finite linear algebra. QED.

This is the Atlas's common-kernel recovery principle applied to the actual recovered ER formula, rather than an unrelated hidden-label model. It is a statement about fields sharing ONE network, not arbitrary independent W(x).

The code assembles the exact coefficient matrix, rejects deficient rank and inconsistent observations, solves only when the solution is unique, and checks the native signs of the recovered weights.

### An explicit five-channel decoder

Set

    Xi(s) = [I_4 | s e_0].

This is full row rank for every s. Write the unknown symmetric correction as

    W-W_ref = [[A,b],[b^T,c]],

where A is four-by-four, b has four components, and c is a scalar. Normalize the corrected metric by lambda:

    D(s) = Delta(s)/lambda.

Direct expansion gives

    D(s) = A + s(e_0 b^T+b e_0^T) + s^2 c e_0 e_0^T.      (12)

The three readouts D(-1), D(0), D(1) therefore give

    A = D(0),
    b_0 = [D(1)_00-D(-1)_00]/4,
    b_i = [D(1)_i0-D(-1)_i0]/2       (i=1,2,3),
    c = [D(1)_00+D(-1)_00-2D(0)_00]/2.                     (13)

These formulas recover all fifteen independent entries. Substitution in (12) proves the round trip for the entire represented metric family, not merely for the three sampled values. The stacked operator has rank fifteen, verified exactly.

The supplied-covector assumption remains: (12) is a test realization of the source's ER covectors, not a recovered microscopic derivation of them. The theorem explains how the actual covector family can remove metric-level ambiguity once known.

### Image membership still matters

For an arbitrary target field, matching three samples does not establish (12) at every point. A target can be modified by

    s(s-1)(s+1) E_22

without changing any of the three samples. That term is not generated by the reconstructed constant graph in this family. The code deliberately tests and detects this failure by the full symbolic field identity.

Coverage is therefore checked by reconstructing W and then checking the original metric identity throughout the declared domain. The finite decoder proves unique candidate recovery, not universal reachability of every metric.

## 8. Native source evaluation that is actually available

The recovered phase stress expression (3) is implemented directly. It uses the computed metric and the specified native phase gradient; it does not define stress by dividing an Einstein tensor by a coupling.

For one test, in a local real lift of the circular phase,

    tau=x y,    alpha=beta=1,    V=0,

with reference eta, unchanged ER weights and zero declared chromatic increment, the archived phase rule gives

    g = eta + d(xy) tensor d(xy),
    det g = -(1+x^2+y^2).

The spatial x-y block is positive definite and the time direction is negative, so the metric is Lorentzian. Independent curvature evaluation gives

    Scal[g] = -2/(1+x^2+y^2)^2.

The phase source also gives

    Box_g tau = -2xy/(1+x^2+y^2)^2,
    nabla^mu T_tau,munu = (Box_g tau) partial_nu tau.

The second expression is generally nonzero. This is deliberately an off-shell input: it tests evaluation and rejects any automatic promotion of a constructed metric/source pair to an Einstein solution.

Full T_ER, chromatic action consistency, couplings and retained matter data are not inferred from this single contribution. Native finite-flux records, when supplied, can still use the existing flux decoder. Their values and conservation cannot be manufactured from target curvature.

## 9. An actual round trip through the prior translator

Use a connected local chart t>0, with constant h>0, unit ER coupling, a white reference (eta,I), zero phase increment and an explicitly declared zero chromatic increment. Supply the test covectors

    Xi(t) = diag(1,f(t),f(t),f(t)),
    f(t) = sqrt(exp(2ht)-1),

and the SAME constant network at every point,

    W = diag(1,2,2,2).

Equation (5), not an externally supplied final metric, computes

    g = diag(-1, exp(2ht), exp(2ht), exp(2ht)).              (14)

The inverse (8) returns diag(1,2,2,2) exactly and verifies its constancy. Since t>0 the covectors are independent. The failure of this inverse at t=0 is an ER-realization rank failure in this example, not a spacetime curvature singularity.

The unchanged prior translator receives the computed metric. It evaluates the source's smooth metric-compatible connection by its native Koszul route, independently evaluates the conventional coordinate route, and obtains matching Riemann tensors. It returns

    Scal=12h^2,    G=-3h^2 g.

A supplied zero total flux tensor and Lambda=3h^2 make the endpoint Einstein residual exactly zero. Translating back and applying (8) returns the original ER weights.

This is a constructed curved Einstein endpoint in the recovered API interface. The ER covectors and total flux are explicit test inputs. It is NOT a demonstration that the still-unspecified native S_ER has zero source on this network, that all microscopic native constraints admit the network, or that the source derives Xi(t). The test does not make that stronger claim.

## 10. Differential and variational implications

Because the new map evaluates actual metric expressions, its derivatives can be passed to the prior operation-preserving tensor translator. This attaches the recovered constituent map to the previously proved smooth correspondence. It does not prove that the chosen smooth connection equals the upstream finite connection selector in every native state.

There is also a precise variational result for the SEPARATELY DECLARED smooth resolved-field interpretation, where the ten W_ij(x) are independent local field variables in an open admissible sector. It does NOT apply to one constant finite graph with only finitely many parameters.

Keep Xi, the background/chromatic context, and alpha/lambda fixed under the variations, with Xi invertible and lambda nonzero. Retain tau as an independent field. The actual constitutive rule gives

    delta g = lambda Xi delta W Xi^T
              + alpha[d tau tensor d(delta tau)
                       + d(delta tau) tensor d tau].      (15)

For every target pair (delta g,delta tau), solve

    delta W = Xi^(-1)[delta g
                 -alpha(d tau tensor d(delta tau)
                         +d(delta tau) tensor d tau)]
                  Xi^(-T)/lambda.                         (16)

Thus the variation map is onto in this declared open field sector. This is a proved rank property of this recovered formula, not merely a stated lifting requirement.

For any specified target action S[g,tau,psi], define its expression in these variables by substitution of the archived metric rule. Let E_g and E_tau denote variational derivative densities in a coordinate chart. With compactly supported variations and the symmetric-matrix pairing,

    E_W = lambda Xi^T E_g Xi,
    E_tau^(W) = E_tau - 2 alpha partial_nu(E_g^(mu nu) partial_mu tau).  (17)

The first identity follows by substituting (15); the second follows by one integration by parts. Invertibility of Xi and lambda gives E_W=0 iff E_g=0; on that locus the phase equations coincide. The argument preserves the same action, and so cannot supply an unknown native action by itself.

If other explicit native W-dependence is present in S_ER, it must be transformed as well; it is not dropped. A target action with that transformed dependence need not be standard minimally coupled GR. Boundary conditions and matter/gauge degrees of freedom must also be carried through.

At a zero edge weight, the entrywise-positive domain may have a boundary and permitted variations can be one-sided or constrained. Then the open-sector proof cannot silently be applied. Additional native constraints can likewise restrict the variation image. These distinctions are essential to avoiding a false variational equivalence.

This explicit calculation is consistent with the general subject of invertible derivative-dependent field transformations [R1]; the proof here is written for the actual recovered rank-four ER map. It does not invoke a general theorem without its hypotheses.

## 11. Source-to-implementation ledger

- ER weight type: recovered, implemented for symmetry and entrywise sign diagnostics.
- Phase metric: recovered, implemented exactly.
- ER metric: recovered, implemented exactly for supplied covectors.
- Composite metric: recovered; reference subtraction derived, implemented.
- Four-channel inverse: newly derived from the recovered formula, implemented.
- Constant-network multipoint inverse: newly derived, implemented with rank and consistency checks.
- Phase stress: recovered, implemented; not a complete source model.
- Full Q_R from (D,relational structure,R,B,H,chi): not established by this run.
- Native Xi evaluator and chromatic metric rule: explicitly open in the recovered API, not invented.
- Full source/dynamics and physical inverse: not established.

The generic raw-state entry point remains unsupported. Only the newly defined recovered-API adapter is accepted. The old transformer is included byte-for-byte; the new functions are separate.

## 12. Verification and reproducibility

Run `python code/checks.py` after installing the recorded SymPy dependency. The final JSON records the actual count and outcomes, versions, execution time and individual test scopes. It includes two development logs: an overly conservative polynomial-constancy classification was corrected, and an immutable-matrix mutation in a negative test was corrected. Neither failure was silently removed.

Checks include general symbolic ten-entry round trips; native sign rejection; a Lorentzian target outside the fixed image; reference calibration; covariance; the actual five-channel kernel; three-readout recovery of all fifteen weights; a forged-between-samples target; the phase source and its off-shell conservation identity; the curved Einstein endpoint and its network return; and the field-variation identity.

These are exact implementation checks on the stated algebra and examples. They are not a proof assistant audit, an empirical validation, or a full solver for the original native gravitational dynamics.

## 13. Determination

The endpoint has advanced from an evaluated-tensor converter to a converter with a concrete recovered native field-level metric input. The ER graph weight part now has an explicit inverse under a single-point rank-four condition or a more general jointly separating constant-network readout family. A curved spacetime calculation returns those input weights exactly.

It would still be wrong to certify total native Genesis–GR equivalence. The values and physical meaning of the ER covectors, the chromatic metric map, complete source realization, and admissibility under all native dynamics remain unestablished. The source identifies several of these omissions explicitly. No lost History is declared gauge, and no guessed Xi is promoted to a recovered law.

This continuation supplies the actual equations and executable inverse for a genuine source-defined part of the native attachment. It does not replace the remaining attachment with another frame change or with an invented fully closed theory.

## References and source provenance

[S1–S7] Exact original API 4.3 passages, source paths, original line numbers and hashes: evidence/API43_EXACT_EXCERPTS.md and evidence/SOURCE_MAP.json. The complete canonical Markdown is in sources/.

[A1] User-supplied The Atlas of Becoming, foundational report, Appendix A.2–A.3, especially joint-kernel recovery and the distinction between unique reconstruction on attained observations and coverage. The already supplied report text is the basis for this reference; no new PDF parsing or image analysis was performed in this run.

[R1] Kazufumi Takahashi, Hayato Motohashi, Teruaki Suyama, Tsutomu Kobayashi, "General invertible transformation and physical degrees of freedom," Physical Review D 95, 084053 (2017), arXiv:1702.01849, v2. Author abstract retrieved 31 October 2026 from https://arxiv.org/abs/1702.01849. This is external context for the variational topic, not evidence for a native Genesis operator.
