SCHEMA = r"""
PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS objects(
 handle TEXT PRIMARY KEY,
 object_type TEXT NOT NULL,
 active_version INTEGER,
 status TEXT NOT NULL DEFAULT 'active',
 created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS versions(
 handle TEXT NOT NULL,
 version INTEGER NOT NULL,
 package_hash TEXT NOT NULL,
 canonical_math_json TEXT NOT NULL,
 metadata_json TEXT NOT NULL,
 language TEXT NOT NULL,
 status TEXT NOT NULL,
 created_at TEXT NOT NULL,
 PRIMARY KEY(handle,version),
 FOREIGN KEY(handle) REFERENCES objects(handle) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS blocks(
 block_id TEXT PRIMARY KEY,
 handle TEXT NOT NULL,
 version INTEGER NOT NULL,
 content_type TEXT NOT NULL,
 title TEXT NOT NULL,
 body TEXT NOT NULL,
 body_format TEXT NOT NULL,
 ordinal INTEGER NOT NULL,
 provenance_json TEXT NOT NULL,
 FOREIGN KEY(handle,version) REFERENCES versions(handle,version) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS provenance(
 provenance_id TEXT PRIMARY KEY,
 handle TEXT NOT NULL,
 version INTEGER NOT NULL,
 record_json TEXT NOT NULL,
 ordinal INTEGER NOT NULL,
 FOREIGN KEY(handle,version) REFERENCES versions(handle,version) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS aliases(
 alias TEXT PRIMARY KEY,
 handle TEXT NOT NULL,
 FOREIGN KEY(handle) REFERENCES objects(handle) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS relations(
 relation_id TEXT PRIMARY KEY,
 source_handle TEXT NOT NULL,
 relation_type TEXT NOT NULL,
 target_handle TEXT NOT NULL,
 model_handle TEXT,
 ordinal INTEGER,
 required INTEGER NOT NULL DEFAULT 1,
 metadata_json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS models(
 model_handle TEXT PRIMARY KEY,
 root_handle TEXT NOT NULL,
 name TEXT NOT NULL,
 package_hash TEXT NOT NULL,
 version INTEGER NOT NULL,
 status TEXT NOT NULL,
 metadata_json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS model_membership(
 model_handle TEXT NOT NULL,
 handle TEXT NOT NULL,
 ordinal INTEGER NOT NULL,
 required INTEGER NOT NULL DEFAULT 1,
 PRIMARY KEY(model_handle,handle),
 FOREIGN KEY(model_handle) REFERENCES models(model_handle) ON DELETE CASCADE,
 FOREIGN KEY(handle) REFERENCES objects(handle) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS receipts(
 receipt_id TEXT PRIMARY KEY,
 operation TEXT NOT NULL,
 affected_json TEXT NOT NULL,
 pre_hash TEXT NOT NULL,
 post_hash TEXT NOT NULL,
 status TEXT NOT NULL,
 details_json TEXT NOT NULL,
 created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS snapshots(
 receipt_id TEXT PRIMARY KEY,
 snapshot_json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS purge_receipts(
 receipt_id TEXT PRIMARY KEY,
 handle TEXT NOT NULL,
 former_hash TEXT,
 reason TEXT NOT NULL,
 impact_json TEXT NOT NULL,
 created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS pending_transactions(
 transaction_id TEXT PRIMARY KEY,
 operation TEXT NOT NULL,
 payload_json TEXT NOT NULL,
 valid INTEGER NOT NULL,
 errors_json TEXT NOT NULL,
 created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_blocks_handle ON blocks(handle,version,content_type,ordinal);
CREATE INDEX IF NOT EXISTS idx_rel_source ON relations(source_handle,relation_type,ordinal);
CREATE INDEX IF NOT EXISTS idx_rel_target ON relations(target_handle,relation_type,ordinal);
CREATE INDEX IF NOT EXISTS idx_membership ON model_membership(model_handle,ordinal);
"""