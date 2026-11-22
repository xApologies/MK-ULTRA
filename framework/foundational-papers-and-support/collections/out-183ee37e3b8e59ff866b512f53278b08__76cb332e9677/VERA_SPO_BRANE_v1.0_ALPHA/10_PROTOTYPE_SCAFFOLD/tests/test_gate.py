import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pytest
from vera_spo import AcousticEvent, TransformRule, Operation, VeraGate
from vera_spo.compiler import compile_policy, CompileError


def policy():
    return compile_policy(
        policy_id="demo",
        rules=[TransformRule("r1", "@steady_noise", Operation.ATTENUATE, min_confidence=0.9)],
        protected_events={"@alarm", "@spoken_warning"},
        supported_operations={Operation.PRESERVE, Operation.ATTENUATE},
        user_override_supported=True,
        min_confidence=0.8,
    )


def test_unknown_preserved():
    d = VeraGate().decide(AcousticEvent("UNKNOWN", 0.99, 0.0), policy())
    assert d.operation is Operation.PRESERVE


def test_low_confidence_preserved():
    d = VeraGate().decide(AcousticEvent("@steady_noise", 0.5, 0.0), policy())
    assert d.operation is Operation.PRESERVE


def test_protected_preserved():
    d = VeraGate().decide(AcousticEvent("@alarm", 1.0, 0.0), policy())
    assert d.operation is Operation.PRESERVE


def test_allowed_rule_applies():
    d = VeraGate().decide(AcousticEvent("@steady_noise", 0.95, 0.0), policy())
    assert d.operation is Operation.ATTENUATE


def test_user_override_wins():
    d = VeraGate().decide(AcousticEvent("@steady_noise", 0.95, 0.0), policy(), user_override=True)
    assert d.operation is Operation.PRESERVE


def test_compile_rejects_transform_of_protected_event():
    with pytest.raises(CompileError):
        compile_policy(
            policy_id="bad",
            rules=[TransformRule("bad", "@alarm", Operation.ATTENUATE)],
            protected_events={"@alarm"},
            supported_operations={Operation.PRESERVE, Operation.ATTENUATE},
            user_override_supported=True,
        )
