"""Create a new byte-integrity manifest. A digest is not an authenticity/proof claim."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from tools.integrity import sha256

def main():
    records=[]
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file():continue
        relative=p.relative_to(ROOT)
        if p.name=='MANIFEST.json' or '__pycache__' in relative.parts or 'reruns' in relative.parts or p.name.endswith('.pyc'):continue
        records.append({'path':relative.as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p)})
    out={'schema':'GR_QMO_COMPLETE_RELEASE_MANIFEST_v1','version':'1.0.0','scope':'complete GR/QMO payload and active-graph integrity','excluded':['MANIFEST.json','__pycache__','*.pyc','reruns/'],'file_count':len(records),'files':records}
    (ROOT/'MANIFEST.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'file_count':len(records),'bytes':sum(v['bytes'] for v in records)}))
if __name__=='__main__':main()
