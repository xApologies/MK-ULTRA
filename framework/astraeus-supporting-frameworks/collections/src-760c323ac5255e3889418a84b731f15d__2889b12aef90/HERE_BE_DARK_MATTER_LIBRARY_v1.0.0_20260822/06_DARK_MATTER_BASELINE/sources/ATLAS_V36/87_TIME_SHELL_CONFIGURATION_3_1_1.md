# 87 — Time-Shell 3+1+1 Configuration Projection

The fresh API contains a native configuration-space handle:

```text
@configuration_space_3_1_1
Type: GeometricConfigurationSpace
Native form: 3 + 1 + 1
Readable projection: 1 + 3
DependsOn:
  @geometric
  @chirality_history
  @artifact_coordinate
  @time_shell
```

The native configuration is

```text
G_geo = (X,Y,Z;A;chi_H)
```

with

```text
G_geo in R^3 x A x Chi.
```

The recovered Time-Shell map is

```text
Pi_TS^conf : R^3 x A x Chi -> M_(1,3)
```

```text
Pi_TS^conf(X,Y,Z;A;chi_H) = (T,X,Y,Z).
```

## Atlas interpretation

This gives direct API support for the claim that **chirality History participates upstream of readable time**.

However, the 3+1+1 model predates the current Atlas `S2 -> T5 -> S3` cartography. They are not silently identified.

Required future reconciliation:

```text
3+1+1 configuration coordinates
<->
S3 continuity address + local S2 directional/projective data.
```

Status: RECOVERED MAP / CROSS-ATLAS IDENTIFICATION OPEN.
