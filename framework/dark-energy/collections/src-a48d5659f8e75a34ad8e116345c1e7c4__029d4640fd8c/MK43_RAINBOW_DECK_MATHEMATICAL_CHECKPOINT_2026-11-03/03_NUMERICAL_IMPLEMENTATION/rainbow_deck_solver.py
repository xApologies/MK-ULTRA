#!/usr/bin/env python3
"""MK43 Rainbow Deck reproducible fixed-vacuum background and conditional shell."""
import mpmath as mp
mp.mp.dps = 85
HREF=mp.mpf("73")
CM=mp.mpf("0.2677779734086515")
CR=mp.mpf("0.0000783820114168425")
CDE=mp.mpf("0.5845821504419774")
WHITE=mp.mpf("0.5389276")
MPC_KM=mp.mpf("3.0856775814913673e19")
SEC_PER_GYR=mp.mpf("365.25")*24*3600*10**9
def H(a):
    a=mp.mpf(a)
    return HREF*mp.sqrt(CR/a**4+CM/a**3+CDE)
def cosmic_time(a):
    a=mp.mpf(a)
    return MPC_KM/SEC_PER_GYR * mp.quad(lambda u: u/mp.sqrt(CR+CM*u+CDE*u**4)/HREF,
                                         [0,a/100,a/10,a])
def shell_late_root(q):
    q=mp.mpf(q)
    if not 0<q<mp.mpf(4)/27: raise ValueError("q outside two-root regime")
    lo=mp.mpf(3); hi=1/q+4
    for _ in range(500):
        mid=(lo+hi)/2
        if (mid-1)**2/mid**3>q:lo=mid
        else:hi=mid
    return (lo+hi)/2
def report(aN="0.01",q="0.005"):
    aD=mp.mpf(aN)*shell_late_root(q)
    for label,value in [("White",WHITE),("C_ref",CDE/WHITE),("H_today",H(1)),
                        ("Age_today_Gyr",cosmic_time(1)),("a_D",aD),
                        ("t_D_Gyr",cosmic_time(aD)),("H_D",H(aD))]:
        print(label,mp.nstr(value,55))
    print("future_dissolution",aD>1)
if __name__=="__main__":report()
