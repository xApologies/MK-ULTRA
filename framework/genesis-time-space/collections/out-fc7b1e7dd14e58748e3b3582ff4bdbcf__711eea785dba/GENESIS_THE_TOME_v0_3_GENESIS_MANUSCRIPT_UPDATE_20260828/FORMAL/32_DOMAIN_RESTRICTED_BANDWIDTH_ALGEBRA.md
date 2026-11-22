# 32 — DOMAIN-RESTRICTED BANDWIDTH ALGEBRA

## Source relation

The existing Bandwidth Algebra reservoir treats Bandwidth as available organizational freedom and admissible transformations as typed composable corridors.

The propagation project restricts that algebra to a declared Genesis domain.

---

## Definition 32.1 — Global Bandwidth generators

Let

\[
\operatorname{Gen}(B)
\]

be the generator family made available by Bandwidth \(B\).

The generated path/category-like algebra is schematically

\[
\mathcal A_B
=
\operatorname{Cl}_{\rm comp}
\left(
\operatorname{Gen}(B)\cup\{\operatorname{id}_x\}
\right).
\]

---

## Definition 32.2 — Domain restriction

For Genesis domain \(D\), define

\[
\operatorname{Gen}_D(B)
=
\left\{
a\in\operatorname{Gen}(B):
a\text{ is admissible in }D
\right\}.
\]

Then

\[
\boxed{
\mathcal A_{B|D}
=
\operatorname{Cl}_{\rm comp}
\left(
\operatorname{Gen}_D(B)\cup\{\operatorname{id}_x\}
\right).
}
\]

This is the domain-restricted Bandwidth Algebra.

---

## Definition 32.3 — Corridor

A corridor is a typed composable word

\[
\gamma=a_n\cdots a_2a_1
\in\mathcal A_{B|D}.
\]

History retains the ordered word even when two corridors have equivalent resolved endpoints.

---

## Definition 32.4 — Resolution quotient

Resolution provides a readout/quotient

\[
\rho_R:\mathcal A_{B|D}\to\mathcal A_{B|D}^{(R)}.
\]

It may occur that

\[
\gamma_1\neq\gamma_2
\]

while

\[
\rho_R(\gamma_1)=\rho_R(\gamma_2).
\]

Therefore:

\[
\boxed{\text{History is not erased by Resolution equivalence.}}
\]

---

## Theorem 32.5 — Propagation algebra placement

Once \(\operatorname{Gen}_D(B)\) is known, generic propagation can be represented entirely inside \(\mathcal A_{B|D}\).

No separate primitive “motion operator” is required.

### Proof

Every admissible propagation is an ordered composition of domain-admissible Bandwidth generators; closure under composition yields the corridor algebra. Identity corridors represent no propagation. Resolution acts downstream as readout. ∎
