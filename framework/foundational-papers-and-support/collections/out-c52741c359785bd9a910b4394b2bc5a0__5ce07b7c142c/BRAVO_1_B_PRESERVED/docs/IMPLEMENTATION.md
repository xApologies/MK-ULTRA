# Implementation

Library 1.B realizes the Alpha address engine over SQLite. Public recovery is read-only and exhaustive. Administrative writes are transactional. REMOVE preserves rollback state; PURGE retracts accidental admissions.
