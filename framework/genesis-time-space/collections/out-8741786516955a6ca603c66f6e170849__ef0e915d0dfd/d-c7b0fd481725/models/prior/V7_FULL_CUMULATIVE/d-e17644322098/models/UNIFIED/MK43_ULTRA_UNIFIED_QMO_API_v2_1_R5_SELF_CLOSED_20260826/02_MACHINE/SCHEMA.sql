CREATE INDEX idx_alias_alias ON aliases(alias);

CREATE INDEX idx_edges_ns ON edges(namespace);

CREATE INDEX idx_edges_rel ON edges(relation);

CREATE INDEX idx_edges_src ON edges(source_handle);

CREATE INDEX idx_edges_tgt ON edges(target_handle);

CREATE INDEX idx_edges_triple ON edges(source_handle,relation,target_handle);

CREATE INDEX idx_eq_hash ON equations(expression_sha256);

CREATE INDEX idx_eq_ns ON equations(namespace);

CREATE INDEX idx_eq_owner ON equations(owner_handle);

CREATE INDEX idx_instances_handle ON object_instances(handle);

CREATE INDEX idx_instances_ns ON object_instances(namespace);

CREATE INDEX idx_source_files_path ON source_files(relative_path);

CREATE INDEX idx_source_files_source ON source_files(source_id);

CREATE TABLE aliases(
 alias TEXT, namespace TEXT, canonical_handle TEXT, source_id TEXT, provenance_json TEXT,
 PRIMARY KEY(alias,namespace,canonical_handle,source_id)
);

CREATE TABLE canonical_handles(
 handle TEXT PRIMARY KEY, canonical_name TEXT, object_type TEXT,
 first_namespace TEXT, first_source_id TEXT, notes TEXT
);

CREATE VIRTUAL TABLE claim_fts USING fts5(claim_id,namespace,claim,status,authority);

CREATE TABLE 'claim_fts_config'(k PRIMARY KEY, v) WITHOUT ROWID;

CREATE TABLE 'claim_fts_content'(id INTEGER PRIMARY KEY, c0, c1, c2, c3, c4);

CREATE TABLE 'claim_fts_data'(id INTEGER PRIMARY KEY, block BLOB);

CREATE TABLE 'claim_fts_docsize'(id INTEGER PRIMARY KEY, sz BLOB);

CREATE TABLE 'claim_fts_idx'(segid, term, pgno, PRIMARY KEY(segid, term)) WITHOUT ROWID;

CREATE TABLE claims(
 claim_id TEXT PRIMARY KEY, namespace TEXT, claim TEXT, status TEXT, authority TEXT,
 source_id TEXT, source_path TEXT, run_id TEXT, payload_json TEXT
);

CREATE TABLE closures(
 closure_id TEXT, namespace TEXT, object_handle TEXT, decision TEXT, checkpoint TEXT,
 status TEXT, source_id TEXT, source_path TEXT, payload_json TEXT,
 PRIMARY KEY(closure_id,namespace,source_id)
);

CREATE TABLE document_mentions(
 file_id TEXT, handle TEXT, mention_count INTEGER,
 PRIMARY KEY(file_id,handle)
);

CREATE TABLE edges(
 edge_id TEXT PRIMARY KEY, source_handle TEXT, relation TEXT, target_handle TEXT,
 namespace TEXT, trust_class TEXT, status TEXT, confidence TEXT,
 closure_eligible INTEGER, navigation_only INTEGER,
 source_id TEXT, source_path TEXT, provenance_json TEXT, payload_json TEXT
);

CREATE VIRTUAL TABLE equation_fts USING fts5(eq_id,owner_handle,namespace,expression,meaning,status);

CREATE TABLE 'equation_fts_config'(k PRIMARY KEY, v) WITHOUT ROWID;

CREATE TABLE 'equation_fts_content'(id INTEGER PRIMARY KEY, c0, c1, c2, c3, c4, c5);

CREATE TABLE 'equation_fts_data'(id INTEGER PRIMARY KEY, block BLOB);

CREATE TABLE 'equation_fts_docsize'(id INTEGER PRIMARY KEY, sz BLOB);

CREATE TABLE 'equation_fts_idx'(segid, term, pgno, PRIMARY KEY(segid, term)) WITHOUT ROWID;

CREATE TABLE equations(
 eq_id TEXT PRIMARY KEY, owner_handle TEXT, namespace TEXT, kind TEXT,
 expression TEXT, meaning TEXT, status TEXT, proof_status TEXT,
 expression_sha256 TEXT, source_id TEXT, source_path TEXT,
 provenance_json TEXT, payload_json TEXT
);

CREATE TABLE meta(key TEXT PRIMARY KEY, value TEXT NOT NULL);

CREATE TABLE models(
 model_handle TEXT, namespace TEXT, root_handle TEXT, name TEXT, version TEXT, status TEXT,
 source_id TEXT, source_path TEXT, payload_json TEXT,
 PRIMARY KEY(model_handle,namespace,source_id)
);

CREATE VIRTUAL TABLE object_fts USING fts5(instance_id,handle,namespace,canonical_name,object_type,definition,status,math);

CREATE TABLE 'object_fts_config'(k PRIMARY KEY, v) WITHOUT ROWID;

CREATE TABLE 'object_fts_content'(id INTEGER PRIMARY KEY, c0, c1, c2, c3, c4, c5, c6, c7);

CREATE TABLE 'object_fts_data'(id INTEGER PRIMARY KEY, block BLOB);

CREATE TABLE 'object_fts_docsize'(id INTEGER PRIMARY KEY, sz BLOB);

CREATE TABLE 'object_fts_idx'(segid, term, pgno, PRIMARY KEY(segid, term)) WITHOUT ROWID;

CREATE TABLE object_instances(
 instance_id TEXT PRIMARY KEY, handle TEXT NOT NULL, namespace TEXT NOT NULL, version TEXT,
 canonical_name TEXT, object_type TEXT, status TEXT,
 proof_status TEXT, typing_status TEXT, validation_status TEXT, canon_status TEXT,
 recovery_status TEXT, publication_status TEXT,
 definition TEXT, math_json TEXT, authority TEXT,
 source_id TEXT, source_path TEXT, provenance_json TEXT, payload_json TEXT,
 UNIQUE(handle,namespace,version,source_id,source_path),
 FOREIGN KEY(handle) REFERENCES canonical_handles(handle)
);

CREATE TABLE proof_debt(
 debt_id TEXT, namespace TEXT, title TEXT, status TEXT, priority TEXT,
 source_id TEXT, source_path TEXT, payload_json TEXT,
 PRIMARY KEY(debt_id,namespace,source_id)
);

CREATE TABLE provenance_edges(id TEXT PRIMARY KEY, source_node TEXT, relation TEXT, target_node TEXT, payload_json TEXT);

CREATE TABLE provenance_nodes(node_id TEXT PRIMARY KEY, kind TEXT, label TEXT, source_id TEXT, payload_json TEXT);

CREATE TABLE qmos(
 qmo_id TEXT PRIMARY KEY, handle TEXT, namespace TEXT, name TEXT, status TEXT,
 source_id TEXT, source_path TEXT, payload_json TEXT
);

CREATE TABLE relation_composition(
 left_relation TEXT, right_relation TEXT, result_relation TEXT, status TEXT, notes TEXT,
 PRIMARY KEY(left_relation,right_relation,result_relation)
);

CREATE TABLE relation_types(
 relation TEXT PRIMARY KEY, semantic_class TEXT, strict_composable INTEGER,
 reversible INTEGER, closure_default INTEGER, notes TEXT
);

CREATE TABLE shared_handle_links(
 handle TEXT, namespace_a TEXT, namespace_b TEXT, relation TEXT,
 PRIMARY KEY(handle,namespace_a,namespace_b)
);

CREATE TABLE source_files(
 file_id TEXT PRIMARY KEY, source_id TEXT, relative_path TEXT, sha256 TEXT, size_bytes INTEGER,
 extension TEXT, mime_type TEXT, text_indexed INTEGER, text TEXT, excerpt TEXT,
 FOREIGN KEY(source_id) REFERENCES source_packages(source_id)
);

CREATE VIRTUAL TABLE source_fts USING fts5(file_id,source_id,relative_path,text);

CREATE TABLE 'source_fts_config'(k PRIMARY KEY, v) WITHOUT ROWID;

CREATE TABLE 'source_fts_content'(id INTEGER PRIMARY KEY, c0, c1, c2, c3);

CREATE TABLE 'source_fts_data'(id INTEGER PRIMARY KEY, block BLOB);

CREATE TABLE 'source_fts_docsize'(id INTEGER PRIMARY KEY, sz BLOB);

CREATE TABLE 'source_fts_idx'(segid, term, pgno, PRIMARY KEY(segid, term)) WITHOUT ROWID;

CREATE TABLE source_packages(
 source_id TEXT PRIMARY KEY, ordinal INTEGER, name TEXT, root_path TEXT, sha256 TEXT,
 size_bytes INTEGER, mount_status TEXT, zip_integrity TEXT, member_count INTEGER,
 authority TEXT, notes TEXT, payload_json TEXT
);

CREATE TABLE theorems(
 theorem_id TEXT PRIMARY KEY, handle TEXT, namespace TEXT, title TEXT, statement TEXT,
 status TEXT, proof_status TEXT, source_id TEXT, source_path TEXT, payload_json TEXT
);

