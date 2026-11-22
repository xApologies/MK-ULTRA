# Population Pseudocode

FUNCTION ADD_PACKAGE(model_package):
    normalized ← NORMALIZE_MODEL_PACKAGE(model_package)
    validation ← VALIDATE_MODEL_PACKAGE(normalized)
    IF NOT validation.pass: RETURN REJECTED(validation)
    job ← PREVIEW_TRANSACTION(ADD_PACKAGE,normalized)
    BEGIN TRANSACTION
    TRY:
        STAGE_MODEL(job,normalized)
        STAGE_ADDRESSES(job,normalized.addresses)
        STAGE_RELATIONS(job,normalized.relations)
        STAGE_PROVENANCE(job,normalized.provenance)
        VALIDATE_STAGED_STATE(job)
        COMMIT
    CATCH error:
        ROLLBACK
        RETURN FAILED(error)
    REBUILD_AFFECTED_INDEXES(job)
    RETURN EMIT_POPULATION_RECEIPT(job)
