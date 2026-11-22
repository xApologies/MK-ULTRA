from dataclasses import dataclass,field
from uuid import uuid4
from .models import *
from .errors import QmoStateError
LEGAL={QmoState.NEW:{QmoState.REQUEST_COMPILED,QmoState.FAILED},QmoState.REQUEST_COMPILED:{QmoState.API_RESOLVING,QmoState.FAILED},QmoState.API_RESOLVING:{QmoState.STRUCTURE_COMPLETE,QmoState.FAILED},QmoState.STRUCTURE_COMPLETE:{QmoState.LIFTING,QmoState.FAILED},QmoState.LIFTING:{QmoState.LIBRARY_RECOVERING,QmoState.FAILED},QmoState.LIBRARY_RECOVERING:{QmoState.COVERAGE_VALIDATING,QmoState.FAILED},QmoState.COVERAGE_VALIDATING:{QmoState.REPORT_ASSEMBLING,QmoState.FAILED},QmoState.REPORT_ASSEMBLING:{QmoState.ARTIFACT_VALIDATING,QmoState.FAILED},QmoState.ARTIFACT_VALIDATING:{QmoState.COMPLETE,QmoState.FAILED},QmoState.COMPLETE:{QmoState.DESTROYED},QmoState.FAILED:{QmoState.DESTROYED},QmoState.DESTROYED:set()}
@dataclass
class Qmo6:
    request_id:str; intent:RecoveryIntent; internal_id:str=field(default_factory=lambda:uuid4().hex); state:QmoState=QmoState.NEW
    graph:CanonicalGraph|None=None; realization:TraversalRealization|None=None; lifted:dict[str,LiftedNode]=field(default_factory=dict); order_to_key:dict[int,str]=field(default_factory=dict); packages:dict[str,KnowledgePackage]=field(default_factory=dict); coverage:CoverageReceipt|None=None; rendered_realizations:set[str]=field(default_factory=set)
    def transition(self,target):
        if target not in LEGAL[self.state]: raise QmoStateError(f'illegal QMO transition {self.state.value}->{target.value}')
        self.state=target
    def add_lifted(self,lifted): self.lifted[lifted.key]=lifted; self.order_to_key[lifted.node.order]=lifted.key
    def key_for_node(self,node): return self.order_to_key[node.order]
    def attach(self,key,pkg): self.packages[key]=pkg
    def destroy(self):
        if self.state not in (QmoState.COMPLETE,QmoState.FAILED): self.state=QmoState.FAILED
        self.graph=None; self.realization=None; self.lifted.clear(); self.order_to_key.clear(); self.packages.clear(); self.coverage=None; self.rendered_realizations.clear(); self.transition(QmoState.DESTROYED)
