# E064 — Conditional Dark-Readout Factorization Theorem

## Status

**CONDITIONAL CLOSURE UNDER EXPLICIT WORKING ASSUMPTIONS**

This theorem is deliberately a speed-taped exploration result. It is mathematically closed relative to the assumptions listed below; it is not promoted to DM 2.2 canon and is not a physical dark-matter claim.

## Working assumptions

1. `WA-DM-E064-001`: a selected positive hidden support exists on the diagnostic sector, giving `Delta rho_H > 0` and the already-closed E063 response/load witness.
2. `WA-DM-E064-002`: there is a controlled pair `u_full,u_vis` with the same ordinary matter readout, `M_R(u_full)=M_R(u_vis)`, under fixed external comparison data.
3. `WA-DM-E064-003`: the native-to-readable density transduction is nonannihilating on the selected positive component, so `Delta rho_read != 0`.

## Theorem

Under the three working assumptions and the source theorems already present in DM 2.2,

```text
M_R(u_full) = M_R(u_vis)
```

while

```text
g_full != g_vis.
```

Therefore the dark-readout defect set

```text
D_R = {(x,y) | M_R(x)=M_R(y) and G_R(x)!=G_R(y)}
```

is nonempty on the admitted conditional sector.

## Proof

By `WA-DM-E064-001`, the selected support has

```text
Delta rho_H > 0.
```

By `WA-DM-E064-003`,

```text
Delta rho_read != 0.
```

ATLAS 201, Theorem 201.1 gives

```text
Delta rho_read != 0
=>
Delta T != 0,
```

so

```text
T_full != T_vis.
```

ATLAS 180, V28-T3 states that for the same readable Einstein equation, constants, gauge equivalence, and external/background data,

```text
T_full != T_vis
=>
g_full != g_vis.
```

By `WA-DM-E064-002`,

```text
M_R(u_full)=M_R(u_vis).
```

The definition in ATLAS 122 therefore places the pair in `D_R`. Hence

```text
D_R != empty
```

on this conditional sector. QED.

## What is gained

The Live Landscape now knows exactly what one small unproved readout assumption would buy. We no longer need to solve the whole hidden embedding, whole UCM map, or full stress-energy tensor to reach a conditional dark-readout witness.

## What remains unpaid

The result is conditional on three proof debts. The highest-leverage one is `PD-DM-003`: prove one source-grounded nonannihilation witness for the native-density -> readable-density transduction.
