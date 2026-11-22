"""Finite exact checks; they do not certify the full native theory."""
from __future__ import annotations
import json, sys, time
from pathlib import Path
import sympy as s
from coupled_source import phase_chromatic_model, evaluate_scalar_action, covariant_stress_divergence
ROOT=Path(__file__).resolve().parents[1]
rows=[]

def equal(actual, expected):
    if isinstance(actual,s.MatrixBase) or isinstance(expected,s.MatrixBase):
        a=s.Matrix(actual);b=s.Matrix(expected)
        assert a.shape==b.shape
        assert all(s.simplify(x)==0 for x in a-b), str(a-b)
    else:
        assert s.simplify(actual-expected)==0, str(s.simplify(actual-expected))

def check(name, fn, scope):
    t=time.time()
    try:
        detail=fn()
        rows.append({'name':name,'passed':True,'scope':scope,'detail':detail,'seconds':time.time()-t})
        print('PASS',name,flush=True)
    except Exception as e:
        rows.append({'name':name,'passed':False,'scope':scope,'error':repr(e),'seconds':time.time()-t})
        print('FAIL',name,repr(e),flush=True)

t,x,y,z=s.symbols('t x y z',real=True);coords=(t,x,y,z)
eta=s.diag(-1,1,1,1)
T,C=s.symbols('tau chi',real=True)
beta,gamma=s.symbols('beta gamma',real=True)

def mixed_phase_mismatch():
    K,P=phase_chromatic_model(T,[C],s.eye(1),beta,gamma,0,0,s.Rational(1,2))
    r=evaluate_scalar_action(coords,eta,(T,C),(0,x),K,P)
    equal(r.euler_lagrange[0],gamma)
    # Printed beta Box tau - V' = gamma chi Box chi gives zero on each side.
    printed=0
    assert s.simplify(r.euler_lagrange[0]-printed)!=0
    return {'action_residual':str(r.euler_lagrange[0]),'printed_residual':'0',
            'not_a_full_gr_solution':'This is a comparison of matter equation expressions on a prescribed flat metric.'}
check('mixed_phase_equation_detects_missing_gradient_term',mixed_phase_mismatch,'Archived action versus printed equation, one active chromatic component')

def mixed_chi_mismatch():
    c=s.symbols('c',nonzero=True,real=True)
    K,P=phase_chromatic_model(T,[C],s.eye(1),beta,gamma,0,0,s.Rational(1,2))
    r=evaluate_scalar_action(coords,eta,(T,C),(t*t,c),K,P)
    equal(r.euler_lagrange[1],-2*gamma*c)
    return {'action_chi_residual':str(r.euler_lagrange[1]),'printed_chi_residual':'0'}
check('mixed_chromatic_equation_detects_missing_phase_backreaction',mixed_chi_mismatch,'One active component; no claim of metric equation solution')

def stress_variation():
    # Independent inverse-metric variation of the local scalar Lagrangian.
    h00,h01,h11=s.symbols('h00 h01 h11');u0,u1,v0,v1=s.symbols('u0 u1 v0 v1')
    gs,gam,c,pot=s.symbols('G gamma chi potential')
    hi=s.Matrix([[h00,h01],[h01,h11]]);g=hi.inv();u=s.Matrix([u0,u1]);v=s.Matrix([v0,v1])
    L=-beta*(u.T*hi*u)[0]/2-gs*(v.T*hi*v)[0]/2-gam*gs*c*(u.T*hi*v)[0]-pot
    wanted=beta*u*u.T+gs*v*v.T+gam*gs*c*(u*v.T+v*u.T)+g*L
    # Offdiagonal variation differentiates two symmetric entries.
    equal(-2*s.diff(L,h00)+g[0,0]*L,wanted[0,0])
    equal(-s.diff(L,h01)+g[0,1]*L,wanted[0,1])
    equal(-2*s.diff(L,h11)+g[1,1]*L,wanted[1,1])
    return {'tested':'diagonal and offdiagonal metric-variation coefficients'}
check('mixed_stress_from_metric_variation',stress_variation,'Exact symbolic local variation, two active directions in four-dimensional metric')

def ward_variable_G():
    K,P=phase_chromatic_model(T,[C],s.Matrix([[1+C*C]]),s.Integer(2),s.Rational(1,3),T*T,C**4,s.Rational(1,2))
    fields=(t*x+t,t*t+x)
    r=evaluate_scalar_action(coords,eta,(T,C),fields,K,P)
    div=covariant_stress_divergence(coords,eta,r.stress_covariant)
    rhs=s.Matrix([sum(r.euler_lagrange[i]*s.diff(fields[i],c) for i in range(2)) for c in coords])
    equal(div,rhs)
    return {'ward_identity':'nabla^mu T_mu,nu = sum_I EL_I partial_nu phi^I','variable_field_metric':True}
check('ward_identity_variable_chromatic_metric',ward_variable_G,'Off-shell, nonlinear fields and nonconstant field-space metric')

def curved_ward():
    # Simple curved metric with exact determinant and no singular coordinate points on this patch.
    a=s.exp(t);g=s.diag(-1,a*a,a*a,a*a)
    K,P=phase_chromatic_model(T,[C],s.eye(1),s.Integer(1),s.Rational(1,4),0,0,s.Rational(1,2))
    fields=(t,x)
    r=evaluate_scalar_action(coords,g,(T,C),fields,K,P,volume_density=a**3)
    div=covariant_stress_divergence(coords,g,r.stress_covariant)
    rhs=s.Matrix([sum(r.euler_lagrange[i]*s.diff(fields[i],c) for i in range(2)) for c in coords])
    equal(div,rhs)
    return {'curved_background':'diag(-1,exp(2t),exp(2t),exp(2t))','fields':['t','x']}
check('ward_identity_curved_background',curved_ward,'Covariant divergence independently computed, not a coupled Einstein solution')

def phase_normalization():
    K,P=phase_chromatic_model(T,[C],s.eye(1),s.Integer(1),s.Integer(0),T*T,0,s.Rational(1,2))
    r=evaluate_scalar_action(coords,eta,(T,C),(t,0),K,P)
    equal(r.euler_lagrange[0],-t)
    K2,P2=phase_chromatic_model(T,[C],s.eye(1),1,0,T*T,0,1)
    r2=evaluate_scalar_action(coords,eta,(T,C),(t,0),K2,P2)
    equal(r2.euler_lagrange[0],-2*t)
    return {'half_potential_EL':'-t','full_potential_EL':'-2*t','choice':'Both action variants retained explicitly'}
check('potential_normalizations_are_not_silently_identified',phase_normalization,'Source-variant distinction')

def source_sign():
    K,P=phase_chromatic_model(T,[C],s.eye(1),1,0,0,1,s.Rational(1,2))
    r=evaluate_scalar_action(coords,eta,(T,C),(0,t),K,P)
    equal(r.stress_covariant[0,0],s.Rational(3,2))
    wrong=1-eta[0,0]*r.lagrangian
    equal(wrong,s.Rational(1,2))
    return {'action_energy':'3/2','printed_minus_L_energy':'1/2'}
check('chromatic_stress_sign_recheck',source_sign,'Known source inconsistency, not automatically amended')

def seven_fields():
    cs=s.symbols('chi0:7');K,P=phase_chromatic_model(T,cs,s.eye(7),2,3,0,0,s.Rational(1,2))
    assert K.shape==(8,8)
    for i in range(7): equal(K[0,i+1],3*cs[i])
    equal(K[1:,1:],s.eye(7))
    return {'chromatic_components':7,'kinetic_matrix_size':[8,8]}
check('seven_component_source_construction',seven_fields,'General action construction with the source arity preserved')

W1=s.eye(4)+s.ones(4);D=s.diag(2,1,1,1);W2=D.inv()*W1*D.inv()

def collision():
    equal(D*W2*D.T,W1)
    assert all(v>0 for v in W1) and all(v>0 for v in W2)
    g0=eta-W1/10
    equal(g0+W1/10,eta);equal(g0+(D*W2*D.T)/10,eta)
    # Background spatial block is positive; Schur complement is negative.
    assert all(k>0 for k in g0[1:,1:].eigenvals())
    schur=(s.Matrix([[g0[0,0]]])-g0[0:1,1:]*g0[1:,1:].inv()*g0[1:,0:1])[0]
    assert schur<0
    return {'W1':str(W1),'W2':str(W2),'same_metric':'Minkowski','scope':'Admitted algebraic inputs, not proven full native solutions'}
check('unknown_covectors_prevent_unique_metric_factorization',collision,'Actual archived ER metric formula with positive symmetric network weights')

def laplacian(W):return s.diag(*[sum(W[i,j] for j in range(W.cols)) for i in range(W.rows)])-W

def spectra():
    L1,L2=laplacian(W1),laplacian(W2)
    assert L1.eigenvals()=={s.Integer(0):1,s.Integer(4):3}
    assert L2.eigenvals()=={s.Integer(0):1,s.Integer(2):1,s.Rational(7,2):2}
    assert L1.trace()!=L2.trace()
    return {'spectrum1':['0','4','4','4'],'spectrum2':['0','2','7/2','7/2'],
            'interpretation':'Not a site relabeling of the supplied graph operator; not a proof of full physical inequivalence'}
check('same_metric_different_archived_graph_operators',spectra,'Uses exact L_ER=sum_j W_ij(f_i-f_j)')

def white_calibration():
    J=s.ones(4);X0=s.eye(4)+(s.sqrt(5)-1)*J/4
    equal(X0*X0.T,W1)
    g0=eta-W1/10
    equal(g0+X0*s.eye(4)*X0.T/10,eta)
    return {'white_reference':'W=I, Xi=X0','not_claimed':'No native law selecting this Xi family is inferred'}
check('factorization_example_can_match_white_reference',white_calibration,'Compatibility of the displayed algebraic reference condition only')

def full_derivative():
    r=s.symbols('r',positive=True);W=s.diag(r*r,1,1,1);Xi=s.diag(1/r,1,1,1)
    G=Xi*W*Xi.T
    equal(G,s.eye(4));equal(G.diff(r),s.zeros(4))
    fixed=Xi*W.diff(r)*Xi.T
    assert fixed!=s.zeros(4)
    total=Xi.diff(r)*W*Xi.T+Xi*W.diff(r)*Xi.T+Xi*W*Xi.diff(r).T
    equal(total,s.zeros(4))
    return {'total_metric_derivative':'0','fixed_covector_piece':str(fixed)}
check('full_native_jacobian_includes_covector_derivatives',full_derivative,'Exact scalar family satisfying the ER metric formula')

def action_chain():
    w,a,c=s.symbols('w a c',real=True)
    g=s.Symbol('g',real=True)
    Sg=g*g/2;SER=-a*w
    pulled=Sg.subs(g,w)+SER
    native=s.diff(pulled,w)
    equal(native,w-a)
    equal(native.subs(w,a),0)
    equal(s.diff(Sg,g).subs(g,a),a)
    return {'native_stationarity':'w-a=0','original_target_stationarity':'g=0',
            'scope':'Finite-dimensional chain-rule illustration, not a proposed gravitational action'}
check('explicit_ER_action_term_cannot_be_omitted',action_chain,'Illustrates E_W=(Dg)^*E_g+explicit_E_W')

def adjoint():
    a=s.Matrix([[1,1,0,0],[0,2,0,0],[0,0,1,1],[0,0,0,1]])
    e=s.Matrix(4,4,lambda i,j:s.Symbol('e'+str(min(i,j))+str(max(i,j))))
    v=s.Matrix(4,4,lambda i,j:s.Symbol('v'+str(min(i,j))+str(max(i,j))))
    left=s.trace(e.T*(a*v*a.T));right=s.trace((a.T*e*a).T*v)
    equal(left,right)
    return {'identity':'<E, Xi dW Xi^T> = <Xi^T E Xi, dW>'}
check('matrix_variation_adjoint',adjoint,'Exact symmetric matrix pairing')

def constant_graph_variations():
    u=s.Symbol('u',real=True);r=u-s.Rational(1,2)
    equal(s.integrate(r,(u,0,1)),0)
    assert r!=0
    return {'integrated_equation':'0','local_residual':'u-1/2','scope':'Function-space illustration of finite versus local variations'}
check('constant_graph_stationarity_is_not_local_field_stationarity',constant_graph_variations,'Not an Einstein solution or no-go theorem for all native models')

report={'status':'PASS' if all(x['passed'] for x in rows) else 'FAIL','count':len(rows),
        'passed':sum(x['passed'] for x in rows),'sympy_version':s.__version__,'python_version':sys.version,
        'scope':'Exact finite symbolic examples and checks of displayed derivations. No native physical inverse or total GR equivalence is certified.',
        'checks':rows}
(ROOT/'results').mkdir(exist_ok=True)
(ROOT/'results/CHECK_RESULTS.json').write_text(json.dumps(report,indent=2))
print(report['status'],report['passed'],'/',report['count'],flush=True)
if report['status']!='PASS':sys.exit(1)
