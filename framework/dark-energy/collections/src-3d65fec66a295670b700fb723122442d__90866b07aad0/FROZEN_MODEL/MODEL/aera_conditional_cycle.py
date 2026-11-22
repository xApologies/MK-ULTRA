"""AERA conditional shell-threshold and transfer evaluator.
This is a computational model of specified assumptions, not Genesis-native syntax or evidence for physical cosmology.
No calculus, no network access, no third-party dependencies.
"""
from dataclasses import dataclass
from math import isclose

@dataclass(frozen=True)
class Shell:
    a0: float
    k_eff: float
    rho_de: float
    ell0: float
    ell_max: float

def binding_density(a, s):
    assert a >= s.a0 > 0 and s.k_eff > 0
    return s.k_eff * (a-s.a0)**2 / a**3

def stable_interval_exists(s):
    return s.rho_de*s.a0/s.k_eff < 4/27

def late_binding_threshold(s, steps=120):
    """Find x_+>3 by monotone bisection, if stable interval exists."""
    if not stable_interval_exists(s):
        return None
    lo=3*s.a0
    hi=lo
    while binding_density(hi,s)>s.rho_de:
        hi*=2
    for _ in range(steps):
        mid=(lo+hi)/2
        if binding_density(mid,s)>s.rho_de: lo=mid
        else: hi=mid
    return (lo+hi)/2

def spacing_threshold(s):
    return s.a0*s.ell_max/s.ell0

def first_failure(s):
    b=late_binding_threshold(s)
    if b is None: return None
    sp=spacing_threshold(s)
    # For model use, starting coherent interval must be checked; a spacing
    # threshold below 3*a0 is not a legitimate late-branch crossing.
    if sp <= 3*s.a0: return None
    return min(b,sp)

@dataclass(frozen=True)
class Budget:
    shell: float
    interior: float
    other: float
    volume: float
    rho_nuc: float

def transfer(b,q):
    assert 0 <= q <= b.shell and b.volume>0 and b.rho_nuc>=0
    out=Budget(b.shell-q,b.interior+q,b.other,b.volume,b.rho_nuc)
    assert isclose(out.shell+out.interior+out.other,
                   b.shell+b.interior+b.other, rel_tol=1e-12, abs_tol=1e-12)
    return out

def eligible(b):
    return b.interior >= b.rho_nuc*b.volume

def run_tests():
    s=Shell(1,1,0.05,1,100)
    assert stable_interval_exists(s)
    a=late_binding_threshold(s)
    assert a>3 and abs(binding_density(a,s)-s.rho_de)<1e-10
    assert first_failure(s)==min(a,100)
    assert not stable_interval_exists(Shell(1,1,0.2,1,100))
    b=Budget(10,2,1,2,5)
    assert not eligible(b)
    assert eligible(transfer(b,8))
    assert not eligible(transfer(b,7))
    print("PASS: conditional shell threshold and transfer-accounting tests")

if __name__=="__main__":
    run_tests()
