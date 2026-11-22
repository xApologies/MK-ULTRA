# R41 — TORUS HISTORY-SIGNATURE CRAWL

## Verdict

The next chain closes a major no-go result:

**Torus winding is not enough to replace ordered History.**

The T2 geometry gives endpoint and winding/net-displacement information. That distinguishes many same-presentation histories, but it does not distinguish every ordered traversal.

Explicit collisions:

[
  {
    "history_1": [
      "A+",
      "A-"
    ],
    "history_2": [
      "B+",
      "B-"
    ],
    "signature_1": [
      0,
      0
    ],
    "signature_2": [
      0,
      0
    ],
    "collision": true
  },
  {
    "history_1": [
      "A+",
      "B+",
      "A-",
      "B-"
    ],
    "history_2": [
      "B+",
      "A+",
      "B-",
      "A-"
    ],
    "signature_1": [
      0,
      0
    ],
    "signature_2": [
      0,
      0
    ],
    "collision": true
  },
  {
    "history_1": [
      "A+",
      "A+",
      "A-",
      "A-"
    ],
    "history_2": [
      "B+",
      "B+",
      "B-",
      "B-"
    ],
    "signature_1": [
      0,
      0
    ],
    "signature_2": [
      0,
      0
    ],
    "collision": true
  }
]

Even net lift displacement collides heavily. Exhaustive ordered-word counts through length six:

{
  "1": {
    "total_words": 4,
    "signature_classes": 4,
    "colliding_classes": 0,
    "max_multiplicity": 1
  },
  "2": {
    "total_words": 16,
    "signature_classes": 9,
    "colliding_classes": 5,
    "max_multiplicity": 4
  },
  "3": {
    "total_words": 64,
    "signature_classes": 16,
    "colliding_classes": 12,
    "max_multiplicity": 9
  },
  "4": {
    "total_words": 256,
    "signature_classes": 25,
    "colliding_classes": 21,
    "max_multiplicity": 36
  },
  "5": {
    "total_words": 1024,
    "signature_classes": 36,
    "colliding_classes": 32,
    "max_multiplicity": 100
  },
  "6": {
    "total_words": 4096,
    "signature_classes": 49,
    "colliding_classes": 45,
    "max_multiplicity": 400
  }
}

Therefore a signature such as:

`(current torus cell, winding pair, invariant residue)`

cannot universally serve as the recovery discriminator if ordered History distinctions remain recovery-relevant.

## Why this is not a failure of T2

T2 captures topological History.

The source `@history_trace` is stronger: it is an ordered structurally relevant traversal/provenance record.

Different ordered paths can share one torus winding class.

Therefore:

`topological History != full provenance History`.

## Conditional closure

Winding would be sufficient only if Genesis explicitly declared histories equivalent whenever they fall in the same relevant torus homotopy class.

No such quotient is currently licensed.

So winding is a valid component of a History signature, not the complete signature.

## Next QMO forced by the chain

The older source already provides:

- `@history_holonomy` = closed-path witness transformation;
- `@holonomy_history_signature` = source-backed scaffold for a History-sensitive transport signature.

Thus the chain forces the question:

`rho_hol : admissible History classes -> witness transformations`.

Is the concrete holonomy representation separating/faithful on recovery-relevant lineages?

If yes, holonomy can compress ordered History sufficiently for recovery/connection.

If no, more ordered provenance must remain attached.

## Roadblock

Faithfulness cannot be tested without the concrete chirality connection/holonomy action.

So the crawl terminates at:

`@open/holonomy_representation_faithfulness`.

The exact missing object is now:

**the concrete chirality holonomy representation on the torus-decorated S2 preimage fiber.**

## Status

- winding pair as History component: VALID;
- winding as universal recovery signature: REFUTED BY COUNTEREXAMPLE;
- common invariant residue appended to an existing collision: cannot rescue it;
- full ordered History: sufficient candidate but potentially over-complete;
- holonomy/history signature: correct next compression candidate;
- faithfulness of concrete holonomy representation: ROADBLOCK.
