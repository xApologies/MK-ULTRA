# Report Generation Specification

## Definition of report

A report is the recovered knowledge organized into a sustained human-readable treatment. It is not a handle list, graph index, synopsis, or executive summary.

## Per-handle expansion

Each handle requested by the QMO should generate a section containing all available relevant chunk families. Empty families are reported as unresolved rather than invented.

## Ordering

The QMO controls structural order. For dependency reports, traversal begins at the highest upstream layer and proceeds through branching dependency structure to the root and then downstream to terminal handles. The assembler must preserve branches, convergence, cycles, and continuation boundaries.

## Report assembly stages

```text
1. Receive QMO ordering and library chunks.
2. Validate coverage per handle.
3. Build raw structured compendium.
4. Insert cross-handle transitions without deleting content.
5. Generate section and chapter hierarchy.
6. Render equations as plain text, Unicode, fenced text, or requested notation.
7. Produce Markdown artifact.
8. Validate size, completeness, encoding, and checksums.
```

## Presentation versus source artifact

The returned Markdown file is the full artifact. A user-facing AI may later summarize or cosmetically reformat it when explicitly requested, but the original remains unchanged and downloadable.

## Large reports

Reports may be very large. The assembler must stream sections, avoid recursive duplication, detect cycles, and use content-addressed references or appendices where policy allows. It must never generate uncontrolled recursive expansion that crashes ordinary readers.
