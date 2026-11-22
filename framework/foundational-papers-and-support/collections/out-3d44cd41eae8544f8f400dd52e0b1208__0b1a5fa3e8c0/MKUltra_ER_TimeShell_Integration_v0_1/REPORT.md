# MK Ultra: ER-preserving Time-Shell integration

**Version:** 0.1 — 31 October 2026  
**Scope:** source-grounded native modal dynamics; an exact dynamical interface; explicitly new nonlinear ER candidates; a continuum boundary-response calculation.  
**Determination:** the ER network and the admitted gravitational-helicon amplitude can be coupled and translated through a memory-bearing interface without erasing their dynamics. This report does **not** complete the original microscopic theory or establish its full nonlinear equivalence with GR. The unresolved step is the native tensor/clock/geometric handoff and its nonlinear gravitational constraints, not the finite-network elimination algebra.

The original Time Shell remains the physical interface. The microscopic ER network is NOT replaced with the eight-channel GRC-1 metric encoding. The latter remains a downstream representational option only. The native 3+1+1 organization is not reinterpreted as an ordinary extra spatial coordinate. Node count, boundary-port count, and native dimension are different quantities.

## 1. Source basis and protected architecture

The full source in `evidence/API43_CANONICAL_UNCHANGED.md` is copied byte-for-byte from the previous native-ER checkpoint. `evidence/SOURCE_EXCERPTS.md` preserves literal passages with original line numbers. This run examined those passages and targeted matches in that source, not every original nested archive or all later versions.

The actual source contracts matter more than a convenient new diagram:

* S01–S02: ER foam has both a propagating-mode branch and a localized-knot branch. The native graviton is the gravitational member of the helicon family. The source explicitly says it is NOT produced by matter, the Time Shell, or projected spacetime. Continuity perturbation passes through a tensor/TT restriction and the Time-Shell projection to a readable metric perturbation.
* S04: an admitted gravitational-helicon amplitude has a weighted-graph Laplacian and a second-order recurrence in integer recursive update depth n. No identification of n with physical clock time is supplied by that equation.
* S03: the archived shell material includes a quadratic shell action on a two-dimensional spatial surface, an induced metric, a projected bulk response, and a scalar response coefficient proportional to 1/sqrt(k^2-omega^2+i0). These expressions have to be compared at the correct dimension and operator type.
* S05: a nonlinear continuity fixed point is recorded, but its complete functional operators are not evaluated by this work.
* S06: the norm-isometry statement concerns an OPTIONAL quantized representation. It is not a reason to reinterpret all native organization as a quantum field or to mistake a classical recurrence matrix for a unitary matrix.
* S07: native configuration has the declared 3+1+1 form and a readable 1+3 projection. This is retained as source context, not filled in by an invented extra normal coordinate in a continuum calculation.

Two literal nested source documents were additionally recovered from the exhaustive recovery ZIP. `05_TIME_SHELL_INTERFACE.md` separates persistent boundary, Time-Shell projection, and Resolution-conditioned readout. `07_TIME_SHELL_HISTORY_READOUT.md` explicitly calls its whole-object tuple an Atlas typing rather than a recovered Tome identity; it places readable time downstream of persistence/history. Both are copied unchanged.

### Interpretation boundaries

The finite shell used below is a chosen set of graph ports, or an equivalent declared linear observation subspace. This is a concrete **candidate realization of part of the interface**, not proof that the original persistent boundary or Pi_T is precisely this node subset. Its selection still needs to be attached to the original geometric definitions. The calculations are exact once the choice is supplied.

The block-elimination theorem is not limited to selecting nodes. For any specified full-row-rank linear readout C, use a singular-value decomposition C=U S V_s^T and complete V_s to an orthogonal basis. In that basis s=V_s^T H and the actual output y=U S s are invertibly related, so the same block equations apply to the transformed operator. The nonnegative-edge/no-crossing interpretation applies specifically to node partitions; the code fixtures use that case. This does not construct the missing physical readout C.

H below denotes an amplitude within the source's ALREADY ADMITTED gravitational-helicon sector. Calling it H does not derive its helicity, polarization tensors, or admission from generic scalar graph oscillations. History records are separate and are not denoted by H in the calculations.

## 2. Native propagation and its variational structure

For a finite symmetric entrywise-nonnegative matrix W, let

    L = diag(W 1) - W,
    A = c_A^2 L.

Self-weights W_ii cancel from L. They remain in the microscopic record because they can enter other readouts. For any real amplitude v,

    v^T L v = sum_{i<j} W_ij (v_i-v_j)^2 >= 0,
    L 1 = 0.

The recovered homogeneous equation is

    H_(n+1) - 2 H_n + H_(n-1) + A H_n = 0.                 (N1)

For source-response analysis introduce a declared external native modal drive J_n, giving RHS J_n. This source probe is new analytical input; it is not automatically the spacetime stress tensor.

A discrete action realizing exactly that recurrence is

    S_d[H] = sum_n { 1/2 ||H_(n+1)-H_n||^2
                    - 1/2 H_n^T A H_n + J_n^T H_n }.       (N2)

Variation with fixed endpoint amplitudes yields N1 with RHS J_n. The variation from the two neighboring kinetic terms is 2H_n-H_(n-1)-H_(n+1), and the potential derivative is -A H_n. Thus no continuum-time approximation is used. The action is a mathematical realization of the recorded recurrence, not a recovered total MK Ultra action.

### Stable band and exact invariant

On an L eigenmode with eigenvalue lambda, define eta=c_A^2 lambda. The characteristic polynomial is

    r^2 - (2-eta)r + 1 = 0.

For 0<eta<4 the roots have unit modulus and the mode is oscillatory. At eta=0, solutions are a+bn, so the zero-restoring-force mode can drift; it is not correct to claim all solutions are bounded. At eta=4 there is a repeated root -1 and possible linearly growing alternating solutions. For eta>4 generic solutions grow exponentially.

For a fixed W and zero drive, the exact invariant is

    I_n = 1/2 ||H_(n+1)-H_n||^2 + 1/2 H_n^T A H_(n+1).     (N3)

Subtract consecutive values and use N1 to prove I_n=I_(n-1). With m=(H_(n+1)+H_n)/2 and d=H_(n+1)-H_n,

    I_n = 1/2 d^T (I-A/4)d + 1/2 m^T A m.                 (N4)

It is nonnegative on the stable band. This is a native-depth invariant, not a calibrated spacetime energy or a proof of the old Persistence energy formula.

The full first-order state X_n=(H_n,H_(n-1)) evolves by

    X_(n+1) = M X_n,
    M = [[2I-A,-I],[I,0]].                                (N5)

M is invertible and symplectic for the standard block symplectic form when A is symmetric. It need not be Euclidean-unitary. This distinction is preserved throughout.

The absence of a bare restoring term at lambda=0 preserves the recorded native zero-mode structure. It does NOT alone prove massless Lorentzian spin-2 propagation, universal coupling, or the Einstein constraints.

## 3. Exact Time-Shell elimination: ER dynamics become memory

Partition admitted amplitudes into shell ports s_n and unresolved interior amplitudes b_n. Write B=2I-A, with blocks B_ss,B_si,B_is,B_ii. Here B is an auxiliary matrix, NOT Genesis Bandwidth. The full equations are

    s_(n+1) = B_ss s_n - s_(n-1) + B_si b_n + J_s,n,
    b_(n+1) = B_ii b_n - b_(n-1) + B_is s_n + J_i,n.        (T1)

Introduce interior response polynomials

    G_0=0, G_1=I,
    G_(m+1)=B_ii G_m-G_(m-1).

For n>=1, direct substitution or induction gives

    b_n = G_n b_1 - G_(n-1)b_0
          + sum_{k=1}^{n-1} G_(n-k)(B_is s_k+J_i,k).        (T2)

Insert T2 into the shell equation:

    s_(n+1) = B_ss s_n - s_(n-1) + J_s,n
              + B_si(G_n b_1-G_(n-1)b_0)
              + sum_{k=1}^{n-1} K_(n-k)s_k
              + sum_{k=1}^{n-1} B_si G_(n-k) J_i,k,

    K_m = B_si G_m B_is.                                  (T3)

This is an explicit, causal, exact memory law in native update order. K_m is computed from the same W and the same recurrence; it is not a fitted replacement graph. The initial-interior term is not noise unless a probability distribution is independently supplied.

### Two-way theorem

Given the graph, partition, drive, and full initial pair, every solution of T1 restricts to a solution of T3. Conversely, given a solution of T3 and b_0,b_1, define b by T2. The interior equation follows from the defining recurrence of G; substitution into T3 supplies the shell equation. Thus both representations give exactly the same full trajectory, and both round trips are identities on this retained-data domain.

This does NOT compress away physically distinct initial interior states. It is a lossless dynamical representation with explicit retained data. The exact dependence on previous states gives a concrete mechanism for memory in an ER-supported interface, rather than a declaration that a shell metric contains all History.

This is a finite discrete version of standard exact elimination/projection methods. Such methods are related to Mori–Zwanzig memory constructions; no novelty claim for Schur complements or memory reduction is made [R1]. The source-specific contribution is their exact application to the recovered ER recurrence and the explicit return map.

### A useful impossibility result for a particular shortcut

An autonomous second-order law for (s_n,s_(n-1)) alone, valid for arbitrary hidden initial pairs, can exist only if B_si=0. Necessity: change b_n while holding the shell pair fixed; T1 changes s_(n+1) by B_si delta b_n. Sufficiency follows directly from T1 when this block vanishes.

For a node partition in a symmetric nonnegative network, B_si=0 precisely when there are no cross-boundary edges. Therefore an interacting ER boundary generically cannot be made memoryless on its instantaneous shell pair without losing dynamics. Higher-order history encodings, restricted initial families, or enlarged shell state are different possibilities, not excluded by this theorem.

## 4. The response operator and the propagator are different objects

For a stationary Fourier mode e^(-i omega n), set

    z=4 sin^2(omega/2).

The source equation is (A-zI)H=J. Away from singular interior resolvents, eliminating b gives

    D_sigma(z) = A_ss-zI
                 -A_si(A_ii-zI)^(-1)A_is,                  (T4)

    J_eff = J_s - A_si(A_ii-zI)^(-1)J_i,
    D_sigma(z)s = J_eff.

D_sigma is the inverse-response/dynamic stiffness. The shell propagator is

    G_sigma(z)=D_sigma(z)^(-1)
              =[(A-zI)^(-1)]_ss.                          (T5)

The symbol K_TT in the archived expression denotes a projected response. It must not be equated to the stiffness D_sigma without inversion. Poles require the specified analytic continuation or initial/boundary prescription. An interior singularity can make this particular factorization undefined even when a limit of the full shell response exists; no pole is silently canceled.

The frequency-domain Schur identity is algebraic. The causal initial-value law is T3. We do not claim that varying an ordinary single-history action with a purely retarded nonsymmetric kernel reproduces T3; that would need an appropriate initial-value/in-in formalism. The parent action and full system are retained.

### Static reduction and induced inertia

Assume every connected interior component touches the selected boundary, so L_ii is positive definite. Then

    D_sigma(0) = c_A^2 [L_ss-L_si L_ii^(-1)L_is].           (T6)

The bracket is the Kron/Schur-reduced Laplacian. It annihilates the constant boundary vector, so eliminating the bulk has not introduced an artificial constant-mode mass.

For |z|<a_min=min eig(A_ii), the convergent resolvent series gives

    D_sigma(z)=D_sigma(0)-z M_eff+R_2(z),
    M_eff=I+A_si A_ii^(-2)A_is.                            (T7)

M_eff is positive definite because its additional term is a Gram matrix. A useful error bound is

    ||R_2(z)|| <= |z|^2 ||A_si||^2 /
                  [a_min^3(1-|z|/a_min)].                 (T8)

The exact shell theory therefore contains induced inertia and higher-history effects from the foam. A static reduced graph can approximate it only in a controlled band, not at every frequency. There is no uniform low-frequency approximation across a closing interior gap.

## 5. Reconstruction from readable history when it is actually possible

Retaining b_0,b_1 always supplies the finite return map above. Sometimes sufficient shell observations recover them instead.

Let C select the shell components of X_n in N5. Define

    O = [C; CM; CM^2; ...; CM^(2N-1)].                     (R1)

For the unforced system, the first 2N shell samples are O X_1. A unique complete initial pair is recoverable iff rank O=2N. On that domain,

    X_1=(O^T O)^(-1)O^T observations.                      (R2)

Known drives can be subtracted before applying the formula. With unknown drives this criterion is insufficient. Numerical rank and conditioning matter; an exact rank statement is not a guarantee of robust noisy inversion.

For a three-node path and observation at an endpoint, rank O=6. The implementation reconstructs all six initial amplitude values from six successive endpoint samples. Observing only the center gives rank 4. The antisymmetric endpoint mode (1,0,-1) is invisible at the center for its entire linear trajectory; its two initial coefficients must be retained or otherwise measured.

These dark modes are not declared gauge. Nor does the boundary response alone identify the labeled graph W: distinct internal realizations can have the same boundary transfer function. W, node typing, and the chosen shell observation remain part of the supplied representation context.

## 6. An original Time-Shell kernel has a natural boundary interpretation

S03 records

    K_TT(omega,k)=Pi_TT G_bulk Pi_TT,
    K_TT(omega,k)=4 pi G_N / sqrt(k^2-omega^2+i0),           (B1)

alongside a spatial two-surface action and an induced surface metric. It would be premature to interpret B1 as a four-dimensional bulk propagator and reject it merely because of its inverse-square-root power.

Work first in a Euclidean or real spacelike spectral region with p>0, so no causal-prescription ambiguity enters. A massless bulk scalar coefficient with one normal momentum q obeys

    int_R dq/(2 pi) [1/(q^2+p^2)] = 1/(2p).               (B2)

With bulk coefficient 8 pi G_N, its restriction to the surface is

    int dq/(2 pi) [8 pi G_N/(q^2+p^2)] = 4 pi G_N/p.       (B3)

Thus the archived scalar prefactor is exactly the form of a bulk-to-surface trace. In a 3+1 bulk, the spatial surface has two tangential coordinates and its worldvolume is 2+1. The integrated normal coordinate in this calculation belongs to the READABLE bulk; it is not an identification of the native artifact/chirality coordinate with an extra spacetime dimension.

This is a precise possible interpretation, not proof that the source intended all of these boundary conditions or normalizations. In particular:

1. The scalar denominator and prefactor match. The full spin-2 projector/numerator, matter coupling, and gauge constraints still need an actual comparison.
2. A momentum-dependent tensor projector cannot generally be pulled out of the normal-momentum integral. B2 alone is not a tensor-propagator proof.
3. Retarded continuation would use a chosen branch associated with p^2=|k_parallel|^2-(omega+i0)^2. The source's printed '+i0' is not silently asserted to specify that prescription.
4. This is a selected boundary calculation, not recovery of an arbitrary bulk state from one surface value.

### An ER-chain calculation supplies the same continuum limit

Take an infinite nearest-neighbor normal chain with readable spacing ell, and a fixed positive tangential spectral parameter p. This is an explicit continuum-limit fixture; it is not a derived embedding of the full native 3+1+1 structure. Its exact on-site resolvent, with physical normal-momentum normalization, is

    G_ell(p)= int_{-pi/ell}^{pi/ell} dk/(2pi)
       [p^2+4/ell^2 sin^2(ell k/2)]^(-1)
       =1/[p sqrt(4+ell^2 p^2)].                           (B4)

Derivation: put q=ell k and use the elementary integral of 1/(a-b cos q). The calculation is independently checked by numerical quadrature.

Consequently

    8 pi G_N G_ell(p)
       = (4 pi G_N/p) [1+ell^2 p^2/4]^(-1/2).             (B5)

For fixed p as ell->0 this is exactly B3. Its first relative correction is

    -ell^2 p^2/8 + O(ell^4 p^4).                           (B6)

Finite spacing is NOT exactly the continuum response at all momenta. No experimental prediction or Planck-scale identification follows until ell, clock conversion, couplings, and the tensor projection are physically fixed.

This resolves one potential confusion: a nonlocal surface response can coexist with local bulk field equations. It is compatible with the Time Shell acting as an interface instead of being confused with the full spacetime. Standard GR's linearized spin-2 structure is described in [R2]; B2–B6 here prove only the scalar-response part.

## 7. A nonlinear ER–helicon branch with explicit backreaction

This section is NEW MODEL DEVELOPMENT under the user's full-agency instruction. It is not attributed to the original manuscript. Its aim is to supply a coherent native-depth dynamical candidate while leaving the graph physical, rather than replacing it with the GRC-1 encoding.

### 7.1 Local edge-amplitude version

For a fixed allowed edge set, introduce retained real amplitudes r_e,n and set off-diagonal weights W_e,n=r_e,n^2. Nonnegative weights follow identically. Self-weights remain separate. The r variables are additional branch data; their sign history at zero crossings is not reconstructed from W by fiat.

Define the discrete action

    S = sum_n [ 1/2 ||H_(n+1)-H_n||^2
                + sum_e I_e/2 (r_e,n+1-r_e,n)^2
                - V(H_n,r_n) ],

    V(H,r)= c_A^2/2 sum_{e=(i,j)} r_e^2 (H_i-H_j)^2
             + sum_e nu_e/4 (r_e^2-r_e,*^2)^2,              (D1)

with I_e>0, nu_e>=0. The equations are

    Delta_n^2 H + c_A^2 L(r^2)H=0,
    I_e Delta_n^2 r_e + c_A^2 r_e(H_i-H_j)^2
                      + nu_e r_e(r_e^2-r_e,*^2)=0.         (D2)

The first is exactly the recovered recurrence for the instantaneous graph; freezing r recovers the source's fixed graph. The second supplies backreaction rather than treating changing weights as external parameters. The potential is nonnegative. It is not a proven global stability theorem for the finite-step dynamics.

The two-step update is explicitly invertible: q_(n-1)=2q_n-q_(n+1)-M^(-1)grad V(q_n), for q=(H,r) and the positive diagonal inertial matrix M. In canonical kick–drift coordinates the map is symplectic. The report does not claim exact energy conservation for this nonlinear fixed-step integrator. The fixed-W invariant N3 does not survive unchanged when W changes.

Uniform shifts H->H+c1 leave V invariant, and sum_i H_i has zero second difference. This preserves the native constant mode. It does not prove Lorentzian masslessness.

General edge changes can mix previously selected spectral subspaces. Consequently D2 alone does not meet every archived gravitational-projector preservation condition. This is an identified issue, not suppressed.

### 7.2 A mode-preserving coherent breathing branch

A particularly useful controlled branch avoids this mixing. Fix the physical graph shape W0 and its Laplacian L0. Let a_n be one retained collective amplitude for a coherent finite foam patch:

    W_ij(n)=a_n^2 W0_ij   (i!=j),
    L_n=a_n^2 L0,

while retaining the specified self-weights. This does not identify W0 with canonical GRC-1 weights.

Use

    V(H,a)=c_A^2 a^2 H^T L0 H/2 + nu(a^2-a_*^2)^2/4.      (D3)

The exact coupled recurrence is

    Delta_n^2 H + c_A^2 a_n^2 L0 H_n=0,
    I_a Delta_n^2 a_n + c_A^2 a_n H_n^T L0 H_n
                       +nu a_n(a_n^2-a_*^2)=0.             (D4)

This supplies two-way ER/mode feedback and an explicit reversible update. Every fixed spectral projector P of L0 commutes with L_n. If two initial H states lie in its image, all subsequent H states do too. Thus a previously admitted spectral sector is retained without declaring its complement physically irrelevant. This invariant-subspace statement is weaker than commutation of the complete nonlinear backreaction map with a projector on arbitrary extended states: the breathing equation itself depends on the occupied amplitudes. The full archived correction-algebra condition is not established by this step. The identification of that P with the actual gravitational-helicon/TT sector is still a separate source obligation.

The shape restriction is substantial: it describes a coherent breathing patch, not arbitrary topology changes, independent edge rearrangements, or microscopic locality of a globally shared collective variable. It is a controlled new branch, not an assertion that all ER foam has only one degree of freedom.

At a=0, off-diagonal weights vanish and a uniform stationary H gives a fixed state, compatible algebraically with identity-like adjacency when self-weights are one. Its stability depends on the potential; if a_* is nonzero, a=0 is an unstable stationary point. No cosmological bounce, nucleation mechanism, or original white-core physics is inferred.

### Nonlinear stability warning

Even if each instantaneous eta_n lies in (0,4), a varying sequence can have parametric instability. For one mode alternate eta=1/2 and eta=7/2. Each fixed recurrence is oscillatory, but the two-step transfer has determinant one and trace -17/4, so one Floquet multiplier has modulus greater than one.

This sequence is a counterexample to an incorrect stability criterion, not asserted to be a trajectory of D4. A nonlinear stability proof for the coupled branch remains open. All executions in this report are finite tests, not global guarantees.

## 8. The changing-foam Time Shell retains ordered History

For an arbitrary retained graph history W_n, let B_n=2I-c_A^2 L_n. Put Y_n=(b_n,b_(n-1)), and define

    F_n=[[B_ii,n,-I],[I,0]],
    G_n=[[B_is,n],[0]],
    D_n=[B_si,n,0].

The interior recursion is

    Y_(n+1)=F_nY_n+G_ns_n

for zero drive. With ordered products

    Phi(n,k)=F_(n-1)...F_k,

its exact solution is

    Y_n=Phi(n,1)Y_1
          +sum_{k=1}^{n-1}Phi(n,k+1)G_k s_k.               (H1)

Therefore the shell has a two-time kernel

    K(n,k)=D_n Phi(n,k+1)G_k.                              (H2)

This is generally not a function of n-k. Matrix order matters when the graph changes. The calculations reproduce both a prescribed noncommuting graph history and the graph history generated by the new nonlinear breathing action.

For coupled dynamics the graph history is NOT an unexplained external oracle: it must be evolved by its retained equations, or supplied as a recorded history. H1–H2 do not by themselves recover that graph history from shell observations. Eliminating it as well produces a nonlinear history functional, not the fixed linear convolution in T3.

This supplies a concrete reason to preserve History in the interface, while keeping archival history and dynamical state mathematically distinct.

## 9. The actual obstruction to full model completion

The computations reach the native modal dynamics and their exact shell response. They do not yet reach a derivation of the full spacetime metric and Einstein equations from the protected upstream model.

### 9.1 Tensor geometry and polarization

The original source requires a tensor/TT restriction before readable graviton projection, but a scalar graph Laplacian does not determine an embedding of its nodes into a Lorentzian tangent bundle, a spin-2 polarization structure, or diffeomorphism constraints. Supplying two copies of an oscillator is not a derivation of helicity two.

A concrete negative control is useful. For a spatial wavevector k, let P=I-kk^T/k^2 and define the usual TT projector on symmetric tensors. The tempting map h_ij=k_i H_j+k_j H_i satisfies

    TT(h)=0.

Thus simply taking a symmetric gradient of the helicon one-form cannot manufacture a radiative transverse-traceless gravitational mode. This particular map is NOT attributed to the source. The test explains why a real tensor handoff, rather than a label, is essential. The actual source has richer continuity/tensor structure that must be evaluated.

### 9.2 Clock and dimensions

n remains native update depth. A clock t(n), spatial continuum limit, and dimensional normalization are required before a native dispersion becomes a measured frequency. The normal direction in B2 is in a specified readable bulk; it is not the native fifth organizational coordinate. No native dimension has been deleted or quietly identified with ordinary time.

### 9.3 Nonlinear gravitational action and sources

The original nonlinear continuity fixed point is retained unchanged in evidence. Neither the exact boundary kernel nor the new native-depth action proves it equals Einstein–Hilbert dynamics. Matching the scalar propagator is necessary evidence for one linear response, not sufficiency for nonlinear GR.

The localized-knot branch, its matter readout, phase/chromatic action reconciliation, universal coupling, and full stress tensor must also match. No graph drive J has been relabeled T_munu. The previous action-derived matter results remain usable, but their original variants have not been overwritten.

A legitimate nonlinear boundary comparison can use an explicitly defined gravitational action and its induced boundary stress/response, as in the Brown–York construction [R3]. That provides a target interface, not a derivation of the native action. Timelike boundary data alone do not come with an automatic unique bulk completion. Initial data and well-posedness hypotheses still matter.

### 9.4 Role of GRC-1

If and when the Time Shell outputs a metric and the matched matter description, GRC-1 can encode that output reversibly. It does not supply the original ER foam, the native Time Shell, or the missing tensor/clock map. The native W and representation weights W_code remain different objects. This integration has not replaced the original matter action with the free-scalar completion.

## 10. What the work now earns

**Source-derived and proved for the stated finite sector:** the modal recurrence's action realization; exact initial-value shell memory; a full return map with retained initial data; a shell-history inverse precisely when the observation matrix is injective; Schur response and controlled low-frequency expansion; native zero-mode preservation under static elimination.

**New and explicitly proposed:** a local edge-backreaction action and a coherent breathing-foam action. Both are implemented with reversible updates. The breathing branch preserves fixed spectral subspaces. Their physical identification with the complete upstream model, full stability, tensor content, and empirical applicability are not established.

**A new compatibility calculation:** the source's inverse-square-root scalar shell kernel is exactly a normal-momentum restriction of a massless bulk response, and an explicit ER-chain resolvent reaches it in a declared continuum scaling. This removes a potential false incompatibility; it does not prove the complete spin-2 kernel or the native dimension/clock map.

**Still unresolved:** complete Genesis/Resolution/Bandwidth generation of the selected graph and boundary, helicon subtype admission, covariant tensor Time-Shell map, physical clock, native nonlinear Einstein action/source correspondence, physical inverse without hidden-state loss, quantum extension, and experiments.

The first unresolved physics gate is therefore specific: construct the admitted ER/helicon tensor boundary data and their clock/geometry readout so the full response and nonlinear constraints are those of the intended GR sector. It is not honest to call the graph-memory result itself a full solution of MK Ultra.

## 11. Executed verification

Run:

    python code/checks.py

The recorded suite contains 48 named checks. Three of them compare forced full-network and memory-reconstructed trajectories at different graph sizes. It also checks exact symbolic Schur inversion, the native invariant, symplecticity, history observability and dark modes, noncommuting graph histories, continuum and lattice boundary integrals, the new nonlinear variational terms, reversible backreaction, preserved spectral sectors, the parametric-instability negative control, and the TT symmetric-gradient negative control.

Checks that reject an invalid shortcut count as passing checks of the analysis, NOT evidence that the shortcut works. Numerical tolerances, symbolic conventions, and scope are recorded in `results/CHECK_RESULTS.json`. The general statements rely on the explicit derivations above, not on finite tests alone.

## References

**Primary user sources:** exact passages S01–S08, original canonical Markdown, and the two extracted Time-Shell notes are under `evidence/`. Extraction paths and hashes are recorded. Source content is not silently reconciled.

**External mathematical background, retrieved 31 October 2026:**

R1. A. Gouasmi, E. J. Parish, K. Duraisamy, *A priori estimation of memory effects in reduced-order models of nonlinear systems using the Mori–Zwanzig formalism*, Proc. R. Soc. A 473 (2017), 20170385. https://pmc.ncbi.nlm.nih.gov/articles/PMC5627381/ . Exact elimination and its computational limitations, not a claim about MK Ultra.

R2. D. Tong, *General Relativity*, Section 5, *When Gravity is Weak*. https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S5.html . Linearized Einstein tensor, gauge invariance, and transverse-traceless propagation. Our scalar boundary integration does not replace those tensor requirements.

R3. J. D. Brown and J. W. York, *Quasilocal Energy and Conserved Charges Derived from the Gravitational Action*, arXiv:gr-qc/9209012; Phys. Rev. D 47 (1993) 1407. https://arxiv.org/abs/gr-qc/9209012 . A primary reference for action-derived boundary stress, not an assumed native-shell identification.

No novel-science priority, complete unification, global nonlinear stability, native quantization, or independent experimental validation is claimed.
