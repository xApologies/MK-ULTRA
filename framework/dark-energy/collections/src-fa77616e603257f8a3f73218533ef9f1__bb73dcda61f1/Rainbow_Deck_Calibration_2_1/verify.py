import mpmath as mp
mp.mp.dps = 65
Cr=mp.mpf('0.0000783820114168425')
Cm=mp.mpf('0.2678818747')
Cde=mp.mpf('0.5844998671')
White=mp.mpf('0.5389276')
H_ref=mp.mpf('73')
mpc_km=mp.mpf('3.0856775814913673e19')
seconds_gyr=mp.mpf('365.25')*86400*10**9
H0=H_ref*mp.sqrt(Cr+Cm+Cde)
age=mpc_km/seconds_gyr/H_ref*mp.quad(lambda a:a/mp.sqrt(Cr+Cm*a+Cde*a**4),[0,mp.mpf('.001'),mp.mpf('.1'),1])
for name,value in [('H0_km_s_Mpc',H0),('age_Gyr',age),('Omega_r',Cr/(Cr+Cm+Cde)),('Omega_m',Cm/(Cr+Cm+Cde)),('Omega_DE',Cde/(Cr+Cm+Cde)),('C_ref',Cde/White)]:
 print(name,mp.nstr(value,55))
