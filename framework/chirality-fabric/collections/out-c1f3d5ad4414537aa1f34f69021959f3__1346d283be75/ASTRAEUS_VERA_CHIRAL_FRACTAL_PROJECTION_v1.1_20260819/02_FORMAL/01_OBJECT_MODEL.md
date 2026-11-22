# 01 - Chiral Fractal Object Model

## 1. Symbolic history

Let `B={0,...,b-1}` be a finite branch alphabet. A finite recursive history of depth D is

`w = i_1 i_2 ... i_D`, with `i_k in B`.

The infinite history space is `H = B^N`. A finite-depth experiment uses `H_D=B^D`.

## 2. Recursive geometry

For a representation/profile p, associate contractions or recursive embeddings

`S_i^(p): X_p -> X_p`.

For history w, the level-D cell is

`S_w^(p) = S_i1^(p) o ... o S_iD^(p)`.

The representation map `rho_p` sends symbolic history to its geometric/readable realization.

## 3. Chirality/history fiber

Attach a fiber state `c(w)` to the recursive history. In the simplest Z2 toy,

`c(w) in {+1,-1}`.

More generally the fiber may be a state in a chirality space `C`, a transport class, a path-history object, or a representation-bearing state.

The source object is therefore not merely a point set. A minimal package is

`F_chi = (H, {S_i}, C, T_chi, A, I, P)`

where:
- H = recursive history space;
- {S_i} = recursive geometric generators;
- C = chirality/history fiber;
- T_chi = admissible chirality transport;
- A = admissibility relation;
- I = declared invariant family;
- P = projection/readout family.

## 4. Projection profile

A readout profile is a map

`Pi_p : F_chi -> Y_p`.

The label `square`, `triangle`, or `circle` names a target/readout family, not the source ontology.

Two distinct source states may satisfy

`x != y` but `Pi_p(x)=Pi_p(y)`.

The correct object of study is the fiber

`Pi_p^{-1}(y) = {x : Pi_p(x)=y}`.

## 5. Identity discipline

This package keeps separate:

- source object;
- recursive history;
- chirality/history fiber;
- representation map;
- projection profile;
- observable/readout;
- equivalence class induced by the projection.

No same-name or same-picture shortcut identifies these objects.
