# CRD → QCD Inheritance Model v1.1

**Status:** algebraic SU(3) transition bridge sharpened; physical QCD inheritance still open.

## 1. Upstream frozen object

CRD remains the frozen upstream dynamics. A state carries graph/seam/chirality/basin/Resolution/Bandwidth/invariant/Portal/History information. Exact-sector relaxation is cooperative and Cluster-Portal closed.

## 2. Road/Helicon factorization

Retain the recovered factorization

`Pi_YM = rho_YM o Pi_Q o S_RH`.

`S_RH` is the Road/Helicon mode selector. It must precede readable QFT/Yang-Mills realization.

## 3. Mode-decorated Road

For a Portal Road `Gamma = (P1,...,Pn)`, the recovered formal mode-decoration target is

`S_RH(Gamma) = {(H_a1,...,H_an) : H_ai in H(P_i)}`.

Road-sensitive Helicon coupling remains conditional; the parent supplies Helicon-spectral terms of the form

`Gamma_n(x) = <grad Psi_n, R H>`

and higher-order rotational modes `H^(k)=R^k H`.

## 4. Generic Road transport covariance

Recovered L05 structure:

`G_Gamma = G_n ... G_1`

with endpoint frame transformation

`G'_Gamma = g_final G_Gamma g_initial^{-1}`.

This is retained as a generic orientation/connection product, not yet a physical gauge transporter.

## 5. SU(3) complement theorem

Use anti-Hermitian Gell-Mann basis `Ta=i lambda_a/2`.

Set

`g0 = span_R(T1,T2,T3,T8) ~= su(2) + u(1)`

and

`m = span_R(T4,T5,T6,T7)`.

Then

`su(3) = g0 direct_sum m`

with reductive/symmetric bracket relations

`[g0,g0] subset g0`,
`[g0,m] subset m`,
`[m,m] subset g0`.

Thus `m ~= C^2` as a real four-dimensional `U(2)` module.

An explicit embedding of `z=(z1,z2) in C^2` is

```
X(z) = [ 0   0   z1 ]
       [ 0   0   z2 ]
       [-z1* -z2* 0  ]
```

which is traceless anti-Hermitian and spans `m`.

The upstream closure condition is now precise: a Road/Helicon/Q fiber must naturally supply a complex rank-two sector `V_Gamma` plus the correct `U(2)` action. The parent Q handoff only guarantees finite complex rank `n>=1`, so rank two is not source-closed yet.

## 6. C6 / A2 conditional theorem

Let `B6={1,...,6}` denote the six basin states `k/7` and let

`kappa(k)=3k mod 7`.

The orbit is

`1 -> 3 -> 2 -> 6 -> 4 -> 5 -> 1`.

This is the recovered provisional 142857 rotational grammar.

Since `3^3=-1 mod 7`,

`kappa^3(k)=7-k`.

Let `Phi(A2)` be the six roots and `r` the 60-degree rotation. Both `(B6,kappa)` and `(Phi(A2),r)` are C6 torsors, so an equivariant bijection exists and is unique after choosing one phase origin. Orientation reversal adds the inverse generator.

Consequently opposite basin pairs map to opposite roots automatically.

## 7. Representative root map

Choose one representative of the automorphism class:

`1 -> E12`
`3 -> E13`
`2 -> E23`
`6 -> E21`
`4 -> E31`
`5 -> E32`.

The A2 root coordinates with Cartan `(H3,H8)` are:

- `E12 : ( 1, 0)`
- `E13 : ( 1/2, sqrt(3)/2)`
- `E23 : (-1/2, sqrt(3)/2)`
- `E21 : (-1, 0)`
- `E31 : (-1/2,-sqrt(3)/2)`
- `E32 : ( 1/2,-sqrt(3)/2)`.

This is a regular root hexagon.

## 8. Portal path algebra -> SU(3)

Let the three downstream basis states be `1,2,3` and interpret each directed Portal lane as a typed edge operator `Eij`.

Matrix-unit composition gives

`Eij Ekl = delta_jk Eil`.

Hence admitted two-edge Roads compose exactly as directed paths.

Examples under the representative basin map:

- `B1 B2 = B3` (`E12 E23 = E13`)
- `B3 B5 = B1` (`E13 E32 = E12`)
- `B2 B4 = B6` (`E23 E31 = E21`)
- `B6 B3 = B2` (`E21 E13 = E23`)
- `B4 B1 = B5` (`E31 E12 = E32`)
- `B5 B6 = B4` (`E32 E21 = E31`).

Inverse-pair commutators generate the Cartan sector:

- `[E12,E21] = E11-E22`
- `[E23,E32] = E22-E33`
- `[E13,E31] = E11-E33` (dependent sum of the first two).

Therefore six directed transition modes plus composition generate eight independent traceless directions.

## 9. Relation to L07 complement

If one inverse root pair is designated as the already recovered `su(2)` root sector, the other two inverse pairs provide exactly four real complement directions. Any of the three choices is Weyl-equivalent; no basin pair is intrinsically privileged before a downstream frame is selected.

## 10. Discrete gauge-transport candidate

Assign each admitted Portal edge `e` an SU(3) link variable `U_e` once a local amplitude/normalization map is derived.

Then

`U_Gamma = product_ordered U_e`

and a vertex gauge frame change acts by

`U_e -> g_t(e) U_e g_s(e)^(-1)`.

For closed loops,

`W_Gamma = Tr(U_Gamma)`

is gauge invariant.

This is the correct future location for Wilson-like observables. Road History remains separate provenance.

## 11. Remaining proof debt

1. Derive rank-two Road/Helicon/Q mode sector or replace it with the six-edge path-algebra realization directly.
2. Promote the provisional C6 Road ordering only if independently justified; otherwise retain the full automorphism class.
3. Derive `rho_link` from actual Road/Helicon data, including amplitude and locality.
4. Specify the SU(3) principal/link configuration space and physical gauge quotient.
5. Define downstream Yang-Mills/QCD evolution.
6. Evaluate `Pi_YM o R_CRD ?= R_YM o Pi_YM`.
7. Only then unlock the glueball test.

# v1.2 Addendum — Exact gauge skeleton and compact lift

## 12. CRD cochain gauge embedding

Set `eta=diag(-1,-1,1)` and `r=f+delta x`.

The map `J_e=eta^(r_e)` intertwines every CRD byte/cluster reorientation with an SU(3) vertex gauge transformation.

It descends to an injective map of the Q3 32-class CRD defect quotient into the restricted SU(3) lattice-gauge quotient, detected by loop traces.

The exact potential identity is

`Phi=(3/4) sum_e c_e [1-(1/3)ReTr J_e]`.

Therefore CRD relaxation is gauge-fixing descent in this subrepresentation.

## 13. C6 compact generator orbit

Conditional on the provisional C6 grammar, define `sigma(X)=-P X^T P^-1` and the signed root orbit `F_j`.

The unique compact half-turn lift is

`K_j=i(F_j-F_(j+3))`.

It obeys

`sigma K_j=K_(j+1)`,
`K_(j+3)=-K_j`,
and
`Lie<K0,K1,K2>=su(3)`.

Thus a real normalized Helicon/Road amplitude can be exponentiated directly into SU(3).

## 14. Physicality discriminator

The cochain gauge map proves that upstream reorientation alone cannot provide nontrivial physical Yang-Mills evolution.

For a full mode-decorated link map, compare the actual updated link to the exact cochain-predicted gauge transform:

`D_P(e)=U_e(PX) [g_P(t(e)) U_e(X) g_P(s(e))^-1]^-1`.

The full CRD->QCD inheritance problem is now localized to whether `S_RH` gives a nontrivial `D_P` plus a physically declared normalization/evolution law.
