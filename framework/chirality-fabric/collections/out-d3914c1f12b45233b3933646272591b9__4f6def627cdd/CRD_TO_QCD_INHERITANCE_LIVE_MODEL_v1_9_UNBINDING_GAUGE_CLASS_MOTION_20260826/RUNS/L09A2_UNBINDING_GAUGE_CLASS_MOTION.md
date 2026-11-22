# L09A2 — Unbinding-Induced Gauge-Class Motion

**Verdict: CLOSED — EXACT GAUGE-ORBIT CLASSIFICATION / GAUGE-INVARIANT DEFECT MOTION PASS**

This result is algebraic and independent of the still-open Time-Shell→Q handoff.

## 1. L09A embedding

Let

\[
\eta=\operatorname{diag}(-1,-1,1)\in SU(3).
\]

For seam cochain and vertex reorientation

\[
f\in C^1(G;\mathbb Z_2),\qquad
x\in C^0(G;\mathbb Z_2),
\]

define

\[
r_{f,x}=f+\delta x
\]

and

\[
J_{f,x}(e)=\eta^{r_{f,x}(e)}.
\]

At fixed `f`, changing `x` by a vertex 0-cochain is the exact embedded `Z2` gauge transformation already closed in L09A.

## 2. Gauge-orbit classification

For seam patterns `f,f'`:

\[
\boxed{
J_{f,x}\sim_{\rm gauge}J_{f',x'}
\iff
[f]=[f']\in H^1(G;\mathbb Z_2).
}
\]

### Proof

Gauge equivalence means the exponents differ by a vertex coboundary:

\[
f'+\delta x'
=
f+\delta x+\delta y.
\]

Hence

\[
f'-f=\delta(x+y+x'),
\]

so `[f']=[f]`.

Conversely, if `[f']=[f]`, then `f'-f=\delta z` for some vertex 0-cochain `z`, and that coboundary is absorbed into the vertex gauge transformation.

Therefore the CRD cohomology class exactly labels the gauge orbit in this restricted embedded sector.

## 3. Closed-loop separator

For a graph cycle `gamma` define

\[
\operatorname{Hol}_f(\gamma)
=
\sum_{e\in\gamma}f(e)\pmod2.
\]

A coboundary has zero pairing with a closed cycle, so

\[
\operatorname{Hol}_{f+\delta x}(\gamma)
=
\operatorname{Hol}_f(\gamma).
\]

The embedded loop holonomy is

\[
J_\gamma=\eta^{\operatorname{Hol}_f(\gamma)}
\]

and

\[
\operatorname{Tr}J_\gamma
=
\begin{cases}
3,&\operatorname{Hol}_f(\gamma)=0,\\
-1,&\operatorname{Hol}_f(\gamma)=1.
\end{cases}
\]

For a finite graph over `Z2`, distinct cohomology classes are separated by some cycle. Thus if `[f'] != [f]`, at least one closed-loop parity and Wilson trace changes.

That change is gauge invariant.

## 4. CRD motion splits into two types

### Fixed seam pattern
\[
f\text{ fixed},\qquad x\to x+y.
\]

Result:

\[
\boxed{\text{pure gauge / gauge-fixing motion}.}
\]

### Unbinding changes the seam class
\[
f\to f',\qquad [f']\ne[f].
\]

Result:

\[
\boxed{\text{gauge-invariant orbit transition}.}
\]

If unbinding trivializes the knot,

\[
[f]\ne0\to[f']=0,
\]

then all restricted `Z2` cycle holonomies become trivial and the link configuration is gauge-equivalent to the trivial embedded configuration.

## 5. Physical firewall

Every link still lies in

\[
\{I,\eta\}\subset SU(3),
\]

which is an abelian embedded `Z2` subgroup.

Therefore

\[
[J_e,J_{e'}]=0.
\]

So L09A2 gives genuine gauge-invariant **defect-sector motion**, but not the non-Abelian commutator dynamics of Yang-Mills/QCD.

Correct statement:

\[
\boxed{
\text{CRD unbinding can move between embedded }Z_2\text{ gauge orbits.}
}
\]

Incorrect statement:

\[
\boxed{\text{CRD has already derived QCD.}}
\]

## 6. Roadmap significance

The old fixed-`f` statement must be read locally:

- fixed defect class -> gauge fixing;
- changed defect class -> gauge-invariant orbit motion;
- non-Abelian curvature/self-interaction -> still open;
- physical QFT/QCD readout -> still blocked by L08D1.

This is an independent exact lily pad.
