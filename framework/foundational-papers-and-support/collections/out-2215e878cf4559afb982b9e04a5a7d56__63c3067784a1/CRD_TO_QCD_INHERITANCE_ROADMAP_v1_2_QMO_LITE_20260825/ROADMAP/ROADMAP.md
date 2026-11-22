# CRD → QCD Inheritance Roadmap v1.2

**Mission:** construct or falsify a typed downstream QCD/SU(3) readout of frozen Chirality Relaxation Dynamics (CRD) without rewriting CRD to fit QCD.

**Direction:**

`CRD -> Portal/Rainbow Road -> Helicon/Q handoff -> SU(3)/Yang-Mills representation -> QCD dynamics`

## Hard firewalls

- CRD chirality is not QCD color charge.
- Basin labels/states are not themselves QCD red/green/blue.
- The six basin scalar states are not asserted to be six independent Lie-algebra directions.
- CRD defect holonomy is not Wilson-loop holonomy.
- Road History is provenance and is not itself a gauge observable.
- CRD frustration/Phi is not Yang-Mills action/energy.
- A structural SU(3) representation is not yet physical QCD.
- Frozen CRD is never modified to force downstream agreement.

## Live run ledger

| Run | Target | Status |
|---|---|---|
| L01 | CRD -> Portal/Road inheritance | PASS |
| L02 | Helicon spectral witness | FORMAL PASS |
| L03 | Mode-decorated Rainbow Road | FORMAL PASS |
| L04 | Road-sensitive Helicon coupling | CONDITIONAL PASS |
| L05 | Generic orientation/connection product | PASS |
| L06 | Direct initial `U(1) x SU(2) x C -> SU(3)` | FAIL / NO-GO |
| L07 | Four-real-dimensional complement / SU(3) completion | PASS AS TARGET ALGEBRA; CRD REALIZATION CONDITIONAL |
| L08 | Six Road lanes -> A2 root system | CONDITIONAL PASS under provisional 142857 C6 grammar |
| L09A | CRD Z2 cochain -> SU(3) gauge orbit | **PASS — exact** |
| L09B | C6 compact SU(3) generator lift | **CONDITIONAL PASS** |
| L09C | Physical gauge-class motion / naturality | **OPEN** |
| L10 | Glueball / pure-gauge imitation test | LOCKED |

## L09A — exact CRD gauge skeleton

For the CRD residual

`r_x=f+delta x in C1(G;Z2)`

choose

`eta=diag(-1,-1,1) in SU(3)`.

Define

`J_f(x)_e = eta^(r_x(e))`.

For a Portal flip `x -> x+y`, let `g_y(v)=eta^(y_v)`. Then

`J_f(x+y)_e = g_y(t(e)) J_f(x)_e g_y(s(e))^(-1)`.

Thus every frozen CRD Cluster Portal is exactly a vertex gauge transformation in this embedded subgroup.

For a closed loop,

`J_gamma = eta^(Hol_f(gamma))`,

so CRD loop parity is represented downstream by trace `3` or `-1`.

The CRD potential has the exact identity

`Phi_f(x) = (3/4) sum_e c_e [1-(1/3) ReTr J_f(x)_e]`.

Therefore spontaneous CRD relaxation is a weighted gauge-fixing descent inside one target gauge orbit, **not** Yang-Mills action descent.

This proves a useful no-go: the cochain sector alone cannot supply nontrivial physical Yang-Mills dynamics.

## L09B — compact C6 lift

Conditional on the provisional Road cycle

`1 -> 3 -> 2 -> 6 -> 4 -> 5 -> 1`,

there is an order-six automorphism of `su(3)`

`sigma(X)=-P X^T P^(-1)`

with

`P=[[0,1,0],[0,0,1],[1,0,0]]`.

Using the signed root orbit

`F0=E12, F1=-E13, F2=E23, F3=-E21, F4=E31, F5=-E32`,

define

`K_j=i(F_j-F_(j+3))`.

Then

`sigma(K_j)=K_(j+1)`,
`K_(j+3)=-K_j`,
and
`Lie<K0,K1,K2>=su(3)`.

The half-turn plus anti-Hermiticity uniquely selects this compact lift up to real scale.

Thus a real Road/Helicon amplitude `a(P)` gives a valid link

`U(P)=exp(a(P) K_beta(P)) in SU(3)`.

The remaining scalar problem is the physical dimensionless normalization and the still-open `S_RH` selector.

## L09C — exact physicality discriminator

The CRD cube/dyadic lattice supports an ordinary lattice-gauge target

`SU(3)^E / SU(3)^V`.

For plaquette `p`:

`U_p=product_(boundary p) U_e`,
`W_p=(1/3) ReTr U_p`.

Under the cochain-only embedding, all such gauge-invariant observables remain constant during a spontaneous CRD relaxation Road. Therefore strict CRD `Phi` descent is gauge fixing, not physical Yang-Mills relaxation.

For the full mode-decorated map, let `P:X->X'` and let `g_P` be the exact cochain gauge transformation. Define

`D_P(e)=U_e(X') [g_P(t(e)) U_e(X) g_P(s(e))^(-1)]^(-1)`.

The decisive gate is whether `D_P` is identically the identity after Road/Helicon/Q decoration.

- `D_P=I` for all links -> downstream move is pure gauge.
- nontrivial gauge-invariant `D_P` -> the selector contributes physical gauge-class motion.

## Consequence for the original imitation contract

The original target

`Pi_YM o R_CRD = R_YM o Pi_YM`

must be tested on **gauge-equivalence classes**.

L09A shows that the frozen cochain portion of `R_CRD` acts trivially on the physical quotient. Therefore any nontrivial QCD imitation of CRD relaxation must be carried by the additional Helicon/Q representation data, not by the Z2 residual cochain alone.

## Progress

`[■■■■■×◐◐■◐○□]`

Legend: `■` pass, `×` retained no-go, `◐` conditional/partial, `○` open, `□` locked.

## Next exact target

Close or falsify the **mode physicality gate**:

1. instantiate the Road-sensitive scalar from `S_RH` / Helicon spectral data;
2. freeze a dimensionless normalization `a(P)`;
3. build `U(P)=exp(a(P)K_beta)` on the lattice;
4. evaluate `D_P` across actual CRD Cluster Portals;
5. determine whether the selected mode update is purely gauge or changes Wilson/curvature observables;
6. only if gauge-class motion is nontrivial, choose a downstream Yang-Mills evolution and evaluate the original naturality/imitation equation.

Glueball remains locked until this gate closes.
