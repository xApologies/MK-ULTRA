# AERA Reconciliation 020 — Genesis GR dark-energy correspondence
Date: 2026-10-28. Authority: `AUTHORITIES/GENESIS_GR_DROPIN_v1.2.1/GENESIS_GR_13_POINT_COMPLETE.md` and its audit. Earlier dark-energy live model and original Chat 00 source are preserved in this archive.

## Source-derived mathematical objects
The audited Genesis GR v1.2.1 defines native metric `mathfrak g_G`, Einstein curvature `mathfrak E_G`, source `mathfrak T_G`, cosmological term `Lambda_G`, coupling `kappa_G`, and readout `rho_G` with:

`mathfrak E_G + Lambda_G mathfrak g_G = kappa_G mathfrak T_G`

`rho_G(mathfrak E_G)=G_mu nu`, `rho_G(mathfrak T_G)=T_mu nu`, `rho_G(Lambda_G)=Lambda`, `rho_G(kappa_G)=8 pi G/c^4`, `rho_G(mathfrak D_G mathfrak T_G)=nabla_mu T^mu nu=0`.
The native source is a refinement density of witnessed four-momentum transfer, `dP_G^a=mathfrak T_G^{ab}dSigma_b`. The package gives the correspondence *type* but does not uniquely compute a dark-energy-specific native source from Chirality and Persistence.

## Exact conditional GR readout / avoid double counting
Signature (-+++); `epsilon_A` is physical energy density (J/m^3). For the coherent-shell regime, impose the inherited **vacuum-like observable correspondence** `p_A=-epsilon_A`, constant `epsilon_A>0`, and FLRW homogeneity/isotropy. This is an adopted correspondence, not deduced from the native chirality operators.

**Option A: geometric Lambda placement (preferred canonical representation):**
`mathfrak E_G+Lambda_G mathfrak g_G=kappa_G mathfrak T_G^(ordinary)`.
Readout: `G_mu nu+Lambda g_mu nu=(8 pi G/c^4) T_mu nu^(ordinary)`.

**Option B: vacuum source placement (equivalent representation):**
`mathfrak E_G=kappa_G[mathfrak T_G^(ordinary)+mathfrak T_G^(A)]`, where `rho_G(mathfrak T_G^(A))=-epsilon_A g_mu nu` and `Lambda=8 pi G epsilon_A/c^4`.
This assumes a native preimage/lift of the vacuum-like tensor exists in the admissible source domain. The source document does not construct a unique such lift. If `rho_G` is not injective, any two lifts differ by a readout-kernel element. Existence, gauge choice and native physical selection are OPEN.
**Never** retain both `Lambda_G` on the left and the identical `mathfrak T_G^(A)` on the right unless subtracting one copy.

## Effective energy-volume relation
For a homogeneous coherent-shell comoving physical volume `V(a)=V0 a^3` with `a_today=1`, effective vacuum energy is `E_A(V)=epsilon_A V` and pressure `p_A=-epsilon_A`. This follows from the inherited vacuum-like equation of state plus local GR conservation; it is not a unique Genesis Persistence scaling theorem. Native history energy and mass-lock persistence are distinct from `E_A`.

## Effective observable H(z)
In the inherited flat FLRW readout with noninteracting radiation and matter:
`H_A(z)=H0 sqrt[Omega_r(1+z)^4+Omega_m(1+z)^3+Omega_A]` with `Omega_A=1-Omega_r-Omega_m`.
This reproduces standard Lambda-CDM by construction and is *not* an independent prediction or likelihood fit. It is defined only while the Time Shell remains coherent.

## Structural termination / nucleation
Retain Chat 00's original elastic binding `rho_bind(a)=K_eff(a-a0)^2/a^3`, bead spacing `a_spacing=a0 ell_max/ell0`, and historical nucleation thresholds, as recorded in `LIVE_MODEL/`. `rho_bind` is a structural stability diagnostic, **not** the physical vacuum density `epsilon_A/c^2` unless an independent dimensional/physical correspondence is supplied. On the late stable branch, failure occurs at the first admissible binding/spacing threshold; the corresponding `z_f=1/a_f-1` is a model parameter, not currently measured. AERA does not require `H(z_f)=0` or a Big Crunch.
Beyond that boundary the FLRW effective description terminates; the source package does not uniquely prescribe a distributional stress tensor or a smooth spacetime junction to ER foam / White-State Core. Do not extrapolate Einstein GR through the boundary without a defined matching construction.

## Closure classification
**Closed as a conditional effective model:** Genesis GR-to-Einstein GR correspondence (inherited v1.2.1), two equivalent dark-energy placements, vacuum stress-energy, local conservation, H(z), algebraic shell endpoint.
**Not independently derived:** uniqueness/existence of dark-energy native source lift, microscopic Genesis chirality-to-vacuum equation of state, native stress tensor during dissolution, observed deviation from LCDM, numerical time-to-failure, physical recurrence. These are explicit research obligations, not reasons to rewrite Chat 00.
**Verdict:** full effective coherent-shell model completed under stated assumptions; fundamental native dark-energy derivation and independent observational validation remain open. The mathematically significant new audit result is that source-vs-Lambda placement must be exclusive to avoid double counting.
