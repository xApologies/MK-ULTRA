# Report Builder Pseudocode

```text
FUNCTION BUILD(qmo, report_spec):
    writer ← STREAMING_MARKDOWN_WRITER()
    writer.WRITE_TITLE(report_spec.title)
    writer.WRITE_RECOVERY_METADATA(qmo.validation.public_metadata)

    FOR layer IN qmo.realization.ORDERED_LAYERS():
        writer.WRITE_LAYER_INTRO(layer)

        FOR handle IN layer.HANDLES_IN_BRANCH_ORDER():
            package ← qmo.LIBRARY_PACKAGE(handle)
            writer.WRITE_HANDLE_SECTION(package, context=layer.context)

        writer.WRITE_LAYER_SYNTHESIS(layer, qmo)

    writer.WRITE_CONTINUATION_APPENDIX(qmo.realization.continuation_handles)
    writer.WRITE_UNRESOLVED_APPENDIX(qmo.UNRESOLVED_PACKAGES())
    writer.WRITE_PROVENANCE_APPENDIX(qmo)

    RETURN writer.FINALIZE()
```
