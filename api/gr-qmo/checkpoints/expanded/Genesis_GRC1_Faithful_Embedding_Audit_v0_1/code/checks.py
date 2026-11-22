"""Exact checks of the old-to-GRC-1 embedding comparison.

FAILURE witnesses are expected successful checks, not validations of embedding.
The graph fixtures satisfy inspected interface laws, not every microscopic equation.
The field-space obstruction specializes the displayed action to G^{ab}=delta^{ab}.
"""
from __future__ import annotations
from pathlib import Path
import json, time, platform
import sympy as s
from field_space_geometry import geometry_from_jets, model_jets
import grc1_reference as grc
import gr_geometry_reference as geo

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
records=[]
def zero(x):
    x=s.simplify(x)
    return x==0 or (x.has(s.sinh,s.cosh) and s.simplify(x.rewrite(s.exp))==0)
def mz(m):return all(zero(x) for x in m)
def record(name,condition,scope):
    condition=bool(condition)
    records.append({'name':name,'passed':condition,'scope':scope})
    print(('PASS ' if condition else 'FAIL ')+name,flush=True)
    if not condition:raise AssertionError(name)

def laplacian(W):return s.diag(*[sum(W.row(i)) for i in range(W.rows)])-W

# 1. Explicit canonical readout is regular, but cannot undo an input collision.
g=s.diag(-1,1,1,1)
pair=grc.encode_metric(g)
record('GRC1 encoder preserves decoded Minkowski metric',mz(pair.decode()-g),'representation identity')
record('GRC1 flat reference is not original identity adjacency',pair.network()!=s.eye(8),'different encoding, not a physical no-go')
r=s.symbols('r',real=True)
record('canonical encoder has no vanishing scalar derivative',zero(s.diff(s.asinh(r),r)-1/s.sqrt(1+r*r)),'regular readout transfer')

Xi=s.eye(4).row_join(s.Matrix([1,0,0,0]))
v=s.Matrix([-1,0,0,0,1])
K=v*v.T
W1=2*s.eye(5)+s.ones(5)
W2=W1+K/2
lam=s.Rational(1,10)
background=g-lam*Xi*W1*Xi.T
record('same fixed ER covectors annihilate ambiguity',mz(Xi*K*Xi.T),'source metric-interface fixture')
record('both networks strictly entrywise positive',all(x>0 for W in (W1,W2) for x in W),'source weight admissibility only')
record('networks distinct and symmetric',W1!=W2 and W1==W1.T and W2==W2.T,'source weight-interface fixture')
g1=background+lam*Xi*W1*Xi.T
g2=background+lam*Xi*W2*Xi.T
record('both readouts are the same Lorentzian metric',mz(g1-g) and mz(g2-g),'fixed-background metric fixture, not full solutions')
p1,p2=grc.encode_metric(g1),grc.encode_metric(g2)
record('canonical GRC1 encoding preserves collision',mz(p1.P-p2.P) and mz(p1.Q-p2.Q),'proves re-encoding cannot recover these two networks')
L1,L2=laplacian(W1),laplacian(W2)
record('original graph spectra differ',L1.eigenvals()=={s.S.Zero:1,s.S(5):4} and L2.eigenvals()=={s.S.Zero:1,s.S(4):1,s.S(5):3},'exact source graph operators')
# A stable spectral branch for both networks; n denotes recursive depth, not time.
v0=s.Matrix([1,0,0,0,0]); cA2=s.Rational(1,2)
next1=(2*s.eye(5)-cA2*L1)*v0-v0
next2=(2*s.eye(5)-cA2*L2)*v0-v0
record('same initial amplitude has different next native update',next1!=next2,'source recurrence, no identification of recursive depth with physical time')
R=s.eye(4).col_join(s.zeros(1,4))
auxiliary_ok=True
for W in (W1,W2):
    readout=Xi*W*Xi.T
    missing=W-R*readout*R.T
    auxiliary_ok=auxiliary_ok and mz(Xi*missing*Xi.T) and mz(R*readout*R.T+missing-W)
record('complementary kernel record restores each full network',auxiliary_ok,'exact decoder with additional kernel data; not GRC1 alone')

# 2. Source action specialization vs completed GRC1 matter.
beta=s.symbols('beta',positive=True)
gamma=s.symbols('gamma',real=True,nonzero=True)
chi=s.Matrix(s.symbols('c0:7',real=True)); n=7
r2=(chi.T*chi)[0]; a=gamma**2/beta
Kold=s.diag(beta,*([1]*7))
for i in range(7):Kold[0,i+1]=Kold[i+1,0]=gamma*chi[i]
Knew=grc.field_space_metric(list(chi),beta,gamma)
expected=s.zeros(8); expected[1:,1:]=a*chi*chi.T
record('new completion changes kinetic metric by rank-one term',mz(Knew-Kold-expected),'source-derived specialization vs exact new model')
J=s.eye(8)
for i in range(7):J[0,i+1]=gamma*chi[i]/beta
record('GRC1 kinetic metric is flat-metric pullback',mz(Knew-J.T*s.diag(beta,*([1]*7))*J),'all seven fields; flatness follows by explicit diffeomorphism')
Jinv=J.inv()
reduced=s.diag(beta,*([1]*7));reduced[1:,1:]-=a*chi*chi.T
record('original phase shift leaves a nontrivial transverse metric',mz(Jinv.T*Kold*Jinv-reduced),'same scalar map does not flatten original action')
record('old determinant and positivity threshold',zero(Kold.det(method='domain-ge')-(beta-gamma**2*r2)),'eight-dimensional original kinetic matrix')
record('completed determinant never degenerates',zero(Knew.det(method='domain-ge')-beta),'new completion comparison')

origin_old=geometry_from_jets(*model_jets([0]*7,beta,gamma,False))
origin_new=geometry_from_jets(*model_jets([0]*7,beta,gamma,True))
record('original eight-field curvature at origin',zero(origin_old['scalar']+42*gamma**2/beta),'exact full 8D metric jets; not a 2D slice argument')
record('original sectional curvature at origin',zero(origin_old['R'][1,2,1,2]+gamma**2/beta),'chosen distinct chromatic directions')
record('completed full Riemann tensor vanishes at origin',not origin_new['R'],'exact full 8D metric jets')
for num,chs,b,ga in [(2,[s.Rational(1,4),s.Rational(1,5)],s.S(2),s.S(3)),(7,[s.Rational(1,4)]+[0]*6,s.S(2),s.S(3))]:
    old=geometry_from_jets(*model_jets(chs,b,ga,False))
    new=geometry_from_jets(*model_jets(chs,b,ga,True))
    aval=ga**2/b; rval=sum(x*x for x in chs)
    prediction=-aval*(num-1)*(num-(num-2)*aval*rval)/(1-aval*rval)**2
    record(f'original full curvature agrees with radial formula n={num}',zero(old['scalar']-prediction),'independent exact jets at a nonzero interior point')
    record(f'GRC1 Riemann vanishes at nonzero point n={num}',not new['R'],'exact local comparison')
record('one-chromatic-field special case has no curvature obstruction',not geometry_from_jets(*model_jets([s.Rational(1,4)],s.S(2),s.S(3),False))['R'],'negative control prevents overgeneralization to one scalar')
record('zero coupling removes this kinetic discrepancy',mz((Knew-Kold).subs(gamma,0)),'conditional agreement, not a full microscopic embedding')

# A target on-shell fixture is not on shell for the original displayed scalar sector.
t=s.symbols('t',positive=True);x,y,z=s.symbols('x y z',real=True);coords=(t,x,y,z)
gf=s.diag(-1,t**s.Rational(2,3),t**s.Rational(2,3),t**s.Rational(2,3))
theta=s.log(t)/s.sqrt(3);c=theta;tau=theta-c*c
u=s.Matrix([s.diff(tau,v) for v in coords]);vc=s.Matrix([s.diff(c,v) for v in coords])
kin_old=u*u.T+vc*vc.T+2*c*(u*vc.T+vc*u.T)
lag_old=s.simplify(-s.trace(gf.inv()*kin_old)/2)
Told=s.simplify(kin_old+gf*lag_old)
lag_new,Tnew=grc.scalar_source(coords,gf,theta,[c],1)
Gamma=geo.christoffel(coords,gf);RR=geo.curvature_gr(coords,Gamma)
Ric,Scal,Ein=geo.scalar_and_einstein(RR,gf)
record('curved fixture solves GRC1 Einstein equations',mz(Ein.matrix()-Tnew),'complete GRC1 metric/scalar fixture, no old ER claim')
source_diff=s.Rational(2,9)*s.log(t)**2/t**2
record('same inverse fixture fails old Einstein-source equation',zero((Ein.matrix()-Told)[0,0]-source_diff) and source_diff!=0,'old displayed scalar action only; explicit ER action not specified')
record('spatial stress discrepancy matches completed-square term',all(zero((Tnew-Told)[i,i]-gf[i,i]*source_diff) for i in (1,2,3)),'action-derived tensor comparison')
uf=s.Function('u')(t);vf=s.Function('v')(t)
Lold_h=t*(s.diff(uf,t)**2+s.diff(vf,t)**2+4*vf*s.diff(uf,t)*s.diff(vf,t))/2
Lnew_h=Lold_h+2*t*vf**2*s.diff(vf,t)**2
el=lambda lag,f:s.diff(lag,f)-s.diff(s.diff(lag,s.diff(f,t)),t)
subs={uf:tau,vf:c}
eold_chi=s.simplify(el(Lold_h,vf).subs(subs).doit()/t)
enew_chi=s.simplify(el(Lnew_h,vf).subs(subs).doit()/t)
eold_tau=s.simplify(el(Lold_h,uf).subs(subs).doit()/t)
record('GRC1 mixed scalar equation vanishes independently',zero(enew_chi),'direct homogeneous action variation')
record('old scalar residual is nonzero exact expression',zero(eold_chi-4*s.log(t)/(3*s.sqrt(3)*t**2)) and eold_chi!=0,'source specialization under proposed direct inverse')
record('phase equation still agrees on this fixture',zero(eold_tau),'difference localized to chromatic and stress sectors')

# Matter-preserving alternative: no altered kinetic action is necessary for gravity encoding.
zz,ell=s.symbols('zz ell',real=True)
Jg=s.cosh(zz)
record('same old matter can be retained by regular metric reexpression',zero(s.diff(ell*s.sinh(zz),zz)-ell*Jg),'algebraic chain rule; not completion of unresolved original microphysics')

report={
 'task':'Original microscopic Genesis -> unchanged GRC-1 faithful embedding audit',
 'determination':'NOT_ESTABLISHED; canonical coarse metric map nonfaithful on tested interface; regular same-metric scalar point-map obstruction for stated source-action specialization',
 'total':len(records),'passed':sum(r['passed'] for r in records),'checks':records,
 'python':platform.python_version(),'sympy':s.__version__,'elapsed_seconds':round(time.perf_counter()-START,3),
 'new_invariant':{'n_chromatic':7,'old_scalar_curvature_at_origin':'-42 gamma^2/beta','GRC1_scalar_curvature':'0','hypotheses':'constant chromatic coefficient identity, beta>0, gamma!=0, no compensating additional kinetic action, same spacetime metric, regular derivative-free scalar redefinition'},
 'graph_witness':{'spectra_1':{'0':1,'5':4},'spectra_2':{'0':1,'4':1,'5':3},'scope':'source formula and recurrence fixture, not complete native on-shell states'},
 'limits':['No full microscopic solution-space construction or classification performed.',
           'Curvature obstruction excludes the stated class of local action-preserving scalar identifications, not all possible derivative/nonlocal embeddings.',
           'G^{ab}=identity is an explicit specialization, not a recovered unique global field-space law.',
           'Additional original sectors could change total kinetic geometry; none is assumed to cancel the discrepancy.',
           'Passing tests includes detecting negative witnesses; it does not certify the requested embedding.']}
(ROOT/'results/CHECK_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print(f"{len(records)} checks passed in {report['elapsed_seconds']} s",flush=True)
