# ASTRAEUS — FORWARD/BACKWARD INTERSECTION EXECUTION R27
## Does T5 viability close Problem B2?

**Date:** 2026-08-27

## Verdict

**No. The concrete finite test does not close B2. It exposes the remaining circularity precisely.**

Under the only Bandwidth-independent dynamics currently earned—the full conservative R16 graph—every fixed-sum component is connected and reversible. Therefore every internal candidate remains compatible with a recovery-saturated component.

So, under full availability:

`Viab_5` contains the entire fixed-sum component,

and:

`Cand_5(x)=Cand(x)`.

The backward T5 filter removes no candidates.

## Exhaustive state audit

States: `4096`.

No nontrivial candidate: `2`.

Exactly one candidate: `0`.

Multiple candidates: `4094`.

Thus raw update selection is non-singleton for most states.

## Exact chirality-seed audit

Non-neutral exact diagonal chirality seeds: `56`.

Using only the previously discussed structural preference criteria:
1. minimize diagonal chirality defect;
2. preserve chirality sign;
3. minimize transfer magnitude;

and deliberately refusing an arbitrary address-order tie-break:

Unique best candidate: `0`.

Tied best candidates: `56`.

Tie-size distribution: `{4: 36, 8: 20}`.

Representative unresolved forks:

[
  {
    "state": [
      0,
      1,
      1,
      0
    ],
    "best_score": [
      2,
      1,
      1
    ],
    "forks": [
      {
        "to": [
          1,
          0,
          1,
          0
        ],
        "edge": [
          "q01",
          "q00"
        ],
        "delta": 1
      },
      {
        "to": [
          1,
          1,
          0,
          0
        ],
        "edge": [
          "q10",
          "q00"
        ],
        "delta": 1
      },
      {
        "to": [
          0,
          0,
          1,
          1
        ],
        "edge": [
          "q01",
          "q11"
        ],
        "delta": 1
      },
      {
        "to": [
          0,
          1,
          0,
          1
        ],
        "edge": [
          "q10",
          "q11"
        ],
        "delta": 1
      }
    ]
  },
  {
    "state": [
      0,
      2,
      2,
      0
    ],
    "best_score": [
      2,
      0,
      1
    ],
    "forks": [
      {
        "to": [
          1,
          1,
          2,
          0
        ],
        "edge": [
          "q01",
          "q00"
        ],
        "delta": 1
      },
      {
        "to": [
          1,
          2,
          1,
          0
        ],
        "edge": [
          "q10",
          "q00"
        ],
        "delta": 1
      },
      {
        "to": [
          0,
          1,
          2,
          1
        ],
        "edge": [
          "q01",
          "q11"
        ],
        "delta": 1
      },
      {
        "to": [
          0,
          2,
          1,
          1
        ],
        "edge": [
          "q10",
          "q11"
        ],
        "delta": 1
      }
    ]
  },
  {
    "state": [
      0,
      3,
      3,
      0
    ],
    "best_score": [
      2,
      0,
      1
    ],
    "forks": [
      {
        "to": [
          1,
          2,
          3,
          0
        ],
        "edge": [
          "q01",
          "q00"
        ],
        "delta": 1
      },
      {
        "to": [
          1,
          3,
          2,
          0
        ],
        "edge": [
          "q10",
          "q00"
        ],
        "delta": 1
      },
      {
        "to": [
          0,
          2,
          3,
          1
        ],
        "edge": [
          "q01",
          "q11"
        ],
        "delta": 1
      },
      {
        "to": [
          0,
          3,
          2,
          1
        ],
        "edge": [
          "q10",
          "q11"
        ],
        "delta": 1
      }
    ]
  },
  {
    "state": [
      0,
      4,
      4,
      0
    ],
    "best_score": [
      2,
      0,
      1
    ],
    "forks": [
      {
        "to": [
          1,
          3,
          4,
          0
        ],
        "edge": [
          "q01",
          "q00"
        ],
        "delta": 1
      },
      {
        "to": [
          1,
          4,
          3,
          0
        ],
        "edge": [
          "q10",
          "q00"
        ],
        "delta": 1
      },
      {
        "to": [
          0,
          3,
          4,
          1
        ],
        "edge": [
          "q01",
          "q11"
        ],
        "delta": 1
      },
      {
        "to": [
          0,
          4,
          3,
          1
        ],
        "edge": [
          "q10",
          "q11"
        ],
        "delta": 1
      }
    ]
  }
]

Therefore natural T1 preference reduces the candidate set but does not generically make it singleton.

## Theorem R27.1 — Full-Bandwidth Viability Degeneracy

In the finite conservative reversible realization, T5 viability is constant on each fixed-sum component and cannot discriminate among internal redistribution candidates.

## Theorem R27.2 — Viability/Bandwidth Circularity Firewall

A nontrivial T5 viability kernel depends on the operative transformation graph.

That graph depends on Bandwidth.

Therefore an arbitrarily chosen Bandwidth restriction cannot be used to construct a viability kernel and then cited as proof that the same update/Bandwidth choice was forced.

A T5 viability kernel constrains Problem B only if Bandwidth evolution is independently derived or state trajectory, Bandwidth trajectory, and T5 closure are solved jointly.

## What recursion accomplished

Problem B is now a global consistency problem.

A finite Genesis execution solution is a tuple:

`Sigma=(state trajectory, Bandwidth trajectory, T5 witnessed closure)`

such that every transition is forward-lawful, every History/provenance condition holds, every Bandwidth state removes no forbidden transformations, and every intermediate state remains compatible with the same eventual T5 closure.

Problem B closes without a new local event axiom only if this global consistency problem has a unique solution up to admitted equivalence.

## Status

Problem A: `CLOSED_WORKING`.

Problem B1: `CLOSED`.

Problem B2: `OPEN`.

R26 backward viability: `VALID CONSTRAINT`.

R27 singleton test: `FAIL`.

Problem C: `BLOCKED`.

## Next attack

There are two clean routes:

1. independently derive Bandwidth evolution, then recompute `Viab_5` and `Cand_5`; or
2. solve simultaneously for state trajectory + Bandwidth trajectory + T5 closure and test global uniqueness.

The second route is the remaining way the recursive system might close itself without adding a local choice axiom.

**Stopping result:** backward closure constrains actualization, but does not yet determine it.
