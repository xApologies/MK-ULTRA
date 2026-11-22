# Native Genesis gravitational geometry
Choose frame \(e_a\), coframe \(\theta^a\), \(\theta^a(e_b)=\delta^a_b\).
\[
g^G_{ab}=g_G(e_a,e_b),\qquad g_G^{ac}g^G_{cb}=\delta^a_b,\qquad
\boxed{ds_G^2=g^G_{ab}\theta^a\theta^b.}
\]
Causal classes:
\[
g_G(v,v)<0\ {\rm timelike},\quad =0\ {\rm null},\quad >0\ {\rm spacelike}.
\]
\[
d\tau_G=c^{-1}\sqrt{-ds_G^2}.
\]

The upstream connection-selection architecture is restricted in the gravitational branch by
\[
\boxed{\operatorname{Tor}_G(u,v)=0,\qquad \nabla_Gg_G=0.}
\]
Hence, in a coordinate frame,
\[
\boxed{\Gamma^{G\,a}_{bc}=\frac12g_G^{ad}
(\partial_bg^G_{dc}+\partial_cg^G_{db}-\partial_dg^G_{bc}).}
\]

For Rainbow Road path \(\gamma=a_n\circ\cdots\circ a_1\),
\[
\boxed{P_\gamma^G=\lambda_{a_n}\circ\cdots\circ\lambda_{a_1}.}
\]
Smooth parallel transport: \(\nabla^G_{\dot\gamma}V=0\).
Geodesic:
\[
\boxed{\nabla^G_{\dot\gamma}\dot\gamma=0,\qquad
\ddot X^a+\Gamma^{G\,a}_{bc}\dot X^b\dot X^c=0.}
\]

Holonomy:
\[
\operatorname{Hol}_G(\gamma)=P_\gamma^G.
\]
Finite same-endpoint defect:
\[
K_G(\gamma_1,\gamma_2;x)=\operatorname{Def}(P_{\gamma_1}^Gx,P_{\gamma_2}^Gx).
\]
Curvature:
\[
\boxed{R_G(u,v)w=\nabla^G_u\nabla^G_vw-\nabla^G_v\nabla^G_uw-\nabla^G_{[u,v]}w.}
\]
Components:
\[
\boxed{R_G{}^a{}_{bcd}=
\partial_c\Gamma^{G\,a}_{db}-\partial_d\Gamma^{G\,a}_{cb}
+\Gamma^{G\,a}_{ce}\Gamma^{G\,e}_{db}
-\Gamma^{G\,a}_{de}\Gamma^{G\,e}_{cb}.}
\]
Finite-to-smooth contract:
\[
R_G(u,v)w=\lim_{A_G(\square)\to0}\frac{(P_\square^G-I)w}{A_G(\square)}
\]
where the Resolution refinement limit exists.

Ricci/scalar/Einstein:
\[
\boxed{\operatorname{Ric}^G_{bd}=R_G{}^a{}_{bad},\qquad
\mathcal R_G=g_G^{bd}\operatorname{Ric}^G_{bd},}
\]
\[
\boxed{G^G_{ab}=\operatorname{Ric}^G_{ab}-\frac12\mathcal R_Gg^G_{ab},\qquad
G^{G,\Lambda}_{ab}=G^G_{ab}+\Lambda_Gg^G_{ab}.}
\]

Bianchi:
\[
\nabla^G_{[e}R_G{}^a{}_{|b|cd]}=0,\qquad
\boxed{\nabla_G^aG^G_{ab}=0.}
\]

Volume:
\[
dV_G=\sqrt{|\det g_G|}\,d^4X.
\]
Killing:
\[
\boxed{\mathcal L_Kg_G=0\iff\nabla^G_aK_b+\nabla^G_bK_a=0.}
\]
Geodesic deviation (fixed sign convention):
\[
\boxed{\nabla^G_u\nabla^G_u\xi=-R_G(\xi,u)u.}
\]
