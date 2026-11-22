# 02 — Identity Witness and Transport

## 1. Identity Witness

A valid Identity Witness

```text
W_Id(x,y;h)
```

is recoverable data certifying that the endpoint realizations connected by History `h` belong to the same declared Identity class under the selected invariant contract.

This is intentionally stronger than:

```text
same name,
same coordinates,
same rendered appearance.
```

## 2. Witness transport

Let

```text
T_Id(h)
```

be the transport/action of History on Identity-Witness data.

For composable histories require

```text
T_Id(h2 o h1)
=
T_Id(h2) o T_Id(h1)
```

on the declared admissible sector.

## 3. Witness-chain theorem

Let

```text
h = h_n o ... o h_1.
```

Suppose each segment transports a valid Identity Witness and the identity-preserving witness class is closed under composition. Then

```text
T_Id(h)
=
T_Id(h_n) ... T_Id(h_1)
```

is itself identity-preserving.

Therefore segmentwise certified Identity inheritance implies global certified Identity inheritance.

## 4. Formal Identity vs Observational Identity

Define:

```text
Formal Identity
=
Identity class under the full declared witness structure.
```

Define:

```text
Observational Identity_R
=
Identity assigned after Resolution quotient / readout.
```

Distinct Formal Identities may share one Observational Identity at finite Resolution.

## Status

The Identity-Witness concept is recovered from Transduction Geometry D39-D42. The witness-chain theorem is an Atlas algebraic consequence under explicit closure/composition assumptions.
