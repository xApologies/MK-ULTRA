# ASTRAEUS Dark-Matter Wind Tunnel E020
## Gravitational-Helicon Source Recovery and Bottleneck Reclassification

**Status:** native propagation law recovered; instance gravitational-sector selector still open  
**Physical dark-matter witness:** not yet  
**Parent promotions:** 0

## Why this pass mattered

E019 closed all eight pre-helicon witness gates, then listed the gravitational-helicon
propagation law and massless branch as remaining work.

That was too conservative.

Source archaeology finds that the gravity archive already contains the native operator
architecture.

## Recovered source law

ER weighted Laplacian:

`(L_ER f)_i = sum_j W_ij (f_i - f_j)`

ER spectral problem:

`L_ER u_a = lambda_a u_a`

Gravitational-helicon recursive update:

`H_g[n+1] - 2 H_g[n] + H_g[n-1] + c_A^2 L_ER H_g[n] = 0`

Mode ansatz:

`H_g[n] = q_a exp(-i omega_a n) u_a`

Exact discrete dispersion:

`4 sin^2(omega_a / 2) = c_A^2 lambda_a`

Long-wave branch:

`omega_a^2 = c_A^2 lambda_a + O(lambda_a^2)`

Mass condition:

`mu_g = 0`

So the generic propagation/massless mathematics is not an open invention task.

## What remains genuinely open

The archive only gives `W_ij` as ER adjacency weights and says mutual information
*may* weight them schematically:

`W_ij proportional to f(I(i:j))`.

It does not recover a source-authoritative numerical weight function for the E019
endogenous ER state.

Likewise `c_A` is recovered as the maximum admissible expression ceiling, with readable
identification `c_A -> c`, but no separate sandbox calibration is present.

Most importantly, `P_g` is named and constrained:

`[R,P_g]=0`

`P_lock R P_g=0`

but the same source explicitly lists the **full helicon kernel derivation** as an open
formal obligation.

Therefore the frontier is now sharply instance-specific:

`E019 endogenous ER witness`
-> `source-valid W_ij`
-> `L_ER instance spectrum`
-> `candidate eigenmodes carrying Delta C`
-> `gravitational-sector selection P_g`
-> `Time-Shell TT readout`.

## Reclassification

The native H_g propagation equation: **RECOVERED**.

The massless dispersion branch: **RECOVERED**.

The E019-specific H_g eigenmode: **OPEN**.

The constructive gravitational selector/kernel `P_g`: **OPEN**.

The readable Time-Shell gravitational separation: **BLOCKED on instance H_g + P_g**.

## Next handle

`RECOVER_SOURCE_VALID_ER_EDGE_WEIGHTS_FOR_E019_OR_PROVE_ONLY_SCALE_FREE_SPECTRAL_TEST_IS_AVAILABLE`
