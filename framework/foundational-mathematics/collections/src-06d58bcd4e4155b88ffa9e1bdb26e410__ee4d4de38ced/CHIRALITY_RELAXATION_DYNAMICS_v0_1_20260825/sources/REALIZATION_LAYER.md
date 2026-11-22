# STONEWAKE Realization Layer v1.1

This layer densifies the single engine-facing QMO without rewriting the upstream MK43/Dark Matter/Higgs/QFT-GR mathematics.

## Rule

The graph is **not** made complete. Arbitrary all-to-all edges would destroy semantics. Instead, v1.1 adds typed sector hubs and recursively indexes every source handle that can be placed in a physics neighborhood by conservative lexical/semantic rules.

## Physics hierarchy

```text
@stonewake_physics
  -> chirality / QFT / matter / molecular / thermodynamic / transport / continuum
  -> EM / plasma / optics / acoustics / material / gravity-geometry
  -> derived LocalPhysicsQMO templates
  -> reduced 1+3 runtime realization
  -> readout
  -> Metal
```

## Molecular catalog

The QFT-GR bridge already supplies an Atomic Chirality Carrier and a Molecular Relation Manifold. v1.1 mounts those structures and reserves explicit extension points for a future periodic-table / atomic-species / molecular-species catalog. It does **not** claim that exhaustive chemistry exists yet.

## Effects versus physics

`plasma_channel` and `poison_cloud` are STONEWAKE-derived child-QMO templates. They are not asserted as fundamental source handles. The template specifies the mathematical sectors that must be composed; material/species-dependent closures stay explicit.

## Poison cloud

A cloud is represented by one or more species concentration fields `c_i(x,t)` transported by the fluid velocity, diffusion and reactions. Density and temperature feed buoyancy/flow and rendering. Harm is downstream: accumulated exposure is integrated along the target trajectory and then passed to a target-specific response model.
