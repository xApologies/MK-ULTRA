# MK43 Rainbow Deck — CALIBRATION VALUES AND INTERPRETATION
Checkpoint: 2026-11-03. This file contains numbers intentionally excluded from the symbolic model.

## Current working numerical selection
- White / 🌀 = 0.5389276 (candidate, not uniquely identified).
- H_ref = 73 km/s/Mpc (normalization convention for coefficients).
- C_m = 0.2677779734086515 (fitted from the earlier 67.4 km/s/Mpc + 13.8 Gyr reference targets).
- C_r = 0.0000783820114168425 (latest radiation candidate based on standard thermal radiation assumptions; *not* a measured 16-digit determination).
- C_DE = 0.5845821504419774 (fitted prior to radiation update).
- C_ref = C_DE / White (dependent coefficient, not independently fitted).
- a(today) = 1 (convention; not a fitted physical scale).
- Historical target H0 = 67.4 km/s/Mpc; age = 13.8 Gyr.
- Conditional shell illustrations: a_N = 0.01, q = 0.005; other examples a_N = 0.01, q = 0.002 and a_N = 0.02, q = 0.005.
- q is a dimensionless shell threshold, NOT the cosmological deceleration parameter. Use q_dec for the latter.

## Calibration chronology and limitations
The earlier coefficients C_m=0.2677779734086515, C_r=0.0001, C_DE=0.5845821504419774 were calibrated to H0=67.4 and age=13.8 by construction. Changing C_r alone shifts both outputs slightly; do not keep reporting exact 67.4 and 13.8 without recalibration.
Earlier White sweeps 0.53–0.54 and beyond are sensitivity experiments. If C_ref is varied inversely with White, the expansion history is exactly degenerate; a 100-digit brute-force scan does not break this degeneracy.
The latest radiation coefficient was selected from standard photon/neutrino radiation assumptions, not from a full likelihood fit to CMB anisotropies. Its displayed digits are numerical, not physical, precision.
Historical past expansion is described by a flat constant-vacuum FLRW branch. The equation-level assembly includes references to BAO, BBN, supernova and CMB sectors, but a full joint covariance-aware fit and full Einstein–Boltzmann solver have NOT been demonstrated by this checkpoint.
At exact t=0, the FLRW limit is singular; no numerical native nucleation trajectory is asserted.
A finite future shell dissolution follows conditionally for admissible a_N and q, not uniquely from White. No computed native bounce/next-cycle map is included.
The full gravity/graviton framework is inherited and frozen on its declared domain. This checkpoint neither modifies nor re-proves it.

## Exact current working expression
H(a) = 73 sqrt[0.0000783820114168425 a^-4 + 0.2677779734086515 a^-3 + 0.5845821504419774] km/s/Mpc.

## Calibration versus prediction
H0 and age were calibration targets in the earlier branch; independent H(z), distance/redshift, BAO, supernova, CMB and BBN measurements remain out-of-sample tests. Future dissolution is a conditional extrapolation.
