"""Reproducible implementation checks, not a proof of native Q_R realizability."""
from __future__ import annotations
from itertools import product
from pathlib import Path
import json,sys,time,platform
import sympy as s
from translator import *

RESULTS=[]
OBSERVATIONS=[]
START=time.perf_counter()

def check(name,condition,detail=''):
    ok=bool(condition)
    RESULTS.append({'name':name,'passed':ok,'detail':detail})
    print(('PASS ' if ok else 'FAIL ')+name,flush=True)
    if not ok: raise AssertionError(name)

def equal_m(a,b):
    return a.shape==b.shape and all(zero(a[i,j]-b[i,j]) for i in range(a.rows) for j in range(a.cols))

def equal_c(a,b):
    return len(a)==len(b) and all(equal_m(x,y) for x,y in zip(a,b))

def rejects(name,fn,exception=ValueError):
    try:fn()
    except exception:check(name,True);return
    check(name,False)


def divergence_cov(tensor,metric,C,derivative):
    d=covariant_derivative(tensor,C,derivative);ki=metric.inv();n=metric.rows
    return Tensor(n,(-1,),{(b,):simp(sum(ki[a,c]*d[a,b,c] for a in range(n) for c in range(n))) for b in range(n)})


def fixture(name,coords,A,k,tupper,domain,expected_scalar=None):
    fr=Frame(tuple(coords),s.ImmutableMatrix(A),tuple(domain))
    C=koszul_native(fr,k)
    g=fr.translate(Tensor.from_matrix(k,(-1,-1))).matrix()
    Gamma=christoffel(coords,g)
    check(name+': selected native connection matches independent GR connection',equal_c(native_connection_to_gr(fr,C),Gamma))
    check(name+': connection inverse',equal_c(gr_connection_to_native(fr,Gamma),C))
    RN=curvature_native(fr,C);RG=curvature_gr(coords,Gamma)
    check(name+': full Riemann commutation',fr.translate(RN).equals(RG))
    rn,scn,en=scalar_and_einstein(RN,k);rg,scg,eg=scalar_and_einstein(RG,g)
    check(name+': Ricci and scalar commutation',fr.translate(rn).equals(rg) and zero(scn-scg))
    if expected_scalar is not None:check(name+': specified scalar curvature',zero(scn-expected_scalar))
    check(name+': Einstein tensor commutation',fr.translate(en).equals(eg))
    u=s.Matrix(s.symbols('u0:4'));w=s.Matrix(s.symbols('w0:4'))
    velocity=fr.A*u
    coord_acc=fr.A*w+sum((velocity[mu]*fr.A.diff(coords[mu])*u for mu in range(4)),s.zeros(4,1))
    coord_acc+=sum((velocity[mu]*Gamma[mu]*velocity for mu in range(4)),s.zeros(4,1))
    native_acc=w+sum((u[a]*C[a]*u for a in range(4)),s.zeros(4,1))
    check(name+': affine geodesic operator commutation',equal_m(coord_acc,fr.A*native_acc))
    if name=='FLRW':
        x=coords[0];a=s.Function('a')(x);kap=s.Symbol('kappa',nonzero=True);lam=s.Symbol('Lambda');rho=s.Function('rho')(x);p=s.Function('p')(x)
        tdown=k*tupper*k.T
        FN=en.add(Tensor.from_matrix(k,(-1,-1)).scale(lam)).add(Tensor.from_matrix(tdown,(-1,-1)).scale(-kap))
        tg=fr.translate(Tensor.from_matrix(tupper,(1,1))).matrix()
        FG=eg.add(Tensor.from_matrix(g,(-1,-1)).scale(lam)).add(Tensor.from_matrix(g*tg*g.T,(-1,-1)).scale(-kap))
        check(name+': full off-shell Einstein-source residual',fr.translate(FN).equals(FG))
        check(name+': independent source gives expected temporal equation',zero(FN[0,0]-(3*(s.diff(a,x)/a)**2-lam-kap*rho)))
        check(name+': independent source gives expected spatial equation',zero(FN[1,1]-(-2*s.diff(a,x,2)/a-(s.diff(a,x)/a)**2+lam-kap*p)))
        divn=divergence_cov(Tensor.from_matrix(tdown,(-1,-1)),k,C,fr.directional)
        divg=divergence_cov(Tensor.from_matrix(g*tg*g.T,(-1,-1)),g,Gamma,lambda i,v:s.diff(v,coords[i]))
        check(name+': source divergence commutation',fr.translate(divn).equals(divg))
        check(name+': off-shell continuity residual',zero(divn[0]+s.diff(rho,x)+3*s.diff(a,x)/a*(rho+p)))
        OBSERVATIONS.append({'name':'FLRW residual expressions','detail':{'F00':str(FN[0,0]),'F11':str(FN[1,1]),'div_cov0':str(divn[0]),'source_status':'rho and p are independent; no equation of state imposed'}})
    # Generic nonconstant vector makes derivative-of-frame terms observable.
    v=Tensor(fr.n,(1,),{(i,):coords[i]**2+coords[(i+1)%fr.n] for i in range(fr.n)})
    dvn=covariant_derivative(v,C,fr.directional)
    vg=fr.translate(v)
    dvg=covariant_derivative(vg,Gamma,lambda i,f:s.diff(f,coords[i]))
    check(name+': covariant derivative of vector',fr.translate(dvn).equals(dvg))
    # Operate twice, to test the composition mechanism on a genuine differential word.
    if name=='Sheared flat':
        d2n=covariant_derivative(dvn,C,fr.directional)
        d2g=covariant_derivative(dvg,Gamma,lambda i,f:s.diff(f,coords[i]))
        check(name+': composed covariant derivatives',fr.translate(d2n).equals(d2g))
    N=s.ImmutableMatrix([[1,1,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    kap=s.Symbol('kappa',nonzero=True);lam=s.Symbol('Lambda')
    native=EvaluatedGenesisEndpoint(fr,s.ImmutableMatrix(k),C,N,mat_simp(tupper*N),lam,kap,
                                    (('matter_and_boundary','opaque retained fields; not inferred from T'),))
    target=native.to_gr();back=target.to_genesis_endpoint()
    check(name+': Genesis endpoint round trip',equal_m(back.metric,k) and equal_m(back.probe_flux,native.probe_flux)
          and equal_c(back.selected_connection,C) and back.retained_data==native.retained_data
          and back.coupling==kap and back.cosmological_constant==lam)
    target2=back.to_gr()
    check(name+': GR endpoint round trip',equal_m(target2.metric,target.metric) and equal_m(target2.source_upper,target.source_upper))
    return fr,C,RN


def main():
    t,x,y,z=s.symbols('t x y z',real=True);coords=(t,x,y,z);eta=s.diag(-1,1,1,1)
    anchor=s.ImmutableMatrix([[1,x,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    frame,C,R=fixture('Sheared flat',coords,anchor,anchor.T*eta*anchor,s.diag(2,3,5,7),['all real coordinates; det A=1; Lorentzian by congruence'],s.S.Zero)
    # Wrong connection transformation, omitting dA, must not pass.
    B=frame.B
    wrong=tuple(mat_simp(anchor*sum((B[a,mu]*C[a] for a in range(4)),s.zeros(4))*B) for mu in range(4))
    correct=christoffel(coords,eta)
    check('Negative control: omitting derivative-of-frame is detected',not equal_c(wrong,correct))
    bad=list(C);bad[0]=mat_simp(bad[0]+s.eye(4))
    rejects('Negative control: reject incompatible selected connection',lambda:validate_selected_connection(frame,anchor.T*eta*anchor,bad))
    r=s.symbols('r',positive=True); spherecoords=(t,x,y,z)
    frame2,C2,R2=fixture('Curved product',spherecoords,s.diag(1,1,1/s.sin(x),1),eta,s.diag(2,0,0,-2),
                        ['0<x<pi; oriented local chart; Lorentzian metric'],s.Integer(2))
    # Direct transport ODE on a latitude segment, starting at y=0, x fixed.
    P=s.eye(4); angle=y*s.cos(x)
    P[1,1]=P[2,2]=s.cos(angle);P[1,2]=s.sin(angle);P[2,1]=-s.sin(angle)
    P=s.ImmutableMatrix(P)
    Cmu=sum((frame2.B[a,2]*C2[a] for a in range(4)),s.zeros(4))
    check('Curved product: native transport ODE',equal_m(P.diff(y)+Cmu*P,s.zeros(4)))
    G=christoffel(coords,s.diag(-1,1,s.sin(x)**2,1))
    Pg=mat_simp(frame2.A*P*frame2.B)
    check('Curved product: translated transport ODE',equal_m(Pg.diff(y)+G[2]*Pg,s.zeros(4)))
    check('Curved product: transport round trip',equal_m(frame2.B*Pg*frame2.A,P))
    check('Curved product: reversed-path inverse',equal_m(P.subs(y,-y)*P,s.eye(4)))
    # Detect the omitted non-coordinate-frame bracket contribution.
    C2naive=[]
    missing={}
    for a,b in product(range(4),repeat=2):
        mm=s.Matrix(4,4,lambda c,d:frame2.directional(a,C2[b][c,d])-frame2.directional(b,C2[a][c,d]))+C2[a]*C2[b]-C2[b]*C2[a]
        for c,d in product(range(4),repeat=2):missing[c,d,a,b]=simp(mm[c,d])
    check('Negative control: missing frame bracket changes curvature',not Tensor(4,(1,-1,-1,-1),missing).equals(R2))
    a=s.Function('a')(t);rho=s.Function('rho')(t);p=s.Function('p')(t)
    fixture('FLRW',coords,s.diag(1,1/a,1/a,1/a),eta,s.diag(rho,p,p,p),
            ['a(t)>0 smooth; fixed oriented chart; rho(t), p(t) arbitrary smooth functions'],
            6*(s.diff(a,t,2)/a+(s.diff(a,t)/a)**2))
    # General mixed-variance algebra tests with a rational invertible anchor.
    fr=Frame(coords,s.ImmutableMatrix([[1,1,0,0],[0,2,1,0],[0,0,3,1],[0,0,0,1]]),('constant invertible frame',))
    nround=0
    for rank in range(4):
        for variance in product((1,-1),repeat=rank):
            q=Tensor(4,tuple(variance),{idx:s.Integer(sum((i+1)*v for i,v in enumerate(idx))+1)
                                     for idx in product(range(4),repeat=rank)})
            assert fr.translate(fr.translate(q),to_gr=False).equals(q)
            nround+=1
    check('Mixed-variance round trips',True,f'{nround} variance types, ranks zero through three')
    v=Tensor(4,(1,),{(i,):s.Integer(i+1) for i in range(4)})
    w=Tensor(4,(-1,),{(i,):s.Integer(4-i) for i in range(4)})
    check('Tensor product preservation',fr.translate(v.product(w)).equals(fr.translate(v).product(fr.translate(w))))
    check('Contraction preservation',fr.translate(v.product(w).contract(0,1)).equals(fr.translate(v).product(fr.translate(w)).contract(0,1)))
    rejects('Negative control: illegal same-variance contraction',lambda:v.product(v).contract(0,1))
    rejects('Negative control: singular anchor',lambda:Frame(coords,s.ImmutableMatrix(s.diag(1,1,1,0)),('all points',)))
    rejects('Negative control: degenerate metric',lambda:koszul_native(fr,s.diag(-1,1,1,0)))
    rejects('Negative control: deficient flux probes',lambda:flux_to_source(s.diag(1,1,1,0),s.eye(4)))
    rejects('Negative control: asymmetric non-spin source',lambda:flux_to_source(s.eye(4),s.Matrix([[1,1,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])))
    rejects('Native attachment is not fabricated',lambda:attach_raw_native_state({'R':'unspecified','B':'unspecified'}),UnresolvedNativeAttachment)
    # Small-loop sign and non-coordinate integral conventions remain proof-scoped,
    # not automatically inferred from this component test suite.

if __name__=='__main__':
    output=Path(__file__).resolve().parent.parent/'results'/'CHECK_RESULTS.json'
    try:
        main();status='PASS'
    except Exception as exc:
        status='FAIL';RESULTS.append({'name':'exception','passed':False,'detail':repr(exc)})
        raise
    finally:
        output.write_text(json.dumps({'status':locals().get('status','ERROR'),'tests':RESULTS,'named_checks':len(RESULTS),
                                      'passed':sum(r['passed'] for r in RESULTS),'observations':OBSERVATIONS,'elapsed_seconds':time.perf_counter()-START,
                                      'python':platform.python_version(),'sympy':s.__version__,
                                      'scope':'Exact local symbolic tests on constructed evaluated smooth fields. No Q_R-native state, history inverse, global PDE existence, or empirical validation.'},indent=2))
