CREATE INDEX idx_qmo_status ON qmo_objects(status)

CREATE INDEX idx_qmo_type ON qmo_objects(object_type)

CREATE INDEX idx_rel_source ON qmo_relations(source_qmo)

CREATE INDEX idx_rel_target ON qmo_relations(target_qmo)

CREATE TABLE aliases(alias TEXT PRIMARY KEY,qmo_address TEXT NOT NULL,notes TEXT,FOREIGN KEY(qmo_address) REFERENCES qmo_objects(qmo_address))

CREATE TABLE api_routes(route_id INTEGER PRIMARY KEY AUTOINCREMENT,method TEXT NOT NULL,route TEXT NOT NULL,qmo_pattern TEXT,description TEXT NOT NULL)

CREATE TABLE artifacts(artifact_id INTEGER PRIMARY KEY AUTOINCREMENT,qmo_address TEXT UNIQUE NOT NULL,filename TEXT NOT NULL,artifact_type TEXT NOT NULL,sha256 TEXT,size_bytes INTEGER,relative_path TEXT,status TEXT NOT NULL)

CREATE TABLE chronology(chronology_id INTEGER PRIMARY KEY AUTOINCREMENT,qmo_address TEXT UNIQUE NOT NULL,sequence_no INTEGER NOT NULL,phase TEXT NOT NULL,event TEXT NOT NULL,verdict TEXT,artifact TEXT)

CREATE TABLE equations(equation_id INTEGER PRIMARY KEY AUTOINCREMENT,qmo_address TEXT UNIQUE NOT NULL,name TEXT NOT NULL,expression TEXT NOT NULL,status TEXT NOT NULL,interpretation TEXT,provenance TEXT)

CREATE TABLE metadata(key TEXT PRIMARY KEY,value TEXT NOT NULL,qmo_address TEXT UNIQUE NOT NULL)

CREATE TABLE open_questions(question_id INTEGER PRIMARY KEY AUTOINCREMENT,qmo_address TEXT UNIQUE NOT NULL,priority INTEGER NOT NULL,question TEXT NOT NULL,status TEXT NOT NULL,dependencies_json TEXT NOT NULL,notes TEXT)

CREATE TABLE qmo_objects(
 qmo_address TEXT PRIMARY KEY,canonical_name TEXT NOT NULL,object_type TEXT NOT NULL,status TEXT NOT NULL,
 scope TEXT,definition TEXT,payload_json TEXT NOT NULL,provenance TEXT,created_at TEXT NOT NULL,supersedes TEXT,notes TEXT
)

CREATE TABLE qmo_relations(
 relation_id INTEGER PRIMARY KEY AUTOINCREMENT,source_qmo TEXT NOT NULL,relation_type TEXT NOT NULL,target_qmo TEXT NOT NULL,
 status TEXT NOT NULL,payload_json TEXT,
 FOREIGN KEY(source_qmo) REFERENCES qmo_objects(qmo_address), FOREIGN KEY(target_qmo) REFERENCES qmo_objects(qmo_address)
)

CREATE TABLE sources(source_id INTEGER PRIMARY KEY AUTOINCREMENT,qmo_address TEXT UNIQUE NOT NULL,filename TEXT NOT NULL,role TEXT NOT NULL,size_bytes INTEGER,sha256 TEXT,embedded INTEGER NOT NULL DEFAULT 0,provenance_status TEXT NOT NULL,notes TEXT)

CREATE TABLE sqlite_sequence(name,seq)

CREATE TABLE theorems(theorem_id INTEGER PRIMARY KEY AUTOINCREMENT,qmo_address TEXT UNIQUE NOT NULL,name TEXT NOT NULL,statement TEXT NOT NULL,status TEXT NOT NULL,dependencies_json TEXT NOT NULL,proof_summary TEXT,provenance TEXT)
