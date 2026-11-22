from pathlib import Path
import json, sqlite3, hashlib, sys
root=Path(__file__).resolve().parents[1]
errs=[]
# machine JSON
items=json.loads((root/'MACHINE/formal_items.json').read_text())
ids=[x['id'] for x in items]
if len(ids)!=len(set(ids)): errs.append('duplicate formal ids')
roots=json.loads((root/'MACHINE/roots.json').read_text())
if len(roots)!=20: errs.append(f'expected 20 roots, got {len(roots)}')
ops=json.loads((root/'MACHINE/operators.json').read_text())
if len(ops)!=7: errs.append(f'expected 7 operators, got {len(ops)}')
asp=json.loads((root/'MACHINE/aspects.json').read_text())
if len(asp)!=4: errs.append(f'expected 4 aspects, got {len(asp)}')
cc=json.loads((root/'MACHINE/candidate_compounds.json').read_text())
if len(cc)!=8400: errs.append(f'expected 8400 candidate compounds, got {len(cc)}')
# sqlite
con=sqlite3.connect(root/'MACHINE/genesis.sqlite')
cur=con.cursor()
if cur.execute('select count(*) from formal_items').fetchone()[0] != len(items): errs.append('sqlite formal item mismatch')
# theorem deps resolve
known=set(ids)
for src,dst,rel in cur.execute('select src,dst,relation from dependencies'):
    if src not in known: errs.append(f'unknown dependency src {src}')
    if dst not in known: errs.append(f'unknown dependency dst {dst}')
con.close()
print('PASS' if not errs else 'FAIL')
for e in errs: print(e)
sys.exit(1 if errs else 0)
