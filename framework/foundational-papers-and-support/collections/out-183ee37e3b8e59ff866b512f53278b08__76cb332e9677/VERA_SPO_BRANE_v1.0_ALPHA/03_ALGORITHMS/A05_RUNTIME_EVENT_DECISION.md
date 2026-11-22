# A05 — Runtime Event Decision

1. Receive one or more event hypotheses from the realtime front end.
2. For each event, preserve explicit uncertainty.
3. Resolve matching policy rule(s).
4. Invoke Vera gate before DSP selection.
5. If Vera gate rejects transformation, preserve event information.
6. Otherwise pass bounded transform parameters to DSP.
7. Emit a lightweight decision receipt without storing raw audio unless explicitly authorized.
