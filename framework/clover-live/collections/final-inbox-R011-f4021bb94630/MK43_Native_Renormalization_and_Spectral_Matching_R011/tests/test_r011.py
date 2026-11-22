from __future__ import annotations
import json
import sys
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"code"))

from spectral_matching import mode_decomposition,schur,hard_threshold,smooth_threshold
from parameter_rank import symmetric_parameter_map,relation_basis
from functional_determinant import bosonic_one_loop,background_derivative

R010=ROOT.parent/"MK43_Continuum_Field_Action_Closure_R010/operators"
A=np.load(R010/"HIDDEN_FEEDBACK_A.npy")
B=np.load(R010/"HIDDEN_FEEDBACK_B.npy")
K=np.load(R010/"HIDDEN_FEEDBACK_K.npy")
S=np.load(R010/"HIDDEN_FEEDBACK_SCHUR.npy")

modes=mode_decomposition(B,K)
spectral=sum(term for _,_,term in modes)
assert np.linalg.norm(spectral-B@np.linalg.inv(K)@B.T)<1e-10
assert np.linalg.norm(schur(A,B,K)-S)<1e-10

high=hard_threshold(A,modes,100.)
low=hard_threshold(A,modes,0.)
assert np.linalg.norm(high-A)<1e-10
assert np.linalg.norm(low-S)<1e-10

smooth_high=smooth_threshold(A,modes,1e6)
smooth_low=smooth_threshold(A,modes,0.)
assert np.linalg.norm(smooth_high-A)<1e-8
assert np.linalg.norm(smooth_low-S)<1e-10

F=symmetric_parameter_map([term for _,_,term in modes])
relations,rank=relation_basis(F)
assert rank==4
assert relations.shape[0]==17
assert np.linalg.norm(relations@(F@np.ones(4)))<1e-10

G=np.diag([.2,-.1,.15,.05])
eps=1e-6
fd=(bosonic_one_loop(K+eps*G)-bosonic_one_loop(K-eps*G))/(2*eps)
analytic=background_derivative(K,G)
assert abs(fd-analytic)<1e-8

R007=ROOT.parent/"MK43_Mote_Ensemble_ER_Foam_Assembly_R007/operators"
T7=np.load(R007/"DIMER_PRISM.npy")
B7=np.load(R007/"DIMER_BRIDGE.npy")
C7=T7@B7
assert np.linalg.matrix_rank(C7,tol=1e-10)==1
u,s,vh=np.linalg.svd(C7,full_matrices=False)
target=np.array([0.,-1.,1.,0.])/np.sqrt(2)
assert abs(abs(u[:,0]@target)-1)<1e-10

print(json.dumps({
    "spectral_decomposition_error":float(np.linalg.norm(spectral-B@np.linalg.inv(K)@B.T)),
    "Schur_error":float(np.linalg.norm(schur(A,B,K)-S)),
    "R010_parameter_rank":rank,
    "R010_relation_count":relations.shape[0],
    "one_loop_derivative_error":float(abs(fd-analytic)),
    "R007_dimer_coupling_rank":int(np.linalg.matrix_rank(C7,tol=1e-10)),
    "R007_antisymmetric_overlap":float(abs(u[:,0]@target)),
},indent=2))
