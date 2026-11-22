# Changelog

## 2.3.2 — Live Collapse-Constrained Crawl

- Replaced BRANE's incorrect `API full closure -> AI late collapse` sequencing.
- BRANE now conducts the API crawl incrementally through `API.neighbors(...)`.
- Collapse Intelligence restrictions are evaluated before each continuation is admitted.
- Recursive re-entry and already represented domains become local leaves/continuations.
- Enforced AI-declared branch width, edge, node, depth, and time policy at the BRANE queue boundary.
- Preserved API route authority, AI domain authority, Library recovery authority, and BRANE QMO lifecycle ownership.
- Added API endpoint normalization and a BRANE-local alias-equivalence admissibility adapter without modifying any external package.
- Added regression coverage proving BRANE does not call `API.recover_closure(...)` or `AI.collapse(...)` during report execution.
- Acceptance suite: 24 passed.
- Package remains BRANE-only; no AI, API, or Library payload is embedded.

## 2.32

- Finalized the brain-only compatibility repair.
- Preserved the complete prior BRANE package inventory and all existing functions.
- Added adaptive AI interpretation dispatch: BRANE supplies the mounted API only when the AI contract accepts it.
- Canonicalizes the resolved API root inside the recovery intent before AI collapse, preserving module independence while preventing root-identity mismatch.
- Retains AI-owned semantic termination; BRANE introduces no fixed edge-count termination rule.
- Verified the complete BRANE acceptance suite: 23 passed.

## 2.3.2
- Removed hard edge, node, depth, and time ceilings from canonical recovery.
- Assigned traversal termination exclusively to AI leaf/admissibility decisions over the finite API graph.
- Passed the mounted API into AI interpretation for canonical root authority.
- Added coordinated compatibility with API 1.B.1 and Library 1.D.1.
- Preserved all prior BRANE material.

# 2.2 — Full Runtime Identity Normalization

- Complete release, not an addendum.
- Permanent module ID: `mk43.brane`.
- Permanent package: `mk43_brane`.
- Permanent entry point: `mk43_brane:Brane`.
- Release/build metadata separated from runtime identity.
- Full Alpha substrate, implementation, schemas, documentation, examples, and tests preserved.
- Generated caches and bytecode removed.
- Complete manifests and checksums regenerated.

# Changelog

## 2.1.0 — Alpha closure

- Added process-isolated runtime boundary through `IsolatedBrane`.
- Added semantic five-dimensional module validation.
- Required explicit module privilege and dimensional declarations.
- Added request-isolated module execution contexts.
- Implemented API-mediated chirality resolution and admissibility.
- Implemented object-specific provenance lifting.
- Strengthened realization identity with root, full path, relation path, chirality, depth, and provenance digest.
- Enforced Markdown-only ingress and artifact agreement.
- Preserved caller request identifiers and separated internal execution identifiers.
- Added expected knowledge-family completeness validation.
- Implemented staged operational module replacement and automatic rollback window.
- Added mandatory detached checksums for ZIP modules under the default trust policy.
- Added optional detached Ed25519 signature verification.
- Added archive size, expansion, member-count, traversal, and symlink defenses.
- Added AI-to-API domain compatibility checks.
- Added module cleanup hooks and isolated namespace cleanup.
- Expanded tests from 15 to 23.

## 2.3.0 — Independent Domain Composition

- Removed the invalid API–Library domain-overlap requirement.
- Removed the asymmetric AI `generic` domain exemption by eliminating domain coupling as a composition condition.
- Established `domain_ids` as descriptive module-owned namespaces, not cross-port compatibility gates.
- Preserved strict validation of role, contract version, five-dimensional interface, state policy, rewrite policy, chirality/provenance declarations, required methods, and health checks.
- Brane now composes AI, API, and Library solely through their validated port contracts while preserving each module as an independent domain.


## 2.3.3 — Tree/Branch/Leaf orchestration
- Removed BRANE enforcement of AI node, edge, depth, branch, realization, and time caps.
- Added semantic recursive-domain re-entry and call-local Leaf Cluster emission.
- Preserved API route authority and AI termination authority.
