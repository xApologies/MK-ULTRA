# Time-Space Rainbow Road Transport Model v1.0 Candidate

**Status:** FORMAL TRANSPORT ARCHITECTURE CLOSED / PHYSICAL INDUCED TRANSPORT OPEN  
**Date:** 2026-08-25

## 1. Time-Space geometry

The operative global object is five-dimensional Time-Space:

\[
\pi:T_5\to S^3.
\]

For a continuity address \(p\in S^3\),

\[
\Sigma_p:=\pi^{-1}(p)\cong S^2.
\]

The dimensional bookkeeping is:

\[
\dim T_5=\dim S^3+\dim S^2=3+2=5.
\]

For a base path

\[
\gamma:[0,1]\to S^3,\qquad
\gamma(0)=p_\alpha,\quad
\gamma(1)=p_\beta,
\]

define its Time-Space Corridor as the pullback:

\[
W_\gamma:=\gamma^*(T_5).
\]

When locally trivial,

\[
W_\gamma\cong S^2\times[0,1],
\]

with endpoint boundary

\[
\partial W_\gamma
=
\Sigma_\alpha\sqcup(-\Sigma_\beta).
\]

Thus the Corridor is not an extra tunnel added to Time-Space. It is the restriction of the existing five-dimensional structure to an admissible continuity path.

## 2. Address Object

A transport Address is

\[
\boxed{
A_p=
(
p,\Sigma_p,F_p,\chi_p,\operatorname{Inv}_p,
R_p,B_p,O_p,H_p
).
}
\]

Fields:

- \(p\): S3 continuity address;
- \(\Sigma_p\): localized S2 fiber;
- \(F_p\): operative organized state;
- \(\chi_p\): chirality organization carried by that state;
- \(\operatorname{Inv}_p\): invariant organizational residue;
- \(R_p\): available Resolution;
- \(B_p\): available Bandwidth;
- \(O_p\): recursive ordering state;
- \(H_p\): append-only History/provenance.

The Address is not merely a coordinate. It records where the state is, what state it is, what must remain recoverable, and how it arrived.

## 3. Corridor Transport

For an admissible path \(\gamma:p_\alpha\to p_\beta\), let

\[
P_\gamma:
F_\alpha\rightharpoonup F_\beta
\]

be the partial Time-Space transport map.

The chirality component is

\[
P_\gamma^\chi:
\chi_\alpha\to\chi_\beta.
\]

The map is partial because transport is defined only when the complete admissibility contract passes.

## 4. Portal

A Portal is a transaction over one Corridor:

\[
\boxed{
\mathsf P_{\alpha\beta}
=
(
A_\alpha,A_\beta,\gamma,
P_\gamma,\mathcal C_{\alpha\beta},
W_{\alpha\beta}
).
}
\]

Here:
- \(\gamma\) supplies the route;
- \(P_\gamma\) supplies the state transport/re-realization;
- \(\mathcal C_{\alpha\beta}\) is the preservation/admission contract;
- \(W_{\alpha\beta}\) is the append-only transaction witness.

The minimum success predicate is:

\[
\operatorname{Adm}(\mathsf P_{\alpha\beta},F_\alpha)=1
\]

iff all declared conditions hold:

\[
\begin{aligned}
&\text{target address resolves},\\
&\chi_\beta=\tau_\gamma(\chi_\alpha),\\
&F_\beta\sim_{\rm id}F_\alpha,\\
&\operatorname{Inv}_\beta=\operatorname{Inv}_\alpha,\\
&R_\gamma\ge R_{\min},\\
&B_\gamma\ge B_{\min},\\
&\text{target recursive closure exists},\\
&\text{provenance/witness is complete}.
\end{aligned}
\]

The Portal is the transaction. The Corridor is the route. They are not the same object.

## 5. Rainbow Road

Let

\[
\mathsf P_i:A_{i-1}\to A_i,\qquad i=1,\ldots,n
\]

be admissible Portals with matching intermediate addresses.

The Rainbow Road is

\[
\boxed{
\mathfrak R
=
\mathsf P_n\circ\cdots\circ\mathsf P_1.
}
\]

Its base route is the ordered concatenation

\[
\Gamma
=
\gamma_1\star\cdots\star\gamma_n,
\]

and its state transport is

\[
P_\Gamma
=
P_{\gamma_n}\circ\cdots\circ P_{\gamma_1}.
\]

Its History is not quotient-collapsed:

\[
H(\mathfrak R)
=
H(\mathsf P_1)\Vert\cdots\Vert H(\mathsf P_n).
\]

The Road is therefore a persistent navigable path, not an unexplained direct source-to-target edge.

## 6. Theorem TR-1 — Portal composition preserves the declared identity contract

Assume:
1. each \(\mathsf P_i\) is admissible;
2. the intermediate target/source Address objects match;
3. \(\sim_{\rm id}\) is the declared persistent-identity equivalence;
4. chirality transport maps compose;
5. invariant residue is preserved on every segment.

Then the composite Road satisfies:

\[
F_n\sim_{\rm id}F_0,
\]

\[
\chi_n
=
(\tau_{\gamma_n}\circ\cdots\circ\tau_{\gamma_1})(\chi_0),
\]

and

\[
\operatorname{Inv}_n
=
\operatorname{Inv}_0.
\]

**Proof.**
Persistent identity follows by transitivity of the declared equivalence.
Chirality transport follows by ordinary map composition.
Invariant-residue equality follows inductively from segmentwise equality.
Resolution, Bandwidth, closure, and provenance remain segmentwise obligations along the full Road.

Therefore an object can change address and representation while remaining recoverably the same declared persistent object.

## 7. Exact identity versus persistent identity

The model distinguishes:

### Exact full-state identity

\[
A_\alpha=A_\beta.
\]

All Address fields agree.

### Persistent identity

\[
F_\alpha\sim_{\rm id}F_\beta
\]

with transported chirality and invariant residue agreement.

### Readable equivalence

For readout map

\[
\Pi_{\rm read}:A\to Y,
\]

two states may satisfy

\[
\Pi_{\rm read}(A_1)
=
\Pi_{\rm read}(A_2)
\]

even though

\[
A_1\ne A_2.
\]

### History equality

\[
H_1=H_2
\]

is stronger than same endpoint.

Hence:

\[
\boxed{
\text{same readable endpoint}
\not\Rightarrow
\text{same full state}
\not\Rightarrow
\text{same Road History}.
}
\]

## 8. Theorem TR-2 — Projection does not erase formal route multiplicity

If \(\Pi_{\rm read}\) is not injective, there exist formally distinct Address states or Roads whose readable projection agrees.

Therefore readout equality cannot be used as proof of path equality.

Road History must remain an independent provenance field.

This is the transport analogue of the existing project rule:

\[
\text{carrier/readout confluence}
\ne
\text{History/provenance confluence}.
\]

## 9. Local QFT and GR representations

At \(p\in S^3\), let the local operative state be \(F_p\).

Define typed representation maps:

\[
\rho_{Q,p}:F_p\to\mathcal Q_p,
\]

\[
\rho_{G,p}:F_p\to\mathcal G_p.
\]

These are distinct representations of common local ancestry; they are not identities between a quantum field and a metric.

Define the local common-ancestry relation:

\[
\mathcal R_{QG,p}
=
\{
(q,g):
\exists F_p,\ 
q=\rho_{Q,p}(F_p),\
g=\rho_{G,p}(F_p)
\}.
\]

## 10. Induced readable transport

For a Corridor/Road \(\Gamma:p_\alpha\to p_\beta\), introduce candidate readable transports

\[
U_Q(\Gamma):
\mathcal Q_\alpha\to\mathcal Q_\beta,
\]

\[
U_G(\Gamma):
\mathcal G_\alpha\to\mathcal G_\beta.
\]

These are formal targets. Their actual physical construction is not supplied by the present transport model.

The sector naturality target is

\[
\boxed{
\rho_{s,\beta}\circ P_\Gamma
=
U_s(\Gamma)\circ\rho_{s,\alpha},
\qquad
s\in\{Q,G\}.
}
\]

Plain language:

**transport the full state, then read it = read the state, then propagate that readable representation consistently.**

## 11. Theorem TR-3 — Segmentwise commutation implies Road-wise commutation

Let

\[
\mathsf P_i:A_{i-1}\to A_i
\]

be a composable Rainbow Road.

Assume for sector \(s\) that every segment satisfies

\[
\rho_{s,i}\circ P_i
=
U_{s,i}\circ\rho_{s,i-1}.
\]

Then

\[
\boxed{
\rho_{s,n}\circ
(P_n\circ\cdots\circ P_1)
=
(U_{s,n}\circ\cdots\circ U_{s,1})
\circ\rho_{s,0}.
}
\]

**Proof by induction.**
For two segments,

\[
\rho_{s,2}P_2P_1
=
U_{s,2}\rho_{s,1}P_1
=
U_{s,2}U_{s,1}\rho_{s,0}.
\]

Repeated substitution proves the \(n\)-segment result.

Therefore local compatibility is sufficient for global Road compatibility, provided all maps are typed and composable.

## 12. Corollary TR-3A — QFT/GR common ancestry is transport-stable under the naturality hypotheses

If both QFT and GR naturality squares commute along a Road and

\[
(q_0,g_0)\in\mathcal R_{QG,p_0},
\]

then the transported pair

\[
(q_n,g_n)
=
(
U_Q(\Gamma)q_0,
U_G(\Gamma)g_0
)
\]

has common transported ancestry \(P_\Gamma(F_0)\), hence

\[
(q_n,g_n)\in\mathcal R_{QG,p_n}.
\]

This is a formal representation-compatibility theorem, not a proof that the physical maps \(U_Q,U_G\) have already been derived.

## 13. Failure predicate

A Road fails at the first segment for which any declared obligation fails:

\[
\operatorname{Fail}(\mathfrak R)
=
\min\{
i:
\operatorname{Adm}(\mathsf P_i)=0
\}.
\]

Failure classes include:

- unresolved target;
- chirality incompatibility;
- invariant-residue mismatch;
- persistent-identity failure;
- insufficient Resolution;
- insufficient Bandwidth;
- failed target closure;
- incomplete provenance;
- representation transport mismatch.

The correct response is to stop at the last verified Address, not invent the missing segment.

## 14. What has closed

The following are now one formal object:

\[
\boxed{
T_5
\supset
W_\Gamma
\supset
\{\mathsf P_i\}
\supset
\mathfrak R
}
\]

together with:

- Address typing;
- Portal transaction typing;
- Rainbow Road composition;
- persistent identity transport;
- projection/readout equivalence;
- History preservation;
- QFT/GR local common ancestry;
- conditional Road-wise representation naturality.

## 15. What remains open

The main open physics objects are:

\[
\boxed{
U_Q(\Gamma),\qquad U_G(\Gamma)
}
\]

as actual derived readable transport laws.

Also open:
- exact physical generator/connection for horizontal chirality transport;
- full typing of the horizontal/vertical chirality connection split;
- quantitative Resolution/Bandwidth capacities;
- physical interpretation of color-indexed routing;
- experimental validation.

These are not required to keep the present transport architecture as a recoverable formal model.
