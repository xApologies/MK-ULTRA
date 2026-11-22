# 07 - Finite Identifiability Theorems and Lemmas

## Theorem T-CFP-1: Projection Non-Identity

If `Pi:X->Y` is noninjective, then a readable profile y does not uniquely identify its source object.

**Proof.** Noninjectivity means there exist x1 != x2 with Pi(x1)=Pi(x2)=y. QED.

## Theorem T-CFP-2: Common-Kernel No-Recovery

Let `P_i:V->W_i` be linear probes and `O=[P_1;...;P_m]`. If `h != 0` lies in `ker O`, then x and x+h are exactly indistinguishable under every P_i.

**Proof.** `O(x+h)=Ox+Oh=Ox`. QED.

## Theorem T-CFP-3: Admissible Linear Recovery Criterion

For an admissible linear difference space S, O is injective on S iff `ker O intersect S={0}`.

**Proof.** Standard kernel criterion for injectivity restricted to S. QED.

## Theorem T-CFP-4: Z2 Gauge-Class Count on a Connected Graph

For a connected graph with beta_1=E-V+1, Z2 edge assignments modulo vertex gauge have `2^beta_1` classes.

**Proof sketch.** There are 2^E edge assignments. Vertex gauge has 2^V assignments, but the global sign acts trivially, leaving 2^(V-1) effective transformations. The action is free on a connected graph, so the quotient has 2^(E-V+1) classes. Equivalently the quotient is H^1(G;Z2). QED.

## Corollary T-CFP-4a: Tree Triviality

A connected tree has beta_1=0 and therefore one Z2 gauge class. No loop-holonomy bit survives.

## Theorem T-CFP-5: Cantor-Product Projection Dimension Drop

For the standard product `C^5` and coordinate projection to `C^3`, the source and target Hausdorff dimensions are respectively `5 log2/log3` and `3 log2/log3`; the dropped product fiber contributes `2 log2/log3`.

This theorem belongs to the self-similar toy, not to physical MK43 dimensionality.

## Lemma L-CFP-1: Dimension Blindness to Mirror Sign

If two self-similar systems differ only by orientation-reversing isometries while retaining the same contraction ratios and separation structure, their similarity dimension is identical. Therefore dimension alone cannot recover chirality.

## Lemma L-CFP-2: Resolution Cannot Undo Exact Quotient Loss

If Pi(x)=Pi(y) exactly, decreasing numerical measurement tolerance on Pi cannot distinguish x and y. Any recovery requires an additional observable, a different projection, or a prior restriction excluding one state.
