# 51 — CONNECTION / LIFT SELECTION ARCHITECTURE

R33 recovers the missing architecture:

\[
\boxed{
\text{History-decorated candidate lifts}
\to
\text{Bandwidth filter}
\to
\text{Connection selection}
\to
\text{KOR realization gate}.
}
\]

## Candidate lifts

For arrow \(f:U\to V\) and state \(x\),

\[
\operatorname{Lift}_f(x)
\]

is the formally admissible lift family.

## Bandwidth restriction

\[
\operatorname{Lift}^{B}_f(x)
\subseteq
\operatorname{Lift}_f(x)
\]

contains only currently available lifts.

Bandwidth does not select among survivors.

## Connection

A connection/selection rule chooses an operative horizontal lift from the Bandwidth-surviving decorated family.

History/provenance are part of the decorated input.

## KOR/A19

Only after connection selection does the witness/completion gate decide whether the resulting event enters completed realized History.

This factorization is a major architectural closure.
