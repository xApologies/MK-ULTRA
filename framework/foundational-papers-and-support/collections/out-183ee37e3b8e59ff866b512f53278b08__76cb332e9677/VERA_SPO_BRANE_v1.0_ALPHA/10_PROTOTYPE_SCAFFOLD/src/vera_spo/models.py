from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

class Operation(str, Enum):
    PRESERVE = "PRESERVE"
    ATTENUATE = "ATTENUATE"
    TRANSFORM = "TRANSFORM"
    EMPHASIZE = "EMPHASIZE"

@dataclass(frozen=True)
class AcousticEvent:
    event_class: str
    confidence: float
    timestamp: float
    semantic_tags: tuple[str, ...] = ()
    context_tags: tuple[str, ...] = ()

@dataclass(frozen=True)
class TransformRule:
    rule_id: str
    event_class: str
    operation: Operation
    min_confidence: float = 0.8
    parameters: dict[str, Any] = field(default_factory=dict)
    preserve_semantics: tuple[str, ...] = ()
    required: bool = False

@dataclass(frozen=True)
class DevicePolicy:
    policy_id: str
    rules: tuple[TransformRule, ...]
    protected_events: frozenset[str]
    supported_operations: frozenset[Operation]
    min_confidence: float = 0.8
    user_override_supported: bool = True

    def rule_for(self, event_class: str) -> TransformRule | None:
        for rule in self.rules:
            if rule.event_class == event_class:
                return rule
        return None

@dataclass(frozen=True)
class Decision:
    operation: Operation
    reason: str
    rule_id: str | None = None
    parameters: dict[str, Any] = field(default_factory=dict)
