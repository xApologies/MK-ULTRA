# 200 — Energy-to-Stress Handle Recovery

## Status

```text
RECOVERED_API_DEPENDENCY
plus Atlas type analysis
```

## 1. Handle-first recovery

V31 left the large question

```text
P_T(u_full) ?= P_T(u_vis)
```

open.

The v32 handle-first attack does not attempt to construct `P_T` globally.

The already-preserved API 4.3 native-energy source contains three relevant recovered edges:

```text
@continuity_conservation
    CORRESPONDS_TO
@local_energy_momentum_conservation

@general_energy
    PROJECTS_TO
@stress_energy_tensor

@energy_density
    ENTERS
@stress_energy_tensor
```

Local source witness:

```text
SOURCES/API_4_3_NATIVE_ENERGY_20260816/RP45_GR_DEPENDENCY_LANDSCAPE_REPORT.md
```

The source report records these relations directly in its recovered dependency landscape.

## 2. Native energy objects remain distinct

The native-energy recovery supplies

```text
E_MK(H)
=
[Pi(U_n)-Pi(U_0)] / epsilon_MK
```

for ordered history `H`, together with

```text
E_MK(H_closed) = 0.
```

Separately, local energy density is recovered as

```text
rho_E = Relationship * TransitionCapacity / ContainmentVolume.
```

Therefore

```text
@general_energy != @energy_density
```

as mathematical roles.

The first measures endpoint persistence difference along a history.

The second measures supported local relational/transition load per containment volume.

## 3. Consequence for the dark-network branch

V29 derived, under its positive hidden-load assumptions,

```text
Delta rho_H
=
[sum over hidden e of r(e) T_run(e)] / V
> 0.
```

That is naturally a difference in the `@energy_density` object.

Therefore the API already supplies a downstream handle:

```text
hidden S3 relational-capacity load
-> Delta rho_H
-> @energy_density
-> @stress_energy_tensor.
```

This does **not** yet determine the complete tensor.

It does mean the stress-energy question can be attacked component-by-component instead of inventing one monolithic source map.

## 4. Dynamic / history branch

A formation or reconfiguration history may instead generate

```text
Delta E_general != 0,
```

which has the recovered API route

```text
@general_energy PROJECTS_TO @stress_energy_tensor.
```

A static persistent network can have nonzero `rho_E` while a closed history has zero `E_MK`.

The two branches must therefore remain separate.

## 5. Conservation handle

The recovered correspondence

```text
@continuity_conservation
CORRESPONDS_TO
@local_energy_momentum_conservation
```

is a useful bridge but not by itself a proof that a proposed hidden sector satisfies the full covariant condition.

The readable target remains

```text
nabla_m T^mn = 0
```

or a declared exchange-current law whose total source is conserved.

## 6. Updated attack surface

The v31 single unknown

```text
P_T
```

is now decomposed into smaller handles:

```text
static supported load
    -> @energy_density
    -> density component of stress-energy

formation / reconfiguration history
    -> @general_energy
    -> stress-energy projection

continuity bookkeeping
    -> @continuity_conservation
    -> local energy-momentum conservation compatibility
```

The remaining work is typing/calibrating those transductions and recovering the non-density tensor data, not inventing the entire tensor from scratch.
