CREATE INDEX idx_rel_source ON relations(source_address)

CREATE INDEX idx_rel_target ON relations(target_address)

CREATE INDEX idx_rel_type ON relations(relation)

CREATE TABLE aliases(
    alias TEXT PRIMARY KEY,
    canonical_address TEXT NOT NULL,
    notes TEXT
)

CREATE TABLE analogies(
    address TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    mapping TEXT,
    status TEXT,
    notes TEXT
)

CREATE TABLE chronology(
    seq INTEGER PRIMARY KEY,
    event_date TEXT,
    phase TEXT,
    event TEXT NOT NULL,
    status TEXT,
    source_ref TEXT,
    notes TEXT
)

CREATE TABLE claims(
    address TEXT PRIMARY KEY,
    category TEXT,
    statement TEXT NOT NULL,
    status TEXT NOT NULL,
    authority TEXT,
    source_ref TEXT,
    notes TEXT
)

CREATE TABLE equations(
    address TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    expression TEXT NOT NULL,
    interpretation TEXT,
    status TEXT NOT NULL,
    authority TEXT,
    source_ref TEXT,
    notes TEXT
)

CREATE TABLE metadata(
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
)

CREATE TABLE objects(
    address TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    object_type TEXT,
    status TEXT NOT NULL,
    definition TEXT,
    authority TEXT,
    source_ref TEXT,
    notes TEXT
)

CREATE TABLE open_debt(
    address TEXT PRIMARY KEY,
    priority INTEGER,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL,
    blocked_by TEXT,
    source_ref TEXT,
    notes TEXT
)

CREATE TABLE qmos(
    address TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    version TEXT,
    status TEXT NOT NULL,
    scope TEXT,
    definition TEXT,
    authority TEXT,
    source_ref TEXT,
    notes TEXT
)

CREATE TABLE recovery_rules(
    address TEXT PRIMARY KEY,
    rule TEXT NOT NULL,
    rationale TEXT,
    priority INTEGER
)

CREATE TABLE relations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_address TEXT NOT NULL,
    relation TEXT NOT NULL,
    target_address TEXT NOT NULL,
    status TEXT NOT NULL,
    authority TEXT,
    source_ref TEXT,
    notes TEXT
)

CREATE TABLE sources(
    address TEXT PRIMARY KEY,
    filename TEXT NOT NULL,
    sha256 TEXT,
    size_bytes INTEGER,
    kind TEXT,
    embedded INTEGER NOT NULL DEFAULT 0,
    role TEXT,
    status TEXT,
    notes TEXT
)

CREATE TABLE sqlite_sequence(name,seq)

CREATE TABLE supersessions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    old_statement TEXT NOT NULL,
    new_statement TEXT NOT NULL,
    reason TEXT,
    status TEXT,
    source_ref TEXT
)
