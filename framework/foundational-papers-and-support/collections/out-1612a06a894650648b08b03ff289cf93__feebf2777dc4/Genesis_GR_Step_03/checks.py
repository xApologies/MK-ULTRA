"""Independent checks of Step 03 representation identities.

These exercise constructed smooth examples, not the unspecified native Q_R,
Time-Shell operator, native self-coupling, or empirical predictions.
Run: python checks.py. Requires sympy; does not execute uploaded source code.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as s

OUT=Path(__file__).resolve().parent
RESULTS=[]

def check(name, ok, detail):
    ok=bool(ok)
    RESULTS.append({'name':name,'passed':ok,'scope':detail})
    if not ok:
        raise AssertionError(name)

def zero(value):
    if isinstance(value,s.MatrixBase):
        return all(s.simplify(x)==0 for x in value)
    if isinstance(value,(list,tuple)):
        return all(zero(x) for x in value)
    return s.simplify(value)==0

t,x,y,z=s.symbols('t x y z',real=True)
coords=[t,x,y,z]; n=4
a=s.Function('a',positive=True)(t)
g=s.diag(-1,a*a,a*a,a*a); gi=g.inv()
Gamma=[[[s.simplify(sum(gi[r,l]*(s.diff(g[l,b],coords[c])+s.diff(g[l,c],coords[b])-s.diff(g[b,c],coords[l])) for l in range(n))/2) for c in range(n)] for b in range(n)] for r in range(n)]
Gm=[s.Matrix(n,n,lambda r,b:Gamma[r][mu][b]) for mu in range(n)]
Omega={}
for mu in range(n):
 for nu in range(n):
  Omega[mu,nu]=(Gm[nu].diff(coords[mu])-Gm[mu].diff(coords[nu])+Gm[mu]*Gm[nu]-Gm[nu]*Gm[mu]).applyfunc(s.simplify)
Ric=s.Matrix(n,n,lambda b,d:s.simplify(sum(Omega[k,d][k,b] for k in range(n))))
R=s.simplify(s.trace(gi*Ric)); E=(Ric-R*g/2).applyfunc(s.simplify)
h=s.diff(a,t)/a
Ric_expected=s.diag(-3*s.diff(a,t,2)/a,*([a*s.diff(a,t,2)+2*s.diff(a,t)**2]*3))
E_expected=s.diag(3*h*h,*([-2*a*s.diff(a,t,2)-s.diff(a,t)**2]*3))
check('FLRW Ricci computed from Christoffel symbols',zero(Ric-Ric_expected),'Full nonlinear spatially flat FLRW ansatz; arbitrary smooth nonzero a(t).')
check('FLRW scalar curvature',zero(R-6*(s.diff(a,t,2)/a+h*h)),'No perturbative expansion.')
check('FLRW Einstein tensor',zero(E-E_expected),'Computed from Ricci and scalar contraction.')
# A maps components in a non-coordinate orthonormal frame to coordinate components.
A=s.diag(1,1/a,1/a,1/a); B=A.inv(); eta=s.diag(-1,1,1,1)
gG=(A.T*g*A).applyfunc(s.simplify)
check('Metric round trip',zero(B.T*gG*B-g) and zero(gG-eta),'Smooth invertible moving-frame realization; not native Q_R reconstruction.')
CG=[(B*Gm[mu]*A+B*A.diff(coords[mu])).applyfunc(s.simplify) for mu in range(n)]
check('Connection includes derivative of frame',zero(CG[0]) and not zero(B*Gm[0]*A),'Connection transforms inhomogeneously; omitting A inverse dA is not correct.')
check('Connection metric compatibility',all(zero(gG.diff(coords[mu])-CG[mu].T*gG-gG*CG[mu]) for mu in range(n)),'Covariant derivative along coordinate direction, in native frame indices.')
OmegaG={}
for mu in range(n):
 for nu in range(n):
  OmegaG[mu,nu]=(CG[nu].diff(coords[mu])-CG[mu].diff(coords[nu])+CG[mu]*CG[nu]-CG[nu]*CG[mu]).applyfunc(s.simplify)
check('All curvature matrix transformations',all(zero(OmegaG[k]-B*Omega[k]*A) for k in Omega),'All 16 ordered coordinate-direction pairs in moving frame.')
# Contract in frame directions: R^a_bcd = A^mu_c A^nu_d OmegaG_mu,nu[a,b].
RicG=s.Matrix(n,n,lambda b,d:s.simplify(sum(A[mu,k]*A[nu,d]*OmegaG[mu,nu][k,b] for k in range(n) for mu in range(n) for nu in range(n))))
check('Ricci transformation after contraction',zero(RicG-A.T*Ric*A),'Full native-frame directional conversion before contraction.')
RG=s.simplify(s.trace(gG.inv()*RicG)); EG=(RicG-RG*gG/2).applyfunc(s.simplify)
check('Scalar is invariant',zero(RG-R),'Inverse metric and Ricci transform consistently.')
check('Einstein tensor naturality',zero(EG-A.T*E*A),'Full nonlinear moving-frame calculation.')
rho,p=s.Function('rho')(t),s.Function('p')(t)
T=s.diag(rho,p*a*a,p*a*a,p*a*a)
TG=(A.T*T*A).applyfunc(s.simplify)
Lam,kappa=s.symbols('Lambda kappa',real=True,nonzero=True)
F=E+Lam*g-kappa*T; FG=EG+Lam*gG-kappa*TG
check('Full gravitational field residual round trip',zero(FG-A.T*F*A) and zero(B.T*FG*B-F),'Includes independent symbolic source, Lambda and coupling; not solved by defining T from curvature.')
check('Source tensor round trip',zero(TG-s.diag(rho,p,p,p)) and zero(B.T*TG*B-T),'Energy and stresses are preserved by the tensor readout.')
# Contravariant divergence computed directly, including both connection terms.
def div_contra(S):
 return [s.simplify(sum(s.diff(S[mu,nu],coords[mu])+sum(Gamma[mu][mu][lam]*S[lam,nu]+Gamma[nu][mu][lam]*S[mu,lam] for lam in range(n)) for mu in range(n))) for nu in range(n)]
check('Contracted Bianchi in nonlinear ansatz',zero(div_contra(gi*E*gi)),'Off-shell a(t) is arbitrary.')
D=div_contra(gi*T*gi)
check('Perfect-fluid covariant conservation',zero(D[0]-(s.diff(rho,t)+3*h*(rho+p))) and zero(D[1:]),'Energy condition is rho prime + 3 H (rho+p)=0, not ordinary constant cell energy.')
pressure_res=s.simplify(s.diff(a**3*rho,t)+p*s.diff(a**3,t)-a**3*D[0])
check('Pressure-work balance',zero(pressure_res),'d(a^3 rho)/dt + p d(a^3)/dt = a^3 div(T)^0.')
# A pointwise/first-jet readout is not curvature-complete.
k=s.symbols('k',real=True,nonzero=True); ac=1+k*t*t
Rcurved=s.simplify(R.subs({s.diff(a,t,2):s.diff(ac,t,2),s.diff(a,t):s.diff(ac,t),a:ac}))
check('Same metric and first derivatives need not have same curvature',zero(ac.subs(t,0)-1) and zero(s.diff(ac,t).subs(t,0)) and zero(Rcurved.subs(t,0)-12*k),'Minkowski a=1 vs a=1+k t^2 at t=0; local positive a. This is a counterexample to arbitrary coarse readout, not to supplied Q_R.')
# A quotient evaluation map that is multiplicative need not commute with d/dt.
check('Algebraic quotient need not admit derivative descent',(t.subs(t,0)==0) and (s.diff(t,t).subs(t,0)==1),'Ideal of functions vanishing at 0 is not derivative-stable.')
# de Sitter specialization is an independent exact vacuum-with-Lambda check.
H=s.symbols('H',real=True,nonzero=True); ae=s.exp(H*t)
Eds=E.subs({s.diff(a,t,2):s.diff(ae,t,2),s.diff(a,t):s.diff(ae,t),a:ae}).applyfunc(s.simplify)
gds=g.subs(a,ae)
check('de Sitter vacuum with Lambda',zero(Eds+3*H**2*gds),'Constructed exact solution with Lambda=3 H^2, c=1.')
# Null planes need parameter-area rather than division by metric area.
u=s.Matrix([1,1,0,0]); v=s.Matrix([0,0,1,0]); gram=s.Matrix([[(u.T*eta*u)[0],(u.T*eta*v)[0]],[(v.T*eta*u)[0],(v.T*eta*v)[0]]])
check('Null two-plane can have zero metric area with independent tangents',gram.det()==0 and s.Matrix.hstack(u,v).rank()==2,'Reason to use signed parameter bivector in the small-loop limit.')
# Arbitrary tensor inverse, not restricted to isotropic diagonal examples.
A2=s.Matrix([[1,1,0,0],[0,2,1,0],[0,0,3,1],[0,0,0,4]])
b2=A2.inv(); syms=s.symbols('s0:10'); S=s.zeros(4); jj=0
for i in range(4):
 for j in range(i,4): S[i,j]=S[j,i]=syms[jj]; jj+=1
check('Generic symmetric tensor inverse',zero(b2.T*(A2.T*S*A2)*b2-S),'All ten independent components in a non-diagonal invertible frame.')
report={'sympy_version':s.__version__,'passed':sum(x['passed'] for x in RESULTS),'total':len(RESULTS),'checks':RESULTS,'limitations':'Constructed classical tensor examples and algebraic counterexamples only. No native metric-generator, native self-coupling, Time-Shell implementation, global native lift, full matter model, or empirical predictions were tested.'}
(OUT/'CHECK_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':report['passed'],'total':report['total'],'sympy_version':s.__version__},indent=2))
