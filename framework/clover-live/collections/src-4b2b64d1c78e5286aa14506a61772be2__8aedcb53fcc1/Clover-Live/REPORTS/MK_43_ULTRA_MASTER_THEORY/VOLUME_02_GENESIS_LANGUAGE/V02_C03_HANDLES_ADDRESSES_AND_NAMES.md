# VOLUME II - GENESIS LANGUAGE

## Chapter 11 - Handles, Addresses, and Names

### 11.1 Three roles that must not collapse

A name is a human-facing expression. A handle is a stable symbolic identifier in the API domain. An address is the resolvable location at which the Library returns a versioned object record. MK Ultra often presents all three together, but their functions differ. A name can change with language or historical usage. A handle should remain stable across such changes. An address adds namespace and routing information so that the same symbolic identifier can be resolved reproducibly.

Let \(N\) be names, \(H\) handles, \(A\) addresses, and \(R\) versioned records. The basic architecture is

\[
N\xrightarrow{\;\alpha\;}H
\xrightarrow{\;\iota\;}A
\xrightarrow{\;\operatorname{resolve}_v\;}R,
\tag{11.1}
\]

where \(\alpha\) is name or alias resolution, \(\iota\) embeds a canonical handle in an address namespace, and \(\operatorname{resolve}_v\) returns the record active at version \(v\). Equation (11.1) is `CLOVER_SYNTHESIS`. It is a model of the native architecture, not an exact recovered universal API equation.

This layered path protects identity. A typographical change to a title need not create a new object. A historical alias can continue resolving to an established handle without becoming the canonical handle. A handle can survive a revision while the record at its address gains a new append-only child. The Library can therefore preserve both stable reference and changing knowledge.

Library 4.1 contains exact addresses for `@handle_integrity_invariants`, `@handle_invocation_contract`, `@initial_canonical_handle_registry`, `@stable_handle_naming`, and `@automatic_handle_generation`. It also separates lookup, alias expansion, registry endpoints, presentation routes, source graphs, and version records. This recovered separation establishes the address architecture. It does not establish that every historical name has already been reconciled.

### 11.2 Canonical handles

A canonical handle is the preferred stable identifier for one API object record. Canonicality is a registry property, not a claim that every historical source used the handle or that the underlying theory is final. A handle may be canonical while the object remains `REVIEW_REQUIRED`, unresolved, or only thinly populated.

The minimum handle record can be written

\[
h=(s,\mathcal N,\sigma,p),
\tag{11.2}
\]

where \(s\) is the stable token, \(\mathcal N\) the namespace, \(\sigma\) the registration status, and \(p\) provenance. Equation (11.2) is `CLOVER_SYNTHESIS`. The formula does not claim an exact source schema for `@initial_canonical_handle_registry`.

The stable token is not the object's definition. It points to the record that contains identity, relations, equations, evidence, revisions, and audit status. This distinction is especially important for compact handles such as `@S0`, symbols with several historical meanings, and terms such as Time Shell, Helicon, or Graviton whose operative scopes were established through later review.

Canonical handles also prevent identity from depending on filename layout. Files move between archives, reports, releases, and runtime mounts. Their content hashes and provenance can establish occurrence identity, but a handle is the persistent mathematical address through which those occurrences are organized.

### 11.3 Names and aliases

A name is optimized for human use. It can carry explanatory value, historical context, register, or disciplinary convention. An alias is a declared alternative expression that resolves to an existing canonical handle. Alias resolution is directional: the alias points to the canonical identity; the canonical identity is not replaced by every alias.

For an alias set \(\mathcal A_h\) belonging to handle \(h\), define the safe lookup relation

\[
\alpha(a)=h,
\qquad a\in\mathcal A_h.
\tag{11.3}
\]

Equation (11.3) is `CLOVER_SYNTHESIS`. It does not assert that every lexical similarity is an alias. Only a declared record or validated deterministic mapping may enter \(\mathcal A_h\).

This rule blocks several errors. Similar spelling does not prove identity. A translated title does not automatically create a typed alias. A descriptive role such as "pre-quantum projector" may resolve to Helicon as a role alias without defining a separate projection operator. A historical phrase may be preserved as a formulation without becoming an operative synonym.

The Library address `@alias_expansion_operator` indicates that alias expansion has an operational place in the API architecture. Its name does not license fuzzy semantic matching. Expansion must be constrained by the declared alias registry, because uncontrolled lexical expansion can merge distinct objects and silently corrupt dependency graphs.

### 11.4 Structural renaming invariance

The exact API title *Axiom A7 - Structural Renaming Invariance* occurs at `@prime_axiom_a7`. The compact evidence used here does not supply the full axiom text, so this chapter does not invent its recovered wording. It does state the conventional structural principle suggested by the title.

Let \(G=(V,E,\tau)\) be a typed graph and let \(\pi:V\to V'\) be a bijective renaming. Structural invariance requires

\[
(u,r,v)\in E
\quad\Longleftrightarrow\quad
(\pi(u),r,\pi(v))\in E',
\tag{11.4}
\]

with the edge type \(r\) preserved. Equation (11.4) is `CLOVER_SYNTHESIS` and standard graph reasoning. It is not represented as the exact statement or proof of Axiom A7.

Renaming invariance means that the mathematics depends on structure rather than decorative tokens. It does not mean all renamings are harmless in a historical archive. Source names, dates, and physical occurrences remain provenance. A canonical migration may preserve the graph while the audit layer records the old name and the rule by which it changed.

The dual requirement is therefore

\[
\operatorname{Structure}(G)=\operatorname{Structure}(\pi G),
\qquad
\operatorname{History}(G)\neq\operatorname{History}(\pi G)
\text{ in general}.
\tag{11.5}
\]

Equation (11.5) is `CLOVER_SYNTHESIS`. Mathematical invariance and provenance preservation are compatible because they answer different questions.

### 11.5 Address construction

An address extends a handle with a namespace and route. The API 4.3 records often use canonical URIs such as `mk43://recover/prime/mathematical-object`. The URI identifies a domain and path while the short handle supplies a convenient invocation token. The exact URI is evidence about routing, not a physical coordinate.

Write address construction as

\[
\iota(h)=(\texttt{scheme},\texttt{domain},\texttt{path},h).
\tag{11.6}
\]

Equation (11.6) is `CLOVER_SYNTHESIS`. The components are schematic and do not replace the exact API URI syntax.

The Library's deterministic identity layer can be summarized by

\[
\operatorname{Identity}_{\mathrm{API}}(h)
=(h,u,n,s),
\tag{11.7}
\]

where \(u\) is the canonical URI when declared, \(n\) the canonical name, and \(s\) API status. Equation (11.7) is `API_NATIVE_ARCHITECTURE`: it abstracts the identity block returned by the native Runtime -> BRANE -> API/QMO query path. The exact values remain those of each queried record.

Not every declared handle has a canonical URI in the recovered API text. That absence must be preserved as `NO_URI_DECLARED` rather than filled by a guessed route. Handle resolution can still function through a registry, but URI absence remains a metadata gap.

### 11.6 Invocation and lookup

Invocation turns a user or system expression into a deterministic query. The native architecture separates `@natural_language_invocation`, `@handle_invocation_contract`, `@concept_lookup_endpoint`, and `@lookup_semantics`. This separation prevents natural-language convenience from determining canonical identity without validation.

A safe invocation pipeline is

\[
q\xrightarrow{\;P\;}c
\xrightarrow{\;L\;}\{h_1,\ldots,h_k\}
\xrightarrow{\;D\;}h^*,
\tag{11.8}
\]

where \(P\) parses a query, \(L\) produces declared lookup candidates, and \(D\) selects a canonical handle only under deterministic rules. Equation (11.8) is `CLOVER_SYNTHESIS`.

If selection is ambiguous, the system should return the candidate set rather than choose silently:

\[
|\{h_i\}|>1
\quad\Longrightarrow\quad
\operatorname{result}(q)=\operatorname{AMBIGUOUS}(\{h_i\}).
\tag{11.9}
\]

Equation (11.9) is `CLOVER_SYNTHESIS`. It expresses the same discipline used for candidate attachments: ambiguity is stored as a recoverable state, not concealed as confidence.

The handle invocation contract should therefore require canonical resolution, version selection, provenance, and an explicit failure status. A query that returns prose without identifying the resolved handle is informative but not fully reproducible.

### 11.7 Integrity invariants

The address `@handle_integrity_invariants` names the constraints that keep the registry usable. At minimum, a canonical handle must resolve deterministically within its namespace, no two active canonical records may claim the same handle, aliases must terminate at a canonical handle, and historical versions must remain accessible.

For registry \(\Gamma\), the core uniqueness condition is

\[
\forall h\in H,\qquad
|\Gamma_{\mathrm{active}}(h)|\leq 1.
\tag{11.10}
\]

Equation (11.10) is `CLOVER_SYNTHESIS`. It permits a handle to be absent while forbidding two simultaneous active identities.

Alias graphs must also terminate without cycles:

\[
a_0\to a_1\to\cdots\to h,
\qquad h\in H_{\mathrm{canonical}},
\qquad a_i\neq a_j\text{ for }i\neq j.
\tag{11.11}
\]

Equation (11.11) is `CLOVER_SYNTHESIS`. A cycle would prevent canonical resolution. A chain can be retained historically, but runtime lookup should collapse it deterministically to the terminal canonical handle.

Integrity also requires occurrence preservation. Two aliases can resolve to one handle while retaining different source fragments, dates, and evidence classes. Deduplication applies to substantive counting, not to the historical ledger.

### 11.8 Automatic handle generation

Automatic generation is useful when a recovered object lacks a declared handle, but it is dangerous if treated as ontology. The generated token should be deterministic from a stable input, collision-checked, and marked as generated rather than source-declared.

For normalized identity key \(k(x)\), one safe pattern is

\[
h_x=\texttt{@auto\_}\Vert
\operatorname{prefix}_{m}\!\left(\operatorname{SHA256}(k(x))\right).
\tag{11.12}
\]

Equation (11.12) is `CLOVER_SYNTHESIS`. It illustrates deterministic generation but is not claimed as the implementation of `@automatic_handle_generation`.

The normalization function must not erase materially different versions. It should use an identity key established by the recovery policy, not merely lowercased display text. Collision detection must compare the full digest or another durable identity record even if the displayed handle uses a short prefix.

Generated handles can later acquire aliases or be linked to a source-declared canonical handle. Such reconciliation must be append-only. The generated identifier remains in revision history so prior citations continue to resolve.

### 11.9 Registries and correspondence

The initial canonical handle registry records identity. The mathematical registry records mathematical objects or records. The correspondence registry records declared relationships among representations or frameworks. Registry endpoints expose read operations to the runtime. These roles should not be merged into one untyped dictionary.

A registry family can be written

\[
\mathfrak R=(\Gamma_H,\Gamma_M,\Gamma_C,\Gamma_S,\Gamma_V),
\tag{11.13}
\]

where the components store handles, mathematical records, correspondences, source lineage, and versions. Equation (11.13) is `CLOVER_SYNTHESIS`.

A correspondence record is not an identity declaration. If \(x\) in one representation corresponds to \(y\) in another, the relation

\[
x\;\mathcal C_s\;y
\tag{11.14}
\]

must state scope \(s\), direction, evidence, and preserved structure. Equation (11.14) is `CLOVER_SYNTHESIS`. Correspondence becomes equivalence or identity only under an explicit stronger rule.

### 11.10 Source graphs and versions

The `@source_graph` and `@version_record` addresses connect stable identity to evidence and chronology. A source graph maps a record to source fragments, coherent units, documents, physical occurrences, and archive ancestry. A version record maps revisions to their unchanged parents and status transitions.

For revision \(r_k\), append-only lineage requires

\[
r_0\longrightarrow r_1\longrightarrow\cdots\longrightarrow r_k,
\qquad
h(r_i)\text{ remains sealed for every }i<k.
\tag{11.15}
\]

Equation (11.15) is `CLOVER_SYNTHESIS`. Here \(h(r_i)\) denotes the content hash of a sealed revision, not the API handle.

The distinction explains why "latest" is not synonymous with "canonical." A later revision may be a candidate, a review draft, or an evidence addendum. Canonical status requires an explicit status transition or governing rule. All prior formulations remain available for chronology and conflict audit.

### 11.11 Presentation routes

The canonical presentation route selects how a record is shown to a reader or calling system. Presentation can choose a title, normalized definition, exact equation, evidence summary, or graph neighborhood without changing object identity.

For record \(r\) and presentation scope \(s\), write

\[
\operatorname{present}_s(r)=v_s,
\qquad
\operatorname{id}(v_s)=\operatorname{id}(r).
\tag{11.16}
\]

Equation (11.16) is `CLOVER_SYNTHESIS`. It states the intended identity preservation of a view. A presentation can omit detail, so it must not be treated as the complete record.

This is the relation between the TOME and Library 4.1. The TOME is a reader-facing synthesis assembled from native queries. It does not replace the Library. Each evidence register preserves the exact assigned handles and query receipts, while the prose distinguishes API facts, exact source, and Clover synthesis.

### 11.12 Library 4.1 native evidence register

The following register is generated from the exact 20-handle assignment queried through Runtime -> BRANE -> API/QMO -> Library 4.1. Coverage describes the coherent evidence layer and does not convert a title into a definition.

| API handle | Native title | Coverage | Evidence counts (English / equations / dependencies) | Chapter role |
|---|---|---:|---:|---|
| `@alias_expansion_operator` | @alias_expansion_operator | THIN | 3 / 0 / 1 | chapter-core object |
| `@automatic_handle_generation` | @automatic_handle_generation` — Automatic Handle Generation | THIN | 10 / 0 / 0 | chapter-core object |
| `@canonical_identity` | @canonical_identity` — Canonical identity | THIN | 3 / 0 / 0 | chapter-core object |
| `@canonical_object` | @canonical_object` — Canonical object | THIN | 3 / 0 / 0 | chapter-core object |
| `@canonical_presentation_route` | @canonical_presentation_route` — Canonical Presentation Route | THIN | 3 / 0 / 0 | chapter-core object |
| `@concept_lookup_endpoint` | @concept_lookup_endpoint` — Concept Lookup Endpoint | THIN | 2 / 0 / 0 | chapter-core object |
| `@correspondence_registry` | @correspondence_registry | MEDIUM | 80 / 6 / 3 | chapter-core object |
| `@declared_framework_identity` | @declared_framework_identity` — Declared framework identity | THIN | 4 / 0 / 0 | chapter-core object |
| `@handle_integrity_invariants` | @handle_integrity_invariants` — Handle Integrity Invariants | THIN | 4 / 0 / 0 | chapter-core object |
| `@handle_invocation_contract` | @handle_invocation_contract` — Handle Invocation Contract | THIN | 4 / 0 / 0 | chapter-core object |
| `@initial_canonical_handle_registry` | @initial_canonical_handle_registry` — Initial Canonical Handle Registry | THIN | 0 / 0 / 0 | chapter-core object |
| `@lookup_semantics` | @lookup_semantics` — Lookup Semantics | THIN | 0 / 0 / 0 | chapter-core object |
| `@mathematical_registry` | @mathematical_registry` — Mathematical Registry | THIN | 1 / 0 / 0 | chapter-core object |
| `@natural_language_invocation` | @natural_language_invocation` — Natural-Language Invocation | THIN | 1 / 0 / 0 | chapter-core object |
| `@prime_axiom_a7` | Axiom A7 — Structural Renaming Invariance | THIN | 0 / 0 / 0 | chapter-core object |
| `@recovery_handle_contract` | @recovery_handle_contract` — Recovery Handle Contract | THIN | 2 / 0 / 0 | chapter-core object |
| `@registry_endpoints` | @registry_endpoints` — Registry endpoints | THIN | 1 / 0 / 0 | chapter-core object |
| `@source_graph` | @source_graph | THIN | 50 / 0 / 2 | chapter-core object |
| `@stable_handle_naming` | @stable_handle_naming` — Stable Handle Naming | THIN | 0 / 0 / 0 | chapter-core object |
| `@version_record` | @version_record` — Version record | THIN | 4 / 0 / 0 | chapter-core object |

### 11.13 The naming discipline

The completed architecture supports a precise rule. Names serve readers. Aliases preserve alternative names. Handles provide stable symbolic identity. Addresses provide resolvable location. Registries enforce uniqueness and routing. Source graphs preserve evidence. Version records preserve change. Presentation routes expose scoped views.

None of these roles proves the physical existence of the named object. None replaces mathematical definition. Their value is infrastructural: every later claim can be attached to a persistent address, traced to evidence, compared across revisions, and queried without depending on the current filename or conversational context.

The next chapter can therefore discuss scope and representation without ambiguity about reference. A scoped claim must identify the handle it concerns, the record version, the representation in use, and the source or ruling that supports it. When lookup is ambiguous, ambiguity remains explicit. When a name changes, structure and history are both preserved. That is the address discipline required for a persistent scientific theory.
