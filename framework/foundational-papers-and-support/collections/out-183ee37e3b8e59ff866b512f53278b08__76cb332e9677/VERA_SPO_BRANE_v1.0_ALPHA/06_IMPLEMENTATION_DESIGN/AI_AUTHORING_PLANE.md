# AI Authoring Plane

The authoring AI is a translator/compiler assistant, not a clinician.

Allowed:
- convert structured or prose requirements into candidate schema fields;
- identify missing values;
- propose mappings to canonical event/transform handles;
- explain conflicts;
- produce diffs between profile revisions;
- generate test cases from approved requirements.

Not allowed by architecture:
- fabricate diagnoses;
- silently infer clinical thresholds;
- approve its own medical claims;
- bypass protected-event constraints;
- directly mutate canonical SPO_API^5;
- deploy a policy without the required validation path.
