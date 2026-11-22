# E063 — Joint Multi-Port Hidden-Network Witness Theorem

## Status

**LIVE DERIVED CLOSED INTERNAL / CONDITIONAL MATHEMATICAL RESULT**

This theorem combines two already established Dark Matter 2.2 source results. It does not assert that the required hidden network is physically realized.

## Premises

Take one hidden path joining two distinct readable ports,

```text
a --p-- h --q-- b
```

with `p>0`, `q>0`. Assume the same selected hidden support also satisfies the positive native-load hypotheses: `r(e) T_run(e) >= 0` on hidden edges, at least one strict positive term, and fixed `V>0` for the full/visible comparison.

## Response coordinate

The Mode-0 port-attachment theorem gives

```text
w_eff = p q/(p+q) > 0
```

and

```text
DeltaLambda_H
=
w_eff [[1,-1],[-1,1]]
!= 0.
```

## Load coordinate

The equilibrium hidden-edge load theorem gives

```text
Delta rho_H
=
[sum_(e in E_H) r(e) T_run(e)] / V
> 0.
```

## E063-T1 — Joint witness

Therefore, whenever one selected hidden two-port support satisfies both source premise sets,

```text
W_H^R = (Delta boldrho_H^R, Lambda_H)
```

has both a nonzero load coordinate and a nonzero response coordinate.

Equivalently for the selected finite region,

```text
Delta rho_H > 0
and
DeltaLambda_H != 0.
```

The conclusion is simply the conjunction of the two source theorems. No new interaction law, stress-energy map, or dark-matter identity is introduced.

## Concrete diagnostic vector

For `p=2`, `q=3`, `V=10`, with positive unit transition capacity on both edges and the diagnostic sector `r_e=w_e`,

```text
w_eff = 6/5 = 1.2
DeltaLambda_H = 1.2 [[1,-1],[-1,1]]
Delta rho_H = (2+3)/10 = 0.5.
```

For boundary test vector `c=(1,0)`,

```text
Delta j_H = (1.2,-1.2) != 0.
```

## Scope firewall

This closes only a finite conditional witness theorem. It does **not** prove:

- global hidden-state embedding nonemptiness;
- that the hidden support exists in nature;
- UCM source-projection sensitivity;
- native-density to readable-density nonannihilation;
- stress-energy realization;
- gravitational readout;
- physical dark matter.
