# 5. Time-Shell Interface

Source material treats a Time Shell as persistent boundary organization / a translation boundary, and Resolution as the mechanism governing when such a boundary becomes accessible.

Let `dXi` be a persistent boundary and let

```text
Pi_TS : dXi -> M
```

be a typed Time-Shell projection/readout.

At Resolution `R`, define

```text
Pi_TS,R := Read_R o Pi_TS.
```

This keeps three objects distinct:

```text
persistent boundary state
-> Time-Shell translation/projection
-> Resolution-conditioned readout.
```

## Candidate: Time-Shell Resolution Address

Genesis proposed using a readable ordering marker such as a clock value (for example, the 12:06 mark) to select a Resolution domain within a Time Shell.

This is preserved as a candidate, not promoted to canon:

```text
TSAddr(o*,R)
=
{ x in dXi | Order(Read_R(Pi_TS(x))) = o* }.
```

Here `o*` is a readable ordering address. A clock label is a downstream coordinate for that address, not assumed to be the native History object.

The construction says: fix one readable ordering address, then vary Resolution to determine what distinctions inside that address become accessible.

It does **not** yet prove that changing Resolution grants access to additional physical dimensions. That claim requires a separate typed map from Resolution classes to dimensional access/readout.
