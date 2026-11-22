# QMO Mini API

Canonical database: `../database/thread_continuity_qmo.sqlite`

Run:

```bash
python api/qmo_api.py
```

Default endpoint: `http://127.0.0.1:8766`

Useful QMO addresses:
- `@primitive/cradle`
- `@carrier/white`
- `@group/v4`
- `@space/riemann_sphere`
- `@pipeline/t0` … `@pipeline/t5`
- `@concept/genesis_rank`
- `@target/su2`
- `@target/su3`
- `@open/genesis_rank`

Routes:
- `/qmo`
- `/qmo/<address-or-alias>`
- `/qmo/<address-or-alias>/relations`
- `/equations`
- `/theorems`
- `/hypotheses`
- `/open`
- `/chronology`
- `/sources`
- `/supersession`
- `/artifacts`
- `/search?q=...`
