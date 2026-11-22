# Quantum-Atomic-Projection-01 → Chirality-Field-Seed-01

## Purpose

This branch implements the supplied MK43 Ultra Atomic Profile handoff:

```text
external quantum / atomic structure
        ↓
Atomic Profile Translator
        ↓
stable topology variables
        ↓
blank manifold population
        ↓
3+1+1 chirality field seed
```

It deliberately does **not** call the MK43 output a solved quantum state. The uploaded Atomic Profile defines the pipeline as a topology translator that consumes external quantum/atomic structures. The uploaded recursive/quantum-wave equations likewise describe recursive continuity operators rather than validated literal atomic physics.

## Physical ledger

### Small molecules

Where a local SDF is present, the model carries explicit:

- element identity;
- formal charge;
- three-dimensional coordinates;
- CIP stereocenters;
- protons and electrons;
- common-isotope neutron proxy;
- valence `u/d` quark inventory of the nucleons.

A **gluon count is never invented**. QCD dynamics remain implicit below the nuclear bookkeeping layer.

### Macromolecules

Protein and nucleic-acid structure anchors use experimental PDB metadata: atom count, molecular mass, modeled residues, method, resolution and biopolymer chirality class. The coordinate archives are referenced rather than redistributed, so exact proton/electron/nuclear inventories remain unresolved for these macromolecular anchors.

## MK43 numerical realization

The source equations establish roles but do not uniquely define numerical kernels. Therefore the implementation explicitly labels its numerical choices:

- Gaussian local occupancy for structural anchors;
- neighborhood smoothing for inheritance/adjacency;
- signed chirality redistribution;
- persistence from occupancy + adjacency + resolution;
- closure from persistence and local boundary gradient;
- normalized 11-channel blank-manifold population.

These are **computational realization choices**, not source-derived physical equations.

## Output shapes

For each model:

```text
source_4d                    (11,32,32,32)
setlift_5d                   (11,32,32,32,2)
chirality_statecode          (32,32,32)
chirality_field_3p1p1        (32,32,32,2,2)
```

The final two axes of the explicit 3+1+1 field are:

```text
chirality:   [left, right]
persistence: [transient/unresolved, persistent]
```

## Objects projected

1. `HSV1-REFERENCE-MMO-QMODEL-01` — derived from the live virus MMO.
2. `UTERINE-ENDOMETRIOID-QMODEL-01` — derived from the compact endometrioid reference voxel.
3. `UTERINE-SEROUS-QMODEL-01` — derived from the compact serous reference voxel.
4. `UTERINE-CARCINOSARCOMA-QMODEL-01` — derived from the compact carcinosarcoma reference voxel.
5. `HEALTHY-ENDOMETRIUM-QMODEL-01` — control reference.

## Virus/tumor overlap probe

The build computes only a **centered normalized field-overlap probe**. It measures same-sign and opposite-sign chirality occupancy when two independent normalized fields are placed in the same cube.

It does not contain a physical virus–tumor coupling law. Therefore it cannot predict infection, binding, lysis, tumor destruction, safety, or efficacy. The next physical requirement is a measured coupling/interaction realization before the field evolution can be interpreted biologically.
