from __future__ import annotations
from .models import AcousticEvent, DevicePolicy, Decision, Operation

class VeraGate:
    """Safety-policy gate only. This is not an acoustic DSP implementation."""

    def decide(self, event: AcousticEvent, policy: DevicePolicy, *, user_override: bool = False) -> Decision:
        if user_override:
            return Decision(Operation.PRESERVE, "USER_OVERRIDE")
        if event.event_class == "UNKNOWN" or not (0.0 <= event.confidence <= 1.0):
            return Decision(Operation.PRESERVE, "UNKNOWN_OR_INVALID_EVENT")
        if event.confidence < policy.min_confidence:
            return Decision(Operation.PRESERVE, "LOW_CONFIDENCE")
        if event.event_class in policy.protected_events:
            return Decision(Operation.PRESERVE, "PROTECTED_EVENT")
        rule = policy.rule_for(event.event_class)
        if rule is None:
            return Decision(Operation.PRESERVE, "NO_RULE")
        if event.confidence < max(policy.min_confidence, rule.min_confidence):
            return Decision(Operation.PRESERVE, "RULE_CONFIDENCE_NOT_MET")
        if rule.operation not in policy.supported_operations:
            return Decision(Operation.PRESERVE, "DEVICE_UNSUPPORTED_OPERATION")
        return Decision(rule.operation, "APPROVED", rule.rule_id, dict(rule.parameters))
