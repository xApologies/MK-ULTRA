# Library Design

Candidate address families:

```text
@event/*
@transform/*
@protected/*
@device/*
@profile_field/*
@evidence/*
@approval/*
@simulation/*
@rollback/*
```

The Library stores complete recoverable content beneath API/QMO addresses. It must not originate canonical API handles during ordinary recovery.

For early prototypes, the Library can remain deliberately small. Its key value is provenance, version recovery, and separation of canonical handles from content payloads.
