# L09A — CRD Z2 cochain -> SU(3) gauge-orbit embedding

**Verdict: PASS — EXACT STRUCTURAL EMBEDDING**

This run uses only frozen CRD cochain structure plus standard SU(3) matrix algebra. It does **not** use the provisional 142857/C6 basin ordering.

Let `G=(V,E)` be the oriented CRD byte graph, let `x in C0(G;Z2)` be the byte-reorientation cochain, and let `f in C1(G;Z2)` be the fixed seam/backreaction cochain. Define the residual

`r_x = f + delta x`  (mod 2).

Choose

`eta = diag(-1,-1,1) in SU(3)`,

so `eta^2=I`, `det eta=1`, and `Tr eta=-1`.

For each oriented graph edge define

`J_f(x)_e = eta^(r_x(e))`.

For a CRD Portal flip with vertex indicator `y in C0(G;Z2)`, `x' = x+y`, hence `r_x' = r_x + delta y`. Define the target vertex gauge transformation

`g_y(v)=eta^(y_v)`.

Then for every oriented edge `e:s(e)->t(e)`,

`J_f(x')_e = g_y(t(e)) J_f(x)_e g_y(s(e))^(-1)`.

Therefore every frozen CRD reorientation/Cluster-Portal move maps to an ordinary SU(3) lattice gauge transformation in this embedded Z2 subgroup.

## Loop witness

For every closed loop `gamma`,

`J_f(x)_gamma = eta^(Hol_f(gamma))`

because the coboundary contribution cancels on a closed loop.

Hence:
- `Hol_f(gamma)=0 -> Tr J_gamma = 3`;
- `Hol_f(gamma)=1 -> Tr J_gamma = -1`.

This is an explicit representation of CRD defect holonomy into a downstream SU(3) loop observable. It does **not** identify the two notions.

Because the five independent Q3 parity bits determine the CRD defect class and the loop trace distinguishes parity, the 32 Q3 defect classes inject into distinct gauge-equivalence classes inside this restricted SU(3) image.

## Exact CRD potential identity

Frozen CRD uses

`Phi_f(x)=sum_e c_e r_x(e)`

with positive route weights `c_e`.

Since `Re Tr(I)=3` and `Re Tr(eta)=-1`,

`Phi_f(x) = (3/4) sum_e c_e [1 - (1/3) Re Tr J_f(x)_e]`.

Thus CRD strict Cluster-Portal descent is strict descent of a weighted link-alignment/gauge-fixing functional **within one target gauge orbit**. It is not Yang-Mills action descent.

## Consequence

In the cochain-only embedding, spontaneous CRD relaxation changes the gauge representative but not the physical SU(3) gauge-equivalence class.

For exact/coboundary `f`, the entire relaxation Road is gauge-equivalent to the identity link configuration.

For nontrivial `[f]`, relaxation remains in the same nontrivial loop-holonomy class.

This closes a static gauge-structure bridge while proving a no-go:

**the frozen cochain relaxation by itself cannot be interpreted as nontrivial physical Yang-Mills evolution.**

Physical QCD-like evolution, if inherited, must enter through additional Road/Helicon/Q mode data rather than through `x,f` gauge redundancy alone.
