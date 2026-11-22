# 34 — SHADOW, SEED, AND LIFT

## Definition 34.1 — Projection profile

A domain-relative projection profile is a typed map/relation

\[
\Pi_d:\mathfrak F^5\rightsquigarrow Y^d
\]

with \(0\le d\le5\) in the current scope.

The squiggled arrow emphasizes that the generic construction need not be an ordinary single-valued linear projection.

---

## Definition 34.2 — Shadow seed

For

\[
y=\Pi_d(x),
\]

the lower-dimensional expression \(y\) is a **seed/readout**, not necessarily the complete identity of \(x\).

---

## Definition 34.3 — Lift fiber

The compatible higher-dimensional landscape is

\[
\operatorname{Fib}_{\Pi_d}(y)
=
\{x:\Pi_d(x)=y\}.
\]

At Resolution \(R\), with Bandwidth and History constraints,

\[
\operatorname{AdmLift}_{R,d}(y)
\subseteq
\operatorname{Fib}_{\Pi_d}(y).
\]

The admissible fibers satisfy recursive refinement

\[
\operatorname{AdmLift}_{R+1,d}(y)
\subseteq
\operatorname{AdmLift}_{R,d}(y).
\]

---

## Definition 34.4 — Identity closure

\[
\operatorname{IdClose}_d(y)
=
\bigcap_R \operatorname{AdmLift}_{R,d}(y).
\]

If this intersection is a singleton, the structured projection/lift tower determines a unique compatible identity.

If not, the readout retains a residual identity fiber.

---

## Theorem 34.5 — Projection need not be information destruction

A many-to-one lower-dimensional readout does not imply loss of full identity if the retained projection/lift tower plus History/Bandwidth constraints separates the source identity.

Thus:

\[
\boxed{
\text{shadow}\neq\text{whole identity},
\qquad
\text{shadow can remain an address into the whole identity}.
}
\]

This is the formal shadow-box principle.
