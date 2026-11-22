# Recovery Context Quotient Theorem — Pass 004

## Construction
Let `H` be the admitted typed History path algebra and `T_rec` the declared recovery-test family. For same-typed histories `h,k`, define

`h ~_Rec k`

iff every declared recovery test gives the same result after every admissible left/right History context in which both composites are defined.

Define the recovery signature

`Sig_Rec(h) := [h]_Rec`.

## Result
1. `~_Rec` is an equivalence relation.
2. Because equivalence is quantified over all admissible composition contexts, it is a History congruence.
3. Therefore `[h2]_Rec ⊙ [h1]_Rec := [h2 o h1]_Rec` is well-defined.
4. The quotient preserves every distinction observable by the declared recovery-test family.
5. Any other compositional recovery-sufficient signature must distinguish at least every pair distinguished by this quotient; therefore the quotient is the coarsest/minimal such signature relative to the declared test family.

## Guard
This is an abstract minimality result. It does not prove that the source `Sig_Hol` tuple, or any finite field subset, realizes the quotient. Full ordered History/provenance remains recoverable upstream.
