# L09C — Lattice SU(3) readout and physicality discriminator

**Verdict: PARTIAL PASS / PHYSICAL NATURALITY OPEN**

The frozen CRD byte graph `Q3` and its dyadic tilings already provide a cubic graph/lattice support. Once a Portal/Road representation supplies link matrices `U_e in SU(3)`, the downstream discrete gauge configuration space is typed as

`C_link = SU(3)^E / SU(3)^V`.

For every oriented reverse edge, the target convention is `U_(e^-1)=U_e^-1`.

For each square face/plaquette `p` of the CRD cubic lattice, define

`U_p = ordered_product_(e in boundary p) U_e`

and the gauge-invariant plaquette readout

`W_p = (1/3) Re Tr(U_p)`.

This gives a standard pure-gauge lattice comparison layer without identifying CRD defect holonomy with Wilson holonomy.

## Exact cochain-only no-go

Under the exact L09A embedding, every spontaneous Cluster Portal is a gauge transformation. Therefore every gauge-invariant loop/plaquette observable is unchanged throughout a fixed-seam CRD relaxation Road.

But CRD requires `Phi_f(x_next) < Phi_f(x)` for every spontaneous relaxation Portal.

Therefore the cochain-only map cannot send strict CRD relaxation to nontrivial gauge-invariant Yang-Mills evolution. It instead sends CRD relaxation to gauge fixing.

This is a genuine negative result, not a missing calculation.

## Where physical motion can enter

A full readout has additional Road/Helicon/Q data. Let `U(X)` be the link configuration after mode decoration and let `P:X->X'` be one CRD Portal.

The cochain gauge skeleton predicts a vertex frame change `g_P`.

Define the departure transporter

`D_P(e) = U_e(X') [ g_P(t(e)) U_e(X) g_P(s(e))^(-1) ]^(-1)`.

If `D_P(e)=I` for every edge, the Portal is pure gauge in the downstream readout.

If some gauge-invariant function of `D_P` is nontrivial, then the Road/Helicon decoration has moved the target gauge-equivalence class and can carry physical Yang-Mills/QCD behavior.

A convenient work-layer discriminator is

`Delta_P = sum_e [1 - (1/3) Re Tr D_P(e)]`.

Its final domain/normalization remains open until `rho_link` is completed.

## Revised L09 frontier

The next question is no longer merely “can CRD be represented by SU(3)?” The static answer is yes on a precisely typed restricted sector.

The physical question is:

**Does `S_RH` contribute a non-gauge component to the SU(3) link update under an actual CRD Portal?**

That is now the decisive L09 naturality gate.
