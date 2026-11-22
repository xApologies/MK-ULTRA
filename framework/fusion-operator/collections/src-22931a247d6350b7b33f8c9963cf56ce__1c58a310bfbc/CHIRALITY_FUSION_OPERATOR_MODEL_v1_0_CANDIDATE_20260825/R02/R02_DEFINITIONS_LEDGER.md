# R02 — Definitions Ledger
## Subsystem Test

### D-S01 — Canonical source maps into the R01 quotient
Let

\[
\pi:C_A\sqcup C_B\to Q_\rho
\]

be the quotient map, and let \(\iota_A,\iota_B\) be the disjoint-union injections. Define

\[
j_A=\pi\circ\iota_A:C_A\to Q_\rho,
\qquad
j_B=\pi\circ\iota_B:C_B\to Q_\rho.
\]

### D-S02 — Source image subobjects
Define

\[
A_F=j_A(C_A),\qquad B_F=j_B(C_B).
\]

These are **source images** inside the fused carrier. The word *factor* is deliberately withheld.

### D-S03 — Constructional recoverability
A source is constructionally recoverable when the Fusion construction/witness supplies enough data to identify its canonical source image and invert the source map on that image.

Thus, if \(j_A\) is injective, then

\[
j_A^{-1}:A_F\to C_A
\]

exists as a map on the image. Likewise for B.

### D-S04 — Intrinsic recoverability
A source decomposition is intrinsically recoverable from \(F\) when the output object alone, under its declared equivalence and without external construction history, uniquely determines the source subobjects up to the declared source equivalence.

Constructional recoverability does **not** imply intrinsic recoverability.

### D-S05 — Total source retraction
A total retraction onto A is a map

\[
r_A:Q_\rho\to C_A
\]

such that

\[
r_A\circ j_A=\mathrm{id}_{C_A}.
\]

A quotient construction does not automatically supply such a retraction. A corresponding definition holds for B.

### D-S06 — Free separability
The fused source images are freely separable if the fused carrier is naturally equivalent to a product/coproduct decomposition in which the source components can be varied independently without violating the shared Fusion relation.

The R01 one-point quotient does not satisfy free disjointness because

\[
A_F\cap B_F\neq\varnothing.
\]

### D-S07 — Carrier factorization
At the finite carrier level, a factorization means a canonical isomorphism to an explicitly typed product-like object. No Hilbert tensor product is used in R02 because R01 supplied no Hilbert-space structure.

### D-S08 — Weak quotient Fusion
A Fusion is **weak quotient Fusion** when:

1. one global quotient carrier is formed;
2. the source images overlap nontrivially through the Fusion interface;
3. source images remain recoverable from construction/provenance data;
4. no canonical independent-factor decomposition is supplied by the fused carrier.

### D-S09 — Strong factor-erasing Fusion
A Fusion would be **strong factor-erasing Fusion** if the output no longer retained a recoverable source decomposition even with the declared internal Fusion witness/provenance, or if the new state space erased the source factorization in a formally demonstrated way.

R02 treats this as a comparison class, not an established property.

### D-S10 — R02 classification vocabulary
The roadmap classifications are read as:

- **Model S / subsystem-preserving:** independent factor structure continues natively;
- **Model Q / quotient fusion:** source provenance/images remain identifiable but the global carrier is a glued quotient rather than two freely separable factors;
- **Model E / emergent composite:** a new native state space is established that has no canonical source factorization;
- **hybrid:** two or more of these are independently established in different typed layers;
- **unresolved:** available data do not distinguish them.
