from __future__ import annotations
import numpy as np

def bosonic_one_loop(K):
    sign,logdet=np.linalg.slogdet(K)
    if sign<=0:
        raise ValueError("Positive gauge-fixed Hessian required")
    return .5*logdet

def background_derivative(K,G):
    return .5*np.trace(np.linalg.inv(K)@G)
