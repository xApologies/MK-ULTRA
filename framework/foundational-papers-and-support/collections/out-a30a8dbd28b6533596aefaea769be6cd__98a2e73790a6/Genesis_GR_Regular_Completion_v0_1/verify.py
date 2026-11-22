"""Verify the saved payload bytes against MANIFEST.json (integrity, not proof)."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
errors=[]
for item in manifest['files']:
    p=root/item['path']
    if not p.is_file():errors.append('missing: '+item['path']);continue
    b=p.read_bytes()
    if len(b)!=item['size'] or hashlib.sha256(b).hexdigest()!=item['sha256']:
        errors.append('changed: '+item['path'])
print(json.dumps({'verified':not errors,'checked':len(manifest['files']),'errors':errors},indent=2))
raise SystemExit(1 if errors else 0)
