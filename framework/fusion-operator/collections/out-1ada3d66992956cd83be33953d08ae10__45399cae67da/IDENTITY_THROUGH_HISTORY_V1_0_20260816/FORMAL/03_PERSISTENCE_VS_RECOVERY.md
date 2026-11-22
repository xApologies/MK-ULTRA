# 03 — Persistence Is Not the Same as Recovery

MK43 historically used recursion as **Identity Recovery**. The Atlas now separates that idea from stronger continuous persistence.

## 1. Endpoint recovery

For History

```text
h:x_0 -> x_n,
```

endpoint recovery holds when the selected Identity invariants at `x_n` admit a valid witness back to `x_0`.

Write

```text
Rec_Id(h)=1.
```

This permits intermediate reorganization.

## 2. Strong History persistence

Define

```text
Pers_Id(h)=1
```

iff every prefix `h|k` carries a valid Identity Witness from `x_0` to `x_k`.

Thus:

```text
Pers_Id(h)=1 => Rec_Id(h)=1,
```

but the converse need not hold.

## 3. Why the distinction matters

A system can:

```text
leave a readable configuration,
reorganize,
return to a strongly correlated configuration,
```

and therefore demonstrate recovery without proving point-by-point Identity persistence.

The T0->T7->T0 recursive-continuity experiment reported recovered T0 correlation `0.9631099269`; this is strong ancestry/recovery evidence in that experiment, not literal equality of all intermediate states.

## 4. Mode persistence

For a Helicon quotient descriptor

```text
pi_H(x)=H_alpha,
```

mode-identity persistence across an update History requires

```text
pi_H(x_k)=H_alpha
```

for each declared stage, together with preservation of the selected invariant residue.

This gives the v8 Helicon quotient an explicit persistence test.
