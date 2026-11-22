# R42 — CHIRALITY HOLONOMY REPRESENTATION CRAWL

## Verdict

The source crawl resolves R41's generic holonomy-faithfulness question more sharply.

### 1. A concrete Möbius/basin holonomy action already exists

Rainbow Road v0.8 closes, under its typed Möbius-basin coordinate:

`T^6 = id`

`H^2 = id`

`H T H^-1 = T^-1`.

So the ideal basin/orientation action is dihedral-type.

This is a genuine concrete holonomy/monodromy component.

### 2. But that finite holonomy element cannot encode full ordered History

Finite test over ordered words in `T`, `T^-1`, `H`:

{
  "1": {
    "total_words": 3,
    "holonomy_elements_reached": 3,
    "colliding_elements": 0,
    "max_multiplicity": 1
  },
  "2": {
    "total_words": 9,
    "holonomy_elements_reached": 5,
    "colliding_elements": 3,
    "max_multiplicity": 3
  },
  "3": {
    "total_words": 27,
    "holonomy_elements_reached": 6,
    "colliding_elements": 6,
    "max_multiplicity": 7
  },
  "4": {
    "total_words": 81,
    "holonomy_elements_reached": 6,
    "colliding_elements": 6,
    "max_multiplicity": 19
  },
  "5": {
    "total_words": 243,
    "holonomy_elements_reached": 6,
    "colliding_elements": 6,
    "max_multiplicity": 51
  },
  "6": {
    "total_words": 729,
    "holonomy_elements_reached": 6,
    "colliding_elements": 6,
    "max_multiplicity": 143
  },
  "7": {
    "total_words": 2187,
    "holonomy_elements_reached": 6,
    "colliding_elements": 6,
    "max_multiplicity": 407
  }
}

Representative collisions:

[
  {
    "element": [
      0,
      0
    ],
    "history1": [
      "T",
      "t"
    ],
    "history2": [
      "t",
      "T"
    ]
  },
  {
    "element": [
      1,
      1
    ],
    "history1": [
      "T",
      "H"
    ],
    "history2": [
      "H",
      "t"
    ]
  },
  {
    "element": [
      5,
      1
    ],
    "history1": [
      "t",
      "H"
    ],
    "history2": [
      "H",
      "T"
    ]
  },
  {
    "element": [
      3,
      0
    ],
    "history1": [
      "T",
      "T",
      "T"
    ],
    "history2": [
      "t",
      "t",
      "t"
    ]
  },
  {
    "element": [
      1,
      0
    ],
    "history1": [
      "T",
      "T",
      "t"
    ],
    "history2": [
      "T",
      "t",
      "T"
    ]
  },
  {
    "element": [
      2,
      1
    ],
    "history1": [
      "T",
      "T",
      "H"
    ],
    "history2": [
      "T",
      "H",
      "t"
    ]
  },
  {
    "element": [
      5,
      0
    ],
    "history1": [
      "T",
      "t",
      "t"
    ],
    "history2": [
      "t",
      "T",
      "t"
    ]
  },
  {
    "element": [
      0,
      1
    ],
    "history1": [
      "T",
      "t",
      "H"
    ],
    "history2": [
      "T",
      "H",
      "T"
    ]
  }
]

The result is unavoidable: a finite D6-type element has only twelve values, while ordered History words grow without bound.

Therefore:

**Möbius/basin holonomy is a History signature component, not a faithful encoding of arbitrary ordered History.**

This strengthens R41's winding no-go.

### 3. The source itself already warns us what holonomy is

D45 defines History Holonomy as the equivalence class of the returned Identity-Witness transformation around a closed History loop.

That is not the ordered loop word.

The source schema also explicitly separates a `HolonomyRecord` into:

- loop;
- type;
- transport_action;
- equivalence_scope;
- defect;
- visibility_by_resolution;
- provenance.

So collapsing the record to one group element would throw away fields the source intentionally types separately.

### 4. Necessary source-backed signature floor

For the S2-preimage recovery problem, the safe History/holonomy signature must retain at least the recovery-relevant parts of:

`(transport action / witness-equivalence class, scope, defect, Resolution visibility, provenance)`.

Whether every field is necessary on every fiber remains open.

This is a **necessary floor**, not a claimed minimal signature.

### 5. The decisive dependency flips direction

R41 asked whether a concrete holonomy representation could supply the missing connection discrimination.

The source schema shows a dependency we must respect:

`ConnectionSelection` already contains:

`selected_lift`
and
`selection_witness`.

Holonomy transport is computed from selected lifts along a path.

Therefore a concrete holonomy representation on our new torus/S2-preimage landscape cannot be fully computed **before** the concrete connection semantics are instantiated.

So:

`connection -> selected lifts -> path transport -> holonomy`

is the source-typed dependency.

Holonomy can audit/compress History after selection; it cannot conjure the missing connection selector from nothing.

### 6. Exact roadblock

The source gives the **record type** of connection selection:

`(arrow,state,R,B,H,E,chi,selected_lift,selection_witness,status)`.

But it does not give the concrete rule `lambda_f` for choosing the selected lift in the new torus-decorated S2-preimage problem.

Thus the crawl stops at:

`@open/connection_selection_semantics`.

This is now narrower than R41's holonomy-faithfulness roadblock.

The missing object is specifically:

**the semantics of the selection witness that certifies one horizontal lift from the operative lift family.**

### 7. Next chain

Crawl the dependencies of `ConnectionSelection.selection_witness` itself:

`R`
`+ B`
`+ H`
`+ E`
`+ chi`
`+ operative lift family`
`-> selection_witness`
`-> selected_lift`.

Search the source/QMO landscape for the exact meaning of `E`, admissibility, chirality constraint, and any uniqueness/coherence lemmas attached to horizontal-lift selection.

That is the next object chain.
