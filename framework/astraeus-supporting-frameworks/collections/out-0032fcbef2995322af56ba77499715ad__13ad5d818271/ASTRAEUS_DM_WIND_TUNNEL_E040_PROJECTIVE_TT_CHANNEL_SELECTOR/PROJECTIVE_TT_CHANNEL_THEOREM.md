# E040 — Projective TT Channel Geometry and Selector No-Go

## 1. Natural channel space

For a nonzero symmetric trace-free tensor `S`, a conventional TT projector depends on
a propagation direction `n`.

But:

`P_TT(n) = P_TT(-n)`.

Therefore the direction variable is naturally an **unoriented line**:

`[n] in RP^2`

rather than an oriented vector in `S^2`.

Chirality may later lift this projective channel to an oriented one only if the
chirality/identity data actually distinguishes `n` from `-n`.

That orientation lift is not assumed.

## 2. Exact silent-axis theorem for a biaxial STF tensor

Let `S` have three distinct eigenvalues:

`lambda_1 < lambda_2 < lambda_3`

with orthonormal eigenvectors:

`e_1,e_2,e_3`.

A TT-silent direction satisfies:

`TT_n(S)=0`.

Geometrically this means that the restriction of `S` to the plane `n^perp` is
isotropic.

For a biaxial tensor, such a plane must contain the middle eigenvector `e_2`.
The second transverse direction lies in the extreme-eigenvector plane
`span(e_1,e_3)`.

Solving the circular-section condition gives two projective silent axes:

`n_±`
`= sqrt((lambda_2-lambda_1)/(lambda_3-lambda_1)) e_1`
`  ± sqrt((lambda_3-lambda_2)/(lambda_3-lambda_1)) e_3`.

The signs `n` and `-n` are already identified projectively.

Therefore the silent set is exactly:

`Z_TT(S) = {[n_+],[n_-]}`.

The supported TT channel space is:

`U_TT(S) = RP^2 \ Z_TT(S)`.

So for a generic/biaxial STF precursor the channel space is a continuum with only two
projective silent axes removed.

## 3. E006 result

All 12 E006 trace-free precursor tensors have three distinct eigenvalues.

Therefore every one has:
- exactly two projective TT-silent axes;
- a nonempty open continuum of TT-supported channels.

The analytic axes reproduce the E038 numerically minimized silent directions to
floating-point precision.

## 4. Exact uniqueness no-go from TT geometry alone

Because:

`U_TT(S)`

contains infinitely many supported projective channels, the tensor plus TT support
condition alone cannot define a unique gravitational channel.

This is not a failure of the precursor.

It is a proof that **selection requires additional structure**.

No scalar threshold or extra calculus fixes that mathematical underdetermination.

## 5. Chirality / holonomy role

Holonomy & Chirality gives the missing kind of structure, but not yet an instance
selector.

The source architecture says:

`chirality structure`
-> `allowed spectral mode`
-> `admissible update`.

It also requires:
- ancestry preservation;
- chirality admissibility;
- residue preservation;
- Bandwidth supportability;
- History/holonomy coherence;
- minimal unsupported structure.

Thus the gravitational channel should first be treated as a **filtered channel family**,
not as one arbitrary direction.

Candidate object:

`C_g(x,S)`
`= {([n],m) |`
`    [n] in U_TT(S),`
`    m is an allowed helicon/spectral mode,`
`    chirality/residue/Bandwidth/History constraints pass }`.

Only if this set contains one equivalence class may a unique selector be claimed.

## 6. Existence / uniqueness status

TT-support existence:
**CLOSED.**

Full source-valid gravitational channel existence:
**OPEN**, because the instance helicon mode and supportability/transport filters are not
fully evaluated.

Uniqueness:
**NOT DERIVABLE** from TT geometry and current source state.

This is the exact result the hunt needed.

The frontier is no longer:
"find a direction with TT support."

It is:
"instantiate the source filters that reduce the projective TT channel family."
