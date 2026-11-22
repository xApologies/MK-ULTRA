"""Verify original packaged file bytes. Run from any directory."""
from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
errors=[]
for r in manifest['files']:
    p=root/r['path']
    if not p.is_file():errors.append({'path':r['path'],'error':'missing'});continue
    b=p.read_bytes()
    if len(b)!=r['bytes'] or hashlib.sha256(b).hexdigest()!=r['sha256']:
        errors.append({'path':r['path'],'error':'content mismatch'})
print(json.dumps({'checked':len(manifest['files']),'errors':errors,'passed':not errors},indent=2))
sys.exit(bool(errors))
