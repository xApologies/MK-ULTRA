# Failure and Rollback Pseudocode

```text
ON module load failure:
    reject candidate
    preserve previously mounted module

ON API recovery failure:
    mark request failed
    do not fabricate graph

ON library gap:
    create unresolved record
    obey strict/annotated policy

ON projection crash:
    delete incomplete artifact or mark partial explicitly

ON QMO cleanup failure:
    quarantine workspace
    emit internal security alert
    never expose raw workspace path

ON unexpected exception:
    return sanitized failure receipt
    retain internal diagnostic log under access policy
```
