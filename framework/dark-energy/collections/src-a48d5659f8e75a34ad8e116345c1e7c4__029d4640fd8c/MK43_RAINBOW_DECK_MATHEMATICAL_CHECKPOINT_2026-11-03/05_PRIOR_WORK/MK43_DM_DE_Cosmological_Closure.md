# MK43 — Dark-Matter/Dark-Energy Cosmological Closure
2026-11-02 | Mathematical continuation, not observational certification

## Recovered source
From `HERE BE DARK MATTER(1).zip`:
- `206_V33_TIME_SHELL_DENSITY_FACTORIZATION.md`: native Resolution density profile → partial basin map β_R → Time-Shell field-intensity map F_TS^B → readable calibration C_{ρ,u}. Explicitly not a complete numerical calibration.
- `204_V33_SCALAR_DENSITY_RECONSTRUCTION_NOGO.md`: regional mean cannot reconstruct a nonuniform density profile.
- `27_BIANCHI_AND_SOURCE_EXCHANGE_CLOSURE.md`: covariant conservation of total stress-energy; individual sectors may exchange through a compensating current. The archive does not establish a nonzero cosmological exchange current.

## New mathematical composition
Let ρ_DM(x,t) = \bar ρ_DM(t)[1+δ_DM(x,t)] be the readable mass-equivalent density (kg/m³), with volume-weighted mean of δ_DM zero on the chosen homogeneous averaging domain. The native map is partial:
ρ_DM(x,t) = C_{ρ,u}∘F_TS^B∘β_R[boldρ_DM^R](x,t), whenever the state lies in its admitted domain.
No claim that this expression is numerically calibrated or determines Ω_DM.

Let ν=𝓦(Ψ_N) be the fixed neon selection, and ε_DE(a;ν)=ν ε_ref F(a;ν) the candidate energy density. Its pressure is fixed by conservation if there is no dark-sector exchange:
p_DE=−ε_DE−(1/3)dε_DE/dln a.

The total readable stress tensor is
T_tot=T_b+T_γ+T_ν+T_DM+T_DE,
with dark energy appearing once, either as T_DE or as Λ when F=1. For evolving F, a constant geometric Λ alone is insufficient; use the conserved fluid stress tensor or a separately defined dynamical gravitational source.

On a spatially flat FLRW background, if dark matter is pressureless and separately conserved:
H²(a;ν)=(8πG/3c²)[ε_γ(a)+ε_ν(a)+ε_b0 a⁻³+ε_DM0 a⁻³+ν ε_ref F(a;ν)].
No extra dark matter is added to an Ω_m that already includes it: Ω_m=Ω_b+Ω_DM.

## Perturbation inheritance
For scalar Fourier perturbations in conformal Newtonian gauge, pressureless CDM obeys (one conventional sign convention):
δ_DM' = −θ_DM + 3φ',
θ_DM' = −ℋ θ_DM + k² ψ.
The gravitational potentials φ and ψ obey the full linearized Einstein equations sourced by perturbations of *all* sectors. The native dark-matter profile is the candidate source of δ_DM, but no transfer function is inferred from the mean density alone.
The power spectrum is P_DM(k,z)=⟨|δ_DM(k,z)|²⟩ with a specified Fourier normalization. Without a primordial spectrum, native profile and transfer functions, its numerical amplitude and shape are undetermined.

## General conservation and optional exchange
Let Q(t) be an energy-transfer density per unit proper time, defined positive from dark energy into dark matter. Then
ε̇_DM+3H ε_DM = Q,
ε̇_DE+3H(ε_DE+p_DE) = −Q.
These sum to a conserved dark-sector stress tensor. If Q=0, standard a⁻³ dark matter evolution and the independent F(a;ν) law apply. A nonzero Q is *not* derived from the dark-matter archive; it would be a new physical hypothesis requiring a covariant transfer current and perturbation equations. Thus adopt Q=0 as the minimal baseline, not a discovered interaction.

## A precise result: no automatic background correction
If Q=0, w_DM=0, and the calibrated mean ε_DM0 equals the dark-matter density already included in the reference Ω_m, then replacing the generic CDM symbol with the native DM readout changes neither H(a) nor the previous BAO/supernova background predictions. Proof: the Friedmann source sum is identical term by term. The inheritance can change the perturbation predictions only if its nonuniform profile or additional constitutive properties differ from the reference CDM perturbations.

## Audit verdict
Established: source separation, no-double-counting, mean/profile distinction, total conservation, and the conditional background-invariance lemma.
Not established: native SI calibration, independent Ω_DM0 prediction, native perturbation transfer function, nonzero dark-sector interaction, or improved fit to CMB/BAO/structure-growth data.
Gravity and ν unchanged. Do not infer a dark-energy fit improvement from merely renaming the matter source.
