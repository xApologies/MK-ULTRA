# MK43 Ultra — First Observational Audit (2026-11-02)

## Model and provenance
Frozen gravity and ν=𝓦(Ψ_N). Corrected reference: H0=67.4 km/s/Mpc; Ωr=0.000092; Ωm=0.315; ΩDE=0.684908.
E(a;β)^2=Ωr a^-4+Ωm a^-3+ΩDE exp[3β(a−1−ln a) exp(−(a−1)^2)].
β=0 is constant vacuum. β=0.2964 is the previously selected bounded candidate. β is a diagnostic fit coefficient and has NOT been derived from ν.

## Actual data test
32 cosmic-chronometer entries loaded from `provenance://unavailable/path-sha256/2503b386f6ca87e419617be0f53d9fad4f90aa582e99ae80a95367b6436fd221/observed_cc32.csv`. For each z_i, H_model(z_i)=H0 E(1/(1+z_i);β).
Diagonal χ²(β)=Σ_i[(H_model(z_i)−H_obs,i)/σ_i]^2.
Results: χ²(0)=14.89148033; χ²(0.2964)=14.64035289.
Independent minimization β∈[-1,1] gives β=0.34925306, χ²=14.63380298.
AIC baseline = 14.89148+2k; AIC fitted evolving =14.63380+2(k+1); ΔAIC(evolving−baseline)=+1.74232. Smaller AIC preferred, so baseline weakly preferred for this test. Note unusually low reduced χ² may indicate conservative errors or correlations; do not treat as an independent precision certification.
The chronometer covariance was not available in this run. This is a diagonal-only likelihood.

## Other observational regimes
- DESI BAO: previous exploratory diagonal-error comparisons exist but no official full covariance and fully computed r_drag were applied in this run; not upgraded to an accepted fit.
- Pantheon+: no Pantheon+ measurement and covariance files are present in the local runtime. No numerical Pantheon+ χ² is claimed. The existing model distance-modulus predictions are not observed data.
- CMB: no calculated angular spectra for these two models.
- BBN: no computed nuclear abundances for these two models.
- Structure: previous growth ODE predictions exist; no independent observed fσ8 covariance applied.

## Verdict
The bounded candidate is not selected by the actual 32-point chronometer comparison. Keep both candidates; observational selection requires real supernova and BAO covariance data, physically consistent sound horizon, and CMB/BBN/growth calculations. Gravity and neon unchanged.
