# WL-v163 — Killing -> Isometry -> Noether Charge

**Status:** API symmetry crawl / no parent promotion

The API was asked what sits underneath the `@killing_vector` handle. It returns the direct accepted dependency:

`@killing_vector DEPENDS_ON @isometry`.

`@isometry` is a metric-preserving diffeomorphism. Its accepted family contains stationary/axisymmetric spacetime, Komar quantities, and `@noether_charge`. The latter is defined as a **covariant phase-space conserved charge**.

So the API has converted the rotational branch from a scalar-looking parameter into an algebraic symmetry/conserved-charge branch.

## Next handle

`@noether_charge`
