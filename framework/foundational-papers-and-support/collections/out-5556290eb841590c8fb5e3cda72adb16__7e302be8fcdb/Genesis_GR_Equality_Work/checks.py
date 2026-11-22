"""Reproduce local algebra checks only; these do NOT validate native Genesis–GR equivalence.

Requires sympy. Run: python checks.py
The full tensor derivations and hypotheses are in DERIVATION.md.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp


def run_checks() -> dict:
    x = sp.symbols('x', real=True)
    beta = sp.symbols('beta', nonzero=True, real=True)
    tau = sp.Function('tau')(x)
    V = sp.Function('V')
    L_tau = -sp.Rational(1, 2) * (beta * sp.diff(tau, x)**2 + V(tau))
    euler_tau = sp.diff(L_tau, tau) - sp.diff(sp.diff(L_tau, sp.diff(tau, x)), x)
    expected_tau = beta * sp.diff(tau, x, 2) - sp.diff(V(tau), tau) / 2
    assert sp.simplify(euler_tau - expected_tau) == 0

    # Lorentzian diagonal inverse metric. The determinant variation is checked explicitly.
    a0 = sp.symbols('a0', negative=True)
    a1, a2, a3 = sp.symbols('a1 a2 a3', positive=True)
    aa = [a0, a1, a2, a3]
    vv = sp.symbols('v0:4', real=True)
    U = sp.symbols('U', real=True)
    measure = 1 / sp.sqrt(-a0*a1*a2*a3)
    L_chi = -sum(a*v*v for a, v in zip(aa, vv)) / 2 - U
    components = []
    for a, v in zip(aa, vv):
        derived = sp.simplify(-2 / measure * sp.diff(measure * L_chi, a))
        corrected = v*v + L_chi/a
        archived = v*v - L_chi/a
        assert sp.simplify(derived - corrected) == 0
        assert sp.simplify(archived - derived + 2*L_chi/a) == 0
        components.append(str(sp.simplify(derived)))
    flat = {a0:-1, a1:1, a2:1, a3:1, vv[1]:0, vv[2]:0, vv[3]:0}
    derived00 = sp.simplify((-2/measure*sp.diff(measure*L_chi,a0)).subs(flat))
    archived00 = sp.simplify((vv[0]**2-L_chi/a0).subs(flat))
    assert sp.simplify(derived00 - (vv[0]**2/2 + U)) == 0
    assert sp.simplify(archived00 - (3*vv[0]**2/2 - U)) == 0

    # Exact equation-space equivalence with a nonzero off-shell correction.
    E1, E2 = sp.symbols('E1 E2')
    A = sp.Matrix([[2,1],[0,3]])
    E = sp.Matrix([E1,E2])
    assert A.det() == 6
    assert A.inv()*(A*E) == E

    # Bijective but nonregular field redefinition: x=q^3, S(x)=x.
    q = sp.symbols('q', real=True)
    assert sp.diff(q**3, q).subs(q,0) == 0
    assert sp.diff(x, x) == 1

    return {
        'status':'PASS: local symbolic checks only',
        'sympy_version':sp.__version__,
        'phase_Euler_Lagrange':str(euler_tau),
        'phase_result':'beta*Box(tau) - V_prime(tau)/2, for the isolated displayed phase action',
        'chromatic_Hilbert_diagonal_components':components,
        'homogeneous_chromatic_energy_correct':str(derived00),
        'homogeneous_chromatic_energy_archived':str(archived00),
        'invertible_equation_multiplier_determinant':str(A.det()),
        'singular_reparametrization':'x=q^3 is bijective, but DP=0 at q=0; S(x)=x has no critical point while S(q^3)=q^3 does.',
        'limitations':[
            'Not a proof of a native projection, a GR lift, native gauge identification, nonlinear closure, or empirical agreement.',
            'The diagonal scalar calculation checks coefficients and signs; the report supplies the general tensor derivation.',
            'Cross-couplings and ER terms are not silently set to zero in the total theory; the phase check isolates the archived S_tau contribution.'
        ]
    }

if __name__ == '__main__':
    result = run_checks()
    text = json.dumps(result, indent=2, ensure_ascii=False)
    Path(__file__).with_name('CHECK_RESULTS.json').write_text(text+'\n')
    print(text)
