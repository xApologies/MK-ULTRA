# WL-v260 — Radial Shell Contraction Geometry Without a Preferred Down

**Work layer:** WL-041  
**Status:** PURE GEOMETRY TEST HARNESS  
**Parent promotions:** 0

## Three-dimensional shell organization

Use the abstract unit-edge lattice from v259 and choose one occupied center/address `c`.

Define the shell index geometrically by shortest Unit-String path count:

```text
s(v) = d_Lambda(c,v).
```

An oriented lattice edge points inward when it lowers shell index by one:

```text
u ->_c v  iff  {u,v} is an edge and s(v)=s(u)-1.
```

No external vertical direction is introduced. `+x`, `-x`, `+y`, `-y`, `+z`, and `-z` are treated symmetrically by the center-based rule.

## Readable radial realization

For a geometric point with baseline readable radius `r>=0`, define an illustrative contraction profile

```text
g_alpha(r) = r - alpha*r/(1+r),
0 <= alpha < 1.
```

and realize each noncentral point along its existing radial ray with new radius `g_alpha(r)`.

This formula is only a sanity harness. `alpha` is not a recovered gravitational constant.

### Geometry-only properties

For `r>0` and `alpha>0`:

```text
g_alpha(r) < r,
```

so every affected point moves inward.

The center is fixed:

```text
g_alpha(0)=0.
```

For `r2>r1>=0`, direct algebra gives

```text
g_alpha(r2)-g_alpha(r1)
=
(r2-r1) * [1 - alpha/((1+r1)(1+r2))]
> 0.
```

Therefore radial shell order is preserved; shells do not cross.

Because the rule depends only on `r`, it does not privilege a downward axis.

## Unit String distinction

The abstract edge remains

```text
ell_U(e)=1.
```

The contraction occurs in the **readable realization**, not by redefining the intrinsic Unit String.

Thus:

```text
invariant continuation grammar survives,
readable spatial relation deforms.
```

That separation is exactly the type of information-preserving representation change now central to the dark-matter hunt.
