# Time-Space S0→S4 Core Mathematics

## 0. Notation and dimensional bookkeeping

For the standard sphere

\[
S^n=\{q\in\mathbb R^{n+1}:\|q\|^2=1\},
\]

`S^n` has intrinsic dimension `n` and `n+1` ambient real coordinates. In the project language this is why `S^3` is the **four-coordinate stage** and `S^4` is the **five-coordinate stage**.

To avoid symbol collisions across levels this package uses:

- `S^2`: \(n=(n_x,n_y,n_z)\),
- `S^3`: \(q_3=(x,y,z,w)\),
- `S^4`: \(Q_4=(X,Y,Z,W,V)\).

Historical/local notes may call the `S^3` coordinates `X,Y,Z,W`; those are aliases of the level-local `(x,y,z,w)` used here.

---

## 1. S0 — distinction

Source-preserved foundational object:

\[
\boxed{S^0=\{-1,+1\}.}
\]

Semantic role in the recovered Time Structure source:

\[
\boxed{S^0=\text{minimal admissible distinction}.}
\]

The recovered local transformation rule is the square-root admission:

\[
\sqrt{+1}=1,\qquad \sqrt{-1}=i.
\]

The project interprets this not as merely an arithmetic trick but as the opening of the complex admissible path while preserving the original distinction.

---

## 2. S1 — closure of the invariant interval

The source closes the Unit String by identifying endpoints, producing a circle. A standard coordinate realization is

\[
\boxed{S^1=\{(a,b)\in\mathbb R^2:a^2+b^2=1\}}
\]

or equivalently

\[
\boxed{z=e^{i\theta},\quad |z|=1.}
\]

The source semantic role is **closure / recoverable continuation**. A complete traversal returns to the origin without selecting a privileged beginning/end.

---

## 3. S2 — Riemann sphere / compactified readable geometry

The Riemann sphere is

\[
\boxed{S^2=\{(n_x,n_y,n_z)\in\mathbb R^3:n_x^2+n_y^2+n_z^2=1\}.}
\]

The recovered Time Structure source emphasizes **compactification / recoverable infinity** as its important role.

### 3.1 Standard stereographic chart

For a complex-plane coordinate

\[
\zeta=u+iv,
\]

let

\[
D=1+u^2+v^2.
\]

One standard pole convention is

\[
\boxed{
 n_x=\frac{2u}{D},\qquad
 n_y=\frac{2v}{D},\qquad
 n_z=\frac{u^2+v^2-1}{D}.
}
\]

Then

\[
n_x^2+n_y^2+n_z^2=1.
\]

**Provenance boundary:** this is a standard mathematical chart inserted as an explicit coordinate realization. The historical Time Structure source preserved the Riemann-sphere role but did not uniquely canonize this exact `(u,v)` convention. The recursive `S^2->S^3->S^4` law below is chart-independent.

---

## 4. S3 — recursive ordering

Source-preserved sphere constraint:

\[
\boxed{S^3=\{(x,y,z,w)\in\mathbb R^4:x^2+y^2+z^2+w^2=1\}.}
\]

Source-preserved semantic role:

\[
\boxed{S^3=\text{recursive ordering structure}.}
\]

The source describes the geometry as a point-to-sphere-to-point organization as the fourth coordinate moves between its poles.

### 4.1 Explicit S2→S3 recursive lift

Let

\[
n=(n_x,n_y,n_z)\in S^2
\]

and let

\[
\tau\in[-\pi/2,\pi/2].
\]

Define

\[
\boxed{
L_{23}(n,\tau)
=
(\cos\tau\,n_x,
 \cos\tau\,n_y,
 \cos\tau\,n_z,
 \sin\tau).
}
\]

Thus

\[
\boxed{
\begin{aligned}
x&=\cos\tau\,n_x,\\
y&=\cos\tau\,n_y,\\
z&=\cos\tau\,n_z,\\
w&=\sin\tau.
\end{aligned}}
\]

Closure is exact:

\[
\begin{aligned}
x^2+y^2+z^2+w^2
&=\cos^2\tau(n_x^2+n_y^2+n_z^2)+\sin^2\tau\\
&=\cos^2\tau+\sin^2\tau\\
&=1.
\end{aligned}
\]

At fixed \(w\), the cross-section is an `S^2` of radius

\[
\sqrt{1-w^2}.
\]

At \(\tau=0\), the full unit `S^2` is recovered as the equator. At \(\tau=\pm\pi/2\), the `S^2` cross-section collapses to the two poles.

### 4.2 Explicit chart from the complex plane to S3

Substitute the standard Riemann-sphere chart:

\[
\boxed{
\begin{aligned}
x&=\cos\tau\frac{2u}{D},\\
y&=\cos\tau\frac{2v}{D},\\
z&=\cos\tau\frac{u^2+v^2-1}{D},\\
w&=\sin\tau,
\end{aligned}
\qquad D=1+u^2+v^2.}
\]

---

## 5. S4 — organization of ordering / recursive stabilization

Source-preserved sphere constraint:

\[
\boxed{S^4=\{(X,Y,Z,W,V)\in\mathbb R^5:X^2+Y^2+Z^2+W^2+V^2=1\}.}
\]

Source-preserved semantic role:

\[
\boxed{S^4=\text{organization of ordering / recursive stabilization}.}
\]

The source explicitly says:

\[
\boxed{3+(1+1)}
\]

rather than an independent `3+1+1`: the second `+1` is **inherited**, and the attack is to **lift the structure already present**, not bolt on a new independent axis.

### 5.1 Explicit S3→S4 recursive organization lift — completed 2026-09-03

Let

\[
q_3=(x,y,z,w)\in S^3
\]

and let

\[
\sigma\in[-\pi/2,\pi/2].
\]

Define

\[
\boxed{
L_{34}(q_3,\sigma)
=
(\cos\sigma\,x,
 \cos\sigma\,y,
 \cos\sigma\,z,
 \cos\sigma\,w,
 \sin\sigma).
}
\]

Therefore

\[
\boxed{
\begin{aligned}
X&=\cos\sigma\,x,\\
Y&=\cos\sigma\,y,\\
Z&=\cos\sigma\,z,\\
W&=\cos\sigma\,w,\\
V&=\sin\sigma.
\end{aligned}}
\]

Exact closure:

\[
\begin{aligned}
X^2+Y^2+Z^2+W^2+V^2
&=\cos^2\sigma(x^2+y^2+z^2+w^2)+\sin^2\sigma\\
&=1.
\end{aligned}
\]

This realizes the standard suspension structure

\[
\boxed{S^4\cong \Sigma S^3}
\]

and is adopted here as a **source-constrained candidate formalization** because it exactly implements the recovered instructions `lift the inherited structure` and `the second +1 is inherited`.

At fixed \(V\), the cross-section is an `S^3` of radius

\[
\sqrt{1-V^2}.
\]

At \(\sigma=0\), the entire `S^3` ordering object is recovered at the equator. At \(\sigma=\pm\pi/2\), the inherited `S^3` cross-section collapses to the two organizational poles.

---

## 6. Fully nested S2→S3→S4 law

Substituting the `S^3` lift into the `S^4` lift gives

\[
\boxed{
\begin{aligned}
X&=\cos\sigma\cos\tau\,n_x,\\
Y&=\cos\sigma\cos\tau\,n_y,\\
Z&=\cos\sigma\cos\tau\,n_z,\\
W&=\cos\sigma\sin\tau,\\
V&=\sin\sigma.
\end{aligned}}
\]

with

\[
n_x^2+n_y^2+n_z^2=1.
\]

Therefore

\[
\boxed{X^2+Y^2+Z^2+W^2+V^2=1}
\]

identically.

This supplies a precise mathematical form for the recovered semantic decomposition

\[
\boxed{
\underbrace{(X,Y,Z)}_{3\text{-coordinate inherited geometry}}
+
\left(
\underbrace{W}_{\text{ordering}}
+
\underbrace{V}_{\text{organization of ordering}}
\right).
}
\]

`V` is **not** defined here to be chirality itself. Chirality remains a separate orientation/admissibility/History structure acting within the admitted higher-order geometry.

---

## 7. Fully explicit `(u,v,tau,sigma)` chart

Using the standard Riemann chart, `D=1+u^2+v^2`:

\[
\boxed{
\begin{aligned}
X&=\cos\sigma\cos\tau\frac{2u}{D},\\
Y&=\cos\sigma\cos\tau\frac{2v}{D},\\
Z&=\cos\sigma\cos\tau\frac{u^2+v^2-1}{D},\\
W&=\cos\sigma\sin\tau,\\
V&=\sin\sigma.
\end{aligned}}
\]

This is an explicit four-parameter chart into the five-coordinate `S^4` constraint manifold.

---

## 8. Squared-coordinate constraint language

Define

\[
p_X=X^2,\quad p_Y=Y^2,\quad p_Z=Z^2,\quad p_W=W^2,\quad p_V=V^2.
\]

Then

\[
\boxed{p_X+p_Y+p_Z+p_W+p_V=1.}
\]

Group the sectors:

\[
\boxed{
G=X^2+Y^2+Z^2=\cos^2\sigma\cos^2\tau,
}
\]

\[
\boxed{
O=W^2=\cos^2\sigma\sin^2\tau,
}
\]

\[
\boxed{
C=V^2=\sin^2\sigma.
}
\]

Then

\[
\boxed{G+O+C=1.}
\]

These are dimensionless structural/constraint weights. They are **not automatically probabilities, energies, densities, masses, or dark-matter fractions**. Such interpretations require an independently typed downstream map.

---

## 9. Generic recursive sphere law

Both lifts are instances of the same construction:

\[
\boxed{
L_{n,n+1}(q,\theta)=(\cos\theta\,q,\sin\theta),\qquad q\in S^n.
}
\]

Then

\[
\|L_{n,n+1}(q,\theta)\|^2
=\cos^2\theta\|q\|^2+\sin^2\theta=1.
\]

Thus the hierarchy can be read recursively as

\[
S^2\xrightarrow{\text{ordering }\tau}S^3
\xrightarrow{\text{organization }\sigma}S^4.
\]

The geometry supplies the admissible constraint manifold; it does not by itself replace History, Resolution, Bandwidth, Persistence, Chirality, Connection, or other MK Ultra operators.
