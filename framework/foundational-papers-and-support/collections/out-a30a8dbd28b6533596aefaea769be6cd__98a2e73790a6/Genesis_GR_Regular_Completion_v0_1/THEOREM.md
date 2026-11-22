# GRC-1: a regular positive-pair Genesis–GR completion

**Version:** 0.1, 31 October 2026  
**Classification:** New proposed classical representation model, developed under the user's express permission to go beyond the inherited specification.  
**Mathematical result:** An explicit, regular, two-sided correspondence with smooth metric general relativity coupled to the SAME specified matter theory.  
**Not asserted:** Equivalence of the unchanged historical MK43/Genesis microscopic model, emergence of spacetime from a pre-spacetime substrate, quantum equivalence, empirical validation, or priority for a novel general theorem.

## 1. The change of research question

The previous work recovered a nonnegative-adjacency metric expression, but its full physical inverse depended on unspecified covectors, a chromatic metric term, an independent ER action, and admissibility rules. It also found source action/equation variants that cannot be silently treated as identical. Repeating an existence condition does not complete those definitions.

The user has now authorized work outside the original domain and specification. This note takes that permission literally: it defines a NEW completion whose content and departures are explicit, then proves its equivalence. It does not pretend that the new definitions were found in the old files.

The aim is a working representation of GR, not an independent deduction that the old native microscopic theory must obey GR. The proposed model intentionally has the same classical physical content as the target. Its positive relational variables are a regular, fully reconstructible representation of that content. This is analogous in purpose, though not identical in mathematics, to established alternative formulations of GR. Rosenstock, Barrett, and Weatherall establish a separate categorical equivalence for Einstein algebras [R1]; their theorem does not establish anything about the historical Genesis variables.

## 2. Source inheritance and explicit departures

The inherited API supplies the expression

    g_ER = lambda Xi W Xi^T,
    W = W^T, W_ij >= 0.

Entrywise nonnegativity is NOT positive semidefiniteness. A symmetric adjacency matrix with nonnegative entries can have negative eigenvalues.

The new branch retains the algebraic form and nonnegative weights, but changes their interpretation and closes their representation:

* W(x) is a smooth, local, eight-channel relational encoding field. It is not asserted to be the old single finite graph of microscopic sites.
* The columns of Xi are the signed local cotangent basis (dx^0,...,dx^3,-dx^0,...,-dx^3). Eight is a channel count, not a number of spacetime dimensions.
* W is constrained to a canonical positive-pair form. The constraints remove encoding ambiguities exactly, not by declaring unknown old physical distinctions to be gauge.
* This encoding describes the TOTAL metric. The old separate background/phase/chromatic/ER decomposition is not imposed as an additional physical constraint.
* Dynamics come from the explicit action below. There is no independently appended ER action or old graph-wave recurrence. Adding such an action generally changes the target theory.
* A flat reference is encoded by W(eta). It is not generally W=I. The historical white-state identification is not derived or retained as an extra condition.
* Historical records of derivations remain in the archive. No claim is made that the old native History, chirality, or Bandwidth variables are all physically redundant. They are not extra unspecified physical variables of this new model.

These are substantial modeling choices, not notation corrections. An extension of the older theory must later demonstrate compatibility; the equivalence proved here does not supply that demonstration.

## 3. Domain and units

Fix a smooth four-dimensional manifold M and the same orientation, time-orientation, matter bundles, constants, and boundary conventions on both sides. Use smooth nondegenerate metrics of signature (-,+,+,+). No globally preferred frame, global coordinate chart, or simple-connectivity hypothesis is needed. An atlas is used and its transition maps are retained.

The construction applies to every smooth metric in this class, including strong-field metrics on their regular regions. A singular coordinate chart is replaced by another chart; a genuinely degenerate metric or missing singular point is not declared covered by the nondegenerate theorem. The argument does not assert existence of a solution for every conceivable boundary datum.

Use c=1 and fixed normalized coordinate units. Two positive constants sigma and lambda normalize the encoding; they are not new measurable couplings. For different coordinate units, component normalization belongs to the encoding convention. The nonlinear gluing below, rather than a false tensor law for the encoding variables, supplies covariance.

Every exponential, hyperbolic sine, inverse hyperbolic sine, and square root applied to a component array below is ELEMENTWISE. None is a spectral matrix function.

## 4. The native variables and metric construction

On a coordinate chart introduce ten independent real smooth fields Z_mu,nu=Z_nu,mu. Define

    P_mu,nu = sigma exp(Z_mu,nu)/(4 lambda),
    Q_mu,nu = sigma exp(-Z_mu,nu)/(4 lambda),

and the symmetric eight-channel weight array

    W = [ P  Q ]
        [ Q  P ].

All entries of W are strictly positive. Let Xi=[I_4 | -I_4] in the chosen cotangent frame. Then

    h(Z) = lambda Xi W Xi^T
         = 2 lambda(P-Q)
         = sigma sinh_ewise(Z).                              (1)

Admit precisely those Z for which h(Z) has Lorentzian signature. This is an open subset of the ten-dimensional real symmetric component space. The entries Z are the independent field variables: P and Q are NOT varied independently.

The canonical constraints on the pair are

    P=P^T, Q=Q^T, P_mu,nu>0, Q_mu,nu>0,
    P_mu,nu Q_mu,nu = sigma^2/(16 lambda^2).                   (2)

These equations reduce the twenty independent pair entries to ten. The other W blocks are copies, not new degrees of freedom.

## 5. Explicit inverse and full metric coverage

Given ANY real symmetric metric array g, set, component by component,

    r_mu,nu = sqrt(g_mu,nu^2 + sigma^2),
    P_mu,nu = (r_mu,nu + g_mu,nu)/(4 lambda),
    Q_mu,nu = (r_mu,nu - g_mu,nu)/(4 lambda),                 (3)

or equivalently

    Z_mu,nu = asinh(g_mu,nu/sigma).                           (4)

Because sigma>0, r_mu,nu>|g_mu,nu|. Both weights are strictly positive for every finite real component; no sign of g is excluded. Their difference gives

    2 lambda(P-Q)=g,

and their product gives (2).

Conversely, start with positive P,Q satisfying (2), and put d=2 lambda(P-Q). Then

    [2 lambda(P+Q)]^2 = d^2 + sigma^2.

The left square root is positive, so r=2 lambda(P+Q). Substituting into (3) recovers exactly P and Q. Thus the two-sided inverse holds for every canonical pair, not only for pairs produced in the tests.

This proves a smooth bijection between the canonical pairs and all real symmetric metric arrays. Restricting both sides to Lorentzian signature preserves the bijection. There is no residual weight/covector-factorization ambiguity: Xi is prescribed representation context and normalization (2) fixes the positive-pair redundancy.

The same statement in the ten independent coordinates is the global component-space diffeomorphism g=sigma sinh(Z), Z=asinh(g/sigma).

## 6. Regularity, not just set-theoretic invertibility

For the independent symmetric index I=(mu,nu), mu<=nu,

    d g_I / d Z_J = sigma cosh(Z_I) delta_IJ.                 (5)

Every diagonal factor is strictly positive; it is at least sigma. The Jacobian never vanishes at a finite field value. Its inverse is

    delta Z_I = delta g_I / sqrt(sigma^2+g_I^2).              (6)

Thus every admissible compactly supported infinitesimal metric variation has a unique compactly supported Z variation. This is the condition the earlier constant-network parametrization did not supply. Here Z consists of independent local fields, not finitely many global parameters.

The Lorentzian condition is open, so sufficiently small variations around a nondegenerate smooth metric preserve the signature locally. Compact support controls the region being varied. This proof is the simple derivative-free case of regular field-redefinition equivalence; it does not rely on a blanket assertion that every invertible transformation preserves dynamics. The literature contains singular/derivative-dependent qualifications [R2,R3].

## 7. Global gluing and diffeomorphisms

Let J=dx/dy on overlapping coordinate charts. A metric obeys

    g_y = J^T g_x J,

with both sides evaluated at the same point. Define the native transition by

    Z_y = asinh_ewise( J^T [sigma sinh_ewise(Z_x)] J / sigma ). (7)

Equivalently, decode W_x, apply the metric transition, and encode the result by (3). These transitions are generally nonlinear. Z and W are not assigned a false linear tensor-transformation law.

Cocycle proof: if the next Jacobian is K, the second decoded transition gives

    K^T(J^T g J)K = (JK)^T g(JK).

Encoding is single-valued, so two successive transitions equal the transition associated with JK. Identity and inverse chart changes work the same way. Therefore compatible native local fields glue precisely when the corresponding metric fields glue. No global coframe assumption has entered.

The same definition transports active diffeomorphisms. Before gauge quotient, the configuration maps are injective. On gauge classes, a target symmetry phi induces E o phi o D in the new variables, where E is encoding and D is decoding. This is not an arbitrary identification of invisible states: it is the same invertible change of variables applied to an already defined gauge action. Large transformations and boundary restrictions are inherited, not silently discarded.

## 8. A completely specified action

First take vacuum or cosmological-constant GR. Define

    S_GRC[Z] = (1/(2 kappa)) int_M sqrt(-det h(Z))
                         [ R(h(Z))-2 Lambda ] d^4x
                 + B_GR[h(Z)].                              (8)

B_GR is the same selected boundary action as in the target, when boundaries are used. The simplest proof uses compactly supported variations in the interior, so no unstated boundary cancellation is required. For a full boundary problem, the action, boundary conditions, and allowed boundary variations are all pulled back together.

This is a FULL definition of the new branch's gravitational dynamics. It is Einstein-Hilbert gravity expressed in regular positive-pair variables, not a claim to derive Einstein-Hilbert gravity from the old microscopic graph. There is no missing independent S_ER. An extra native action term must either have its own matching target term or undergo a new equivalence analysis.

The connection is the Levi-Civita connection of h(Z). In coordinates it can be evaluated directly from the native fields:

    Gamma^rho_mu,nu = (1/2) h^rho,ell sigma [
       cosh(Z_ell,nu) partial_mu Z_ell,nu
      +cosh(Z_ell,mu) partial_nu Z_ell,mu
      -cosh(Z_mu,nu) partial_ell Z_mu,nu ].                    (9)

The repeated ell is summed. The hyperbolic factors are componentwise. Curvature is the full derivative-plus-quadratic-connection expression. These formulas require no separate uncomputed native connection selector in THIS new model.

For any fully specified matter action S_m[g,psi], one can set

    S_GRC[Z,psi] = S_GR[h(Z),psi].                            (10)

The fields, bundles, sources, potentials and boundary data are retained on both sides. This is a theorem schema over specified target models, not a claim that the stress tensor determines every matter field. The next section gives an explicit matter completion so the result need not stop at an unspecified S_m.

## 9. A consistent phase–chromatic completion

Use seven real fields chi_a and a circle-valued phase tau. Fix beta>0 and a real representation parameter gamma. Define the target phase by

    Theta = tau + (gamma/(2 beta)) sum_a chi_a^2   mod 2 pi.  (11)

The reverse is

    tau = Theta - (gamma/(2 beta)) sum_a chi_a^2   mod 2 pi.  (12)

This is a smooth bijection of S^1 x R^7. It does not require a globally chosen real lift of either phase; adding the same single-valued real function to a circle-valued field is globally defined. Local lifts are used for calculations, and global circle data remain part of the field.

The explicit target matter Lagrangian is

    L_m = -beta/2 (dTheta)^2 -1/2 sum_a (dchi_a)^2.            (13)

No potential is needed for this base model. Prescribed smooth periodic V(Theta) and a prescribed U(chi) may be added equally on both sides, but are not used in the executed exact solution.

In native fields the same action is

    L_m,G = -beta/2 [d tau + (gamma/beta) sum_a chi_a dchi_a]^2
            -1/2 sum_a (dchi_a)^2.                           (14)

Expanding gives

    -beta/2 (d tau)^2 - gamma sum_a chi_a d tau . dchi_a
    -1/2 sum_a(dchi_a)^2
    -gamma^2/(2 beta) [sum_a chi_a dchi_a]^2.                  (15)

The middle interaction resembles the inherited constant-field-metric interaction. The LAST term is a new, explicitly added completion, and choosing the chromatic metric to be the identity is also a branch choice. It is not falsely attributed to the archive. This replaces the inconsistent mixed-equation specification with ONE action and its actual Euler–Lagrange equations.

The field-space kinetic form is

    K = [ beta             gamma chi^T              ]
        [ gamma chi        I + gamma^2 chi chi^T/beta ].

For any tangent vector (v0,v),

    (v0,v)^T K (v0,v) = beta [v0+(gamma/beta)chi.v]^2 + |v|^2.

It is positive definite for beta>0. Its determinant is beta: the field map has unit triangular Jacobian and K=J^T diag(beta,I_7)J. There are no hidden extra scalar degrees of freedom and no artificial negative kinetic direction introduced by this mixing. Gamma is a coordinate parameter of this completed scalar model, not an extra physical coupling inherited without change from the old model.

The stress tensor is derived from (13), not from the Einstein tensor:

    T_mu,nu = beta partial_mu Theta partial_nu Theta
             +sum_a partial_mu chi_a partial_nu chi_a + g_mu,nu L_m.  (16)

Equation (14) gives the same tensor after substitution. The full scalar fields, not merely T, are carried by the target representation.

## 10. Exact equivalence of the field equations

Let the target variation, written using independent symmetric metric components, be

    delta S_GR = int [sum_I E_g^I delta g_I
                     + E_Theta delta Theta
                     + sum_a E_chi,a delta chi_a] d^4x
                   + matched boundary terms.

E denotes an Euler–Lagrange density here, not energy. Substitute (1) and (11). The native equations are exactly

    E_Z^I = sigma cosh(Z_I) E_g^I,
    E_tau = E_Theta,
    E_chi,a(native) = E_chi,a(target)
                      +(gamma/beta)chi_a E_Theta.             (17)

The metric scaling factors are nonzero and the scalar transformation is triangular with diagonal entries one. Therefore

    all native Euler–Lagrange residuals vanish
       IFF
    all target Euler–Lagrange residuals vanish.                (18)

No inverse differential operator, unsupplied ER variation, or boundary assumption is hidden in this step. The map is derivative-free even though the action contains derivatives of its fields.

For the target in (8),(13), the equations are

    G_mu,nu + Lambda g_mu,nu = kappa T_mu,nu,
    beta Box_g Theta = 0,
    Box_g chi_a = 0.

The corresponding native phase/chromatic equations are their explicit triangular combination (17), not the incompatible printed equations of the older source. The gravitational equations expressed in Z may look nonlinear, but (17) proves they have exactly the same zeros.

## 11. Completion theorem and proof

**Theorem (new GRC-1 model).** Fix the domain and boundary prescription in section 3, positive sigma, lambda and beta, finite gamma, kappa and Lambda, and the massless phase/seven-scalar action above (or another fully specified retained matter theory with a specified regular field map). Then the maps

    rho(Z,tau,chi) = (sigma sinh_ewise Z,
                     tau+gamma |chi|^2/(2 beta), chi),

    L(g,Theta,chi) = (asinh_ewise(g/sigma),
                     Theta-gamma |chi|^2/(2 beta), chi)        (19)

are globally defined inverse maps of compatible smooth field configurations, on the Lorentzian domain, and induce inverse maps of classical solution spaces with matched boundaries. They respect the corresponding diffeomorphism and matter gauge actions. Every smooth target solution in this class is represented. Both round trips hold before the quotient; the induced physical solution-class maps are inverse as well.

**Proof.** Componentwise sinh and asinh are smooth real inverses; (11),(12) are inverse maps of the scalar-field target space. Sections 5–7 prove strict positivity, canonical uniqueness, global gluing, and all-metric coverage. Section 6 and the triangular matter Jacobian show that allowed compactly supported variations correspond bijectively. Equation (17) then proves both directions of stationarity. The matched boundary prescription gives the same statement for the selected boundary problem. Conjugating the already-specified symmetry actions by an invertible field transformation preserves group composition, admissibility and orbits. Thus (19) descends to the corresponding physical classes without a new declaration that old hidden degrees of freedom are gauge. QED.

This is a complete proof for the DEFINED new classical branch. It is a constructive reformulation theorem; it is not an inference about any unspecified older action or microscopic state space. Independent checking of the proof and implementation remains appropriate.

## 12. Preservation of calculations and dynamics

The smooth decode/encode maps identify the same metric and specified matter fields. Equation (9) is exactly the chain-rule expression of the ordinary connection. Substitution into the connection commutator preserves curvature; contractions preserve Ricci, scalar and Einstein curvature. Covariant differentiation extends to tensor products by its defining product rule.

For any finite expression built from these typed operations, translate-after-evaluate equals evaluate-after-translate by structural induction. Inverse metric, field equations and partially defined operations use matching domains. For functions involving limits or integrations, the same smoothness, convergence, volume and boundary conditions must be used; finite algebraic-expression closure alone is not a universal theorem about arbitrary analytic procedures.

Parallel transport and geodesics use exactly the same reconstructed connection, so their differential equations, parameters, initial data and solutions agree on their common existence domain. Gauge-fixed Cauchy evolution is similarly conjugate wherever it is defined for the specified target. This does not prove a new global well-posedness theorem for GR.

Because the actions and boundary prescriptions are related by an ordinary point-field diffeomorphism, the target variational and covariant phase-space structures can be pulled back without changing their values. Charges and observables must be carried with their target boundary definitions, not recomputed under a different boundary action. No quantum measure, operator-ordering, or unitary-equivalence claim is made.

The representation parameters sigma, lambda and gamma do not introduce independent measurable observables. In particular a raw graph Laplacian spectrum of the encoded W is not added as an extra coordinate-independent physical observable. Doing that would require a new model and could destroy the stated GR equivalence.

## 13. An exact curved, sourced solution

Set kappa=beta=1, Lambda=0 and gamma=2. Let t>0 and

    ds^2 = -dt^2 + t^(2/3)(dx^2+dy^2+dz^2),
    Theta = log(t)/sqrt(3),
    chi_1 = log(t)/sqrt(3),   chi_2=...=chi_7=0.

The metric is Lorentzian and smooth for t>0. The scalar fields solve their independent wave equations. Their action-derived source has

    rho = T_00 = 1/(3 t^2),
    T_ii = t^(2/3)/(3 t^2).

Direct curvature evaluation gives G=T, nonzero scalar curvature -2/(3t^2), and covariant source conservation. The point t=0 is outside the declared domain.

The native configuration is EXPLICIT:

    Z_00 = -asinh(1),
    Z_ii = asinh(t^(2/3)),
    Z_mu,nu=0 for mu!=nu,
    tau = log(t)/sqrt(3) - [log(t)]^2/3,

with W generated from Z by section 4. The mixed native scalar action is varied independently in the homogeneous reduction and gives zero field residuals on this configuration. Equations (17) supply the full general proof; the check is not used to infer the theorem from one example.

Both metric and scalar round trips recover every declared native variable. The source is not picked by dividing G by kappa, and no unspecified total flux is set to zero to obtain the solution. This differs from the previous constructed endpoint fixture: it solves a completely specified action, but that action belongs to THIS new branch.

## 14. Executed verification and scope

Run `python code/checks.py`. The checked-in result records 43 named checks. They include symbolic scalar and ten-component encoding identities; positive-pair normalization; ER factorization; the nonvanishing Jacobian; a 100-metric numerical family (seed 43); coordinate transitions and cocycles; invalid input controls; the seven-component kinetic completion; and the full sourced curved example.

A first test run did not normalize an exponential expression into a hyperbolic one automatically. Rewriting hyperbolic functions into exponentials in the checker resolved that representational simplification failure. The mathematical formula did not change. The execution history is retained in results/TEST_HISTORY.json.

Tests are not a formal proof assistant, independent peer review, or empirical validation. The general theorem rests on the explicit inverse, regularity and variational proofs above. Numeric coverage tests are finite examples; universal coverage follows from formula (3). Code uses SymPy for local calculations and NumPy for the finite random fixture family. The previously written translator is included unchanged and used only for its coordinate geometric routines; its old unresolved-attachment function is NOT the entry point of this new model.

## 15. Exactly what has been solved

**Solved for this new model:** a positive symmetric relational encoding of every smooth Lorentzian metric, exact reconstruction, globally compatible coordinate changes, a nonsingular variation map, a fully specified classical action, consistent retained scalar matter, equivalence of all its classical equations and solution classes, and agreement of the represented tensor calculations.

**Not solved or claimed:** physical equivalence of the unchanged old microscopic Genesis framework; derivation of the signed covector channels from the old ER substrate; compatibility with every old independent recurrence or white-state normalization; quantum gravity; new observable predictions; or independent empirical confirmation.

This is therefore a definite constructive alternative rather than another audit of absent definitions. Its price is explicit: it is a NEW regular GR representation branch. A claim about the old entire model would require a separate faithful, dynamics-preserving embedding into this branch or an equivalent construction, and could not be asserted merely by reusing the word Genesis.

## References and source distinction

[S1] API43_EXACT_EXCERPTS.md, copied from the previous checkpoint: the nonnegative ER metric expression, source declarations and recorded open questions. Its hashes are in PROVENANCE.json.

[S2] PRIOR_CLOSURE_ASSESSMENT.md, previous derivation copied unchanged: source-action mismatch, factorization ambiguity, and variational limitations. This work is not a revision of its historical findings.

[S3] The supplied *Atlas of Becoming*, checkpoint report dated 31 October 2026: chapter 11.2 says a proof translated into a new theory version is a new artifact; Appendix A.3 restricts inverse recovery to evidence that distinguishes the selected classes. Those principles are observed here; no earlier theorem is silently promoted to this new model.

[R1] S. Rosenstock, T. W. Barrett, J. O. Weatherall, *On Einstein Algebras and Relativistic Spacetimes*, arXiv:1506.00124. A separate example of rigorous equivalence between formulations, not a proof of GRC-1.

[R2] K. Takahashi, H. Motohashi, T. Suyama, T. Kobayashi, *General invertible transformation and physical degrees of freedom*, arXiv:1702.01849v2. Background on field transformations and Euler–Lagrange equivalence.

[R3] P. Jirousek, K. Shimada, A. Vikman, M. Yamaguchi, *New Dynamical Degrees of Freedom from Invertible Transformations*, arXiv:2208.05951v3. Warns against treating bare invertibility as sufficient for dynamics. GRC-1 explicitly has an everywhere nonzero point-transformation Jacobian.

[R4] D. Tong, *General Relativity*, section 4, *The Einstein Equations*, Cambridge lecture notes. Conventional Einstein–Hilbert and matter-variation definitions used in specifying the target. These standard facts are not presented as new discoveries.

Web access: 31 October 2026. The proof in this document is supplied explicitly and does not infer its conclusion merely from the titles of the references.
