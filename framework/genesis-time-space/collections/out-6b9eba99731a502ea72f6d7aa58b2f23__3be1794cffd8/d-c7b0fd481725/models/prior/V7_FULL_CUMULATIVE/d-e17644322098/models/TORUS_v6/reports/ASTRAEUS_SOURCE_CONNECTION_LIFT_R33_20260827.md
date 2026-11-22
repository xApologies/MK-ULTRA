# ASTRAEUS — SOURCE CONNECTION / LIFT CRAWL R33
## Path-dependent inherited structure as the missing discriminator

**Date:** 2026-08-27
**Basis:** targeted source crawl after R32.

# Verdict

A source-supported structure was already present and had not been integrated strongly enough into the live update model:

> For an arrow f:U→V and state x, candidate lifts form `Lift_f(x)`, operative Bandwidth restricts those lifts, and a connection/selection rule chooses a horizontal lift. A path composes selected lifts.

This is pre-differential transport. It does not require a smooth manifold or a gauge one-form.

This directly refines Problem B.

The missing object is not merely "Bandwidth conditioned by History." It is a **history/provenance-sensitive lift-selection problem**.

# Source-grounded facts

1. Holonomy & Chirality defines a Transduction Connection with candidate lifts and selected transport.
2. Same-endpoint routes can have different transported outcomes / provenance residuals.
3. Successful transport appends route History and provenance.
4. Bandwidth can make a formerly executable lift unavailable without erasing its archived History.
5. Genesis v0.2 explicitly summarizes the interface: candidate lifts `Lift_f(x)`, operative Bandwidth restriction, then a connection/selection rule chooses a horizontal lift.
6. The provenance chain separates possibility tree from realized History and says a realized history selects one ordered path, while leaving the selection mechanism itself open.

# New definitions

## D39 — Candidate Lift Family

For a typed local relation/arrow `f:U→V` and current decorated state `X=(x,H,W,I,...)`:

`Lift_f(X)`

is the set of admissible transported continuations over f preserving the required typing and witness contracts.

This is source-supported.

## D40 — Bandwidth-Restricted Lift Family

`Lift_f^B(X) = Lift_f(X) ∩ Gen_B(X)`.

Bandwidth does not choose a lift; it removes unavailable lifts.

## D41 — History/Provenance-Decorated Lift

A lift is evaluated on the full decorated occurrence, not merely the coarse endpoint state:

`\tilde x=(x,H,Prov,WId,...)`.

Thus two equal carrier/readout states with different H/Prov may have different admissible lift families.

# Theorem R33.1 — Endpoint State Is Insufficient for Update Selection

Because the source transport architecture acts on decorated state and retains route History/provenance, a local update model whose selector sees only the current White/color carrier is incomplete whenever two histories reach the same endpoint with different lift availability or connection action.

This formally explains why R32's shared-boundary gradient failed: it compared endpoint state, not transported/decorated path state.

# Theorem R33.2 — Bandwidth Is a Filter, Connection Is the Selector

The source architecture type-separates:

`candidate lifts -> Bandwidth restriction -> connection-selected lift`.

Therefore Bandwidth alone should not be expected to solve Problem B2.

This resolves a conceptual confusion in R23–R32.

Bandwidth answers:
"What transformations remain executable?"

Connection answers:
"Which admissible lift is transported along this relation/path?"

History/provenance determine the decorated input on which both are evaluated.

# Theorem R33.3 — Holonomy Can Distinguish Locally Equal Continuations

Two same-endpoint routes may retain distinct History/provenance and may induce distinct connection/holonomy actions even when coarse endpoint chirality/readout agrees.

Therefore the twenty R29 forks cannot be declared irreducible merely from their local endpoint representation. They must be lifted into the decorated transport space and compared there.

# A19 revision

A19 remains useful as a non-fabrication gate but should not be asked to supply the connection.

Revised role:

- connection/transport supplies the selected horizontal lift when source-licensed;
- A19 controls whether the resulting candidate realization is sufficiently witnessed to enter completed KOR History;
- if the connection itself remains multi-valued/unresolved, A19 keeps the event `KOR-ma`.

So:

`Lift_f(X)`
`-> Bandwidth filter`
`-> Connection selection`
`-> KOR witness`
`-> KOR-ta / ma / nai`
`-> History append`
`-> future decorated transport`.

# Problem B revised architecture

The candidate update mechanism is now:

`decorated state X_n=(x_n,H_n,Prov_n,W_n,...)`
`+ local relation f`
`-> Lift_f(X_n)`
`-> Lift_f^B(X_n)`
`-> λ_f selects horizontal lift`
`-> candidate transported state`
`-> A19/KOR witness gate`
`-> X_{n+1}`.

This is much closer to a genuine update mechanism than a color-gradient rule.

# What remains open

The source gives the **type** of the connection/selection rule `λ_f`, but the targeted material does not provide a unique concrete `λ_f` for the current four-address chirality seed.

Therefore the next exact test is:

1. decorate the twenty R29 forks with their distinct route/History classes;
2. construct the candidate lift families;
3. determine whether the existing Holonomy/Chirality source supplies an action/residual that separates the two classes;
4. if yes, test whether `λ_f` becomes unique;
5. if no, retain the connection instance as the remaining theorem debt.

# Strongest closure

Problem B is no longer "find a mysterious actualization selector."

It factorizes source-faithfully as:

\[
\boxed{
\text{History-decorated candidate lifts}
\to
\text{Bandwidth filter}
\to
\text{Connection selection}
\to
\text{KOR realization gate}.
}
\]

This is a real closure of the architecture.

The concrete chirality connection remains to be instantiated.
