# 35 — RELATIONAL PROPAGATION

## Foundational statement

\[
\boxed{
\textbf{Relationship propagates first. Motion is a resolved description of that propagation.}
}
\]

---

## Definition 35.1 — Relational propagation

For objects/identities \(A,B\), let

\[
r_{AB}^{(0)},r_{AB}^{(1)}
\]

be two relational states in a Genesis domain.

A propagation event is an admissible History-bearing corridor

\[
r_{AB}^{(0)}
\overset{\gamma}{\longrightarrow}
r_{AB}^{(1)}
\]

with \(\gamma\in\mathcal A_{B|D}\).

The primitive event is the relational update, not an absolute trajectory through a pre-given coordinate grid.

---

## Definition 35.2 — Reachability

\[
\operatorname{Reach}_{D,B}(x)
=
\left\{
y:
\exists\gamma\in\mathcal A_{B|D},
\gamma:x\to y
\right\}.
\]

At Resolution \(R\),

\[
\operatorname{Reach}_{D,B}^{(R)}(x)
=
\rho_R(\operatorname{Reach}_{D,B}(x)).
\]

---

## Theorem 35.3 — Distance is an incomplete relational invariant

Let

\[
\delta:\operatorname{Rel}_D\to\mathbb R_{\ge0}
\]

be a separation readout whenever the domain model supplies one.

It is possible that

\[
r_0\neq r_1
\]

but

\[
\delta(r_0)=\delta(r_1).
\]

Therefore constant pairwise separation does not imply absence of propagation.

### Interpretation

An object may change its orientation/placement relation around another while retaining constant separation.

The relation contains more information than the distance readout.

---

## Definition 35.4 — Anchor duality

Choosing \(A\) or \(B\) as the local anchor gives two directed readouts of one underlying relational event.

In a symmetric local metric realization:

\[
\vec P(A|B)=-\vec P(B|A).
\]

The invariant content is the History-bearing relational update, not which English sentence is chosen:

- “the ball moved away from the table”;
- “the table moved away from the ball.”

---

## Definition 35.5 — Relation-relative transverse component

A transverse distinction is a resolved component of relational change not represented by the current longitudinal/separation readout.

No globally fixed absolute transverse axis is required.

The transverse structure is generated relative to the currently resolved relational span.
