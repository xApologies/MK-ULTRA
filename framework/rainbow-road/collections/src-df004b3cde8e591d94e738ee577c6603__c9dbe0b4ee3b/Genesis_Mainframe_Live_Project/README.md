# Genesis Mainframe — Live Architecture Project

**Status:** Active working repository  
**Initialized:** 2026-08-03 12:45 CDT  
**Current snapshot:** v0.3.2  
**Primary target:** Full start-to-finish architecture map for the Genesis Mainframe  
**Long-term application:** VÆLD-class vehicle, Clover, robotics, scientific systems  
**Current scope:** The mainframe itself—not a toy prototype and not yet the ship

## What this repository is

This is the live working model for the Genesis Mainframe. It consolidates the current architecture into one maintainable project so future corrections can be incorporated without losing prior reasoning.

The repository is designed to be:

- additive;
- provenance-preserving;
- correction-friendly;
- explicit about unresolved questions;
- separable into hardware, language, intelligence, portal, energy, and verification workstreams without treating those workstreams as independent ontological systems.

## Prime architectural statement

> The Genesis Mainframe is one recursively dynamic topology expressed as Stored Geometry, Active Geometry, and Observed Geometry.

The hardware remembers.  
The runtime evolves.  
The intelligence understands.  
Closure recovers the topology.

## Current model in one line

```text
Physical energy
  -> six-basin persistent substrate
  -> chirality cell/byte
  -> recursive chirality fabric
  -> instantiated Geometrics
  -> Genesis operators and operating topology
  -> Portal interconnect
  -> Guardian Intelligence
  -> applications
```

## Repository navigation

- `00_Project_Control` — status, update rules, changelog, manifest
- `01_Current_Model` — the current integrated working model
- `02_Architecture` — system maps and boot/runtime organization
- `03_Hardware` — physical substrate, storage, fabric, processor requirements
- `04_Language` — position and role of the Genesis language
- `05_Intelligence` — Guardian/AI framework
- `06_Portals` — portal bus and transport contracts
- `07_Energy` — physical and organizational energy models
- `08_Verification` — evidence, test requirements, and claims boundaries
- `09_Roadmap` — start-to-finish research and development plan
- `10_Source_Canon` — selected source documents copied into the project
- `11_Recovery_Evidence` — prior recovery and transport artifacts
- `12_Future_Applications` — VÆLD, Clover, robotics
- `99_Inbox_for_Corrections` — drop point for future corrective uploads

## Live-project rule

Every future correction should update:

1. `01_Current_Model/CURRENT_WORKING_MODEL.md`
2. `00_Project_Control/DECISION_REGISTER.md`
3. `00_Project_Control/CHANGELOG.md`
4. `00_Project_Control/STATUS.json`
5. the source manifest and repository ZIP

No correction should silently erase the prior model.


## Language-first milestone

The project is now organized around the Genesis programming language.

The first mandatory language primitive is `portal`.

Start here:

- `04_Language/GENESIS_PROGRAMMING_LANGUAGE_SPEC_v0.1.md`
- `04_Language/GENESIS_PORTAL_CONSTRUCT_v0.1.md`
- `04_Language/GENESIS_CORE_GRAMMAR_v0.1.ebnf`
- `04_Language/examples/GENESIS_PORTAL_0.gen`


## Current language checkpoint

The project is in pre-formal Genesis language discovery.

Current working foundation:

```text
Geometric
  = candidate primitive data type

3 + 1 + 1 manifold
  = candidate native construction

colored chirality byte
  = local occupancy/chirality structure with site-level basin energy densities

portal
  = first language-development handle
```

Start here:

- `04_Language/CURRENT_GENESIS_LANGUAGE_MODEL.md`
- `04_Language/GEOMETRIC_PRIMITIVE_WORKING_MODEL.md`
- `04_Language/PORTAL_FIRST_LANGUAGE_ENTRY.md`
- `04_Language/OPEN_LANGUAGE_QUESTIONS.md`

- `04_Language/COLOR_INDEXED_PORTALS_WORKING_MODEL.md`

- `04_Language/RAINBOW_ROAD_WORKING_MODEL.md`
