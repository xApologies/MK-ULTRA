"""Verify the payload against MANIFEST.json. Integrity is not theorem validity."""
from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
failures=[]
for entry in manifest['files']:
    path=root/entry['path']
    if not path.is_file():failures.append({'path':entry['path'],'problem':'missing'});continue
    data=path.read_bytes()
    if len(data)!=entry['bytes'] or hashlib.sha256(data).hexdigest()!=entry['sha256']:
        failures.append({'path':entry['path'],'problem':'size or checksum mismatch'})
print(json.dumps({'status':'PASS' if not failures else 'FAIL','checked_files':len(manifest['files']),'failures':failures},indent=2))
sys.exit(0 if not failures else 1)
