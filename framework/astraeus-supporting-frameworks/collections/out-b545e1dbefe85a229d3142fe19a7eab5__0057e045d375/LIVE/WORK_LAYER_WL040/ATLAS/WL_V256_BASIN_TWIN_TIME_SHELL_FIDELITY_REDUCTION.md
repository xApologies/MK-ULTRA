# WL-v256 — Basin-Twin Time-Shell Fidelity Reduction

**Work layer:** WL-040  
**Status:** PAIR-SPECIFIC DENSITY/TRANSDUCTION REDUCTION  
**Parent promotions:** 0

## Why the Rainbow pair is useful even though the chromatic branch is optional

Rainbow's working Geometric explicitly carries

```text
site-level basin distribution,
site-level energy-density field,
adjacency,
coarse resolved color.
```

Its two Orange examples have different internal energy-density organization while sharing one coarse Color value.

Dark Matter API 2.2 separately supplies a Resolution-level native density profile and a Time-Shell density factorization target:

```text
native density profile
-> BasinOrg_R
-> F_TS^B
-> FieldIntensity_R
-> C_rho,u
-> readable density.
```

The parent source correctly warns that the inverse density-to-basin map is not globally unique and that the chromatic branch is optional.

For the Rainbow pair we do **not** need to invert density into basin organization: the source already supplies the two basin organizations directly.

## Pair-specific gate

Let

```text
b_A = BasinOrg(A),
b_B = BasinOrg(B).
```

The source gives

```text
b_A != b_B
```

while coarse Color agrees.

The next structural test is exactly

```text
F_TS^B(b_A) ?= F_TS^B(b_B).
```

If the two field-intensity outputs differ and final readable calibration is non-annihilating on that difference, then parent Theorem 201 gives

```text
Delta rho_read != 0
=>
T_full != T_vis.
```

## Important status

The Tome/Companion keeps

```text
basin organization -> field intensity
```

as a current-canon **candidate translation**, not a completely typed proved operator.

Therefore WL-v256 is a reduction to one explicit pair-specific fidelity test, not a proof that the test passes.

## Connection to the square-root heuristic

The pair has the exact structural form now central to the hunt:

```text
coarse representation identifies A and B,
fine organization preserves A != B.
```

The open question is whether the Time-Shell translation preserves enough of that hidden distinction to make the downstream source separate.
