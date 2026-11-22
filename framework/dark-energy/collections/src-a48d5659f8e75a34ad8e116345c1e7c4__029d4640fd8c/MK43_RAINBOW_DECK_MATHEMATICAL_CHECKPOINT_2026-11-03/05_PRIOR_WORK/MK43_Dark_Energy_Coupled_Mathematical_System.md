# MK43 Ultra — Coupled Dark-Energy Mathematical System
**Mathematical construction, 2026-11-02.** Gravity and Genesis↔GR are inherited, not re-derived. This is a conditional mathematical model, not a proof of a microscopic neon mechanism.

## 0. Definitions and domain
The sole neon readout is **ν = 𝓦(Ψ_N)**, selected once at nucleation, 0<ν<1. Individual rainbow/neon configurations are not reconstructed. Work on the post-nucleation homogeneous/isotropic coherent FLRW branch, with a(t)>0 and a(today)=1. The native nucleation boundary at exactly a=0 is not asserted to be described by FLRW.

The model's **explicit physical postulates** (not consequences of the existing graviton theorem) are
ε_DE(ν)=ν ε_ref, p_DE=−ε_DE, and ρ_threshold(ν)=ν ρ_ref,
with fixed physical reference scales ε_ref and ρ_ref. This selects the constant-vacuum branch, so dark-energy density is constant while the fractional contribution to expansion evolves. Other dark-energy histories require a different source postulate.

## 1. Homogeneous background (inherited GR)
Define H=ȧ/a and physical energy densities ε_i, with c explicit.
H² = (8πG/3c²)(ε_r+ε_b+ε_c+ε_DE) − kc²/a²;
ä/a = −(4πG/3c²) Σ_i(ε_i+3p_i).
Conservation for separately conserved components:
ε̇_i+3H(ε_i+p_i)=0.
p_r=ε_r/3, p_b≈p_c≈0, p_DE=−ε_DE.
Thus ε_r=ε_r0 a⁻⁴, ε_b=ε_b0 a⁻³, ε_c=ε_c0 a⁻³, ε_DE=ν ε_ref.
For the flat branch k=0:
H²(a;ν)=(8πG/3c²)[ε_r0 a⁻⁴+(ε_b0+ε_c0)a⁻³+ν ε_ref].
a(t) is determined by ȧ=aH(a;ν) and the chosen positive-a initial slice. Cosmic time between two positive scale factors:
t(a₂)−t(a₁)=∫[a₁,a₂] da/(aH).
A one-input prediction requires all other background and microphysical constants to be fixed independently of ν.

## 2. Thermal history, photon/baryon coupling, neutrinos
T_γ(a)=T_γ0/a prior to entropy-release corrections; in general use comoving entropy conservation g_*S(T) T³ a³=constant.
Radiation density ε_r(T)=(π²/30)g_*(T)(k_B T)⁴/(ℏ³ c³) (natural conventions: ε_r=π²g_*T⁴/30).
Photon phase-space f_γ evolves via the covariant Boltzmann equation
p^μ ∂_μ f_γ − Γ^i_{αβ}p^αp^β ∂f_γ/∂p^i = C_Thomson[f_γ,f_e].
For neutrinos, the same Liouville operator equals the weak-interaction collision term C_weak; after decoupling it is collisionless. These equations fix the thermal/kinetic sector; no values of ν are inserted into reaction rates.
Charge neutrality: n_e=n_p (plus ion contributions where appropriate). Baryon number conservation: n_b a³=constant.

## 3. Recombination and CMB visibility
The electron ionization fraction x_e(z) follows the full atomic kinetic system, schematically
dx_i/dt=Σ_j[x_j R_{j→i}(T,n_e,J_ν)−x_i R_{i→j}(T,n_e,J_ν)],
subject to charge neutrality, detailed balance where applicable, and a specified atomic level network.
Thomson optical depth: τ(η_c)=∫[η_c,η_c0] a n_e σ_T c dη_c, where η_c is **conformal time**, NOT the neon parameter ν or baryon-to-photon ratio η_b.
Visibility: g(η_c)=−τ'(η_c)e^(−τ(η_c)) for τ' = dτ/dη_c < 0.
Sound speed c_s²=c²/[3(1+R)], R=3ρ_b/(4ρ_γ).
Sound horizon r_s(z)=∫_z^∞ c_s(z')/H(z') dz'.
The baryon-drag sound horizon r_d is r_s evaluated at the baryon-drag epoch defined by its momentum-transfer optical depth, not an independently fitted distance constant.

## 4. Linear Einstein–Boltzmann perturbations (inherited physical equations)
Choose conformal Newtonian gauge:
ds²=a²(η_c)[−(1+2ψ)dη_c²+(1−2φ)δ_ij dx^i dx^j].
For Fourier mode k and conformal Hubble rate ℋ=a'/a, the linearized Einstein constraints include
k²φ+3ℋ(φ'−ℋψ)=4πG a² δT⁰₀/c⁴ [with sign conventions fixed by δT⁰₀];
k²(φ'−ℋψ)=4πG a²(ρ+p)θ/c⁴ [up to the adopted velocity normalization].
**Important:** exact signs and c factors must be fixed together with the metric/δT conventions; do not mix gauge conventions.

For a perfect pressureless component in a standard conformal-time convention:
δ_c'=−θ_c+3φ',  θ_c'=−ℋθ_c+k²ψ.
For photons (with optical depth derivative κ̇=a n_e σ_T c>0):
δ_γ'=−4θ_γ/3+4φ',
θ_γ'=k²(δ_γ/4−σ_γ)+k²ψ+κ̇(θ_b−θ_γ).
For baryons:
δ_b'=−θ_b+3φ',
θ_b'=−ℋθ_b+c_b²k²δ_b+k²ψ+(4ρ_γ/3ρ_b)κ̇(θ_γ−θ_b).
The photon and neutrino multipole hierarchies extend to all ℓ, including anisotropic stress, polarization and free-streaming; a finite ℓ cutoff is a **numerical approximation**, not a different physical law.
A constant, unperturbed vacuum sector has δε_DE=δp_DE=0 in the vacuum-fluid description. All other perturbations evolve on the **same** ν-dependent background.
Initial scalar perturbations require a specified primordial spectrum P_R(k)=A_s(k/k_*)^(n_s−1) and a mode choice (e.g., adiabatic growing mode); ν alone does not determine A_s or n_s.

The angular spectra are obtained from transfer functions:
C_ℓ^{XY}=4π∫d ln k P_R(k) Δ_ℓ^X(k) Δ_ℓ^Y(k), X,Y∈{T,E,...}.
This is a definition of the full physical prediction, not an assertion that the infinite hierarchy has an analytic closed-form solution.

## 5. Primordial nucleosynthesis (BBN)
Let Y_i=n_i/n_b be abundances per baryon and let each reaction r have stoichiometric coefficients s_ir. The complete network has
dY_i/dt=Σ_r s_ir λ_r(T,n_b,{Y_j},f_ν),
including weak n↔p conversion, light-nucleus production/destruction, reverse rates and thermodynamic detailed balance.
The neutron/proton interconversion and neutron decay are part of the network. Expansion H(T;ν) is supplied by §1–2, not independently assigned.
The baryon-to-photon ratio η_b=n_b/n_γ is **not** neon ν. Neutrino decoupling, entropy transfer and nuclear-rate uncertainties must be consistently included. BBN predicts Y_p, D/H, etc., which can be compared with abundance observations.

## 6. Distances and large-scale structure
1+z=1/a; D_C(z)=c∫_0^z dz'/H(z';ν).
For k=0, D_M=D_C; D_L=(1+z)D_M; D_A=D_M/(1+z).
BAO: D_H=c/H, D_M/r_d, D_H/r_d, D_V/r_d with D_V=[z D_M² D_H]^(1/3).
Supernovae: μ(z)=5log₁₀(D_L/Mpc)+25, with a nuisance absolute-magnitude calibration.
Matter power: P_m(k,z)=P_R(k)×(specified transfer/growth factors); growth and lensing follow the same Einstein–Boltzmann solution, not an independently chosen curve.
Observed likelihoods require full covariance and observational nuisance treatment. These likelihoods are tests of the mathematical predictions, not extra dark-energy source laws.

## 7. Native Time-Shell dissolution (October framework)
ρ_bind(a)=K_eff (a−a_N)²/a³.
For x=a/a_N and r=νρ_ref a_N/K_eff, the threshold condition is
(x−1)²/x³=r.
For 0<r<4/27, the late root x_f>3 is the candidate coherence-loss boundary. To describe a future event, the present scale factor must lie within the admitted coherent interval and a_f=a_N x_f>1.
t_diss−t_today=∫_1^{a_f} da/(aH(a;ν)).
This is a **conditional** endpoint; neither r nor the numerical date follows from the CMB/BBN equations alone. It does not imply H(a_f)=0 or gravitational recollapse.

## 8. Mathematical closure statement and limitations
Given fixed physical constants and microphysical inputs, a specified initial perturbation spectrum, atomic/nuclear reaction rates, a coherent positive-a initial slice, and the explicit ν-source and shell-threshold postulates, §§1–7 define a *coupled initial/boundary-value mathematical system*. Its predictions include H(a), distance relations, CMB spectra, light-element abundances, structure growth and conditional dissolution.
This is **equation-level assembly**, not a theorem of global existence/uniqueness, a completed exact analytic solution of the Einstein–Boltzmann/BBN hierarchies, or a derivation of the ν source from native ER foam. Exact t=0 is outside the admitted FLRW regime. The required native-to-observable handoff is inherited only where the completed Genesis↔GR equivalence applies.
If data do not admit a common ν under fixed parameters, the proposed dark-energy coupling is falsified within that model family. No retroactive retuning is allowed.
