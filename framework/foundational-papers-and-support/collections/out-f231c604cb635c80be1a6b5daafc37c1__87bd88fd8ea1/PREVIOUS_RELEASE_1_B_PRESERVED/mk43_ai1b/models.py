from __future__ import annotations
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any

class Decision(str,Enum):
    CONTINUE='CONTINUE'; TERMINATE='TERMINATE'; DEFER='DEFER'; REJECT_INVALID='REJECT_INVALID'

@dataclass(frozen=True)
class IntentModel:
    request_id:str|None; operation:str; subject:str; root_candidates:tuple[str,...]; requested_scope:str
    audience:str; artifact_format:str; completeness_mode:str; budgets:dict[str,Any]; constraints:dict[str,Any]
    ambiguities:tuple[str,...]=(); interpretation_provenance:tuple[str,...]=()

@dataclass(frozen=True)
class RankRecord:
    candidate:Any; score:float; rank:int; reason_codes:tuple[str,...]; features:dict[str,float]; policy_id:str

@dataclass(frozen=True)
class DecisionRecord:
    candidate_handle:str; parent_handle:str|None; decision:str; score:float; rank:int; reason_codes:tuple[str,...]
    policy_id:str; evidence_refs:tuple[str,...]; sequence:int; request_id:str|None

@dataclass(frozen=True)
class ContinuationRecord:
    handle:str; parent_handle:str; reason:str; depth:int; path:tuple[str,...]; policy_id:str; resumable_receipt:str

@dataclass
class AIRequestContext:
    request_id:str|None=None; sequence:int=0; decisions:list[DecisionRecord]=field(default_factory=list)
    continuations:list[ContinuationRecord]=field(default_factory=list); diagnostics:list[str]=field(default_factory=list)
    closed:bool=False
    def next_sequence(self): self.sequence+=1; return self.sequence
    def close(self):
        self.closed=True; self.decisions.clear(); self.continuations.clear(); self.diagnostics.clear()

@dataclass(frozen=True)
class ValidationReceipt:
    valid:bool; root_preserved:bool; branch_accounted:bool; no_fabrication:bool; deterministic_order:bool
    budget_compliant:bool; continuation_accounted:bool; input_fingerprint:str; output_fingerprint:str
    errors:tuple[str,...]=()

@dataclass(frozen=True)
class LibraryRecoveryPlan:
    handles:tuple[str,...]; priorities:tuple[tuple[str,int],...]; requested_families:tuple[str,...]
