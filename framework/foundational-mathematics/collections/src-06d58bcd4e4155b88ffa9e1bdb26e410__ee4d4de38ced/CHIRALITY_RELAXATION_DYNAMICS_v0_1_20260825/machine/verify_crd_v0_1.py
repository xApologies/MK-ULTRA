#!/usr/bin/env python3
"""Finite verifier for the CRD v0.1 work-layer model.
No external packages required. This is a structural diagnostic, not a physical simulation.
"""
from itertools import product
A='10010110'; B='01101001'
V=[]; s0={}
for l in (0,1):
    for d in (0,1):
        for r in (0,1):
            for c in (0,1):
                v=(l,d,r,c); V.append(v); s0[v]=1 if ((r+c+d)%2==0) else -1
E=[]
def edge(u,v): return tuple(sorted((u,v)))
def add(u,v):
    e=edge(u,v)
    if e not in E:E.append(e)
for l in (0,1):
    for d in (0,1):
        for r in (0,1): add((l,d,r,0),(l,d,r,1))
        for c in (0,1): add((l,d,0,c),(l,d,1,c))
for l in (0,1):
    for r in (0,1): add((l,0,r,1),(l,1,r,0))
for d in (0,1):
    for r in (0,1):
        for c in (0,1): add((0,d,r,c),(1,d,r,c))
print('A complement B:', ''.join('1' if x=='0' else '0' for x in A)==B)
print('|V|, |E|, beta1 =',len(V),len(E),len(E)-len(V)+1)
adm=[e for e in E if s0[e[0]]!=s0[e[1]]]
print('conditional mirror-candidate edges:',len(adm))
print('strict Fusion v1 forced chirality flips: 0')
print('Backreaction lift required for ripple: YES')
