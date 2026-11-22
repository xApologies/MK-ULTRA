# Module Loading

```text
Runtime
  │
  └── load(BRANE package)
          ├── load Collapse Intelligence module
          ├── mount API module read-only
          ├── connect Library module
          ├── negotiate contracts
          └── expose one sealed BRANE endpoint
```

Upgrades remain modular:

```text
Replace API only     → reload BRANE composition
Replace Library only → reload BRANE composition
Replace AI only      → rerun invariant regression tests
```
