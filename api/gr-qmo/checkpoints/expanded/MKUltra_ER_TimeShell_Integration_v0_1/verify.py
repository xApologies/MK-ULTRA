"""Verify the delivered immutable payload; a fresh test run changes its timed result."""
from pathlib import Path
import hashlib,json
base=Path(__file__).resolve().parent
manifest=json.loads((base/'MANIFEST.json').read_text())
errors=[]
for item in manifest['files']:
    p=(base/item['path']).resolve()
    if not p.is_relative_to(base.resolve()) or not p.is_file():
        errors.append(item['path']+': missing or unsafe');continue
    b=p.read_bytes()
    if len(b)!=item['bytes'] or hashlib.sha256(b).hexdigest()!=item['sha256']:
        errors.append(item['path']+': checksum mismatch')
print(json.dumps({'checked':len(manifest['files']),'passed':not errors,'errors':errors},indent=2))
raise SystemExit(bool(errors))
