# Failure Injection Plan

Inject:
- classifier timeout;
- empty event class;
- confidence NaN/out of bounds;
- invalid policy signature;
- missing protected-event table;
- device capability mismatch;
- Library recovery failure;
- API root resolution failure;
- AI collapse receipt failure;
- out-of-order profile revision;
- policy corruption during atomic replacement;
- resource pressure / low battery;
- user override during active transformation.

Expected system behavior must be explicit and preservation-safe for each case.
