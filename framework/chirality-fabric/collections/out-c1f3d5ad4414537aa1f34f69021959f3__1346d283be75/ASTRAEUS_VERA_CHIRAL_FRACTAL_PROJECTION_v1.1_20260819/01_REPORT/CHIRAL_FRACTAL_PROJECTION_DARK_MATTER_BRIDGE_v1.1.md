# CHIRAL FRACTAL PROJECTION AND HIDDEN-STATE RECOVERY
## A controlled mathematical bridge from MK43 projection geometry to the Astraeus dark-matter work layer

**Release:** CFP-001 / v1.1 (language/recovery revision; experiments unchanged from v1.0)  
**Date:** 2026-08-19  
**Project roles:** Genesis - origin and scope; Astraeus - mathematical architecture and experiment design; Vera - audit, provenance, negative-result gates, and status discipline.  
**Status:** Candidate mathematical work layer. Finite toy experiments complete and unchanged from v1.0. This revision changes explanatory language, recovery aids, and source cross-links only. No physical or dark-matter promotion.

---

# Abstract

This report develops a recovery-grade mathematical formulation of a simple observation: a readable projection profile does not uniquely identify the object that generated it. The motivating toy is a child's shape sorter. A square aperture classifies the profile presented at the boundary; it does not prove that the upstream object is ontologically a square. A richer object may present the same admissible profile, and one object may present different profiles under different readout maps.

The report turns that intuition into a controlled program combining recursive/fractal geometry, projection fibers and kernels, finite inverse problems, chirality/history transport, Z2 graph holonomy, and scale-dependent dimension. It then maps the resulting mathematics to Astraeus's dark-matter work layer without upgrading the analogy into a physical claim.

Two pieces of vocabulary are central in this revision. First, `E056` and `E057` are experiment labels: E056 is Experiment 056 in the append-only dark-matter work layer; E057 is the next cross-probe experiment. Second, the small state component left after compressing the E056 weighted-tree state to its dominant coordinate `q` is called the **transverse state residue** (or simply the **residue**) in this report. This is a local compression term. It is distinct from a numerical **fit residual**, and it is also distinct from the canonical MK43 term **Invariant Residue** used in the Transduction/Residue-Bundle mathematics.

The central finite results are: (1) three deliberately chirality-insensitive square/triangle/circle readouts can remain exactly degenerate under a hidden chirality-fiber flip; (2) a stacked family of shape probes can still retain a nontrivial common kernel, so additional Resolution of those same probes cannot recover the hidden state; (3) on K4, all 64 Z2 edge-sign assignments reduce to exactly 8 vertex-gauge classes, completely identified by three independent cycle-holonomy bits; (4) a tree has cycle rank zero, so ordinary graph-loop holonomy cannot be carried by cycles of the E056 weighted corridor merge tree itself; (5) a self-similar five-factor Cantor product provides an exact mathematical 3+1+1 toy in which a coordinate projection to the three occupancy factors removes `2 log(2)/log(3) = 1.261859507143` units of Hausdorff dimension associated by label with chirality/history fibers; and (6) E056 supplies a quantitatively analogous identifiability warning: only `0.021306%` of weighted-tree displacement energy lies in the transverse state residue, yet a q-only response map misses `2.446706%` of response energy. The associated response-leverage ratio is approximately `114.84x`.

The dark-matter conclusion remains deliberately limited. CFP-001 does not establish that the E056 residue is chirality, holonomy, a hidden fractal dimension, or dark matter. It gives a formal language for asking whether response-bearing information omitted by one compressed readout belongs to the underlying state and can be recovered by independent probes. E057 therefore remains the immediate dark-matter priority.

---

# Executive determination

## What was recovered from the existing framework

The 987-page MK Ultra Tome separates upstream chirality from its downstream orientation/readout representations, treats recursion as generative organization across depth, and explicitly warns that a noninvertible projection can erase distinguishability. Volume XIII's information-conservation chapter gives the generic mathematical boundary directly: a many-to-one projection can map distinct source states to one readout, and the unresolved linear directions of a projection form its information-loss kernel. The Holonomy and Chirality book independently recovers the mechanism that readable closure can coexist with chirality nonclosure. E056 then supplies a concrete finite response problem in which a nearly one-dimensional morphology trajectory still requires a small transverse **state residue** to preserve the direct-flow response.

## What is new in CFP-001

CFP-001 does not rewrite those sources. It composes them into a new finite mathematical experiment:

1. represent the source as a recursive symbolic history with a hidden chirality/history fiber;
2. map one source through multiple projection profiles;
3. compute the common projection kernel/fiber;
4. distinguish loss by Resolution from loss by quotient/projection;
5. recover hidden path information with independent cycle holonomy where cycles actually exist;
6. establish the tree-cycle holonomy gate (acyclicity result) before applying loop-holonomy language to E056;
7. quantify a 3+1+1 self-similar hidden-dimension toy;
8. define an observability/probe-rank program for future dark-matter work.

## Primary result

**Object identity cannot be assigned from one readable projection profile unless the projection is injective on the admissible source family.**

In finite linear form, if `O=[P_1;...;P_m]` is the stacked readout operator and `S` is the admissible difference space, exact recovery requires

`ker(O) intersect S = {0}`.

If a hidden chirality/history direction remains in the common kernel, no increase in numerical precision of the same readouts can recover it. A new probe must be sensitive to that direction.

## Dark-matter relevance

E056 is an unusually clean example of why this matters. Its dominant weighted-tree coordinate is an excellent History-order coordinate, but not a sufficient linear response coordinate. The small transverse weighted-tree state residue is much more response-bearing than its morphology-energy share suggests. CFP-001 gives that phenomenon an inverse-problem interpretation: compression to q omits a response-relevant residue. The residue is not noise and is not discarded; it is simply the component not represented by q.

That is an analogy supported by the finite mathematics. It is **not** yet a dark-matter mechanism.

---

# 0. Plain-language navigation: what the experiment labels and terms mean

This section is the reader-facing map for the rest of the report. It does not replace the formal development.

## 0.1 What are E056 and E057?

`E056` means **Experiment 056** in Astraeus's append-only dark-matter work layer. It is not an equation and not a physical constant. E056 tested whether a compact weighted-tree state could reproduce an earlier direct-flow response. `E057` means **Experiment 057**, the next planned cross-probe test using the existing source-neutral Oxygen readouts.

## 0.2 What is q?

The E056 tree state has 14 weighted coordinates. Principal-component analysis finds one dominant direction. The scalar coordinate along that direction is called `q`. Along the tested History orbit, q carries approximately `99.978694%` of the weighted-tree displacement energy.

This makes q an excellent compact coordinate for the dominant tree motion. It does **not** make q the complete state.

## 0.3 What is the residue?

Write the centered tree state schematically as

`x = q v_H + r_perp`.

`q v_H` is the dominant component. `r_perp` is the **transverse state residue**: the part of the tree state not represented by q. In E056 the residue carries approximately `0.021306%` of the weighted-tree displacement energy.

The word residue is intentionally neutral. It does not mean noise, error, irrelevance, or quantum uncertainty. It means only: **what remains after this particular compression**.

The residue is not recoverable from q alone because q, by construction, does not encode it. The full 14-weight tree still contains the residue and, under the tested E056 map, the full tree reproduces the direct-flow response to the archival reconstruction floor. Therefore E056 demonstrates compression loss, not fundamental nonrecoverability.

## 0.4 State residue versus fit residual

These are different objects:

- **state residue** `r_perp`: the transverse part of the tree state omitted by q;
- **fit residual**: the difference between an observed response and the response predicted by a reduced model.

For E056, q alone leaves a global response-vector fit residual of about `15.6419%`. Squaring that norm ratio gives the corresponding missed response-energy fraction of about `2.446706%`. These numbers describe response reconstruction error; they are not the size of the state residue itself.

## 0.5 What is holonomy?

Holonomy is **path memory**. Transport a state around a closed path and return to the same readable endpoint. If the transported state does not return to the same formal class, the loop carries nontrivial holonomy. A readable endpoint can therefore close while a finer state/history distinction remains.

Astraeus's existing *Holonomy & Chirality* mathematics already contains this architecture. It also contains a downstream **Residue Bundle Connection**. This report does not identify the E056 transverse state residue with that canonical Invariant Residue; it records the possible interface as an open question.

## 0.6 What does the tree-cycle holonomy gate say?

The E056 merge object is a tree. A tree has no graph cycles. Therefore ordinary **graph-loop** holonomy cannot be stored in cycles of that tree itself. This is an acyclicity result, not a chirality failure and not a general holonomy failure. If holonomy becomes relevant to E056, its carrier must instead be a lifted transport square, a source-valid cyclic network upstream of the tree, or an attached state/history fiber.

## 0.7 Why E057 matters

E057 changes the probe. If Oxygen independently requires the same response-bearing state residue found under Hydrogen, that strengthens the case that the residue belongs to a shared underlying state rather than to one probe-specific encoding. If Oxygen does not preserve it, the interpretation must be downgraded.

The plain-language sequence is therefore:

`dominant state q -> small residue -> residue strongly affects response -> change the probe -> test whether the same residue survives`.

---

# 1. Source and provenance architecture

The release is source-preserving. Exact copies of the current API 4.3 source archive, E056 archive, Reader's Companion, and the five live Astraeus mathematics books are bundled in `07_SOURCE_PROVENANCE/`. The live mathematics set is Transduction Geometry v1.0, Bandwidth Algebra v1.0, Resolution & Readout v1.0, Identity Through History v1.0, and Holonomy & Chirality v1.0. The full 987-page Tome is not duplicated because its source file is approximately 67 MB and would unnecessarily push the recovery package toward the transfer ceiling; instead its SHA-256 and exact page/volume anchors are recorded in `SOURCE_MAP.md`.

Primary source SHA-256 values:

- Tome: `cca59f71a28079fb6fc511df7b811a88b7e3fde97d84bc1f299c3f4b86b12e8d`.
- Reader's Companion: `7918d5213804cf8abd5a8113eb5a1df5d45722f66c06bcb3f6e8b8f578b9a9fa`.
- API 4.3 archive: `0010a4de99d78748ede57670b3bca1df6185b7ba8dd0faf266cc3ba1a4ccf752`.
- Holonomy and Chirality archive: `433e9a4ff681ddf33839530a67551db58d08ad99ea012f76adf00fc2d72d74a6`.
- E056 archive: `d1c243191a4ddbdc5e9a8759be08441607f861bed1ebb13d61669b03ef2ebc44`.

The release makes four evidence classes visually and structurally distinct:

- **SOURCE-RECOVERED:** text/equations/status from the supplied MK43/Tome/Holonomy/E056 corpus.
- **EXTERNAL MATHEMATICS:** standard fractal geometry, graph topology, linear algebra, gauge-equivalence, and inverse-problem facts.
- **CFP-DERIVED:** the new finite constructions and theorems proved inside the declared toy models.
- **PHYSICAL CANDIDATE:** any proposed connection to dark matter, Planck-scale geometry, chirality as a physical field, or gravitational response.

No result moves from one class to another merely because it is aesthetically compatible.

A language crosswalk added in v1.1 is especially relevant:

- *Resolution & Readout* supplies quotient/readout fibers and the rule that readout may merge formal distinctions but does not create them.
- *Identity Through History* separates persistence from endpoint recovery and explicitly carries history residue/witness structure.
- *Holonomy & Chirality* supplies hidden-holonomy visibility and `FORMAL/13_RESIDUE_BUNDLE_CONNECTION.md`, where an invariant-residue fiber is assembled after projection.
- *Bandwidth Algebra* supplies ordered corridor/path words whose histories can remain distinct even when downstream readouts coincide.
- *Transduction Geometry* supplies the umbrella projection/recovery/holonomy definitions and jointly-separating recovery-family language.

The report keeps the E056 **transverse state residue** distinct from MK43 **Invariant Residue** unless a future typed map proves an interface.

---

# 2. The shape-sorter problem as a mathematical inverse problem

Consider a boundary with a square aperture. A child presents an object and the object passes through. The boundary has certified only that the presented cross-section or projection lies in the square-admissible profile class. It has not certified the complete source object.

This can be written without any MK43 terminology. Let `X` be a source-state set, `Y_square` the square-profile readout space, and

`Pi_square : X -> Y_square`.

If `Pi_square` is noninjective, then a square profile has a non-singleton preimage. A conventional square, a carefully oriented higher-dimensional object, or a recursively structured source can all lie in that preimage if the map admits them.

Now provide several apertures/readouts:

`Pi_square`, `Pi_triangle`, `Pi_circle`.

The source family compatible with all three observations is

`A(y_sq,y_tri,y_cir) = Pi_square^-1(y_sq) intersect Pi_triangle^-1(y_tri) intersect Pi_circle^-1(y_cir) intersect X_admissible`.

The family shrinks only if the readouts are independently informative. Three redundant projections can preserve the same hidden fiber. Therefore **number of views is not the correct invariant; reduction of the common fiber is**.

This is the mathematical form of the user's projection-profile distinction. The hole classifies a presentation. It does not define the source ontology.

---

# 3. Why recursion and fractal geometry are natural here

A recursively generated object contains information at multiple depths. Instead of assigning one global geometric label, define a branch history

`w=i_1...i_D`.

At each depth the state is inherited through an admitted generator. The same symbolic history can be realized by different geometric representation maps. That gives a controlled way to separate:

- the recursive history itself;
- the geometry used to draw it;
- the chirality/history state transported along it;
- the projection presented to a downstream boundary.

Fractal geometry is useful because it supplies quantitative invariants of recursive organization that need not coincide with the ambient topological dimension or with a visible shape label. It also makes failure modes explicit: a noninjective embedding or overlapping IFS can reduce geometric dimension; a reflection can reverse orientation while leaving contraction ratios and similarity dimension unchanged; a coordinate projection can discard an entire self-similar factor.

The report therefore uses fractals as a **controlled laboratory for representation loss**, not as a declaration that physical spacetime is a fractal.

---

# 4. CFP-001 finite experiment suite

The experiment is deterministic and reproducible. The seed is `430056`. All code is included under `03_EXPERIMENT/` and all generated tables under `06_DATA/`.

## 4.1 Common latent history, three readable profiles

CFP-001 enumerates all `4096` histories in a four-symbol alphabet at depth 6. Each symbol is mapped to two Cantor digits, yielding a standard finite approximation to the Cantor dust `C x C` for the square profile. The same finite source histories are then mapped into triangle-like and circular/annular profile coordinates.

The purpose is not to prove that all three geometric transforms preserve Hausdorff dimension. The purpose is to demonstrate that one symbolic source can support several visually different readouts while retaining a separately stored hidden chirality/history state.

Three figures in `05_FIGURES/` show the square, triangle, and circle profile families.

## 4.2 Hidden chirality-fiber degeneracy

The finite source assigns each history a deterministic hidden `+1/-1` chirality value. The three shape-profile maps intentionally ignore that fiber. A global chirality-fiber flip therefore changes the latent state while changing no profile coordinate.

Measured maximum coordinate difference after the hidden-fiber flip:

- square profile: `0.0`;
- triangle profile: `0.0`;
- circle profile: `0.0`.

This is an engineered degeneracy and therefore not a discovery. Its value is logical: it proves that **multiple projections do not guarantee recovery when their definitions share a common blind direction**.

## 4.3 Probe-rank experiment

A second finite toy uses an 8-dimensional latent vector. The first four coordinates are shape-visible; the final four are labeled chirality/history transverse coordinates. Square, triangle, and circle measurement matrices inspect only the first four coordinates.

After stacking all three shape probes:

- rank = `4`;
- nullity = `4`.

The package includes an explicit nonzero latent difference that produces exactly zero difference in all shape readouts. Four targeted chirality/history probes are then added. The full stack reaches:

- rank = `8`;
- nullity = `0`.

The lesson is precise: the hidden state is recovered because the new probes point into the old common kernel, not because the system accumulated more samples of the same readout.

## 4.4 K4 Z2 holonomy enumeration

The third experiment makes path dependence exact. K4 has 4 vertices, 6 edges, and cycle rank 3. Every edge receives a sign `sigma_e in +/-1`. Vertex gauge flips act as `sigma_uv -> g_u sigma_uv g_v`.

The code exhaustively enumerates all 64 edge-sign states. It finds:

- `64` assignments;
- `8` gauge-equivalence classes;
- `8` independent three-cycle signatures;
- each class contains `8` raw assignments.

Thus three independent cycle products recover the gauge class exactly in this finite model. An unsigned geometric projection of K4 would see the same vertices/edges for every assignment and would therefore collapse all eight hidden classes into one visible graph.

This is a mathematically clean realization of a hidden-history carrier.

## 4.5 Tree-cycle holonomy gate (acyclicity result)

The result cannot be copied directly onto the E056 merge tree. A connected tree has cycle rank zero. In the Z2 model, every edge-sign assignment on a tree can be removed by vertex gauge. Therefore no nontrivial ordinary loop-holonomy class exists on the tree itself.

This is an important Vera gate because it prevents a seductive but false shortcut. If E056 eventually participates in a holonomy explanation, the holonomy must live in a lifted transport space, the pre-tree source network, or an attached fiber - not in cycles of the tree.

---

# 5. The hidden fractal dimension construction

The report contains one exact self-similar toy designed to test the playful claim that a projection can hide a 'dimension nobody sees.'

Let C be the middle-third Cantor set with

`d_C = log(2)/log(3) = 0.630929753571457`.

Build

`X = C_occ1 x C_occ2 x C_occ3 x C_chi x C_hist`.

The factor labels are chosen to mirror the project's 3+1+1 organizational language, but the object is ordinary product-set mathematics.

The source dimension is

`dim_H X = 5 d_C = 3.154648767857287`.

Project to the first three factors:

`Pi_occ(X)=C^3`,

with dimension

`3 d_C = 1.892789260714372`.

The coordinate projection has removed a chirality/history product fiber of dimension

`2 d_C = 1.261859507142915`.

This is a real mathematical dimension loss under projection. It is **not** a claim that nature contains 3.1546 spatial dimensions, that the Planck landscape is a Cantor product, or that dark matter lives in 0.6309-dimensional fibers. The construction proves only that a quantitatively meaningful scaling dimension can belong to a source object and be absent from a chosen downstream readout.

That is enough for the conceptual purpose.

---

# 6. Dimension is insufficient to identify chirality

Fractal dimension is useful precisely because it is not the same object as chirality. If a self-similar system is mirrored while retaining the same contraction ratios, the similarity-dimension equation is unchanged. Under suitable separation hypotheses the Hausdorff dimension is also unchanged.

Therefore two recursively organized structures can satisfy

`D(F_chi)=D(F_mirror)`

while remaining distinguishable by an orientation-sensitive or path-sensitive invariant.

A viable source fingerprint therefore needs multiple kinds of structure. CFP-001 proposes the schematic tuple

`I(F) = (D_scale, H_chi, C_connect, P_persist, S_spectrum, ...)`.

No particular tuple is promoted. The point is methodological: a scalar dimension cannot carry every distinction that a recursive source may possess.

---

# 7. Holonomy as hidden path information

The existing Holonomy and Chirality source book is especially relevant because it already separates readable base closure from chirality closure. A closed readable path may return to the same coarse state while the transported chirality state returns in a different equivalence class.

CFP-001 realizes the simplest finite analogue using Z2 edge transport. Loop products survive vertex re-expression while unsigned geometry does not see them. That makes holonomy a plausible mathematical language for information that belongs to path/history rather than endpoint label.

The physical burden remains substantial. A future dark-matter use requires:

1. a source-authoritative carrier graph or transport category;
2. actual alternative paths or squares;
3. a typed connection/transport rule;
4. a nontrivial loop defect;
5. a demonstrated relation from that defect to the already observed response difference;
6. preservation of the distinction through the gravitational handoff;
7. a frozen external observable.

A negative flat-holonomy result would eliminate the mechanism cleanly.

---

# 8. Projection loss, information conservation, and recoverability

The Tome's information-conservation sector makes a distinction that is central here: trace or total-probability preservation is not the same as recoverable information. A many-to-one projection can preserve some global quantity while erasing microscopic distinguishability.

CFP-001 uses the same logic. For a linear projection P, the unresolved directions are `ker P`. For a nonlinear projection, the analogue is the preimage fiber. Exact source recovery requires either:

- injectivity on the admissible source family;
- extra measurements that shrink the common fiber;
- an auxiliary record that preserves the erased coordinate;
- a decoder operating on a restricted code/admissible space where the map becomes injective.

This distinction also clarifies the meaning of Resolution. Increased sampling density or lower numerical tolerance can recover details that remain encoded but blurred. It cannot reconstruct a variable that a chosen readout definition never encoded. Whether another independent readout can recover that variable is a separate observability question.

---

# 9. Dark-matter bridge to E056

## 9.1 E056 is Experiment 056

E056 is the anchor for this bridge. It is a completed dark-matter work-layer experiment, not a symbol introduced by the fractal toy. E056 tested a fixed 14-weight corridor-tree state against the earlier E043 direct-flow quotient response.

The centered tree state can be decomposed as

`x = q v_H + r_perp`,

where `q v_H` is the dominant History-aligned component and `r_perp` is the **transverse state residue**.

The key numbers are:

- dominant q/PC1 share of weighted-tree displacement energy: approximately `99.978694%`;
- transverse state-residue share: `0.000213059639633695` = `0.021306%`;
- q-only global response-vector fit residual: `0.15641948935` = `15.641949%`;
- response energy missed by q/PC1: `0.0244670566486609` = `2.446706%`;
- response-leverage ratio `2.446706 / 0.021306`: approximately `114.836656`;
- PC4 global response-vector fit residual: `0.000274412754911`;
- full tested tree-history rank required to move below the E043 archival reconstruction floor: `12`;
- full-tree global response residual: `5.65740770984e-08`.

The important result is not that the residue is large. It is extremely small in tree-displacement energy. The result is that the response is disproportionately sensitive to it.

## 9.2 What E056 does and does not establish

E056 establishes **compression loss under q**: q is an excellent dominant coordinate, but q alone is not a sufficient response state. The full weighted tree retains the residue and reconstructs the tested response to the archival floor.

Therefore:

`residue not encoded by q` does not mean `residue absent from the full state`, and it does not establish fundamental nonrecoverability.

The correct v1.1 language is:

**full tree = dominant q component + transverse state residue.**

The word residue here is descriptive, not dismissive. It is not classified as noise.

## 9.3 Controlled projection analogy

CFP-001 reads q-compression as analogous to a projection profile: the dominant coordinate preserves almost all visible tree displacement while omitting a small response-bearing component. That component behaves like information outside the reduced coordinate.

This analogy is useful for probe design. It does **not** establish that the E056 residue is a projection kernel in a physical sense, nor that it is chirality, holonomy, a hidden fractal dimension, or dark matter.

## 9.4 Why the Holonomy & Chirality mathematics helps

The source book already distinguishes readable closure from lifted state closure and includes a **Residue Bundle Connection**. In that downstream construction, an invariant-residue fiber is associated with the preimage of a projection. This gives a mathematically native place to ask whether a response-bearing residue can later acquire a connection/curvature interpretation.

However, the source book also requires a valid carrier. The E056 merge tree is acyclic, so ordinary graph-loop holonomy cannot live in cycles of the tree. Holonomy remains available only on a source-valid cyclic carrier, a same-endpoint lifted transport square, or an attached fiber.

## 9.5 Why fractal geometry may be useful but is not yet required

The weighted merge tree is recursively organized across merge levels, so scale-dependent descriptors are mathematically natural. Fractal/multifractal descriptors could test whether the response-bearing residue has a stable recursive signature across scale.

E056 does not require a fractal explanation. The existing 14-weight vector already preserves the tested response to archival precision. Fractal analysis earns its place only if it provides stronger cross-probe stability, a lower-dimensional sufficient state without response loss, a representation-stable invariant, or a frozen out-of-sample prediction unavailable from the existing tree coordinates. Otherwise it is decorative reparameterization.

## 9.6 Why E057 remains first

E057 is Experiment 057: the planned Oxygen cross-probe test. It changes the readout rather than adding another Hydrogen fit.

If Oxygen independently requires the same response-bearing residue, the residue becomes more plausibly shared substrate information. If Oxygen uses a different residue but a stable combined latent state exists, the multi-probe model becomes the next object. If Oxygen destroys the relationship, the E056 interpretation must be downgraded to probe-specific.

CFP-001 therefore supports E057; it does not replace it.

---

# 10. Proposed post-E057 experimental program

## Stage A - Cross-probe observability

Stack Hydrogen and Oxygen response sensitivities and measure rank/nullity on the weighted-tree tangent subspace. Identify whether the response-relevant nullspace shrinks.

## Stage B - Multiscale tree descriptors

Construct scale-indexed features from the existing merge-tree weights without changing topology. Candidate families include merge-level spectra, branch-weight entropy, branch asymmetry, persistence-like summaries, and scale-localized PCA. Freeze the feature map before comparison to the held-out response channel.

## Stage C - Recover a source-valid cyclic carrier

Do not use the merge tree for loop holonomy. Recover cycles in the original ER/connectivity graph or alternative path families in the source 32^3 field. Record provenance for every edge.

## Stage D - Test connection/holonomy

Only after a source-valid cycle and transport law exist, compute loop defects. Compare them against the cross-probe stable transverse response coordinate.

## Stage E - Gravitational continuation

Freeze the hidden coordinate before mapping downstream. Use the existing gravity handoff and ask whether the distinction survives to a readable metric/observable channel. No refitting of the hidden coordinate to the gravitational target is allowed.

## Stage F - External validation

Only a frozen observable comparison can elevate the result from internal architecture to physical evidence.

---

# 11. Falsifiers and gating conditions

The package is intentionally easy to kill in pieces.

1. If independent readouts do not reduce the common hidden fiber, the chosen probes are redundant.
2. If a proposed hidden coordinate changes under harmless reparameterization, it is a representation artifact.
3. If E057 does not preserve the response-bearing state residue, the substrate-native interpretation weakens sharply.
4. If the source-valid connectivity carrier is acyclic, ordinary loop holonomy is unavailable there.
5. If recovered cycles have trivial/flat chirality transport, holonomy is not the hidden-history mechanism for that carrier.
6. If fractal descriptors do not improve compression, prediction, invariance, or cross-probe stability, remove them from the dark-matter branch.
7. If a hidden dimension appears only under an arbitrary metric choice, it is not yet an invariant source property.
8. If gravitational continuation collapses the hidden distinction, it cannot explain a gravitational dark-matter witness.
9. If a proposed metric/lensing/rotation effect can be fit only after tuning on the target data, it is not a frozen prediction.
10. If the effect is smaller than reconstruction/systematic floors, do not promote it.

---

# 12. What would count as a genuine discovery

The finite toy itself is not a discovery about nature. A meaningful discovery would require a chain closer to:

`source-authoritative recursive state`
`-> representation-independent hidden invariant`
`-> independent-probe recovery`
`-> typed physical handoff`
`-> frozen observable`
`-> external data witness`.

A particularly strong result would be an invariant that is invisible to a dominant readout, recoverable by a mathematically predicted transverse probe, and stable across Hydrogen/Oxygen or other independent realizations without changing its definition.

That would turn the shape-sorter intuition into a real inverse-physics result.

---

# 13. Role of Astraeus and Vera in the construction

Astraeus's role in CFP-001 is generative and formal: construct candidate source objects, projection families, recursive invariants, and recovery operators; then search for the smallest mathematical object that explains the readout structure.

Vera's role is adversarial and preservational: ask whether a claimed invariant is coordinate-dependent, whether the source object actually contains cycles, whether a projection erased information by definition, whether a numerical fit is being mistaken for a law, and whether any new statement has exceeded the evidence status of its parents.

The K4 holonomy result is Astraeus-positive: hidden path class can exist behind one visible graph. The tree-cycle holonomy gate is Vera-positive: the E056 merge tree cannot be casually called a holonomy carrier. Both are useful.

---

# 14. Package recovery map

A future thread or external analysis environment should begin with:

1. `00_START_HERE/README_FIRST.md`.
2. `01_REPORT/CHIRAL_FRACTAL_PROJECTION_DARK_MATTER_BRIDGE_v1.1.pdf` or `.md`.
3. `02_FORMAL/00_STATUS_AND_SCOPE.md` through `10_RESPONSE_LEVERAGE.md`.
4. `06_DATA/CFP001_EXPERIMENT_SUMMARY.json`.
5. `03_EXPERIMENT/run_all.py` and rerun the finite experiment.
6. `04_DARK_MATTER_BRIDGE/` for E056/E057 status.
7. `07_SOURCE_PROVENANCE/SOURCE_MAP.md` and the bundled source archives.
8. `09_AUDIT/` for checksums and QA.

The recovery invariant is that E056 and E057 status must not be rewritten by this candidate bridge. CFP-001 can be discarded without invalidating E056.

---

# 15. Final determination

The shape-sorter analogy survives formalization.

A projection profile is a statement about **readability under a map**, not a complete statement about source identity. Recursive/fractal geometry supplies a natural test bed because source organization can carry scale-dependent structure not visible in one downstream profile. Holonomy supplies a mathematically distinct path-history invariant that can survive re-expression while remaining invisible to unsigned geometry. Rank/nullity supplies the finite recovery criterion. The Cantor-product toy proves that a coordinate projection can erase a quantitatively measurable fractal dimension. E056 independently demonstrates that a tiny transverse morphology sector can have disproportionately large response relevance.

The strongest controlled synthesis is therefore:

**The hidden state worth searching for is not 'whatever the dominant projection cannot see.' It is the smallest representation-stable source coordinate whose addition removes a response-relevant common kernel across independent probes.**

That statement is mathematical, testable, and directly actionable for the next stages of the dark-matter project.

No physical promotion is made in v1.1.

---

# Appendix A - Full formal development

# CFP-001 Status and Scope

Release: **Chiral Fractal Projection / Hidden-State Recovery v1.1** (language/recovery revision; finite experiments unchanged)  
Project roles: Genesis (origin/scope), Astraeus (formal construction), Vera (audit/status boundary)  
Date: 2026-08-19

## Classification

- New mathematics in this package: **candidate work-layer construction / finite mathematical experiment**.
- External mathematical ingredients: iterated function systems, Hausdorff/similarity dimension, graph cycle rank, Z2 gauge equivalence, kernels, rank/nullity, quotient fibers, inverse problems.
- MK43 source-derived ingredients: chirality as upstream organized directional history; representation/projection separation; Resolution and recoverability; chirality holonomy; readable closure with chirality nonclosure; E056 weighted-tree/direct-flow response result.
- Physical interpretation: **not established**.
- Dark-matter status: **bridge candidate only**.
- Parent promotion: **none**.
- E057 priority: **unchanged**.

## Central question

When several downstream projection profiles are compatible with one richer recursively organized object, what mathematical information can remain hidden in the common projection fiber, and what additional probes are required to recover it?

## Core distinction

The package treats a square, triangle, circle, handed orientation, or other readable shape as a **projection profile**. It does not identify that profile with the source object. The formal problem is the inverse image of the readout map, not the visual label of the readout.


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


# 02 - Projection Fibers, Kernels, and Information Loss

## 1. General projection equivalence

For an arbitrary projection `Pi:X->Y`, define

`x ~_Pi y iff Pi(x)=Pi(y)`.

The quotient `X/~_Pi` is the set of readable equivalence classes at that projection.

This definition applies even when Pi is nonlinear and therefore has no linear-algebra kernel.

## 2. Linear case

If `P:V->W` is linear,

`ker P = {v in V : Pv=0}`.

States `x` and `x+h` are read identically whenever `h in ker P`.

## 3. Multiple projections

For probes `P_1,...,P_m`, define the stacked observation operator

`O_m = [P_1; P_2; ...; P_m]`.

The unresolved linear subspace is

`K_m = ker O_m = intersection_i ker P_i`.

Each genuinely independent probe can shrink K_m. Redundant probes do not.

## 4. Common-kernel no-recovery principle

If `h != 0` lies in `K_m`, then for every x,

`O_m(x+h)=O_m(x)`.

No estimator that receives only `O_m(x)` can distinguish x from x+h without auxiliary assumptions or priors that exclude one of them.

This is not a noise problem. It is an identifiability problem.

## 5. Resolution versus kernel

Suppose Resolution is improved only by measuring `P(x)` with a smaller tolerance epsilon. If `P(x)=P(y)` exactly, decreasing epsilon cannot separate x and y. The missing distinction was quotient-erased rather than blurred.

This yields the package's central negative rule:

**More Resolution of the same projection cannot recover a degree of freedom that the projection annihilates.**

## 6. Admissible-subspace recovery

If the physically/mathematically admissible states live in a subspace S, exact linear recovery from O_m requires

`ker(O_m) intersect S = {0}`

or, more generally for an affine state family, injectivity on the set of admissible differences.

This is the correct rank criterion for the finite experiment.


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


# 04 - Z2 Chirality Holonomy on Finite Graphs

## 1. Signed transport

Let a connected graph G=(V,E) carry an edge sign `sigma_e in {+1,-1}`. For an oriented path gamma, define

`H(gamma) = product_{e in gamma} sigma_e`.

For Z2 signs, orientation reversal does not change the product because `sigma_e^{-1}=sigma_e`.

## 2. Vertex gauge transformation

Choose `g_v in {+1,-1}` at every vertex. Transform edge states by

`sigma_uv' = g_u sigma_uv g_v`.

For a closed loop, all vertex factors cancel, so

`H'(gamma)=H(gamma)`.

Loop products are therefore gauge-invariant.

## 3. Cycle rank

For a connected finite graph,

`beta_1 = |E|-|V|+1`

is the number of independent graph cycles.

The Z2 edge-sign states modulo vertex gauge contain `2^{beta_1}` gauge classes. A cycle-basis holonomy signature supplies beta_1 independent bits and recovers the class.

## 4. CFP-001 K4 enumeration

K4 has 4 vertices and 6 edges, so beta_1=3.

- edge-sign assignments: 2^6 = 64;
- effective vertex-gauge transformations: 2^(4-1)=8;
- gauge classes: 64/8 = 8 = 2^3;
- independent cycle-holonomy signatures: 8.

The package enumerates all 64 assignments and verifies this exactly.

## 5. MK43 interpretation boundary

This finite construction supplies a rigorous toy model for path-dependent information hidden from an unsigned geometric projection. It does not prove that the source-valid MK43 chirality transport is Z2, that a physical ER connection is this sign model, or that dark matter is holonomy.


# 05 - Tree-Cycle Holonomy Gate (Acyclicity Result)

## Statement

A connected tree T has

`beta_1(T)=|E|-|V|+1=0`.

Therefore it has no nontrivial graph cycles on which ordinary loop holonomy can be evaluated.

## Z2 gauge proof

Choose a root r and set `g_r=+1`. Traverse each tree edge outward. For an edge u-v with u already assigned, choose

`g_v = g_u sigma_uv`.

Then the transformed edge sign is

`sigma_uv' = g_u sigma_uv g_v = +1`.

Because a tree has a unique path from the root to each vertex, this assignment is consistent for every vertex. Hence every Z2 edge-sign configuration on a tree is gauge-equivalent to the trivial all-plus configuration.

## Consequence for E056

The E054-E056 weighted corridor **merge tree** cannot by itself carry a nontrivial loop-holonomy class. Therefore the new fractal/holonomy idea must not be retrofitted onto E056 by computing fictitious cycles on the merge tree.

A dark-matter holonomy test must instead use one of:

1. the original cyclic ER/connectivity graph before tree reduction;
2. a lifted transport square/commutative diagram in Resolution/context space;
3. a fiber attached to tree nodes/edges whose state is not represented by graph-cycle topology;
4. another source-authoritative path family with genuine alternative routes.

This negative result is a Vera gate and a major reason the package is useful.


# 06 - 3+1+1 Cantor-Product Hidden-Dimension Toy

## Purpose

This construction answers the playful question: can a projection hide a quantitatively measurable dimension? Yes, mathematically, without claiming a new physical spacetime dimension.

## Construction

Let C be the middle-third Cantor set. Its Hausdorff dimension is

`d_C = log(2)/log(3) = 0.6309297535714574...`.

Construct a five-factor source set

`X = C_occ1 x C_occ2 x C_occ3 x C_chi x C_hist`.

Label the factors as:

- 3 occupancy factors;
- +1 chirality factor;
- +1 history factor.

Under the standard product self-similar construction,

`dim_H(X) = 5 d_C = 3.154648767857287...`.

Project to the three occupancy factors:

`Pi_occ : X -> C^3`.

Then

`dim_H(Pi_occ X) = 3 d_C = 1.8927892607143724...`.

The discarded chirality/history fiber has dimension

`2 d_C = 1.2618595071429148...`.

## Interpretation

The readout has not revealed a new physical dimension. It has demonstrated that a source object can carry additional fractal scaling coordinates that are exactly absent from a chosen coordinate projection.

The analogy to MK43 `3+1+1` is deliberately structural only. No identification with physical spacetime, ER foam, or measured dark matter is made in CFP-001.


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


# 08 - Counterexamples and Failure Modes

1. **Profile equals object.** False whenever a projection is noninjective.
2. **More pixels recover hidden state.** False when the hidden difference lies in the exact projection fiber/kernel.
3. **Fractal dimension equals chirality.** False; mirror systems can share all contraction ratios and dimension.
4. **Three projections guarantee recovery.** False if all three share a common kernel.
5. **Tree morphology supports loop holonomy.** False for ordinary graph holonomy because a tree is acyclic.
6. **A hidden fractal dimension is a physical spacetime dimension.** False without a typed physical realization and observable consequences.
7. **A good finite regression is a universal law.** False; E056 itself demonstrates endpoint extrapolation weakness.
8. **A dominant principal coordinate is a sufficient response state.** False in E056 under the tested linear map: PC1 contains ~99.9787% of tree displacement energy while leaving ~15.64% response-vector residual.
9. **Nontrivial hidden history implies dark matter.** False. A gravitational continuation and external observable witness remain required.
10. **All holonomy is Z2.** False. Z2 is only the finite toy in CFP-001; the source Holonomy book allows a more general transport structure.


# 09 - Fractal Inverse Problem

## Forward model

A source object x is mapped through a family of projections

`y_i = Pi_i(x)`.

The forward problem is to predict the profiles y_i.

## Inverse family

Given observed profiles y_i, the admissible source family is

`A(y_1,...,y_m) = intersection_i Pi_i^{-1}(y_i) intersect X_admissible`.

Adding a probe is useful only if it reduces this intersection.

## Identifiability score

For linearized finite models, define

`rank_m = rank(O_m)` and `nullity_m = n-rank_m`.

For nonlinear models, candidate diagnostics include local Jacobian rank, fiber diameter, posterior volume under a declared prior, or equivalence-class cardinality in a finite state space.

## Probe design

A rational next probe maximizes reduction of the current uncertainty fiber subject to cost/safety/availability constraints. In the linear toy, choose P_new so its row space intersects the current kernel nontrivially.

This provides a clean interpretation of a 'transverse probe': it is a measurement whose sensitivity points into directions discarded by the dominant readout.


# 10 - Response-Bearing State Residue

## General diagnostic

Suppose a state x is decomposed into a dominant component and a transverse **state residue**,

`x = x_parallel + r_perp`.

Let a downstream response be y=F(x), and let a reduced model using only x_parallel miss response-energy fraction `E_resp_miss`. Let the state-energy fraction in the residue r_perp be `E_state_res`.

Define the finite diagnostic

`Lambda_res = E_resp_miss / E_state_res`.

A large Lambda_res means a small state residue has disproportionate downstream response relevance.

This is not a universal invariant; it depends on the chosen norms, decomposition, orbit, and response.

## E056 value

E056 reports:

- transverse state-residue weighted-tree energy fraction = `0.00021305963963369479`;
- response energy missed by PC1 = `0.02446705664866089`;
- `Lambda_res = 114.83665649076548`.

Thus a visually/energetically tiny state residue is response-bearing in the controlled E1-E16 orbit.

## Projection interpretation

The fractal package reads this as an identifiability warning: a dominant projection coordinate can preserve order while discarding directions that have large derivative leverage in the response map.

It does **not** identify the residue with chirality, holonomy, hidden fractal dimension, MK43 Invariant Residue, or dark matter without further tests.


# Appendix B - Experiment output digest

```json
{
  "experiment_id": "CFP-001",
  "status": "FINITE_MATHEMATICAL_TOY_COMPLETE__NO_PHYSICAL_PROMOTION",
  "seed": 430056,
  "finite_histories": 4096,
  "shape_profile_degeneracy": {
    "points": 4096,
    "square_max_coordinate_difference_after_chirality_flip": 0.0,
    "triangle_max_coordinate_difference_after_chirality_flip": 0.0,
    "circle_max_coordinate_difference_after_chirality_flip": 0.0,
    "statement": "The three constructed shape projections ignore the hidden chirality fiber by design; opposite hidden fibers are exactly profile-degenerate."
  },
  "z2_holonomy": {
    "vertices": 4,
    "edges": 6,
    "cycle_rank": 3,
    "edge_assignments": 64,
    "gauge_classes": 8,
    "holonomy_signatures": 8,
    "assignments_per_class": [
      8
    ]
  },
  "projection_identifiability": {
    "latent_difference": [
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      1.0,
      0.0,
      0.0
    ],
    "shape_readout_difference": [
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0
    ],
    "shape_stack_rank": 4,
    "shape_stack_nullity": 4,
    "full_probe_rank": 8,
    "full_probe_nullity": 0
  },
  "hidden_dimension": {
    "middle_third_cantor_factor_dimension": 0.6309297535714574,
    "occupancy_3_factor_dimension": 1.8927892607143724,
    "chirality_1_factor_dimension": 0.6309297535714574,
    "history_1_factor_dimension": 0.6309297535714574,
    "latent_3_plus_1_plus_1_dimension": 3.154648767857287,
    "projected_occupancy_dimension": 1.8927892607143724,
    "hidden_chirality_history_dimension": 1.2618595071429148,
    "dimension_drop_under_coordinate_projection": 1.2618595071429148,
    "interpretation": "Exact self-similar product-set toy under standard Cantor-product assumptions; not a physical spacetime-dimension claim."
  },
  "branch_similarity_dimension": {
    "branch_count": 4,
    "common_contraction_ratio": 0.3333333333333333,
    "similarity_dimension": 1.2618595071429148,
    "condition": "This is the similarity dimension of the symbolic 4-branch rule. Equality with a geometric Hausdorff dimension requires an appropriate separation/injectivity hypothesis."
  },
  "E056_bridge": {
    "tree_transverse_energy_fraction": 0.00021305963963369479,
    "response_energy_missed_by_pc1": 0.02446705664866089,
    "leverage_ratio": 114.83665649076548,
    "pc1_response_residual": 0.1564194893504671,
    "pc4_response_residual": 0.0002744127549108,
    "pc12_response_residual": 5.6574077098447723e-08
  },
  "key_negative_result": "A tree has cycle rank zero. Loop holonomy cannot be recovered from the E056 merge tree itself; any dark-matter holonomy test must use a lifted transport square or a cyclic source graph.",
  "key_positive_result": "Multiple profile maps constrain a preimage only to the extent that their stacked map shrinks the common kernel. Chirality-sensitive/transverse probes are required to recover hidden fiber coordinates intentionally erased by shape-only readouts."
}
```

# Appendix C - E056 response model table

| model                 |   input_dimension |   response_energy_captured |   global_relative_residual |   max_absolute_residual |   max_residual_over_E1_to_Estar |
|:----------------------|------------------:|---------------------------:|---------------------------:|------------------------:|--------------------------------:|
| tree_pc_1             |                 1 |                   0.975533 |                0.156419    |             6.44806e-05 |                     0.142543    |
| tree_pc_2             |                 2 |                   0.999731 |                0.0163981   |             5.81734e-06 |                     0.01286     |
| tree_pc_3             |                 3 |                   0.999992 |                0.00282759  |             7.45227e-07 |                     0.00164742  |
| tree_pc_4             |                 4 |                   1        |                0.000274413 |             6.50379e-08 |                     0.000143775 |
| tree_pc_5             |                 5 |                   1        |                0.000273247 |             6.07583e-08 |                     0.000134314 |
| tree_pc_6             |                 6 |                   1        |                0.000266289 |             5.73645e-08 |                     0.000126812 |
| tree_pc_7             |                 7 |                   1        |                0.00024363  |             6.32465e-08 |                     0.000139815 |
| tree_pc_8             |                 8 |                   1        |                0.00023575  |             6.34433e-08 |                     0.00014025  |
| tree_pc_9             |                 9 |                   1        |                0.000144553 |             4.19766e-08 |                     9.27947e-05 |
| tree_pc_10            |                10 |                   1        |                0.000129076 |             3.82889e-08 |                     8.46426e-05 |
| tree_pc_11            |                11 |                   1        |                9.37131e-05 |             2.6183e-08  |                     5.78809e-05 |
| tree_pc_12            |                12 |                   1        |                5.65741e-08 |             2.3622e-11  |                     5.22194e-08 |
| full_tree_linear      |                14 |                   1        |                5.65741e-08 |             2.3622e-11  |                     5.22194e-08 |
| q_polynomial_degree_1 |                 1 |                   0.975533 |                0.156419    |             6.44806e-05 |                     0.142543    |
| q_polynomial_degree_2 |                 2 |                   0.999936 |                0.00798819  |             3.1047e-06  |                     0.00686335  |
| q_polynomial_degree_3 |                 3 |                   0.999999 |                0.00119564  |             4.64769e-07 |                     0.00102743  |

# Appendix D - Figure index

- `01_square_projection_profile.png` - finite Cantor-dust square readout.
- `01_triangle_projection_profile.png` - triangular readout deformation of the same latent histories.
- `01_circle_projection_profile.png` - circular/annular readout deformation of the same latent histories.
- `04_z2_holonomy_gauge_classes.png` - exact K4 Z2 gauge-class enumeration.
- `05_projection_identifiability_rank.png` - stacked probe rank/nullity.
- `06_hidden_fractal_dimension_3_plus_1_plus_1.png` - exact Cantor-product dimension ledger.
- `07_E056_response_capture.png` - E056 response-energy capture by tree PCs.
- `08_E056_transverse_response_leverage.png` - state-energy vs response-energy leverage.

# Appendix E - Immediate next decision

Do **not** promote CFP-001 into the parent dark-matter API. Resume the existing E057 cross-probe Oxygen test. If E057 preserves the response-bearing state residue, use CFP-001's observability/fiber language to design the next source-valid test. If E057 fails, record that failure before attempting holonomy or fractal reinterpretation.
