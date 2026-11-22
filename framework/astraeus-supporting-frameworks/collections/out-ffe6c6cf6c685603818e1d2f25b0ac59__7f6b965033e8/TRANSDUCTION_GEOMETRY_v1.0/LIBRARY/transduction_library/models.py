from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class KnowledgeChunk:
    chunk_type: str
    title: str
    content: str
    sequence: int = 0
    language: str = "en-US"
    provenance: tuple[str,...] = ()
    status: str = "recoverable"

@dataclass
class KnowledgePackage:
    handle: str
    display_name: str
    chunks: list[KnowledgeChunk] = field(default_factory=list)
    metadata: dict[str,Any] = field(default_factory=dict)
    unresolved_reason: str | None = None
    package_hash: str | None = None
    @property
    def resolved(self):
        return self.unresolved_reason is None and bool(self.chunks)
