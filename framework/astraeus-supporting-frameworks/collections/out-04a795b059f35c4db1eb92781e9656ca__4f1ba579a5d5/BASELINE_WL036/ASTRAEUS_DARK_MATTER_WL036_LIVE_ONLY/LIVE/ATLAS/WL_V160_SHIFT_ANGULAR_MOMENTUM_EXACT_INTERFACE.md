# WL-v160 — Shift / Angular-Momentum Exact Interface

**Status:** exact-handle QMO composition / no parent promotion

A radius-2 direct-source QMO was generated around `@shift_vector` and a second around `@angular_momentum_parameter`. Their exact interface contains only:

- `@cauchy_problem`
- `@einstein_field_equation`

Thus the API does not require a hand-built shift-to-rotation theorem. The two objects already meet in the accepted initial-value/Einstein landscape.

The accepted direct rotational dependency is:

`@angular_momentum_parameter DEPENDS_ON @kerr_geometry`.

## Next handle

`@kerr_geometry`

This is downstream comparison mathematics only. `@shift_vector` is still not defined as frame dragging.
