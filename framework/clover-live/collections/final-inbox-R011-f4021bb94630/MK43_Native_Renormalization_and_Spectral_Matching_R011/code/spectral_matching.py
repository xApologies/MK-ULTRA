from __future__ import annotations
import numpy as np

def mode_decomposition(B,K):
    values,vectors=np.linalg.eigh((K+K.conj().T)/2)
    modes=[]
    for i,value in enumerate(values):
        q=vectors[:,i:i+1]
        c=B@q
        modes.append((value,c,c@c.conj().T/value))
    return modes

def schur(A,B,K,z=0.0):
    return A-B@np.linalg.inv(K-z*np.eye(K.shape[0]))@B.conj().T

def hard_threshold(A,modes,mu):
    correction=np.zeros_like(A,dtype=complex)
    for mass_squared,c,term in modes:
        if np.sqrt(mass_squared)>mu:
            correction+=term
    return A-correction

def smooth_threshold(A,modes,mu):
    correction=np.zeros_like(A,dtype=complex)
    for mass_squared,c,term in modes:
        correction+=mass_squared/(mass_squared+mu*mu)*term
    return A-correction
