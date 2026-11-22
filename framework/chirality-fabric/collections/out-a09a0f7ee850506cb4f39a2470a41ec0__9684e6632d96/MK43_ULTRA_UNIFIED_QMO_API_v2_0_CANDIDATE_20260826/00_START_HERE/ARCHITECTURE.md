# Architecture

```text
17 IMMUTABLE SOURCE PACKAGES
        |
        v
SOURCE RECEIPTS + FILE HASHES + FULL-TEXT INDEX
        |
        +---------------------------+
        |                           |
        v                           v
CANONICAL HANDLE GRAPH       NAMESPACE OBJECT INSTANCES
        |                           |
        +------------+--------------+
                     v
             TYPED EDGE LEDGER
                     |
             EQUATION / QMO / CLAIM
                     |
                     v
            BOUNDED QUERY ENGINE
       search | route | recover | local-qmo
```

### Why two identity layers?

The graph needs one stable address for cross-domain traversal. The research corpus also needs to preserve that the same handle can carry different definitions, statuses, representations, or source roles in different namespaces. Therefore the API does not collapse object instances merely because their handle strings match.

### No all-to-all linking

Links are admitted from source registries/databases, source-declared schemas, exact source/document handle mentions, source-mount metadata, or shared canonical-handle membership. Document mentions and source mounts are navigation/provenance data, not mathematical closure edges.
