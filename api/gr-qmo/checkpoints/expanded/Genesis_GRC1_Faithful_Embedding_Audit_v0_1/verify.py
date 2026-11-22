"""Verify exact packaged payload hashes. Integrity is not mathematical validity."""
from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
errors=[]
for item in manifest['files']:
 p=root/item['path']
 if not p.is_file():errors.append({'path':item['path'],'error':'missing'});continue
 if p.stat().st_size!=item['bytes']:errors.append({'path':item['path'],'error':'size'})
 if hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:errors.append({'path':item['path'],'error':'sha256'})
print(json.dumps({'verified':not errors,'checked':len(manifest['files']),'errors':errors},indent=2))
sys.exit(bool(errors))
