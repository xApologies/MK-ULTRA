# Native metric and source realization: explicit construction and its boundary

**Date:** 31 October 2026  
**Status:** Exact reconstruction theorem for a specified smooth transport–metric–flux sector. **Total physical equivalence of the existing native Genesis theory with GR is not established.**  
**Source integrity:** No user source or repository file has been changed. Proposed constructions and additional realization hypotheses are distinguished from recovered source statements.

## 1. Result, without a change of question

This work constructs a metric from an admitted smooth transport family and its calibrated bilinear form at one reference point. It constructs the local stress-energy tensor from directional four-momentum flux densities. The two constructions have explicit inverses at the level of the smooth geometric records.

The strongest completed equality is:

    calibrated Levi-Civita transport + smooth symmetric momentum-flux density
        ↔
    smooth Lorentzian metric + smooth symmetric stress tensor.

This is a geometric representation theorem. It neither postulates a new native gravitational update law nor proves that the existing Genesis configuration (D, ℛ, R, B, H, χ, C, P) generates every such record. The latter is the actual native realization problem asked for by the user. It remains unevaluated, not solved by renaming the record space.

In particular, this work does NOT define the stress tensor as the Einstein tensor divided by a coupling; does NOT take GR field equations as a derived consequence of unspecified native dynamics; does NOT quotient unseen native differences away by decree; and does NOT identify a finite pre-differential lift with a smooth linear parallel transport without an explicit hypothesis.

## 2. Recovered source basis

[S1] The latest thirteen-point module prescribes

    𝔤_G(x;a,b) = Q_R[ℛ_x(a,b), B_x, H_x, χ_x],
    ρ_G(𝔤_G) = g,
    dP_G^a = 𝔗_G^{ab} dΣ_b.

It gives a GR-sector connection realization, path transport, curvature contractions and an Einstein equation. It does not give an evaluation rule for Q_R in the displayed metric definition.

[S2] The drop-in contract protects the upstream MK Ultra objects and says the downstream representation must be revised rather than changing an upstream equation's meaning.

[S3] The audit retains nondegeneracy, the smooth/refinement curvature limit, and existence of source densities as mathematical realization conditions.

[S4–S5] The earlier formalism declares a rank-four real Lorentzian GR sector, torsion-free metric compatibility, and finite-to-local source conditions. Its status file explicitly labels the introduced GR constructions as new module axioms/definitions, not recovered upstream theorems. The later module's Q_R condition remains binding; the earlier freely declared metric is not used to bypass it.

[S6–S7] The transport sources distinguish the finite/pathwise Transduction Connection from a downstream smooth differential connection, and retain their compatibility as a problem rather than identifying them automatically.

[S8] The finite source file defines additive four-momentum, witnessed oriented transfers, and assumes densities under refinement before using dP_G^a = 𝔗_G^{ab}dΣ_b.

The Atlas gives exact feature/history recovery criteria relative to specified evidence and a specified equivalence relation [A1]. Its criterion is used at the end to distinguish geometric recovery from recovery of a complete native physical state.

Exact archive member paths, hashes, and original line-numbered excerpts are included in SOURCE_EVIDENCE.md and PROVENANCE.json. A bounded text-index scan was used to locate relevant passages; it was not a substantive audit of every mathematical claim in the archives.

## 3. Declared smooth realization setting

Work on a connected smooth four-dimensional region U, with a chosen orientation and base point x₀. The native GR-readable rank-four real bundle must have a specified identification with TU. An unanchored internal rank-four bundle is not automatically the tangent bundle.

Assume the represented native path maps P_γ are the parallel transports of a smooth linear connection D on TU. They are invertible, compose along concatenation, reverse under path reversal, and have the required smooth path dependence. For the GR sector require D to have zero torsion. These are conditions for the present theorem, not deductions from arbitrary partial native lifts.

Full global claims require the complete holonomy of the admitted region, including noncontractible loops. If Bandwidth restrictions make only some paths available, the theorem applies only after an adequate transport family is established; it does not silently add forbidden native paths. Nonorientable settings can instead use densities, but that extension is not needed here.

K denotes the reference-point bilinear form. It is not Bandwidth, not curvature, and not energy. It must come from the metric functional or equivalent native calibration, not from a convenient guessed value.

## 4. Constructing all compatible metrics from the native transport

### 4.1 The algebraic problem at one point

For every closed loop ℓ based at x₀, let H_ℓ = P_ℓ. Define

    I_H = {K ∈ Sym²(T*_{x₀}U) : H_ℓᵀ K H_ℓ = K for every such loop ℓ}.

This is a vector space of invariant symmetric bilinear forms. Its matrices have ten independent entries in four dimensions. The invariance equations are linear in those entries. A metric requires a member with nonzero determinant and signature (−,+,+,+).

A finite list of holonomies determines the full answer only if it is independently known to generate the relevant holonomy group, or otherwise impose all its invariant-form conditions. Testing a few loops is not proof about all loops.

For a connected Lie holonomy group whose full Lie algebra has been determined, invariance can be expressed as

    XᵀK + KX = 0

for every Lie-algebra generator X. Disconnected components require their own checks. Curvature matrices at one point need not generate the full holonomy algebra; no such shortcut is used.

### 4.2 Metric formula

Choose an invariant Lorentzian K, with its scale and other free parameters fixed by the native interval calibration. For a path γ from x₀ to x define

    𝔤_x = P_γ^(−T) K P_γ^(−1).                           (M1)

Coordinate-free, for u,v ∈ T_xU,

    𝔤_x(u,v) = K(P_γ^(−1)u, P_γ^(−1)v).

### 4.3 Proof of path independence

Let α and β be two paths from x₀ to x. Their relative transport H = P_α^(−1)P_β is a based-loop holonomy. Thus P_β = P_αH. Since HᵀKH=K, also H^(−T)KH^(−1)=K. Consequently

    P_β^(−T) K P_β^(−1)
      = P_α^(−T) H^(−T) K H^(−1) P_α^(−1)
      = P_α^(−T) K P_α^(−1).

Equation M1 is therefore independent of the chosen path. It preserves signature and nondegeneracy by invertible congruence.

Smoothness follows locally by using a smoothly varying family of paths, together with the assumed smooth transport. Path independence makes these local definitions agree on overlaps.

### 4.4 Metric compatibility and necessity

Extend a path from x₀ by any path from x to y. M1 gives

    𝔤_y(P_{x→y}u, P_{x→y}v) = 𝔤_x(u,v).

Thus the connection preserves the metric, D𝔤=0. Conversely, if a metric is preserved by the supplied transport, transporting it from x₀ forces M1; a loop forces H_ℓᵀKH_ℓ=K. Therefore invariant seed forms parametrize exactly the parallel metrics for that connection.

With zero torsion, uniqueness of the Levi-Civita connection identifies D with the Levi-Civita connection of the reconstructed metric. This is a standard metrizability argument, specialized here to the source's path-transport language [R1–R3]. It is not claimed as a new general theorem.

### 4.5 Exact scope of metric uniqueness

Fixing D and K fixes the metric uniquely on the connected region. Fixing D alone generally does not.

For example, if transport is trivial in a global frame, every constant symmetric form is parallel. There are ten linear calibration parameters before imposing Lorentzian signature. For the declared test family of three Lorentz boosts, the invariant space is one-dimensional, proportional to diag(−1,1,1,1); one physical scale remains to be calibrated. Neither example is asserted to be the actual native gravitational holonomy.

More generally, if dim I_H = r, r independent linear calibration conditions with full rank on I_H determine at most one member. Consistency, nondegeneracy, and Lorentzian signature remain necessary. It is not justified to assume r=1 in the native theory.

### 4.6 Native interval calibration without guessing a Minkowski matrix

If the native signed interval q(v)=𝔤(v,v) is available on a basis e_a and their sums, then

    K_aa = q(e_a),
    K_ab = [q(e_a+e_b) − q(e_a) − q(e_b)] / 2, a<b.      (M2)

Four diagonal and six pair-sum evaluations reconstruct all ten entries. This is polarization of a symmetric bilinear form. Ten observations do not prove a general interval rule is quadratic; bilinearity/quadraticity must follow from the admitted metric realization. Absolute lengths |q| or unsigned lengths alone are not substituted for signed intervals.

M2 is a decoder for actual interval data. It is not a new formula for how ℛ, B, H and χ generate those data.

### 4.7 The exact Q_R compatibility identity

Any actual metric functional consistent with the declared smooth native connection must satisfy

    Q_R[ℛ_x, B_x, H_x, χ_x]
      = P_{x₀→x}^(−T) Q_R[ℛ_{x₀}, B_{x₀}, H_{x₀}, χ_{x₀}]
        P_{x₀→x}^(−1).                                  (M3)

Here Q_R is being evaluated as a bilinear-form matrix in the specified frames. M3 follows from the existing metric-compatibility requirement plus the smooth-realization hypothesis. It reduces a compatible metric field to the actual selected transport and calibrated reference form.

It does not evaluate the right side when those native inputs are unspecified. Declaring M3 to be a new definition of Q_R would be a proposed closure of the model, not a recovered evaluation of its original functional.

## 5. Constructing the source tensor from witnessed flux

### 5.1 Four independent directional probes

At x fix four linearly independent oriented hypersurface conormals n^(I), I=0,1,2,3, with their physical normalization recorded. Let v_I^a be the native four-momentum flux density through the corresponding infinitesimal hypersurface element.

The source equation gives

    v_I^a = 𝔗^{ab} n_b^(I).

Form matrices N_bI=n_b^(I) and V_aI=v_I^a. Then

    V = 𝔗^up N,
    𝔗^up = V N^(−1).                                   (S1)

This is an explicit source reconstruction, not a source defined by curvature. The inverse readout is

    V = 𝔗^up N.                                         (S2)

For fixed invertible N, both round trips are the identity. The non-spin GR sector additionally requires 𝔗^up to be symmetric. A change of probe basis N→NC, V→VC leaves VN^(−1) unchanged.

These are local density values. Integrated flux over finite surfaces cannot be substituted directly for them without accounting for surface measure, variation within the surface, and tangent-space comparison. A null surface has no unit timelike/spacelike normal; using calibrated conormals and directed hypersurface elements avoids an invalid unit-normal assumption.

The covariant tensor entering Einstein's equation is

    𝔗_down = 𝔤 𝔗^up 𝔤ᵀ.                                (S3)

This index conversion matters when comparing S1 with the covariant field equation.

### 5.2 What is needed for the density to exist

The source itself assumes densities under refinement [S8]. A sufficient local interpretation is that the component fluxes in a declared frame define countably additive, locally finite signed measures on the relevant hypersurfaces, absolutely continuous with respect to the directed area measure, with regular densities. Almost-everywhere densities alone determine tensor fields only almost everywhere; smoothness or continuity supplies the stronger pointwise version.

Finite additivity alone does not prove a density exists. Four independent probes reconstruct a tensor only if the full flux law is linear in the oriented conormal, as required by dP_G^a = 𝔗_G^{ab}dΣ_b. A test on four directions does not prove an arbitrary flux law has that linearity.

### 5.3 Covariant assembly and exact inverse

Let vol_𝔤 be the metric volume form. In a local frame e_a, define the tangent-bundle-valued three-form

    𝒥 = e_a ⊗ 𝔗^{ab} ι_{e_b} vol_𝔤.                    (S4)

The four three-forms ι_{e_b}vol_𝔤 are a basis, so their coefficients determine 𝔗^{ab} uniquely. This gives a coordinate-independent encoding/decoding of the source tensor and its local momentum-flux density, once the metric and orientation are fixed.

In a curved space, summing flux vectors from different tangent spaces needs the supplied transport. S4 does not pretend they are already vectors in one common vector space. Global integration must use an appropriate trivialization or explicit comparison rule; the local reconstruction is intrinsic.

### 5.4 Conservation is a separate compatibility test

For the Levi-Civita connection, the covariant exterior derivative satisfies

    D𝒥 = e_a ⊗ (∇_b 𝔗^{ab}) vol_𝔤.                     (S5)

Proof in coordinates: write dΣ_b=ι_{∂_b}vol_𝔤. The ordinary derivative of 𝔗^{ab}dΣ_b contributes ∂_b𝔗^{ab}+Γ^c_cb𝔗^{ab}. The connection on the free vector index contributes Γ^a_bc𝔗^{cb}. After relabeling dummy indices, the sum is ∇_b𝔗^{ab}. Torsion-free volume compatibility is used here.

Thus D𝒥=0 is precisely covariant stress-energy conservation in this smooth setting. Reconstruction does not impose it automatically. The supplied finite accounting must produce this covariant limit, including its comparison transport; raw scalar cancellation of cell faces is not by itself that proof.

## 6. A complete inverse for the geometric records

Define a geometric-record space K(U) consisting of:

- a full smooth torsion-free tangent parallel-transport family P;
- an invariant Lorentzian form K at x₀ with fixed calibration;
- a smooth tangent-valued three-form 𝒥 whose decoded source tensor is symmetric.

The base manifold, tangent identification, orientation and boundary conventions are retained. No independent native History, Bandwidth or chirality data are hidden in this definition.

Define F_geom(P,K,𝒥)=(𝔤,𝔗), using M1 and S4. Define the reverse map by

    L_geom(𝔤,𝔗)
      = (parallel transport of ∇^𝔤, 𝔤|_{x₀}, 𝒥_𝔤[𝔗]).   (I1)

For any smooth Lorentzian metric and smooth symmetric source tensor, metric preservation implies that F_geom(L_geom(𝔤,𝔗))=(𝔤,𝔗).

Conversely, start with an admitted record (P,K,𝒥). The reconstructed 𝔤 is parallel for the supplied torsion-free connection. Uniqueness of the Levi-Civita connection makes ∇^𝔤 exactly that connection, so every path transport is recovered. The reference value and the three-form are recovered by construction. Therefore

    L_geom(F_geom(P,K,𝒥)) = (P,K,𝒥).                     (I2)

This proves both directions and uniqueness for geometric records, not just endpoint isomorphism of individual tensors. It is compatible with changes of frame and diffeomorphisms preserving the declared domain and boundary data.

A caveat about computation: recovering a connection from transport uses infinitesimal paths starting at EACH point. Taking −dP(x)P(x)^(−1) for one chosen family of paths from x₀ is not generally the original curved connection; that construction alone can confuse a frame with the full path-dependent transport.

## 7. Einstein equations and complete physical states

For the reconstructed geometric pair, evaluate the actual residual

    𝔉 = Ric[𝔤] − (Scal[𝔤]/2) 𝔤 + Λ_G 𝔤 − κ_G 𝔗_down. (E1)

The geometric-record bijection restricts to a bijection on E1=0. This is an exact representation of the metric-plus-source Einstein system. It does not derive that condition from an independent native dynamics.

A complete matter theory includes matter fields and their equations, not only their combined stress tensor. For a specified matter model, retain its fields, bundles, couplings, equations, gauge, charges and boundary conditions on both sides. The geometric inverse does not reconstruct them from 𝔗 alone. They can be carried through I1 unchanged as additional data, but that is not an inverse to a native matter-generation map.

## 8. Applying the construction to the actual native state

Let q denote an actual admitted native gravitational configuration/history, and let A(q) extract the geometric records above from its existing laws. Then the intended readable map factors as

    q ──A──> (P^q, K^q, 𝒥^q, retained matter data)
      ──F_geom──> (g,T, retained matter data).            (N1)

F_geom now has the explicit inverse I1 on its stated domain. The unresolved inverse is A, not the downstream matrix algebra.

For a target solution (g,T,ψ), the actual native lift must solve simultaneously

    P^q_γ = parallel transport of ∇^g along γ,
    Q_R[q at x₀] = g|_{x₀},
    𝒥^q = 𝒥_g[T],
    native retained matter readout(q) = ψ,
    q satisfies every applicable native constraint and equation.       (N2)

These are simultaneous native realization conditions, not a definition that makes them true. No q solving N2 for an arbitrary GR solution has been constructed in this work. Nor has it been proved that all such q represent the same native physical state.

The Atlas supplies the exact distinction [A1]: recoverability of a target class requires the retained evidence to distinguish all classes that remain physically different. Its criterion does not decide which histories are physical redundancies, and does not supply missing input values for Q_R, P or 𝒥.

Hence the complete physical inverse would be

    L_phys = A_phys^(−1) ∘ L_geom,

only after A_phys has been shown to be a structure-preserving bijection onto the required geometric/matter solution sector. A_phys^(−1) is not implemented or asserted to exist here.

## 9. Executed nonlinear check

The implementation verifies a constructed curved example, not a native-corpus gravitational solution. Use a local chart on R×S²×R with 0<x<π, reference x₀=π/2, and independently supplied nonzero connection coefficients

    Γ^x_yy = −sin(x)cos(x),
    Γ^y_xy = Γ^y_yx = cot(x).

Set the calibrated seed to diag(−1,1,1,1) for this example only. Along an x segment, transport is diag(1,1,1/sin(x),1). Along a y segment at fixed x, its x-y block is

    [ cos(y cos x),       sin x · sin(y cos x) ]
    [−sin(y cos x)/sin x, cos(y cos x)         ].

M1 reconstructs

    ds² = −dt² + dx² + sin²(x)dy² + dz².

The script verifies metric compatibility, zero torsion, recovery of all 64 Christoffel components, and scalar curvature 2. It reconstructs an independently prescribed directional-flux source

    T^up = diag(1/κ,0,0,−1/κ)

and verifies the Einstein residual with Λ=0 and covariant conservation. This is a designed consistency fixture with independently specified flux data. It is not a claim that native Mass/Persistence produces those fluxes or that a particular native matter equation realizes the source.

Other checks verify symbolic reconstruction of all ten symmetric form components, symbolic flux round trips, rejection of deficient directional data and nonsymmetric sources, and holonomy-preserving path independence. Eighteen named checks passed. Their detailed scopes are in CHECK_RESULTS.json. They are not eighteen independent native-equivalence theorems.

## 10. Determination

Completed: a constructive metric-extension theorem from native-compatible smooth transport and calibration; a unique source decoder from directional momentum-flux densities; and a complete inverse between those geometric records and the metric/source presentation.

Not completed: evaluation of those records from the full existing native variables; existence and physical uniqueness of the native solutions of N2; matching native dynamics and full matter/boundary observables; total native Genesis–GR equivalence.

The source clauses retain Q_R as the metric functional and selected lifts as the operative transport. Filling their remaining operational content by stipulating GR data would be a new realization choice. This work does not silently make that substitution. It supplies the explicit geometric decoder and identifies exactly which preceding map it does not invert.

## References

[S1–S8] User-provided source excerpts with archive paths and hashes: SOURCE_EVIDENCE.md.

[A1] The Atlas of Becoming, supplied foundational report, Appendix A.2–A.3 (PDF pages 53–54; printed pages 48–49), especially the attainable-evidence limitation and the feature-versus-whole-state distinction. The supplied page-54 rendering was inspected alongside the provided text.

[R1] Erico Tanaka and Demeter Krupka, On Metrizability of Invariant Affine Connections, arXiv:1111.3009, introduction: metric-compatibility equations and the inverse metrizability problem. Retrieved 31 October 2026. `https://arxiv.org/abs/1111.3009`

[R2] David Tong, General Relativity, Section 3: metrics, Levi-Civita connections, parallel transport, holonomy. Retrieved 31 October 2026. `https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S3.html`

[R3] Charles Boubel, On the holonomy of Lorentzian metrics, Annales de la Faculté des Sciences de Toulouse 16(3), 2007, Section 1.1: full and restricted holonomy. Parsed text inspected; web screenshot request failed with HTTP 403. `https://afst.centre-mersenne.org/item/10.5802/afst.1156.pdf`

These standard references validate the geometric language, not the native Genesis realization. The native-specific compatibility claims must come from the supplied theory or a new explicitly justified construction.
