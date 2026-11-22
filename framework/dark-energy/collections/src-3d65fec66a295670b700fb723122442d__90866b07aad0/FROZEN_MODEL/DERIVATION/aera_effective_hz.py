"""Reproducible conditional AERA effective coherent-shell H(z) baseline."""
import math
H0=67.4
OMEGA_M=0.315
OMEGA_R=9.2e-5
OMEGA_L=1-OMEGA_M-OMEGA_R
C=299792458.0
G=6.67430e-11
MPC=3.0856775814913673e22
def hubble(z):
    if z<=-1: raise ValueError("redshift must exceed -1")
    return H0*math.sqrt(OMEGA_R*(1+z)**4+OMEGA_M*(1+z)**3+OMEGA_L)
def rho_critical():
    h_si=H0*1000/MPC
    return 3*h_si*h_si/(8*math.pi*G)
def epsilon_dark_energy():
    return OMEGA_L*rho_critical()*C*C
def elastic_binding(a,a0,k):
    return k*(a-a0)**2/a**3
def binding_late_root(a0,k,rho_de):
    r=rho_de*a0/k
    if not 0<r<4/27: return None
    lo=3*a0;hi=lo
    while elastic_binding(hi,a0,k)>rho_de:hi*=2
    for _ in range(120):
        mid=(lo+hi)/2
        if elastic_binding(mid,a0,k)>rho_de:lo=mid
        else:hi=mid
    return (lo+hi)/2
def run_tests():
    assert abs(hubble(0)-H0)<1e-10
    assert OMEGA_L>0
    assert abs(hubble(1)-120.689)<0.01
    assert epsilon_dark_energy()>0
    a=binding_late_root(1,1,.05)
    assert a>3 and abs(elastic_binding(a,1,1)-.05)<1e-10
    print("PASS: coherent-phase expansion and elastic-threshold algebra")
if __name__=="__main__":
    run_tests()
    print("Omega_Lambda =",OMEGA_L)
    print("rho_crit0 =",rho_critical(),"kg/m^3")
    print("epsilon_A0 =",epsilon_dark_energy(),"J/m^3")
    print("p_A0 =",-epsilon_dark_energy(),"Pa")
    for z in [0,.25,.5,1,2,3,-.25,-.5,-.75]:
        print(f"z={z:>5}: H={hubble(z):.3f} km/s/Mpc")
