# R52 — LOCAL CANDIDATE-MAP SIEVE POPULATION FROM ALTERNATE QMO CHAINS

## Goal

R51 closed the local candidate-map sieve:

`S_t = { f:F_t->E | pi_E o f = j_T(t), C o f = 0 }`

and physical candidates:

`S_t^phys = { f in S_t | f injective and inheritance-equivariant }`.

Instead of recovering `j_T` more explicitly right now, R52 crawls alternate source-QMO chains looking for maps that can populate `S_t`.

## Method

The cumulative API/source registry was crawled for:
- embedding;
- inclusion;
- lift;
- section;
- morphism;
- continuation;
- state-bundle maps;
- constraint/kernel maps;
- inheritance maps;
- projection/transport maps.

Candidate objects were ranked by structural relevance, then filtered by the R51 sieve.

## Key result

The search does find multiple **map-like source objects**, but they fall into three different mathematical types:

1. **embedding/inclusion candidates** — strongest possible population sources for `S_t`;
2. **lift candidates** — local transport maps whose codomain may not be the native constraint-kernel fiber;
3. **inheritance/continuation morphisms** — organizational transport maps that need separate proof of base/kernel compatibility.

This matters because R51's sieve prevents us from promoting every source transport map into `s_t`.

## Population rule

For each source map candidate `f`, evaluate:

### Gate P1 — correct domain
Does `f` restrict to `F_t`?

### Gate P2 — correct native base
Does:

`pi_E(f(x)) = j_T(t)`

hold for all `x in F_t`?

### Gate P3 — physical constraint kernel
Does:

`C(f(x)) = 0`

hold?

If P1–P3 pass, the map enters `S_t`.

Then evaluate:

### Gate P4 — injectivity
Is `f|_{F_t}` injective?

### Gate P5 — inheritance equivariance
Does:

`I(f(x)) = f'(I_H(x))`

hold under the appropriate target-fiber continuation?

If P4–P5 also pass, the map enters `S_t^phys`.

## Strongest source branches found

The ranked source search identifies these kinds of branches as the highest-value candidates:

- constraint-preserving embedding families;
- hidden/native state-bundle embeddings or inclusions where present;
- local lift realizations;
- inheritance morphisms;
- continuation operators;
- recursive-inheritance maps.

But the decisive point is this:

**the candidate-map sieve is now reusable across all of them.**

We no longer need one bespoke proof per QMO chain.

Every source map can be fed through the same P1–P5 certification pipeline.

## New QMO closure

Define a reusable certification object:

`Cert_S(f,t) = (P1,P2,P3,P4,P5,evidence)`.

Then:

`f in S_t` iff P1=P2=P3=PASS.

And:

`f in S_t^phys` iff P1=P2=P3=P4=P5=PASS.

This turns local embedding population into a source-agnostic certification problem.

## Why this is useful

The brute-force/Codex strategy the user described becomes straightforward:

1. crawl every map-like QMO in the API;
2. normalize it to a candidate map record;
3. run `Cert_S`;
4. retain passes;
5. append failures with reason;
6. recursively generate downstream QMOs from surviving maps.

This is exactly the right place for a future recursive protocol / blockchain-like QMO generation pass.

## Current status

R52 does **not** claim a fully certified physical `s_t` yet.

What it closes is the machinery for populating the sieve from arbitrary source chains.

The highest-value next move is therefore no longer to manually inspect one map at a time.

It is to run an exhaustive source-map certification crawl.

## Exact next frontier

`@open/exhaustive_source_map_certification`

Input:
all map-like QMO objects.

Output:
- PASS_TO_S_t;
- PASS_TO_S_t_phys;
- FAIL_DOMAIN;
- FAIL_BASE;
- FAIL_KERNEL;
- FAIL_INJECTIVITY;
- FAIL_EQUIVARIANCE;
- INSUFFICIENT_SOURCE_DATA.

This is the first branch in this sequence that is naturally suited to the user's planned future brute-force API crawl.

## Verdict

**CLOSURE OF POPULATION METHOD / OPEN EXHAUSTIVE EXECUTION.**

The roadblock has moved from "find a map" to "run the certification sieve over the entire map landscape."
