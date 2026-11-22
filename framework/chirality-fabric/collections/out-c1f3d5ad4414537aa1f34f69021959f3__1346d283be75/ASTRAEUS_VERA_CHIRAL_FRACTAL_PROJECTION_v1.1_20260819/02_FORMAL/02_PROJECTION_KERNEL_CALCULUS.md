# 02 - Projection Fibers, Kernels, and Information Loss

## 1. General projection equivalence

For an arbitrary projection `Pi:X->Y`, define

`x ~_Pi y iff Pi(x)=Pi(y)`.

The quotient `X/~_Pi` is the set of readable equivalence classes at that projection.

This definition applies even when Pi is nonlinear and therefore has no linear-algebra kernel.

## 2. Linear case

If `P:V->W` is linear,

`ker P = {v in V : Pv=0}`.

States `x` and `x+h` are read identically whenever `h in ker P`.

## 3. Multiple projections

For probes `P_1,...,P_m`, define the stacked observation operator

`O_m = [P_1; P_2; ...; P_m]`.

The unresolved linear subspace is

`K_m = ker O_m = intersection_i ker P_i`.

Each genuinely independent probe can shrink K_m. Redundant probes do not.

## 4. Common-kernel no-recovery principle

If `h != 0` lies in `K_m`, then for every x,

`O_m(x+h)=O_m(x)`.

No estimator that receives only `O_m(x)` can distinguish x from x+h without auxiliary assumptions or priors that exclude one of them.

This is not a noise problem. It is an identifiability problem.

## 5. Resolution versus kernel

Suppose Resolution is improved only by measuring `P(x)` with a smaller tolerance epsilon. If `P(x)=P(y)` exactly, decreasing epsilon cannot separate x and y. The missing distinction was quotient-erased rather than blurred.

This yields the package's central negative rule:

**More Resolution of the same projection cannot recover a degree of freedom that the projection annihilates.**

## 6. Admissible-subspace recovery

If the physically/mathematically admissible states live in a subspace S, exact linear recovery from O_m requires

`ker(O_m) intersect S = {0}`

or, more generally for an affine state family, injectivity on the set of admissible differences.

This is the correct rank criterion for the finite experiment.
