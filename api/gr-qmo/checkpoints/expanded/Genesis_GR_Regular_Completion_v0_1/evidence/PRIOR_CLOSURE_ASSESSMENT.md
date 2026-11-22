# Genesis–GR endpoint completion attempt
## Source consistency, the coupled-source calculation, and the actual closure boundary

**Date:** 31 October 2026  
**Requested result:** a source-grounded native Genesis → GR → native Genesis equivalence, with both round trips and all admitted calculations preserving their physical meaning.  
**Determination:** that full result is **not established**. This work completes the variation of the displayed real phase–chromatic action, identifies a concrete discrepancy with its printed coupled equations, and evaluates two further native-attachment ambiguities using the recovered ER metric and graph formulas. It does not install a replacement native metric law or ER action.

The original source, the prior ER-attachment checkpoint, and all source variants remain unchanged. An action-derived equation below is a derived result under an explicit action choice, **not a silent correction of project canon**.

## 1. What was actually checked

The source basis is API 4.3's `MK43_Ultra_API_CURRENT_CANONICAL.md`, SHA-256

`0071c1d9d6a89c283f57a9c225857fa8f49a63f8caff86d83cca4a66896b0259`.

The exact original passages and line numbers are in `evidence/API43_ACTION_SOURCE.md`; the whole canonical file is preserved unchanged. The prior checkpoint, including its code and evidence, is included as its original ZIP.

A bounded scan examined 1,114 expanded Markdown, text and TeX source files, totaling 26,881,556 bytes, in the exhaustive recovery snapshot. The scan includes the archived indexed gravity-manuscript text. It does not exhaust every nested original archive, binary database, or remote repository revision. `evidence/BOUNDED_SOURCE_SCAN.json` records the literal terms, matching lines, hashes and scope. An OPEN label or a failed search is not a proof that no later construction exists elsewhere.

The inspected kernel explicitly leaves the ER covectors, the chromatic metric contribution, the coarse-graining map, and action reconciliation open [S6]. Its recovery-status section defers the exact ER action and ER stress tensor [S4]. The following analysis asks what can be established without assigning arbitrary values to them.

## 2. The exact source equations under examination

The recovered metric interface is

    g = g0 + alpha d(tau)⊗d(tau) + g_chi + lambda Xi W Xi^T,       (M1)

with symmetric entrywise-nonnegative ER weights W. Xi has the ER covectors as columns. Entrywise nonnegativity is not positive semidefiniteness of W.

The displayed local matter terms are

    L_tau = -beta (d tau)^2/2 - V(tau)/2,
    L_chi = -G^{ab}(chi) (d chi_a · d chi_b)/2 - U(chi),
    L_mix = -gamma G^{ab}(chi) chi_b (d tau · d chi_a).            (A1)

Source S7 contains another action presentation with `-V(tau)` rather than `-V(tau)/2`. This distinction is retained. Introduce the explicit coefficient zeta, so the phase potential is `-zeta V`; zeta=1/2 is the first displayed phase-action branch and zeta=1 is the other normalization. No implicit default selects between the source variants.

The printed phase–chromatic equations include

    beta Box tau - V'(tau) = gamma G^{ab} chi_b Box chi_a,
    nabla_mu(G^{ab} partial^mu chi_b) - partial^a U
        = gamma (partial_mu tau)(partial^mu chi_a).              (A2)

These are preserved as printed source statements, not as the result of our variation. The test below eliminates the potential-normalization ambiguity by using V=0.

A complete original action also names S_ER. Equations derived from A1 alone are the complete contribution of A1, not the contribution of an unspecified S_ER or other omitted interactions. Such additional sectors could alter the total equations; no cancellation is presumed without their explicit functional form.

## 3. Complete variation of the displayed real phase–chromatic sector

### 3.1 Setting

Work on a smooth Lorentzian region with signature (-,+,+,+), c=1, a nondegenerate metric and compactly supported variations, or an equivalent stated boundary prescription. Treat the metric and scalar fields as independent for this calculation. A subsequent native metric substitution has a separate chain rule in section 7.

Use the source's seven real chromatic components. A local real lift of the circle-valued phase is sufficient for this calculation; global phase winding is not reconstructed from gradients. A globally used phase potential must respect the intended circle structure. The code can also test a restricted number of active components without claiming that the source's arity changed.

Let

    u_mu = partial_mu tau,
    v_a,mu = partial_mu chi_a,
    b_a(chi) = sum_b G^{ab}(chi) chi_b.                           (A3)

The coefficient b_a is local notation for this contraction, not the native Bandwidth object. Assume G^{ab}=G^{ba} depends on chi, and beta and gamma are constants. The local Lagrangian is

    L = -beta u·u/2 - zeta V(tau)
        -G^{ab} v_a·v_b/2 - U(chi)
        -gamma b_a u·v_a.                                       (A4)

### 3.2 Metric stress tensor

With the stress convention in the archive,

    T_munu = -(2/sqrt(-g)) delta S / delta g^{munu},

direct variation gives

    T_munu = beta u_mu u_nu
             + G^{ab} v_a,mu v_b,nu
             + gamma b_a (u_mu v_a,nu + u_nu v_a,mu)
             + g_munu L.                                       (A5)

Proof. Differentiate the inverse-metric contractions in A4. A diagonal kinetic term produces the symmetric product of its two gradients. The mixed contraction produces its symmetrized gradient product. Variation of the volume density contributes g_munu L. These operations yield A5. No Einstein tensor is used to define this source.

The separate interaction stress is consequently

    T_mix,munu = gamma b_a [u_mu v_a,nu + u_nu v_a,mu
                            - g_munu (u·v_a)].                  (A6)

It must be included somewhere in the complete source accounting if the interaction is present. Merely adding the uncoupled phase and chromatic stresses does not include A6.

The source's separately printed chromatic stress has `-g_munu L_chi`; the action convention gives `+g_munu L_chi`. This is the already-identified sign discrepancy, retained here rather than silently edited. Its resolution depends on which source expression is adopted as authoritative.

### 3.3 Phase equation

Define EL_tau as the variational residual: delta S = integral sqrt(-g) EL_tau delta tau plus the other field variations. EL is not an energy variable.

For A4,

    EL_tau = beta Box tau - zeta V'(tau)
             + gamma nabla_mu(b_a partial^mu chi_a).             (A7)

Proof. The derivative of L with respect to u_mu is `-beta u^mu - gamma b_a v_a^mu`. Integration by parts gives its negative divergence; the explicit potential derivative is `-zeta V'`. This is A7.

When G is constant, the last term expands to

    gamma G^{ab} [chi_b Box chi_a
                   + partial_mu chi_b partial^mu chi_a].        (A8)

The gradient-product term is present, and the interaction appears with the sign fixed by A4. It is not removable just by treating the phase potential with a different normalization.

### 3.4 Chromatic equations

For each component chi_c, let partial_c denote differentiation with respect to that field coordinate, not a spacetime derivative. Then

    EL_chi_c = nabla_mu(G^{cb} partial^mu chi_b
                        + gamma b_c partial^mu tau)
               - (partial_c G^{ab}) (v_a·v_b)/2
               - partial_c U
               - gamma (partial_c b_a) (u·v_a).                 (A9)

Proof. Vary the chromatic gradients in A4 and integrate by parts. Vary the explicit G(chi), b(chi) and U(chi) dependence. Their contributions are respectively the three terms following the divergence. This accounts for all chi variations in the displayed action.

For constant symmetric G, derivative terms in the interaction cancel in pairs, leaving

    EL_chi_c = G^{cb} Box chi_b - partial_c U
               + gamma b_c Box tau.                            (A10)

The cancellation does not justify discarding the phase-backreaction term. It follows from equality of the mixed derivatives of the quadratic field-space contraction.

### 3.5 General field-space formulation

Let phi^I=(tau,chi_1,...,chi_7). The entire kinetic part is

    L = -K_IJ(phi) g^{munu} partial_mu phi^I partial_nu phi^J/2
        -P(phi),

where

    K = [[beta, gamma b^T], [gamma b, G]],
    P = zeta V + U.                                            (A11)

K is an 8-by-8 field-space matrix, not an additional spacetime metric. The general residual is

    EL_I = nabla_mu(K_IJ partial^mu phi^J)
           -(partial_I K_JK) partial_mu phi^J partial^mu phi^K/2
           -partial_I P.                                      (A12)

The implementation uses A11–A12. Positivity of K, hyperbolicity, stability, global existence and empirical validity are not supplied by this algebra. They remain separate properties of a chosen physical model.

## 4. A direct action/equation discrepancy in the source's own sector

Set G=I_7, V=U=0, tau=0, chi_1=x and all other chi components to zero, on a prescribed Minkowski patch. Take gamma nonzero.

The printed phase equation A2 has both sides equal to zero:

    Box tau=0,   chi_a Box chi_a=0.

Its printed chromatic equations also vanish on this assignment because the chromatic second derivatives and phase gradient vanish.

The phase variation of the displayed action instead gives

    EL_tau = gamma partial_mu(chi_1 partial^mu chi_1)
            = gamma partial_x(x)
            = gamma != 0.                                     (A13)

This is an exact counterexample to identifying A2 with the Euler–Lagrange equations of A4. It specializes the source formulas; it is not an invented alternative gravitational dynamics. The field assignment is NOT claimed to solve the Einstein metric equation. It tests the identity of the two claimed matter-equation presentations on a fixed background.

An additional ER or other interaction term could in principle supply compensating variations. No such cancellation is established without its action. Therefore the narrow conclusion is: **the printed phase–chromatic equations do not follow from the printed phase–chromatic action by themselves**. The original theory is not declared disproved.

The code also checks a complementary assignment, tau=t^2 and constant nonzero chi_1=c. The action gives EL_chi_1=-2 gamma c, while the printed chromatic equation gives zero. This isolates the missing phase-backreaction term.

## 5. Conservation check for the action-derived source

For A11, the stress tensor and residuals satisfy the off-shell identity

    nabla^mu T_munu = sum_I EL_I partial_nu phi^I.               (A14)

Proof. Differentiate `K_IJ partial_mu phi^I partial_nu phi^J + g_munu L`. The derivative of K produces the field-space derivative terms of A12. The two terms containing second derivatives of a scalar in different orders cancel because the connection is torsion-free and K is symmetric. The remaining terms are precisely A12 contracted with partial_nu phi^I.

Thus all scalar equations imply conservation of this sector's stress on a prescribed metric. Conservation alone does not imply every scalar equation; the gradients may fail to distinguish all residuals.

The code independently computes the coordinate Christoffel symbols and divergence of T. It verifies A14 for a nonlinear field-space metric G(chi)=1+chi^2 and for a curved expanding background. The source is never inferred by solving Einstein's equation for T. These tests check the displayed action, not the unspecified ER source.

## 6. The native metric differential is not the fixed-context inverse

For fixed alpha, lambda and background, differentiating M1 along a native variation gives

    delta g = alpha[d(delta tau)⊗d tau + d tau⊗d(delta tau)]
              +delta g_chi
              +lambda Xi(delta W)Xi^T
              +lambda(delta Xi)W Xi^T
              +lambda Xi W(delta Xi)^T.                        (M2)

If the context itself varies, its extra background or coupling variations must also be retained. The last two terms vanish only when the native covectors are genuinely fixed under the variation in question. A missing law for Xi cannot be replaced by setting its variation to zero without saying so.

The previous four-channel inverse is correct for its declared fixed context. It does not calculate the rank of M2 for a native construction in which Xi depends on W or other unknown fields.

An exact example makes the distinction visible. For r>0, let

    W(r)=diag(r^2,1,1,1),
    Xi(r)=diag(1/r,1,1,1).

Then Xi W Xi^T=I for every r. Xi is invertible and W is entrywise nonnegative, yet the complete metric derivative in the r direction is zero. The partial expression `Xi (dW/dr) Xi^T` is nonzero and is canceled by the two covector-variation terms. A fixed-Xi inversion cannot recover r from this metric. It can recover r only if the additional context Xi is retained or otherwise determined.

This is an algebraic metric-realization family, not a demonstrated collision among full native physical solutions.

### 6.1 The ambiguity can affect the source's graph operator

The source also supplies

    (L_ER f)_i = sum_j W_ij(f_i-f_j),

and a helicon recurrence involving this operator [S10]. Therefore arbitrary changes of W cannot be declared harmless representations without checking those other native constructions.

Take

    W1 = I4 + Ones4,
    D = diag(2,1,1,1),
    W2 = D^(-1) W1 D^(-1),
    Xi1=I4,   Xi2=D.                                          (M3)

Explicitly,

    W1 = [[2,1,1,1], [1,2,1,1], [1,1,2,1], [1,1,1,2]],
    W2 = [[1/2,1/2,1/2,1/2], [1/2,2,1,1],
          [1/2,1,2,1], [1/2,1,1,2]].

Both are symmetric and strictly entrywise positive. They satisfy

    Xi1 W1 Xi1^T = Xi2 W2 Xi2^T = W1.                          (M4)

With lambda=1/10 and the same Lorentzian background g0=eta-W1/10, both give g=eta when the phase and chromatic contributions in this algebraic comparison vanish.

However,

    spectrum(L_ER[W1]) = {0,4,4,4},
    spectrum(L_ER[W2]) = {0,2,7/2,7/2}.                        (M5)

The two graph operators are not related by a site permutation or any similarity transformation, since their spectra differ. For the same fixed c_A they give different native recurrence spectra. Thus the covector/weight factorization freedom is not automatically a gauge symmetry of all supplied native formulas.

The reference-state condition need not be the source of this ambiguity: a separate white-state input W=I, Xi_ref=I+(sqrt(5)-1)Ones4/4 gives the same calibrated eta with this background. This verifies algebraic compatibility with the displayed white condition, not a native law selecting the covectors at each state.

The limitations are precise: M3–M5 are valid inputs and outputs of the recovered metric and graph formulas. They are NOT certified complete native solution histories. Other constraints, stress readouts, or a specified Xi-selection law might exclude or distinguish them. The result explains why that law matters physically; it does not prove that all complete GR histories necessarily forget a native distinction.

## 7. The ER action contributes to the variational equations independently

The metric expression alone is not an action-equivalence theorem.

Suppose the full specified action has the form

    S[g,phi,W] = S_EH[g] + S_src[g,phi,W].

Let g=h(W,phi) be the native metric construction. Its substituted action is

    S_hat[W,phi] = S[h(W,phi),phi,W].                           (V1)

Let V_g denote the variational derivative density with respect to the covariant metric, holding W and phi fixed. Let V_W,explicit denote the full functional derivative with respect to W at fixed g and phi, including any derivatives of W in S_ER. With fixed Xi and g_chi independent of W, the local resolved-field chain rule is

    V_W,native = lambda Xi^T V_g Xi + V_W,explicit.             (V2)

The matrix identity behind this formula is

    <V_g, lambda Xi(delta W)Xi^T>
       = <lambda Xi^T V_g Xi, delta W>,

with the symmetric Frobenius pairing. Compactly supported variations justify any integrations by parts.

If Xi or g_chi depends on W, their linearized operators add the corresponding formal-adjoint terms from M2. They are not optional corrections.

Therefore `V_W,native=0` does not imply `V_g=0` merely because Xi is invertible. The explicit ER-action derivative may cancel a nonzero metric residual. Removing it changes the equations unless another proved constraint makes it vanish.

A one-variable example verifies the logical point, not gravitational physics: S_GR(g)=g^2/2, g=w, and S_extra(w)=-a w. The substituted action is stationary at w=a, while the original S_GR is stationary at g=0. The variable map is invertible; the difference is that the action is not merely S_GR rewritten. Including S_extra on the target gives the correct reexpressed theory, but changes which target action is being compared.

### 7.1 Constant graphs are not independent metric fields

For one constant graph W, the variation is a finite parameter variation, not an arbitrary local delta W(x). Then the appropriate relation is an integrated equation,

    partial S_hat / partial W_ij
       = integral [lambda Xi^T V_g Xi]_ij d^4x
         + partial S_explicit / partial W_ij.                 (V3)

Vanishing of finitely many integrals does not force every local Einstein residual to vanish. The elementary function r(u)=u-1/2 integrates to zero on [0,1] but is not pointwise zero. This illustrates the variation-space distinction; it is not asserted to be an Einstein residual of an actual native solution.

A resolved local field W(x) might supply the required arbitrary variations. The source retains the coarse-graining/type map as open. It cannot be silently substituted for the finite graph.

### 7.2 What a valid field-redefinition theorem would establish

For a fully specified action and an actual regular, invertible field map between the matched admissible spaces, one can prove equality of stationary solutions by the variational chain rule and a surjective map of allowed variations. Boundary terms and all retained matter fields must be matched. The existing restricted translator provides some of this algebra, not the missing hypotheses of the complete native theory.

Regularity is not a dispensable technicality. The literature on derivative-dependent field transformations distinguishes regular equivalence from transformations with singular branches or altered dynamics. No theorem about an invertible field redefinition supplies an unspecified native S_ER, Xi, or g_chi. See the reference notes below.

## 8. The complete source closure is not determined by the recovered interface

The genuinely new derivation in this run is A5–A14, together with the explicit native-factorization and variational checks M2–M5 and V1–V3. These complete a source-consistency calculation. They do not manufacture a native theory.

There are two independently important boundaries:

1. **The source action and its listed coupled equations are not yet one reconciled dynamical specification.** A2 is not the variation of A4 alone. Treating A4 as authoritative produces the equations derived here; choosing the printed equations instead requires a compatible action or an explicitly nonvariational specification. A compensating S_ER contribution would need to be supplied and checked.
2. **The metric/source realization is not specified by M1 alone.** The actual Xi-selection rule, g_chi functional, complete ER source, and admissible variations are still needed to determine the forward map and its physical inverse. The exact source sections explicitly preserve those open obligations.

A new realization could choose functions and an action to make the missing pieces definite. That would be a proposed extension. It must be labeled and tested against all upstream constraints; it is not a recovery of the original law merely because it uses the same names.

## 9. What is and is not delivered

Delivered:

- exact original evidence for the action, coupling, open-definition and graph-operator statements;
- the complete real phase–chromatic action variation with explicit potential normalization;
- its stress tensor, interaction stress and off-shell conservation identity;
- an executable evaluator for that stated sector on a supplied metric;
- exact tests of source discrepancies and ER-factorization ambiguities;
- the full metric linearization and explicit ER-action chain-rule contribution;
- preservation of the prior ER attachment ZIP without modifications.

Not delivered or asserted:

- a source-derived selector for Xi or g_chi;
- an invented S_ER or cancellation of its variations;
- a complete source-grounded native metric-and-source evaluator;
- a physical identification of all states with the same metric;
- a universal native lift of arbitrary GR solutions;
- a completed total native Genesis–GR equivalence theorem.

The requested endpoint therefore remains unestablished. This is a determination about the present construction and inspected specification, not a statement that the research goal is impossible or that the original full theory has been disproved.

## 10. Execution and reproducibility

Run:

    python code/checks.py

The test suite uses Python and SymPy 1.14.0. It contains 15 named checks. All passed in this run. Passing includes correctly detecting the deliberately tested mismatches; it does not mean those source equations were validated as equivalent.

The tests cover: two mixed-equation discrepancies; stress variation; two independent divergence checks; potential normalization; the chromatic stress sign; seven-component construction; metric-factorization ambiguity; graph spectra; reference calibration; complete versus partial metric differentiation; the explicit-action term; the matrix adjoint; and global versus local variations.

`results/CHECK_RESULTS.json` supplies the detailed scope of every check. `verify.py` verifies the artifact manifest; file integrity is not mathematical validation.

## Reference notes

**Primary project evidence:** the exact original API passages in `evidence/API43_ACTION_SOURCE.md`, and the byte-identical prior checkpoint. These determine the source-specific claims. No external physics model has been substituted.

**Atlas:** the supplied Atlas of Becoming report, Appendix A.2–A.3, distinguishes recovery on attainable evidence from existence of every target realization. The metric ambiguity here is a direct test using the recovered ER formula, not a new proof that every native physical history is invisible.

**External mathematical background only:**

- David Tong, General Relativity, Section 4, especially metric stress variation and scalar-field dynamics. `https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S4.html`
- K. Takahashi, H. Motohashi, T. Suyama, T. Kobayashi, General invertible transformation and physical degrees of freedom, Physical Review D 95, 084053 (2017). `https://arxiv.org/abs/1702.01849`
- P. Jirousek, K. Shimada, A. Vikman, M. Yamaguchi, New dynamical degrees of freedom from invertible transformations, JHEP 07 (2023) 154. `https://link.springer.com/article/10.1007/JHEP07(2023)154`

These sources are not invoked to determine the missing native functions. Our displayed calculations and hypotheses remain explicit, and no blanket inference from set-theoretic invertibility to physical equivalence is used.
