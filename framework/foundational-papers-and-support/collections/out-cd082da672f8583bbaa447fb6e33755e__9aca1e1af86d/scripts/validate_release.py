from pathlib import Path
import hashlib, json, sys
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'PACKAGE_MANIFEST.json').read_text())
errors=[]
for rec in manifest['files']:
 p=root/rec['path']
 if not p.is_file(): errors.append('missing '+rec['path']); continue
 h=hashlib.sha256(p.read_bytes()).hexdigest()
 if h!=rec['sha256']: errors.append('hash '+rec['path'])
print(json.dumps({'status':'PASS' if not errors else 'FAIL','files':len(manifest['files']),'errors':errors},indent=2))
sys.exit(bool(errors))
