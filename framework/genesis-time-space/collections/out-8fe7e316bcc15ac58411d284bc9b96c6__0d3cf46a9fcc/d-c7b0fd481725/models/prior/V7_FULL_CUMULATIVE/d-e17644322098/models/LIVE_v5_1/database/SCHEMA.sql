CREATE TABLE aliases(alias TEXT PRIMARY KEY,qmo_address TEXT,notes TEXT)

CREATE TABLE api_routes(qmo_address TEXT PRIMARY KEY,method TEXT,route TEXT,description TEXT)

CREATE TABLE artifacts(qmo_address TEXT PRIMARY KEY,filename TEXT,artifact_type TEXT,relative_path TEXT,sha256 TEXT,size_bytes INTEGER,status TEXT)

CREATE TABLE chronology(qmo_address TEXT PRIMARY KEY,sequence_no INTEGER,event TEXT,result TEXT,status TEXT,artifact TEXT)

CREATE TABLE equations(qmo_address TEXT PRIMARY KEY,name TEXT,expression TEXT,status TEXT,interpretation TEXT,provenance TEXT)

CREATE TABLE hypotheses(qmo_address TEXT PRIMARY KEY,name TEXT,statement TEXT,status TEXT,outcome TEXT,provenance TEXT)

CREATE TABLE metadata(qmo_address TEXT PRIMARY KEY,key TEXT UNIQUE,value TEXT,notes TEXT)

CREATE TABLE no_go(qmo_address TEXT PRIMARY KEY,name TEXT,statement TEXT,status TEXT,provenance TEXT)

CREATE TABLE open_questions(qmo_address TEXT PRIMARY KEY,priority INTEGER,question TEXT,status TEXT,dependencies_json TEXT,notes TEXT)

CREATE TABLE qmo_objects(qmo_address TEXT PRIMARY KEY,name TEXT,type TEXT,status TEXT,definition TEXT,payload_json TEXT,provenance TEXT,superseded_by TEXT)

CREATE TABLE relations(qmo_address TEXT PRIMARY KEY,source_qmo TEXT,relation TEXT,target_qmo TEXT,status TEXT,payload_json TEXT)

CREATE TABLE sources(qmo_address TEXT PRIMARY KEY,filename TEXT,role TEXT,size_bytes INTEGER,sha256 TEXT,embedded INTEGER,policy TEXT)

CREATE TABLE supersession(qmo_address TEXT PRIMARY KEY,older_qmo TEXT,newer_qmo TEXT,reason TEXT,status TEXT)

CREATE TABLE theorems(qmo_address TEXT PRIMARY KEY,name TEXT,statement TEXT,status TEXT,dependencies_json TEXT,proof_note TEXT,provenance TEXT)
