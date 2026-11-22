import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from vera_spo import AcousticEvent, TransformRule, Operation, VeraGate
from vera_spo.compiler import compile_policy

policy = compile_policy(
    policy_id="synthetic-demo",
    rules=[TransformRule("r1", "@steady_mechanical_noise", Operation.ATTENUATE, min_confidence=0.90)],
    protected_events={"@alarm", "@spoken_warning", "@vehicle_warning"},
    supported_operations={Operation.PRESERVE, Operation.ATTENUATE},
    user_override_supported=True,
)

gate = VeraGate()
for event in [
    AcousticEvent("@steady_mechanical_noise", 0.98, 0.0),
    AcousticEvent("@alarm", 0.99, 1.0),
    AcousticEvent("UNKNOWN", 0.30, 2.0),
]:
    print(event, "=>", gate.decide(event, policy))
