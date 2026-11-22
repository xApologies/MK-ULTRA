#!/usr/bin/env python3
"""Check Step 02 algebra and interpolation.

The matrices and parameter values here are mathematical test fixtures, not
recovered Genesis operator implementations or empirical measurements.
Requires Python 3, sympy, and numpy. No network or repository writes.
"""
from pathlib import Path
import json
import math
import sys
import numpy as np
import sympy as sp

results = []

def exact(name, residual):
    if isinstance(residual, sp.MatrixBase):
        simplified = residual.applyfunc(sp.trigsimp)
        ok = simplified == sp.zeros(*residual.shape)
    else:
        simplified = sp.trigsimp(sp.simplify(residual))
        ok = simplified == 0
    results.append({'name': name, 'kind': 'exact_symbolic', 'passed': bool(ok),
                    'residual': str(simplified)})
    if not ok:
        raise AssertionError(f'{name}: {simplified}')

th, n = sp.symbols('theta n', real=True)
# The native characteristic equation at eta = 4 sin(theta/2)^2.
exact('native_characteristic_equation', 2*sp.cos(th)-2+4*sp.sin(th/2)**2)
# C maps adjacent native configurations (q_n,q_{n+1}) to (q,v).
C = sp.Matrix([[1, 0], [-th*sp.cos(th)/sp.sin(th), th/sp.sin(th)]])
U = sp.Matrix([[0, 1], [-1, 2*sp.cos(th)]])
M = sp.Matrix([[sp.cos(th), sp.sin(th)/th], [-th*sp.sin(th), sp.cos(th)]])
exact('exact_interpolation_conjugacy_M_C_equals_C_U', M*C-C*U)
exact('initial_data_map_determinant', C.det()-th/sp.sin(th))
C0 = C.applyfunc(lambda x: sp.limit(x,th,0))
U0 = U.subs(th,0)
M0 = M.applyfunc(lambda x: sp.limit(x,th,0))
exact('zero_mode_conjugacy', M0*C0-C0*U0)
# An isometric embedding need not cover its chosen target space.
T = sp.Matrix([[1,0], [0,1], [0,0]])
Pg, Q = sp.eye(2), T*T.T
exact('isometry_left_round_trip', T.T*T-Pg)
exact('range_projector_idempotent', Q*Q-Q)
D = sp.eye(3)-Q
exact('coverage_defect_projector_idempotent', D*D-D)
assert D != sp.zeros(3)
results.append({'name':'isometry_does_not_imply_surjectivity',
                'kind':'exact_counterexample_to_extra_inference','passed':True,
                'target_defect':str(D)})
z = sp.symbols('z', real=True)
residual = z**2-4*sp.sin(z/2)**2
series = sp.series(residual,z,0,10)
exact('naive_spectrum_residual_series',
      series.removeO()-(z**4/sp.Integer(12)-z**6/sp.Integer(360)+z**8/sp.Integer(20160)))
results.append({'name':'naive_spectrum_residual_at_z_1','kind':'numeric_fixture',
                'passed':bool(float(residual.subs(z,1))>0),
                'value':float(residual.subs(z,1))})
# The endpoint eta=4 carries an extra generalized recurrence solution.
a,b = sp.symbols('a b', real=True)
# q_n=(-1)^n (a+bn); remove the common (-1)^n before simplification.
exact('eta_4_generalized_mode', -(a+b*(n+1))+2*(a+b*n)-(a+b*(n-1)))
# Explicit spectral matrix fixture: no claim this is the native ER network.
V = np.array([[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]],dtype=float)/2
eta = np.array([0.,.25,1.,3.])
theta = 2*np.arcsin(np.sqrt(eta)/2)
N = V @ np.diag(eta) @ V.T
q0 = np.array([.2,-.7,1.1,.3])
q1 = np.array([.9,.2,-.1,.8])
a_mode = V.T@q0
r = V.T@q1-np.cos(theta)*a_mode
fac = np.ones_like(theta)
mask = theta>0
fac[mask] = theta[mask]/np.sin(theta[mask])
v_mode = fac*r

def continuous(s):
    sin_over = np.full_like(theta,float(s))
    sin_over[mask] = np.sin(s*theta[mask])/theta[mask]
    return V@(np.cos(s*theta)*a_mode+sin_over*v_mode)

prev,current=q0.copy(),q1.copy()
max_error=max(np.max(np.abs(continuous(0)-q0)),np.max(np.abs(continuous(1)-q1)))
for k in range(1,20):
    nxt=(2*np.eye(4)-N)@current-prev
    max_error=max(max_error,float(np.max(np.abs(nxt-continuous(k+1)))))
    prev,current=current,nxt
assert max_error<1e-11, max_error
results.append({'name':'four_mode_exact_interpolant_vs_recurrence_20_steps',
                'kind':'numeric_fixture','passed':True,'max_abs_error':float(max_error),
                'native_eigenvalues_used':eta.tolist()})
# Intertwining spectral identity for the same fixture.
Theta = V@np.diag(theta)@V.T
B = V@np.diag(4*np.sin(theta/2)**2)@V.T
max_spectral_error=float(np.max(np.abs(N-B)))
assert max_spectral_error<1e-12
results.append({'name':'spectral_matching_fixture','kind':'numeric_fixture','passed':True,
                'max_abs_error':max_spectral_error})
report={
 'status':'ALL_LISTED_CHECKS_PASSED',
 'scope':'Algebraic consequences and synthetic fixtures only. Not native GR equivalence validation.',
 'python':sys.version.split()[0],'numpy':np.__version__,'sympy':sp.__version__,
 'tests':results,'check_count':len(results),
 'not_checked':['Actual native operators R_C, F_g, Pi_T',
                'Actual ER weights or a Time-Shell clock law',
                'Global or nonlinear Einstein equivalence',
                'Empirical predictions or observations']}
path=Path(__file__).with_name('CHECK_RESULTS.json')
path.write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
