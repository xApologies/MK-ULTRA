from __future__ import annotations
import hashlib
from .models import TraversalNode, Module5Coordinate, Realization6Coordinate, RealizationKey, RecoveryIntent
from .errors import PrivilegeViolation

class ChiralityLift:
    version='2.1.0'
    def lift(self,node:TraversalNode,*,request_id:str,root:str,intent:RecoveryIntent,api)->Realization6Coordinate:
        provenance=tuple(api.recover_provenance(node.handle))
        chirality=api.resolve_chirality(node,intent,provenance)
        if not api.admissible(node,intent,chirality,provenance):
            raise PrivilegeViolation('inadmissible six-dimensional lift')
        dep='ROOT' if node.parent is None else f'{node.parent}-[{node.incoming_relation}]->{node.handle}'
        pd=hashlib.sha256('\n'.join(provenance).encode()).hexdigest()[:16]
        key=RealizationKey(root,node.handle,node.path,node.relation_path,chirality,node.depth,pd)
        m5=Module5Coordinate(node.handle,dep,chirality,node.depth,provenance)
        return Realization6Coordinate(m5,f'request:{request_id}:realization:{key.encode()}',request_id,key)
