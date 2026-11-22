# Dependency Graph + Dependency Chain Upgrade

**API release:** 0.7.0  
**Live-model revision:** v0.20.0

## Core distinction

- **Dependency Graph QMO**: focused registered graph object (path / induced / ego).
- **Dependency Landscape QMO**: recursive/merged dependency network; inputs may be QMO, Dependency Graph, or Dependency Landscape.
- **Dependency Chain QMO**: ordered history-bearing recursion of crawl -> graph -> landscape -> resolved QMO.

## Chain stop states

`CLOSED_FIXED_POINT`, `OPEN_FRONTIER`, `OPEN_FORK`, `FORK`, `CYCLE_DETECTED`, `MAX_STEPS`.

A chain becomes a closed subdomain only when its terminal state is `CLOSED_FIXED_POINT` and its construction/closure obligations validate. Open/forked chains remain queryable QMOs and preserve full History.

## User-directed rule

A dependency chain may require multiple recursive links before a closed object emerges. The chain itself may become a domain if it closes under its declared dependency/closure contract.
