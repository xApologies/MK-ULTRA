# AST-DM-WL-P008 — Persistent Residual Transaction-Fiber / Q-Action Test

**Work layer:** WL-013  
**Status:** SOURCE-ALIGNED STRUCTURAL PROTOCOL — NOT PARENT PROMOTED

## Goal

Test QMO-AST-DM-052 against the actual parent Gate-B family without identifying UCM `ResidualFieldState` with a Time-Space Projection Residue.

## P008-0 — Select a persistent rotational residual

Choose

```text
r in Res_P,rot^R.
```

Require the existing R7 persistence qualification and rotational/S3 transaction provenance.

## P008-1 — Recover the transaction fiber

Using

```text
Res(u)=ResidualFieldState(u),
```

construct or recover

```text
Fib_Res^R(r)={u in U_rot^R | Res(u)=r}.
```

If the fiber is empty, the selected residual has no source transaction witness in the current mounted corpus.

## P008-2 — Recover the source tensor target

For each admitted `u`, evaluate/recover in one declared tensor convention:

```text
T_U(u),
T_vis^R(u),
T_D^R(u)=T_U(u)-T_vis^R(u).
```

Do not substitute scalar `rho_E` for `T_D^R`.

## P008-3 — Conservation/exchange filter

Require

```text
nabla_mu T_D^(mu nu)=-J^nu
```

for the declared full/visible comparison, or separate conservation in the `J=0` specialization.

Failure kills the corresponding transaction from the current action fiber.

## P008-4 — Use a legitimate residue bundle only

If a Projection Residue Bundle `B_res` is available from the parent hidden-state/persistence/boundary-contact route, use it.

Do not construct `B_res` from `ResidualFieldState` by name or analogy.

If no source-supported bundle instance exists, mark the physical-instance step unresolved while retaining the abstract action-family audit.

## P008-5 — Source-matched Q/action test

Search only Q completions in

```text
C_Q,T^R(B_res,T_D^R(u);g)
```

whose existing `S` constituent has the required metric variation and exchange law.

## P008-6 — Rotational refinement

Require a declared upstream/downstream rotational action and test

```text
F_Q(rho_H(g)x)=rho_Q(g)F_Q(x)
```

plus action invariance under `rho_Q` on the declared sector.

Successful witnesses lie in

```text
C_Q,T,rot^R(B_res,T_D^R(u);g).
```

## P008-7 — Classify

- `NO_TRANSACTION`: residual fiber empty.
- `NO_SOURCE_TENSOR`: source target cannot be recovered/typed.
- `CONSERVATION_FAIL`: target fails exchange law.
- `NO_BUNDLE_INSTANCE`: action audit abstract only; Gate-A instance missing.
- `ACTION_FIBER_EMPTY`: no source-matched admitted Q action.
- `ROTATION_FAIL`: source-matched action exists but rotational refinement fails.
- `GATE_B_STRUCTURAL_WITNESS`: at least one full source-matched rotational Q/action witness exists.
- `PHYSICAL_DM`: forbidden label until full parent DM_R and observational gates pass.

## Firewalls

```text
ResidualFieldState != ProjectionResidue != T_D^R != rho_E.
```

```text
B_BH^org != B_contact,H^R != B_res.
```
