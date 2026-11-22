from __future__ import annotations
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any
import json, re

_ID_RE=re.compile(r'^[A-Za-z0-9._:-]{1,128}$')

class CoverageMode(str, Enum):
    STRICT='strict'; ANNOTATED='annotated'; STRUCTURAL_ONLY='structural_only'
class TraversalDirection(str, Enum):
    UPSTREAM='upstream'; DOWNSTREAM='downstream'; BOTH='both'
class QmoState(str, Enum):
    NEW='NEW'; REQUEST_COMPILED='REQUEST_COMPILED'; API_RESOLVING='API_RESOLVING'; STRUCTURE_COMPLETE='STRUCTURE_COMPLETE'; LIFTING='LIFTING'; LIBRARY_RECOVERING='LIBRARY_RECOVERING'; COVERAGE_VALIDATING='COVERAGE_VALIDATING'; REPORT_ASSEMBLING='REPORT_ASSEMBLING'; ARTIFACT_VALIDATING='ARTIFACT_VALIDATING'; COMPLETE='COMPLETE'; FAILED='FAILED'; DESTROYED='DESTROYED'

@dataclass(frozen=True)
class RuntimeRequest:
    operation:str; subject:str; request_id:str|None=None; language:str='en'; artifact_format:str='markdown'; depth:str='complete'
    direction:TraversalDirection=TraversalDirection.BOTH; coverage_mode:CoverageMode=CoverageMode.ANNOTATED
    title:str|None=None; presentation_requirements:dict[str,Any]=field(default_factory=dict); integrity_requirements:dict[str,Any]=field(default_factory=dict); options:dict[str,Any]=field(default_factory=dict)
    @classmethod
    def from_dict(cls,data):
        if not isinstance(data,dict): raise TypeError('request must be an object')
        allowed={'operation','subject','request_id','language','artifact_format','format','depth','direction','coverage_mode','title','presentation_requirements','integrity_requirements','options'}
        unknown=set(data)-allowed
        if unknown: raise ValueError('unknown request fields: '+', '.join(sorted(unknown)))
        if data.get('operation')!='generate_report': raise ValueError('operation must be generate_report')
        subject=data.get('subject')
        if not isinstance(subject,str) or not subject.strip(): raise ValueError('subject is required')
        fmt=str(data.get('artifact_format',data.get('format','markdown'))).lower()
        if fmt!='markdown': raise ValueError('only markdown artifact format is supported')
        language=str(data.get('language','en')).strip()
        if not language or len(language)>35: raise ValueError('invalid language')
        rid=data.get('request_id')
        if rid is not None and (not isinstance(rid,str) or not _ID_RE.match(rid)): raise ValueError('invalid request_id')
        depth=str(data.get('depth','complete')).lower()
        if depth not in {'complete','bounded','structural'}: raise ValueError('invalid depth')
        return cls('generate_report',subject.strip(),rid,language,fmt,depth,TraversalDirection(data.get('direction','both')),CoverageMode(data.get('coverage_mode','annotated')),data.get('title'),dict(data.get('presentation_requirements',{})),dict(data.get('integrity_requirements',{})),dict(data.get('options',{})))

@dataclass(frozen=True)
class RecoveryIntent:
    operation:str; subject:str; root_hint:str; language:str; artifact_format:str; depth:str; direction:TraversalDirection; coverage_mode:CoverageMode; title:str; traversal_policy:dict[str,Any]

@dataclass(frozen=True)
class Module5Coordinate:
    identity:str; dependency:str; chirality:str; recursion:int; provenance:tuple[str,...]

@dataclass(frozen=True)
class RealizationKey:
    root:str; handle:str; path:tuple[str,...]; relations:tuple[str,...]; chirality:str; depth:int; provenance_digest:str
    def encode(self)->str:
        import hashlib
        raw='|'.join((self.root,self.handle,'>'.join(self.path),'>'.join(self.relations),self.chirality,str(self.depth),self.provenance_digest))
        return f'{self.handle}|{hashlib.sha256(raw.encode()).hexdigest()[:24]}'

@dataclass(frozen=True)
class Realization6Coordinate:
    module:Module5Coordinate; realization:str; request_id:str; key:RealizationKey

@dataclass(frozen=True)
class EdgeRecord:
    source:str; relation:str; target:str; provenance:str|None=None; confidence:str='canonical'; chirality:str|None=None

@dataclass
class CanonicalGraph:
    root:str; nodes:set[str]=field(default_factory=set); edges:list[EdgeRecord]=field(default_factory=list)
    def add_edge(self,e): self.nodes.update((e.source,e.target)); self.edges.append(e)
    def neighbors(self,h,direction=TraversalDirection.BOTH):
        out=[]
        if direction in (TraversalDirection.DOWNSTREAM,TraversalDirection.BOTH): out += [e for e in self.edges if e.source==h]
        if direction in (TraversalDirection.UPSTREAM,TraversalDirection.BOTH): out += [EdgeRecord(e.target,'INVERSE:'+e.relation,e.source,e.provenance,e.confidence,e.chirality) for e in self.edges if e.target==h]
        return out

@dataclass(frozen=True)
class TraversalNode:
    handle:str; depth:int; parent:str|None; incoming_relation:str|None; order:int; kind:str='branch'; path:tuple[str,...]=(); relation_path:tuple[str,...]=()

@dataclass
class TraversalRealization:
    root:str; ordered_nodes:list[TraversalNode]=field(default_factory=list); continuation_handles:list[str]=field(default_factory=list); cycle_references:list[tuple[str,str]]=field(default_factory=list); frontier:list[str]=field(default_factory=list)
    def ordered_handles(self): return [n.handle for n in self.ordered_nodes]
    def unique_handles(self): return list(dict.fromkeys(self.ordered_handles()))
    def layers(self): return [(d,[n for n in self.ordered_nodes if n.depth==d]) for d in sorted({n.depth for n in self.ordered_nodes})]

@dataclass(frozen=True)
class LiftedNode:
    node:TraversalNode; coordinate:Realization6Coordinate
    @property
    def key(self)->str: return self.coordinate.key.encode()

@dataclass(frozen=True)
class KnowledgeChunk:
    chunk_type:str; title:str; content:str; sequence:int=0; language:str='en'; provenance:tuple[str,...]=(); status:str='recoverable'

@dataclass
class KnowledgePackage:
    handle:str; display_name:str; chunks:list[KnowledgeChunk]=field(default_factory=list); unresolved_reason:str|None=None; version:str='1.0'; realization_key:str|None=None; expected_chunk_types:tuple[str,...]=()
    @property
    def resolved(self): return self.unresolved_reason is None and bool(self.chunks)
    def by_type(self,t:str): return [c for c in self.chunks if c.chunk_type==t]

@dataclass(frozen=True)
class CoverageReceipt:
    expected_count:int; recovered_count:int; unresolved:tuple[str,...]; duplicates:tuple[str,...]=(); incomplete_families:tuple[str,...]=()
    @property
    def complete(self): return not self.unresolved and not self.incomplete_families

@dataclass(frozen=True)
class ArtifactReceipt:
    path:str; format:str; encoding:str; size_bytes:int; sha256:str; rendered_realizations:int; unresolved_realizations:int

@dataclass(frozen=True)
class RuntimeResponse:
    request_id:str; status:str; artifact:ArtifactReceipt|None=None; recovery_receipt:dict[str,Any]=field(default_factory=dict); errors:tuple[dict[str,str],...]=()
    def to_dict(self): return asdict(self)
    def to_json(self): return json.dumps(self.to_dict(),indent=2,sort_keys=True)
