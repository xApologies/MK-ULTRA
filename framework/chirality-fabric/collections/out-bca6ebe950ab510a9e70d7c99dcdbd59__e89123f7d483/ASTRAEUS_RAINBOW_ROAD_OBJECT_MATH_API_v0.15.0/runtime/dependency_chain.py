#!/usr/bin/env python3
import argparse,json,sqlite3,hashlib,re,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];API=ROOT/'api';LIVE=ROOT/'live_model';LIB=ROOT/'library';DB=ROOT/'db'/'astraeus_math.sqlite';CLIB=LIB/'dependency_chains';CLIB.mkdir(parents=True,exist_ok=True)
def load(p):return json.load(open(p,encoding='utf-8'))
def dump(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def state():
 s=load(API/'LIVE_RUNTIME_STATE.json');return s.get('api_release','0.7.0'),s.get('live_model_revision','v0.20.0')
def resolve(h):
 if h.startswith('@'):return h
 for x in load(API/'ALIAS_REGISTRY.json')['aliases']:
  if x['alias'].lower()==h.lower():return x['handle']
 return h
def objects():return {o['handle']:o for o in load(API/'OBJECT_REGISTRY.json')['objects']}
def graphs():return {x['qmo_address']:x for x in load(API/'DEPENDENCY_GRAPH_REGISTRY.json')['graphs']}
def landscapes():return {x['qmo_address']:x for x in load(API/'DEPENDENCY_LANDSCAPE_REGISTRY.json')['landscapes']}
def chains():return {x['qmo_address']:x for x in load(API/'DEPENDENCY_CHAIN_REGISTRY.json')['chains']}
def math_edges():return [e for e in load(API/'EDGE_REGISTRY.json')['edges'] if e.get('graph_family') not in ('landscape_metadata','dependency_graph_metadata','dependency_chain_metadata')]
def focus_for(h):
 h=resolve(h);oset=objects();gs=graphs();ls=landscapes()
 if h in oset:return h,'qmo'
 if h in gs:
  g=gs[h];return (g.get('roots') or g.get('member_qmos'))[-1],'dependency_graph'
 if h in ls:
  L=ls[h];active=[x for x in L.get('member_qmos',[]) if (oset.get(x) or {}).get('status')=='ACTIVE_FRONTIER'];return (active[0] if len(active)==1 else (L.get('roots') or L.get('member_qmos'))[-1]),'landscape'
 raise SystemExit('unknown chain seed '+h)
def next_options(focus):
 es=math_edges();by={}
 for e in es:
  if e['source']==focus:by.setdefault(e['relation'],[]).append(e)
 priorities=['ADVANCES_TO','RESOLVES_TO','CLOSES_TO','DERIVES_TO','PROMOTES_TO']
 for rel in priorities:
  opts=by.get(rel,[])
  if opts:return {'kind':'progression','relation':rel,'edges':opts}
 exploratory=[]
 for rel in ['QUERIES','TESTS','REQUIRES','PROPOSES_TEST_OF','USES','READS']:
  exploratory+=by.get(rel,[])
 return {'kind':'exploration','relation':None,'edges':exploratory}
def preview(seed,max_steps=5,landscape_depth=1,direction='bidirectional'):
 seed=resolve(seed);focus,seed_kind=focus_for(seed);steps=[];visited=[focus];terminal=None
 for i in range(max_steps):
  op=next_options(focus);opts=op['edges']
  if op['kind']=='progression' and len(opts)==1:
   e=opts[0];nxt=e['target'];steps.append({'step':i+1,'input_focus':focus,'progression_relation':e['relation'],'resolved_qmo':nxt,'edge_id':e['edge_id'],'graph_handle':None,'landscape_handle':None});focus=nxt
   if focus in visited:terminal={'state':'CYCLE_DETECTED','focus':focus,'reason':'progression returned to an earlier focus'};break
   visited.append(focus);continue
  if op['kind']=='progression' and len(opts)>1:
   terminal={'state':'FORK','focus':focus,'relation':op['relation'],'candidates':[e['target'] for e in opts]};break
  obj=objects().get(focus,{});expl=[{'relation':e['relation'],'target':e['target'],'edge_id':e['edge_id']} for e in opts]
  if obj.get('status')=='ACTIVE_FRONTIER' or expl:terminal={'state':'OPEN_FRONTIER' if len(expl)<=1 else 'OPEN_FORK','focus':focus,'exploration_targets':expl}
  else:terminal={'state':'CLOSED_FIXED_POINT','focus':focus,'reason':'no registered progression/exploration edge under chain policy'}
  break
 else:terminal={'state':'MAX_STEPS','focus':focus,'reason':'chain step limit reached'}
 return {'seed':seed,'seed_kind':seed_kind,'initial_focus':visited[0],'steps':steps,'terminal':terminal,'visited_focuses':visited,'landscape_depth':landscape_depth,'direction':direction,'subdomain_eligibility':terminal['state']=='CLOSED_FIXED_POINT'}
def next_edge_id(es):
 ns=[]
 for e in es:
  m=re.fullmatch(r'E-(\d+)',e['edge_id']);
  if m:ns.append(int(m.group(1)))
 return f'E-{max(ns+[0])+1:05d}'
def refresh(meta,es):
 inc={};out={}
 for e in es:out.setdefault(e['source'],[]).append(e);inc.setdefault(e['target'],[]).append(e)
 for h,r in meta.items():
  ii=inc.get(h,[]);oo=out.get(h,[]);r['relations']={'incoming_count':len(ii),'outgoing_count':len(oo),'incoming_edge_ids':[e['edge_id'] for e in ii],'outgoing_edge_ids':[e['edge_id'] for e in oo],'incoming_relations':sorted({e['relation'] for e in ii}),'outgoing_relations':sorted({e['relation'] for e in oo}),'neighbors_in':sorted({e['source'] for e in ii}),'neighbors_out':sorted({e['target'] for e in oo})}
def default_handle(seed):return '@dc_'+hashlib.sha256(seed.encode()).hexdigest()[:12]
def run_json(cmd):
 cp=subprocess.run(cmd,capture_output=True,text=True,check=True);return json.loads(cp.stdout)
def register(seed,max_steps,landscape_depth,direction,handle=None):
 rel,lr=state();seed=resolve(seed);h=resolve(handle) if handle else default_handle(seed);h=h if h.startswith('@') else '@'+h
 creg=load(API/'DEPENDENCY_CHAIN_REGISTRY.json');ex=next((x for x in creg['chains'] if x['qmo_address']==h),None)
 if ex:return {'registered':False,'reason':'already_registered','chain':ex}
 pv=preview(seed,max_steps,landscape_depth,direction);prev_land=None
 for st in pv['steps']:
  idx=st['step'];gh=f"{h}_g{idx:02d}";lh=f"{h}_l{idx:02d}"
  g=run_json([sys.executable,str(ROOT/'runtime'/'dependency_graph.py'),'register',st['input_focus'],st['resolved_qmo'],'--mode','path','--depth','1','--direction','downstream','--handle',gh]);st['graph_handle']=g.get('qmo_address',gh)
  inputs=[st['graph_handle']] if prev_land is None else [prev_land,st['graph_handle']]
  l=run_json([sys.executable,str(ROOT/'runtime'/'dependency_landscape.py'),'register',*inputs,'--depth',str(landscape_depth),'--direction',direction,'--handle',lh]);st['landscape_handle']=l.get('qmo_address',lh);prev_land=st['landscape_handle']
 cid='DC-'+hashlib.sha256((h+'|'+seed).encode()).hexdigest()[:12];closed=pv['terminal']['state']=='CLOSED_FIXED_POINT';status='DERIVED_CLOSED_INTERNAL' if closed else 'ACTIVE_DEPENDENCY_CHAIN'
 rec={**pv,'chain_id':cid,'qmo_address':h,'canonical_name':'Dependency Chain: '+seed,'status':status,'construction':{'operator':'@dependency_chain','progression_policy':['ADVANCES_TO','RESOLVES_TO','CLOSES_TO','DERIVES_TO','PROMOTES_TO'],'max_steps':max_steps,'landscape_depth':landscape_depth,'direction':direction,'member_claim_promotion':False},'history':{'policy':'APPEND_ONLY','created_in_api_release':rel,'created_live_model_revision':lr,'step_count':len(pv['steps'])},'resolution_context':{'operator':'@resolution','policy':'EACH_CHAIN_STEP_HAS_ITS_OWN_GRAPH/LANDSCAPE_RESOLUTION; CHAIN_ORDER_PRESERVED'},'bandwidth_context':{'operator':'@bandwidth_algebra','policy':'ONLY_REGISTERED_PROGRESSIONS_AND_EDGES_AVAILABLE_TO_CHAIN'},'domain_state':'CLOSED_SUBDOMAIN_ELIGIBLE' if closed else 'OPEN_NOT_A_DOMAIN','provenance':['GENESIS_DIRECTION::2026-08-22_dependency_chain','QMO:'+seed]+[f"QMO:{x['graph_handle']}" for x in pv['steps']]+[f"QMO:{x['landscape_handle']}" for x in pv['steps']],'semantic_guard':'A Dependency Chain records recursive resolution History. Chain construction does not promote member claims. Domain status requires an independently valid terminal closure condition.'}
 O=load(API/'OBJECT_REGISTRY.json');E=load(API/'EDGE_REGISTRY.json');A=load(API/'ALIAS_REGISTRY.json');C=load(API/'CLOSURE_CERTIFICATE_REGISTRY.json');M=load(LIB/'QMO_METADATA_LIBRARY.json');RT=load(API/'LIVE_RUNTIME_STATE.json');AL=load(LIVE/'API_LIVE_MODEL.json');D=load(API/'DOMAIN_REGISTRY.json')
 o={'handle':h,'canonical_name':rec['canonical_name'],'type':'dependency chain QMO','status':status,'branch':'dependency_chain','definition':f"Dependency Chain QMO seeded by {seed}; contains {len(pv['steps'])} resolved progression step(s) and terminates in state {pv['terminal']['state']} at {pv['terminal']['focus']}.",'provenance':rec['provenance'],'source_status':'GENERATED_BY_RECURSIVE_DEPENDENCY_CHAIN_RUNTIME','metadata':{'chain_id':cid,'terminal':pv['terminal'],'resolution_context':rec['resolution_context'],'bandwidth_context':rec['bandwidth_context'],'history_policy':'APPEND_ONLY','domain_state':rec['domain_state'],'live_model_revision':lr}}
 O['objects'].append(o);O['object_count']=len(O['objects']);A['aliases'].append({'alias':h,'handle':h})
 def ae(s,r,t):
  eid=next_edge_id(E['edges']);E['edges'].append({'edge_id':eid,'source':s,'relation':r,'target':t,'graph_family':'dependency_chain_metadata','status':'DERIVED_ARCHITECTURE','confidence':'high','audit_status':'architectural','provenance':rec['provenance']})
 ae('@dependency_chain','CONSTRUCTS_CHAIN',h);ae(h,'HAS_CHAIN_SEED',seed)
 for st in pv['steps']:
  ae(h,'HAS_CHAIN_GRAPH',st['graph_handle']);ae(h,'HAS_CHAIN_LANDSCAPE',st['landscape_handle']);ae(h,'RESOLVES_CHAIN_STEP_TO',st['resolved_qmo'])
 ae(h,'TERMINATES_AT',pv['terminal']['focus']);E['edge_count']=len(E['edges'])
 cert={'certificate_id':'CERT-DC-'+cid.split('-',1)[1],'handle':h,'status':'VALID','domain':'@rainbow_road_recursive_domain','rule':'DEPENDENCY_CHAIN_CONSTRUCTION_V1','premises':[seed],'obligations':{'seed_registered':True,'step_edges_registered':True,'step_graphs_registered':True,'step_landscapes_registered':True,'history_attached':True,'provenance_complete':True,'member_status_preserved':True,'qmo_address_registered':True,'terminal_closure_valid':closed},'provenance':rec['provenance'],'semantic_guard':'Certificate validates chain construction. CLOSED_SUBDOMAIN status is permitted only when terminal_closure_valid is true.'};C['certificates'].append(cert);C['certificate_count']=len(C['certificates']);creg['chains'].append(rec);creg['chain_count']=len(creg['chains']);creg['api_release']=rel
 if closed:
  if not any(x.get('handle')==h for x in D.setdefault('closed_subdomains',[])):D['closed_subdomains'].append({'handle':h,'kind':'dependency_chain_subdomain','certificate_id':cert['certificate_id'],'status':'CLOSED_INTERNAL_SUBDOMAIN'})
 meta=M['qmo'];meta[h]={'qmo_address':h,'canonical_name':o['canonical_name'],'aliases':[h],'type':o['type'],'status':o['status'],'branch':o['branch'],'meaning':{'definition':o['definition'],'semantic_role':'QUERYABLE_MATHEMATICAL_OBJECT','source_status':o['source_status'],'interpretive_note':None},'relations':{},'mathematical_links':{'equation_handle':None,'theorem_handle':None,'candidate_id':None,'frontier_status':None},'closure':{'closure_status':'CERTIFIED_INTERNAL_CONSTRUCTION'+('_AND_TERMINAL_CLOSURE' if closed else ''),'certificate_id':cert['certificate_id'],'certificate_status':'VALID','audit_status':'architectural'},'provenance':o['provenance'],'recovery':{'canonical_structure_recoverable_required':True,'provenance_refs':o['provenance'],'closure_certificate':cert['certificate_id'],'history_policy':'APPEND_ONLY','identity_witness':'CHAIN_HISTORY_AND_STEP_QMO_ADDRESSES','source_live_model_revision':lr},'native_metadata':o['metadata'],'revision':{'api_release':rel,'live_model_revision':lr,'source_live_model_revision':lr,'metadata_revision':1}}
 refresh(meta,E['edges']);M['address_count']=len(meta);M['qmo']=meta;MR={'schema':'ASTRAEUS_QMO_METADATA_REGISTRY_V2','record_count':len(meta),'records':[meta[x] for x in sorted(meta)]}
 for pth,data in [(API/'OBJECT_REGISTRY.json',O),(API/'EDGE_REGISTRY.json',E),(API/'ALIAS_REGISTRY.json',A),(API/'CLOSURE_CERTIFICATE_REGISTRY.json',C),(API/'DEPENDENCY_CHAIN_REGISTRY.json',creg),(API/'DOMAIN_REGISTRY.json',D),(LIB/'QMO_METADATA_LIBRARY.json',M),(API/'QMO_METADATA_REGISTRY.json',MR)]:dump(pth,data)
 dump(CLIB/(h.strip('@')+'.json'),rec)
 with open(LIVE/'DEPENDENCY_CHAIN_HISTORY.jsonl','a',encoding='utf-8') as f:f.write(json.dumps({'event_type':'DEPENDENCY_CHAIN_QMO_CREATED','qmo_address':h,'chain_id':cid,'api_release':rel,'live_model_revision':lr,'seed':seed,'steps':pv['steps'],'terminal':pv['terminal'],'domain_state':rec['domain_state']},ensure_ascii=False)+'\n')
 with open(LIVE/'QMO_METADATA_HISTORY.jsonl','a',encoding='utf-8') as f:f.write(json.dumps({'event_type':'METADATA_RUNTIME_REGISTER','qmo_address':h,'api_release':rel,'live_model_revision':lr,'status':o['status']},ensure_ascii=False)+'\n')
 RT.update({'object_count':len(O['objects']),'edge_count':len(E['edges']),'dependency_chain_count':len(creg['chains']),'qmo_address_count':len(meta)});dump(API/'LIVE_RUNTIME_STATE.json',RT);AL['inventory']['qmo_addresses']=len(meta);AL['inventory']['typed_edges']=len(E['edges']);AL['inventory']['dependency_chains']=len(creg['chains']);AL['runtime_state']=RT;dump(LIVE/'API_LIVE_MODEL.json',AL);dump(LIVE/'QMO_ADDRESS_INDEX.json',{'schema':'ASTRAEUS_QMO_ADDRESS_INDEX_V2','count':len(meta),'addresses':sorted(meta)})
 con=sqlite3.connect(DB);cur=con.cursor();cur.execute('CREATE TABLE IF NOT EXISTS dependency_chains(qmo_address TEXT PRIMARY KEY, chain_id TEXT, status TEXT, seed TEXT, steps_json TEXT, terminal_json TEXT, resolution_context_json TEXT, bandwidth_context_json TEXT, history_json TEXT, domain_state TEXT, raw_json TEXT)');cur.execute('INSERT INTO objects VALUES(?,?,?,?,?,?,?,?)',(h,o['canonical_name'],o['type'],o['status'],o['branch'],o['definition'],json.dumps(o['provenance']),json.dumps(o['metadata'])));cur.execute('INSERT INTO aliases VALUES(?,?)',(h,h))
 nadded=3*len(pv['steps'])+3
 for e in E['edges'][-nadded:]:cur.execute('INSERT INTO edges VALUES(?,?,?,?,?,?,?,?,?)',(e['edge_id'],e['source'],e['relation'],e['target'],e['graph_family'],e['status'],e['confidence'],e['audit_status'],json.dumps(e['provenance'])))
 cur.execute('DELETE FROM qmo_metadata')
 for mh,mr in meta.items():cur.execute('INSERT INTO qmo_metadata VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(mh,mr['canonical_name'],mr['type'],mr['status'],mr['branch'],mr['meaning']['definition'],json.dumps(mr['aliases']),json.dumps(mr['relations']),json.dumps(mr['closure']),json.dumps(mr['provenance']),json.dumps(mr['recovery']),json.dumps(mr['revision']),json.dumps(mr)))
 cur.execute('INSERT INTO dependency_chains VALUES(?,?,?,?,?,?,?,?,?,?,?)',(h,cid,status,seed,json.dumps(rec['steps']),json.dumps(rec['terminal']),json.dumps(rec['resolution_context']),json.dumps(rec['bandwidth_context']),json.dumps(rec['history']),rec['domain_state'],json.dumps(rec)));cur.execute('INSERT INTO search_fts(handle,text) VALUES(?,?)',(h,h+' '+o['canonical_name']+' '+o['definition']));con.commit();con.close();return {'registered':True,'qmo_address':h,'chain_id':cid,'step_count':len(pv['steps']),'terminal':pv['terminal'],'domain_state':rec['domain_state']}
p=argparse.ArgumentParser();sp=p.add_subparsers(dest='cmd',required=True)
a=sp.add_parser('preview');a.add_argument('seed');a.add_argument('--max-steps',type=int,default=5);a.add_argument('--landscape-depth',type=int,default=1);a.add_argument('--direction',choices=['upstream','downstream','bidirectional'],default='bidirectional')
a=sp.add_parser('register');a.add_argument('seed');a.add_argument('--max-steps',type=int,default=5);a.add_argument('--landscape-depth',type=int,default=1);a.add_argument('--direction',choices=['upstream','downstream','bidirectional'],default='bidirectional');a.add_argument('--handle')
a=sp.add_parser('get');a.add_argument('handle');a=sp.add_parser('list');a=sp.add_parser('history');a.add_argument('handle',nargs='?')
args=p.parse_args();cs=chains()
if args.cmd=='preview':out=preview(args.seed,args.max_steps,args.landscape_depth,args.direction)
elif args.cmd=='register':out=register(args.seed,args.max_steps,args.landscape_depth,args.direction,args.handle)
elif args.cmd=='get':out=cs.get(resolve(args.handle))
elif args.cmd=='list':out=[{'qmo_address':x['qmo_address'],'seed':x['seed'],'step_count':len(x['steps']),'terminal':x['terminal'],'domain_state':x['domain_state']} for x in cs.values()]
else:
 rows=[];p0=LIVE/'DEPENDENCY_CHAIN_HISTORY.jsonl'
 if p0.exists():
  for line in p0.read_text(encoding='utf-8').splitlines():
   x=json.loads(line)
   if not args.handle or x.get('qmo_address')==resolve(args.handle):rows.append(x)
 out=rows
print(json.dumps(out,indent=2,ensure_ascii=False))
