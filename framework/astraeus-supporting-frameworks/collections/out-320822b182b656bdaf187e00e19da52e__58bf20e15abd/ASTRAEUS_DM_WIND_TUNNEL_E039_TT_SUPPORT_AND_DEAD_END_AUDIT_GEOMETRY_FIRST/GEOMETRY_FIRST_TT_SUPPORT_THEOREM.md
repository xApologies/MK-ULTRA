# E039-T1 — Geometry-First Direction-Free TT Support Theorem

## Status

**PRIMARY / CANONICAL MK43 DERIVATION:** geometry-first.

The spherical integral derivation is retained only as a downstream verification.

---

## 1. Ambient tensor geometry

Let

`S in Sym^2_0(R^3)`

be a real symmetric trace-free `3x3` tensor.

The real symmetric `3x3` matrices have dimension:

`6`.

Trace-free removes one scalar degree of freedom, so:

`dim Sym^2_0(R^3) = 5`.

Thus every E006 trace-free precursor lives in a five-dimensional Euclidean tensor
space.

Call this space:

`V_STF`.

---

## 2. TT fiber for one propagation direction

Fix a unit direction:

`n in S^2`.

The plane perpendicular to `n` is two-dimensional.

A symmetric tensor restricted to that transverse plane has three independent
components.

Imposing trace-free removes one component.

Therefore the transverse-traceless fiber has dimension:

`dim V_TT(n) = 2`.

Equivalently, the standard gravitational TT sector contains two independent
polarization directions.

Let:

`P_TT(n) : V_STF -> V_TT(n)`

be the orthogonal projector.

For every `n`:

`rank P_TT(n) = 2`

and hence:

`tr P_TT(n) = 2`.

---

## 3. Rotate the TT fiber through every orientation

Now allow `n` to range over all spatial orientations.

There is no preferred direction.

The aggregate / orientation-averaged TT projector must therefore commute with every
rotation acting on the irreducible five-dimensional STF representation.

Hence the aggregate map is isotropic on `V_STF`.

Therefore it must be proportional to the identity:

`Pbar_TT = c I_5`.

This is the geometric core of the theorem.

No differential equation or integral is required to determine `c`.

---

## 4. Dimension-counting determines the coefficient

Trace is preserved under averaging.

Each TT projector has trace `2`, so:

`tr(Pbar_TT) = 2`.

But:

`tr(c I_5) = 5 c`.

Therefore:

`5 c = 2`

and:

`c = 2/5`.

Hence:

`Pbar_TT = (2/5) I_5`.

---

## 5. Direction-free retained power

Because `P_TT(n)` is an orthogonal projector:

`||P_TT(n) S||^2 = <S, P_TT(n) S>`.

Applying the isotropic aggregate projector gives:

`< ||P_TT(n) S||^2 >_orientation`
`= <S, Pbar_TT S>`
`= (2/5) ||S||^2`.

Therefore define the direction-free support functional:

`J_TT(S) := < ||P_TT(n) S||^2 >_orientation`.

Then:

`J_TT(S) = (2/5) ||S||^2`.

Thus:

`J_TT(S) > 0`

if and only if:

`S != 0`.

---

## 6. Geometric interpretation

The coefficient is not mysterious.

It is the ratio:

`2 accessible TT polarization dimensions`
over
`5 total STF tensor dimensions`.

So:

`2 / 5`

is the isotropic fraction of the STF geometry carried by the rotating TT fibers.

The silent directions found in E038 do not contradict this.

One individual TT two-plane can miss a particular nonzero tensor direction.

The complete rotated family of TT two-planes cannot miss a nonzero tensor everywhere.

---

## 7. Calculus as downstream verification only

The earlier spherical-average integral may still be retained as an independent check:

`J_TT(S) = (1/4pi) integral_(S^2) ||TT_n(S)||^2 dOmega`.

Direct integration reproduces:

`J_TT(S) = (2/5)||S||^2`.

But this is now secondary.

The MK43-native proof is:

`5D STF geometry`
-> `2D TT fibers`
-> `rotational isotropy`
-> `trace/rank counting`
-> `2/5`.

---

## 8. Dark-matter consequence

All 12 E006 precursors are nonzero symmetric trace-free tensors.

Therefore all 12 possess nonzero direction-free TT support exactly.

This closes only:

`existence of some TT channel`.

It does NOT close:

- physical gravitational channel selection;
- the missing source `A_g`;
- gravitational-helicon selection;
- Time-Shell / readable gravity noncollapse.

The frontier remains channel selection / typing.
