# ASTRAEUS — GLOBAL CONSISTENCY HACK R28
## Can the whole recursive solution select the realized update without a new local axiom?

**Date:** 2026-08-27
**Scope:** finite second-order Cradle model; T0→T5 only.

# Verdict

**GLOBAL CONSISTENCY DOES NOT GENERICALLY PRODUCE A UNIQUE LABELED HISTORY.**
But it exposes a deeper closure: much of the remaining choice is symmetry-related and therefore may disappear only after quotienting by the correct equivalence.

This changes the question from:

"Which labeled edge fires?"

to:

"Are the surviving globally consistent histories genuinely different formal identities, or merely different presentations of one symmetry class?"

That is the next closure test.

---

# 1. Why brute-forcing arbitrary Bandwidth trajectories is illegal

The live API does not contain a Bandwidth evolution law.

Therefore enumerating arbitrary Bandwidth subsets and choosing the one that yields a preferred T5 closure would simply move the Choice Gap into the Bandwidth trajectory.

R28 does not do that.

Instead it asks what can be proved from constraints that are already invariant under the carrier's earned symmetries.

---

# 2. Symmetry obstruction to unique actualization

The second-order Cradle square has address automorphisms induced by the inherited binary boundary coordinates.

If a state x is fixed by an automorphism g, and two candidate updates a,b are exchanged by g, while every admitted law and the T5 closure condition are g-equivariant, then no invariant rule constructed solely from those laws can distinguish a from b.

## Theorem R28.1 — Symmetry Choice Obstruction

Let g preserve:
- the current formal state;
- T0 admissibility;
- T1 structural preference;
- T2 adjacency;
- T3 History typing;
- stabilization/Bandwidth constraints;
- T5 viability.

If `g(a)=b` for two distinct candidates, then the existing invariant contracts cannot uniquely choose a over b without:
1. symmetry breaking already present in History/context; or
2. an additional non-invariant selector.

This is a general no-go theorem.

---

# 3. Finite chirality-seed test

Exact non-neutral diagonal chirality seeds tested:
`56`.

All of them had tied best candidates under the non-arbitrary R27 structural preference.

Tied seeds whose entire best-candidate set is one orbit under a state-preserving square symmetry:
`36`.

Tied seeds not fully explained by a single stabilizer orbit:
`20`.

Representative cases:

[
  {
    "state": [
      0,
      1,
      1,
      0
    ],
    "stabilizer_size": 4,
    "best_count": 4,
    "all_best_symmetry_equivalent": true,
    "best": [
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
    "stabilizer_size": 4,
    "best_count": 4,
    "all_best_symmetry_equivalent": true,
    "best": [
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
    "stabilizer_size": 4,
    "best_count": 4,
    "all_best_symmetry_equivalent": true,
    "best": [
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
    "stabilizer_size": 4,
    "best_count": 4,
    "all_best_symmetry_equivalent": true,
    "best": [
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
  },
  {
    "state": [
      0,
      5,
      5,
      0
    ],
    "stabilizer_size": 4,
    "best_count": 4,
    "all_best_symmetry_equivalent": true,
    "best": [
      {
        "to": [
          1,
          4,
          5,
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
          5,
          4,
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
          4,
          5,
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
          5,
          4,
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

Thus symmetry explains a substantial structural source of the Choice Gap, though not every tie is collapsed by the simple square stabilizer test.

---

# 4. Global consistency up to equivalence

The correct uniqueness criterion for a recursive Genesis solution cannot be literal uniqueness of labeled trajectories.

It must be uniqueness **up to the equivalence already admitted by Genesis**.

Define two complete solutions:

`Sigma1 ~ Sigma2`

when there is a provenance-preserving isomorphism carrying:
- carrier states;
- admissible operations;
- History;
- Bandwidth states;
- witnesses;
- T5 closure

from one solution to the other.

Then actualization is closed structurally if the set of globally consistent solutions has exactly one equivalence class.

## Definition R28.D1 — Global Solution Moduli Set

`M_G = {globally consistent Sigma} / ~`.

Problem B closes structurally iff:

`|M_G|=1`.

If `|M_G|>1`, genuinely inequivalent complete Histories survive and an additional actualization law remains necessary.

This is stronger and cleaner than requiring one arbitrary labeled path.

---

# 5. Important consequence for chirality

The two chirality classes themselves must not be quotiented away by a symmetry if chirality orientation belongs to the identity contract.

So the equivalence used in `M_G` must preserve the active chirality/provenance contract.

A mirror map that exchanges chi+ and chi- is not automatically an identity equivalence.

This prevents symmetry quotienting from erasing the phenomenon we are trying to model.

---

# 6. Where global consistency now stands

The finite model proves:

1. forward candidate sets are highly non-singleton;
2. full-Bandwidth backward viability is non-discriminating;
3. arbitrary Bandwidth restriction cannot be used without circularity;
4. structural preference leaves ties;
5. some ties are symmetry-equivalent presentations.

Therefore literal unique trajectory is the wrong finish criterion.

The correct recursive finish criterion is:

\[
oxed{	ext{unique globally consistent solution up to identity-preserving equivalence}}
\]

rather than:

\[
oxed{	ext{unique labeled edge at every step}}.
\]

---

# 7. New endpoint for Problem B

Problem B can close in either of two ways.

## B-Closure Type I — Deterministic

At every stage, the closure-compatible candidate set has one element.

## B-Closure Type II — Structural

Several labeled candidates survive, but all complete solutions belong to one identity-preserving equivalence class in `M_G`.

Then the apparent local choice is gauge/representation redundancy rather than distinct formal actualization.

Only if multiple inequivalent classes remain does a genuine event law remain missing.

---

# 8. Next exact attack

Construct the smallest complete finite-horizon T0→T5 solution space **without arbitrary Bandwidth evolution**, using Bandwidth only where independently fixed by the test context.

Then quotient the resulting complete solutions by:
- address automorphisms that preserve chirality identity;
- History/provenance isomorphism;
- witnessed T5 identity equivalence.

Compute:

`|M_G|`.

If one:
Problem B closes structurally.

If greater than one:
extract the smallest pair of inequivalent solutions and hand that exact fork back as the irreducible missing actualization datum.

# Final status

R28 does not yet close Problem B.

It closes the **correct uniqueness criterion** and proves a symmetry obstruction against arbitrary labeled selection.

The remaining question is now finite and precise:

\[
oxed{|M_G| \stackrel{?}{=} 1}.
\]
