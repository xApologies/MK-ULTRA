# 05 — Parallel Transport

## 1. Path transport

For a composable path

```text
gamma=f_n o ... o f_1,
```

with selected lifts `lambda_f_i`, define

```text
P_gamma^Conn=lambda_f_n o ... o lambda_f_1.
```

This is the pre-differential parallel transport of the Transduction Connection.

## 2. Path coherence

For composable path segments `gamma_1,gamma_2`, source coherence requires, at the declared equivalence level,

```text
P_(gamma_2 o gamma_1) ~ P_gamma_2 o P_gamma_1.
```

This is composition coherence, not global flatness.

## 3. Transported components

A full transport event may carry several distinct records:

```text
state transport
chirality transport
Identity-Witness transport
History append
provenance append
holonomy update.
```

They must not be conflated.

## 4. History update

Unified Transduction Object law UTO-L3 requires successful transport to append the path to History and update relevant holonomy records. Readout closure therefore does not erase path provenance.

## 5. Transport equivalence

When two transport results are compared, the comparison must specify the equivalence in force:

```text
exact equality
Resolution equivalence
admissible equivalence
Identity equivalence
Global equivalence.
```

A loop may be trivial under one equivalence and nontrivial under another.
