# ASTRAEUS — STABILIZATION / REVERSIBILITY HACK R22
## Testing whether `.°.` can create the missing T4 asymmetry

**Date:** 2026-08-27
**Input:** exact R17–R21 four-address G7 execution model.
**Question:** Can the source stabilization operator `.°.` be realized minimally as history-dependent locking of a just-used redistribution boundary, thereby breaking universal exact reversibility without redefining persistence?

# Result

Two minimal hysteresis models were tested.

## H1 — reverse-direction lock only

After:
`u --δ--> v`

stabilization forbids only the immediate reverse directed edge:
`v -> u`.

All other redistribution routes remain admissible.

Unit-transfer cases tested:
`25088`.

Recoverable through an alternate route:
`25088`.

Nonrecoverable:
`0`.

### Verdict
**H1 FAILS TO CREATE T4 ASYMMETRY.**

On the four-address square, forbidding only the immediate reverse direction is insufficient: the alternate three-edge route around the square can transport the unit back whenever carrier capacity permits. Exhaustively, every tested unit transfer remained recoverable.

This is a useful topology result: **local directional hysteresis can be bypassed by a cycle.**

---

## H2 — acted-boundary stabilization

After a redistribution across boundary `{u,v}`, stabilization temporarily locks that entire boundary in both directions.

The remaining three edges still form an alternate path around the square.

Unit-transfer cases tested:
`25088`.

Recoverable through alternate boundaries:
`25088`.

Nonrecoverable:
`0`.

### Verdict
**H2 CREATES NONTRIVIAL RECOVERY ASYMMETRY.**

Unlike H1, capacity constraints on the alternate path matter. Some states can route the transferred unit around the other three boundaries and recover; others cannot.

Therefore stabilization plus bounded White capacity is sufficient, in this finite realization, to make:
`Rec_I(x) != Red_int(x)`
for some states.

That is the first concrete nontrivial T4 persistence asymmetry.

---

# Why H2 works

The square has two routes between adjacent vertices:

1. the direct boundary;
2. the complementary length-3 path.

When stabilization locks the direct boundary, recovery requires the complementary route.

But every edge transfer obeys:
`0 <= δ <= min(source,1-target)`.

So alternate recovery exists only when all intermediate nodes have enough source occupancy and receiving capacity.

Persistence therefore becomes a joint property of:

- History: which boundary was just used;
- stabilization: which boundary is now locked;
- topology: what alternate paths exist;
- Bandwidth/capacity: whether those paths can carry the required transfer.

This is exactly the kind of T4 asymmetry missing at R21.

---

# New theorem — Cycle-Bypass Principle

If stabilization forbids only the reverse orientation of a used edge while the underlying adjacency contains an admissible alternate cycle, exact recovery may remain possible by routing around that cycle.

Therefore directional locking alone does not imply persistence asymmetry.

# New theorem — Stabilized Boundary Recovery Criterion

For a redistribution `u->v` of amount δ followed by stabilization of boundary `{u,v}`, recovery exists iff the complementary admissible network contains a capacity-feasible flow of amount δ from v back to u.

On the four-address square, this is a length-3 path-flow problem.

This turns T4 recovery into a finite max-flow/capacity question.

---

# Interpretation of `.°.`

The source says stabilization means:
- drift resistance;
- inertial lock;
- recursive persistence retention.

H2 is therefore a plausible **working realization**:

> stabilization reduces the immediately available transformation set by locking the boundary that has just settled.

This is not yet proved to be the unique Genesis meaning of `.°.`.

It is better than arbitrary hysteresis because it directly realizes "lock" as a restriction on future admissible redistribution across the stabilized boundary.

---

# T4 persistence profile now becomes nontrivial

For a state x and stabilized redistribution r, define recovery by capacity-feasible alternate flow.

Some states recover.
Some states fail.

Thus:
`Rec_I(x)` and `Fail_I(x)` are both potentially nonempty.

The R21 universal-recovery collapse is broken.

**R21 can now be resumed under H2.**

---

# Important anti-recursion result

No object was redefined.

- persistence remains recoverable self-return;
- redistribution remains the R16 conservative edge kernel;
- stabilization is instantiated as a restriction of the admissible future transformation set;
- topology remains the second-order Cradle square;
- White bounds remain unchanged.

The only new realization parameter is the stabilization lock rule.

---

# Failure examples

Representative unit transfers that become nonrecoverable under acted-boundary locking:

`[]`

Failure count by conserved block-sum units:
`{}`.

This shows persistence failure is state-dependent rather than uniformly assigned.

---

# Next roadmap step

Resume R21 with H2 and compute complete T4 persistence profiles over all finite states and transfer magnitudes.

Then:

1. quotient states by equal recovery profile;
2. extract recovery-compatible basins;
3. test R23 recovery saturation;
4. stop at the first T5 closure or failure.

Do not modify the stabilization rule during that run.

# Verdict

\[
oxed{	extbf{H1 FAILS; H2 PASSES AS A NONTRIVIAL T4 WORKING REALIZATION.}}
\]

The key mechanism is:

\[
oxed{
	ext{stabilization lock}
+
	ext{alternate-path topology}
+
	ext{bounded transfer capacity}
\Rightarrow
	ext{state-dependent recoverability}.
}
\]
