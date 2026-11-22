#!/usr/bin/env python3
import argparse, json, sqlite3, hashlib, subprocess, sys
from pathlib import Path
from collections import deque
ROOT=Path(__file__).resolve().parents[1]
API=ROOT/'api'; DB=ROOT/'db'/'astraeus_math.sqlite'
def load(name): return json.load(open(API/name,encoding='utf-8'))
def dump(name,obj):
    with open(API/name,'w',encoding='utf-8') as f: json.dump(obj,f,indent=2,ensure_ascii=False)
def state_hash():
    h=hashlib.sha256()
    for n in ['OBJECT_REGISTRY.json','EDGE_REGISTRY.json','CLOSURE_CERTIFICATE_REGISTRY.json']:
        h.update((API/n).read_bytes())
    return h.hexdigest()
def cert_valid(c): return c.get('status')=='VALID' and all(c.get('obligations',{}).values())
def promote(commit=False):
    objs=load('OBJECT_REGISTRY.json'); cands=load('CANDIDATE_REGISTRY.json'); certs=load('CLOSURE_CERTIFICATE_REGISTRY.json')
    by={o['handle']:o for o in objs['objects']}; cb={c['handle']:c for c in cands['candidates']}; changes=[]
    for cert in certs['certificates']:
        h=cert['handle']
        if cert_valid(cert) and h in by and by[h]['status'] in ('INTERNAL_CANDIDATE','CANDIDATE'):
            changes.append({'handle':h,'from':by[h]['status'],'to':'DERIVED_CLOSED_INTERNAL','certificate':cert['certificate_id']})
            if commit:
                by[h]['status']='DERIVED_CLOSED_INTERNAL'; by[h].setdefault('metadata',{})['closure_certificate']=cert['certificate_id']
                if h in cb: cb[h]['audit_status']='SELF_PROMOTED_INTERNAL_CLOSURE'; cb[h]['status']='DERIVED_CLOSED_INTERNAL'
    if commit and changes:
        objs['objects']=sorted(by.values(), key=lambda o:o['handle']); objs['object_count']=len(objs['objects']); dump('OBJECT_REGISTRY.json',objs); dump('CANDIDATE_REGISTRY.json',cands)
        con=sqlite3.connect(DB); cur=con.cursor()
        for ch in changes:
            cur.execute('UPDATE objects SET status=?, metadata_json=? WHERE handle=?',(ch['to'],json.dumps(by[ch['handle']].get('metadata',{}),ensure_ascii=False),ch['handle']))
            cur.execute('UPDATE candidates SET status=?, audit_status=? WHERE handle=?',(ch['to'],'SELF_PROMOTED_INTERNAL_CLOSURE',ch['handle']))
        con.commit(); con.close()
        sync_script=ROOT/'runtime'/'qmo_live_model.py'
        for ch in changes:
            subprocess.run([sys.executable,str(sync_script),'sync',ch['handle'],'--event','CLOSURE_PROMOTION'],capture_output=True,text=True,check=True)
    return changes

def traverse(laps=1,commit=False):
    st=load('LIVE_RUNTIME_STATE.json'); hist_path=ROOT/'runtime'/'ROAD_HISTORY.jsonl'; events=[]
    orient=st.get('road_orientation','WHITE_SUPERPOSE')
    for _ in range(laps):
        before=orient; orient='BLACK_NEON' if orient=='WHITE_SUPERPOSE' else 'WHITE_SUPERPOSE'
        token='RRH-'+hashlib.sha256((state_hash()+before+orient+str(hist_path.stat().st_size if hist_path.exists() else 0)).encode()).hexdigest()[:12]
        ev={'history_token':token,'from_presentation':before,'to_presentation':orient,'semantic_state_hash':state_hash(),'law':'return does not reset History'}
        events.append(ev)
        if commit:
            with open(hist_path,'a',encoding='utf-8') as f: f.write(json.dumps(ev,ensure_ascii=False)+'\n')
    if commit:
        st['road_orientation']=orient; st['road_history_token']=events[-1]['history_token'] if events else st.get('road_history_token'); dump('LIVE_RUNTIME_STATE.json',st)
    return events

def impact_native(changes):
    ej=load('EDGE_REGISTRY.json'); inc=load('INCOMPATIBILITY_REGISTRY.json'); certs=load('CLOSURE_CERTIFICATE_REGISTRY.json')
    changed=set(); asserted=[]; conflicts=[]
    for ch in changes:
        if ch.get('op')=='assert_edge':
            changed|={ch['source'],ch['target']}; asserted.append((ch['source'],ch['relation'],ch['target']))
    # direct hard guard match, symmetric endpoints only for SAME_AS
    for s,r,t in asserted:
        for g in inc['guards']:
            direct=(r==g['relation'] and s==g['left'] and t==g['right'])
            symmetric=(r=='SAME_AS' and g['relation']=='SAME_AS' and s==g['right'] and t==g['left'])
            if direct or symmetric: conflicts.append(g)
    graph={}
    for e in ej['edges']:
        graph.setdefault(e['source'],set()).add(e['target'])
        # dependency impact can flow through relations both ways for revalidation scope
        graph.setdefault(e['target'],set()).add(e['source'])
    q=deque((h,0) for h in changed); seen=set(changed); layers={0:sorted(changed)}
    while q:
        n,d=q.popleft()
        if d>=4: continue
        for nxt in graph.get(n,set()):
            if nxt not in seen:
                seen.add(nxt); layers.setdefault(d+1,[]).append(nxt); q.append((nxt,d+1))
    invalid=[]
    for c in certs['certificates']:
        if set(c.get('premises',[])) & seen: invalid.append(c['certificate_id'])
    return {'changed_handles':sorted(changed),'impact_layers':{str(k):sorted(v) for k,v in layers.items()},'hard_guard_conflicts':conflicts,'certificates_requiring_revalidation':invalid,'canonical_mutation':False}

def impact_toy(scenario):
    toy=json.load(open(ROOT/scenario['toy_domain'],encoding='utf-8')); objs=toy['objects']; changed=set();
    for ch in scenario['changes']:
        if ch['op']=='set_attribute': changed.add(ch['object'])
    # reverse dependency map
    rev={}
    for h,o in objs.items():
        for dep in o.get('depends_on',[]): rev.setdefault(dep,set()).add(h)
    q=deque((h,0) for h in changed); seen=set(changed); layers={0:sorted(changed)}
    while q:
        n,d=q.popleft()
        for nxt in rev.get(n,set()):
            if nxt not in seen:
                seen.add(nxt); layers.setdefault(d+1,[]).append(nxt); q.append((nxt,d+1))
    return {'changed_handles':sorted(changed),'impact_layers':{str(k):sorted(v) for k,v in layers.items()},'note':toy['interpretation'],'canonical_mutation':False}

def perturb(sid):
    reg=load('PERTURBATION_REGISTRY.json'); sc=next((s for s in reg['scenarios'] if s['scenario_id']==sid),None)
    if not sc: return {'error':'unknown scenario'}
    res=impact_toy(sc) if sc.get('toy_domain') else impact_native(sc['changes']); res.update({'scenario_id':sid,'name':sc['name'],'kind':sc['kind'],'expected':sc['expected']}); return res

p=argparse.ArgumentParser(description='Rainbow Road recursive closure runtime')
sp=p.add_subparsers(dest='cmd',required=True)
a=sp.add_parser('status')
a=sp.add_parser('close'); a.add_argument('--commit',action='store_true')
a=sp.add_parser('traverse'); a.add_argument('--laps',type=int,default=1); a.add_argument('--commit',action='store_true')
a=sp.add_parser('history')
a=sp.add_parser('perturb'); a.add_argument('scenario_id')
a=sp.add_parser('certificates')
args=p.parse_args()
if args.cmd=='status': out={'domain':load('DOMAIN_REGISTRY.json')['active_domain'],'runtime':load('LIVE_RUNTIME_STATE.json'),'promotable':promote(False)}
elif args.cmd=='close': out={'promotions':promote(args.commit),'commit':args.commit,'state_hash':state_hash()}
elif args.cmd=='traverse': out={'events':traverse(args.laps,args.commit),'commit':args.commit}
elif args.cmd=='history':
    hp=ROOT/'runtime'/'ROAD_HISTORY.jsonl'; out=[json.loads(x) for x in hp.read_text(encoding='utf-8').splitlines()] if hp.exists() else []
elif args.cmd=='perturb': out=perturb(args.scenario_id)
elif args.cmd=='certificates': out=load('CLOSURE_CERTIFICATE_REGISTRY.json')
print(json.dumps(out,indent=2,ensure_ascii=False))
