from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class KnowledgeChunk:
    chunk_type: str
    title: str
    content: str
    sequence: int = 0
    language: str = "en-US"
    provenance: tuple[str, ...] = ()
    status: str = "recoverable"

@dataclass
class KnowledgePackage:
    handle: str
    display_name: str
    chunks: list[KnowledgeChunk] = field(default_factory=list)
    unresolved_reason: str | None = None
    version: str = "1.C"
    realization_key: str | None = None
    expected_chunk_types: tuple[str, ...] = ()
    relation: str | None = None
    depth: int | None = None
    placement: Any = None
    provenance_map: tuple[str, ...] = ()
    package_hash: str | None = None
    @property
    def resolved(self): return self.unresolved_reason is None and bool(self.chunks)
    def by_type(self,t): return [c for c in self.chunks if c.chunk_type==t]

@dataclass(frozen=True)
class TransactionPreview:
    transaction_id: str
    operation: str
    valid: bool
    affected_handles: tuple[str,...]
    errors: tuple[str,...]=()

@dataclass(frozen=True)
class TransactionReceipt:
    receipt_id: str
    operation: str
    affected_handles: tuple[str,...]
    pre_state_hash: str
    post_state_hash: str
    status: str
    details: dict[str,Any]

@dataclass(frozen=True)
class QMORecoveryResult:
    qmo_id: str
    recovered: tuple[KnowledgePackage,...]
    unresolved: tuple[dict[str,Any],...]
    coverage: float
    order_hash: str
    provenance_map: dict[str,tuple[str,...]] = field(default_factory=dict)
    package_hash_map: dict[str,str] = field(default_factory=dict)
