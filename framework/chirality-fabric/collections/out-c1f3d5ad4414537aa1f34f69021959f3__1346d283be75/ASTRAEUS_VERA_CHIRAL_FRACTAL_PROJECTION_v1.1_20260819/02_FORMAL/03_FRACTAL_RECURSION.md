# 03 - Fractal Recursion and Dimension

## 1. Similarity dimension

For a self-similar system with contraction ratios `r_i`, the similarity dimension s solves

`sum_i r_i^s = 1`.

For b equal contractions with ratio r,

`s = log(b)/log(1/r)`.

When the open-set/separation hypotheses appropriate to a standard self-similar set hold, this equals its Hausdorff dimension.

## 2. Four-branch toy

The CFP-001 symbolic branch rule uses b=4 and r=1/3, giving

`s_4 = log(4)/log(3) = 1.2618595071429148...`.

This number belongs to the recursive branch rule. A geometric profile can preserve it, lower it through overlap/noninjectivity, or fail to expose it if the profile map is too coarse.

## 3. Dimension is not chirality

The similarity equation depends on contraction ratios, not on orientation signs. Mirroring an IFS can preserve all r_i and therefore preserve similarity/Hausdorff dimension while reversing an orientation-sensitive structure.

Thus fractal dimension is useful as a recursive invariant but is generally insufficient as a chirality invariant.

## 4. Multiscale descriptors

Candidate descriptors for later experiments include:

- Hausdorff dimension;
- box-counting/Minkowski dimension;
- information dimension;
- generalized Renyi dimensions D_q;
- multifractal spectrum f(alpha);
- lacunarity;
- graph spectral dimension;
- persistence diagrams across scale;
- branch entropy and transition entropy;
- scale-localized response leverage.

No descriptor is promoted merely because it is computable. It must be tested for invariance under the intended representation family and for predictive relevance to the downstream response.
