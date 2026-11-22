# Recovery Prompt — CRD -> QCD v1.2

Mount this package as the current CRD->QCD work-layer checkpoint.

Mission: map frozen CRD into a downstream QCD/SU(3) comparison without modifying CRD.

Carry forward:
- L01 PASS
- L02 FORMAL PASS
- L03 FORMAL PASS
- L04 CONDITIONAL PASS
- L05 PASS
- L06 FAIL/NO-GO
- L07 target algebra PASS / upstream realization conditional
- L08 conditional C6->A2 PASS
- L09A exact CRD Z2 -> SU(3) gauge-orbit embedding PASS
- L09B compact C6 SU(3) generator lift CONDITIONAL PASS
- L09C physical gauge-class motion OPEN
- L10 glueball LOCKED

Critical v1.2 theorem:
`r=f+delta x`, `eta=diag(-1,-1,1)`, `J_e=eta^r_e`.

Every Cluster Portal `x->x+y` satisfies
`J'_e=g_y(t) J_e g_y(s)^-1`, with `g_y(v)=eta^y_v`.

Also:
`Phi=(3/4) sum_e c_e [1-(1/3)ReTr J_e]`.

Interpretation: frozen cochain relaxation is an exact SU(3)-embedded gauge-fixing descent, not physical Yang-Mills action descent.

Conditional compact C6 lift:
`sigma(X)=-P X^T P^-1`,
`K_j=i(F_j-F_(j+3))`,
`sigma K_j=K_(j+1)`,
`K_(j+3)=-K_j`,
`Lie<K0,K1,K2>=su(3)`.

Next gate:
derive normalized `U(P)=exp(a(P)K_beta)` from actual `S_RH`/Helicon data and evaluate whether a Portal produces a non-gauge departure `D_P`.

Do not unlock glueball until gauge-class motion and downstream Yang-Mills naturality are typed.
