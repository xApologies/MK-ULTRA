# MK43 Rainbow Deck — Calibration 2.1

Status: FROZEN NUMERICAL BASELINE for upcoming historical cosmological tests.
Date: 2026-11-03.

## Symbolic law (no calibrated values)

White = W(Psi_N), macroscopic white-superposition readout of unknown native neon configuration.

H(a)^2 = H_ref^2 [ C_r a^(-4) + C_m a^(-3) + White * C_ref ], with a(today)=1.

C_DE = White * C_ref.

t(a) = (Mpc_in_km / seconds_per_Gyr) * integral from 0 to a of [1/(u H(u))] du.

The time-zero FLRW limit is singular; this is not a native nucleation solution.

Candidate shell boundary: x=a/a_N; f(x)=(x-1)^2/x^3; f(x_D)=q, x_D>3; 0<q<4/27. The threshold is conditional, not identified by observed expansion.

## Numerical assignments — Calibration 2.1

White = 0.5389276
H_ref = 73 km/s/Mpc
C_r = 0.0000783820114168425
C_m = 0.2678818747
C_DE = 0.5844998671
C_ref = C_DE/White (computed, not independently fitted)
a(today)=1

Targets used to fit C_m and C_DE: H0=67.4 km/s/Mpc and t0=13.8 Gyr.
The displayed coefficients are rounded from a previous numerical solution; six-decimal agreement is confirmed, not an exact 100-digit match.

## Explicit distinctions

The H0 and age values are calibration targets, not out-of-sample predictions. Radiation C_r was selected from standard thermal-radiation assumptions. White and C_ref are background-degenerate. Shell parameters a_N and q have no calibrated values in 2.1; earlier a_N=0.01 and q=0.005 were illustrative only.

This model inherits flat FLRW/GR background physics. It does not independently derive BBN nuclear reaction rates, BAO sound horizon, supernova luminosity standardization, or CMB anisotropies. These are upcoming tests. Do not alter gravity/graviton canon.

## Test protocol

1. Freeze these coefficients; calculate H(z), age-redshift relation, and distance observables.
2. Test BBN radiation-era expansion and light-element abundances with required baryon density and nuclear inputs. Do not infer abundance agreement from H(z) alone.
3. Test BAO radial and transverse distances; compute sound horizon consistently, not assume it from a fit without disclosure.
4. Test Type Ia supernova luminosity distances with calibration and covariance treatment.
5. Test CMB background distances and, where available, perturbation/anisotropy predictions.
6. Compare independent data using uncertainties, joint likelihoods and residuals. Distinguish fitted from withheld measurements.
7. Preserve all failures, model limitations and parameter provenance.

No independent observational fit to the entire past history is claimed at this checkpoint.
