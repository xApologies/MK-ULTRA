# Chirality, Rainbow Road, Native Energy and Mass
## Source-grounded bridge into the Time Shell

**Date:** 31 October 2026  
**Status:** Source recovery plus exact algebraic consequences; proposed interface tests are distinguished from established identities. No complete gravity model, physical calibration, or native-to-GR equivalence is asserted.

## 1. Determination

The supplied sources help materially. They already connect Native Energy and Native Mass through the same Persistence functional. Rainbow Road supplies a native, History-bearing path language on which that connection can be evaluated. A new physical definition of energy or mass is not needed to establish the scalar relation.

The exact source identity is:

    Energy_lock(H4) = Mass_MK([X]) / epsilon_P = mu_MK([X]),

conditional on an admissible lock-formation history from the native vacuum to P4_lock(X). This is a definitional identity, not an independently derived numerical prediction in joules and kilograms. It does not assert all energy is mass.

The next useful construction is the source-current attachment from these native quantities, together with transport and orientation data, to the Time Shell. The scalar identity does not by itself construct a spacetime metric, tensor source, physical clock, or spin-2 sector.

## 2. Sources and version boundaries

Primary sources used:

1. Uploaded API 4.3 archive, `4.3(20261031-233418).zip`, canonical Markdown at `MK43_Ultra_API_FULL_CURRENT/MK43_Ultra_API_CURRENT_CANONICAL.md`. RP-30.6–8 defines Persistence, its native increment, and General Energy. The canonical text has SHA-256 `0071c1d9d6a89c283f57a9c225857fa8f49a63f8caff86d83cca4a66896b0259`. Exact line-numbered excerpts accompany this note.
2. `_mass_b(4).txt`, internally version 3.0, T4/T5 Pipeline Closure. This is the version used for the corridor-specific equations here. D6 defines Native Mass, D9 its normalized number, D12 the T5 correction, D13 history energy, L11/T6 their lock-formation correspondence, and R2 the Time-Shell gravitational source condition.
3. `_mass 2(4).md`, internally version 1.1, supplies the earlier lock-filtered history functional, faithful Time-Shell mass translation, and a separate mode-dispersion correspondence. Its mass unit is defined from the minimum positive locked-mass spectrum. That unit is NOT silently identified with the minimum positive general persistence increment. Version 3 explicitly uses the shared inherited epsilon_P, so it is the normalization used here.
4. `_mass(3).md`, internally version 1.0, is retained as an earlier version, not silently merged. Among the differences, it uses Omega for the vacuum; the later versions reserve Omega for Chirality Space and use 0_E for vacuum.
5. `FINAL(1).pdf`, internally Director Recovery Edition v7, 27 September 2026, especially sections 11–12 and 15–18. It explicitly leaves the mature Rainbow Road/chirality correspondence and source-current tensorization open. Its status labels are recorded source claims, not a new validation of every earlier theorem.
6. Live `_bricked` repository, default branch `bootstrap/canonical-architecture`: `genesis_mathematics/v3.0/FORMAL/47_RAINBOW_ROAD_INFORMATION_TRANSPORT.md` (Git blob `00776e90e4ab5f8f73d02f6d9f1bf5e627f60f97`) and `53_CHIRALITY_AS_ORDERED_GEOMETRY.md` (Git blob `ce87dac949877e48a80e9860cad3d0a0330e184a`). Their bytes are preserved and Git-blob hashes checked.

The live repository lookup establishes that Rainbow Road is not confined to its computer-science use. Chapter 47 states its payload-independence: physical, computational, or other interpretations do not change its native transport role. Chapter 53 defines chirality as domain-relative oriented identity structure, not merely a two-valued physical handedness.

The older Rainbow Road live model recovered from an earlier checkpoint was inspected as an archival comparator but is not used to supersede the current chapters or imported into this derivation.

## 3. Keep the types distinct

Use P(X) = Pers([X]) as short notation. Let L(X)=Pers([P4_lock(X)]), and v=P(0_E). In the supplied normalization v=0; retaining v makes the cancellation explicit.

    M4(X) = L(X) - v.
    mu4(X) = M4(X) / epsilon_P.

For an admissible ordered history H: X0 -> ... -> Xn:

    E_hist(H) = [P(Xn)-P(X0)] / epsilon_P.

These are different mathematical types: M4 is a scalar on a mass-admissible identity class; E_hist is a signed scalar assigned to a history. The source calls the latter Native Energy. Its formula specifically measures a net Persistence difference, not an arbitrary time-evolution generator or an independently supplied relativistic energy inventory.

For histories whose endpoints are in the lock domain, the lock-filtered functional, inherited from version 1.1 and here evaluated with version 3's selector/unit, is

    E_lock(H) = [L(Xn)-L(X0)] / epsilon_P.

This filtered evaluation does not assert that applying P4_lock to every intermediate state gives an admissible Rainbow Road path. That is an additional operation-compatibility question.

## 4. Exact energy–mass identities

### 4.1 General locked change

Subtracting the two mass evaluations cancels the fixed vacuum:

    M4(Xn)-M4(X0) = L(Xn)-L(X0) = epsilon_P E_lock(H).   (1)

Equation (1) is the finite energy–mass correspondence. No metric on chirality coordinates, continuum limit, or derivative is needed.

### 4.2 Lock formation

For a source-admissible H4: 0_E => K, with K=P4_lock(X) and P4_lock(K)=K,

    E_hist(H4) = E_lock(H4) = M4(K)/epsilon_P = mu4(K).   (2)

This is L11/T6 in the supplied version-3 manuscript. The formula does not prove that every lock is reachable from vacuum, or that formation occurs spontaneously. The existence of the relevant formation history, its environmental input, and full-system conservation are separate obligations.

### 4.3 Not all Persistence change is locked change

Define only for bookkeeping

    R_unlocked(X) = P(X)-L(X).

Then exactly

    epsilon_P E_hist(H)
      = [M4(Xn)-M4(X0)] + [R_unlocked(Xn)-R_unlocked(X0)]. (3)

No nonnegativity, kinetic-energy interpretation, or independent dynamical law for R_unlocked is asserted. The sources do not require P4_lock to be a contraction of the scalar P. This identity simply prevents confusing total and lock-filtered changes.

### 4.4 T4 to T5

Take a non-vacuum T4 knot K and a T5 state Y=Form5(K), with Core5(Y)~K. Version 3 defines

    M5(Y)=P(Y)-v,
    M_core(Y)=M4(Core5(Y))=M4(K),
    DeltaM_shell(Y)=M5(Y)-M_core(Y).

For an admissible formation history H5: K => Y,

    epsilon_P E_hist(H5)
      = P(Y)-P(K)
      = M5(Y)-M4(K)
      = DeltaM_shell(Y).                                    (4)

Equation (4) is a new explicit consequence of the source definitions. It relates the T5 shell-and-relation correction to the signed native change through formation. A persistent core can survive while that correction changes. The source permits positive, zero, or negative correction.

This uses M5, not an unproved identity P4_lock(Y)=Core5(Y). Nor does it identify the set Shell5(Y) with the full Time-Shell projection operator Pi_T. Native core–shell organization and the entire gravitational interface remain different typed objects until their attachment is established.

## 5. Rainbow Road is the correct path carrier

The current repository defines

    RR_(D,B) = Path(Gen_D(B)),
    gamma = a_n o ... o a_1,
    H(gamma)=(a_1,...,a_n).

To evaluate a route physically, each generator must have an admitted action U_a on the selected organizational states, with source/target types and Resolution/Bandwidth restrictions respected. RR supplies admissible path structure; it does not supply every domain-specific U_a merely by naming it.

Once those actions are given, define the edge increments

    e(a;X) = [P(U_a X)-P(X)]/epsilon_P,
    e_lock(a;X) = [L(U_a X)-L(X)]/epsilon_P.

They compose by telescoping:

    E_hist(gamma2 o gamma1)=E_hist(gamma1)+E_hist(gamma2),
    E_lock(gamma)= [M4(X_end)-M4(X_start)]/epsilon_P.

This is an additive path functional; in ordinary mathematical metalanguage it is the coboundary of a state potential. This mathematical terminology is not a new physical primitive.

A closed path has zero net E_hist if its endpoint Persistence equals its initial Persistence. This does NOT make its native organization energyless, its transport trivial, or its full History recoverable from the scalar value. The path word and chirality transport must be retained.

For comparison, the reference-relative quantity

    U_P(X)=[P(X)-P(0_E)]/epsilon_P

obeys E_hist(H)=U_P(X_end)-U_P(X_start). U_P is introduced here only as a useful bookkeeping inventory; no identification with a Hamiltonian or physical energy has been derived. For a nonzero fixed lock it equals mu4 and can be nonzero while an identity-preserving history has zero net E_hist.

## 6. What a derivative with respect to chirality can mean

Chirality is a structured object. It is not automatically a real coordinate, so an unrestricted symbol dE/dchi would conceal typing assumptions.

For an admitted Rainbow Road generator a acting on X, use the unnormalized finite directional difference

    delta_a M4(X)=M4(U_a X)-M4(X).

Then the exact result is

    delta_a M4(X)=epsilon_P e_lock(a;X).                     (5)

If an actual domain-specific positive corridor length d_chi(a;X) has independently been defined, one may normalize both sides:

    D_a M4 = delta_a M4 / d_chi(a;X)
           = epsilon_P e_lock(a;X)/d_chi(a;X).              (6)

Equation (6) is conditional on that length. ER site distance is not silently repurposed as a distance between whole organizational states. A smooth derivative requires an admitted smooth family and limit; it is not needed for (5).

The source supplies chi(I X)=tau_chi(chi(X)) for inheritance. This proves the corresponding law for repeated inheritance by induction. For general RR generators, the needed chirality-transport test is

    chi(U_a X)=V_a^chi(chi(X))                               (7)

on each generator's admitted domain. If (7) holds and the actions compose, it follows for every finite route. This is a sufficient compositional theorem, not a claim that every original generator has passed it.

Likewise, to regard Mass as a function of a chirality readout alone requires

    chi(X)=chi(Y) => M4(X)=M4(Y)

on the stated domain. The full chirality-bearing state may carry sufficient information even when a reduced label does not. Neither a color label nor handedness by itself is substituted for the full state.

### Exact factor response

The source's Persistence profile uses I_d B_d R_d O_d C_d. For the two selected lock states, an exact finite product identity at any depth is

    Delta(IBROC)
      = (Delta I) B R O C
      + I' (Delta B) R O C
      + I' B' (Delta R) O C
      + I' B' R' (Delta O) C
      + I' B' R' O' (Delta C).                              (8)

Summing the product differences gives the mass change, with fixed vacuum. This does not assume infinitesimal calculus. The attribution to individual terms depends on the chosen telescoping order; it is not a unique causal decomposition. For infinitely many active depths, the total difference is well-defined from summability, while interchanging/splitting infinite sums into the five separate terms needs additional convergence control.

## 7. The readable mass–energy test

The source's faithful mass translation T_m preserves zero, reflects zero and is strictly increasing. Those conditions do not force linearity or determine the readable energy map.

Let T_E translate the relevant reference-relative lock-energy count to readable rest energy. The required compatibility test is

    T_E(M4(K)/epsilon_P) = c_shell^2 T_m(M4(K)).              (9)

Here c_shell must be the same invariant causal-speed normalization supplied by the readable Time-Shell geometry. Equation (9) is not deduced from the scalar identities alone.

Under an explicitly linear unit convention,

    m_read=m_* mu4,
    E_rest=E_* mu4,

so E_rest=(E_*/m_*)m_read. The physical match requires E_*/m_*=c_shell^2. This is a calibration/realization condition, not a derivation of the speed of light from the dimensionless native normalization.

For differences between two locks, the desired readable test is

    E_rest(K2)-E_rest(K1)=c_shell^2[m_read(K2)-m_read(K1)].    (10)

A scalar translation of the net difference alone commutes with all such subtractions only with appropriate additivity. For a general nonlinear T_m one must compare the two endpoint readouts, not replace their difference by T_m(Delta M).

A useful independently evaluable defect is

    D_rest(K)=E_shell,rest(K)-c_shell^2 T_m(M4(K)).            (11)

The source gives the mass side. It has not yet independently supplied all of the energy/clock readout required to evaluate (11) physically. Defining T_E solely to make (9) true establishes a convention, not independent physical confirmation.

**External target only:** conventional relativistic energy obeys E^2=p^2 c^2+m^2 c^4 for a particle, with E_rest=mc^2 when p=0. This is used here as the comparison target, not inserted as a native definition. See David Tong, Dynamics and Relativity, section 7.4.3, printed p.137 (PDF page 31), viewed and visually checked on 31 October 2026.

## 8. The separate spectral check

Version 1.1 states, on simultaneous mass/ER eigenmodes,

    4 sin^2(omega/2)=c_A^2 lambda_alpha+mu_alpha^2.

Writing e_spec=2|sin(omega/2)| gives an algebraic mass-shell-shaped identity. It does not identify e_spec with E_hist(H). An oscillatory history can have zero net Persistence change over a cycle while possessing nonzero frequency. A physical frequency, energy and momentum readout still needs the declared clock and calibrations. Native update depth is not automatically readable time. Version-1.1's normalization must also be reconciled explicitly before identifying its mu with version-3 mu4.

This gives a separate compatibility test for helicon propagation and the retained lock invariant; it is not permission to collapse spectral energy and history energy into one symbol.

## 9. The Time-Shell attachment already named in the source

Version 3, R2, states for an isolated lock in its readable rest organization:

    Source_ER([K])=T_m(M4([K])).                              (12)

The director report separately preserves the original gravity route

    ER foam -> helicon -> gravitational helicon mode -> graviton
    -> continuity perturbation -> Time-Shell projection
    -> readable metric perturbation,

with

    Pi_T(delta C)=h_munu,
    g_munu=gbar_munu+h_munu.

The source-current construction is explicitly a candidate:

    locked Persistence -> rest/energy density,
    propagation and redistribution -> momentum/energy flux,
    corridor strain and closure response -> stress,
    Theta_G: J_G -> T_G.

A proposed source tensor must satisfy the rest-mass test (12), energy calibration (9), and the appropriate transport/conservation tests, not merely a convenient Einstein-tensor definition.

The scalar source constraint does not determine all of T_G. Even two symmetric tensors with the same rest-frame 00 component can have different spatial stresses. RR can retain the directions, order, and transport context needed to attempt this extension, but its payload-independence is not itself a Lorentzian four-momentum or tensorization theorem.

A useful record to carry along a route is the full admitted state/History plus chi transport, ER data, Persistence profile, selected lock, M4, and the signed increments. This is a bookkeeping proposal using existing source objects, not a new physical ontology. It should feed the existing Time-Shell/source interface, not replace the microscopic network with GRC-1 metric-code weights.

## 10. Result and boundary

Established from the supplied definitions:

- the conditional lock-formation identity;
- exact locked-energy/mass differences on admitted routes;
- composition by telescoping;
- a general total-versus-locked accounting identity;
- the T4-to-T5 shell-correction identity;
- the exact finite factor-difference formula.

Verified from the live mathematical repository: RR is native History-bearing, payload-independent information transport; chirality is ordered domain-relative identity structure.

Not established:

- evaluation of every native corridor map on arbitrary raw states;
- the general mature RR/chirality transport witness;
- all numerical mass and energy calibrations or physical c;
- identification of net history energy with every use of physical energy;
- full source-current tensorization, the nonlinear Time-Shell realization or complete GR equivalence.

The important change in direction is substantive: the mass and energy attachment is already anchored in native Persistence and ER closure. The new task is to make those readouts commute through the retained chirality/transport and Time-Shell maps, not invent a replacement matter action or remove the foam.

## 11. Reproducibility and source integrity

Run `python code/checks.py`. The fifteen checks cover the displayed algebra and expressly labeled examples, not physical predictions or a numerical implementation of the original operators. Exact source files and excerpts are preserved under evidence/. Source hashes are recorded in PROVENANCE.json and MANIFEST.json. Integrity checking and mathematical or empirical validation remain different claims.

External comparison references:

- David Tong, *Dynamics and Relativity*, Special Relativity, section 7.4.3: https://www.damtp.cam.ac.uk/user/tong/relativity/seven.pdf
- David Tong, *General Relativity*, section 4.5: https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S4.html

These external sources support only the conventional readable target; they do not fill the project's missing native maps.
