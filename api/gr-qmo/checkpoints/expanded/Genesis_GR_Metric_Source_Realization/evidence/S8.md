# Genesis source tensor — finite-to-local closure
Existing finite accounting:
\[
\operatorname{Pers}([X])=\sum_d
\operatorname{Inh}_d\operatorname{Band}_d\operatorname{Res}_d
\operatorname{Occ}_d\operatorname{Close}_d,
\]
\[
\boxed{M_G([X])=\operatorname{Pers}([P_{\rm lock}X])-\operatorname{Pers}([0_E]),}
\]
\[
\boxed{\Delta E_G(H)=
[\operatorname{Pers}([X_n])-\operatorname{Pers}([X_0])]/\epsilon_P.}
\]

For Resolution partition \(\mathcal P_R=\{c\}\), assign additive finite four-momentum \(p_G^a(c)\):
\[
p_G^a(A\sqcup B)=p_G^a(A)+p_G^a(B).
\]
Rest normalization:
\[
\boxed{p_G^0(\Sigma_{\rm rest})c=T_m(M_G([K]))c^2.}
\]

For oriented face \(f\), define witnessed four-momentum transfer \(\Phi_G^a(f;H)\) with
\[
\Phi_G^a(-f;H)=-\Phi_G^a(f;H).
\]
Finite balance:
\[
\boxed{p_G^a(c;H_1)-p_G^a(c;H_0)
=-\sum_{f\subset\partial c}\Phi_G^a(f;H_0\to H_1)+S_G^a(c;H).}
\]
For closed matter accounting \(S_G^a=0\).

Assume the additive source/flux measures admit densities under admissible Resolution refinement. Define the local tensor by
\[
\boxed{dP_G^a=T_G^{ab}\,d\Sigma_b.}
\]
This is the precise local meaning of the source tensor: four-momentum flux through oriented hypersurface elements.

For unit timelike \(u^a\), let
\[
h_G^{ab}=g_G^{ab}+u^au^b/c^2.
\]
Then
\[
\boxed{\varepsilon_G=T^G_{ab}u^au^b/c^2,}
\]
\[
\boxed{q_G^a=-h_G^a{}_cT_G^{cd}u_d,}
\]
\[
\boxed{\sigma_G^{ab}=h_G^a{}_ch_G^b{}_dT_G^{cd}.}
\]
Reconstruction:
\[
\boxed{
T_G^{ab}=
\varepsilon_Gu^au^b/c^2+
(u^aq_G^b+q_G^au^b)/c^2+
\sigma_G^{ab}.
}
\]
For the GR-equivalent non-spin sector:
\[
\boxed{T_G^{ab}=T_G^{ba}.}
\]
The refinement limit of finite balance gives
\[
\boxed{\nabla^G_aT_G^{ab}=0.}
\]
Thus v1.0's semantic energy/flux/stress placeholders are replaced by projections of one finite-to-local four-momentum flux tensor.
