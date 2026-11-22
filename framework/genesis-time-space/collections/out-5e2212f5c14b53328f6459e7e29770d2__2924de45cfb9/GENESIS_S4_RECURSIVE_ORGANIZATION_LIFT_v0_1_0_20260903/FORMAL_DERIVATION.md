# Formal derivation

## D1. Recovered source objects

Let

\[
S^3=\{q=(x,y,z,w)\in\mathbb R^4:\|q\|^2=1\}
\]

and

\[
S^4=\{Q=(X,Y,Z,W,V)\in\mathbb R^5:\|Q\|^2=1\}.
\]

Recovered semantic typing:

- S3: recursive ordering.
- S4: organization of ordering / recursive stabilization.
- second `+1`: inherited, not independent.

## D2. Minimal inherited lift

A lift that treats the new coordinate as an organization of the whole inherited S3 state must scale the inherited coordinates coherently rather than append an unconstrained independent value.

Let `nu in [-1,1]` and set

\[
a(\nu)=\sqrt{1-\nu^2}.
\]

Define

\[
L_{34}(q,\nu)=(a(\nu)q,\nu).
\]

Expanded:

\[
\begin{aligned}
X&=\sqrt{1-\nu^2}\,x,\\
Y&=\sqrt{1-\nu^2}\,y,\\
Z&=\sqrt{1-\nu^2}\,z,\\
W&=\sqrt{1-\nu^2}\,w,\\
V&=\nu.
\end{aligned}
\]

### Proposition 1 - S4 closure

For every `q in S3` and `nu in [-1,1]`, `L_34(q,nu) in S4`.

Proof:

\[
\begin{aligned}
X^2+Y^2+Z^2+W^2+V^2
&=(1-\nu^2)(x^2+y^2+z^2+w^2)+\nu^2\\
&=(1-\nu^2)\cdot1+\nu^2\\
&=1.
\end{aligned}
\]

## D3. Recursive sphere interpretation

The same construction expresses each sphere recursively:

\[
S^n\cong \Sigma S^{n-1}.
\]

For S3:

\[
q_3(n,\omega)=\left(\sqrt{1-\omega^2}\,n,\omega\right),\qquad n\in S^2.
\]

For S4:

\[
Q_4(q,\nu)=\left(\sqrt{1-\nu^2}\,q,\nu\right),\qquad q\in S^3.
\]

This exactly generalizes the recovered S3 `point -> sphere -> point` description:

- fixed S3 ordering coordinate `omega` gives an S2 cross-section;
- fixed S4 organization coordinate `nu` gives an S3 cross-section.

## D4. Nested 3 + (1 + 1) parameterization

Let `n in S2`, `omega=sin(tau)`, and `nu=sin(sigma)`. Then

\[
\boxed{
Q_4(n,\tau,\sigma)=
(\cos\sigma\cos\tau\,n_x,
 \cos\sigma\cos\tau\,n_y,
 \cos\sigma\cos\tau\,n_z,
 \cos\sigma\sin\tau,
 \sin\sigma)
}
\]

and

\[
\|Q_4\|^2
=\cos^2\sigma(\cos^2\tau+\sin^2\tau)+\sin^2\sigma=1.
\]

This is the candidate mathematical realization of the recovered semantic decomposition

\[
3+(1+1).
\]

## D5. Exact local backwards recovery

For `|V|<1`, define

\[
\Pi_{43}(Q)=\frac{(X,Y,Z,W)}{\sqrt{1-V^2}}.
\]

### Proposition 2 - local right-inverse identity

\[
\Pi_{43}\circ L_{34}=\operatorname{id}_{S^3}
\]

for `|nu|<1`.

Thus the S3 ordering state is exactly recoverable from an interior S4 state.

## D6. Pole degeneracy and History

At `V=+/-1`,

\[
(X,Y,Z,W)=(0,0,0,0).
\]

Therefore the coordinate map alone cannot distinguish which S3 history arrived at a pole. This is an unavoidable property of the suspension topology, not a numerical defect.

Genesis continuity therefore requires a separate ancestry/History witness at pole traversal if identity is claimed to survive.

## D7. Constraint-weight form

Define

\[
p_i=Q_i^2.
\]

Then

\[
p_X+p_Y+p_Z+p_W+p_V=1.
\]

If the inherited S3 squared weights are

\[
r_i=q_i^2,\qquad \sum_{i=1}^4r_i=1,
\]

then

\[
\boxed{
p_i=(1-\nu^2)r_i\quad(i=X,Y,Z,W),\qquad p_V=\nu^2.}
\]

Consequently, for `|nu|<1`,

\[
\frac{p_i}{p_j}=\frac{r_i}{r_j}.
\]

The pure lift preserves all relative inherited S3 squared-coordinate ratios while allocating a normalized share to the organizational coordinate.

This is why the fifth coordinate is inherited organization rather than a bolt-on axis.

## D8. Riemann-sphere insertion

Let

\[
n:\widehat{\mathbb C}\to S^2
\]

be a chosen Riemann-sphere chart. Then

\[
Q_4(\zeta,\tau,\sigma)
=\left(\cos\sigma\cos\tau\,n(\zeta),\cos\sigma\sin\tau,\sin\sigma\right).
\]

The S3->S4 lift is therefore independent of the unresolved historical choice of Riemann-sphere coordinates.

With the standard stereographic chart, `zeta=u+iv` and `D=1+u^2+v^2`:

\[
\begin{aligned}
X&=\cos\sigma\cos\tau\frac{2u}{D},\\
Y&=\cos\sigma\cos\tau\frac{2v}{D},\\
Z&=\cos\sigma\cos\tau\frac{u^2+v^2-1}{D},\\
W&=\cos\sigma\sin\tau,\\
V&=\sin\sigma.
\end{aligned}
\]

## D9. Recursion lift

For a possibly set-valued admissible S3 update `F3` and organizational update `G`, define

\[
F_4(L_{34}(q,\nu);H)=
\{L_{34}(q',\nu'):q'\in F_3(q),\ \nu'\in G(q,\nu,H)\}.
\]

The geometry enforces `F4(...) subseteq S4` automatically.

This formalizes the recovered statement that S4 does not itself "perform recursion"; it supplies the constraints under which recursive evolution remains coherent.
