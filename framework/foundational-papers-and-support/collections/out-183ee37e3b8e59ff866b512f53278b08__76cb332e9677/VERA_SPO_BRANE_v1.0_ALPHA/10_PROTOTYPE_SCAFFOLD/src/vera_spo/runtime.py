from __future__ import annotations
from .models import AcousticEvent, DevicePolicy, Decision
from .gate import VeraGate

class EventDrivenRuntime:
    """Consumes already-classified events. Audio capture/classification/DSP are intentionally outside 1.0 Alpha."""
    def __init__(self, policy: DevicePolicy):
        self.policy = policy
        self.gate = VeraGate()

    def handle_event(self, event: AcousticEvent, *, user_override: bool = False) -> Decision:
        return self.gate.decide(event, self.policy, user_override=user_override)
