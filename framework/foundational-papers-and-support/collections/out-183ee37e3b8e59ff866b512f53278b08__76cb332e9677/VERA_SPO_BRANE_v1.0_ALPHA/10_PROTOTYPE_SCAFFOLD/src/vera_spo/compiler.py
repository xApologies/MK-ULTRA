from __future__ import annotations
from .models import DevicePolicy, TransformRule, Operation

class CompileError(ValueError):
    pass

def compile_policy(*, policy_id: str, rules: list[TransformRule], protected_events: set[str], supported_operations: set[Operation], user_override_supported: bool, min_confidence: float = 0.8) -> DevicePolicy:
    if not user_override_supported:
        raise CompileError("user override capability is mandatory")
    for rule in rules:
        if rule.event_class in protected_events and rule.operation != Operation.PRESERVE:
            raise CompileError(f"rule {rule.rule_id} attempts to transform protected event {rule.event_class}")
        if rule.required and rule.operation not in supported_operations:
            raise CompileError(f"required operation unsupported for {rule.rule_id}")
    return DevicePolicy(
        policy_id=policy_id,
        rules=tuple(rules),
        protected_events=frozenset(protected_events),
        supported_operations=frozenset(supported_operations),
        min_confidence=min_confidence,
        user_override_supported=True,
    )
