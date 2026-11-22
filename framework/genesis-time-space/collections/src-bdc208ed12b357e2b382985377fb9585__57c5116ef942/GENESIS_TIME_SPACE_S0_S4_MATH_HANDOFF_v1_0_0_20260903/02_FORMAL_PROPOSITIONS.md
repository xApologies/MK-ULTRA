# Formal Propositions, Recovery Maps, and Guards

## Proposition 1 — S2→S3 closure

For `n in S2` and `tau in [-pi/2,pi/2]`,

\[
L_{23}(n,\tau)=(\cos\tau\,n,\sin\tau)\in S^3.
\]

Proof:

\[
\|L_{23}\|^2=\cos^2\tau\|n\|^2+\sin^2\tau=1.
\]

## Proposition 2 — S3→S4 closure

For `q in S3` and `sigma in [-pi/2,pi/2]`,

\[
L_{34}(q,\sigma)=(\cos\sigma\,q,\sin\sigma)\in S^4.
\]

Proof:

\[
\|L_{34}\|^2=\cos^2\sigma\|q\|^2+\sin^2\sigma=1.
\]

## Proposition 3 — local S4→S3 recovery

For an interior point `Q=(X,Y,Z,W,V) in S4` with `|V|<1`, define

\[
\boxed{
\Pi_{43}(Q)=\frac{(X,Y,Z,W)}{\sqrt{1-V^2}}.
}
\]

Then

\[
\Pi_{43}(L_{34}(q,\sigma))=q
\]

whenever `|sin sigma|<1`.

The organization angle can be recovered using

\[
\boxed{
\sigma=\operatorname{atan2}\left(V,\sqrt{X^2+Y^2+Z^2+W^2}\right).
}
\]

## Proposition 4 — local S3→S2 recovery

For `q=(x,y,z,w) in S3` with `|w|<1`, define

\[
\boxed{
\Pi_{32}(q)=\frac{(x,y,z)}{\sqrt{1-w^2}}.
}
\]

Then

\[
\Pi_{32}(L_{23}(n,\tau))=n.
\]

The ordering angle can be recovered using

\[
\boxed{
\tau=\operatorname{atan2}\left(w,\sqrt{x^2+y^2+z^2}\right).
}
\]

## Proposition 5 — nested interior recovery

For an interior `S4` point with `|V|<1`, recover `q3=Pi_43(Q4)`. If the recovered `q3` also satisfies `|w|<1`, recover `n=Pi_32(q3)`.

Thus away from the suspension poles:

\[
\boxed{S^4\xrightarrow{\Pi_{43}}S^3\xrightarrow{\Pi_{32}}S^2}
\]

is an exact local recovery of the inherited lower state.

## Proposition 6 — inherited-ratio preservation

Let `Q=L_34(q,sigma)`, `|V|<1`. For any inherited coordinates `q_i,q_j` with nonzero denominator,

\[
\frac{Q_i^2}{Q_j^2}=\frac{q_i^2}{q_j^2}.
\]

Reason: all four inherited `S3` coordinates are multiplied by the same common factor `cos sigma`. Therefore the `S4` lift allocates a normalized share to the organization coordinate without distorting relative inherited `S3` squared-coordinate ratios.

This is one precise mathematical sense in which the additional `+1` is **inherited organization**, not a bolt-on independent axis.

## Pole-History Guard

At `w=+/-1` in `S3`, the complete `S2` cross-section collapses to a point. At `V=+/-1` in `S4`, the complete `S3` cross-section collapses to a point.

Therefore coordinate-only inversion cannot recover the incoming lower-level state at an exact pole.

If MK Ultra claims identity survives such a traversal, at least one of the following must hold:

1. a separate History/ancestry witness preserves the incoming identity;
2. the pole event is explicitly typed as identity-changing;
3. exact pole traversal is excluded from the operative domain.

The mathematics does not silently infer lost History from the collapsed coordinate.

## Recursion compatibility

Let `F3(q)` be an admissible, possibly set-valued `S3` update and let `G4(q,sigma,H)` provide admissible organization updates. Define

\[
F_4(L_{34}(q,\sigma);H)
=
\{L_{34}(q',\sigma'):q'\in F_3(q),\ \sigma'\in G_4(q,\sigma,H)\}.
\]

Every output lies in `S4` by Proposition 2. Thus `S4` supplies the constraint manifold in which inherited recursive evolution remains normalized/coherent; the sphere equation alone does not specify the dynamical selector `G4`.
