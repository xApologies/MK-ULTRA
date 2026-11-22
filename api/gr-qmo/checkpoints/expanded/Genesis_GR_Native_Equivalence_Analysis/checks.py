"""Exact finite checks for the accompanying logical examples.

These are tests of explicitly constructed interface examples, NOT tests of the
MK43 native physics, Time-Shell projection, or observational predictions.
Run: python checks.py
Uses only the Python standard library. The infinite statements are proved in
DERIVATION.md; finite checks are not offered as proofs of those statements.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from pathlib import Path
import json
import platform
import sys
from typing import Callable

@dataclass(frozen=True)
class State:
    base: str
    identity_bit: int

E = ('fixed_complete_GR_solution',)
X = tuple(State(e, b) for e in E for b in (0, 1))

def p(x: State) -> str:
    return x.base

def action(a: int, x: State) -> State:
    if a not in (0, 1):
        raise ValueError('This example uses only the two Z2 arrows.')
    return State(x.base, x.identity_bit ^ a)

def adm(a: int, x: State, y: State) -> bool:
    return action(a, x) == y

TESTS: list[tuple[str, Callable[[], None]]] = []
def test(name: str):
    def register(fn: Callable[[], None]):
        TESTS.append((name, fn))
        return fn
    return register

@test('A0: typed admissibility in the two-sheet interface example')
def typed() -> None:
    for a, x in product((0, 1), X):
        assert action(a, x) in X

@test('A1: identity arrow is admissible at every state')
def identity() -> None:
    assert all(adm(0, x, x) for x in X)

@test('A2: composition preserves the declared admissibility relation')
def composition() -> None:
    for a, b, x, y, z in product((0, 1), (0, 1), X, X, X):
        if adm(a, x, y) and adm(b, y, z):
            assert adm(a ^ b, x, z)

@test('A3/A4: identity chart transitions preserve admissibility and cocycles')
def transitions() -> None:
    transition = lambda x: x
    for a, x, y in product((0, 1), X, X):
        if adm(a, x, y):
            assert adm(a, transition(x), transition(y))
    assert all(transition(transition(transition(x))) == x for x in X)

@test('The readout covers the target but has two distinct formal identity lifts')
def coverage_not_uniqueness() -> None:
    assert set(map(p, X)) == set(E)
    assert all(sum(p(x) == e for x in X) == 2 for e in E)

@test('Every candidate section is a right inverse; none is a left inverse')
def sections() -> None:
    right, left = 0, 0
    for selected in product(X, repeat=len(E)):
        lift = dict(zip(E, selected))
        right += all(p(lift[e]) == e for e in E)
        left += all(lift[p(x)] == x for x in X)
    assert right == 2
    assert left == 0

@test('Two distinct native witness histories have identical full readout sequences')
def hidden_history() -> None:
    a, b = X
    for _ in range(64):
        assert a != b and p(a) == p(b)
        a, b = action(1, a), action(1, b)
    # The accompanying proof handles every n by the exact xor formula.

@test('The retained identity-bit observable does not factor through the readout')
def observable() -> None:
    assert p(X[0]) == p(X[1])
    assert X[0].identity_bit != X[1].identity_bit
    for possible_readable_value in (0, 1):
        assert not all(x.identity_bit == possible_readable_value for x in X)

@test('A different gauge interpretation removes the bit, but also removes its observable')
def gauge_alternative() -> None:
    gauge_equivalent = lambda a, b: a.base == b.base
    assert all(gauge_equivalent(a, b) for a, b in product(X, X))
    quotient = {x.base for x in X}
    assert quotient == set(E)
    assert any(gauge_equivalent(a, b) and a.identity_bit != b.identity_bit
               for a, b in product(X, X))

@test('Initial readout can fail to determine projected evolution')
def dynamics_failure() -> None:
    # Separate example: the hidden bit affects the next visible state.
    u = lambda s: (s[0] ^ s[1], s[1])
    p0 = lambda s: s[0]
    a, b = (0, 0), (0, 1)
    assert p0(a) == p0(b)
    assert p0(u(a)) != p0(u(b))

@test('Two-time readout can recover a bit that a one-time readout loses')
def history_rescue() -> None:
    states = tuple(product((0, 1), repeat=2))
    two_time = lambda s: (s[0], s[0] ^ s[1])
    assert len(set(map(two_time, states))) == len(states)
    for x, b in states:
        first, second = two_time((x, b))
        assert (first, first ^ second) == (x, b)

@test('Finite-prefix projections are onto and the all-ones prefixes are compatible')
def prefixes() -> None:
    words = tuple(product((0, 1), repeat=8))
    for n in range(1, 9):
        assert {w[:n] for w in words} == set(product((0, 1), repeat=n))
    for n in range(1, 64):
        assert tuple([1] * (n + 1))[:n] == tuple([1] * n)
    # No finite test establishes inverse-limit completeness. DERIVATION.md
    # proves that finite-support sequences do not contain the all-ones sequence.


def main() -> int:
    records = []
    for name, fn in TESTS:
        try:
            fn()
            records.append({'test': name, 'passed': True})
        except Exception as exc:
            records.append({'test': name, 'passed': False,
                            'error': f'{type(exc).__name__}: {exc}'})
    result = {
        'scope': 'Constructed mathematical interface examples only; not actual native-physics validation.',
        'python': platform.python_version(),
        'tests_run': len(records),
        'passed': sum(r['passed'] for r in records),
        'failed': sum(not r['passed'] for r in records),
        'native_GR_equivalence_proved': False,
        'tests': records,
    }
    Path(__file__).with_name('CHECK_RESULTS.json').write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))
    return int(result['failed'] != 0)

if __name__ == '__main__':
    sys.exit(main())
