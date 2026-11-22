# E042 — Direct-Flow Quotient Rebase

## 1. Why the E006 construction-selection branch terminates

E006 deliberately did **not** claim that one endpoint-to-edge lift was physical.

It stress-tested four symmetric surrogates:

- arithmetic mean;
- geometric mean;
- minimum;
- maximum.

All four preserve the basic endpoint symmetries relevant to a nonnegative unoriented
edge load:
- endpoint exchange symmetry;
- idempotence;
- internality;
- monotonicity;
- positive homogeneity;
- nonnegativity.

They differ only by extra algebraic structure that the source never selects.

Therefore no source-preservation rule currently chooses one of the four.

The E041 fact that the corresponding max-TT axes disagree is not a mystery and should
not be optimized away. The tensors are different surrogate realizations.

**Clover ruling:** do not select a physical precursor by choosing among the four E006
endpoint lifts.

## 2. The source already contains the correct upstream edge-flow object

R7/V24 recovers the local finite continuity law:

`Phi_ij = kappa_ij A_ij (C_j-C_i)`.

On a fixed persistent support with incidence map `B_N`:

`phi = -W_N B_N^T c`

and:

`delta C = D_C phi = B_N phi`.

So the source-native object is the realized edge flow `phi`, not an interpolation of
sitewise memory amplitudes.

The E006 endpoint lifts remain robustness diagnostics because the E003 archive did not
serialize the exact source edge-flow coefficients for that pair.

## 3. Direct-channel quotient geometry

V23 proves that the recovered direct gravity channel is blind to pure cycle additions:

`z in ker(D_C)`

implies:

`G_dir(phi+z)=G_dir(phi)`.

Therefore the direct channel factors through:

`Flow / ker(D_C)`.

Define:

`q : Flow -> Flow/ker(D_C)`.

Now define the induced map:

`Dbar_C([phi]) := D_C(phi)`.

This map is:

- well-defined, because representatives differing by a kernel element have the same
  divergence;
- injective, because `Dbar_C([phi])=0` implies `phi in ker(D_C)`;
- surjective onto `im(D_C)` by definition.

Hence:

`Flow/ker(D_C) ~= im(D_C)`.

This is the exact finite-algebra first-isomorphism statement for the direct continuity
channel.

No calculus is used.

## 4. Current Hydrogen pair

For the fixed fresh-vs-H2-conditioned Hydrogen pair, E007 already established:

`||Delta(delta C)_H||_2 = 0.0036081662333576`

and:

`sum Delta(delta C)_H = 0`.

Thus:

`Delta(delta C)_H != 0`.

Inside the controlled fixed-support linear response sector, write:

`Delta(delta C)_H = D_C(Delta phi_H)`.

Then the direct-flow quotient class satisfies:

`[Delta phi_H] != [0]`

in:

`Flow/ker(D_C)`.

So the pair already has a **nonzero source-native direct-flow equivalence class**
without choosing:
- arithmetic vs geometric endpoint lift;
- minimum vs maximum endpoint lift;
- a cycle-flow representative;
- one E006 principal TT axis.

## 5. What E042 removes

The upstream ambiguity:

`which E006 endpoint lift is the real edge flow?`

is no longer an active physical question.

The source says the direct gravity input sees the flow only through its continuity
redistribution class.

The current pair therefore has a construction-independent upstream certificate:

`same [Q_H]`
+
`nonzero [Delta phi_H]_(Flow/ker D_C)`.

The E006/E039/E040/E041 tensor geometry remains useful as a **diagnostic toolkit** for
possible tensor/helicon realizations, but it is not the definition of the source-native
flow class.

## 6. Remaining boundary

E042 does **not** prove readable gravity separation.

The remaining direct seam is still the map from the nonzero continuity-response class
into the admissible gravitational/tensor sector and through the Time-Shell projection.

But the precursor-construction rabbit hole is now cleanly removed from that seam.

## 7. Next dark-matter handle

Advance away from selector construction and ask whether the fixed Hydrogen quantum
fiber contains a **family** of distinct endogenous History/direct-flow classes rather
than only one fresh/conditioned pair.

That is the next useful dark-defect question:

`same [Q_H]`
+
`multiple endogenous History classes`
+
`multiple nonzero direct-flow quotient responses`.
