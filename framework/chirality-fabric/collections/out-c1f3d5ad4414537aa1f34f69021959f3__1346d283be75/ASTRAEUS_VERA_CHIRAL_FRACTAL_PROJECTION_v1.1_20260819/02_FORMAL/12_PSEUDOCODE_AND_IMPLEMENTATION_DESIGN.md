# 12 - Pseudocode and Implementation Design

## Algorithm A - Recursive source construction

```text
INPUT: branch alphabet B, depth D, generator family S, hidden-fiber rule C
H <- enumerate B^D
for each history w in H:
    x_latent <- recursive_source_state(w)
    c_hidden <- hidden_fiber_state(w)
    store (w, x_latent, c_hidden)
OUTPUT: finite latent source table
```

## Algorithm B - Projection profile family

```text
for each profile p in {square, triangle, circle, ...}:
    for each latent source state x:
        y[p,x] <- Pi_p(x)
    compute profile collisions / fibers
```

## Algorithm C - Common-fiber audit

```text
for each candidate pair x != y:
    signature(x) <- (Pi_1(x), ..., Pi_m(x))
    if signature(x) == signature(y):
        record unresolved pair
```

For linearized probes, use stacked rank/nullity instead of pair enumeration.

## Algorithm D - Probe design

```text
K <- current common kernel
choose candidate probe P_new
score <- dimension(K) - dimension(K intersect ker(P_new))
prefer probes with largest score subject to validity/cost constraints
```

## Algorithm E - Z2 holonomy audit

```text
recover source-valid graph G
if cycle_rank(G) == 0:
    STOP: ordinary graph-loop holonomy unavailable
choose cycle basis gamma_1...gamma_beta
for each source-valid edge state sigma:
    H_j <- product sigma_e around gamma_j
return holonomy signature H=(H_1,...,H_beta)
```

## Algorithm F - Dark-matter bridge discipline

```text
preserve E056 state
run E057 independent Oxygen probe
if transverse response directions are not cross-probe stable:
    downgrade shared-substrate interpretation
    STOP holonomy/fractal promotion
else:
    recover source-valid cyclic or lifted carrier
    test hidden invariant without refitting it to gravitational data
```
