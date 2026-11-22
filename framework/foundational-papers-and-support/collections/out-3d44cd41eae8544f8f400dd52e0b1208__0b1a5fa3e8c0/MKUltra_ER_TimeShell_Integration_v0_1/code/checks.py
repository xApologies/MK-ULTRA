from pathlib import Path
import sys,json,time,platform
import numpy as np
import sympy as s
from scipy.integrate import quad
from er_shell import *
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,condition,scope,detail=None):
    ok=bool(condition)
    checks.append(dict(name=name,passed=ok,scope=scope,detail=detail))
    if not ok: raise AssertionError(name)
def matzero(m):return all(s.simplify(x)==0 for x in m)
def rejected(f):
    try:f()
    except ValueError:return True
    return False
start=time.time()
w=np.array([[1,1,0],[1,1,1],[0,1,1]],float)
l=laplacian(w);a=.5*l
check('Laplacian_row_sum',np.allclose(l@np.ones(3),0),'recovered graph operator')
check('Laplacian_nonnegative',np.linalg.eigvalsh(l).min()>-1e-12,'finite fixture')
check('reject_negative_weights',rejected(lambda:laplacian(np.array([[0,-1],[-1,0]]))),'negative control')
check('self_loops_cancel_only_in_L',np.allclose(l,laplacian(w+7*np.eye(3))),'not a license to discard loops from metric data')
# Source recurrence is exactly stationary for the proposed quadratic discrete action.
xm,x,xp,aa,j=s.symbols('xm x xp aa j')
lf=.5*(xp-x)**2-s.Rational(1,2)*aa*x*x+j*x
lp=.5*(x-xm)**2-s.Rational(1,2)*aa*xm*xm
el=s.diff(lf,x)+s.diff(lp,x)
check('quadratic_discrete_variation',s.simplify(el+(xp-2*x+xm+aa*x-j))==0,'direct variation')
M=s.Matrix.vstack(s.Matrix.hstack(2*s.eye(3)-s.Matrix(a),-s.eye(3)),s.Matrix.hstack(s.eye(3),s.zeros(3)))
J=s.Matrix.vstack(s.Matrix.hstack(s.zeros(3),s.eye(3)),s.Matrix.hstack(-s.eye(3),s.zeros(3)))
check('fixed_recurrence_symplectic',matzero(M.T*J*M-J),'linear phase-space map, not quantum norm')
rng=np.random.default_rng(43)
h0=np.array([.3,-.1,.2]);h1=np.array([.31,-.07,.18])
f=full_trajectory(w,h0,h1,80,c2=.5)
e=native_invariant(f,w,.5)
check('fixed_native_invariant',np.max(np.abs(e-e[0]))<2e-13,'unforced fixed-weight invariant',float(np.max(np.abs(e-e[0]))))
check('strict_oscillatory_bound',np.max(np.linalg.eigvalsh(a))<4,'positive nonzero modes bounded; zero mode may drift')
for n in [3,5,8]:
    v=rng.random((n,n));v=(v+v.T)/2;np.fill_diagonal(v,1)
    c2=.7/max(np.diag(laplacian(v)))
    b0=rng.normal(size=n);b1=rng.normal(size=n)
    forcing=rng.normal(size=(31,n))*.01
    full=full_trajectory(v,b0,b1,30,c2,forcing)
    y,rec,g=reduced_trajectory(v,[0,n-1],b0,b1,30,c2,forcing)
    err=float(np.max(np.abs(full-rec)))
    check(f'exact_memory_forced_N{n}',err<2e-10,'causal elimination plus hidden initial data',err)
# algebraic block inverse / low-frequency expansion
L=s.Matrix([[1,-1,0],[-1,2,-1],[0,-1,1]])
A=L/2;ss=[0,2];ii=[1];z=s.symbols('z')
Ass=A.extract(ss,ss);Asi=A.extract(ss,ii);Aii=A.extract(ii,ii)
Ds=Ass-z*s.eye(2)-Asi*(Aii-z*s.eye(1)).inv()*Asi.T
fullinv=(A-z*s.eye(3)).inv()
check('Schur_response_block_inverse',matzero(fullinv.extract(ss,ss)-Ds.inv()),'resolvent away from singular inverses')
check('Schur_determinant_factor',s.simplify((A-z*s.eye(3)).det()-(Aii-z*s.eye(1)).det()*Ds.det())==0,'algebraic characteristic factorization')
Lk=L.extract(ss,ss)-L.extract(ss,ii)*L.extract(ii,ii).inv()*L.extract(ii,ss)
check('static_Kron_row_sum',matzero(Lk*s.ones(2,1)),'no added constant restoring term; not spin-2 proof')
Meff=s.eye(2)+Asi*Aii.inv()**2*Asi.T
check('low_frequency_inertia',matzero(Ds.diff(z).subs(z,0)+Meff),'derived first-order frequency coefficient')
check('induced_inertia_positive',np.linalg.eigvalsh(np.array(Meff,float)).min()>0,'finite fixture of proved positive form')
zz=.05
rem=np.array((Ds-(Ass-Asi*Aii.inv()*Asi.T)+z*Meff).subs(z,zz),float)
amin=float(Aii[0]);bound=zz**2*np.linalg.norm(np.array(Asi,float),2)**2/(amin**3*(1-zz/amin))
check('remainder_norm_bound',np.linalg.norm(rem,2)<=bound+1e-13,'Neumann-series controlled approximation')
# no memoryless second-order boundary dynamics under arbitrary hidden initial states
zero=np.zeros(3);hidden=np.array([0,1,0.])
f0=full_trajectory(w,zero,zero,2,.5);f1=full_trajectory(w,zero,hidden,2,.5)
check('same_shell_pair_different_successor',np.allclose(f0[:2][:,[0,2]],f1[:2][:,[0,2]]) and not np.allclose(f0[2,[0,2]],f1[2,[0,2]]),'counterexample for instantaneous boundary-state closure')
o,m,c=observation_matrix(w,[0],.5)
check('endpoint_observability_rank6',np.linalg.matrix_rank(o)==6,'three-node path, observing endpoint')
fr=full_trajectory(w,h0,h1,6,.5)
dec=decode_observed_initial(w,[0],fr[1:7,0],.5)
check('history_inverse_recovers_full_state',np.allclose(dec,np.r_[h1,h0],atol=2e-12),'observed-history inverse without separate hidden initial data')
oc,mc,cc=observation_matrix(w,[1],.5)
check('center_observability_rank4',np.linalg.matrix_rank(oc)==4,'two unobservable phase-space directions')
v=np.array([1,0,-1.]);fd=full_trajectory(w,v,2*v,20,.5)
check('dark_mode_zero_shell_history',np.max(np.abs(fd[:,1]))==0,'nonzero native motion invisible to center port')
check('reject_false_inverse_dark_mode',rejected(lambda:decode_observed_initial(w,[1],fd[1:7,1],.5)),'negative control')
# changing foam: exact two-time memory for an explicitly retained graph history
ws=[]
for t in range(25):
    ww=w.copy();ww[0,1]=ww[1,0]=.6+.1*np.sin(t/4)
    ww[1,2]=ww[2,1]=.9+.1*np.cos(t/3);ws.append(ww)
y=time_varying_reduction(ws,[0,2],h0,h1,.3)
fu=np.zeros((25,3));fu[:2]=[h0,h1]
for t in range(1,24):fu[t+1]=(2*np.eye(3)-.3*laplacian(ws[t]))@fu[t]-fu[t-1]
check('ordered_memory_changing_foam',np.allclose(y,fu[:,[0,2]],atol=2e-12),'conditional on retained changing W history')
check('changing_L_not_generically_commuting',not np.allclose(laplacian(ws[0])@laplacian(ws[1]),laplacian(ws[1])@laplacian(ws[0])),'mode-mixing warning')
# Boundary scalar kernel: analytic and numeric.
p,k,spacing=s.symbols('p k a',positive=True)
integral=s.integrate(1/(k*k+p*p),(k,-s.oo,s.oo))/(2*s.pi)
check('continuum_boundary_trace',s.simplify(integral-1/(2*p))==0,'scalar coefficient only, not full tensor projector')
G=s.symbols('G',positive=True)
check('archived_scalar_prefactor_match',s.simplify(8*s.pi*G*integral-4*s.pi*G/p)==0,'normalization choice 8 pi G, Euclidean/spacelike branch')
for av,pv in [(1.,.7),(.1,1.),(.025,2.)]:
    val=quad(lambda q:1/(pv*pv+4/av**2*np.sin(q/2)**2),-np.pi,np.pi,epsabs=1e-10)[0]/(2*np.pi*av)
    expected=1/(pv*np.sqrt(4+av*av*pv*pv))
    check(f'lattice_boundary_kernel_a{av}',abs(val-expected)<1e-9,'infinite nearest-neighbor normal chain integral',abs(val-expected))
Ga=1/(p*s.sqrt(4+spacing*spacing*p*p))
check('lattice_continuum_limit',s.simplify(s.limit(Ga,spacing,0)-1/(2*p))==0,'fixed p limit, not uniform near all poles')
check('finite_spacing_correction',s.simplify(s.limit((2*p*Ga-1)/spacing**2,spacing,0)+p*p/8)==0,'first relative correction')
# New nonlinear variational branch: independent exact derivative and reversal checks.
u0,u1,r,r0,c2,nu,I=s.symbols('u0 u1 r r0 c2 nu I',real=True)
V=c2*r*r*(u0-u1)**2/2+nu*(r*r-r0*r0)**2/4
check('new_edge_variation',s.simplify(s.diff(V,r)-(c2*r*(u0-u1)**2+nu*r*(r*r-r0*r0)))==0,'NEW proposed action, not recovered')
model=CandidateDynamicFoam(3,[(0,1),(1,2)],c2=.1,inertia=2,nu=.02,rstar=.3)
q0=np.array([.02,-.01,.03,.3,.28]);q1=q0+np.array([.001,0,-.001,0,.001])
qs=[q0,q1]
for t in range(1,25):qs.append(model.step(qs[-2],qs[-1]))
err=max(np.max(np.abs(model.reverse(qs[t],qs[t+1])-qs[t-1])) for t in range(1,25))
check('new_dynamic_branch_reversible',err<1e-14,'full signed-amplitude state',float(err))
check('new_dynamic_weights_nonnegative',min(model.weights(q).min() for q in qs)>=0,'weights are squares by construction')
check('new_dynamic_feedback_active',np.ptp(np.array(qs)[:,3])>1e-5,'nontrivial edge response')
check('new_dynamic_uniform_shift',np.allclose(model.gradient(q0+np.r_[np.ones(3)*7,np.zeros(2)])[:3],model.gradient(q0)[:3]),'source constant-mode symmetry')
# direct proof check of symplectic kick-drift map for arbitrary symmetric Hessian
h00,h01,h11,m0,m1=s.symbols('h00 h01 h11 m0 m1',nonzero=True)
H=s.Matrix([[h00,h01],[h01,h11]]);Minv=s.diag(1/m0,1/m1)
Jac=s.Matrix.vstack(s.Matrix.hstack(s.eye(2)-Minv*H,Minv),s.Matrix.hstack(-H,s.eye(2)))
JJ=s.Matrix.vstack(s.Matrix.hstack(s.zeros(2),s.eye(2)),s.Matrix.hstack(-s.eye(2),s.zeros(2)))
check('nonlinear_variational_map_symplectic',matzero(Jac.T*JJ*Jac-JJ),'regular discrete action; not exact continuous energy conservation')
breath=BreathingFoam(w,c2=.1,inertia=2.,nu=.01,astar=.5)
q0=np.r_[np.array([.02,-.03,.01]),.5];q1=q0+np.array([.001,0,-.001,.0001])
qhist=[q0,q1]
for t in range(1,31):qhist.append(breath.step(qhist[-2],qhist[-1]))
check('breathing_backreaction_nontrivial',abs(qhist[-1][-1]-.5)>1e-5,'NEW mode-preserving nonlinear branch')
check('breathing_inverse',all(np.allclose(breath.reverse(qhist[t],qhist[t+1]),qhist[t-1],atol=1e-15) for t in range(1,31)),'full branch state')
vec=np.array([1,0,-1.])/np.sqrt(2);Pg=np.outer(vec,vec)
check('breathing_preserves_selected_spectral_projector',all(np.allclose(Pg@laplacian(breath.weights(q[-1])),laplacian(breath.weights(q[-1]))@Pg) for q in qhist),'NOT derivation of physical graviton projector')
zero_b=np.r_[np.ones(3)*.2,0.]
check('white_edge_fixed_state',np.allclose(breath.step(zero_b,zero_b),zero_b),'off-diagonal W=0; may be unstable if astar>0')
check('breathing_zero_mode_no_bare_mass',all(np.allclose(laplacian(breath.weights(q[-1]))@np.ones(3),0) for q in qhist),'native Laplacian zero mode, not four-dimensional spin-2 proof')
# Every sample of the nonlinear branch obeys the conditional graph recurrence and exact memory.
qhist=np.array(qhist);bw=[breath.weights(q[-1]) for q in qhist]
by=time_varying_reduction(bw,[0,2],qhist[0,:3],qhist[1,:3],.1)
check('nonlinear_branch_shell_memory_identity',np.allclose(by,qhist[:,[0,2]],atol=2e-12),'retains generated breathing history, not shell-only dynamics')
# Instantaneously stable spectra need not give stability under time variation.
Mlo=s.Matrix([[s.Rational(3,2),-1],[1,0]])
Mhi=s.Matrix([[-s.Rational(3,2),-1],[1,0]])
cycle=Mhi*Mlo
check('parametric_instability_negative_control',abs(cycle.trace())>2 and cycle.det()==1,
      'eta alternates 1/2 and 7/2, both in (0,4); not asserted to be a trajectory of the breathing action',str(cycle.trace()))
# Source tensor restriction remains substantive: a symmetric gradient alone
# is killed by TT projection and cannot manufacture a radiative graviton.
pper=s.diag(1,1,0)
def tt(t):
    return pper*t*pper-pper*s.trace(pper*t)/2
hx,hy,hz=s.symbols('hx hy hz');kv=s.Matrix([0,0,1]);hv=s.Matrix([hx,hy,hz])
check('TT_symmetric_gradient_is_zero',matzero(tt(kv*hv.T+hv*kv.T)),
      'negative control for a tempting but NOT attributed source map')
symbasis=[]
for i in range(3):
    for j in range(i,3):
        mm=s.zeros(3);mm[i,j]=1;mm[j,i]=1;symbasis.append(mm)
TT=s.Matrix.hstack(*[s.Matrix([tt(mm)[i,j] for i in range(3) for j in range(i,3)]) for mm in symbasis])
check('TT_projector_rank_two',TT.rank()==2,'prescribed Minkowski polarization construction only')
check('TT_projector_idempotent',matzero(TT*TT-TT),'does not derive a native tensor projector')

results=dict(status='PASS',passed=len(checks),total=len(checks),checks=checks,
             seconds=time.time()-start,python=platform.python_version(),numpy=np.__version__,sympy=s.__version__,
             scope='Checks of recovered linear recurrence, derived elimination, and explicitly new native-depth candidate branches. No full MK Ultra or Einstein emergence certification.')
(ROOT/'results/CHECK_RESULTS.json').write_text(json.dumps(results,indent=2))
print(json.dumps({'passed':len(checks),'seconds':time.time()-start},indent=2))
