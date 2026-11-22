# MK43 — Pantheon+ Initial Observational Audit
2026-11-02

## Data source
PantheonPlusSH0ES/DataRelease GitHub repository:
`Pantheon+_Data/4_DISTANCES_AND_COVAR/Pantheon+SH0ES.dat`
Public repository data retrieved directly. 1701 rows in release, 1580 retained after `IS_CALIBRATOR=0`, `zHD>0.01`, positive `m_b_corr_err_DIAG`.
These are individual SN entries, not necessarily independent astrophysical objects.

## Frozen background
H0=67.4 km/s/Mpc, Ωr=0.000092, Ωm=0.315, ΩDE=0.684908.
E²(a;β)=Ωr a^-4+Ωm a^-3+ΩDE exp[3β(a−1−ln a)exp(−(a−1)²)].
ν=𝓦(Ψ_N) unchanged; β is an exploratory evolution coefficient, not yet a derived function of ν.
Flat FLRW prediction: μ=5log10[(1+zHEL)(c/H0)∫_0^zHD dz'/E(z') /Mpc]+25.
Data field m_b_corr compared to μ plus a fitted constant offset. Simpson quadrature (160 panels) used for each SN.

## Simplified likelihood
Use individual diagonal `m_b_corr_err_DIAG` uncertainties, without the published full covariance.
Let r_i=m_i−μ_i, w_i=1/σ_i². Marginalize/profile a single common intercept M:
χ²_profile=Σw_i r_i²−(Σw_i r_i)²/(Σw_i).
Results:
β=0: χ²=697.5867242; fitted offset −19.4381927.
β=0.2964: χ²=695.0748683; fitted offset −19.4342088.
Δχ²=−2.5118559 (bounded relative to constant baseline).
A coarse scan −0.30≤β≤0.60 showed decreasing χ² through β=0.60; that is NOT a valid parameter determination or evidence for a global minimum.

## Interpretation and limits
The bounded candidate improves this diagonal-only SN statistic modestly. This is not a full Pantheon+ analysis: the official full covariance, selection effects, nuisance correlations, duplicate-object correlations, and any calibration treatment beyond a common intercept are absent. The unexpectedly low χ² per entry underscores the limits of diagonal-only treatment. No CMB/BBN likelihood was evaluated; no claim of a joint cosmological pass.
The observational data were read in the connected GitHub tool, while the audit report was written separately; raw Pantheon+ data are not redistributed in this archive. Reproducible equations and filtering rules are stated above.

## Next decisive audit
Apply the official Pantheon+ covariance to this same model and combine it with the official DESI BAO covariance and a physical drag sound horizon. Keep gravity, ν, and dark-matter source unchanged.
