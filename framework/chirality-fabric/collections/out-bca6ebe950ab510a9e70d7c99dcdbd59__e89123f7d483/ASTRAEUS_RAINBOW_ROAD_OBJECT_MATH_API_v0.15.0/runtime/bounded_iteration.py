#!/usr/bin/env python3
import argparse, json, subprocess, sys, hashlib, re, sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; API=ROOT/'api'; LIVE=ROOT/'live_model'; LIB=ROOT/'library'; DB=ROOT/'db'/'astraeus_math.sqlite'
ILIB=LIB/'iterations'; ILIB.mkdir(parents=True,exist_ok=True)

def load(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def dump(p,o): Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def state():
 s=load(API/'LIVE_RUNTIME_STATE.json'); return s.get('api_release','0.8.0'),s.get('live_model_revision','v0.21.0')
def resolve(h):
 if not h: return h
 if h.startswith('@'): return h
 for x in load(API/'ALIAS_REGISTRY.json')['aliases']:
  if x['alias'].lower()==h.lower(): return x['handle']
 return h
def next_edge_id(es):
 nums=[]
 for e in es:
  m=re.fullmatch(r'E-(\d+)',e.get('edge_id',''))
  if m: nums.append(int(m.group(1)))
 return f'E-{max(nums+[0])+1:05d}'
def run_json(cmd):
 cp=subprocess.run(cmd,capture_output=True,text=True,check=True); return json.loads(cp.stdout)
def target_overlay(pv,target):
 if not target: return pv
 target=resolve(target)
 if target in pv.get('visited_focuses',[]):
  pv['terminal']={'state':'TARGET_RECOVERED','focus':target,'reason':'target appears in resolved iteration lineage'}
  pv['target_recovered']=True; return pv
 term=pv.get('terminal') or {}
 if term.get('focus')==target:
  pv['terminal']={'state':'TARGET_RECOVERED','focus':target,'reason':'target is terminal focus'};pv['target_recovered']=True;return pv
 for x in term.get('exploration_targets',[]):
  if x.get('target')==target:
   pv['terminal']={'state':'TARGET_RECOVERED_AT_FRONTIER','focus':term.get('focus'),'target':target,'via_relation':x.get('relation'),'edge_id':x.get('edge_id')};pv['target_recovered']=True;return pv
 pv['target_recovered']=False; return pv

def preview_chain(seed,N,target=None,direction='bidirectional'):
 cmd=[sys.executable,str(ROOT/'runtime'/'dependency_chain.py'),'preview',resolve(seed),'--max-steps',str(N),'--landscape-depth','1','--direction',direction]
 pv=run_json(cmd); pv=target_overlay(pv,target)
 return {'function':'@bounded_dependency_crawl','mode':'chain','seed':resolve(seed),'requested_iteration_bound':N,'actual_iterations_executed':len(pv.get('steps',[])),'target':resolve(target) if target else None,'terminal':pv['terminal'],'visited':pv.get('visited_focuses',[]),'chain_preview':pv,'history_policy':'APPEND_ONLY','domain':'@black_rainbow_closed_landscape'}

def graph_edges(direction):
 E=load(API/'EDGE_REGISTRY.json')['edges']
 # Mathematical search excludes implementation-only metadata edges by default.
 ex={'landscape_metadata','dependency_graph_metadata','dependency_chain_metadata','iteration_metadata'}
 E=[e for e in E if e.get('graph_family') not in ex]
 out={}; inn={}
 for e in E:
  out.setdefault(e['source'],[]).append(e); inn.setdefault(e['target'],[]).append(e)
 return out,inn

def preview_landscape(seed,N,target=None,direction='bidirectional'):
 seed=resolve(seed); target=resolve(target) if target else None; out,inn=graph_edges(direction)
 frontier={seed}; visited={seed}; step_records=[]; used_edges=[]; terminal=None
 if target==seed: terminal={'state':'TARGET_RECOVERED','focus':seed,'reason':'target equals seed'}
 for i in range(N):
  if terminal: break
  new=set(); sedges=[]
  for n in sorted(frontier):
   candidates=[]
   if direction in ('downstream','bidirectional'): candidates += out.get(n,[])
   if direction in ('upstream','bidirectional'): candidates += inn.get(n,[])
   for e in candidates:
    nxt=e['target'] if e['source']==n else e['source']; sedges.append(e)
    if nxt not in visited: new.add(nxt)
  used_edges.extend(sedges)
  step_records.append({'iteration':i+1,'frontier_in':sorted(frontier),'new_qmos':sorted(new),'edge_ids':sorted({e['edge_id'] for e in sedges})})
  visited.update(new)
  if target and target in visited:
   terminal={'state':'TARGET_RECOVERED','focus':target,'reason':'target entered dependency expansion','iteration':i+1}; break
  if not new:
   terminal={'state':'CLOSED_FIXED_POINT','focus':sorted(frontier)[0] if len(frontier)==1 else None,'reason':'no new registered dependency structure at next expansion','iteration':i+1}; break
  frontier=new
 if terminal is None: terminal={'state':'MAX_ITERATIONS','focus':None,'reason':'requested finite iteration horizon reached','iteration':N}
 return {'function':'@bounded_dependency_crawl','mode':'landscape','seed':seed,'requested_iteration_bound':N,'actual_iterations_executed':len(step_records),'target':target,'terminal':terminal,'visited':sorted(visited),'member_edge_ids':sorted({e['edge_id'] for e in used_edges}),'steps':step_records,'history_policy':'APPEND_ONLY','domain':'@black_rainbow_closed_landscape'}

def preview(seed,N,mode,target,direction):
 if N<0: raise SystemExit('iterations must be >= 0')
 return preview_chain(seed,N,target,direction) if mode=='chain' else preview_landscape(seed,N,target,direction)

def refresh(meta,edges):
 inc={};out={}
 for e in edges: out.setdefault(e['source'],[]).append(e); inc.setdefault(e['target'],[]).append(e)
 for h,r in meta.items():
  ii=inc.get(h,[]);oo=out.get(h,[]);r['relations']={'incoming_count':len(ii),'outgoing_count':len(oo),'incoming_edge_ids':[e['edge_id'] for e in ii],'outgoing_edge_ids':[e['edge_id'] for e in oo],'incoming_relations':sorted({e['relation'] for e in ii}),'outgoing_relations':sorted({e['relation'] for e in oo}),'neighbors_in':sorted({e['source'] for e in ii}),'neighbors_out':sorted({e['target'] for e in oo})}

def find_reusable_chain(seed,pv):
 for c in load(API/'DEPENDENCY_CHAIN_REGISTRY.json').get('chains',[]):
  if c.get('seed')==resolve(seed) and c.get('terminal',{}).get('state')==pv['terminal']['state'] and c.get('terminal',{}).get('focus')==pv['terminal'].get('focus'):
   return c['qmo_address']
 return None

def register(seed,N,mode,target,direction,handle=None):
 rel,lr=state(); seed=resolve(seed); target=resolve(target) if target else None
 h=resolve(handle) if handle else '@it_'+hashlib.sha256(f'{seed}|{mode}|{N}|{target}|{direction}'.encode()).hexdigest()[:12]
 if not h.startswith('@'): h='@'+h
 reg=load(API/'ITERATION_REGISTRY.json')
 ex=next((x for x in reg['runs'] if x['qmo_address']==h),None)
 if ex: return {'registered':False,'reason':'already_registered','iteration':ex}
 pv=preview(seed,N,mode,target,direction); materialized=None
 if mode=='chain':
  materialized=find_reusable_chain(seed,pv.get('chain_preview',{}))
  if materialized is None:
   ch=h+'_chain'; rr=run_json([sys.executable,str(ROOT/'runtime'/'dependency_chain.py'),'register',seed,'--max-steps',str(N),'--landscape-depth','1','--direction',direction,'--handle',ch]); materialized=rr.get('qmo_address',ch)
 else:
  depth=max(0,pv['actual_iterations_executed'])
  lh=h+'_landscape'; rr=run_json([sys.executable,str(ROOT/'runtime'/'dependency_landscape.py'),'register',seed,'--depth',str(depth),'--direction',direction,'--handle',lh]); materialized=rr.get('qmo_address',lh)
 # Reload after possible child materialization.
 O=load(API/'OBJECT_REGISTRY.json'); E=load(API/'EDGE_REGISTRY.json'); A=load(API/'ALIAS_REGISTRY.json'); C=load(API/'CLOSURE_CERTIFICATE_REGISTRY.json'); M=load(LIB/'QMO_METADATA_LIBRARY.json'); RT=load(API/'LIVE_RUNTIME_STATE.json'); AL=load(LIVE/'API_LIVE_MODEL.json')
 rid='IT-'+hashlib.sha256((h+'|'+seed+'|'+str(N)).encode()).hexdigest()[:12]
 terminal=pv['terminal']; closed=terminal['state'] in ('CLOSED_FIXED_POINT','TARGET_RECOVERED','TARGET_RECOVERED_AT_FRONTIER')
 status='DERIVED_ITERATION_RUN'; domain_state='CLOSED_RESULT' if closed else 'OPEN_RESULT'
 prov=['GENESIS_DIRECTION::2026-08-22_bounded_qmo_iteration','QMO:'+seed,'QMO:@bounded_recursive_iteration','QMO:@bounded_dependency_crawl','QMO:'+materialized]
 rec={**pv,'run_id':rid,'qmo_address':h,'canonical_name':f'Bounded Iteration: {seed}','status':status,'materialized_qmo':materialized,'domain_state':domain_state,'construction':{'operator':'@bounded_recursive_iteration','specialization':'@bounded_dependency_crawl','finite_horizon':N,'mode':mode,'direction':direction,'target':target},'history':{'policy':'APPEND_ONLY','created_in_api_release':rel,'created_live_model_revision':lr,'requested_bound':N,'actual_iterations':pv['actual_iterations_executed']},'provenance':prov,'semantic_guard':'Iteration bound N is a ceiling. Early termination is canonical. Registered dependencies only; member claims are not promoted by iteration.'}
 o={'handle':h,'canonical_name':rec['canonical_name'],'type':'iteration run QMO','status':status,'branch':'bounded_iteration','definition':f'Bounded recursive iteration QMO over {seed}; requested horizon {N}, executed {pv["actual_iterations_executed"]} iteration(s), terminal state {terminal["state"]}.','provenance':prov,'source_status':'GENERATED_BY_BOUNDED_RECURSIVE_ITERATION','metadata':{'run_id':rid,'requested_iteration_bound':N,'actual_iterations_executed':pv['actual_iterations_executed'],'terminal':terminal,'mode':mode,'target':target,'materialized_qmo':materialized,'history_policy':'APPEND_ONLY','domain':'@black_rainbow_closed_landscape','live_model_revision':lr}}
 O['objects'].append(o); O['object_count']=len(O['objects']); A['aliases'].append({'alias':h,'handle':h})
 def ae(s,r,t):
  eid=next_edge_id(E['edges']); E['edges'].append({'edge_id':eid,'source':s,'relation':r,'target':t,'graph_family':'iteration_metadata','status':'DERIVED_ARCHITECTURE','confidence':'high','audit_status':'architectural','provenance':prov})
 ae('@bounded_recursive_iteration','CONSTRUCTS_ITERATION',h); ae(h,'HAS_ITERATION_SEED',seed); ae(h,'USES_ITERATION_FUNCTION','@bounded_dependency_crawl'); ae(h,'MATERIALIZES',materialized)
 if terminal.get('focus'): ae(h,'TERMINATES_AT',terminal['focus'])
 E['edge_count']=len(E['edges'])
 cert_id='CERT-IT-'+rid.split('-',1)[1]
 C['certificates'].append({'certificate_id':cert_id,'handle':h,'status':'VALID','domain':'@black_rainbow_closed_landscape','rule':'BOUNDED_ITERATION_RUN_V1','premises':[seed,'@bounded_recursive_iteration'],'obligations':{'finite_horizon_declared':True,'registered_step_function':True,'history_attached':True,'domain_guard_active':True,'materialized_qmo_registered':True,'member_status_preserved':True,'provenance_complete':True},'provenance':prov,'semantic_guard':'Validates iteration-run construction, not truth/promotion of all members encountered.'}); C['certificate_count']=len(C['certificates'])
 meta=M['qmo']; meta[h]={'qmo_address':h,'canonical_name':o['canonical_name'],'aliases':[h],'type':o['type'],'status':o['status'],'branch':o['branch'],'meaning':{'definition':o['definition'],'semantic_role':'QUERYABLE_MATHEMATICAL_OBJECT','source_status':o['source_status'],'interpretive_note':None},'relations':{},'mathematical_links':{'equation_handle':None,'theorem_handle':None,'candidate_id':None,'frontier_status':None},'closure':{'closure_status':'CERTIFIED_ITERATION_CONSTRUCTION','certificate_id':cert_id,'certificate_status':'VALID','audit_status':'architectural'},'provenance':prov,'recovery':{'canonical_structure_recoverable_required':True,'provenance_refs':prov,'closure_certificate':cert_id,'history_policy':'APPEND_ONLY','identity_witness':'ITERATION_RUN_HISTORY_AND_MATERIALIZED_QMO','source_live_model_revision':lr},'native_metadata':o['metadata'],'revision':{'api_release':rel,'live_model_revision':lr,'source_live_model_revision':lr,'metadata_revision':1}}
 refresh(meta,E['edges']); M['address_count']=len(meta); M['qmo']=meta; MR={'schema':'ASTRAEUS_QMO_METADATA_REGISTRY_V2','record_count':len(meta),'records':[meta[x] for x in sorted(meta)]}
 reg['runs'].append(rec); reg['run_count']=len(reg['runs']); reg['api_release']=rel
 for p,d in [(API/'OBJECT_REGISTRY.json',O),(API/'EDGE_REGISTRY.json',E),(API/'ALIAS_REGISTRY.json',A),(API/'CLOSURE_CERTIFICATE_REGISTRY.json',C),(API/'ITERATION_REGISTRY.json',reg),(LIB/'QMO_METADATA_LIBRARY.json',M),(API/'QMO_METADATA_REGISTRY.json',MR)]: dump(p,d)
 dump(ILIB/(h.strip('@')+'.json'),rec)
 with open(LIVE/'ITERATION_HISTORY.jsonl','a',encoding='utf-8') as f: f.write(json.dumps({'event_type':'BOUNDED_ITERATION_RUN_CREATED','qmo_address':h,'run_id':rid,'api_release':rel,'live_model_revision':lr,'seed':seed,'requested_iterations':N,'actual_iterations':pv['actual_iterations_executed'],'terminal':terminal,'materialized_qmo':materialized},ensure_ascii=False)+'\n')
 with open(LIVE/'QMO_METADATA_HISTORY.jsonl','a',encoding='utf-8') as f: f.write(json.dumps({'event_type':'METADATA_RUNTIME_REGISTER','qmo_address':h,'api_release':rel,'live_model_revision':lr,'status':status},ensure_ascii=False)+'\n')
 RT.update({'object_count':len(O['objects']),'edge_count':len(E['edges']),'qmo_address_count':len(meta),'iteration_run_count':len(reg['runs'])}); dump(API/'LIVE_RUNTIME_STATE.json',RT)
 AL['inventory']['qmo_addresses']=len(meta); AL['inventory']['typed_edges']=len(E['edges']); AL['inventory']['iteration_runs']=len(reg['runs']); AL['runtime_state']=RT; dump(LIVE/'API_LIVE_MODEL.json',AL); dump(LIVE/'QMO_ADDRESS_INDEX.json',{'schema':'ASTRAEUS_QMO_ADDRESS_INDEX_V2','count':len(meta),'addresses':sorted(meta)})
 con=sqlite3.connect(DB);cur=con.cursor();cur.execute('CREATE TABLE IF NOT EXISTS iteration_runs(qmo_address TEXT PRIMARY KEY, run_id TEXT, mode TEXT, seed TEXT, requested_iterations INTEGER, actual_iterations INTEGER, target TEXT, terminal_json TEXT, visited_json TEXT, history_json TEXT, raw_json TEXT)')
 cur.execute('INSERT INTO objects VALUES(?,?,?,?,?,?,?,?)',(h,o['canonical_name'],o['type'],o['status'],o['branch'],o['definition'],json.dumps(o['provenance']),json.dumps(o['metadata'])));cur.execute('INSERT INTO aliases VALUES(?,?)',(h,h))
 for e in E['edges'][-(5 if terminal.get('focus') else 4):]: cur.execute('INSERT INTO edges VALUES(?,?,?,?,?,?,?,?,?)',(e['edge_id'],e['source'],e['relation'],e['target'],e['graph_family'],e['status'],e['confidence'],e['audit_status'],json.dumps(e['provenance'])))
 cur.execute('INSERT OR REPLACE INTO qmo_metadata VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(h,meta[h]['canonical_name'],meta[h]['type'],meta[h]['status'],meta[h]['branch'],meta[h]['meaning']['definition'],json.dumps(meta[h]['aliases']),json.dumps(meta[h]['relations']),json.dumps(meta[h]['closure']),json.dumps(meta[h]['provenance']),json.dumps(meta[h]['recovery']),json.dumps(meta[h]['revision']),json.dumps(meta[h])))
 cur.execute('INSERT INTO iteration_runs VALUES(?,?,?,?,?,?,?,?,?,?,?)',(h,rid,mode,seed,N,pv['actual_iterations_executed'],target,json.dumps(terminal),json.dumps(pv.get('visited',[])),json.dumps(rec['history']),json.dumps(rec)));cur.execute('INSERT INTO search_fts(handle,text) VALUES(?,?)',(h,h+' '+o['canonical_name']+' '+o['definition']));con.commit();con.close()
 return {'registered':True,'qmo_address':h,'run_id':rid,'requested_iteration_bound':N,'actual_iterations_executed':pv['actual_iterations_executed'],'terminal':terminal,'materialized_qmo':materialized,'domain_state':domain_state}

p=argparse.ArgumentParser();sp=p.add_subparsers(dest='cmd',required=True)
a=sp.add_parser('preview');a.add_argument('seed');a.add_argument('--iterations',type=int,default=5);a.add_argument('--mode',choices=['chain','landscape'],default='chain');a.add_argument('--target');a.add_argument('--direction',choices=['upstream','downstream','bidirectional'],default='bidirectional')
a=sp.add_parser('register');a.add_argument('seed');a.add_argument('--iterations',type=int,default=5);a.add_argument('--mode',choices=['chain','landscape'],default='chain');a.add_argument('--target');a.add_argument('--direction',choices=['upstream','downstream','bidirectional'],default='bidirectional');a.add_argument('--handle')
a=sp.add_parser('get');a.add_argument('handle');a=sp.add_parser('list');a=sp.add_parser('history');a.add_argument('handle',nargs='?')
args=p.parse_args();reg=load(API/'ITERATION_REGISTRY.json')
if args.cmd=='preview': out=preview(args.seed,args.iterations,args.mode,args.target,args.direction)
elif args.cmd=='register': out=register(args.seed,args.iterations,args.mode,args.target,args.direction,args.handle)
elif args.cmd=='get': out=next((x for x in reg['runs'] if x['qmo_address']==resolve(args.handle)),None)
elif args.cmd=='list': out=[{'qmo_address':x['qmo_address'],'seed':x['seed'],'mode':x['mode'],'requested_iteration_bound':x['requested_iteration_bound'],'actual_iterations_executed':x['actual_iterations_executed'],'terminal':x['terminal']} for x in reg['runs']]
else:
 rows=[]; p0=LIVE/'ITERATION_HISTORY.jsonl'
 if p0.exists():
  for line in p0.read_text(encoding='utf-8').splitlines():
   if not line.strip(): continue
   x=json.loads(line)
   if not args.handle or x.get('qmo_address')==resolve(args.handle): rows.append(x)
 out=rows
print(json.dumps(out,indent=2,ensure_ascii=False))
