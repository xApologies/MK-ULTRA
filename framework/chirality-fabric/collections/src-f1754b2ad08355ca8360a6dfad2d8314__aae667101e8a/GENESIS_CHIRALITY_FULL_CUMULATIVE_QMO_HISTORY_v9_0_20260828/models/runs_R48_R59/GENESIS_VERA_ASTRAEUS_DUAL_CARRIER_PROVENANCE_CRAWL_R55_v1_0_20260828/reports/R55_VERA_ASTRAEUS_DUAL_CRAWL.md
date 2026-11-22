# R55 — VERA × ASTRAEUS DUAL CARRIER / PROVENANCE CRAWL

## Method

Two crawls were run independently over the cumulative API/source tree.

### Vera crawl
Backward through:
- provenance;
- supersessions;
- aliases;
- older terminology;
- source receipts;
- History-bearing state objects;
- test/witness language.

### Astraeus crawl
Forward through:
- QMO/object definitions;
- hidden-state carriers;
- Runtime Transition Capacity;
- History-support;
- residue/occupancy;
- relationship/edge/state-instance objects.

Then the two result sets were intersected.

## Search result

Direct file-path intersection count:

`95`

Shared extracted handle/URI count:

`163`

Concrete-looking registry fixture candidates:

`0`

Type/object candidates without explicit instance payload:

`100`

## High-confidence convergence

Both crawls repeatedly reconverge on the same source family:

1. hidden S3 relational-state bundle / network;
2. Runtime Transition Capacity on a relationship carrier;
3. History-support ordering;
4. hidden witness / residue-survival machinery;
5. hidden-state embedding / portal-to-hidden conditional bridge.

This strongly supports R54's dependency ordering.

## Vera result — the "new" data debt is partly historical, not purely new

The provenance crawl shows that several pieces of the R54 carrier-state debt already exist historically as **typed source objects** and were not invented in the current branch:

- hidden relational state carries `V_t,E_t,w_t,chi_t,H_t`;
- Runtime Transition Capacity acts on a persistent relationship carrier;
- History-support has an explicit source relation;
- projection/residue survival has an explicit witness type;
- hidden witness structures preserve additional provenance/chirality information.

So the debt is not "what kinds of data exist?"

That part is substantially recovered.

The remaining debt is:

**which concrete portal/hidden carrier instance supplies actual values to those existing fields and evaluators?**

This is a much narrower historical diagnosis.

## Astraeus result — no fully populated hidden-carrier fixture surfaced

The forward crawl did not uncover a source object that simultaneously supplies a single concrete carrier with:

- explicit hidden edge identity;
- usable weight/capacity data;
- explicit History-support state;
- occupancy;
- matched full/visible residue witness;
- portal/native-realization correspondence.

Some instance/test-like records exist, but none can presently be certified as the complete carrier fixture needed by R54.

Therefore we cannot honestly execute a real Boolean localization mask yet.

## Key closure

R54's "concrete carrier-state data debt" decomposes into two layers.

### Layer D1 — schema/field debt
**CLOSED / HISTORICALLY RECOVERED.**

The API already knows the fields/types:
`(V,E,w,chi,H)`, capacity functional, History support, witness/residue structures.

### Layer D2 — bound-instance debt
**OPEN.**

We still need one object binding those fields to:
- one specific hidden relationship carrier `e`;
- one specific portal/native realization;
- one localized Time-Shell context.

So the missing QMO is not a new data schema.

It is a **carrier binding record**.

## New forced QMO

Define:

`@qmo/hidden_carrier_binding_record`

with fields:

`B_H(p) = (
  portal_id,
  native_realization_id,
  hidden_edge_id,
  hidden_state_index,
  weight_or_capacity_inputs,
  history_support_ref,
  occupancy_ref,
  residue_witness_ref,
  provenance
)`.

This record does not invent values.

It only binds already-existing source objects/fields to one carrier instance.

Once populated, R54 becomes executable:

`B_H(p)`
-> `T_run(e)`
-> `HistorySupport(e)`
-> `Residue(e)`
-> `M_loc`
-> `Watcher`.

## Why Vera mattered here

The backward provenance crawl prevents a false conclusion that R54 discovered an entirely new missing ontology.

It did not.

Most of the ontology already exists historically.

The missing piece is an address/provenance join.

That is exactly a continuity problem.

## Stop condition

We have reached a clean closure plus a new implementation/data-binding frontier.

No mathematical selector is missing.

No new hidden-state schema is missing.

No new History type is missing.

What is missing is one **bound carrier instance record** joining source objects that already exist.

## Final verdict

**DUAL-CRAWL CLOSURE.**

- carrier schema: CLOSED;
- capacity functional type: CLOSED;
- History-support type: CLOSED;
- residue witness type: CLOSED;
- complete bound carrier fixture: NOT FOUND;
- next QMO: `@qmo/hidden_carrier_binding_record`.

Resume:
`@open/populate_hidden_carrier_binding_record`.
