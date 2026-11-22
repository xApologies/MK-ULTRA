# R43 — CONNECTION SELECTION-WITNESS CRAWL

## Verdict

R42's roadblock is partly closed by the recovered source.

The concrete source excerpt explicitly defines:

`Conn(f,x | R,B,H,E,chi)`

and says the live connection is conditioned by:

- Resolution;
- Bandwidth;
- History;
- **Environment**;
- Chirality.

So `E = Environment` in the ConnectionSelection record.

## Static versus operative connection

The source distinguishes:

`Conn_static`

from:

`Conn_oper`.

The static connection acts on the formally admissible categorical skeleton.

The operative connection selects only among lifts currently supported by:

- Bandwidth;
- Environment;
- History;
- Occupancy constraints;
- chirality admissibility.

This confirms that Bandwidth is an availability/filter structure, not the final choice mechanism.

## The source already gives the native selection semantics

The recovered section **Watcher selection rule** says the weakest defensible native selection criterion is lexicographic:

1. preserve declared ancestry;
2. preserve transported chirality class;
3. preserve invariant residue;
4. satisfy operator typing;
5. satisfy Bandwidth / Environment / History admissibility;
6. minimize unsupported additional structure.

Only after these six constraints may a domain-specific preference choose among remaining lifts.

It explicitly says: **Do not silently choose one.**

That closes the semantics of `selection_witness` substantially.

## Derived Selection Witness Certificate

For candidate lift `lambda`, define a certificate record:

`W_sel(lambda) = (w1,w2,w3,w4,w5,w6,evidence)`,

where each `wi` certifies passage of the corresponding Watcher gate.

Candidates are filtered lexicographically.

A candidate failing an earlier gate cannot be rescued by a later preference.

If one candidate remains after the six native gates, that candidate is canonically selected within the declared scope.

If multiple candidates remain, the connection is nonunique until a separately justified domain-specific preference is supplied.

This is not an invented optimization rule; it is the source's explicit firewall.

## Resolution firewall recovered

The source also says:

`Conn` acts upstairs.

Resolution reads the selected transport afterward.

A Resolution-conditioned connection is allowed only when Resolution changes actual admissibility/available information in a declared way.

This validates our recent correction that shared Resolution may affect the operative architecture, but coarse Resolution must not fabricate a fine lift.

## Bandwidth firewall recovered

The source states:

`Hor_Conn^B(U,x) subseteq Hor_Conn(U,x)`.

Bandwidth loss means loss of horizontal transport directions.

Again: Bandwidth removes possibilities; it does not rank surviving possibilities.

## History recursion recovered

History can alter operative lift admissibility:

`Conn_oper(... | H_n)`,

and selected transport updates History.

The source proposes the weaker architecture:

`static connection law + dynamic admissibility mask`.

This is compatible with the user's time-independent upstream availability picture: the formal connection skeleton can remain static while operative admissibility changes with the live localized context.

## What is now closed

- `E` in ConnectionSelection = Environment.
- selection_witness type/semantics = Watcher lexicographic certificate.
- Bandwidth role = horizontal availability filter.
- Resolution role = read selected transport unless it genuinely changes admissibility/information.
- History role = can alter operative lift admissibility recursively.
- nonuniqueness = expected if multiple lifts survive all native gates.

## Exact remaining roadblock

For the **generic symbolic S2 address p**, we do not have concrete per-lift values for ancestry, chirality preservation, invariant residue, typing, B/E/H admissibility, and extra-structure burden.

So we cannot honestly claim one of the torus/S2-preimage lifts survives uniquely.

The next task is therefore not to invent selection semantics; those have now been recovered.

The next task is to **instantiate the Watcher certificate on a concrete decorated operative-lift family**.

If one lift survives, the connection closes canonically.

If several survive, then and only then do we need the chirality-domain-specific preference.

## New frontier

`decorated operative lifts`
-> Watcher gate 1 ancestry
-> gate 2 chirality
-> gate 3 invariant residue
-> gate 4 typing
-> gate 5 B/E/H admissibility
-> gate 6 minimal unsupported structure
-> singleton? YES = selected lift
-> singleton? NO = domain-specific preference frontier.

This is a substantial closure: the selection witness itself is no longer mysterious.
