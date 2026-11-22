#!/usr/bin/env python3
import argparse,json,sqlite3,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; API=ROOT/'api'; LIVE=ROOT/'live_model'; LIB=ROOT/'library'; DB=ROOT/'db'/'astraeus_math.sqlite'
def load(p): return json.load(open(p,encoding='utf-8'))
def dump(p,o): open(p,'w',encoding='utf-8').write(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def resolve(h):
    a=load(API/'ALIAS_REGISTRY.json')
    if h.startswith('@') and h in {x['handle'] for x in a['aliases']}: return h
    for x in a['aliases']:
        if x['alias'].lower()==h.lower(): return x['handle']
    return h
def sync_handle(h,event_type='METADATA_SYNC'):
    h=resolve(h); objs=load(API/'OBJECT_REGISTRY.json'); edges=load(API/'EDGE_REGISTRY.json'); lib=load(LIB/'QMO_METADATA_LIBRARY.json')
    o=next((x for x in objs['objects'] if x['handle']==h),None)
    if not o: return {'error':'unknown QMO','qmo_address':h}
    r=lib['qmo'].get(h)
    if not r: return {'error':'metadata address missing','qmo_address':h}
    old_status=r.get('status'); old_def=(r.get('meaning') or {}).get('definition') or ''
    r['status']=o.get('status'); r['meaning']['definition']=o.get('definition'); r['native_metadata']=o.get('metadata') or {}; r['revision']['metadata_revision']=int(r['revision'].get('metadata_revision',1))+1
    inc=[e for e in edges['edges'] if e['target']==h]; out=[e for e in edges['edges'] if e['source']==h]
    r['relations'].update({'incoming_count':len(inc),'outgoing_count':len(out),'incoming_edge_ids':[e['edge_id'] for e in inc],'outgoing_edge_ids':[e['edge_id'] for e in out]})
    lib['qmo'][h]=r; dump(LIB/'QMO_METADATA_LIBRARY.json',lib)
    reg=load(API/'QMO_METADATA_REGISTRY.json'); reg['records']=[r if x['qmo_address']==h else x for x in reg['records']]; dump(API/'QMO_METADATA_REGISTRY.json',reg)
    st=load(API/'LIVE_RUNTIME_STATE.json'); rel=st.get('api_release'); lr=st.get('live_model_revision'); ev={'event_type':event_type,'qmo_address':h,'api_release':rel,'live_model_revision':lr,'from_status':old_status,'to_status':r['status'],'from_definition_hash':hashlib.sha256(old_def.encode()).hexdigest(),'to_definition_hash':hashlib.sha256(((r['meaning']['definition'] or '')).encode()).hexdigest()}
    with open(LIVE/'QMO_METADATA_HISTORY.jsonl','a',encoding='utf-8') as f: f.write(json.dumps(ev,ensure_ascii=False)+'\n')
    con=sqlite3.connect(DB); cur=con.cursor(); cur.execute('UPDATE qmo_metadata SET status=?,definition=?,relations_json=?,revision_json=?,raw_json=? WHERE qmo_address=?',(r['status'],r['meaning']['definition'],json.dumps(r['relations'],ensure_ascii=False),json.dumps(r['revision'],ensure_ascii=False),json.dumps(r,ensure_ascii=False),h)); cur.execute('INSERT INTO qmo_metadata_history(qmo_address,event_type,api_release,live_model_revision,status,definition_hash,provenance_hash,raw_json) VALUES(?,?,?,?,?,?,?,?)',(h,event_type,rel,lr,r['status'],ev['to_definition_hash'],hashlib.sha256(json.dumps(r['provenance'],sort_keys=True).encode()).hexdigest(),json.dumps(ev,ensure_ascii=False))); con.commit(); con.close()
    return {'synced':h,'event':ev}
p=argparse.ArgumentParser(); sp=p.add_subparsers(dest='cmd',required=True); a=sp.add_parser('sync'); a.add_argument('handle'); a.add_argument('--event',default='METADATA_SYNC'); a=sp.add_parser('validate')
args=p.parse_args()
if args.cmd=='sync': out=sync_handle(args.handle,args.event)
else:
    lib=load(LIB/'QMO_METADATA_LIBRARY.json'); objs=load(API/'OBJECT_REGISTRY.json'); hs={o['handle'] for o in objs['objects']}; ls=set(lib['qmo']); out={'valid':hs==ls,'object_handles':len(hs),'metadata_addresses':len(ls),'missing_metadata':sorted(hs-ls),'orphan_metadata':sorted(ls-hs)}
print(json.dumps(out,indent=2,ensure_ascii=False))
