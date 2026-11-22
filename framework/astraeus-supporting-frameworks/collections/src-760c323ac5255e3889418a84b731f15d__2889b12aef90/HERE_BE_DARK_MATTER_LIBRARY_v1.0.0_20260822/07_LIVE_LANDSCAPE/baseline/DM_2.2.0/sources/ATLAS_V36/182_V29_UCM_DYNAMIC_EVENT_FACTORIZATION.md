# 182 — UCM Dynamic-Event Factorization

## Status

```text
DERIVED TYPE FACTORIZATION / v29
Source-grounded in the recovered Universal Coupling transaction and API handoff.
```

## 1. Why v28's source projection is still too compressed

V28 wrote the recovered readable-source architecture schematically as

```text
T_U = Pi_U(O,Chi,A,P,Rred,S,B).
```

That is useful for projection-fiber analysis, but the Universal Coupling recovery contains a more detailed upstream transaction:

```text
source manifold
-> Perturb
-> ER Redistribute
-> R4 Corridors
-> R5 Resolve
-> R6 Stabilize
-> coupling event / target response
-> readable energy-momentum projection.
```

V29 separates those two mathematical roles.

## 2. Dynamic event map

Let `X_U` be the admissible domain of UCM transaction states. A state contains the source manifold, environment, candidate target(s), chirality/Bandwidth/ancestry ledgers, and the topology state required by the recovered runtime contract.

Let `E_U` be the space of resolved Universal Coupling event records.

Define the partial dynamic-event map

```text
U_dyn : X_U ⇀ E_U
```

by the recovered transaction

```text
U_dyn(x)
=
Stabilize_R6(
  Resolve_R5(
    Corridors_R4(
      R_ER(
        Perturb(source(x), environment(x))
      )
    )
  )
).
```

The arrow is partial because the recovered source itself lists failure states such as no admissible corridor, R5 resolution failure, and R6 survivability failure.

## 3. Readable-source projection from event space

The recovered API handoff declares that a Universal Coupling event can carry a readable energy-momentum projection.

Accordingly define the still-partially-typed map

```text
P_T : E_U ⇀ T_read
```

where `T_read` is the readable stress-energy/source target appropriate to the downstream gravity problem.

On the common admissible domain, the v28 source projection therefore factorizes as

```text
Pi_U = P_T o U_dyn.
```

This is a type decomposition, not a claim that the missing numerical formula for `P_T` has been recovered.

## 4. Two distinct fibers

Define dynamic-event equivalence

```text
x ~_dyn y
iff
U_dyn(x)=U_dyn(y).
```

Define readable-source equivalence on event space

```text
e ~_T e'
iff
P_T(e)=P_T(e').
```

Then, wherever the composition is defined,

```text
Pi_U(x)=Pi_U(y)
iff
U_dyn(x) ~_T U_dyn(y).
```

This splits UCM blindness into two mathematically distinct possibilities:

```text
1. dynamic blindness:
   U_dyn(x)=U_dyn(y)

2. source-projection compression:
   U_dyn(x)!=U_dyn(y)
   but
   P_T(U_dyn(x))=P_T(U_dyn(y)).
```

## 5. V29-T1 — Event difference is necessary but not sufficient

A changed coupling event does not by itself prove a changed readable gravitational source:

```text
U_dyn(x) != U_dyn(y)
```

does not imply

```text
P_T(U_dyn(x)) != P_T(U_dyn(y)).
```

The source projection may identify distinct event records.

Thus v29 refuses to use `different topology response` as a synonym for `different T_mn`.

## 6. Dark-source criterion in factored form

Let `M_R` be ordinary S2 matter/radiation readout. A UCM dark-source witness is a pair `x,y` such that

```text
M_R(x)=M_R(y)
```

but

```text
U_dyn(x) not~_T U_dyn(y).
```

Equivalently,

```text
P_T(U_dyn(x)) != P_T(U_dyn(y)).
```

The advantage is diagnostic: if the test fails, we can now ask whether the failure occurred before event formation or at the event-to-source projection.

## 7. Status

```text
UCM transaction architecture                 RECOVERED
U_dyn typed partial map                      V29 DERIVED
P_T event-to-source map role                  V29 TYPED; FORMULA OPEN
Pi_U = P_T o U_dyn                           V29 DERIVED ON COMMON DOMAIN
dynamic-event fiber                          V29 DERIVED
readable-source event fiber                   V29 DERIVED
event difference -> T difference             NOT GENERALLY VALID
Mode-0 dark-source witness                    OPEN
```
