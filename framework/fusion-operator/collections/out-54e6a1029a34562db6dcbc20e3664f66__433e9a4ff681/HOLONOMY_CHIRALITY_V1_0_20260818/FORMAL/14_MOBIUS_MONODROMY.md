# 14 — Möbius Monodromy

## 1. Source placement

The Transduction live model explicitly places Möbius monodromy as connection holonomy along a Möbius dependency loop.

This gives a formal home to the project's recurring white/black, visible/underside, and local-orientation intuition.

## 2. Möbius base

A standard Möbius carrier can be written

```text
M = ([0,1] x (-1,1)) / ((0,eta) ~ (1,-eta)).
```

It is globally one-sided. “White” and “black” are therefore best treated as local read labels, not globally separate surfaces.

## 3. Orientation monodromy

One circuit around the base reverses the local transverse orientation; a second returns it.

Book candidate: if a transported chirality/identity component is sensitive to this orientation reversal, the loop may carry nontrivial component holonomy.

## 4. White / black / neon work-layer interpretation

Current Rainbow/Basin work uses:

```text
white = coherent / superposed read
black = underside / hidden-spectrum read candidate.
```

For basin anchor `b in (0,1)`, one local neon deformation coordinate is

```text
N_b(eta)=b(1+eta),        -1<eta<=0
N_b(eta)=b+(1-b)eta,       0<=eta<1.
```

This is work-layer mathematics, not recovered canonical Watcher/Genesis-Stone mathematics.

## 5. Holonomy question

The rigorous question is not “is the universe literally a Möbius strip?” It is:

```text
what connection action is accumulated after a loop whose local orientation returns only on a double cover?
```

That is a holonomy/monodromy problem.
