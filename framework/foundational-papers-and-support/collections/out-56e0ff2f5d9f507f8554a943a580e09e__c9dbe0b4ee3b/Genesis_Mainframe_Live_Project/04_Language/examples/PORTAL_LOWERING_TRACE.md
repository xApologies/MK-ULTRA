# STATUS NOTICE — PROVISIONAL SKETCH

This file predates the language-discovery reset. It is retained for provenance only. It is **not** current Genesis canon and must not be treated as a finalized syntax or language design.

# Genesis Portal 0 — Lowering Trace

## Human source

```genesis
portal Payload_A_to_B {
    from: A
    to: B
    carry: Payload
    preserve: [identity, chirality, basin_expression]
    close: at_target
}
```

## Genesis semantic structure

```text
Environment: root
Source boundary: A
Target boundary: B
Occupancy: Payload
Relationship: admissible corridor A -> B
Identity: PayloadIdentity
Persistence: recoverable
Resolution: sufficient
Closure: PayloadIdentity at B
```

## Architect operation plan

```text
inherit Payload
propagate Payload
stabilize Payload
close Payload
normalize Payload
```

## Architect notation

```text
.·
··
.°.
·°·
■ .· ■
```

## Portal contract

```text
source      = A
target      = B
payload     = Payload
invariants  = identity, chirality, basin expression
capacity    = sufficient Resolution and Bandwidth
arrival     = closure-stable PayloadIdentity
failure     = quarantine and recover last closure
```

## Physical/backend obligations

```text
read source arrangement
reserve route capacity
preserve chirality organization
realize destination arrangement
verify identity
commit closure
record provenance
```
