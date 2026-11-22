# R78 — ENGINE ENGAGEMENT CONTROL LAW

The engine engagement state is:

`d∈{0,1,2,3,4,5}`.

Typed transitions:
- `d->d` with geometry change = DEFORM;
- `d->k<d` = PROJECT;
- `d->k>d` = LIFT / engagement reconstruction.

The state space and transition typing close.

## ROADBLOCK

What selects the next engagement level?

Abstractly:

`d' = C(F,d,R,B,H,input)`.

The current mathematics does not derive the controller `C`.

Possible sources of selection include:
- explicit external command;
- Bandwidth admissibility;
- Resolution demand;
- route/profile compatibility;
- an internal selection/optimization rule.

Choosing one now would invent the controller.

**VERDICT: ROADBLOCK — NO FAILURE. STOP.**

Next: `@qmo/engine_engagement_controller`.
