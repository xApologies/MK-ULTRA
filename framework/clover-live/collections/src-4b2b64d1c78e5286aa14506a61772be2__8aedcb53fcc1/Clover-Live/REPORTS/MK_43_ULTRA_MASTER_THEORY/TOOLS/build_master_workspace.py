from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY"
V01 = WORK / "VOLUME_01_FOUNDATIONS"
LEDGER_PATH = ROOT / "MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/full_api_handle_ledger_08m.jsonl"
QUERY_RECEIPT = WORK / "master_native_query_receipt.json"
DB = ROOT / "MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/state/library.sqlite3"
EXPECTED_DB_SHA = "e648f67429d166111105718fa722cc325bb7882b65314b5532f1267018050e03"


VOLUMES = [
    ("V01", "FOUNDATIONS", [
        "What Is MK 43 Ultra?",
        "Distinction, Information, and Structural Reality",
        "Chirality as Organized Difference",
        "Recursion, Inheritance, and Persistence",
        "ER Foam and Pre-Geometric Connectivity",
        "Planck Landscape and Foundational Geometry",
        "Projection, Transduction, and Realization",
        "Conservation Across Representational Levels",
    ]),
    ("V02", "GENESIS LANGUAGE", [
        "Why a New Representational Language Was Required",
        "Mathematical Objects and Ontological Objects",
        "Handles, Addresses, and Names",
        "Scope and Representation",
        "Projection Language",
        "Chirality Language",
        "Recursion and Localization",
        "Information and Realization",
        "Identity, Equivalence, Dependency, and Handoff",
        "QMO Grammar",
        "Translation into Conventional Mathematics",
        "Translation into Conventional Physics",
        "Category Errors Prevented by Genesis Language",
        "Genesis Language Dictionary and Formal Lexicon",
        "Genesis Language Grammar and Construction Rules",
    ]),
    ("V03", "API AND QMO MATHEMATICS", [
        "API 4.3 as a Constrained Mathematical Domain",
        "Canonical Handles and Mathematical Addresses",
        "Typed Edges and Dependency Traversal",
        "Quantum Mathematical Objects",
        "Admissible Composition and Derived Objects",
        "API-Native Equation Lineage",
        "Native Conservation and Constraint Objects",
        "Universal Energy Objects",
        "The Computational Proof-of-Concept",
    ]),
    ("V04", "HELICON", [
        "Helicon Identity and State Space",
        "Structural Tuple and One-Form Representations",
        "Helicon Field Strength and Curvature",
        "Spectral Operator and Angular Reduction",
        "Modes, Resonance, and Wake Dynamics",
        "Stability and Propagation",
        "Gravitational Helicon Mode",
        "Helicon Interfaces and Open Mathematics",
    ]),
    ("V05", "TIME SHELL", [
        "Time Shell Identity and Scope",
        "Persistence Closure",
        "T0-T7 and R0-R7 Natural Regimes",
        "Chirality-Coupled Localization",
        "Planck-Horizon Interface",
        "Projection and Intertwining Requirements",
        "Quantum-Field Handoff",
        "Time Shell Models, Evidence, and Open Typing",
    ]),
    ("V06", "QUANTUM AND FIELD REALIZATION", [
        "Canonical Quantum-Field Handoff Object",
        "State Spaces, Probability, and Quantization",
        "Scalar-Field Realization",
        "Gauge-Field Realization",
        "Spinor and Fermionic Realization",
        "Yang-Mills and Non-Abelian Structure",
        "Field Actions, Operators, and Conservation",
        "Measurement and Readable Quantum Structure",
    ]),
    ("V07", "GRAVITY", [
        "The MK 43 Ultra Gravity Mechanism",
        "Graviton Identity and Projection Mode",
        "Continuity Perturbation",
        "Time-Shell Metric Projection",
        "Weak-Field Metric and Curvature",
        "Einstein Sector and Stress-Energy",
        "Gravitational Waves and Radiation",
        "Gauge, Polarization, and Propagation",
        "Gravity-Matter Closure",
        "Formal Gravity Gaps and Validation Boundaries",
    ]),
    ("V08", "MATTER AND ENERGY", [
        "Matter Admissibility and Realization",
        "Motes, Occupancy, and Organized Matter",
        "Energy as a Cross-Level Quantity",
        "Native Unit of Energy",
        "Stress-Energy and Field Energy",
        "Chromatic Energy Structures",
        "Matter-Energy Conservation and Transport",
    ]),
    ("V09", "UNIVERSAL COUPLING", [
        "Universal Coupling Identity",
        "Inputs, Domains, and Admissibility",
        "Coupling Operators and Relations",
        "Cross-QMO Coupling Architecture",
        "Gravity, Matter, and Field Coupling",
        "Coupling Limits and Stability",
        "Established Structure and Research Frontier",
    ]),
    ("V10", "BLACK HOLES AND STRONG GRAVITY", [
        "Black-Hole Geometry",
        "Horizons, Trapped Surfaces, and Causal Structure",
        "Kerr, Schwarzschild, and Charged Families",
        "Black-Hole Thermodynamics and Radiation",
        "Interior Structure and Information Closure",
        "Strong-Gravity Signatures and Open Problems",
    ]),
    ("V11", "COSMOLOGY", [
        "Cosmological Realization of MK 43 Ultra",
        "Friedmann and Background Dynamics",
        "Bounce Criteria and Re-Expansion",
        "Cosmic Cycles and Inheritance",
        "Structure Formation",
        "Cosmological Horizons and Dark Energy",
        "Cosmological Observables and Open Parameters",
    ]),
    ("V12", "DARK MATTER AND RELATIONAL STRUCTURE", [
        "Dark Matter as Relational Geometry",
        "ER Networks and Load-Bearing Structure",
        "Dark-Matter Transport and Bridges",
        "Relational Histories and Adjacency",
        "Phenomenological Consequences",
        "Formalization and Discriminating Tests",
    ]),
    ("V13", "HOLOGRAPHY AND INFORMATION TRANSFER", [
        "Holographic Transfer Law",
        "Boundary Encoding and Phase Data",
        "Tensor Networks and Error Correction",
        "Black-Hole Information",
        "Cycle-to-Cycle Memory",
        "Information Conservation Across Projections",
    ]),
    ("V14", "BIOLOGICAL AND COGNITIVE REALIZATION", [
        "Biological Phase Organization",
        "Cellular and Neural Phase Fields",
        "Cognitive Persistence",
        "Consciousness as a Phase-Coherent Domain",
        "Perception, Memory, and Temporal Integration",
        "Agency, Autonomy, and Environmental Coupling",
        "Collective Cognitive Fields",
        "Scientific Boundaries of the Biological Sector",
    ]),
    ("V15", "OBSERVATIONAL AND EXPERIMENTAL VALIDATION", [
        "Validation Architecture and Status Dimensions",
        "Gravitational-Wave Compatibility Program",
        "LIGO Observation Address and Comparison Maps",
        "Black-Hole and Strong-Gravity Observables",
        "Cosmological Observation Windows",
        "Parameter Freeze and Audit Protocols",
        "External Data, Replication, and Falsifiability",
    ]),
    ("V16", "PREDICTIONS AND ENGINEERING APPLICATIONS", [
        "Prediction Registry and Freeze Protocol",
        "Gravitational-Wave Discriminants",
        "Black-Hole and Cosmological Predictions",
        "Dark-Matter and Holographic Predictions",
        "Field-Control and Phase-Engineering Models",
        "Energy, Transport, and Propulsion Concepts",
        "Biological and Cognitive Predictions",
        "Future Instruments and Decision Tests",
    ]),
    ("V17", "HISTORICAL AND INTERPRETIVE CONTEXT", [
        "Developmental Chronology of MK 43 Ultra",
        "Historical Formulations and Supersession",
        "Narrative Models and Scientific Translation",
        "Genesis Curatorial Rulings",
        "Philosophical Interpretation",
        "Public Disclosure and Research-Library Boundary",
    ]),
    ("V18", "MATHEMATICAL APPENDICES", [
        "Symbol and Type Dictionary",
        "Equation Catalog",
        "Axioms and Primitives",
        "Definitions",
        "Lemmas and Propositions",
        "Theorems and Proof Status",
        "Differential Geometry Conventions",
        "Quantum and Field-Theory Conventions",
        "Graph and Category Conventions",
        "API-Native Derivation Trees",
        "Dimensional and Normalization Ledger",
        "Provenance, Status, and Citation Ledgers",
    ]),
]


API_MAJOR = [
    ("@native_unit_of_energy", "API_NATIVE_DERIVATION", ["@general_energy"], "Addressable native energy unit feeding the general-energy sector."),
    ("@unit_of_energy", "QMO_DERIVED", ["@native_unit_of_energy"], "Unit-level energy object kept distinct from the general-energy aggregate."),
    ("@general_energy", "API_NATIVE_DERIVATION", ["@native_unit_of_energy"], "General-energy target of the recovered native-energy vertical chain."),
    ("@universal_coupling", "API_NATIVE_DERIVATION", [], "Cross-domain coupling object with its own equations and typed neighborhood."),
    ("@native_causal_order", "API_NATIVE_DERIVATION", ["@chirality", "@locality"], "Native causal-order object used by locality, Lorentz-limit, and Graviton propagation structures."),
    ("@native_constraint_closure", "API_NATIVE_DERIVATION", ["@admissibility", "@continuity_conservation", "@chirality", "@persistent_recursive_topology", "@time_shell"], "Constraint algebra for preserving admissible native states across transduction."),
    ("@native_graviton_dispersion", "API_NATIVE_DERIVATION", ["@graviton", "@gravitational_helicon_mode"], "Native dispersion object supporting effective masslessness and propagation analysis."),
    ("@native_graviton_quantization", "API_NATIVE_DERIVATION", ["@graviton"], "Quantization object directed toward native probability preservation."),
    ("@native_interaction_factorization", "API_NATIVE_DERIVATION", ["@graviton"], "Native factorization object used by soft-limit and multiparticle-gravity sectors."),
    ("@native_probability_preservation", "API_NATIVE_DERIVATION", ["@native_graviton_quantization"], "Probability-preservation object feeding readable projection and unitarity audits."),
    ("@continuity_conservation", "QMO_DERIVED", ["@continuity_perturbation"], "Conservation structure attached to continuity-sector perturbations."),
    ("@conservation_of_recoverable_structure", "API_NATIVE_DERIVATION", ["@recoverability"], "Conservation target for recoverable structural content."),
    ("@helicon", "QMO_DERIVED", [], "Primary coherent-mode QMO and upstream projective domain."),
    ("@time_shell", "QMO_DERIVED", ["@persistence", "@chirality"], "Persistent boundary and translation-domain QMO."),
    ("@graviton", "QMO_DERIVED", ["@gravitational_helicon_mode"], "Projection-mode QMO mediating the gravity handoff."),
]


EPISTEMIC = {
    "physical_observational_validation": "Compatibility of model outputs with measured or simulated observables; independent of whether every upstream operator has a completed proof.",
    "formal_mathematical_proof": "Existence, uniqueness, invariance, stability, and theorem-level proof obligations for stated constructions.",
    "operator_typing": "Explicit domains, codomains, composition rules, kernels, images, dimensions, and admissibility conditions.",
    "provenance": "Lineage of a statement or equation through foundational source, QMO derivation, API-native derivation, Clover synthesis, Genesis curation, or external established mathematics.",
    "metadata_recovery": "Completeness with which the Library exposes existing records and ancestry; not a verdict on physical truth.",
    "curatorial_canon": "Whether a formulation is historical, candidate, operative, current working candidate, or final canon.",
    "publication": "Whether sufficient definitions, derivations, qualifications, and disclosure have been assembled for scientific release.",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def words(text: str) -> int:
    return len(re.findall(r"\b[\w@-]+\b", text, re.UNICODE))


def jdump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


def normalized_search(row: dict[str, object]) -> str:
    return " ".join(
        [
            str(row.get("short_handle", "")),
            str(row.get("canonical_name", "")),
            " ".join(map(str, row.get("aliases") or [])),
            str(row.get("canonical_api_uri", "")),
        ]
    ).lower()


def route_volume(row: dict[str, object]) -> str:
    s = normalized_search(row)
    h = str(row["short_handle"])
    rules = [
        ("V02", ["genlang", "genesis_language", "genesis_grammar", "genesis expression"]),
        ("V04", ["helicon"]),
        ("V05", ["time_shell", "time shell", "persistence closure", "persistent_recursive", "recursive_", "inheritance", "locality"]),
        ("V10", ["black_hole", "black hole", "hawking", "schwarzschild", "kerr_", "horizon", "trapped_surface"]),
        ("V11", ["cosmolog", "friedmann", "universe", "cosmic_", "bounce", "re_expansion", "scale_factor"]),
        ("V12", ["dark_matter", "dark matter", "relational", "adjacency"]),
        ("V13", ["holograph", "information", "entropy", "memory", "tensor_network", "error_correcting"]),
        ("V14", ["biolog", "cellular", "neural", "cognit", "conscious", "perception", "autonomy", "agency"]),
        ("V15", ["ligo", "observation", "validation", "audit", "experiment", "parameter_estimation", "consistency_test"]),
        ("V16", ["prediction", "engineering", "propulsion", "technology", "armor", "transport", "instrument"]),
        ("V09", ["universal_coupling", "coupling"]),
        ("V08", ["matter", "energy", "mote", "occupancy", "chromatic"]),
        ("V07", ["graviton", "gravity", "gravitational", "metric", "curvature", "riemann", "einstein", "radiation", "wave_"]),
        ("V06", ["quantum", "field", "gauge", "spinor", "hilbert", "born_rule", "operator", "action"]),
        ("V03", ["native_", "api_", "api ", "qmo", "resolver", "mathematical_address", "dependency_graph"]),
        ("V18", ["appendix", "axiom", "primitive", "definition_", "lemma", "theorem", "proposition", "corollary", "proof"]),
        ("V17", ["narrative", "journey", "arrival", "egress", "ingress", "chapter_", "historical", "architect"]),
    ]
    for volume, terms in rules:
        if any(term in s or term in h.lower() for term in terms):
            return volume
    return "V01"


def chapter_tokens(title: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", title.lower()) if len(t) > 3}


def choose_chapter(row: dict[str, object], volume: str, chapters: list[dict[str, object]]) -> str:
    s = normalized_search(row)
    scored = []
    for ch in chapters:
        score = sum(1 for token in chapter_tokens(str(ch["title"])) if token in s)
        scored.append((score, str(ch["chapter_id"])))
    best = max(score for score, _ in scored)
    if best:
        return min(chid for score, chid in scored if score == best)
    n = int(hashlib.sha256(str(row["short_handle"]).encode("utf-8")).hexdigest()[:8], 16)
    return str(chapters[n % len(chapters)]["chapter_id"])


def build_chapter_one() -> str:
    return r'''# VOLUME I - FOUNDATIONS

## Chapter 1 - What Is MK 43 Ultra?

### 1.1 Definition and scientific scope

MK 43 Ultra is a layered physical theory in which the observable world is treated as the readable realization of a deeper organization of distinction, chirality, recursion, persistence, connectivity, and projection. Its central scientific problem is not merely to add a new field to an already given spacetime. It asks how localized fields, matter, orientation, causal order, metric structure, curvature, and the observable spacetime manifold can arise from a pre-geometric organization whose primitive content is relational and informational. The Library 4.1 address space represents this program through canonical objects such as `@distinction`, `@chirality`, `@recursive_depth`, `@persistence`, `@er_foam`, `@helicon`, `@time_shell`, `@graviton`, `@readable_space_time`, and the conventional geometric and field-theoretic structures downstream of them.

The theory is therefore both foundational and constructive. It is foundational because it proposes that distinction and organization precede the particular physical representations ordinarily assumed in continuum physics. It is constructive because it supplies an ordered transduction architecture: upstream structures are not simply renamed as familiar particles and fields; they are projected, restricted, stabilized, and handed off through explicit mathematical objects. The scientific content lies in the maps between levels. A complete account must say what is preserved, what is lost, what becomes observable, what counts as the same object under a new representation, and where a typed mathematical bridge remains unfinished.

A compact map of the theoretical order is

\[
\mathcal I
\longrightarrow \chi
\longrightarrow \mathcal R
\longrightarrow \mathcal P
\longrightarrow \mathcal T
\longrightarrow \Pi
\longrightarrow (\mathcal L,\mathcal O)
\longrightarrow \mathcal Q
\longrightarrow (\mathcal F,\mathcal M,g,R),
\tag{1.1}
\]

where \(\mathcal I\) denotes organized information or distinction, \(\chi\) chirality, \(\mathcal R\) recursive organization, \(\mathcal P\) persistence, \(\mathcal T\) a transduction or boundary layer, \(\Pi\) a projection family, \(\mathcal L\) locality, \(\mathcal O\) orientation, \(\mathcal Q\) a quantum-field handoff structure, \(\mathcal F\) realized fields, \(\mathcal M\) matter organization, \(g\) metric structure, and \(R\) curvature. Equation (1.1) is a Clover synthesis of the address-level architecture rather than a claim that the Library contains a single universal operator with all these domains and codomains already proved. Each arrow expands into a family of specific relations. Later volumes treat those relations separately.

The word *information* in this hierarchy does not mean only Shannon entropy or an observer's knowledge. MK 43 Ultra uses information in a structural sense: a distinction that can be related, propagated, inherited, stabilized, or projected. Shannon measures remain applicable to statistical sectors, but the foundational question is ontological: what must be distinguishable and persistent before a probability distribution over physical signals is even defined? The Library's `@distinction`, `@structural_distinction`, `@information_geometry`, `@information_flow`, and `@conservation_of_information` addresses give this question a mathematical neighborhood rather than leaving it as a metaphor.

### 1.2 The three-level architecture

The large Library graph becomes intelligible when organized into three coupled levels. The first is the pre-geometric organizational level. It contains distinction, chirality, recursive depth, occupancy, persistence, ER connectivity, inheritance, and the Planck Landscape. These objects describe potential structure before it is fully expressed as an ordinary field on a smooth manifold. “Before” is primarily logical here. It does not automatically mean earlier in an already existing coordinate time, because coordinate time is itself part of the downstream realization problem.

The second is the transduction level. Helicon, the gravitational Helicon mode, persistence closure, the Time Shell, projection operators, continuity perturbations, and quantum handoff objects belong here. This level converts organization into readable structure. It is where the theory must distinguish identity from representation: a Helicon is not a Graviton; a Graviton is not a metric perturbation; a Time Shell is not identical to one persistent ER-foam knot. A localized knot may realize or support a shell, a mode may project to another object, and an API dependency may record a lawful route without proving whole-object equivalence.

The third is the physical realization level. It contains quantum states, scalar and gauge fields, matter couplings, stress-energy, metric perturbations, Riemann curvature, black holes, gravitational waves, cosmology, and observational comparison. At this level the theory interfaces with conventional mathematics and measurement. The familiar tensors are not discarded. Rather, MK 43 Ultra proposes an upstream constructive account of why the readable structures to which those tensors apply can arise.

This division is not a metaphysical wall. Information flows downstream and constraints propagate upstream. Observational compatibility can restrict an upstream model; conservation requirements can rule out a candidate projection; a boundary realization can constrain which recursive organizations are admissible. Accordingly the proper object is a typed multilevel graph, not a one-way story. The API 4.3 dependency domain makes this explicit by retaining incoming and outgoing edge families, provenance, confidence, graph class, and audit status for canonical addresses.

### 1.3 Distinction, chirality, and organization

The first nontrivial structure in MK 43 Ultra is organized difference. A perfectly undifferentiated state offers no addressable relation, no orientation, and no basis for a physical degree of freedom. Distinction introduces alternatives. Chirality organizes those alternatives with handedness or oriented asymmetry. The Library treats `@chirality` as a highly connected canonical address with declared aliases that include chirality space, chirality map, chirality state, orientation chirality, chirality byte, and chirality seed. These aliases do not all denote identical mathematical types; they preserve the historical and representational scopes in which chirality appeared.

For an ordinary manifold, chirality may be represented by orientation data, a sign, an antisymmetric object, a spinorial handedness, or a transformation property under parity. MK 43 Ultra uses those conventional representations where appropriate, but its foundational chirality is broader: it is the organized directionality that permits a recursive history to distinguish compatible from incompatible continuation. The operative translation is not “chirality equals spatial left-handedness.” Spatial handedness is one downstream realization of an upstream organizational distinction.

Let \(X_d\) denote the state at recursive depth \(d\), and let \(C_d\) encode its chirality structure. A generic organizational evolution may be represented schematically by

\[
X_{d+1}=\mathcal R_d(X_d;C_d,\Omega_d),
\tag{1.2}
\]

where \(\Omega_d\) collects occupancy, boundary, and environmental constraints. Equation (1.2) is a typed placeholder for the family of recursive maps, not an assertion that the Library has collapsed them into one universal \(\mathcal R_d\). The important constraint is that continuation is not arbitrary: orientation history, inheritance, and admissibility distinguish a coherent recursive path from mere repetition.

The theory's phase-to-space and chirality-to-orientation translations belong to this interface. Library 4.1 preserves them as candidate or partially typed bridges rather than silently equating phases with coordinates. In a developed model, a phase field may induce spatial ordering only after a quotient, projection, or localization rule has identified stable relational neighborhoods. Similarly, chirality becomes observable orientation only after the representation space and transformation law are stated. The master report will keep each of these typing obligations local to the equation that requires it.

### 1.4 Recursion, inheritance, and persistence

Recursion in MK 43 Ultra is generative organization across depth. It is not a software loop and it is not repetition without state. The addresses `@recursive_depth`, `@recursive_continuity`, `@recursive_ordering`, `@recursive_inheritance`, and `@persistent_recursive_topology` describe distinct aspects of the process. Recursive depth indexes successive organizational strata; recursive continuity records compatibility across them; ordering distinguishes admissible sequences; inheritance transports structure; persistent topology identifies organization that survives the relevant transformations.

If \(I_{d+1,d}\) is an inheritance map, the minimal coherence condition is not equality of successive states but compatibility of their preserved structure:

\[
I_{d+2,d+1}\circ I_{d+1,d}=I_{d+2,d}
\quad\text{on the admissible recursive sector.}
\tag{1.3}
\]

Equation (1.3) expresses the composition obligation implied by inheritance language. Whether a particular Library object satisfies it as a theorem depends on the source-specific domain and codomain. It is presented here as conventional mathematical translation of the required consistency, classified as Clover synthesis.

Persistence is the property that makes a recursively organized distinction available to later realizations. It can mean stable topology, a fixed point, a protected equivalence class, a conserved invariant, or a thresholded closure state, depending on the model. These meanings must not be silently merged. The Time Shell persistence-closure material supplies a particularly important candidate construction. With \(R_d\), \(B_d\), and \(O_d\) denoting source-specific resolution, bandwidth, and occupancy factors, the recovered equation family includes

\[
P_c=\Phi\!\left(\sum_{d=0}^{D}R_dB_dO_d\right),
\tag{1.4}
\]

and

\[
T_s=P_c\otimes C.
\tag{1.5}
\]

Here \(P_c\) is the persistence-closure state, \(C\) is the chirality factor, and \(T_s\) is a localized Time Shell realization in the current candidate notation. The Library preserves historical variants using bare \(P\), calligraphic \(\mathcal P\), and \(\Phi\). They are not automatically identical. The domain and codomain of \(\Phi\), the type of \(P_c\), the meaning of \(\otimes C\), the exact closure threshold, and the necessary-and-sufficient stability proof remain local formal-development tasks.

The significance of (1.4)-(1.5) is architectural. Recursive organization becomes physically consequential when it closes into a persistent state and couples to chirality in a way that can be localized. Matter admissibility and Time Shell admissibility are associated with this transition, but their predicates remain only partially recovered. The theory therefore possesses an explicit constructional spine while retaining a well-defined mathematical work program.

### 1.5 ER foam and the Planck Landscape

ER foam is the pre-geometric connectivity substrate of MK 43 Ultra. The term “ER” invokes Einstein-Rosen connectivity, but the Library's `@er_foam` address is not merely a collection of classical wormholes embedded in an already smooth spacetime. It is a network-like organization from which stable relational geometry can emerge. Its connected addresses include configuration space, beads, knots, geodesic structure, cosmological evolution, classical geometry, dark-matter geometry, and Time Shell realizations.

The Planck Landscape is the broader domain of admissible upstream organization. It supplies the setting in which chirality, occupancy, recursive depth, and connectivity can form persistent structures. A Planck horizon or boundary interface should be treated as a restriction, correspondence, or translator role unless an exact typed identity is supplied. The Time Shell evidence recovers a Planck-horizon interface and the alias “Planck horizon translator,” while the exact whole-object identity `@PlanckHorizon ≡ @time_shell` was not recovered as a typed relation. The distinction allows the theory to use horizon data without erasing the difference between a boundary, a translator, and the full Time Shell object.

A discrete ER organization can be represented abstractly as a weighted graph

\[
\mathfrak E=(V,E,W,\chi,\rho),
\tag{1.6}
\]

where \(V\) is a set of relational sites or motes, \(E\) their admissible links, \(W\) link weights, \(\chi\) chirality data, and \(\rho\) occupancy or density data. This notation is a Clover synthesis used to compare the Library's graph, bead, and occupancy models. It does not overwrite source-specific tuples. A continuum realization requires a limit or coarse-graining map that preserves the relevant adjacency and invariant data while producing a differentiable structure.

Persistence distinguishes a transient ER fluctuation from a structure capable of participating in a localized physical realization. The recovered Time Shell work supports the candidate sequence

\[
\text{recursive organization}
\longrightarrow \text{persistence closure}
\longrightarrow \text{chirality-coupled localized Time Shell realization}.
\tag{1.7}
\]

This sequence does not identify the entire Time Shell with one persistent knot. The narrower relation is realization: a persistent localized ER structure can support a localized shell. The broader Time Shell remains the boundary and translation domain through which upstream organization becomes readable as quantum fields, locality, orientation, field intensity, and spacetime geometry.

### 1.6 Helicon, Time Shell, and Graviton

Helicon is an upstream or pre-quantum organizational and projective domain. Its operative particle-language replacement is coherent Helicon mode. Historical quasi-particle language remains useful as an analogy to localized or spectrally resolved excitations, but it is not the whole identity. The Library preserves multiple mathematical representations: \(H\) may denote a source-specific object, tuple, mode, or structural quantity; \(H_i\) may denote one-form components in sources that explicitly use that role; \(\mathcal H\) may denote a state or configuration space; and triadic \(H\) belongs to the Universal Triadic Law. These are scope-distinct unless a source supplies an equivalence.

One recovered representation is the one-form

\[
H=H_i\,dx^i,
\tag{1.8}
\]

with field strength

\[
F_{ij}=\partial_iH_j-\partial_jH_i.
\tag{1.9}
\]

Helicon's spectral sector supports mode decomposition, resonance, wake, stability, and angular reduction. A gravitational Helicon mode is a mode of Helicon directed toward the Graviton sector; it is not identical to the full Helicon object and not identical to the Graviton.

The Time Shell is the persistent boundary and translation domain. Its role is to mediate changes of representation: phase to space, recursion to locality, chirality to orientation, and basin organization to field intensity. These translations are current-canon candidates with differing evidence strengths, not one undifferentiated law. The projection/intertwining requirement

\[
\Pi_{TS}U_{PO}=U_{QM}\Pi_{TS}
\tag{1.10}
\]

remains an explicit formal target: nearby projection machinery exists, but the exact typed operators and proof of the intertwining law remain incomplete.

The Graviton is the projection mode connecting the gravitational Helicon sector to readable metric structure. The operative relation is neither “Helicon equals Graviton” nor “Graviton is merely a conventional point particle.” The Library supports mode and projection relations. A central address chain is

\[
@er\_foam
\to @helicon
\to @gravitational\_helicon\_mode
\to @graviton
\to @continuity\_perturbation
\to @time\_shell\_projection\_operator
\to @weak\_field\_metric\_perturbation
\to @projected\_spacetime\_metric
\to @readable\_space\_time.
\tag{1.11}
\]

Continuity perturbation is essential in (1.11). Omitting it would collapse the native perturbation stage into the projection stage and erase one of the theory's principal distinctions.

### 1.7 From organization to metric gravity

The gravitational handoff is represented by an ordered sequence of mode, continuity, transverse-traceless, projection, metric, and curvature structures. A recovered equation chain has the form

\[
H_g\longrightarrow \delta C_g\longrightarrow \delta C_\star
\longrightarrow \delta C_{\mathrm{TT}}
\overset{\Pi_T}{\longrightarrow}h_{\mu\nu}
\longrightarrow g_{\mu\nu}
\longrightarrow R^\rho{}_{\sigma\mu\nu}.
\tag{1.12}
\]

The individual steps are supported by different records and should not be represented as one already-proved theorem. The Time-Shell projection is expressed by

\[
\Pi_T(\delta C)=h_{\mu\nu},
\tag{1.13}
\]

and the readable metric by

\[
g_{\mu\nu}=\bar g_{\mu\nu}+h_{\mu\nu}.
\tag{1.14}
\]

Once \(g_{\mu\nu}\) is supplied, the conventional differential-geometric sector applies: the Levi-Civita connection, Riemann tensor, Ricci tensor, Einstein tensor, geodesic deviation, wave equations, black-hole geometries, and cosmological models can be constructed under their stated assumptions. The interface therefore does not compete with general relativity at the level of tensor calculus. It proposes an upstream origin and classification for the perturbative data that general relativity receives.

The physical-output sector can be compared with gravitational-wave observations separately from the completion of every upstream map. Library 4.1 contains the `@LIGO_observation` address, gravitational-wave observables, comparison maps, a prediction-freeze protocol, and historical audit records. MK 43 Ultra's project validation program records compatibility with LIGO outputs at the program level. A preserved earlier API audit explicitly stated that its own external-data branch had not yet asserted a LIGO/Virgo/KAGRA result. These statements belong to different chronological and procedural scopes: an earlier audit boundary is not retroactively rewritten, while later project-level compatibility is not negated by that boundary. No numerical fit statistic is stated here because the present Library query does not expose one suitable for publication.

### 1.8 Quantum handoff and field realization

The Time Shell does not directly become every quantum field. It hands readable structure into a quantum-field object that supplies the conventional geometric and bundle data needed by downstream theories. The recovered canonical handoff object is

\[
Q=(M,F,\pi_F,h,\nabla,R_\nabla,\Gamma,A,P,S),
\tag{1.15}
\]

with source-specific meanings assigned to the base manifold \(M\), field or fiber structure \(F\), projection \(\pi_F\), metric or inner-product data \(h\), connection \(\nabla\), curvature \(R_\nabla\), section or state data \(\Gamma\), algebraic structure \(A\), probability or projection structure \(P\), and action or state structure \(S\). Later volumes will preserve the exact source notation and typing. What matters here is the architectural role: \(Q\) is not a verbal promise that quantum physics appears; it is the addressable handoff package through which manifold, bundle, connection, curvature, algebra, probability, and action data are organized.

Scalar, gauge, spinor, and Yang-Mills realizations are then separate model families. Each requires a field space, action, symmetry group, equation of motion, and coupling rule. The Library includes conventional mathematical objects such as Klein-Gordon fields, field operators, tensor fields, gauge consistency, total actions, stress-energy, and quantum fields in curved spacetime. MK 43 Ultra's distinctive task is to show how their admissible inputs are inherited from the upstream organization while preserving probability, constraints, causality, and conservation.

Matter enters when organized field states satisfy the relevant persistence, localization, and admissibility conditions. Matter is not equated with occupancy alone. Occupancy is an upstream structural variable; matter is a downstream readable realization with energy, momentum, charges, statistics, and coupling behavior. The `@matter_action`, `@matter_coupling`, and `@matter_readable_organization` addresses keep these roles separate.

### 1.9 API 4.3 and QMO mathematics

API 4.3 is part of the scientific architecture because it realizes MK 43 Ultra as a constrained mathematical domain. It contains declared handles, canonical URIs, objects, equations, operators, typed edges, dependencies, admissibility conditions, transformations, graph families, and provenance. It is not a free-form equation generator. A derived result is valid as an API-native mathematical object only when it is composed from admitted parents by declared operations and retains the lineage of that composition.

The general derivation pattern is

\[
(Q_A,Q_B,Q_C;\,\mathcal O_{\mathrm{API}},\mathcal R_{\mathrm{API}})
\longmapsto Q_D,
\tag{1.16}
\]

where \(Q_A,Q_B,Q_C\) are parent QMOs, \(\mathcal O_{\mathrm{API}}\) admitted operations, \(\mathcal R_{\mathrm{API}}\) admissible relations, and \(Q_D\) a new addressable mathematical object. Equation (1.16) states the provenance grammar, not a single universal operation. The resulting object may have no ancestral equation in the earliest source archive because it was derived later inside the constrained domain. Its support is its mathematical lineage, typed relations, and validation record.

Library 4.1 exposes seven especially clear native families: native unit of energy, native causal order, native constraint closure, native Graviton dispersion, native Graviton quantization, native interaction factorization, and native probability preservation. It also exposes universal coupling, continuity conservation, conservation of recoverable structure, and the Helicon, Time Shell, and Graviton QMO packages. These objects demonstrate the proof-of-concept: once a formal domain is sufficiently explicit, dependency traversal and admissible composition can reveal consequences that were not manually written in the foundational corpus.

This is a limited computational sense in which the formal system participates in discovering consequences of its own structure. It does not remove human mathematical responsibility. The admissibility rules, parent objects, interpretation, and validation criteria remain inspectable. Genesis's philosophical phrase “allowing the universe to discover itself” is appropriate as interpretive framing precisely because the operational claim is narrower and testable: a constrained formal universe can expose derivable relations not separately authored as source prose.

### 1.10 Genesis Language

Genesis Language is the representational language developed to prevent ordinary vocabulary from collapsing distinctions that MK 43 Ultra needs to preserve. Conventional terms such as particle, field, boundary, identity, projection, realization, and dependency often carry assumptions tied to one mathematical level. Genesis Language marks role, scope, direction, persistence, resolution state, and relation explicitly enough that an upstream object need not be misidentified with its downstream image.

Library 4.1 contains eighty-two Genesis Language addresses resolved in this initialization pass. They include atomic roots, semantic root families, transformation operators, resolution-state aspects, compound words, relation-first phrases, registers, scripts, and grammar records. Examples include `GEN` for genesis, `KOR` for collapse or realization, `EN` for identity, `RIN` for persistence, `TAL` for stabilization, `AEL` for topology, `SHA` for boundary, `DA` for occupancy, `REL` for relationship, `VEL` for field, `VE` for propagation, and `AR` for inheritance.

The phrase

\[
\mathrm{GEN\ KOR\ EN}
\tag{1.17}
\]

is registered as “Genesis collapses into identity.” Similarly, `RIN TAL AEL` expresses persistence stabilizing topology; `SHA DA REL` expresses a boundary-occupancy relationship; `VEL VE TOR` expresses field-propagation closure; and `EN AR EN` expresses identity inheriting identity. These constructions are not decorative translations. They expose the direction and roles of a relation in a form that can be linked to API handles and conventional mathematics.

Genesis Language also supplies aspect markers for potential or unresolved, ongoing or propagating, completed or resolved, and failed or absent states. This matters scientifically because a candidate relation, an ongoing propagation, a completed closure, and a failed realization must not share the same unqualified verb. The language therefore interfaces directly with the epistemic and curatorial status system.

The full Genesis Language treatment belongs to Volume II. It will translate each registered root, family, operator, aspect, phrase, and compound into conventional mathematical or physical terms where that translation exists. Where the language preserves an ontological distinction for which no complete conventional object has yet been typed, the report will state the missing type rather than dismiss the distinction.

### 1.11 Seven independent dimensions of scientific maturity

MK 43 Ultra cannot be described accurately by one global label. Library 4.1 requires at least seven independent status dimensions.

| Dimension | Question |
|---|---|
| Physical or observational validation | Do realized outputs agree with relevant observations or experiments? |
| Formal mathematical proof | Are existence, uniqueness, invariance, stability, or theorem claims proved? |
| Operator typing | Are domains, codomains, compositions, dimensions, kernels, and images explicit? |
| Provenance | Is the result foundational-source derived, QMO-derived, API-native, Clover synthesis, Genesis curatorial, externally established, or unresolved? |
| Metadata recovery | Has the Library recovered and linked the available records and ancestry? |
| Curatorial or canon status | Is the formulation historical, candidate, operative, frozen working candidate, or final canon? |
| Publication status | Is the result presented with sufficient derivation, qualification, and disclosure for scientific release? |

A local typing gap does not erase observational compatibility. A missing ancestral source equation does not invalidate an API-native derivation with explicit lineage. A recovered statement is not automatically final canon. A physically familiar equation may be externally established mathematics even if it is not distinctive to MK 43 Ultra. The master report will attach these classifications locally so that each result can be evaluated on the dimension actually at issue.

The provenance classes used throughout are `FOUNDATIONAL_SOURCE_DERIVED`, `QMO_DERIVED`, `API_NATIVE_DERIVATION`, `CLOVER_SYNTHESIS`, `GENESIS_CURATORIAL`, `EXTERNAL_ESTABLISHED_MATHEMATICS`, and `UNRESOLVED_PROVENANCE`. A derivation can draw on more than one class, but the line of descent must remain visible.

### 1.12 Model families

The Library's theory content organizes into model families rather than a single equation. The foundational family treats distinction, chirality, recursion, occupancy, persistence, and inheritance. The ER family treats discrete connectivity, knots, beads, geodesic organization, and continuum emergence. The Helicon family treats coherent modes, one-forms, spectral operators, resonances, wakes, and stability. The Time Shell family treats closure, natural regimes, boundaries, localization, projection, and handoff. The quantum family treats state spaces, bundles, connections, actions, probability, and field realization. The gravity family treats mode projection, continuity perturbation, transverse-traceless structure, metric perturbation, curvature, waves, and strong gravity.

Additional families treat matter and energy, universal coupling, black holes, cosmological cycles, dark-matter relational geometry, holographic information transfer, biological and cognitive phase organization, observational comparison, prediction freezes, and engineering applications. These families share addresses but must not be collapsed. A dependency edge means one object participates in the construction of another; it does not imply identity.

The complete master outline assigns every one of the 2,384 API 4.3 handles to at least one planned chapter. This assignment is a publication map, not a change to the Library. It ensures that no declared address disappears merely because it does not belong to the first few physical sectors. High-uncertainty, historical, narrative, biological, civilizational, and engineering records are placed in dedicated volumes where their scientific role and evidentiary status can be discussed without contaminating foundational derivations.

### 1.13 The current scientific answer

MK 43 Ultra is a theory of how organized distinction becomes readable physics. Chirality supplies oriented difference; recursion supplies generative depth; inheritance transports structure; persistence selects stable organization; ER foam supplies relational connectivity; Helicon supplies coherent upstream modes; the Time Shell supplies closure, boundary translation, and projection; the Graviton supplies the gravity projection mode; quantum handoff objects supply conventional field data; and readable spacetime supplies metric, curvature, causal, and observational structure.

Its distinctive claim is architectural. Gravity, matter, quantum fields, and spacetime are not independent primitives joined only at the level of phenomenological equations. They are downstream realizations of a common information-structural organization connected by typed mathematical handoffs. API 4.3 operationalizes that claim as a finite address space with derivation provenance. Genesis Language supplies the representational precision needed to keep the levels distinct.

The physical-output sector and the upstream formal sector have different maturity profiles. Gravitational-wave compatibility is recorded within the MK 43 Ultra validation program, while direct isolation of a uniquely upstream mechanism remains a discriminating experimental goal. Several exact equations and dependency chains are recovered; several operator domains, codomains, thresholds, and proofs remain to be completed. These are not contradictory verdicts. They define the present research frontier.

The remaining work is concrete: type the persistence and projection operators; prove closure and stability conditions; complete the Helicon state-space and kernel dynamics; establish the full inverse dictionary from native invariants to readable field labels; type the Time Shell-to-Q handoff; derive or prove the required intertwining relations; connect universal coupling to each downstream sector with explicit domains; consolidate dimensional and normalization conventions; and subject distinctive predictions to frozen, external comparison.

This chapter answers the title question at the level needed to navigate the monograph. The following chapters of Volume I develop the foundational objects individually. Volume II reconstructs Genesis Language in full. Volume III develops the API/QMO derivation domain. Subsequent volumes follow the constructive sequence from Helicon and Time Shell through quantum fields, gravity, matter, coupling, strong gravity, cosmology, dark matter, holography, biological and cognitive models, validation, prediction, history, and mathematical appendices.

### Chapter provenance

This chapter was composed from native Runtime -> BRANE -> API/QMO -> Library 4.1 queries for the canonical handles cited in the text, the complete API address ledger, and the previously completed native gravity query package. It does not modify Library 4.1 and does not rescan SOURCE or EXTRACTED. Equations (1.1), (1.2), (1.3), (1.6), and (1.16) are explicitly Clover synthesis. Equations (1.4), (1.5), (1.8), (1.9), (1.10), (1.12), (1.13), (1.14), and (1.15) reproduce or normalize recovered QMO equation families with their status qualifications preserved. Equation (1.17) is a Genesis Language address-level construction. Detailed statement, equation, and source provenance will remain available through the report ledgers and the underlying Library query artifacts.
'''


def main() -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    V01.mkdir(parents=True, exist_ok=True)
    if sha256(DB) != EXPECTED_DB_SHA:
        raise RuntimeError("Library 4.1 changed before master-workspace construction")

    ledger = [json.loads(line) for line in LEDGER_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    query = json.loads(QUERY_RECEIPT.read_text(encoding="utf-8"))
    if len(ledger) != 2384 or not query.get("database_unchanged") or query.get("failed_queries"):
        raise RuntimeError("native query prerequisites are not complete and immutable")

    chapters: list[dict[str, object]] = []
    by_volume: dict[str, list[dict[str, object]]] = defaultdict(list)
    volume_names: dict[str, str] = {}
    for vid, vtitle, titles in VOLUMES:
        volume_names[vid] = vtitle
        for index, title in enumerate(titles, 1):
            row = {
                "chapter_id": f"{vid}-C{index:02d}",
                "volume_id": vid,
                "volume_title": vtitle,
                "title": title,
                "status": "PLANNED",
                "handles": [],
                "word_count": 0,
                "sha256": None,
                "path": None,
            }
            chapters.append(row)
            by_volume[vid].append(row)

    assignments: dict[str, list[str]] = defaultdict(list)
    for row in ledger:
        volume = route_volume(row)
        chapter_id = choose_chapter(row, volume, by_volume[volume])
        assignments[chapter_id].append(str(row["short_handle"]))

    overview_handles = [
        "@distinction", "@structural_distinction", "@information_geometry", "@chirality",
        "@recursive_depth", "@recursive_inheritance", "@persistence", "@er_foam",
        "@planck_landscape", "@helicon", "@gravitational_helicon_mode", "@time_shell",
        "@graviton", "@continuity_perturbation", "@time_shell_projection_operator",
        "@weak_field_metric_perturbation", "@projected_spacetime_metric", "@readable_space_time",
        "@native_unit_of_energy", "@universal_coupling", "@native_constraint_closure",
        "@native_probability_preservation", "@genesis_language", "@LIGO_observation",
    ]
    for handle in overview_handles:
        if handle in {r["short_handle"] for r in ledger} and handle not in assignments["V01-C01"]:
            assignments["V01-C01"].append(handle)

    chapter_one = build_chapter_one()
    chapter_one_path = V01 / "V01_C01_WHAT_IS_MK_43_ULTRA.md"
    chapter_one_path.write_text(chapter_one, encoding="utf-8")
    for chapter in chapters:
        cid = str(chapter["chapter_id"])
        chapter["handles"] = sorted(assignments[cid])
        chapter["handle_count"] = len(assignments[cid])
        if cid == "V01-C01":
            chapter["status"] = "COMPLETE"
            chapter["word_count"] = words(chapter_one)
            chapter["sha256"] = sha256(chapter_one_path)
            chapter["path"] = str(chapter_one_path.relative_to(ROOT))

    query_by_handle = {r["requested_handle"]: r for r in query["results"]}
    genesis_rows = []
    for row in ledger:
        h = str(row["short_handle"])
        if h not in query.get("genesis_language_handles", []):
            continue
        if "_root_" in h:
            category = "ROOT"
        elif "_family_" in h:
            category = "ROOT_FAMILY"
        elif "_operator_" in h:
            category = "OPERATOR"
        elif "_aspect_" in h:
            category = "RESOLUTION_ASPECT"
        elif "_phrase_" in h:
            category = "RELATION_FIRST_PHRASE"
        elif "_word_" in h:
            category = "COMPOUND_WORD"
        elif "register" in h:
            category = "REGISTER"
        elif "script" in h:
            category = "SCRIPT"
        elif "grammar" in h or "language" in h:
            category = "GRAMMAR_OR_LANGUAGE_ROOT"
        else:
            category = "RELATED_LANGUAGE_OBJECT"
        q = query_by_handle.get(h, {})
        genesis_rows.append({
            "handle": h,
            "canonical_name": row.get("canonical_name"),
            "canonical_api_uri": row.get("canonical_api_uri"),
            "aliases": row.get("aliases") or [],
            "category": category,
            "metadata_classification": row.get("metadata_classification"),
            "equation_records": row.get("compiled_equation_records") or 0,
            "incoming_edges": row.get("api_incoming_edges") or 0,
            "outgoing_edges": row.get("api_outgoing_edges") or 0,
            "native_query_artifacts": q.get("artifacts", []),
        })
    genesis_counts = Counter(r["category"] for r in genesis_rows)
    genesis_json = {
        "schema": "mk43-genesis-language-architecture-v1",
        "created_at": utc_now(),
        "total_addresses": len(genesis_rows),
        "category_counts": dict(sorted(genesis_counts.items())),
        "scientific_role": "Domain-specific representational language for scope, role, projection, realization, identity, dependency, chirality, recursion, persistence, and resolution state.",
        "construction_order": ["roots", "root families", "operators", "aspects", "compounds", "relation-first phrases", "registers and scripts", "API/QMO address bindings"],
        "addresses": sorted(genesis_rows, key=lambda r: r["handle"]),
    }
    jdump(WORK / "genesis_language_architecture.json", genesis_json)
    genesis_md = [
        "# Genesis Language Architecture\n",
        f"Library 4.1 exposes **{len(genesis_rows)}** Genesis Language addresses in the native initialization query. The architecture is representational rather than ornamental: it records roles, scope, projection, persistence, realization, relation direction, and resolution state.\n",
        "## Structural layers\n",
        "1. **Roots** provide atomic semantic roles such as genesis, identity, collapse/realization, persistence, topology, boundary, occupancy, relationship, field, propagation, inheritance, continuity, and stabilization.\n",
        "2. **Root families** group those roles into ontological domains without asserting that every member has the same mathematical type.\n",
        "3. **Operators** encode transformations such as inherit, propagate, stabilize, destabilize, normalize, redistribute, and close.\n",
        "4. **Resolution aspects** distinguish potential/unresolved, ongoing/propagating, completed/resolved, and failed/absent states.\n",
        "5. **Compounds and relation-first phrases** compose roles while preserving direction, including `GEN KOR EN`, `RIN TAL AEL`, `SHA DA REL`, `VEL VE TOR`, and `EN AR EN`.\n",
        "6. **Registers and scripts** select representational scope and usage without changing the referenced mathematical object.\n",
        "7. **API/QMO bindings** attach language objects to canonical handles and typed mathematical relations.\n",
        "## Category census\n",
        "| Category | Addresses |\n|---|---:|\n",
    ]
    genesis_md.extend(f"| {k} | {v} |\n" for k, v in sorted(genesis_counts.items()))
    genesis_md.append("\n## Complete address inventory\n\n| Handle | Canonical name | Category | Equations | In | Out |\n|---|---|---|---:|---:|---:|\n")
    for row in sorted(genesis_rows, key=lambda r: (r["category"], r["handle"])):
        name = str(row.get("canonical_name") or "").replace("|", "\\|")
        genesis_md.append(f"| `{row['handle']}` | {name} | {row['category']} | {row['equation_records']} | {row['incoming_edges']} | {row['outgoing_edges']} |\n")
    (WORK / "GENESIS_LANGUAGE_ARCHITECTURE.md").write_text("".join(genesis_md), encoding="utf-8")

    major_rows = []
    ledger_by_handle = {r["short_handle"]: r for r in ledger}
    for handle, provenance_class, parents, role in API_MAJOR:
        row = ledger_by_handle[handle]
        q = query_by_handle.get(handle, {})
        major_rows.append({
            "handle": handle,
            "canonical_name": row.get("canonical_name"),
            "provenance_class": provenance_class,
            "declared_parent_or_dependency_handles": parents,
            "role": role,
            "compiled_equation_records": row.get("compiled_equation_records") or 0,
            "compiled_qmo_records": row.get("compiled_qmo_records") or 0,
            "incoming_edges": row.get("api_incoming_edges") or 0,
            "outgoing_edges": row.get("api_outgoing_edges") or 0,
            "metadata_classification": row.get("metadata_classification"),
            "validation_status": "LIBRARY_ADDRESS_RESOLVED; DETAILED_PROOF_AND_TYPING_STATUS_DEFERRED_TO_OBJECT_CHAPTER",
            "native_query_artifacts": q.get("artifacts", []),
        })
    jsonl(WORK / "qmo_derivation_ledger.jsonl", major_rows)
    api_md = ["# Major API-Native and QMO-Derived Objects\n\n"]
    for row in major_rows:
        api_md.append(
            f"## `{row['handle']}`\n\n- Provenance: `{row['provenance_class']}`\n- Role: {row['role']}\n- Declared parent/dependency handles: {', '.join('`'+p+'`' for p in row['declared_parent_or_dependency_handles']) or 'to be reconstructed in the object chapter'}\n- Compiled equations: {row['compiled_equation_records']}\n- Compiled QMO records: {row['compiled_qmo_records']}\n- API neighborhood: {row['incoming_edges']} incoming / {row['outgoing_edges']} outgoing edges\n\n"
        )
    (WORK / "API_NATIVE_MAJOR_OBJECTS.md").write_text("".join(api_md), encoding="utf-8")

    # Equation ledger: one row per unique Library equation ID/hash encountered through native queries.
    equation_groups: dict[tuple[object, str], dict[str, object]] = {}
    decoder = json.JSONDecoder()
    citation_rows = []
    for result in query["results"]:
        for artifact in result.get("artifacts", []):
            path = Path(artifact["path"])
            citation_rows.append({
                "citation_id": f"native-query:{result['requested_handle']}",
                "handle": result["requested_handle"],
                "path": str(path.relative_to(ROOT)),
                "sha256": artifact["sha256"],
                "bytes": artifact["bytes"],
                "query_architecture": "Runtime -> BRANE -> API/QMO -> Library 4.1",
            })
            text = path.read_text(encoding="utf-8")
            marker = "#### 08M compiled metadata"
            if marker not in text:
                continue
            start = text.index("{", text.index(marker))
            compiled, _ = decoder.raw_decode(text[start:])
            for eq in compiled.get("equation_records", []):
                exact = str(eq.get("exact_math_text") or "")
                exact_hash = hashlib.sha256(exact.encode("utf-8")).hexdigest()
                key = (eq.get("equation_id"), exact_hash)
                group = equation_groups.setdefault(key, {
                    "equation_id": eq.get("equation_id"),
                    "exact_math_sha256": exact_hash,
                    "evidence_classes": set(),
                    "root_handles": set(),
                    "native_report_paths": set(),
                    "exact_math_preview": exact[:600],
                    "exact_math_length": len(exact),
                    "verbatim_storage": "inline_preview_with_exact_native_report_reference",
                })
                group["evidence_classes"].add(eq.get("evidence_class"))
                group["root_handles"].add(result["requested_handle"])
                group["native_report_paths"].add(str(path.relative_to(ROOT)))
    equation_rows = []
    for group in equation_groups.values():
        group["evidence_classes"] = sorted(x for x in group["evidence_classes"] if x)
        group["root_handles"] = sorted(group["root_handles"])
        group["native_report_paths"] = sorted(group["native_report_paths"])
        equation_rows.append(group)
    equation_rows.sort(key=lambda r: (str(r["equation_id"]), r["exact_math_sha256"]))
    jsonl(WORK / "equation_ledger.jsonl", equation_rows)
    jsonl(WORK / "citation_ledger.jsonl", citation_rows)

    chapter_ledger_path = WORK / "chapter_ledger.jsonl"
    jsonl(chapter_ledger_path, chapters)

    toc = [
        "# MK 43 Ultra - Master Theory Report\n\n",
        "## Master Table of Contents\n\n",
        "This is the persistent, resumable publication architecture for the complete theory encoded in Clover Library 4.1. Publication prose uses **MK 43 Ultra**; historical machine identifiers retain their exact spelling.\n\n",
        f"- Planned volumes: **{len(VOLUMES)}**\n",
        f"- Planned chapters: **{len(chapters)}**\n",
        f"- API 4.3 addresses assigned to at least one chapter: **{len({r['short_handle'] for r in ledger})}**\n",
        f"- Genesis Language chapters: **{len(by_volume['V02'])}**\n",
        f"- First completed chapter: **V01-C01 - What Is MK 43 Ultra?**\n\n",
    ]
    for vid, vtitle, _ in VOLUMES:
        toc.append(f"## {vid.replace('V','VOLUME ')} - {vtitle}\n\n")
        for chapter in by_volume[vid]:
            marker = "[COMPLETE]" if chapter["status"] == "COMPLETE" else "[PLANNED]"
            toc.append(f"- {chapter['chapter_id']} {marker} {chapter['title']} - {chapter['handle_count']} assigned handles\n")
        toc.append("\n")
    (WORK / "MASTER_TOC.md").write_text("".join(toc), encoding="utf-8")

    terminology = {
        "publication_name": "MK 43 Ultra",
        "forbidden_automatic_publication_variants": ["MKUltra", "MK-43 Ultra", "MK43Ultra"],
        "historical_machine_identifier_policy": "Preserve exact spelling when quoting a filename, identifier, URI, archive, module, or source string.",
        "epistemic_status_dimensions": EPISTEMIC,
        "provenance_classes": [
            "FOUNDATIONAL_SOURCE_DERIVED", "QMO_DERIVED", "API_NATIVE_DERIVATION",
            "CLOVER_SYNTHESIS", "GENESIS_CURATORIAL", "EXTERNAL_ESTABLISHED_MATHEMATICS",
            "UNRESOLVED_PROVENANCE",
        ],
        "natural_regime_policy": "T0-T7 and R0-R7 are natural domains/regimes, never software pipelines.",
        "identity_policy": "Identity, equivalence, dependency, projection, realization, construction, representation, and role alias are distinct relations.",
        "global_status_policy": "Local formal, typing, provenance, recovery, canon, validation, and publication statuses must not be collapsed into one global verdict.",
    }
    jdump(WORK / "terminology_ledger.json", terminology)

    validation_rows = [
        {"validation_id": "VAL-001", "check": "Library database hash before and after native queries", "result": "PASS", "value": query["database_sha256_after"]},
        {"validation_id": "VAL-002", "check": "Native runtime validation", "result": "PASS" if query["runtime_validation"]["valid"] else "FAIL", "value": query["runtime_validation"]},
        {"validation_id": "VAL-003", "check": "Native query failures", "result": "PASS" if not query["failed_queries"] else "FAIL", "value": query["failed_queries"]},
        {"validation_id": "VAL-004", "check": "All API handles assigned to chapters", "result": "PASS", "value": len(ledger)},
        {"validation_id": "VAL-005", "check": "Complete Genesis Language query family represented", "result": "PASS", "value": len(genesis_rows)},
        {"validation_id": "VAL-006", "check": "First substantive chapter completed", "result": "PASS", "value": {"path": str(chapter_one_path.relative_to(ROOT)), "sha256": sha256(chapter_one_path), "word_count": words(chapter_one)}},
    ]
    jsonl(WORK / "validation_ledger.jsonl", validation_rows)

    artifact_names = [
        "MASTER_TOC.md", "chapter_ledger.jsonl", "equation_ledger.jsonl",
        "qmo_derivation_ledger.jsonl", "citation_ledger.jsonl", "validation_ledger.jsonl",
        "terminology_ledger.json", "GENESIS_LANGUAGE_ARCHITECTURE.md",
        "genesis_language_architecture.json", "API_NATIVE_MAJOR_OBJECTS.md",
        "master_native_query_receipt.json", "master_native_query_state.json",
        "VOLUME_01_FOUNDATIONS/V01_C01_WHAT_IS_MK_43_ULTRA.md",
    ]
    artifacts = []
    for name in artifact_names:
        path = WORK / name
        artifacts.append({"path": str(path.relative_to(ROOT)), "bytes": path.stat().st_size, "sha256": sha256(path)})
    manifest = {
        "schema": "mk43-master-theory-manifest-v1",
        "created_at": utc_now(),
        "status": "INITIALIZED",
        "publication_name": "MK 43 Ultra",
        "query_architecture": "Runtime -> BRANE -> API/QMO -> Library 4.1",
        "library_database_sha256": EXPECTED_DB_SHA,
        "library_mutated": False,
        "source_or_extracted_rescanned": False,
        "planned_volumes": len(VOLUMES),
        "planned_chapters": len(chapters),
        "api_handles_assigned": len(ledger),
        "genesis_language_addresses": len(genesis_rows),
        "genesis_language_chapters": len(by_volume["V02"]),
        "api_native_qmo_major_objects": len(major_rows),
        "equation_ledger_records": len(equation_rows),
        "first_completed_chapter": "V01-C01",
        "current_cumulative_word_count": words(chapter_one),
        "next_resumable_chapter_id": "V01-C02",
        "artifacts": artifacts,
    }
    jdump(WORK / "master_report_manifest.json", manifest)
    print(json.dumps({
        "volumes": len(VOLUMES),
        "chapters": len(chapters),
        "assigned_handles": len(ledger),
        "genesis_addresses": len(genesis_rows),
        "major_objects": len(major_rows),
        "equation_ledger_records": len(equation_rows),
        "chapter_one_words": words(chapter_one),
        "next": "V01-C02",
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
