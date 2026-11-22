# MK43 Dark Energy — DESI DR2 BAO Baseline Audit

Date: 2026-11-02. **Exploratory mathematical comparison, not a full official DESI likelihood.** Gravity and the canonical neon definition remain frozen.

## Model
H(z)=67.4 sqrt[0.000092(1+z)^4+0.315(1+z)^3+0.684908] km/s/Mpc. Flat FLRW. Assumed drag sound horizon r_d=147.09 Mpc (not calculated from recombination). The constant-vacuum baseline F(a)=1 has no independently identified neon value until the reference energy scale is fixed.

D_M(z)=c integral_0^z dz'/H(z'), D_H=c/H(z), D_V=[z D_M^2 D_H]^(1/3), c=299792.458 km/s.

## Observational inputs
DESI DR2 BAO summary values for 13 quantities, seven tracer bins, as reported in MNRAS: https://academic.oup.com/mnras/article/548/1/stag584/8540252 . Pairwise correlations were reported for each DM/DH pair; this audit uses those within-bin correlations but does not include the full official 13x13 covariance or systematic likelihood modeling.

## Results
| z | Observable | Observed | Predicted | Residual / quoted sigma |
|---|---|---:|---:|---:|
|0.295|DV/rd|7.942|8.053|+1.48|
|0.510|DM/rd|13.588|13.494|-0.56|
|0.510|DH/rd|21.863|22.730|+2.04|
|0.706|DM/rd|17.351|17.692|+1.93|
|0.706|DH/rd|19.455|20.161|+2.14|
|0.934|DM/rd|21.576|21.985|+2.69|
|0.934|DH/rd|17.641|17.562|-0.41|
|1.321|DM/rd|27.601|28.069|+1.47|
|1.321|DH/rd|14.176|14.059|-0.53|
|1.484|DM/rd|30.512|30.263|-0.33|
|1.484|DH/rd|12.817|12.875|+0.11|
|2.330|DM/rd|38.988|39.166|+0.34|
|2.330|DH/rd|8.632|8.613|-0.19|

Diagonal-error chi-square ~25.09. With only the reported within-bin DM/DH correlations included, approximate chi-square ~31.23. Neither number is an official full-covariance likelihood; no formal pass/fail or sigma significance is asserted.

## Finding
The Planck-like constant-vacuum baseline does not match all DESI DR2 BAO central values. The largest individual quoted-error residual in this comparison is DM/rd at z=0.934 (~+2.69 sigma). The result does not establish that evolving dark energy is required, because full covariance, sound-horizon physics and combined supernova/CMB constraints remain unaccounted for.

## Next discriminating operation
Compare this same baseline with a fixed, independently specified evolving F(a;nu) under the *same* physical density normalization and full covariance. Do not fit beta independently and call it a one-neon model. Preserve the Time-Shell endpoint as conditional.
