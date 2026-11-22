# Independent SPO Instance Formalism

The supplied BRANE formalism defines:

```text
QMO^6(q) = Collapse_q(ι_AI(AI^5), ι_API(API^5), ι_LIB(Library^5))
```

For the auditory domain:

```text
API^5 := SPO_API^5
```

and the independent Sound Profile Object is a projection of the private QMO:

```text
SPO_instance(u, q, c, d)
    := π_SPO(QMO^6(q), UserContext_u, Context_c, DeviceCaps_d)
```

`SPO_instance` is not the canonical API object. It has its own:
- object identity;
- parent API fingerprint;
- QMO receipt;
- profile revision;
- device-capability target;
- approvals;
- policy fingerprint;
- provenance chain.

A device policy is then:

```text
DevicePolicy := Compile(SPO_instance, DeviceCaps)
```

Compilation fails if the target device cannot satisfy mandatory safety constraints.
