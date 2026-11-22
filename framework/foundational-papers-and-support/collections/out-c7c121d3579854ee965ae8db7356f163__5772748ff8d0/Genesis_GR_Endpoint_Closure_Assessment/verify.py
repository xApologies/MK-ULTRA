"""Verify file integrity, not mathematical truth."""
from pathlib import Path
import hashlib, json, sys
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
fail=[]
for item in manifest['files']:
    path=root/item['path']
    if not path.is_file():
        fail.append({'path':item['path'],'error':'missing'})
        continue
    data=path.read_bytes()
    if len(data)!=item['bytes'] or hashlib.sha256(data).hexdigest()!=item['sha256']:
        fail.append({'path':item['path'],'error':'size or hash mismatch'})
print(json.dumps({'checked':len(manifest['files']),'failures':fail,'mathematical_validation':False},indent=2))
sys.exit(bool(fail))
