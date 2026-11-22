# Remove and Purge Algorithms

REMOVE deactivates valid knowledge, removes it from active recovery, preserves historical state, and emits a rollback-capable receipt.

PURGE retracts an accidental admission: locate all attached records, calculate deletion/dependent impact, reject unsafe purge unless explicit cascade policy exists, stage deletion, revalidate remaining Library, atomically erase recoverable content, rebuild indexes, and emit a receipt containing transaction metadata but not purged content.
