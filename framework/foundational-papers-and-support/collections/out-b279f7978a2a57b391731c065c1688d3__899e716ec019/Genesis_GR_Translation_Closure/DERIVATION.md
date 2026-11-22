# Genesis–GR: operation-preserving translation closure

Date: 31 October 2026

## Determination

**Established here:** an operation-preserving, two-sided translator for evaluated smooth Genesis–GR endpoint fields, using the connection, curvature, contractions, flux source and divergence prescribed by the supplied module. The theorem includes nonlinear expressions and admissibility within a stated smooth representation domain. A local symbolic implementation computes on both sides independently.

**Not established here:** an evaluator or inverse for the original native attachment

    q ↦ (Q_R[q], selected transport[q], witnessed source[q], retained matter[q]).

Accordingly this is a completed differential-calculus translation theorem and a restricted implementation, **not completion of the user's full source-grounded native realization objective**. It would be false to mark the whole requested endpoint solved. Neither an arbitrary new Q_R nor a new native dynamics is installed.

The distinction between evaluated endpoint data and an unevaluated native state is enforced in the implementation: `attach_raw_native_state` raises `UnresolvedNativeAttachment`. This is an explicit limitation, not a claim that the original theory is impossible.

## 1. Source attachment: what is actually supplied

The source evidence is copied byte-for-byte under `evidence/`; `SOURCE_MAP.json` gives archive paths and digests. The following are source facts, not conclusions from the standard GR references.

- **S03, point 2:** `𝔤_G(x;a,b)=Q_R[ℛ_x(a,b),B_x,H_x,χ_x]`, with the required readout `ρ_G(𝔤_G)=g`. This is a prescription for the metric functional and its target, not an evaluation algorithm in that displayed passage.
- **S03, point 3; S07:** a Transduction Connection selects an admitted lift. Finite lift selection is not automatically a differential connection. S07 explicitly forbids fabricating a connection instance from a convenient formula.
- **S05; S06, A3–A4:** in the smooth gravitational realization, the metric is nondegenerate Lorentzian and the gravitational connection is torsion-free and metric-compatible. S05's geometry formulas remain subordinate to the latest Q_R metric attachment, not a replacement by the old freely postulated metric branch.
- **S03, points 4,6–9,12:** composed path transport; curvature as a connection commutator; Ricci trace; scalar trace; Einstein tensor; covariant divergence.
- **S03, point 10; S09:** local source tensor is the refinement density of witnessed four-momentum transfer. Source density existence and symmetry are conditions, not deductions from finite additivity alone.
- **S06, A13:** readout is required to preserve typed tensor operations and contractions. This run supplies a concrete faithful smooth realization and a proof of its differential extension. It does not treat the requested master correspondence law as its own proof.
- **S02:** upstream MK Ultra objects are not redefined; this module is a mathematical representation attachment.

A bounded source scan examined 1,303 text files in the recovery archive's expanded-source and repository-evidence directories (27,837,099 bytes). It did not inspect binary databases or recursively re-audit every embedded archive. It found no evaluable native metric functional in the inspected matching passages. Case-insensitive `Q_R` hits also include a Resolution quotient and a stratum-graph quotient, which are not silently identified with the metric functional. `evidence/SOURCE_SCAN.json` records the scan and its limits. This is evidence of what this run located, **not a proof that no formula can exist elsewhere**.

## 2. Precisely stated representation domain

Let M be a smooth four-dimensional manifold, with the domain, orientation, boundary conventions, constants and matter content fixed. Work locally on charts and glue only by the actual compatible transition maps. No global frame or simple connectivity is assumed for the theorem.

Let V_G be the admitted real rank-four smooth native gravitational bundle. Require a specified smooth vector-bundle isomorphism

    a: V_G → TM.

This is the **faithful differential realization/anchor**, not an assertion that a coarse native Resolution quotient or the upstream Time-Shell map is globally invertible.

The scalar realization is the identified smooth function sheaf on M, in fixed units. Native vector fields act on those scalars by `(a u)f`; their admitted smooth bracket obeys

    a([u,v]_G)=[a u,a v].                                      (D1)

This differentiable anchoring is substantive. Rank four alone, faithful mass translation alone, or an object-level field label does not prove D1.

The inputs are:

1. An **evaluated** native metric k=𝔤_G, supplied by the actual Q_R on the state under study, smooth and Lorentzian.
2. The **selected** smooth connection C_G, which obeys the connection axioms relative to a, zero torsion, and metric compatibility with k.
3. An evaluated smooth symmetric flux source t_G; original native provenance is retained separately and not manufactured from the target Einstein tensor.
4. Every retained matter field, its bundle or internal gauge structure, constants, domain conditions and boundary data needed by the comparison. No attempt is made to reconstruct matter from its total stress tensor.

The theorem applies whenever these inputs and smooth-realization conditions have actually been supplied. It does not prove their existence for every original native state or every possible GR target.

## 3. Explicit two-way tensor translation

In a local frame, write

    a(e_a)=A^μ_a ∂_μ,       B=A⁻¹.

For a vector and covector, respectively,

    ρ(v_G)=A v_G,           ρ(α_G)=Bᵀ α_G.

For a tensor with r upper and s lower slots, apply A in each upper slot and Bᵀ in each lower slot. The reverse uses B in upper slots and Aᵀ in lower slots. These rules are the explicit maps ρ_(r,s) and L_(r,s).

In particular,

    g=Bᵀ k B,              k=Aᵀ g A,                         (T1)
    T^up=A t_G^up Aᵀ,      t_G^up=B T^up Bᵀ,                 (T2)
    T_down=Bᵀ t_G,down B,   t_G,down=Aᵀ T_down A.             (T3)

### Two-sided proof

Every upper-slot round trip contributes BA or AB, and every lower-slot round trip contributes AᵀBᵀ or BᵀAᵀ. Each is the identity. Therefore, for every supported tensor type,

    L_(r,s) ρ_(r,s)=id,       ρ_(r,s) L_(r,s)=id.             (T4)

This is exact on the admitted bundle sections, not an asymptotic identity. It preserves tensor addition, scalar multiplication, tensor product, slot permutations, evaluation pairing and contraction. For contraction, the paired A and B cancel on the contracted index. A nondegenerate inverse metric maps to the inverse metric by uniqueness of a matrix inverse.

The frame a and local coordinates are representation context. Recovering the same component array requires the same context; changing frames yields the correspondingly transformed representation. These choices are not hidden native physical variables reconstructed from a metric.

## 4. The key new connection proof uses the source's own restriction

One must not simply define all Genesis operations by conjugating a GR operation and call the resulting equality a verification of the source. Instead start with the source's **selected** native connection C_G satisfying its smooth GR restriction.

Define a connection D on TM by

    D_X Y = a(C_(a⁻¹X)(a⁻¹Y)).                              (C1)

Use (D1) and native zero torsion:

    D_XY − D_YX − [X,Y]
      = a(C_u v − C_v u − [u,v]_G)=0.

Use `g(X,Y)=k(a⁻¹X,a⁻¹Y)` and native metric compatibility:

    X g(Y,Z) = g(D_XY,Z)+g(Y,D_XZ).

Thus D is torsion-free and metric-compatible. Uniqueness of the Levi-Civita connection gives

    D=∇^g.

Consequently,

    a(C_u v)=∇_(a u)(a v).                                  (C2)

This is a derived intertwining law, not a separate assumption of operation equality. Its premises are the native smooth connection conditions and the differential anchor. The standard Levi-Civita fact is cited in R1; the application and proof are written here.

### Independent native coefficient formula

Write `D_a=A^μ_a ∂_μ` and `[e_a,e_b]_G=f^c_ab e_c`. Then the source restriction uniquely gives Koszul's identity:

    2 k_cd C^d_ab = D_a k_bc + D_b k_ca − D_c k_ab
                    − k_ad f^d_bc + k_bd f^d_ca + k_cd f^d_ab. (C3)

The implementation uses (C3) to calculate the native connection directly from the evaluated native metric and its anchored derivatives. Separately it computes the coordinate Christoffel formula from the translated g. Equality of those computations is tested; the native result is not copied from the coordinate calculation. When a selected connection is supplied, the program checks that it meets (C3), rather than silently replacing it.

This calculation does not implement the upstream finite lift selector. It verifies a selected connection once an admitted smooth realization exists.

### Explicit connection translations

Let C_a be the connection matrices for derivative along e_a. Convert the derivative index first:

    C_μ = B^a_μ C_a.

Then

    Γ_μ = A C_μ B − (∂_μ A) B,                              (C4)
    C_μ = B Γ_μ A + B(∂_μ A),
    C_a = A^μ_a C_μ.                                        (C5)

Equations (C4) and (C5) are two-sided inverses. The derivative-of-frame term is indispensable. Its removal is detected by a negative test.

## 5. All tensor derivatives now commute

The connection on covectors is characterized by the derivative of the evaluation pairing:

    (C_u α)(v) = (a u)(α(v)) − α(C_u v).

Since scalar action, vector differentiation and pairing commute with ρ, covector differentiation does too. The tensor connection is characterized by its Leibniz rule. Induction over tensor products and linear combinations therefore proves, for every smooth tensor S,

    ρ(C_u S) = ∇_(a u) ρ(S).                               (D2)

Equivalently, with the derivative treated as an additional covariant slot,

    ρ_(r,s+1)(D_G S)=∇ρ_(r,s)(S).                           (D3)

Repeated application proves the same for every finite order of covariant differentiation. It is not limited to a first derivative, a constant frame, linearized gravity or a particular metric.

### Non-coordinate frames

For connection matrices in an arbitrary anchored frame,

    R_G,ab = D_a C_b − D_b C_a + [C_a,C_b] − f^c_ab C_c.     (D4)

This is exactly the source commutator definition. Dropping its final term implicitly assumes the frame is coordinate. The curved moving-frame negative control detects that error.

## 6. Applying the theorem to the existing source operations

### Curvature

Apply a to the source formula

    R_G(u,v)w=C_u C_v w − C_v C_u w − C_[u,v]_G w.

Using (D1) and (C2) term by term gives

    a(R_G(u,v)w)=R^g(a u,a v)(a w).                          (R1)

This proves full nonlinear Riemann correspondence. Quadratic connection terms have not been dropped.

### Ricci, scalar and Einstein objects

Trace and contraction commute with tensor translation, so the source's actual definitions yield

    ρ(Ric_G)=Ric[g],
    ρ(Scal_G)=Scal[g],
    ρ(Ein_G)=Ein[g].                                        (R2)

With matched constant Λ and nonzero κ,

    ρ(Ein_G+Λ_G k−κ_G t_G,down)
         = Ein[g]+Λg−κT_down.                               (R3)

Faithfulness (T4) gives both implications for the vanishing residual. This is equivalence of the **represented field equations**, not a derivation of them from an independent unspecified native update rule.

### Source and directional flux

The source's `dP_G^a=t_G^{ab}dΣ_b` gives `V_G=t_G^up N_G` for independent conormal probes. Decode

    t_G^up=V_G N_G⁻¹.

Under translation, `N_GR=BᵀN_G`, `V_GR=A V_G`; hence

    T^up N_GR = A t_G^up Aᵀ Bᵀ N_G = A V_G = V_GR.         (S1)

Thus the flux law itself, not only a tensor named T, is preserved. Symmetry and index lowering are preserved too. The densities must actually exist. None of this turns a finite total into a pointwise density without the source's refinement hypotheses.

### Divergence and conservation

The source defines a covector

    (Div_G S)_b=k^{ac}(C_e_c S)_ab.

By (D3) and contraction,

    ρ(Div_G S)_ν=∇^μρ(S)_μν.                               (S2)

The displayed source readout `∇_μT^{μν}` has a raised free index. It is equivalent after raising the output with the metric; treating a covector and a vector as literally the same type would be wrong. The implementation compares covectors consistently. The original source is preserved unchanged, and this typing convention is recorded rather than silently edited into it.

Bianchi and source conservation translate in both directions. Constant Λ and κ are essential for the simple implication from the field equation to `Div T=0`; variable couplings require their derivative terms.

### Transport and holonomy

Along the same admitted path γ, (C2) maps native parallel sections to GR parallel sections with the same translated initial value. Uniqueness of the smooth linear transport ODE gives

    P_GR(γ)=A(γ(1)) P_G(γ) B(γ(0)).                         (P1)

The inverse is

    P_G(γ)=B(γ(1)) P_GR(γ) A(γ(0)).                         (P2)

The source's path composition is preserved since the intermediate A and B cancel. On loops this is conjugacy of holonomy. The theorem concerns paths admitted on both sides. A Bandwidth filter which excludes a GR path is not erased by the translator.

The source's finite defect `Def(...)` is not provided as a general numerical operation in these passages. It is not replaced by curvature or claimed to have an evaluated inverse. The small-loop curvature limit requires a stated oriented area/bivector and orientation convention consistent with the commutator; it is not an identity between an arbitrary finite loop and a curvature value.

### Geodesics

For a represented curve, `γdot=A u`. Differentiation plus (C4) gives

    γddot + Γ(γdot,γdot) = A(udot + C_μ γdot^μ u).           (P3)

Therefore the source's affine geodesic equation has exactly the corresponding GR solutions on the same domain, including null curves. The length extremum written in the source requires the usual non-null and parameterization qualifications; this proof uses the separately supplied affine-connection equation rather than claiming length variation resolves null geodesics.

### Other natural expressions

Lie derivative on tensor fields follows from derivative and bracket compatibility. Raising/lowering, Killing equations, geodesic deviation and invariant volume/integrals follow when their inputs, orientation, domains and boundary prescriptions are retained. Integration over an actual domain is not claimed from a finite number of sample values. The code implements the listed local tensor/derivative operations, not arbitrary global integration or PDE evolution.

## 7. Completion for a finitely generated expression language

Let L_G be the well-typed **finite** expression language generated by admitted scalar/tensor leaves, sums, scalar products, tensor products, permutations, contraction, nondegenerate metric inversion and covariant differentiation. Curvature is expanded by its source commutator, and the source's Ricci/scalar/Einstein/divergence expressions by their source definitions. Transport can be included with (P1) as a separate path operator on matching domains.

Take corresponding leaves in L_GR using the explicit ρ maps. The structural translation replaces each generator with its proved counterpart and retains types and declared domains.

### Expression theorem

For every expression e in that language and every admitted valuation v,

    e_G(v) is defined iff e_GR(ρv) is defined,               (E1)
    ρ(e_G(v)) = e_GR(ρv),                                  (E2)
    L(e_GR(ρv)) = e_G(v).                                  (E3)

Proof by structural induction:

1. Leaves satisfy the statement by the supplied correspondence and (T4).
2. For an operation node, the induction hypothesis maps all arguments. Its generator law maps the outputs. Its domain equivalence maps definedness as well.
3. Composition is a special case of the preceding step. Finite nesting terminates at the leaves.
4. Apply the inverse output map to (E2) for (E3).

Metric inverse requires a nonzero determinant. By (T1), `det k=(det A)^2 det g`, so it is defined on exactly the corresponding nondegenerate domain. Contraction requires matching dual slots on both sides. Smooth differentiability is preserved by the assumed smooth anchor. Other partial operations carry their own matched conditions. No arbitrary native partial operation is included simply because it has a name.

This closes the differential-expression proof on its stated language. Checking each possible compound expression separately is unnecessary. The source's actual operators C, R, Ric, Scal, Ein, Div enter through their defining formulas, not through a wholesale definition `C_G:=L C_GR ρ`.

Unbounded limits, nonlinear coarse Resolution quotients, finite path defects without a supplied evaluation, arbitrary native update rules, matter-generation operations and native Q_R are outside this expression grammar unless independently added with their own valid interpretation and domain proofs.

### Equation-system corollary

Let a system of represented equations be built from the admitted expressions, with corresponding matter fields and boundary conditions explicitly retained. By (E2), zero residuals map to zero residuals. By faithfulness, zero residuals are reflected as well. The component inverses therefore restrict to inverse maps on the solution sets of that represented equation system.

A GR solution returned by a solver can consequently be translated back to a solution of the represented Genesis equation system. This is not a theorem that a solver finds all solutions, that numerical approximations are exact, or that the returned endpoint is realized by an upstream native state. Those are separate assertions. No global nonlinear PDE existence or well-posedness proof is supplied here.

## 8. Patching and what 'global' can mean here

The tensor and connection formulas are intrinsic. A change of local frame and chart gives the usual compatible transformed formulas, so local evaluated geometric translations agree on overlaps where the native differential anchor and metric/source data actually glue. This does not require a single global frame.

For a represented geometric-record object `(P,K,J)`, the previous checkpoint's inverse `(PT_(∇g),g|x0,J_g[T])` is compatible with these translations. The connection proof above makes its operation-preservation explicit.

This does not prove that every allowed native branch glues to a smooth four-manifold, that every topology admits the native structure, or that an inverse native lift exists on every GR spacetime. The theorem is global over the **already supplied compatible smooth geometric objects**, not a global native existence theorem.

The same distinction applies to boundaries and observables: formulas built naturally from retained fields and boundary structure are preserved. An independent native charge, boundary mode or matter state cannot be dropped by naming it gauge. Singular charts are excluded or patched, not inverted at their singular points.

## 9. Executed end-to-end demonstration

The implementation has an `EvaluatedGenesisEndpoint` with a smooth frame anchor, evaluated native metric, selected connection, conormal probes, witnessed local flux densities, Λ and κ, and retained data. It translates to a `GREndpoint`, then back. The reverse returns endpoint components in the fixed frame/probe context. It does not claim to manufacture native History, Bandwidth or chirality.

Three constructed four-dimensional fixtures are checked:

1. Flat spacetime in a nonconstant sheared native frame. The code computes native Koszul connection and non-coordinate curvature, independently computes the GR Christoffel route, and compares both covariant derivatives and their composition.
2. A curved product chart, with constant orthonormal native metric but nontrivial frame brackets. Both routes give scalar curvature 2. Removing the bracket term makes curvature disagree.
3. A spatially flat expanding geometry with arbitrary smooth positive a(t), independent density ρ(t) and pressure p(t), and constant Λ and κ. Starting native data are k=diag(−1,1,1,1), A=diag(1,1/a,1/a,1/a) and independently supplied flux diag(ρ,p,p,p). Both independent calculations yield

       F_G,00 = 3(a'/a)^2 − Λ − κρ,
       F_G,ii = −2a''/a − (a'/a)^2 + Λ − κp,
       (Div_G T)_0 = −[ρ' + 3(a'/a)(ρ+p)].

The GR metric is diag(−1,a²,a²,a²), and its spatial residual is a² times the displayed native spatial residual. Translating it back recovers the original expression. No equation of state or native physical solution is inferred. These are off-shell symbolic identities, not a comparison forced by setting the residual to zero.

The JSON ledger records the exact number and outcome of checks. The first development run passed 32 checks, then encountered a rank-one indexing TypeError in the test interface. That trace is retained. The indexing interface was corrected and the suite rerun. This was an implementation error, not a change to the mathematical model or its claims.

The test suite also rejects singular anchors, degenerate metrics, incompatible selected connections, insufficient probe data, asymmetric sources in the declared sector and unsupported raw-native input. Signature and smoothness over symbolic regions are explicit mathematical assumptions of the fixtures, not globally proved by SymPy.

## 10. The remaining native obstruction is not renamed away

The requested full translation would begin with an actual native state q. The retained source still requires an actual attachment

    A_native(q) = (Q_R[q], selected transport[q], witnessed flux[q], retained matter[q]).

The theorem and code now close the tensor/connection/operation portion **after** an admitted evaluated attachment. They do not evaluate A_native on the original unresolved raw variables. Its reverse still requires a native state satisfying the actual constraints and producing the prescribed output; the uniqueness must be physical, not obtained by deleting hidden distinctions.

The Atlas's exact recovery criterion states that a decoder for the requested class exists on attainable observations if equal observations imply equality of that class. It does not supply missing evaluation rules, attainability, or a new definition of physical identity. Its partial-operation criterion also requires domain equality; that is why the translator refuses unsupported native inputs rather than filling them from the target.

There is no contradiction between the following statements:

- A complete operation-preserving tensor translator has been proved for evaluated smooth endpoint data.
- The original native-to-endpoint attachment and full native physical inverse have not been established.

The user requested both. Only the first has been completed in this run. No percentage or total-equivalence certificate is issued.

## References and provenance

S01–S09: original source copies and hashes in `evidence/SOURCE_MAP.json`.

A1: The Atlas of Becoming, supplied 68-page report, checkpoint v2.5.0, Appendix A.3 (PDF page 54), and sections 8.1, 9.2. The supplied page-54 image was visually inspected. Its linear recovery result is not used as a theorem about this nonlinear native attachment.

R1: David Tong, General Relativity, section 3, especially Levi-Civita uniqueness, covariant differentiation, parallel transport and moving-frame curvature. https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S3.html (accessed 31 October 2026).

R2: David Tong, General Relativity, section 4, for the conventional Einstein/source conventions and cosmological comparison. https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S4.html (accessed 31 October 2026).

R1 and R2 support standard differential-geometric identities only. They are not evidence that the native Genesis metric functional has been evaluated. The implementation and its test results are products of this run, not recovered historical source files.
