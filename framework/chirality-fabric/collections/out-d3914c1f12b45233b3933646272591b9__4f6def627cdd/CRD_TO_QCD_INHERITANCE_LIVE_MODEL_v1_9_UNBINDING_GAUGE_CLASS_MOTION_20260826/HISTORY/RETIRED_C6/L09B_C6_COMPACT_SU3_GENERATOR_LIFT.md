# L09B — Conditional C6 compact SU(3) generator lift

**Verdict: CONDITIONAL PASS — depends on provisional 142857/C6 Road grammar**

L08 established a conditional C6 root-hexagon indexing. The remaining reality problem was that the directed root matrices `E_ij` live naturally in the complexified algebra and are not themselves anti-Hermitian SU(3) generators.

This run closes that compact-real-form problem.

## Order-six SU(3) automorphism

Let `E_ij` be matrix units and let

`P = [[0,1,0],[0,0,1],[1,0,0]]`.

Define

`sigma(X) = - P X^T P^(-1)`.

On `su(3)` this is a real Lie-algebra automorphism of order six.

Choose signed root vectors

- `F0 = E12`
- `F1 = -E13`
- `F2 = E23`
- `F3 = -E21`
- `F4 = E31`
- `F5 = -E32`.

Then `sigma(F_j)=F_(j+1 mod 6)`.

Match these positions to the recovered provisional Road orbit `(1,3,2,6,4,5)`. The signs do not change root lines; they make the C6 action exact on chosen root vectors.

## Compact half-turn lift

The signed root vectors satisfy `F_j^dagger = -F_(j+3)`.

Define

`K_j = i (F_j - F_(j+3))`.

Then:
- `K_j in su(3)`;
- `sigma(K_j)=K_(j+1)`;
- `K_(j+3)=-K_j`.

Explicitly,
- `K0 = i(E12+E21)`
- `K1 = -i(E13+E31)`
- `K2 = i(E23+E32)`
- `K3 = -K0`
- `K4 = -K1`
- `K5 = -K2`.

Thus the Road half-turn becomes inversion of the compact generator direction.

### Uniqueness

Inside the two-root plane spanned by `F_j,F_(j+3)`, impose simultaneously:
1. anti-Hermiticity;
2. `sigma^3(K)=-K`.

These conditions force

`K = real_scale * i(F_j-F_(j+3))`.

Therefore the compact lift is unique up to real scale/sign, not an arbitrary choice of six complex coefficients.

## Lie-generation theorem

The three independent generators `K0,K1,K2` generate all of `su(3)` under commutators.

First commutators give the complementary off-diagonal quadratures:
- `[K0,K1] = E23-E32`
- `[K0,K2] = -(E13-E31)`
- `[K1,K2] = E12-E21`.

Commuting those with the original `K` generators produces the two independent diagonal Cartan directions. Hence

`Lie<K0,K1,K2> = su(3)`.

Equivalently, the one-parameter subgroups `exp(t K_j)` generate connected `SU(3)`.

## Portal link consequence

If a Road/Helicon selector supplies a real dimensionless segment amplitude `a(P)`, define

`U(P)=exp(a(P) K_beta(P)) in SU(3)`.

Then ordered Portal composition immediately yields an SU(3) Road product.

The recovered Helicon spectral coupling is real-valued, so the remaining amplitude problem is normalization/selection, not complex-conjugacy completion.

## Firewall

This does not canonize the 142857 Road ordering.

It proves: **if** that C6 grammar is the Road ordering selected by the upstream model, **then** it admits a compact, reversal-compatible, Lie-generating SU(3) lift.
