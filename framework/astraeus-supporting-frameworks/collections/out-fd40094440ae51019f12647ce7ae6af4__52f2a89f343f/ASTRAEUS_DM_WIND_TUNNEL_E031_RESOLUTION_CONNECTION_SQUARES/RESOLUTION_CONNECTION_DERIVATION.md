# E031 — Resolution Squares as Transduction-Connection Tests

## 1. Source recovery succeeded

The source archive already contains a promoted pre-differential connection architecture.

For a dependency arrow:

`f : U -> V`

and state:

`x in F(U)`,

the live model defines a candidate lift family:

`Lift_f(x)`

and a Transduction Connection:

`Conn(f,x | R,B,H,E,chi)`

that selects an admissible horizontal lift:

`lambda_f,x : (U,x) -> (V,y)`.

For a path:

`gamma = f_n o ... o f_1`,

the connection-generated transport is:

`P_gamma^Conn = lambda_fn o ... o lambda_f1`.

## 2. The six E030 squares fit the source exactly

For every pair of contextual Hydrogen directions `a,b`:

`U = H13`

`V = H13+a`

`W = H13+b`

`Z = H13+a+b`.

The two same-endpoint paths are:

`h o f = a then b`

and:

`k o g = b then a`.

The source square defect is therefore:

`K_square^(a,b)(x)`
`= Def(P^Conn_(b o a)(x), P^Conn_(a o b)(x))`.

There are exactly six such tests.

## 3. Exact null result at the presentation layer

In the E029 ancestry-access model, refinement acts on readable feature sets by set union.

Therefore:

`(S union {a}) union {b}`
`=`
`(S union {b}) union {a}`.

All six Resolution squares commute exactly at the **base/readout presentation level**.

Hence:

`K_base^(a,b)=0`

for all six squares.

This is not a claim that the transported state upstairs is flat.

The source explicitly distinguishes base/dependency path structure from lifted state
curvature.

## 4. The actual dark target is upstairs

The state-level defect remains:

`K_Conn^(a,b)(x)`
`= Def(P^Conn_(b o a)(x), P^Conn_(a o b)(x))`.

Its value is currently open because the current Hydrogen experiment does not yet supply
the candidate lift family or a canonical native lift selector for each refinement arrow.

This is a sharp result:

**any nontrivial path memory cannot come from the Boolean combinatorics of "which
features are visible."**

It must come from the state transported while those Resolution directions are
traversed.

## 5. Bandwidth / Resolution / Connection roles now separate cleanly

The source gives:

- Dependency arrows: where transport may go.
- Connection: how state is lifted along those arrows.
- Bandwidth: which horizontal lifts are available.
- Occupancy: which path is realized.
- History: records the composed lifts.
- Holonomy: what a closed lifted path does.
- Curvature: failure of alternative lifted paths to agree.
- Resolution: which connection/curvature distinctions are readable.

For Hydrogen:

`B_H`

is therefore not the connection.

It constrains:

`Hor_Conn^B_H(H,x) subseteq Hor_Conn(H,x)`.

The connection acts upstairs, then Resolution reads its result.

## 6. Möbius branch

The same live source explicitly states:

`Hol_Conn(gamma)=P_gamma^Conn`

for closed paths and places Möbius monodromy as:

`connection holonomy along the Möbius dependency loop`.

This gives the earlier Rainbow Road / Möbius intuition a precise formal home.

It does not make the six Hydrogen Resolution squares Möbius loops by default.

## 7. Next obligation

The source says a connection is extra structure unless native rules make lift selection
canonical.

Watcher supplies the weakest defensible selection order:

1. preserve ancestry;
2. preserve transported chirality;
3. preserve invariant residue;
4. satisfy operator typing;
5. satisfy Bandwidth/environment/history admissibility;
6. minimize unsupported additional structure.

The next hunt is therefore not "invent a connection."

It is:

`recover the candidate Lift_f(x) families for the Hydrogen Resolution arrows`

and test whether the Watcher rule leaves:
- one unique selected lift,
- multiple admissible lifts,
- or no admissible lift.

Only then can the six `K_Conn` values be evaluated.
