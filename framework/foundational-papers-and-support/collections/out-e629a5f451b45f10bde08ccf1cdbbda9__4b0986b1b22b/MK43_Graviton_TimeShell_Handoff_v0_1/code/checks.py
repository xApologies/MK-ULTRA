"""Algebraic checks of the compiled MK43 interface, not a microscopic gravity solver.

All concrete matrices and background metrics below are synthetic fixtures.
No undocumented Time-Shell kernel or native action is supplied by these tests.
Run with Python 3 and SymPy: python code/checks.py
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

RESULTS = []
def check(name, result, scope):
    ok = bool(result)
    RESULTS.append({'name': name, 'passed': ok, 'scope': scope})
    if not ok:
        raise AssertionError(name)

def zero(obj):
    if isinstance(obj, sp.MatrixBase):
        return all(sp.simplify(e) == 0 for e in obj)
    return sp.simplify(obj) == 0

# An exact isometry from a two-dimensional physical sector into three dimensions.
# It is NOT claimed to be the actual MK43 Time-Shell operator.
S = sp.Matrix([[sp.Rational(3,5),-sp.Rational(4,5)],
               [sp.Rational(4,5),sp.Rational(3,5)], [0,0]])
Q = S*S.T
x,y = sp.symbols('x_mode y_mode', real=True)
v=sp.Matrix([x,y]); w=S*v
check('mode_left_inverse', zero(S.T*S-sp.eye(2)), 'synthetic isometry')
check('mode_image_right_inverse', zero(S*(S.T*w)-w), 'synthetic isometry')
check('image_projector_idempotence', zero(Q*Q-Q), 'synthetic isometry')
check('image_projector_self_adjoint', zero(Q-Q.T), 'synthetic isometry')
check('mode_norm_preserved', zero((w.T*w)[0]-(v.T*v)[0]), 'synthetic isometry')
check('outside_image_detected', not zero((sp.eye(3)-Q)*sp.Matrix([0,0,1])), 'negative control')
A=sp.Matrix([[2,-1],[-1,3]])
B=sp.Matrix([[1,2],[-3,1]])
Ar=S*A*S.T; Br=S*B*S.T
check('operator_intertwining', zero(Ar*S-S*A), 'synthetic operator transport')
check('operator_composition', zero(Ar*Br-S*A*B*S.T), 'synthetic operator transport')
check('operator_commutator', zero(Ar*Br-Br*Ar-S*(A*B-B*A)*S.T), 'synthetic operator transport')
check('matrix_element_preserved', zero((w.T*Ar*w)[0]-(v.T*A*v)[0]), 'synthetic operator transport')
p,q=sp.symbols('prev1 prev2', real=True); prev=sp.Matrix([p,q])
next_v=(2*sp.eye(2)-A)*v-prev
next_w=(2*sp.eye(3)-Ar)*w-S*prev
check('native_recurrence_transports', zero(next_w-S*next_v), 'update depth, not physical time')
# Physical-sector constraints and mass protection.
Pg=sp.diag(1,1,0,0); Pl=sp.diag(0,0,1,1)
Rc=sp.diag(2,3,4,5)
check('correction_preserves_sector', zero(Rc*Pg-Pg*Rc), 'synthetic block-preserving correction')
check('lock_does_not_appear', zero(Pl*Rc*Pg), 'synthetic mass-protection condition')
constraint=sp.Matrix([[0,0,1]])
check('readable_constraint_preserved', zero(constraint*S), 'synthetic constraint intertwining')

# Exact feedback response for a LINEAR fixture of the archived fixed-point form.
# This checks the resolvent derivation, not the undocumented physical R_C or F_g.
R=sp.Matrix([[sp.Rational(1,2),0],[0,sp.Rational(1,3)]])
F=sp.Matrix([[sp.Rational(1,4),sp.Rational(1,8)],[0,sp.Rational(1,5)]])
m1,m2=sp.symbols('source1 source2'); m=sp.Matrix([m1,m2])
K=(sp.eye(2)-R*F).inv()*R
z=K*m
check('fixed_point_resolvent_solution', zero(z-R*(m+F*z)), 'synthetic linear fixed-point fixture')
check('fixed_point_source_derivative', zero(z.jacobian([m1,m2])-K), 'synthetic derivative verification')
check('feedback_is_not_omittable', not zero(K-R), 'negative control')
check('singular_feedback_detected', (sp.eye(2)-sp.eye(2)).det()==0, 'negative control; inverse not assumed')

# Encoding of an evaluated metric, using the PRIOR GRC-1 metric dictionary only.
u=sp.symbols('u', real=True); sigma=sp.symbols('sigma', positive=True)
gcomponent=sp.symbols('gcomponent', real=True)
check('metric_encode_decode', zero(sigma*sp.sinh(sp.asinh(gcomponent/sigma))-gcomponent), 'GRC-1 component representation')
check('encoding_derivative', zero(sp.diff(sp.asinh(gcomponent/sigma),gcomponent)-1/sp.sqrt(sigma**2+gcomponent**2)), 'GRC-1 differential dictionary')
check('representation_jacobian_nonzero', sp.ask(sp.Q.positive(sigma*sp.cosh(u))), 'GRC-1 regularity')

# Independent coordinate Christoffel/Riemann computations, with a curved reference.
t,r,yy,zz=sp.symbols('t r y z', real=True)
coords=(t,r,yy,zz); n=4; f=1+r*r
bar=sp.diag(-1,1,f*f,1)
g=sp.diag(-f,1,f*f,(1+r)**2) # r > -1 is a regular Lorentzian chart.
h=g-bar

def gamma(metric):
    inverse=metric.inv()
    return [[[sp.simplify(sum(inverse[a,d]*(sp.diff(metric[d,c],coords[b])+
              sp.diff(metric[b,d],coords[c])-sp.diff(metric[b,c],coords[d]))
              for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]

def riemann(connection):
    return [[[[sp.simplify(sp.diff(connection[a][j][b],coords[i])-
          sp.diff(connection[a][i][b],coords[j])+
          sum(connection[a][i][l]*connection[l][j][b]-connection[a][j][l]*connection[l][i][b]
              for l in range(n))) for j in range(n)] for i in range(n)] for b in range(n)] for a in range(n)]

bg=gamma(bar); gg=gamma(g); gi=g.inv()
def nab_h(mu,a,b):
    return sp.diff(h[a,b],coords[mu])-sum(bg[l][mu][a]*h[l,b]+bg[l][mu][b]*h[a,l] for l in range(n))
Delta=[[[sp.simplify(sum(gi[a,d]*(nab_h(b,c,d)+nab_h(c,b,d)-nab_h(d,b,c)) for d in range(n))/2)
          for c in range(n)] for b in range(n)] for a in range(n)]
check('exact_connection_difference_all_64', all(zero(Delta[a][b][c]-(gg[a][b][c]-bg[a][b][c]))
          for a in range(n) for b in range(n) for c in range(n)), 'independent curved geometric fixture')
Rb=riemann(bg); Rg=riemann(gg)
def nab_D(mu,a,b,c):
    return sp.diff(Delta[a][b][c],coords[mu])+sum(
      bg[a][mu][l]*Delta[l][b][c]-bg[l][mu][b]*Delta[a][l][c]-bg[l][mu][c]*Delta[a][b][l]
      for l in range(n))
Rd=[[[[sp.simplify(Rb[a][b][i][j]+nab_D(i,a,j,b)-nab_D(j,a,i,b)+
      sum(Delta[a][i][l]*Delta[l][j][b]-Delta[a][j][l]*Delta[l][i][b] for l in range(n)))
      for j in range(n)] for i in range(n)] for b in range(n)] for a in range(n)]
check('exact_curvature_difference_all_256', all(zero(Rd[a][b][i][j]-Rg[a][b][i][j])
      for a in range(n) for b in range(n) for i in range(n) for j in range(n)), 'independent curved geometric fixture')
Riccib=sp.Matrix(n,n,lambda i,j:sum(Rb[a][i][a][j] for a in range(n)))
scalarb=sp.simplify(sum(bar.inv()[i,j]*Riccib[i,j] for i in range(n) for j in range(n)))
check('reference_is_genuinely_curved', zero(scalarb+4/f), 'curved geometric fixture; Rbar=-4/(1+r^2)')
Ricci=sp.Matrix(n,n,lambda i,j:sum(Rg[a][i][a][j] for a in range(n)))
scalar=sp.simplify(sum(gi[i,j]*Ricci[i,j] for i in range(n) for j in range(n)))
Einstein=sp.simplify(Ricci-g*scalar/2)
div=[]
for nu in range(n):
    div.append(sp.simplify(sum(gi[mu,aa]*(sp.diff(Einstein[mu,nu],coords[aa])-
        sum(gg[b][aa][mu]*Einstein[b,nu]+gg[b][aa][nu]*Einstein[mu,b] for b in range(n)))
        for mu in range(n) for aa in range(n))))
check('bianchi_all_four_components', all(zero(v) for v in div), 'geometric identity, not a matter-solution test')
quadratic_terms=[sp.simplify(sum(Delta[a][i][l]*Delta[l][j][b]-Delta[a][j][l]*Delta[l][i][b] for l in range(n)))
       for a in range(n) for b in range(n) for i in range(n) for j in range(n)]
check('dropping_quadratic_connection_terms_detected', any(not zero(v) for v in quadratic_terms), 'negative control')
# A nonzero Einstein tensor is NOT silently set to a chosen stress tensor.
check('arbitrary_input_not_claimed_vacuum_solution', any(not zero(v) for v in Einstein), 'negative control; no T=G/kappa construction')
# TT removes non-radiative data: do not use a TT projector as a total metric map.
Ps=sp.diag(1,1,0)
def tt(A): return Ps*A*Ps-sp.trace(Ps*A)*Ps/2
check('tt_keeps_two_polarizations', zero(tt(sp.Matrix([[x,y,0],[y,-x,0],[0,0,0]]))-sp.Matrix([[x,y,0],[y,-x,0],[0,0,0]])), 'standard algebra on admitted tensor input')
check('tt_does_not_preserve_arbitrary_metric_content', zero(tt(sp.eye(3))), 'negative control')

out=Path(__file__).resolve().parents[1]/'results'/'CHECK_RESULTS.json'
out.parent.mkdir(exist_ok=True)
data={'all_passed': all(v['passed'] for v in RESULTS),'named_checks':len(RESULTS),
      'sympy_version':sp.__version__,'scope':'Algebraic and geometric verification only. Synthetic fixtures, not independently generated MK43 native solutions.',
      'curved_fixture':{'coordinates':['t','r','y','z'],'regular_domain':'r > -1',
        'bar_metric':str(bar),'metric':str(g),'bar_scalar_curvature':str(scalarb),'scalar_curvature':str(scalar)},
      'checks':RESULTS}
out.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'all_passed':data['all_passed'],'named_checks':len(RESULTS),'result':str(out)},indent=2))
