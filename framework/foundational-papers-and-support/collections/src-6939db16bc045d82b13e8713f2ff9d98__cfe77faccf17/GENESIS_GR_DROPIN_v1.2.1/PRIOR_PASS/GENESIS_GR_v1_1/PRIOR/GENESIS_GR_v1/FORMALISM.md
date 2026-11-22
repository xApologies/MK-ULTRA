# GENESIS GENERAL RELATIVITY — FORMALISM

## 1 Two worlds
\[
X^w=(X,H_X,W_X,I_X),\quad
G_R^{(d)}=(V_R,E_R,\rho_d,H_d),\quad
\mathsf{RR}_{D,B}=\operatorname{Path}(\operatorname{Gen}_D(B)).
\]
\[
\Pi:X\rightsquigarrow Y,\qquad \operatorname{AdmLift}_R(y)\subseteq\Pi^{-1}(y).
\]
\[
\rho_R^{GR}:=\operatorname{Realize}^{GR}_R\circ q_R.
\]

## 2 Genesis metric
On a GR-readable rank-four local Genesis module \(T_x^G\):
\[
\boxed{\mathfrak g_G:T_x^G\times T_x^G\to\mathbb R},\qquad
\mathfrak g_G(u,v)=\mathfrak g_G(v,u),
\]
\[
\det\mathfrak g_G\ne0,\qquad \operatorname{sig}(\mathfrak g_G)=(-,+,+,+).
\]
\[
\boxed{ds_G^2=\mathfrak g_G(dX,dX).}
\]

## 3 Genesis connection
Bandwidth filters admissible lifts; the connection selects:
\[
\boxed{\mathcal C_G(a,x)=\lambda_{a,x}\in\operatorname{AdmLift}_{R,B}(a,x).}
\]
Gravitational sector:
\[
\boxed{\operatorname{Tor}_G(u,v)=\mathcal C_{G,u}v-\mathcal C_{G,v}u-[u,v]_G=0}
\]
and
\[
\boxed{u[\mathfrak g_G(v,w)]
=\mathfrak g_G(\mathcal C_{G,u}v,w)+\mathfrak g_G(v,\mathcal C_{G,u}w).}
\]

## 4 Genesis transport
For \(\gamma=a_n\circ\cdots\circ a_1\):
\[
H(\gamma)=(a_1,\ldots,a_n),\qquad
\boxed{P_\gamma^G=\lambda_{a_n}\circ\cdots\circ\lambda_{a_1}.}
\]
\[
P_{\gamma_2\circ\gamma_1}^G=P_{\gamma_2}^G\circ P_{\gamma_1}^G,\qquad P_{1_x}^G=I_x.
\]

## 5 Genesis geodesic
\[
\boxed{\mathcal C_{G,\dot\gamma}\dot\gamma=0.}
\]
Smooth metric form:
\[
\delta\int_\gamma\sqrt{|\mathfrak g_G(\dot\gamma,\dot\gamma)|}\,d\lambda=0.
\]

## 6 Genesis curvature
\[
\boxed{\operatorname{Hol}_G(\gamma)=P_\gamma^G.}
\]
Finite path defect:
\[
\boxed{K_G(\gamma_1,\gamma_2;x)=\operatorname{Def}(P_{\gamma_1}^G(x),P_{\gamma_2}^G(x)).}
\]
Smooth curvature:
\[
\boxed{\mathcal R_G(u,v)w=
\mathcal C_{G,u}\mathcal C_{G,v}w-\mathcal C_{G,v}\mathcal C_{G,u}w-\mathcal C_{G,[u,v]_G}w.}
\]
Finite-to-smooth:
\[
\boxed{\mathcal R_G(u,v)w=
\lim_{A_G(\square_{uv})\to0}\frac{(P_{\square_{uv}}^G-I)w}{A_G(\square_{uv})}.}
\]

## 7 Ricci
\[
\boxed{\operatorname{Ric}_G(u,v)=\operatorname{Tr}[w\mapsto\mathcal R_G(w,u)v].}
\]
If \(\mathcal R_G(e_c,e_d)e_b=\mathcal R^a{}_{bcd}e_a\):
\[
\boxed{(\operatorname{Ric}_G)_{bd}=\mathcal R^a{}_{bad}.}
\]

## 8 Scalar curvature
\[
\boxed{\operatorname{Scal}_G=\mathfrak g_G^{ab}(\operatorname{Ric}_G)_{ab}.}
\]

## 9 Einstein curvature
\[
\boxed{\operatorname{Ein}_G=\operatorname{Ric}_G-\frac12\operatorname{Scal}_G\mathfrak g_G.}
\]
\[
\boxed{\operatorname{Ein}_G^\Lambda=\operatorname{Ein}_G+\Lambda_G\mathfrak g_G.}
\]

## 10 Genesis source object
Inherited Persistence:
\[
\operatorname{Pers}_d([X])=
\operatorname{Inh}_d([X])\operatorname{Band}_d([X])\operatorname{Res}_d([X])
\operatorname{Occ}_d([X])\operatorname{Close}_d([X]),
\quad
\operatorname{Pers}([X])=\sum_d\operatorname{Pers}_d([X]).
\]
Native Mass:
\[
\boxed{\operatorname{Mass}_{MK}([X])=\operatorname{Pers}([P_{\rm lock}X])-\operatorname{Pers}([0_E]).}
\]
History energy:
\[
\boxed{\Delta E_G(H)=\frac{\operatorname{Pers}([X_n])-\operatorname{Pers}([X_0])}{\epsilon_P}.}
\]
With local coframe \(\theta^a\), define
\[
\boxed{\mathbb T_G=
\varepsilon_G\theta^0\otimes\theta^0+
\sum_i j_{G,i}(\theta^0\otimes\theta^i+\theta^i\otimes\theta^0)+
\sum_{ij}\sigma_{G,ij}\theta^i\otimes\theta^j.}
\]
Here \(\varepsilon_G\) is local witnessed History-energy density; \(j_G\) is directed History/Persistence transport; \(\sigma_G\) is directional relational stress/closure transfer.

Finite source constraints:
\[
\sum_{c\subset\Sigma}\varepsilon_G(c)\nu_G(c)=E_G(\Sigma),
\]
and for isolated rest lock \(K\):
\[
\boxed{E_G^{rest}(\Sigma)=c^2T_m(\operatorname{Mass}_{MK}([K])).}
\]
Admissible refinement preserves these integrated quantities.

## 11 Field equation
\[
\boxed{\operatorname{Ein}_G^\Lambda=\kappa_G\mathbb T_G.}
\]

## 12 Conservation
For a \((0,2)\) tensor \(S\):
\[
\boxed{(\operatorname{Div}_G S)_b=\mathfrak g_G^{ac}(\mathcal C_{G,e_c}S)_{ab}.}
\]
Bianchi chain:
\[
\mathcal R_G(u,v)w+\mathcal R_G(v,w)u+\mathcal R_G(w,u)v=0,
\]
\[
\mathcal C_{G,[a}\mathcal R^d{}_{|e|bc]}=0,
\]
\[
\boxed{\operatorname{Div}_G\operatorname{Ein}_G=0},
\qquad
\boxed{\operatorname{Div}_G\mathbb T_G=0}.
\]

## 13 Complete spine
\[
\boxed{
\mathfrak g_G\to\mathcal C_G\to P_\gamma^G\to\operatorname{Hol}_G
\to\mathcal R_G\to\operatorname{Ric}_G\to\operatorname{Scal}_G
\to\operatorname{Ein}_G^\Lambda=\kappa_G\mathbb T_G.
}
\]

## Construction axioms
A0 History/provenance integrity.
A1 Resolution refinement does not cause the event and preserves stabilized readable invariants.
A2 Bandwidth filters; it does not invent transformations.
A3 \(\mathfrak g_G\) is Lorentzian/nondegenerate in the GR sector.
A4 The gravitational connection is torsion-free and metric-compatible.
A5 Transport is functorial on typed paths.
A6 Normalized small-loop defect has a smooth/refinement limit.
A7 Local readable rank is four and metric trace is legal.
A8 Source cell subdivision preserves total source.
A9 Rest source normalizes to Native Mass energy.
A10 Finite boundary flux equals witnessed History-energy/momentum change.
A11 \(\mathbb T_G\) is symmetric.
A12 \(\rho_R^{GR}(\Lambda_G)=\Lambda\), \(\rho_R^{GR}(\kappa_G)=8\pi G/c^4\).
A13 Readout preserves typed composition, tensor operations, contraction and trace.

## Core theorems
T1 A3-A4 select the Genesis Levi-Civita connection.
T2 A1,A5,A6 realize finite holonomy/path defect as \(\mathcal R_G\).
T3 A7 makes Ricci/scalar contractions well-defined and yields the Genesis Einstein object.
T4 A8-A11 extend finite Persistence/History/Mass accounting into a local symmetric source tensor.
T5 The Bianchi chain makes the field equation compatible with source conservation.
T6 Under A12-A13 every object and operation below commutes with its GR realization.
