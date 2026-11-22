#!/usr/bin/env python3
import argparse, json, sqlite3, subprocess, sys
from pathlib import Path
from collections import deque
DB=Path(__file__).resolve().parents[1]/"db"/"astraeus_math.sqlite"

def conn():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c

def asdicts(rows): return [dict(r) for r in rows]
def resolve(cur,h):
    if h.startswith('@'): return h
    cur.execute('SELECT handle FROM aliases WHERE lower(alias)=lower(?) LIMIT 1',(h,)); r=cur.fetchone(); return r['handle'] if r else h

COMMAND_ADDRESS_TO_RUNTIME = {
    '@help': 'help',
    '@qmo': 'qmo',
    '@meta': 'meta',
    '@meaning': 'meaning',
    '@qmo_history': 'qmo-history',
    '@object': 'object',
    '@neighbors': 'neighbors',
    '@search': 'search',
    '@path': 'path',
    '@equation': 'equation',
    '@theorem': 'theorem',
    '@branch': 'branch',
    '@frontier': 'frontier',
    '@candidates': 'candidates',
    '@source': 'source',
    '@why': 'why',
    '@crawl': 'crawl',
    '@domain': 'domain',
    '@closure_contract': 'closure-contract',
    '@certificates': 'certificates',
    '@perturbations': 'perturbations',
    '@runtime_state': 'runtime-state',
    '@api_live': 'api-live',
    '@dependency_landscape': 'dependency-landscape',
    '@landscape': 'landscape',
    '@landscapes': 'landscapes',
    '@landscape_history': 'landscape-history',
    '@dependency_graph': 'dependency-graph',
    '@graph': 'graph',
    '@graphs': 'graphs',
    '@graph_history': 'graph-history',
    '@dependency_chain': 'dependency-chain',
    '@chain': 'chain',
    '@chains': 'chains',
    '@chain_history': 'chain-history',
    '@qmo_types': 'qmo-types',
    '@graph_types': 'graph-types',
}
# Structural command namespace is positional: first token may be an @command.
# QMO/landscape @handles remain mathematical addresses in argument positions.
if len(sys.argv)>1:
    first=sys.argv[1]
    if first in COMMAND_ADDRESS_TO_RUNTIME:
        sys.argv[1]=COMMAND_ADDRESS_TO_RUNTIME[first]
    elif first=='/help':
        sys.argv[1]='help'  # deprecated compatibility alias; canonical surface is @help

p=argparse.ArgumentParser(description='Astraeus Object Mathematics API')
sp=p.add_subparsers(dest='cmd',required=True)
a=sp.add_parser('object'); a.add_argument('handle')
a=sp.add_parser('neighbors'); a.add_argument('handle'); a.add_argument('--direction',choices=['in','out','both'],default='both')
a=sp.add_parser('search'); a.add_argument('query'); a.add_argument('--limit',type=int,default=20)
a=sp.add_parser('path'); a.add_argument('source'); a.add_argument('target'); a.add_argument('--depth',type=int,default=8)
a=sp.add_parser('equation'); a.add_argument('handle')
a=sp.add_parser('theorem'); a.add_argument('handle')
a=sp.add_parser('branch'); a.add_argument('branch')
a=sp.add_parser('frontier')
a=sp.add_parser('candidates')
a=sp.add_parser('source'); a.add_argument('source_id')
a=sp.add_parser('why'); a.add_argument('handle')
a=sp.add_parser('crawl'); a.add_argument('handle',nargs='?',default='@object_resolution_recovery_witness_minimality'); a.add_argument('--depth',type=int,default=2)
a=sp.add_parser('domain')
a=sp.add_parser('closure-contract')
a=sp.add_parser('certificates')
a=sp.add_parser('perturbations')
a=sp.add_parser('runtime-state')
a=sp.add_parser('qmo'); a.add_argument('handle')
a=sp.add_parser('meta'); a.add_argument('handle')
a=sp.add_parser('meaning'); a.add_argument('handle')
a=sp.add_parser('qmo-history'); a.add_argument('handle')
a=sp.add_parser('api-live')
a=sp.add_parser('help'); a.add_argument('topic',nargs='?')
a=sp.add_parser('dependency-landscape'); a.add_argument('inputs',nargs='+'); a.add_argument('--depth',type=int,default=2); a.add_argument('--direction',choices=['upstream','downstream','bidirectional'],default='bidirectional'); a.add_argument('--register',action='store_true'); a.add_argument('--handle')
a=sp.add_parser('landscape'); a.add_argument('handle')
a=sp.add_parser('landscapes')
a=sp.add_parser('landscape-history'); a.add_argument('handle',nargs='?')
a=sp.add_parser('dependency-graph'); a.add_argument('inputs',nargs='+'); a.add_argument('--mode',choices=['path','induced','ego'],default='path'); a.add_argument('--depth',type=int,default=1); a.add_argument('--direction',choices=['upstream','downstream','bidirectional'],default='bidirectional'); a.add_argument('--register',action='store_true'); a.add_argument('--handle')
a=sp.add_parser('graph'); a.add_argument('handle')
a=sp.add_parser('graphs')
a=sp.add_parser('graph-history'); a.add_argument('handle',nargs='?')
a=sp.add_parser('dependency-chain'); a.add_argument('seed'); a.add_argument('--max-steps',type=int,default=5); a.add_argument('--landscape-depth',type=int,default=1); a.add_argument('--direction',choices=['upstream','downstream','bidirectional'],default='bidirectional'); a.add_argument('--register',action='store_true'); a.add_argument('--handle')
a=sp.add_parser('chain'); a.add_argument('handle')
a=sp.add_parser('chains')
a=sp.add_parser('chain-history'); a.add_argument('handle',nargs='?')
a=sp.add_parser('qmo-types')
a=sp.add_parser('graph-types')
args=p.parse_args(); con=conn(); cur=con.cursor()

if args.cmd=='object':
    h=resolve(cur,args.handle); cur.execute('SELECT * FROM objects WHERE handle=?',(h,)); r=cur.fetchone(); out=dict(r) if r else None
elif args.cmd=='neighbors':
    h=resolve(cur,args.handle); out=[]
    if args.direction in ('out','both'): cur.execute('SELECT * FROM edges WHERE source=?',(h,)); out+=asdicts(cur.fetchall())
    if args.direction in ('in','both'): cur.execute('SELECT * FROM edges WHERE target=?',(h,)); out+=asdicts(cur.fetchall())
elif args.cmd=='search':
    q=args.query.replace('"',' ')
    try: cur.execute('SELECT handle,text FROM search_fts WHERE search_fts MATCH ? LIMIT ?',(q,args.limit))
    except sqlite3.OperationalError: cur.execute('SELECT handle,text FROM search_fts WHERE text LIKE ? LIMIT ?',(f'%{q}%',args.limit))
    out=asdicts(cur.fetchall())
elif args.cmd=='path':
    s,t=resolve(cur,args.source),resolve(cur,args.target); cur.execute('SELECT source,relation,target,status FROM edges'); graph={}
    for r in cur.fetchall(): graph.setdefault(r['source'],[]).append((r['relation'],r['target'],r['status']))
    q=deque([(s,[])]); seen={s}; found=None
    while q:
        n,path=q.popleft()
        if len(path)>=args.depth: continue
        for rel,nxt,status in graph.get(n,[]):
            np=path+[(n,rel,nxt,status)]
            if nxt==t: found=np; q.clear(); break
            if nxt not in seen: seen.add(nxt); q.append((nxt,np))
    out={'found':found is not None,'path':found}
elif args.cmd=='equation':
    h=resolve(cur,args.handle); cur.execute('SELECT * FROM equations WHERE handle=?',(h,)); r=cur.fetchone(); out=dict(r) if r else None
elif args.cmd=='theorem':
    h=resolve(cur,args.handle); cur.execute('SELECT * FROM theorems WHERE handle=?',(h,)); r=cur.fetchone(); out=dict(r) if r else None
elif args.cmd=='branch':
    cur.execute('SELECT * FROM objects WHERE branch=? ORDER BY handle',(args.branch,)); out=asdicts(cur.fetchall())
elif args.cmd=='frontier':
    cur.execute('SELECT * FROM frontier ORDER BY priority,status'); out=asdicts(cur.fetchall())
elif args.cmd=='candidates':
    cur.execute('SELECT * FROM candidates ORDER BY candidate_id'); out=asdicts(cur.fetchall())
elif args.cmd=='source':
    cur.execute('SELECT * FROM sources WHERE source_id=?',(args.source_id,)); r=cur.fetchone(); out=dict(r) if r else None
elif args.cmd=='why':
    h=resolve(cur,args.handle); cur.execute('SELECT * FROM objects WHERE handle=?',(h,)); obj=cur.fetchone(); cur.execute('SELECT * FROM edges WHERE target=?',(h,)); inbound=asdicts(cur.fetchall()); cur.execute('SELECT * FROM edges WHERE source=?',(h,)); outbound=asdicts(cur.fetchall()); out={'object':dict(obj) if obj else None,'inbound':inbound,'outbound':outbound}
elif args.cmd=='domain': out=json.load(open(DB.parent.parent/'api'/'DOMAIN_REGISTRY.json',encoding='utf-8'))
elif args.cmd=='closure-contract': out=json.load(open(DB.parent.parent/'api'/'CLOSURE_CONTRACT.json',encoding='utf-8'))
elif args.cmd=='certificates': out=json.load(open(DB.parent.parent/'api'/'CLOSURE_CERTIFICATE_REGISTRY.json',encoding='utf-8'))
elif args.cmd=='perturbations': out=json.load(open(DB.parent.parent/'api'/'PERTURBATION_REGISTRY.json',encoding='utf-8'))
elif args.cmd=='runtime-state': out=json.load(open(DB.parent.parent/'api'/'LIVE_RUNTIME_STATE.json',encoding='utf-8'))
elif args.cmd=='meta':
    h=resolve(cur,args.handle); cur.execute('SELECT raw_json FROM qmo_metadata WHERE qmo_address=?',(h,)); r=cur.fetchone(); out=json.loads(r['raw_json']) if r else None
elif args.cmd=='meaning':
    h=resolve(cur,args.handle); cur.execute('SELECT qmo_address,definition,type,branch,status FROM qmo_metadata WHERE qmo_address=?',(h,)); r=cur.fetchone(); out=dict(r) if r else None
elif args.cmd=='qmo-history':
    h=resolve(cur,args.handle); cur.execute('SELECT raw_json FROM qmo_metadata_history WHERE qmo_address=? ORDER BY event_id',(h,)); out=[json.loads(r['raw_json']) for r in cur.fetchall()]
elif args.cmd=='qmo':
    h=resolve(cur,args.handle); cur.execute('SELECT * FROM objects WHERE handle=?',(h,)); o=cur.fetchone(); cur.execute('SELECT raw_json FROM qmo_metadata WHERE qmo_address=?',(h,)); m=cur.fetchone(); out={'qmo_address':h,'object':dict(o) if o else None,'metadata':json.loads(m['raw_json']) if m else None}
elif args.cmd=='api-live': out=json.load(open(DB.parent.parent/'live_model'/'API_LIVE_MODEL.json',encoding='utf-8'))
elif args.cmd=='help':
    h=json.load(open(DB.parent.parent/'api'/'COMMAND_REGISTRY.json',encoding='utf-8'))
    if args.topic:
        q=args.topic.lower().lstrip('@').replace('-','_')
        def match(x):
            blob=' '.join([x.get('address',''),x.get('runtime_name',''),x.get('syntax',''),x.get('purpose',''),x.get('category','')]).lower().replace('-','_')
            return q in blob
        out={'topic':args.topic,'canonical_help':'@help','namespace':h['namespace'],'matches':[x for x in h['commands'] if match(x)]}
    else:
        out={'canonical_help':'@help','namespace':h['namespace'],'semantic_rule':h['semantic_rule'],'resolution_rule':h['resolution_rule'],'command_count':h['command_count'],'commands':h['commands']}
elif args.cmd=='dependency-landscape':
    sub='register' if args.register else 'preview'; cmd=[sys.executable,str(DB.parent.parent/'runtime'/'dependency_landscape.py'),sub,*args.inputs,'--depth',str(args.depth),'--direction',args.direction];
    if args.register and args.handle: cmd += ['--handle',args.handle]
    cp=subprocess.run(cmd,capture_output=True,text=True,check=True); out=json.loads(cp.stdout)
elif args.cmd=='landscape':
    cp=subprocess.run([sys.executable,str(DB.parent.parent/'runtime'/'dependency_landscape.py'),'get',args.handle],capture_output=True,text=True,check=True); out=json.loads(cp.stdout)
elif args.cmd=='landscapes':
    cp=subprocess.run([sys.executable,str(DB.parent.parent/'runtime'/'dependency_landscape.py'),'list'],capture_output=True,text=True,check=True); out=json.loads(cp.stdout)
elif args.cmd=='landscape-history':
    cmd=[sys.executable,str(DB.parent.parent/'runtime'/'dependency_landscape.py'),'history'] + ([args.handle] if args.handle else []); cp=subprocess.run(cmd,capture_output=True,text=True,check=True); out=json.loads(cp.stdout)
elif args.cmd=='dependency-graph':
    sub='register' if args.register else 'preview'; cmd=[sys.executable,str(DB.parent.parent/'runtime'/'dependency_graph.py'),sub,*args.inputs,'--mode',args.mode,'--depth',str(args.depth),'--direction',args.direction];
    if args.register and args.handle: cmd += ['--handle',args.handle]
    cp=subprocess.run(cmd,capture_output=True,text=True,check=True); out=json.loads(cp.stdout)
elif args.cmd=='graph':
    cp=subprocess.run([sys.executable,str(DB.parent.parent/'runtime'/'dependency_graph.py'),'get',args.handle],capture_output=True,text=True,check=True); out=json.loads(cp.stdout)
elif args.cmd=='graphs':
    cp=subprocess.run([sys.executable,str(DB.parent.parent/'runtime'/'dependency_graph.py'),'list'],capture_output=True,text=True,check=True); out=json.loads(cp.stdout)
elif args.cmd=='graph-history':
    cmd=[sys.executable,str(DB.parent.parent/'runtime'/'dependency_graph.py'),'history'] + ([args.handle] if args.handle else []); cp=subprocess.run(cmd,capture_output=True,text=True,check=True); out=json.loads(cp.stdout)
elif args.cmd=='dependency-chain':
    sub='register' if args.register else 'preview'; cmd=[sys.executable,str(DB.parent.parent/'runtime'/'dependency_chain.py'),sub,args.seed,'--max-steps',str(args.max_steps),'--landscape-depth',str(args.landscape_depth),'--direction',args.direction];
    if args.register and args.handle: cmd += ['--handle',args.handle]
    cp=subprocess.run(cmd,capture_output=True,text=True,check=True); out=json.loads(cp.stdout)
elif args.cmd=='chain':
    cp=subprocess.run([sys.executable,str(DB.parent.parent/'runtime'/'dependency_chain.py'),'get',args.handle],capture_output=True,text=True,check=True); out=json.loads(cp.stdout)
elif args.cmd=='chains':
    cp=subprocess.run([sys.executable,str(DB.parent.parent/'runtime'/'dependency_chain.py'),'list'],capture_output=True,text=True,check=True); out=json.loads(cp.stdout)
elif args.cmd=='chain-history':
    cmd=[sys.executable,str(DB.parent.parent/'runtime'/'dependency_chain.py'),'history'] + ([args.handle] if args.handle else []); cp=subprocess.run(cmd,capture_output=True,text=True,check=True); out=json.loads(cp.stdout)
elif args.cmd=='qmo-types': out=json.load(open(DB.parent.parent/'api'/'QMO_TYPE_REGISTRY.json',encoding='utf-8'))
elif args.cmd=='graph-types': out=json.load(open(DB.parent.parent/'api'/'GRAPH_TYPE_REGISTRY.json',encoding='utf-8'))
elif args.cmd=='crawl':
    start=resolve(cur,args.handle); q=deque([(start,0)]); seen={start}; nodes=[]; edge_out=[]
    while q:
        n,d=q.popleft(); cur.execute('SELECT handle,canonical_name,type,status,branch,definition FROM objects WHERE handle=?',(n,)); r=cur.fetchone();
        if r: nodes.append(dict(r))
        if d>=args.depth: continue
        cur.execute('SELECT source,relation,target,status,audit_status FROM edges WHERE source=?',(n,));
        for e in cur.fetchall():
            ed=dict(e); edge_out.append(ed); nxt=e['target']
            if nxt not in seen: seen.add(nxt); q.append((nxt,d+1))
    cur.execute('SELECT * FROM candidates WHERE handle IN (%s)'%(','.join('?'*len(seen))) if seen else "SELECT * FROM candidates WHERE 0", tuple(seen) if seen else ())
    cand=asdicts(cur.fetchall()) if seen else []
    out={'start':start,'nodes':nodes,'edges':edge_out,'candidate_records':cand,'policy':'Crawl expands declared dependencies. Candidates self-promote only with a valid internal Closure Certificate; domain extensions remain audit-gated.'}
print(json.dumps(out,indent=2,ensure_ascii=False))
