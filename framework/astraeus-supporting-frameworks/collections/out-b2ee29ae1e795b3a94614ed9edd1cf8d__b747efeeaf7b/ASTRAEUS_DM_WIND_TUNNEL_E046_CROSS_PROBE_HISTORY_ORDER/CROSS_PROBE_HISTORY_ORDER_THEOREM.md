# E046 — Cross-Probe History Order

## 1. Question

E045 showed that exact topographic quotient partitions are probe-dependent.

The next question is weaker and more useful:

Does endogenous History still define a robust **order of approach to the saturated
substrate/readout state** across independent probe views?

## 2. Reject the naive scalar

For each probe view `A`, define the response magnitude from fresh:

`M_A(k) = ||R_A(E_k)-R_A(E_0)||`.

Across the seven H/O projections, monotone growth of `M_A(k)` is:

`False`.

It fails.

The response slightly overshoots and then relaxes.

Therefore:

**History depth is not a monotone "response strength" coordinate.**

This candidate scalar is parked.

## 3. Geometry-first replacement: distance to the saturated representative

Use the late representative `E_16` from the controlled orbit.

For each fixed probe view:

`d_A(k) = ||R_A(E_k)-R_A(E_16)||`.

Normalize away probe scale:

`delta_A(k) = d_A(k)/d_A(0)`.

This is a finite Euclidean distance in the readout-state geometry.

No derivative, fit, or differential equation is required.

## 4. Result

For every one of the seven independent H/O readout projections:

`delta_A(k+1) <= delta_A(k)`

for all tested depths.

All-seven monotonicity:

`True`.

The normalized cross-probe envelope contracts as follows:

`k= 0: [1, 1]`
`k= 1: [0.073349, 0.107739]`
`k= 2: [0.00784973, 0.0113684]`
`k= 3: [0.000924194, 0.00190348]`
`k= 4: [0.000180111, 0.000424577]`
`k= 5: [4.50608e-05, 8.4918e-05]`
`k= 6: [1.06039e-05, 1.67787e-05]`
`k= 7: [2.37257e-06, 3.96929e-06]`
`k= 8: [5.18861e-07, 9.20423e-07]`
`k= 9: [1.03363e-07, 2.10042e-07]`

Already after one endogenous write, every view has moved to within approximately
`7.3%-10.8%` of its original distance from the saturated response.

After three writes:

`0.092%-0.190%`.

After six writes:

`0.00106%-0.00168%`.

## 5. Cross-view order versus within-view order

Within each fixed probe view, the order is exact over the tested orbit.

A stronger demand would compare distances measured in **different probe metrics**
directly.

That stronger all-view envelope order is not required by the geometry because each
probe defines its own metric scale/distortion.

Nevertheless, `16` of the 16 adjacent depth transitions have
non-overlapping normalized H/O envelopes.

The maximum prefix for which every pair of depths is separated even under arbitrary
cross-view comparison is:

`E0...E16`.

## 6. Correct object

The probe-robust object is therefore not one universal scalar magnitude.

It is an **order family**:

`E_i precedes E_j`

iff, for every fixed admissible view `A`,

`delta_A(i) >= delta_A(j)`.

For the controlled E043 orbit this ordering agrees with History depth.

So define the work-layer convergence order:

`E_0 >=_sat E_1 >=_sat ... >=_sat E_16`.

This is a preorder/order statement, not a universal physical clock.

## 7. Relation to E044/E045 topography

E044:
substrate topography enters its stable quotient class at `E6`.

E045:
all tested H/O readout topographies are stable by `E7`.

E046:
the exact readout states continue moving inside those stable topographic classes, but
their distance to saturation continues to decrease monotonically.

Thus the geometry naturally separates:

1. **topographic basin entry**;
2. **microstate convergence inside the basin**.

That is exactly why the topographic quotient can stabilize before the numerical state.

## 8. Dark-sector consequence

The hidden History family now has three independently recovered levels:

`same [Q_H]`
-> `distinct direct-flow quotient classes`
-> `ordered convergence toward a stable cross-probe basin`.

This is substantially stronger structure than a one-off hidden response.

It remains pre-gravitational.

## 9. Next handle

Do not optimize the convergence coordinate.

The highest-value next question is persistence:

**After the History orbit has entered the stable basin, does the retained substrate
state survive when new H2 History writes stop?**

That directly tests whether the hidden state is persistent memory rather than merely a
driven transient.
