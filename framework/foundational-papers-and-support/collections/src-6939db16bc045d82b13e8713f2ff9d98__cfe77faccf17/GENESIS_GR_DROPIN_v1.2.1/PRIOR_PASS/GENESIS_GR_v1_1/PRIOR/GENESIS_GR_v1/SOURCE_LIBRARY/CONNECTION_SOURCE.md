# 04 — Transduction Connection

## 1. Why a connection is required

A dependency arrow says where a state may continue. When more than one admissible lift exists, an additional rule is required to specify which lifted continuation is realized or compared.

The Transduction Connection is that rule.

## 2. Candidate lift family

For `f:U->V` and `x in F(U)`:

```text
Lift_f(x)={y in F(V)|Adm_f(x,y)}.
```

Under Bandwidth:

```text
Lift_f^B(x) subseteq Lift_f(x).
```

## 3. Connection selection

Recovered live-model form:

```text
Conn(f,x | R,B,H,E,chi)
```

selects an admissible horizontal lift

```text
lambda_f,x:(U,x)->(V,y).
```

The selection depends only on declared variables. Hidden tie-breakers are prohibited.

## 4. Watcher selection order

Recovered Watcher logic supplies the weakest defensible lexicographic selection policy:

1. preserve declared ancestry;
2. preserve transported chirality class;
3. preserve invariant residue;
4. satisfy operator/source-target typing;
5. satisfy Bandwidth, environment, and History admissibility;
6. minimize unsupported additional structure.

A domain-specific rule may only act after these constraints.

## 5. Nonexistence and multiplicity

Define disposition:

```text
NO_LIFT
UNIQUE_LIFT
MULTIPLE_LIFTS
TYPE_MISMATCH
ADMISSIBILITY_FAILURE
COMPOSITION_FAILURE
UNRESOLVED.
```

`MULTIPLE_LIFTS` means branching survives; it is not automatically curvature.

## 6. Connection is extra structure

The source explicitly warns that a connection is additional structure unless native rules make the lift selection canonical. This book preserves that warning. A convenient formula is never a license to fabricate a connection instance.

## 7. Connection versus transduction

Transport moves state along a declared dependency/base context. Transduction may change the dependency/base context itself. Connection-selected transport is therefore a suboperation inside the larger transduction architecture.
