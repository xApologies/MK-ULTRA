# Live Update Protocol

## When new files are supplied

For every corrective or additive upload:

1. Preserve the uploaded file unchanged in `10_Source_Canon` or `99_Inbox_for_Corrections`.
2. Record its filename, size, checksum, and date in `SOURCE_MANIFEST.json`.
3. Identify which current statements it:
   - confirms;
   - refines;
   - contradicts;
   - leaves unresolved.
4. Update the working model.
5. Add a decision-register entry for any unresolved conflict.
6. Add a changelog entry.
7. Rebuild the repository ZIP.
8. Report the new uncompressed workspace size and ZIP size.

## Canon labels

Every substantive statement should be understood as one of:

- **Recovered canon** — directly supported by supplied materials.
- **Working synthesis** — an integration or formalization proposed from the canon.
- **Engineering hypothesis** — a possible implementation mechanism.
- **Open problem** — required but not yet solved.
- **Deprecated interpretation** — retained for provenance but no longer active.

## Integrity rule

The live repository is additive by default.

Material may be replaced only when:

- the replacement is explicitly corrective;
- the displaced interpretation is preserved in the changelog or decision register;
- the reason is recorded.
