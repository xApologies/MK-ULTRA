# Genesis GR — Thirteen-Point Complete Mathematical Map

## 1. Two mathematical worlds
Genesis state:
\[
\boxed{
\mathfrak G=(D,\mathcal R,R,B,H,\chi,\mathcal C,P).
}
\]
GR target:
\[
(M,g,\nabla,\mathrm{Riem},\mathrm{Ric},R,G,T).
\]
Readout:
\[
\boxed{\rho_G:\mathfrak G_{\rm GR}\to\mathfrak G_{\rm Einstein}.}
\]

## 2. Genesis metric
Use the roadmap definition:
\[
\boxed{
\mathfrak g_G(x;a,b)
=
\mathcal Q_R[\mathcal R_x(a,b),B_x,H_x,\chi_x].
}
\]
Required realization:
\[
\boxed{\rho_G(\mathfrak g_G)=g_{\mu\nu}.}
\]
Native interval:
\[
\boxed{ds_G^2=\mathfrak g_G(dX,dX),\qquad
\rho_G(ds_G^2)=g_{\mu\nu}dx^\mu dx^\nu.}
\]
No claim is made that spacetime inherits Genesis; this is the Genesis-side representation of the already-established spacetime metric readout.

## 3. Genesis connection
\[
\operatorname{AdmLift}_R(y)\subseteq\Pi^{-1}(y).
\]
\[
\boxed{
\mathcal C_G:
(x,\operatorname{AdmLift}_{R,B}(x),H)\mapsto\ell_x.
}
\]
\[
\boxed{\rho_G(\mathcal C_G)=\nabla.}
\]
In the GR sector:
\[
\boxed{
\rho_G(\mathcal C_G)^\rho{}_{\mu\nu}
=
\Gamma^\rho{}_{\mu\nu}
=
\frac12g^{\rho\lambda}
(\partial_\mu g_{\lambda\nu}+\partial_\nu g_{\lambda\mu}-\partial_\lambda g_{\mu\nu}).
}
\]

## 4. Genesis transport
For
\[
\gamma=a_n\circ\cdots\circ a_1,
\qquad
H(\gamma)=(a_1,\ldots,a_n),
\]
define
\[
\boxed{
P_\gamma^G=P_{a_n}\circ\cdots\circ P_{a_1}.
}
\]
Equivalence:
\[
\boxed{
\rho_G\circ P_\gamma^G
=
P_{\rho_G(\gamma)}^\nabla\circ\rho_G.
}
\]

## 5. Genesis geodesic
\[
\boxed{\mathcal C_G(\dot\gamma_G)\dot\gamma_G=0.}
\]
Variational form:
\[
\boxed{
\gamma_G^\star
=
\operatorname*{ext}_{\gamma\in\mathsf{RR}_{D,B}}
\int_\gamma\sqrt{|\mathfrak g_G(dX,dX)|}.
}
\]
Readout:
\[
\boxed{
\frac{d^2x^\mu}{d\lambda^2}
+
\Gamma^\mu{}_{\alpha\beta}
\frac{dx^\alpha}{d\lambda}
\frac{dx^\beta}{d\lambda}=0.
}
\]

## 6. Genesis curvature
Holonomy:
\[
\boxed{\operatorname{Hol}_G(\gamma)=P_\gamma^G.}
\]
Finite path defect:
\[
\boxed{
K_G(\gamma_1,\gamma_2;x)
=
\operatorname{Def}(P_{\gamma_1}^G(x),P_{\gamma_2}^G(x)).
}
\]
Smooth/refined curvature:
\[
\boxed{
\mathfrak R_G(a,b)
=
\lim_{\operatorname{Area}_G(\gamma)\to0}
\frac{P_{\gamma(a,b)}^G-I}{\operatorname{Area}_G(\gamma)}.
}
\]
Equivalently:
\[
\mathfrak R_G(u,v)w=
\mathcal C_{G,u}\mathcal C_{G,v}w
-\mathcal C_{G,v}\mathcal C_{G,u}w
-\mathcal C_{G,[u,v]}w.
\]
Readout:
\[
\boxed{\rho_G(\mathfrak R_G)=R^\rho{}_{\sigma\mu\nu}.}
\]

## 7. Genesis Ricci contraction
\[
\boxed{
\mathfrak{Ric}_G(u,v)
=
\operatorname{Tr}[w\mapsto\mathfrak R_G(w,u)v].
}
\]
In components:
\[
\boxed{
(\mathfrak{Ric}_G)_{bd}
=
\mathfrak R_G{}^a{}_{bad}.
}
\]
Readout:
\[
\boxed{\rho_G(\mathfrak{Ric}_G)=R_{\mu\nu}.}
\]

## 8. Genesis scalar curvature
\[
\boxed{
\mathfrak R_G^{(0)}
=
\operatorname{Tr}_{\mathfrak g_G}(\mathfrak{Ric}_G)
=
\mathfrak g_G^{ab}(\mathfrak{Ric}_G)_{ab}.
}
\]
\[
\boxed{\rho_G(\mathfrak R_G^{(0)})=R.}
\]

## 9. Genesis Einstein curvature
\[
\boxed{
\mathfrak E_G
=
\mathfrak{Ric}_G-\frac12\mathfrak R_G^{(0)}\mathfrak g_G.
}
\]
\[
\boxed{
\mathfrak E_G^\Lambda
=
\mathfrak E_G+\Lambda_G\mathfrak g_G.
}
\]
\[
\boxed{\rho_G(\mathfrak E_G)=G_{\mu\nu}.}
\]

## 10. Genesis source object
Native mass remains:
\[
\boxed{
\operatorname{Mass}_{MK}([X])
=
\operatorname{Pers}([P_{\rm lock}X])
-
\operatorname{Pers}([0_E]).
}
\]
History energy:
\[
\boxed{
\Delta E_G(H)
=
\frac{\operatorname{Pers}([X_n])-\operatorname{Pers}([X_0])}{\epsilon_{MK}}.
}
\]
Define the local source object as the refinement density of witnessed four-momentum transfer:
\[
\boxed{dP_G^a=\mathfrak T_G^{ab}\,d\Sigma_b.}
\]
Rest normalization:
\[
\boxed{
P_G^0(\Sigma_{\rm rest})c
=
T_m(\operatorname{Mass}_{MK}([K]))c^2.
}
\]
Local decomposition relative to timelike \(u\):
\[
\varepsilon_G=\mathfrak T^G_{ab}u^au^b/c^2,
\]
\[
q_G^a=-h_G^a{}_c\mathfrak T_G^{cd}u_d,
\]
\[
\sigma_G^{ab}=h_G^a{}_ch_G^b{}_d\mathfrak T_G^{cd}.
\]
Readout:
\[
\boxed{\rho_G(\mathfrak T_G)=T_{\mu\nu}.}
\]

## 11. Genesis field equation
\[
\boxed{
\mathfrak E_G+\Lambda_G\mathfrak g_G
=
\kappa_G\mathfrak T_G.
}
\]
with
\[
\boxed{
\rho_G(\Lambda_G)=\Lambda,\qquad
\rho_G(\kappa_G)=\frac{8\pi G}{c^4}.
}
\]
Therefore
\[
\boxed{
\rho_G[
\mathfrak E_G+\Lambda_G\mathfrak g_G
=
\kappa_G\mathfrak T_G]
=
G_{\mu\nu}+\Lambda g_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu}.
}
\]

## 12. Genesis conservation law
Define
\[
\boxed{
(\mathfrak D_GS)_b
=
\mathfrak g_G^{ac}(\mathcal C_{G,e_c}S)_{ab}.
}
\]
The curvature connection satisfies the Bianchi chain:
\[
\mathcal C_{G,[e}\mathfrak R_G{}^a{}_{|b|cd]}=0
\]
and hence
\[
\boxed{\mathfrak D_G\mathfrak E_G=0.}
\]
For constant couplings the field equation gives
\[
\boxed{\mathfrak D_G\mathfrak T_G=0.}
\]
Readout:
\[
\boxed{\rho_G(\mathfrak D_G\mathfrak T_G)=\nabla_\mu T^{\mu\nu}=0.}
\]

## 13. Complete Genesis-GR spine
\[
\boxed{
\mathfrak g_G
\to
\mathcal C_G
\to
P_\gamma^G
\to
\operatorname{Hol}_G
\to
\mathfrak R_G
\to
\mathfrak{Ric}_G
\to
\mathfrak R_G^{(0)}
\to
\mathfrak E_G^\Lambda
=
\kappa_G\mathfrak T_G.
}
\]

Correspondence:
\[
\boxed{
\begin{aligned}
\mathfrak g_G&\leftrightarrow g_{\mu\nu}\\
\mathcal C_G&\leftrightarrow\Gamma^\rho{}_{\mu\nu}\\
P_\gamma^G&\leftrightarrow\text{parallel transport}\\
\operatorname{Hol}_G&\leftrightarrow\text{holonomy}\\
\mathfrak R_G&\leftrightarrow R^\rho{}_{\sigma\mu\nu}\\
\mathfrak{Ric}_G&\leftrightarrow R_{\mu\nu}\\
\mathfrak R_G^{(0)}&\leftrightarrow R\\
\mathfrak E_G&\leftrightarrow G_{\mu\nu}\\
\mathfrak T_G&\leftrightarrow T_{\mu\nu}.
\end{aligned}
}
\]
