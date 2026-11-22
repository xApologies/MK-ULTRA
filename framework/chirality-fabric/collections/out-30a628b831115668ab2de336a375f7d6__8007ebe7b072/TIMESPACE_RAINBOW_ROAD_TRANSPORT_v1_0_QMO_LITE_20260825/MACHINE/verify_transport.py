#!/usr/bin/env python3
"""Synthetic verifier for the transport-composition theorem.
This is an algebraic witness, not physical evidence.
"""
MOD=7
PORTALS=[1,3,2,4]
rhoQ=lambda x:(2*x)%MOD
rhoG=lambda x:(3*x)%MOD
UQ=lambda y,d:(y+2*d)%MOD
UG=lambda y,d:(y+3*d)%MOD

for x in range(MOD):
    for d in PORTALS:
        assert rhoQ((x+d)%MOD)==UQ(rhoQ(x),d)
        assert rhoG((x+d)%MOD)==UG(rhoG(x),d)

for x in range(MOD):
    xt=x
    q=rhoQ(x); g=rhoG(x)
    for d in PORTALS:
        xt=(xt+d)%MOD
        q=UQ(q,d); g=UG(g,d)
    assert q==rhoQ(xt)
    assert g==rhoG(xt)

def walk(x,road):
    for d in road:x=(x+d)%MOD
    return x
assert walk(0,[1,3])==walk(0,[2,2])
assert [1,3] != [2,2]
print("PASS")
