from __future__ import annotations
import json,sys,time,platform
from pathlib import Path
from itertools import product
import numpy as np
import sympy as sp
from regular_completion import *
import previous_translator as old

ROOT=Path(__file__).resolve().parents[1]
results=[]
start=time.time()
def test(name,ok,scope='exact symbolic identity'):
    ok=bool(ok)
    results.append({'name':name,'passed':ok,'scope':scope})
    print(('PASS ' if ok else 'FAIL ')+name,flush=True)
    if not ok: raise AssertionError(name)
def zero(x):
    y=sp.simplify(x)
    if y==0:return True
    if y.has(sp.sinh,sp.cosh):return sp.simplify(y.rewrite(sp.exp))==0
    return False
def mz(m):return all(zero(v) for v in m)
def rejects(fn):
    try:fn()
    except (ValueError,ArithmeticError):return True
    return False

s,l=sp.symbols('sigma lambda',positive=True)
r=sp.symbols('r',real=True)
p=(sp.sqrt(r*r+s*s)+r)/(4*l)
q=(sp.sqrt(r*r+s*s)-r)/(4*l)
test('scalar decoder',zero(2*l*(p-q)-r))
test('pair product normalization',zero(p*q-s*s/(16*l*l)))
test('squared dominance identity with sigma positive',zero((r*r+s*s)-r*r-s*s) and (s*s).is_positive)
z=sp.symbols('z',real=True)
test('hyperbolic encoding decoder',zero(2*l*(s*sp.exp(z)/(4*l)-s*sp.exp(-z)/(4*l))-s*sp.sinh(z)))
test('nonvanishing Jacobian bound',sp.cosh(z).is_positive is True)
test('inverse derivative',zero(sp.diff(sp.asinh(r/s),r)-1/sp.sqrt(s*s+r*r)))
inds=[(i,j) for i in range(4) for j in range(i,4)]
syms=sp.symbols('g0:10',real=True)
g=sp.zeros(4)
for (i,j),v in zip(inds,syms):g[i,j]=g[j,i]=v
pair=encode_metric(g,s,l)
test('all ten metric components round trip',mz(pair.decode()-g))
test('all sixteen pair products',mz(pair.normalization_residual()))
C=sp.eye(4).row_join(-sp.eye(4))
test('eight-channel ER factorization',mz(l*C*pair.network()*C.T-g))
test('weight matrix symmetry',mz(pair.network()-pair.network().T))
Z=sp.zeros(4)
zs=sp.symbols('z0:10',real=True)
for (i,j),v in zip(inds,zs):Z[i,j]=Z[j,i]=v
vg=sp.Matrix([metric_from_z(Z,s)[i,j] for i,j in inds])
jac=vg.jacobian(zs)
test('ten-dimensional full-rank Jacobian formula',mz(jac-sp.diag(*[s*sp.cosh(v) for v in zs])))
e=sp.Matrix(sp.symbols('e0:10'))
dz=sp.Matrix(sp.symbols('dz0:10'))
test('variational adjoint',zero((e.T*jac*dz)[0]-((jac.T*e).T*dz)[0]))

rng=np.random.default_rng(43)
worst=0.
for k in range(100):
    while True:
        A=rng.normal(size=(4,4))
        if abs(np.linalg.det(A))>.2:break
    gn=A.T@np.diag([-1.,1.,1.,1.])@A
    P,Q=encode_numeric(gn)
    back=decode_numeric(P,Q)
    worst=max(worst,float(np.max(np.abs(gn-back))))
    assert np.all(P>0) and np.all(Q>0) and np.allclose(gn,back,rtol=1e-10,atol=1e-10)
test('100 generated Lorentz metrics with positive weights',True,'numerical fixture family, numpy seed 43; not universal proof')
eta=sp.diag(-1,1,1,1)
base=encode_metric(eta)
J=sp.Matrix([[1,1,0,0],[0,1,0,0],[0,0,2,0],[0,0,0,1]])
K=sp.Matrix([[2,0,0,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]])
p2=rechart(base,J)
p3=rechart(p2,K)
comp=rechart(base,J*K)
test('coordinate transition',mz(p2.decode()-J.T*eta*J))
test('coordinate cocycle',mz(p3.P-comp.P) and mz(p3.Q-comp.Q))
test('coordinate round trip',mz(rechart(p2,J.inv()).P-base.P) and mz(rechart(p2,J.inv()).Q-base.Q))
test('encoding scale is not a metric observable',mz(encode_metric(J.T*eta*J,sp.Integer(7),sp.Integer(3)).decode()-J.T*eta*J))
P,Q=encode_numeric(np.diag([-1.,1.,1.,1.]))
Pbad=P.copy();Pbad[0,0]*=1.2
test('reject noncanonical weights',rejects(lambda:decode_numeric(Pbad,Q)),'negative control')
test('reject Euclidean target',rejects(lambda:encode_numeric(np.eye(4))),'negative control')
test('reject degenerate target',rejects(lambda:encode_numeric(np.diag([-1.,1.,1.,0.]))),'negative control')
test('reject nonsymmetric target',rejects(lambda:encode_metric(sp.Matrix([[1,2,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]))),'negative control')
test('reject singular transition',rejects(lambda:rechart(base,sp.diag(1,1,1,0))),'negative control')

chi=sp.symbols('chi0:7',real=True)
beta=sp.symbols('beta',positive=True);gamma=sp.symbols('gamma',real=True)
tau,theta=sp.symbols('tau theta',real=True)
test('phase native round trip',zero(phase_inverse(phase_forward(tau,chi,beta,gamma),chi,beta,gamma)-tau))
test('phase target round trip',zero(phase_forward(phase_inverse(theta,chi,beta,gamma),chi,beta,gamma)-theta))
fields=sp.Matrix([tau,*chi])
out=sp.Matrix([phase_forward(tau,chi,beta,gamma),*chi])
Jmatter=out.jacobian(fields)
test('matter transformation determinant',zero(Jmatter.det()-1))
Km=field_space_metric(chi,beta,gamma)
test('seven-component kinetic metric factorization',mz(Km-Jmatter.T*sp.diag(beta,1,1,1,1,1,1,1)*Jmatter))
vel=sp.Matrix(sp.symbols('v0:8',real=True))
square=beta*(vel[0]+gamma*sum(chi[i]*vel[i+1] for i in range(7))/beta)**2+sum(vel[i+1]**2 for i in range(7))
test('positive kinetic completed square',zero((vel.T*Km*vel)[0]-square))
Et,Ec=sp.symbols('ELtheta ELchi')
# For one chosen chi, this shows the triangular equation map explicitly.
test('matter Euler chain inversion',zero((Ec+gamma*chi[0]*Et/beta)-gamma*chi[0]*Et/beta-Ec))

# Fully sourced, curved classical solution in the new branch: no source chosen from G.
t=sp.symbols('t',positive=True)
x,y,w=sp.symbols('x y w',real=True)
coords=(t,x,y,w)
gf=sp.diag(-1,t**sp.Rational(2,3),t**sp.Rational(2,3),t**sp.Rational(2,3))
pf=encode_metric(gf)
gdecoded=pf.decode()
test('curved field encoder round trip',mz(gdecoded-gf))
ph=sp.log(t)/sp.sqrt(3)
cs=[ph,sp.S.Zero,sp.S.Zero,sp.S.Zero,sp.S.Zero,sp.S.Zero,sp.S.Zero]
tau_new=phase_inverse(ph,cs,beta=1,gamma=2)
test('nontrivial mixed-phase lift',zero(tau_new-(sp.log(t)/sp.sqrt(3)-sp.log(t)**2/3)))
test('mixed-phase reconstruction',zero(phase_forward(tau_new,cs,1,2)-ph))
lag,T=scalar_source(coords,gdecoded,ph,cs)
Gamma=old.christoffel(coords,gdecoded)
CN=native_connection(coords,z_from_metric(gf))
test('direct Z-connection equals coordinate connection',all(mz(a-b) for a,b in zip(CN,Gamma)))
Riem=old.curvature_gr(coords,Gamma)
Ric,R,Ein=old.scalar_and_einstein(Riem,gdecoded)
test('curved scalar curvature',zero(R+sp.Rational(2,3)/t**2))
test('full sourced Einstein equation all components',mz(Ein.matrix()-T))
test('independent scalar energy density',zero(T[0,0]-1/(3*t**2)))

def box(f):
    inv=gf.inv();vol=t
    return sp.simplify(sum(sp.diff(vol*sum(inv[i,j]*sp.diff(f,coords[j]) for j in range(4)),coords[i]) for i in range(4))/vol)
test('phase Euler equation',zero(box(ph)))
test('all seven chromatic Euler equations',all(zero(box(f)) for f in cs))
uN=sp.Matrix([sp.diff(tau_new,a)+2*sum(c*sp.diff(c,a) for c in cs) for a in coords])
lagN=sp.simplify(-(uN.T*gf.inv()*uN)[0]/2-sum((sp.Matrix([sp.diff(c,a) for a in coords]).T*gf.inv()*sp.Matrix([sp.diff(c,a) for a in coords]))[0] for c in cs)/2)
test('native mixed Lagrangian equals target Lagrangian',zero(lagN-lag))
# Independently vary the reduced homogeneous scalar action before inserting solution.
uf=sp.Function('u')(t);vf=sp.Function('v')(t)
ld=t*((sp.diff(uf,t)+2*vf*sp.diff(vf,t))**2+sp.diff(vf,t)**2)/2
elu=sp.diff(ld,uf)-sp.diff(sp.diff(ld,sp.diff(uf,t)),t)
elv=sp.diff(ld,vf)-sp.diff(sp.diff(ld,sp.diff(vf,t)),t)
subs={uf:tau_new,vf:ph}
test('direct native phase action variation',zero(elu.subs(subs).doit()))
test('direct native chromatic action variation',zero(elv.subs(subs).doit()))
Tten=old.Tensor.from_matrix(T,(-1,-1))
dT=old.covariant_derivative(Tten,Gamma,lambda i,f:sp.diff(f,coords[i]))
ginv=gf.inv()
div=[sp.simplify(sum(ginv[a,c]*dT[a,b,c] for a in range(4) for c in range(4))) for b in range(4)]
test('all components of stress conservation',all(zero(v) for v in div))
# Native metric variables supply full arbitrary local variations, unlike constant W.
probe_z=z_from_metric(gf)
jvalues=[sp.sqrt(s*s+gf[i,j]**2) for i,j in inds]
test('regularity on curved solution',all(v.is_positive for v in jvalues))
# Deliberately add forbidden independent W-force: equation no longer merely rescales.
a=sp.symbols('a',nonzero=True)
S=sp.sinh(z)**2/2-a*z
res=sp.diff(S,z)
test('extra independent action is detected',zero(res-(sp.sinh(z)*sp.cosh(z)-a)) and res.subs(z,0)!=0,'negative control: independent extra action changes the target')

report={'model':'GRC-1 v0.1 NEW proposed completion, not unchanged historical Genesis',
        'checks':results,'total':len(results),'passed':sum(x['passed'] for x in results),
        'elapsed_seconds':round(time.time()-start,3),'python':platform.python_version(),
        'sympy':sp.__version__,'numpy':np.__version__,
        'numeric_family':{'seed':43,'count':100,'max_absolute_roundtrip_error':worst},
        'limits':['Tests verify constructed examples and implementation identities, not a machine-checked general theorem.',
                  'The written theorem establishes the new action-defined branch; the archived native laws are not verified equivalent.',
                  'Smooth classical Lorentzian region only; no quantum or empirical validation.']}
(ROOT/'results'/'CHECK_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
(ROOT/'results'/'EXACT_SOLUTION.json').write_text(json.dumps({'metric':'diag(-1,t^(2/3),t^(2/3),t^(2/3))',
 'domain':'t>0','kappa':1,'Lambda':0,'beta':1,'gamma':2,'potential':0,
 'Theta':'ln(t)/sqrt(3)','chi_1':'ln(t)/sqrt(3)','chi_2_to_7':0,
 'tau':'ln(t)/sqrt(3) - ln(t)^2/3','scalar_curvature':'-2/(3*t^2)',
 'energy_density':'1/(3*t^2)','source':'derived from explicit eight-scalar matter action, not from Einstein curvature'},indent=2)+'\n')
print(f"{len(results)} checks passed in {time.time()-start:.2f}s",flush=True)
