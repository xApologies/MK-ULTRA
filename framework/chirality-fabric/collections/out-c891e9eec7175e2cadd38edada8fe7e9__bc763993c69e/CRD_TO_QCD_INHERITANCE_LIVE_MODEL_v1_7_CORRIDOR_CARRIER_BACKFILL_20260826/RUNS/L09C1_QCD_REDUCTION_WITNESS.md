# L09C1 — QCD Reduction Witness Typing and Source Search

**Status: ACTIVE**

Define the required witness

\[
W_3=(E_c,\rho_c,h_c,\omega_c,\nabla_c).
\]

It must establish on a declared sector `U subseteq M`:

1. `E_c -> U` is a complex rank-3 bundle.
2. `rho_c : F|_U -> E_c` is a source-supported subbundle/quotient/readout derived from projected residue.
3. `h_c` is inherited or induced consistently from the handoff Hermitian geometry.
4. `omega_c` is a nowhere-vanishing unit determinant form, giving a reduction from `U(3)` to `SU(3)`.
5. `nabla_c h_c = 0` and `nabla_c omega_c = 0`.
6. The reduction is fixed before testing the CRD path and may not be fitted to the desired QCD result.
7. Basin labels, color names, the retired C6 construction, or raw upstream fields that failed L08C descent may not define the witness.

**Close condition:** either recover/construct a source-supported `W_3`, or identify the exact missing datum and remap without unlocking L09D.
