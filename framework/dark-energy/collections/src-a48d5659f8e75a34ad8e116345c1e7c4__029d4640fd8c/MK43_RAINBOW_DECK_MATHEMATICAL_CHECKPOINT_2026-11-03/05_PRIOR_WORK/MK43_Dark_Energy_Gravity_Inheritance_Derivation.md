# MK43 Ultra — Dark Energy: Gravity Inheritance and Cosmological Consequences
**Research continuation, 2026-11-02. Mathematical derivation, not software.**

## Source-specific provenance
Directly examined `9(1).zip`, especially `MK43_Genesis_GR_Installed_v0_1/INTEGRATION_SPEC.md`, `.../Genesis_GR_Native_ER_Attachment/DERIVATION.md`, and `.../Genesis_GR_Metric_Source_Realization/DERIVATION.md`. The installation preserves the source chain helicon → gravitational helicon → graviton → continuity perturbation → Time-Shell projection → metric, and its fixed-point equations
q* = R_C[δC_m+F_g(q*)], h=Π_T(q*), g=ḡ+h.
The source records specify reversible smooth readout domains, not a proof that every microscopic native state realizes every GR cosmology. We inherit the GR-equivalent branch without modifying the gravity program.

## A. Native-to-cosmology composition
Let ρ_G be the installed GR readout, with ρ_G(𝔤_G)=g and ρ_G(𝔈_G)=G[g]. On the declared GR-equivalent coherent domain, impose the **new dark-energy source postulate** ν=𝓦(Ψ_N), 0<ν<1, ε_DE=ν ε_ref (fixed ε_ref>0). The geometric-vacuum convention is
𝔈_G+Λ_G(ν)𝔤_G=κ_G 𝔗_G^ordinary,
Λ_ν=8πG νε_ref/c⁴.
Readout:
G[g]_{μν}+Λ_ν g_{μν}=(8πG/c⁴)T^ordinary_{μν}.
This uses the cosmological term once, avoiding double-counting a vacuum source on the right.

## B. Exact homogeneous evolution
Let ρ_i denote mass-equivalent density (kg/m³), ε_i=ρ_i c². Assume spatially flat FLRW and separately conserved pressureless baryons+CDM, radiation, and constant vacuum.
Define A=(8πG/3c²)ε_r0, B=(8πG/3c²)ε_m0, C(ν)=(8πG/3c²)νε_ref, each in s⁻².
Then
H²(a;ν)=A a⁻⁴+B a⁻³+C(ν),
ȧ=a√(A a⁻⁴+B a⁻³+C),
ä/a=−A a⁻⁴−(B/2)a⁻³+C.
Cosmic time:
t(a)−t(a_i)=∫_(a_i)^a da/[a√(A a⁻⁴+B a⁻³+C)].
This is an exact implicit solution on a>0, no 13-point interpolation.

## C. Derived monotonicity and acceleration transition
Differentiate H² with respect to a:
d(H²)/da=−4A a⁻⁵−3B a⁻⁴ <0 for positive radiation/matter.
Thus H decreases monotonically, even when ä>0. Since C>0, H→√C as a→∞ absent dissolution.
The transition from deceleration to acceleration satisfies
C a_acc⁴ − (B/2)a_acc − A=0.
For A,B,C>0, the function ä/a is strictly increasing with a (derivative 4A a⁻⁵+(3B/2)a⁻⁴>0), so exactly one positive acceleration transition exists.
For negligible radiation, a_acc≈(B/(2C))^(1/3).
The fractional vacuum contribution
f_DE(a;ν)=C/[A a⁻⁴+B a⁻³+C]
strictly increases with a, from 0 as a→0+ to 1 as a→∞ (on the formal coherent continuation).
**This is the rising dark-energy dominance graph; the density ε_DE itself is constant.**
Comoving vacuum energy in V(a)=V0 a³ is E_DE(a)=νε_ref V0 a³, which increases with volume even while density remains constant.

## D. Inherited observable equivalence, with precise scope
If ν* satisfies Λ_ν*=Λ_ref and all ordinary physical parameters, initial distributions and perturbation initial conditions match a reference flat ΛCDM model, the field equations for GR+Maxwell+kinetic transport+atomic+nuclear reactions are identical on the coherent domain. Wherever the coupled initial-value problem is well posed and unique, its solutions and observables coincide:
H(z), D_L(z), BAO distances and sound horizon, CMB angular spectra, BBN light-element yields, and linear matter power.
This is a conditional **equation equivalence** statement. It does not claim the full equations have been numerically solved or observations jointly fitted; identical equations alone do not select the reference parameters.

## E. Time-Shell dissolution is a distinct structural event
Inherit ρ_bind(a)=K_eff(a−a_N)²/a³. Let ρ_th be the shell failure density and r=ρ_th a_N/K_eff. If 0<r<4/27, the late root x_f>3 solves
(x_f−1)²/x_f³=r, a_f=a_N x_f.
If a_f>1 and the current shell lies in the admitted coherent interval, its conditional remaining time is
Δt=∫_1^{a_f} da/[a H(a;ν)].
The source archive does **not** require ρ_th=νε_ref/c²; this identification, when used, is a distinct optional dark-energy postulate. A numerical endpoint cannot be inferred from ν without specifying ρ_th,K_eff,a_N.

## F. Source-derived limits and integrity
- The installed archive contains an exact representation on specified smooth domains, but its native ER attachment document explicitly limits what is proven about microscopic realization. No new gravity theorem is asserted here.
- The ν→vacuum-energy law is adopted, not extracted from the native source.
- Exact t=0 nucleation is not solved by the FLRW equations.
- Early-universe g*(T), neutrino decoupling, BBN rates, CMB transfer functions and perturbation initial conditions remain inherited physics with independently fixed parameters. This derivation establishes shared equations and their conditional equivalence, not a numerical all-observation pass.
- Neither a good background fit nor the conditional dissolution time demonstrates a measured neon constant.

## G. Derived mathematical verdict
**Established under stated postulates:** unique positive expanding homogeneous solution locally for a>0; monotone H, increasing fractional vacuum dominance, a unique acceleration transition, exact ΛCDM background correspondence for matching constants, and a conditional late shell boundary.
**Not established:** a unique microscopic ν normalization, all-observation joint fit, or source-determined dissolution date.
This is progress in dark-energy mathematics, not a reopening of gravity.
