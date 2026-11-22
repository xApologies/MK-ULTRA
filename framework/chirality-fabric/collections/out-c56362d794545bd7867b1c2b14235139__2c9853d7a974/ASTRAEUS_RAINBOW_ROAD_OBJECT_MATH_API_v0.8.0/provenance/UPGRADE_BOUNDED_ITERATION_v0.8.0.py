#!/usr/bin/env python3
from pathlib import Path
import json, re, sqlite3, hashlib, os
ROOT=Path(__file__).resolve().parents[1]
API=ROOT/'api'; LIB=ROOT/'library'; LIVE=ROOT/'live_model'; REPORTS=ROOT/'reports'; RUNTIME=ROOT/'runtime'
REL='0.8.0'; LIVE_REV='v0.21.0'

def load(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def dump(p,o): Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def next_edge_id(edges):
    nums=[]
    for e in edges:
        m=re.fullmatch(r'E-(\d+)',e.get('edge_id',''))
        if m: nums.append(int(m.group(1)))
    return f'E-{max(nums+[0])+1:05d}'

def refresh_meta(meta,edges):
    inc={}; out={}
    for e in edges:
        out.setdefault(e['source'],[]).append(e); inc.setdefault(e['target'],[]).append(e)
    for h,r in meta.items():
        ii=inc.get(h,[]); oo=out.get(h,[])
        r['relations']={
            'incoming_count':len(ii),'outgoing_count':len(oo),
            'incoming_edge_ids':[e['edge_id'] for e in ii],
            'outgoing_edge_ids':[e['edge_id'] for e in oo],
            'incoming_relations':sorted({e['relation'] for e in ii}),
            'outgoing_relations':sorted({e['relation'] for e in oo}),
            'neighbors_in':sorted({e['source'] for e in ii}),
            'neighbors_out':sorted({e['target'] for e in oo})}

def add_obj(O,M,A,C, handle,name,typ,status,branch,definition,provenance,metadata, cert_rule=None, source_status='DERIVED_ARCHITECTURE'):
    if any(x['handle']==handle for x in O['objects']): return
    o={'handle':handle,'canonical_name':name,'type':typ,'status':status,'branch':branch,'definition':definition,
       'provenance':provenance,'source_status':source_status,'metadata':metadata}
    O['objects'].append(o); A['aliases'].append({'alias':handle,'handle':handle})
    cert_id=None
    if cert_rule:
        cert_id='CERT-'+hashlib.sha256((handle+'|'+cert_rule).encode()).hexdigest()[:12]
        C['certificates'].append({'certificate_id':cert_id,'handle':handle,'status':'VALID','domain':'@black_rainbow_closed_landscape','rule':cert_rule,
            'premises':metadata.get('premises',[]),'obligations':metadata.get('closure_obligations',{'provenance_complete':True,'domain_typed':True,'history_policy_declared':True}),
            'provenance':provenance,'semantic_guard':'Certificate validates internal architectural construction; it does not promote unrelated member claims.'})
    M['qmo'][handle]={
        'qmo_address':handle,'canonical_name':name,'aliases':[handle],'type':typ,'status':status,'branch':branch,
        'meaning':{'definition':definition,'semantic_role':'QUERYABLE_MATHEMATICAL_OBJECT','source_status':source_status,'interpretive_note':metadata.get('interpretive_note')},
        'relations':{},'mathematical_links':{'equation_handle':None,'theorem_handle':None,'candidate_id':None,'frontier_status':None},
        'closure':{'closure_status':'CERTIFIED_INTERNAL' if cert_id else 'ACTIVE_DOMAIN_DECLARATION','certificate_id':cert_id,'certificate_status':'VALID' if cert_id else None,'audit_status':'architectural'},
        'provenance':provenance,
        'recovery':{'canonical_structure_recoverable_required':True,'provenance_refs':provenance,'closure_certificate':cert_id,'history_policy':'APPEND_ONLY','identity_witness':'QMO_ADDRESS_AND_ITERATION_HISTORY' if 'iteration' in typ else 'QMO_ADDRESS_AND_DOMAIN_HISTORY','source_live_model_revision':LIVE_REV},
        'native_metadata':metadata,
        'revision':{'api_release':REL,'live_model_revision':LIVE_REV,'source_live_model_revision':LIVE_REV,'metadata_revision':1}}

def add_edge(E,s,r,t,prov, fam='iteration_architecture', status='DERIVED_ARCHITECTURE'):
    if any(x['source']==s and x['relation']==r and x['target']==t for x in E['edges']): return
    E['edges'].append({'edge_id':next_edge_id(E['edges']),'source':s,'relation':r,'target':t,'graph_family':fam,'status':status,'confidence':'high','audit_status':'architectural','provenance':prov})

O=load(API/'OBJECT_REGISTRY.json'); E=load(API/'EDGE_REGISTRY.json'); A=load(API/'ALIAS_REGISTRY.json'); C=load(API/'CLOSURE_CERTIFICATE_REGISTRY.json'); M=load(LIB/'QMO_METADATA_LIBRARY.json')
prov=['GENESIS_DIRECTION::2026-08-22_bounded_qmo_iteration','ASTRAEUS_DERIVATION::bounded_recursive_iteration','VERA_AUDIT::domain_and_history_guard']

add_obj(O,M,A,C,'@black_rainbow_closed_landscape','Black Rainbow Closed Landscape','closed landscape QMO','ACTIVE_DOMAIN_CONSTRAINT','domain',
    'Closed mathematical landscape bounding the Astraeus Object Mathematics API. Rainbow Road supplies recursive traversal/runtime behavior and the Möbius carrier supplies recursive presentation geometry; all internally promoted mathematics must remain admissible under this landscape closure contract.',prov,
    {'runtime':'@rainbow_road_recursive_domain','carrier':'@mobius_recursive_carrier','closure_operator':'@dynamic_recursive_closure','lower_boundary_object':'@primitive_structural_zero','whole_domain_closure_object':'@closed_domain_unity','history_policy':'RETURN_DOES_NOT_RESET_HISTORY','interpretive_note':'Project mathematical architecture; not an external physical-universe claim.'},None,'GENESIS_DOMAIN_DIRECTION')
add_obj(O,M,A,C,'@bounded_recursive_iteration','Bounded Recursive Iteration Functional','iteration function QMO','DERIVED_CLOSED_INTERNAL','iteration_function',
    'Mathematical functional on queryable states in the Black Rainbow closed landscape. Given X_0, an admitted step functional Phi, Bandwidth/Resolution context, a finite iteration horizon N, and stop predicate Sigma, it constructs X_(i+1)=Cl_BR(Phi_(B,R)(X_i)) while i<N, appending History and terminating early when Sigma holds.',prov,
    {'signature':'I[Phi,B,R,Sigma,N](X0)','recurrence':'X_(i+1) = Cl_BR(Phi_(B,R)(X_i))','iteration_horizon':'FINITE_REQUESTED_BOUND','early_termination':['TARGET_RECOVERED','CLOSED_FIXED_POINT','OPEN_FORK','FORK','CYCLE_DETECTED','NO_NEW_STRUCTURE','HARD_DEFECT','BANDWIDTH_EXHAUSTED','DOMAIN_BOUNDARY','MAX_ITERATIONS'],'history_policy':'APPEND_ONLY','premises':['@black_rainbow_closed_landscape','@dynamic_recursive_closure','@resolution','@bandwidth_algebra'],'closure_obligations':{'finite_bound_declared':True,'step_operator_registered':True,'stop_predicate_declared':True,'history_preserved':True,'domain_guard_active':True,'provenance_complete':True}},'BOUNDED_RECURSIVE_ITERATION_V1')
add_obj(O,M,A,C,'@bounded_dependency_crawl','Bounded Dependency Crawl Functional','iteration function QMO','DERIVED_CLOSED_INTERNAL','iteration_function',
    'Specialization of bounded recursive iteration in which Phi expands registered dependency structure from a QMO/graph/landscape/chain state. The requested horizon bounds search; closure, target recovery, cycle, fork, or lack of new structure may terminate earlier.',prov,
    {'specializes':'@bounded_recursive_iteration','step_function':'REGISTERED_DEPENDENCY_EXPANSION','outputs':['dependency graph','dependency landscape','dependency chain','iteration run QMO'],'premises':['@bounded_recursive_iteration','@dependency_graph','@dependency_landscape','@dependency_chain'],'closure_obligations':{'registered_edges_only':True,'no_invented_edges':True,'member_status_preserved':True,'history_preserved':True,'domain_guard_active':True}},'BOUNDED_DEPENDENCY_CRAWL_V1')

add_edge(E,'@black_rainbow_closed_landscape','USES_RECURSIVE_RUNTIME','@rainbow_road_recursive_domain',prov)
add_edge(E,'@black_rainbow_closed_landscape','USES_CARRIER','@mobius_recursive_carrier',prov)
add_edge(E,'@black_rainbow_closed_landscape','CLOSES_WITH','@dynamic_recursive_closure',prov)
add_edge(E,'@bounded_recursive_iteration','OPERATES_IN','@black_rainbow_closed_landscape',prov)
add_edge(E,'@bounded_recursive_iteration','USES','@dynamic_recursive_closure',prov)
add_edge(E,'@bounded_recursive_iteration','READS','@resolution',prov)
add_edge(E,'@bounded_recursive_iteration','READS','@bandwidth_algebra',prov)
add_edge(E,'@bounded_dependency_crawl','SPECIALIZES','@bounded_recursive_iteration',prov)
add_edge(E,'@bounded_dependency_crawl','BUILDS','@dependency_chain',prov)
add_edge(E,'@bounded_dependency_crawl','BUILDS','@dependency_landscape',prov)

O['object_count']=len(O['objects']); E['edge_count']=len(E['edges']); C['certificate_count']=len(C['certificates']); M['address_count']=len(M['qmo']); M['api_release']=REL; M['live_model_revision']=LIVE_REV
refresh_meta(M['qmo'],E['edges'])
MR={'schema':'ASTRAEUS_QMO_METADATA_REGISTRY_V2','record_count':len(M['qmo']),'records':[M['qmo'][h] for h in sorted(M['qmo'])]}
dump(API/'OBJECT_REGISTRY.json',O); dump(API/'EDGE_REGISTRY.json',E); dump(API/'ALIAS_REGISTRY.json',A); dump(API/'CLOSURE_CERTIFICATE_REGISTRY.json',C); dump(LIB/'QMO_METADATA_LIBRARY.json',M); dump(API/'QMO_METADATA_REGISTRY.json',MR)

# QMO types
qt=load(API/'QMO_TYPE_REGISTRY.json'); qt['api_release']=REL
existing={x['type'] for x in qt['types']}
for x in [
 {'type':'closed_landscape_qmo','role':'Closure envelope that bounds an admitted mathematical runtime/domain.'},
 {'type':'iteration_function_qmo','role':'Mathematical functional defining bounded recursive iteration over QMO states.'},
 {'type':'iteration_run_qmo','role':'History-bearing execution/result object of a bounded mathematical iteration.'}]:
 if x['type'] not in existing: qt['types'].append(x)
dump(API/'QMO_TYPE_REGISTRY.json',qt)

# Function registry
F={'schema':'ASTRAEUS_MATHEMATICAL_FUNCTION_REGISTRY_V1','api_release':REL,'function_count':2,'functions':[
 {'handle':'@bounded_recursive_iteration','name':'Bounded Recursive Iteration Functional','kind':'recursive_qmo_function','signature':'I[Phi,B,R,Sigma,N](X0)','recurrence':'X_(i+1)=Cl_BR(Phi_(B,R)(X_i))','parameters':{'X0':'seed QMO/graph/landscape/chain','Phi':'registered step functional','B':'Bandwidth context','R':'Resolution context','Sigma':'stop predicate family','N':'finite iteration/search horizon'},'semantic_guard':'N is a maximum horizon, not a required traversal count. Early stopping preserves mathematical meaning.'},
 {'handle':'@bounded_dependency_crawl','name':'Bounded Dependency Crawl Functional','kind':'dependency_iteration_specialization','signature':'Crawl_BR[X0;N,target,direction,mode]','recurrence':'expand registered dependencies; reclose/query; append History','parameters':{'mode':['chain','landscape'],'target':'optional recovery target','N':'finite maximum iteration count','direction':['upstream','downstream','bidirectional']},'semantic_guard':'Uses only registered dependency structure and preserves member statuses.'}
]}
dump(API/'FUNCTION_REGISTRY.json',F)
I={'schema':'ASTRAEUS_ITERATION_REGISTRY_V1','api_release':REL,'run_count':0,'runs':[]}
dump(API/'ITERATION_REGISTRY.json',I)
(LIVE/'ITERATION_HISTORY.jsonl').touch(exist_ok=True)

# Domain retyping: Black Rainbow = closure envelope; Rainbow Road/Mobius = runtime/carrier.
D=load(API/'DOMAIN_REGISTRY.json'); D['schema']='ASTRAEUS_BLACK_RAINBOW_DOMAIN_V1'; D['version']=REL
old=D.get('active_domain',{})
D['active_domain']={
 'handle':'@black_rainbow_closed_landscape','name':'Black Rainbow Closed Mathematical Landscape',
 'lower_boundary_object':'@primitive_structural_zero','whole_domain_closure_object':'@closed_domain_unity',
 'recursive_runtime':'@rainbow_road_recursive_domain','carrier':'@mobius_recursive_carrier','mathematics_root':'@object_mathematics',
 'native_branches':old.get('native_branches',[]),'closure_operator':'@dynamic_recursive_closure','history_policy':'RETURN_DOES_NOT_RESET_HISTORY',
 'local_presentations':old.get('local_presentations',['WHITE_SUPERPOSE','BLACK_NEON']),'presentation_handoff':old.get('presentation_handoff',{}),
 'interpretation_guard':'Black Rainbow is the project closed mathematical landscape; Rainbow Road/Mobius supplies recursive runtime/carrier structure. This is not an external physical-universe claim.',
 'dependency_graph_constructor':'@dependency_graph','landscape_constructor':'@dependency_landscape','dependency_chain_constructor':'@dependency_chain','iteration_function':'@bounded_recursive_iteration',
 'dependency_chain_policy':old.get('dependency_chain_policy'),
 'bounded_iteration_policy':'Every iterative query declares a finite horizon N and stop predicates. Results remain in the Black Rainbow landscape or terminate as a domain-boundary condition; no unbounded generative escape is licensed.'}
D.setdefault('semantic_state',{})['closure_condition']='Cl_BR(X) ~= X under current Black Rainbow domain equivalence'
D['semantic_state']['iteration_condition']='Bounded recursion may run to N but terminates early on target recovery, fixed-point closure, fork/cycle/defect, exhausted admissibility, or domain boundary.'
dump(API/'DOMAIN_REGISTRY.json',D)

CC=load(API/'CLOSURE_CONTRACT.json'); CC['version']='0.3.0'; CC['closed_landscape']='@black_rainbow_closed_landscape'; CC['laws']['domain_bounded_iteration']='Every recursive iteration has a finite requested horizon and remains inside the Black Rainbow closure envelope unless explicitly terminated as a domain-extension condition.'; dump(API/'CLOSURE_CONTRACT.json',CC)

# Commands
CR=load(API/'COMMAND_REGISTRY.json'); CR['api_release']=REL
newcmds=[
 {'address':'@iterate','runtime_name':'iterate','syntax':'@iterate SEED --iterations N [--mode chain|landscape] [--target @QMO] [--direction upstream|downstream|bidirectional] [--register] [--handle @name]','purpose':'Execute/preview a bounded recursive mathematical iteration over registered QMO dependency structure. Requested N is a maximum horizon; stop predicates may terminate earlier.','category':'mathematical_function','implementation':'runtime/bounded_iteration.py via runtime/astraeus_math_api.py','produces_qmo':True,'qmo_backing_handle':'@bounded_recursive_iteration','aliases':['iterate']},
 {'address':'@function','runtime_name':'function','syntax':'@function @handle','purpose':'Return one registered mathematical function QMO/contract.','category':'query','implementation':'runtime/astraeus_math_api.py','produces_qmo':False,'qmo_backing_handle':None,'aliases':['function']},
 {'address':'@functions','runtime_name':'functions','syntax':'@functions','purpose':'List registered mathematical function QMOs.','category':'query','implementation':'runtime/astraeus_math_api.py','produces_qmo':False,'qmo_backing_handle':None,'aliases':['functions']},
 {'address':'@iteration','runtime_name':'iteration','syntax':'@iteration @handle','purpose':'Return one registered bounded iteration-run QMO.','category':'query','implementation':'runtime/bounded_iteration.py via runtime/astraeus_math_api.py','produces_qmo':False,'qmo_backing_handle':None,'aliases':['iteration']},
 {'address':'@iterations','runtime_name':'iterations','syntax':'@iterations','purpose':'List registered bounded iteration-run QMOs.','category':'query','implementation':'runtime/bounded_iteration.py via runtime/astraeus_math_api.py','produces_qmo':False,'qmo_backing_handle':None,'aliases':['iterations']},
 {'address':'@iteration_history','runtime_name':'iteration-history','syntax':'@iteration_history [@handle]','purpose':'Read append-only bounded-iteration History.','category':'history','implementation':'runtime/bounded_iteration.py via runtime/astraeus_math_api.py','produces_qmo':False,'qmo_backing_handle':None,'aliases':['iteration-history']}
]
existing={x['address'] for x in CR['commands']}
for c in newcmds:
 if c['address'] not in existing: CR['commands'].append(c)
CR['command_count']=len(CR['commands']); dump(API/'COMMAND_REGISTRY.json',CR)
H=dict(CR); H['schema']='ASTRAEUS_API_HELP_REGISTRY_V2'; dump(API/'HELP_REGISTRY.json',H)

# API schema updates
S=load(API/'API_SCHEMA.json'); S['version']=REL; S.setdefault('registries',{})['functions']='FUNCTION_REGISTRY.json'; S['registries']['iterations']='ITERATION_REGISTRY.json'; S['registries']['iteration_history']='live_model/ITERATION_HISTORY.jsonl'; S['command_namespace']['command_count']=len(CR['commands']); S['command_namespace'].setdefault('intentional_dual_role_addresses',[]); dump(API/'API_SCHEMA.json',S)

# metadata schema
MS=load(API/'QMO_METADATA_SCHEMA.json'); MS['api_release']=REL; MS['live_model_revision']=LIVE_REV
for p in ['bounded_iteration_run_qmo_has_own_metadata_address','bounded_iteration_history_is_append_only','iteration_horizon_is_maximum_not_required_count','black_rainbow_is_closed_landscape_runtime_envelope']:
 if p not in MS['principles']: MS['principles'].append(p)
dump(API/'QMO_METADATA_SCHEMA.json',MS)

# Runtime state/live model
RT=load(API/'LIVE_RUNTIME_STATE.json'); RT.update({'api_release':REL,'live_model_revision':LIVE_REV,'root_handle':'@black_rainbow_closed_landscape','domain':'BLACK_RAINBOW','recursive_runtime':'RAINBOW_ROAD','carrier':'MOBIUS','object_count':len(O['objects']),'edge_count':len(E['edges']),'qmo_address_count':len(M['qmo']),'command_count':len(CR['commands']),'bounded_iteration_model':'ACTIVE_V1','mathematical_function_count':2,'iteration_run_count':0,'function_registry':'api/FUNCTION_REGISTRY.json','iteration_registry':'api/ITERATION_REGISTRY.json'}); dump(API/'LIVE_RUNTIME_STATE.json',RT)
AL=load(LIVE/'API_LIVE_MODEL.json'); AL['api_identity'].update({'release':REL,'root_handle':'@black_rainbow_closed_landscape','mathematical_domain':'BLACK_RAINBOW','recursive_runtime':'RAINBOW_ROAD','carrier':'MOBIUS','live_model_revision':LIVE_REV}); AL['semantic_contract']['closed_landscape_rule']='Black Rainbow is the closure envelope; Rainbow Road/Mobius is the recursive runtime/carrier. Iterative mathematics remains in the closed landscape or terminates at a declared domain boundary.'; AL['semantic_contract']['bounded_iteration_rule']='Mathematical iteration declares seed, admitted step functional, finite horizon N, stop predicates, Resolution/Bandwidth context, and append-only History. N is a ceiling; early termination is canonical.'; AL['inventory'].update({'qmo_addresses':len(M['qmo']),'typed_edges':len(E['edges']),'structural_commands':len(CR['commands']),'mathematical_functions':2,'iteration_runs':0}); AL['runtime_state']=RT; AL['domain_registry']=D; AL['storage_surfaces']['function_registry']='api/FUNCTION_REGISTRY.json'; AL['storage_surfaces']['iteration_registry']='api/ITERATION_REGISTRY.json'; AL['storage_surfaces']['iteration_history']='live_model/ITERATION_HISTORY.jsonl'; dump(LIVE/'API_LIVE_MODEL.json',AL)
dump(LIVE/'QMO_ADDRESS_INDEX.json',{'schema':'ASTRAEUS_QMO_ADDRESS_INDEX_V2','count':len(M['qmo']),'addresses':sorted(M['qmo'])})

# Append history
with open(LIVE/'QMO_METADATA_HISTORY.jsonl','a',encoding='utf-8') as f:
 for h in ['@black_rainbow_closed_landscape','@bounded_recursive_iteration','@bounded_dependency_crawl']:
  f.write(json.dumps({'event_type':'METADATA_ARCHITECTURE_REGISTER','qmo_address':h,'api_release':REL,'live_model_revision':LIVE_REV,'status':M['qmo'][h]['status']},ensure_ascii=False)+'\n')
with open(LIVE/'API_COMMAND_HISTORY.jsonl','a',encoding='utf-8') as f:
 f.write(json.dumps({'event_type':'COMMAND_NAMESPACE_EXPANDED','api_release':REL,'live_model_revision':LIVE_REV,'added_commands':[c['address'] for c in newcmds],'reason':'GENESIS bounded mathematical iteration direction'},ensure_ascii=False)+'\n')

# Human report
report='''# Bounded Recursive Iteration / Black Rainbow Closure Architecture\n\n## Governing retyping\n\n- **Black Rainbow** = closed mathematical landscape / closure envelope.\n- **Rainbow Road** = recursive runtime inside that landscape.\n- **Möbius** = recursive presentation carrier.\n- The API may iterate deeply without licensing mathematical escape from the closed landscape.\n\n## Mathematical functional\n\n`@bounded_recursive_iteration`\n\n`X_(i+1) = Cl_BR(Phi_(B,R)(X_i))`, for `i < N`, with append-only History.\n\n`N` is a finite search/iteration ceiling. It does not force `N` transitions. Early termination is canonical.\n\n### Default stop predicates\n\n- TARGET_RECOVERED\n- CLOSED_FIXED_POINT\n- OPEN_FORK / FORK\n- CYCLE_DETECTED\n- NO_NEW_STRUCTURE\n- HARD_DEFECT\n- BANDWIDTH_EXHAUSTED\n- DOMAIN_BOUNDARY\n- MAX_ITERATIONS\n\n## Dependency specialization\n\n`@bounded_dependency_crawl` applies the functional to registered QMO dependency structure and can build/query Dependency Graphs, Landscapes, and Chains.\n\n## Consistency guard\n\nA closed landscape bounds admissible derivation; it does not by itself prove consistency. Hard guards, typed transformations, provenance, recovery witnesses, and Closure Certificates remain mandatory.\n'''
(REPORTS/'BOUNDED_RECURSIVE_ITERATION_ARCHITECTURE.md').write_text(report,encoding='utf-8')

# Update README lightly
rp=ROOT/'README.md'; txt=rp.read_text(encoding='utf-8'); txt=txt.replace('v0.7.0','v0.8.0')
if '## Bounded mathematical iteration' not in txt:
 txt += '\n\n## Bounded mathematical iteration\n\nBlack Rainbow is the closed landscape; Rainbow Road/Mobius supplies recursive runtime/carrier behavior. Use `@iterate` for a finite-horizon recursive QMO search. Example: `@iterate @seed --iterations 1000000 --mode chain --target @target`. The bound is a ceiling; the runtime terminates early on closure/fork/cycle/target/defect.\n'
rp.write_text(txt,encoding='utf-8')

# Update SQLite incrementally for added architecture
DB=ROOT/'db'/'astraeus_math.sqlite'; con=sqlite3.connect(DB); cur=con.cursor()
for h in ['@black_rainbow_closed_landscape','@bounded_recursive_iteration','@bounded_dependency_crawl']:
 o=next(x for x in O['objects'] if x['handle']==h)
 cur.execute('INSERT OR REPLACE INTO objects VALUES(?,?,?,?,?,?,?,?)',(h,o['canonical_name'],o['type'],o['status'],o['branch'],o['definition'],json.dumps(o['provenance']),json.dumps(o['metadata'])))
 cur.execute('INSERT INTO aliases(alias,handle) SELECT ?,? WHERE NOT EXISTS(SELECT 1 FROM aliases WHERE alias=? AND handle=?)',(h,h,h,h))
 m=M['qmo'][h]
 cur.execute('INSERT OR REPLACE INTO qmo_metadata VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(h,m['canonical_name'],m['type'],m['status'],m['branch'],m['meaning']['definition'],json.dumps(m['aliases']),json.dumps(m['relations']),json.dumps(m['closure']),json.dumps(m['provenance']),json.dumps(m['recovery']),json.dumps(m['revision']),json.dumps(m)))
 cur.execute('INSERT INTO search_fts(handle,text) VALUES(?,?)',(h,h+' '+o['canonical_name']+' '+o['definition']))
for e in E['edges']:
 if e['graph_family']=='iteration_architecture':
  cur.execute('INSERT OR REPLACE INTO edges VALUES(?,?,?,?,?,?,?,?,?)',(e['edge_id'],e['source'],e['relation'],e['target'],e['graph_family'],e['status'],e['confidence'],e['audit_status'],json.dumps(e['provenance'])))
cur.execute('CREATE TABLE IF NOT EXISTS iteration_runs(qmo_address TEXT PRIMARY KEY, run_id TEXT, mode TEXT, seed TEXT, requested_iterations INTEGER, actual_iterations INTEGER, target TEXT, terminal_json TEXT, visited_json TEXT, history_json TEXT, raw_json TEXT)')
con.commit(); con.close()

print(json.dumps({'release':REL,'live_model_revision':LIVE_REV,'objects':len(O['objects']),'edges':len(E['edges']),'metadata_addresses':len(M['qmo']),'commands':len(CR['commands'])},indent=2))
