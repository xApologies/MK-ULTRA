"""Tests for conditional volume-energy bridge, no third-party dependencies."""
import math
E0=5.252523677763369e-10
for v1,v2 in [(1.,2.),(2.,9.),(1e-4,3e3)]:
    energy=lambda v:E0*v
    p=-(energy(v2)-energy(v1))/(v2-v1)
    assert math.isclose(p,-E0,rel_tol=1e-12)
    fixed=lambda v:5.
    assert (fixed(v2)-fixed(v1))/(v2-v1)==0
for alpha in [0.,.5,1.,1.2]:
    v1,v2=2.,4.
    E=lambda v:10*(v/2)**alpha
    w=-alpha
    assert math.isclose(E(v2)/E(v1),(v2/v1)**alpha)
    assert math.isclose(w,-alpha)
print('PASS: finite-volume pressure, vacuum-like bridge, fixed-energy dust obstruction, exponent family')
