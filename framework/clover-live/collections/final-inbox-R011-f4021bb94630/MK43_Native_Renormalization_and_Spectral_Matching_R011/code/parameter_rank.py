from __future__ import annotations
import numpy as np

def symmetric_parameter_map(matrices):
    n=matrices[0].shape[0]
    upper=np.triu_indices(n)
    return np.stack([m[upper] for m in matrices],axis=1)

def relation_basis(F,tol=1e-10):
    u,s,vh=np.linalg.svd(F,full_matrices=True)
    rank=int(np.sum(s>tol))
    return u[:,rank:].T,rank
