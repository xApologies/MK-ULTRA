# ASTRAEUS Dark-Matter Wind Tunnel E006
## Native Edge-Flow -> Symmetric Rank-Two Continuity Tensor

**Status:** work-layer mathematical closure of the rank-two input type  
**Exact physical A_g selection:** still open  
**Physical dark-matter witness:** NOT ESTABLISHED  
**Parent/API promotions:** 0

## Result

The source stack already provides:
- an admissibility graph with oriented/embedded neighboring states;
- native continuity flow `Phi_ij` on admissible edges;
- a target-neutral local flow law;
- the graviton chain `delta C -> tensor-mode admissibility -> TT -> Pi_T -> h_mn`.

E006 supplies the missing **minimal graph-geometric rank-two constructor**:

`C2 = sum_e L_e (n_e tensor n_e)`.

Its trace-free component

`C2_0 = C2 - tr(C2)/3 I`

is the geometry-first anisotropic continuity tensor candidate.

It is:
- symmetric by construction;
- invariant to reversing an edge label;
- covariant under spatial/orientation rotation;
- trace-normalized to total directional edge load;
- exactly zero for an isotropic constant-field control.

## Endogenous E003 test

The constructor was applied to the E003 H2-conditioned-minus-fresh ER history.

E003 stores sitewise environment-memory fields rather than explicit edge `Phi_ij`.
Therefore the finite-grid realization was deliberately stress-tested under four
different **symmetric endpoint-to-edge lifts**:

- arithmetic mean
- geometric mean
- minimum
- maximum

No lift was selected to optimize the result.

For every one of the 12 field/lift combinations
(3 endogenous memory fields x 4 lifts):

`||C2_0|| > 0`.

Therefore the rank-two anisotropy is not an artifact of choosing one endpoint
interpolation.

### Trace-free norm ranges

- `adjacency_memory`: `0.036800 .. 3.552137`
- `corridor_memory`: `0.516378 .. 9.308210`
- `persistent_memory`: `0.021336 .. 3.035570`

## Validation

- isotropic-null controls: **PASS**
- x/y rotation covariance: **PASS**
- edge-orientation sign invariance: **PASS**
- unit-edge trace identity: **PASS**
- all endogenous field/lift combinations rank-two anisotropic: **PASS**
- each field/lift combination has a nonzero standard TT diagnostic for at least
  one tested direction: **PASS**

The TT operation remains a diagnostic here. E006 does not silently promote the
derived tensor into the physical gravitational sector.

## Closure ruling

E005's open question was:

`Can a source-native continuity redistribution be given a legitimate symmetric
rank-two geometric representation before TT projection?`

At the **mathematical/type level**, E006 answers **YES**.

The source-native object is edge flow.
The dyadic edge-direction lift is sufficient to construct a symmetric rank-two
continuity-load tensor without calculus.

The remaining gravity question is no longer "where does rank two come from?"

It is:

> Which subset/mode of this rank-two continuity redistribution is admitted by
> the MK43 gravitational helicon / tensor-mode admissibility rule?

## Next handle

`RECOVER_GRAVITATIONAL_HELICON_MODE_SELECTION_ON_C2`

The source already says the graviton is the gravitational member of the native
helicon-mode family, produced by substrate-bias deformation -> orientation
restructuring -> continuity redistribution. The next parse will use that source
to determine whether the endogenous E003 continuity tensor has a gravitational
helicon-mode component before applying the Time-Shell projection.
