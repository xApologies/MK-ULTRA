# C01 — Layered Chirality Domain

**Verdict:** CLOSED — `TWO-LAYER COMPLEMENT-CHECKERBOARD DOMAIN TYPED; INTER-LAYER PHYSICS UNRESOLVED`

## Direct transcription of the supplied map

Two serialized chirality-byte labels are visibly repeated:

- `A = 10010110`
- `B = 01101001`

They are exact bitwise complements at the serialization level. That fact is about the diagram bytes; it does not by itself prove a physical chirality map.

The left-hand map is represented minimally as two layers `l in {0,1}`. Each layer contains two 2x2 seed domains:

```text
D0 = A B      D1 = B A
     B A           A B
```

Thus the finite diagnostic has 16 seed vertices. The drawing supplies enough geometry to distinguish three candidate adjacency classes: 16 axial edges inside the 2x2 domains, 4 bridges between the two domains in each layer, and 8 corresponding-position inter-layer relations. This gives `|V|=16`, `|E|=28`, and cycle rank `beta_1=13` for the declared diagnostic graph.

The exact physical meaning of the inter-domain and inter-layer lines is **not** promoted from drawing adjacency. They are retained as work-layer constraints to test propagation.

## Typed domain

`D = (V,E,L,b,J,R,Beta,mathcalB,P,H)`

where `L` is layer, `b` is serialized byte, `J` is baseline edge relation, `R` Resolution, `Beta` Bandwidth, `mathcalB` the six basin labels `{R,O,Y,G,B,V}`, `P` persistence status, and `H` History/provenance.

The six basin labels remain labels/capacity inputs only. No numeric physical energy is assigned.

## Fusion-site condition

For the finite diagnostic only, we declare the work-layer bridge `A <-> B = mirror-pair classes` so that the existing Fusion operator can be stress-tested. Under that declaration, all 16 intra-domain axial edges are mirror-class candidates and the 12 inter-domain/inter-layer edges are same-class. **Every actual seam still requires the null/contact port witness demanded by Fusion v1.**
