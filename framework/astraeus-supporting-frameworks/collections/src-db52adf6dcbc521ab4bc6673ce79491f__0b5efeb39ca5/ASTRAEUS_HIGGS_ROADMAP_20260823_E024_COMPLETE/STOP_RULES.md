# STOP RULES

A run terminates when one of the following occurs:

1. its declared gate passes;
2. one exact typed edge blocks the gate;
3. the working assumption is contradicted;
4. additional detail would not change the gate result.

When terminating on a blocker:
- name exactly one blocker handle;
- do not recursively expand neighboring open objects;
- append the blocker to LIVE_LOG;
- proceed only if the roadmap explicitly requires resolution.

When terminating on a pass:
- package the witness;
- append the result;
- move to the next run.
