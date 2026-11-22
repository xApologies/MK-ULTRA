# WL-v217 — S3 History State-Space / Identity-Witness Seam

**QMO:** QMO-AST-DM-WL-101  
**Work layer:** WL-035  
**Parent promotions:** 0  
**Status:** CROSS-SOURCE INSTANCE CANDIDATE / HISTORY TRANSPORT STILL OPEN

## Source question

Identity Through History v1.0 leaves the following formal task open:

```text
Specify the exact History state space carried by the S3 continuity domain.
```

Dark Matter 2.2 independently supplies a conditional relational-state bundle:

```text
pi_H : E_H^R -> T_H
```

with fiber:

```text
R_H(t)=(V_t,E_t,w_t,chi_t,H_t)_R.
```

The object is `@dm_hidden_state_bundle`. It is explicitly a candidate domain for the still-open physical embedding `iota_H`, and it already contains a typed relational-History component.

## Retype

Within the Dark Matter work layer only, the DM2.2 bundle is a strong **instance candidate** for the S3 History state-space role needed by Identity Through History.

This is not a cross-source identity theorem:

```text
S3 History state space != @dm_hidden_state_bundle
```

by declaration.

It says only that the DM bundle is already typed with the data required to test that role.

## Identity Witness

Identity Through History defines:

```text
W_Id(x,y;h)
```

as recoverable data certifying that History-related endpoints belong to the same declared Identity class, and:

```text
T_Id(h2 o h1)=T_Id(h2)oT_Id(h1)
```

for witness transport on the admissible sector.

Therefore the next useful question is no longer “what state space does History act on?” in the abstract.

It is:

```text
Can the selected DM S3 relational-state bundle carry a source-compatible Identity-Witness transport?
```

## Next handle

```text
@history_transport
```

The source status of D44 is `BRACED`, so the work layer must recover/type a bundle-specific instance rather than silently assert one.
