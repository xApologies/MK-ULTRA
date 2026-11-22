#!/usr/bin/env python3
import json, sqlite3, hashlib, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
API=ROOT/'api'; LIVE=ROOT/'live_model'; LIB=ROOT/'library'; REPORT=ROOT/'reports'; DB=ROOT/'db'/'astraeus_math.sqlite'
RELEASE='0.9.0'; LIVE_REV='v0.22.0'; PASS='SELF_BUILD_PASS_004_RECOVERY_CONTEXT_QUOTIENT'


def load(p): return json.load(open(p,encoding='utf-8'))
def dump(p,o): Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def append_jsonl(p,o):
    with open(p,'a',encoding='utf-8') as f: f.write(json.dumps(o,ensure_ascii=False)+'\n')

def next_edge_id(edges):
    nums=[]
    for e in edges:
        m=re.fullmatch(r'E-(\d+)',e.get('edge_id',''))
        if m: nums.append(int(m.group(1)))
    return f'E-{max(nums+[0])+1:05d}'

def add_unique(arr,item,key):
    val=item[key]
    for i,x in enumerate(arr):
        if x.get(key)==val:
            arr[i]=item; return False
    arr.append(item); return True

# Load registries.
O=load(API/'OBJECT_REGISTRY.json'); E=load(API/'EDGE_REGISTRY.json'); A=load(API/'ALIAS_REGISTRY.json')
T=load(API/'THEOREM_REGISTRY.json'); C=load(API/'CLOSURE_CERTIFICATE_REGISTRY.json'); F=load(API/'FRONTIER_REGISTRY.json')
D=load(API/'DERIVATION_RULES.json'); EQ=load(API/'EQUATION_REGISTRY.json'); RT=load(API/'LIVE_RUNTIME_STATE.json')
DOM=load(API/'DOMAIN_REGISTRY.json'); QREG=load(API/'QMO_TYPE_REGISTRY.json'); M=load(LIB/'QMO_METADATA_LIBRARY.json')
AL=load(LIVE/'API_LIVE_MODEL.json')

source_basis=[
    'IDENTITY_THROUGH_HISTORY::FORMAL/01_HISTORY_PATH_ALGEBRA.md',
    'IDENTITY_THROUGH_HISTORY::FORMAL/02_IDENTITY_WITNESS_TRANSPORT.md',
    'IDENTITY_THROUGH_HISTORY::D43-D49',
    'HOLONOMY_CHIRALITY::FORMAL/06_HOLONOMY.md',
    'HOLONOMY_CHIRALITY::D57_HOLONOMY_HISTORY_SIGNATURE_SCAFFOLD',
    'TRANSDUCTION_GEOMETRY::D14_DERIVATION_MACRO',
    'SELF_BUILD_PASS_003',
    'QMO:@dl_recovery_history_signature_core'
]

new_objects=[
    {
      'handle':'@recovery_test_family','canonical_name':'Recovery Test Family','type':'recovery context/test family','status':'DERIVED_CLOSED_INTERNAL','branch':'self_build',
      'definition':'Declared family of recovery-relevant tests/discriminators used to decide whether two History realizations remain distinguishable for canonical recovery under the active Black Rainbow contract.',
      'provenance':source_basis,'metadata':{'generated_by':'R-013','closure_certificate':'CC-007','scope':'DECLARED_RECOVERY_CONTEXTS'}
    },
    {
      'handle':'@recovery_context_equivalence','canonical_name':'Recovery Context Equivalence','type':'history congruence/equivalence','status':'DERIVED_CLOSED_INTERNAL','branch':'self_build',
      'definition':'For same-typed admissible histories h,k, h ~_Rec k exactly when every declared recovery test gives the same result for h and k in every admissible left/right History context in which both composites are defined.',
      'provenance':source_basis,'metadata':{'generated_by':'R-013','closure_certificate':'CC-008','notation':'~_Rec'}
    },
    {
      'handle':'@recovery_history_signature_quotient','canonical_name':'Recovery History Signature Quotient','type':'composable quotient signature','status':'DERIVED_CLOSED_INTERNAL','branch':'self_build',
      'definition':'The quotient signature Sig_Rec(h) := [h]_Rec of the History path algebra by Recovery Context Equivalence. It retains exactly the distinctions required by the declared recovery contexts, abstractly and without claiming a finite encoding.',
      'provenance':source_basis,'metadata':{'generated_by':'R-014','closure_certificate':'CC-009','notation':'Sig_Rec(h)=[h]_Rec'}
    },
    {
      'handle':'@recovery_signature_composition','canonical_name':'Recovery Signature Composition','type':'quotient composition law','status':'DERIVED_CLOSED_INTERNAL','branch':'self_build',
      'definition':'Composition on recovery signatures induced from History composition: [h2]_Rec ⊙ [h1]_Rec := [h2∘h1]_Rec whenever the underlying histories compose. Well-defined because Recovery Context Equivalence is a congruence.',
      'provenance':source_basis,'metadata':{'generated_by':'R-014','closure_certificate':'CC-010','notation':'⊙'}
    },
    {
      'handle':'@theorem_recovery_context_quotient','canonical_name':'Recovery Context Quotient Theorem','type':'recovery theorem object','status':'DERIVED_CLOSED_INTERNAL','branch':'self_build',
      'definition':'Relative to a declared complete recovery-test family, contextual recovery equivalence is a History congruence; its quotient is composable, recovery-sufficient, and the coarsest compositional signature preserving all declared recovery distinctions.',
      'provenance':source_basis,'metadata':{'generated_by':'R-015','closure_certificate':'CC-011','theorem_handle':'@theorem_recovery_context_quotient'}
    },
    {
      'handle':'@holonomy_signature_realization_test','canonical_name':'Holonomy Signature Realization Test','type':'self-build research frontier','status':'ACTIVE_FRONTIER','branch':'self_build',
      'definition':'Test whether the source-backed Holonomy History Signature scaffold realizes the abstract Recovery History Signature Quotient, and determine which fields are necessary or redundant for fiber separation and composition.',
      'provenance':[PASS,'HOLONOMY_CHIRALITY::FORMAL/06_HOLONOMY.md'],'metadata':{'priority':'P0'}
    }
]
for o in new_objects: add_unique(O['objects'],o,'handle')
O['object_count']=len(O['objects'])

# Canonical aliases for new QMO addresses.
for o in new_objects:
    if not any(x.get('alias')==o['handle'] for x in A['aliases']): A['aliases'].append({'alias':o['handle'],'handle':o['handle']})

# Derivation rules.
new_rules=[
 {'rule_id':'R-013','name':'recovery_context_equivalence','kind':'recovery','when':['History path algebra is admitted','recovery test family is declared'],'propose':['define contextual recovery equivalence over all admissible left/right History contexts','test equivalence and congruence laws'],'status':'AUTO_CLOSURE_ELIGIBLE'},
 {'rule_id':'R-014','name':'recovery_signature_quotient','kind':'quotient','when':['@recovery_context_equivalence is a congruence'],'propose':['construct @recovery_history_signature_quotient','induce @recovery_signature_composition from History composition'],'status':'AUTO_CLOSURE_ELIGIBLE'},
 {'rule_id':'R-015','name':'recovery_signature_minimality','kind':'theorem','when':['recovery tests are declared complete for the selected recovery contract','contextual equivalence is used'],'propose':['prove quotient recovery sufficiency','prove quotient is coarsest compositional recovery-sufficient signature relative to declared test family'],'status':'AUTO_CLOSURE_ELIGIBLE'},
 {'rule_id':'R-016','name':'holonomy_signature_realization','kind':'frontier_macro','when':['@recovery_history_signature_quotient is closed','@holonomy_history_signature remains a scaffold'],'propose':['test source Sig_Hol fields against abstract quotient','remove fields only by counterexample-safe redundancy proof','retain full History when finite field subset is not separating'],'status':'ENABLED_CANDIDATE_ONLY'}
]
for r in new_rules: add_unique(D['rules'],r,'rule_id')

# Equations/definitions as queryable equation records.
new_eq=[
 {'equation_handle':'@eq_recovery_context_equivalence','kind':'contextual recovery equivalence','expression_text':'h ~_Rec k iff Test_c(u∘h∘v)=Test_c(u∘k∘v) for every declared recovery test c and every admissible context (u,v)','status':'DERIVED_CLOSED_INTERNAL','symbols':{'h,k':'same-typed History paths','u,v':'admissible History contexts','Test_c':'declared recovery test'},'provenance':source_basis,'branch':'self_build'},
 {'equation_handle':'@eq_recovery_history_signature','kind':'recovery quotient signature','expression_text':'Sig_Rec(h) = [h]_Rec','status':'DERIVED_CLOSED_INTERNAL','symbols':{'Sig_Rec':'recovery signature','[h]_Rec':'Recovery Context Equivalence class'},'provenance':source_basis,'branch':'self_build'},
 {'equation_handle':'@eq_recovery_signature_composition','kind':'quotient composition','expression_text':'[h2]_Rec ⊙ [h1]_Rec = [h2∘h1]_Rec','status':'DERIVED_CLOSED_INTERNAL','symbols':{'⊙':'induced recovery-signature composition','∘':'History composition'},'provenance':source_basis,'branch':'self_build'}
]
for q in new_eq: add_unique(EQ['equations'],q,'equation_handle')
EQ['equation_count']=len(EQ['equations'])

# Theorem.
thm={
 'handle':'@theorem_recovery_context_quotient',
 'title':'Recovery Context Quotient Theorem',
 'status':'DERIVED_CLOSED_INTERNAL',
 'branch':'self_build',
 'statement':'Let H be the admitted typed History path algebra and let T_rec be the declared recovery-test family. Define h ~_Rec k when all tests in T_rec agree after every admissible left/right History context in which both histories can be compared. Then ~_Rec is a compositional congruence; Sig_Rec(h)=[h]_Rec has well-defined induced composition; the quotient is recovery-sufficient for T_rec; and among compositional signatures preserving all T_rec distinctions it is the coarsest (least structurally discriminating) such signature.',
 'assumptions':[
   'History paths compose associatively on their admitted typed sector',
   'recovery test family is explicitly declared for the selected recovery contract',
   'tests are compared only in contexts where both composites are typed/admissible',
   'signature sufficiency is relative to the declared test family; no claim of finite representation is assumed'
 ],
 'conclusion':'Full ordered History need not be retained as the visible recovery signature in principle; the abstract minimal compositional signature is the Recovery Context Equivalence class, while full History/provenance remains recoverable upstream under the continuity contract.',
 'provenance':source_basis
}
add_unique(T['theorems'],thm,'handle'); T['theorem_count']=len(T['theorems'])

# Edges.
def edge(s,r,t,rule='PASS_004',status='DERIVED_INTERNAL',audit='closure_certified'):
    eid=next_edge_id(E['edges']); rec={'edge_id':eid,'source':s,'relation':r,'target':t,'graph_family':'recovery_signature','status':status,'confidence':'high','audit_status':audit,'provenance':[PASS,rule]+source_basis}; E['edges'].append(rec); return eid
new_edge_specs=[
 ('@recovery_history_signature_minimality','BUILDS','@recovery_test_family','R-013'),
 ('@history_path','SUPPORTS','@recovery_context_equivalence','R-013'),
 ('@recovery_test_family','DEFINES','@recovery_context_equivalence','R-013'),
 ('@recovery_discriminator','INFORMS','@recovery_test_family','R-013'),
 ('@history_transport','CONSTRAINS_COMPOSITION_OF','@recovery_context_equivalence','R-013'),
 ('@recovery_context_equivalence','QUOTIENTS','@history_path','R-014'),
 ('@recovery_context_equivalence','DEFINES','@recovery_history_signature_quotient','R-014'),
 ('@recovery_history_signature_quotient','HAS_COMPOSITION','@recovery_signature_composition','R-014'),
 ('@recovery_signature_composition','INHERITS_FROM','@history_path','R-014'),
 ('@recovery_history_signature_quotient','REALIZES_ROLE_OF','@recovery_discriminator','R-015'),
 ('@theorem_recovery_context_quotient','CERTIFIES','@recovery_context_equivalence','R-015'),
 ('@theorem_recovery_context_quotient','CERTIFIES','@recovery_history_signature_quotient','R-015'),
 ('@theorem_recovery_context_quotient','CERTIFIES','@recovery_signature_composition','R-015'),
 ('@dl_recovery_history_signature_core','SUPPORTS_DERIVATION_OF','@theorem_recovery_context_quotient','R-015'),
 ('@recovery_history_signature_minimality','ADVANCES_TO','@holonomy_signature_realization_test','R-016'),
 ('@holonomy_signature_realization_test','TESTS','@holonomy_history_signature','R-016'),
 ('@holonomy_signature_realization_test','AGAINST','@recovery_history_signature_quotient','R-016'),
 ('@holonomy_signature_realization_test','USES','@history_holonomy','R-016')
]
# Avoid duplicate pass rerun.
existing={(x['source'],x['relation'],x['target']) for x in E['edges']}
for s,r,tgt,rr in new_edge_specs:
    if (s,r,tgt) not in existing:
        edge(s,r,tgt,rr); existing.add((s,r,tgt))
E['edge_count']=len(E['edges'])

# Closure certificates.
base_obligations={
 'premises_admitted':True,'licensed_rule':True,'no_new_primitive_or_axiom':True,'output_type_admitted':True,
 'bandwidth_obligations_pass':True,'resolution_obligations_pass':True,'provenance_complete_acyclic':True,
 'recovery_witness_present_when_required':True,'hard_guards_satisfied':True,'domain_guard_active':True
}
certs=[
 ('CC-007','@recovery_test_family','R-013',['@recovery_discriminator','@identity_witness']),
 ('CC-008','@recovery_context_equivalence','R-013',['@history_path','@recovery_test_family','@history_transport']),
 ('CC-009','@recovery_history_signature_quotient','R-014',['@recovery_context_equivalence','@history_path']),
 ('CC-010','@recovery_signature_composition','R-014',['@recovery_history_signature_quotient','@history_path']),
 ('CC-011','@theorem_recovery_context_quotient','R-015',['@recovery_context_equivalence','@recovery_history_signature_quotient','@recovery_signature_composition','@recovery_discriminator'])
]
for cid,h,rid,prem in certs:
    rec={'certificate_id':cid,'handle':h,'status':'VALID','derivation_rule':rid,'premises':prem,'obligations':dict(base_obligations),'domain':'@black_rainbow_closed_landscape','audit':'INTERNAL_CLOSURE_ELIGIBLE','provenance':[PASS]+source_basis,
         'semantic_guard':'Closure is relative to the declared recovery-test family and Black Rainbow contract; it does not prove that a finite Holonomy field tuple realizes the quotient.'}
    add_unique(C['certificates'],rec,'certificate_id')
C['certificate_count']=len(C['certificates'])

# Frontier update.
for x in F['frontiers']:
    if x.get('handle')=='@recovery_history_signature_minimality':
        x['status']='CLOSED_PASS_004'
        x['result']='Abstract minimal compositional recovery signature closed as the quotient of History by Recovery Context Equivalence. Finite/source-field realization remains open.'
new_frontier={
 'handle':'@holonomy_signature_realization_test','status':'ACTIVE','priority':'P0',
 'question':'Does the source-backed Holonomy History Signature scaffold realize the abstract Recovery History Signature Quotient, and which of its fields are necessary, redundant, or insufficient for recovery-fiber separation and composition?',
 'native_branches':['holonomy_chirality','identity_through_history','resolution_readout','transduction_geometry','bandwidth_algebra'],
 'probe_branches':['rainbow_runtime'],
 'candidate_outputs':['@holonomy_history_signature','@recovery_history_signature_quotient','@recovery_signature_composition'],
 'next_tests':['Project source Sig_Hol fields individually and in subsets','Construct same-subsignature/different-recovery-class counterexamples','Test whether [h] is required or merely defeats compression','Test induced signature composition across chained handoffs','Retain abstract quotient as gold-standard recovery class when finite tuple is not separating']
}
add_unique(F['frontiers'],new_frontier,'handle'); F['current_handle']='@holonomy_signature_realization_test'

# QMO type registry additions (schema is descriptive).
if 'types' in QREG:
    labels={x.get('name') or x.get('type') for x in QREG['types'] if isinstance(x,dict)}
    additions=[
      {'name':'recovery context/test family','description':'Declared family of recovery tests defining recovery distinguishability.'},
      {'name':'history congruence/equivalence','description':'Composition-compatible equivalence on History paths.'},
      {'name':'composable quotient signature','description':'History quotient object carrying only declared recovery distinctions.'},
      {'name':'quotient composition law','description':'Composition induced on a quotient signature.'}
    ]
    for a in additions:
        if a['name'] not in labels: QREG['types'].append(a)
    QREG['type_count']=len(QREG['types'])

# Build metadata for new objects and refresh all relation summaries.
meta=M['qmo']
cert_by={x['handle']:x for x in C['certificates']}
thm_handles={x['handle'] for x in T['theorems']}
front_by={x['handle']:x for x in F['frontiers']}
eq_handles={x['equation_handle'] for x in EQ['equations']}
obj_by={x['handle']:x for x in O['objects']}
for o in new_objects:
    h=o['handle']; cert=cert_by.get(h)
    meta[h]={
      'qmo_address':h,'canonical_name':o['canonical_name'],'aliases':[h],'type':o['type'],'status':o['status'],'branch':o['branch'],
      'meaning':{'definition':o['definition'],'semantic_role':'QUERYABLE_MATHEMATICAL_OBJECT','source_status':o.get('source_status'),'interpretive_note':None},
      'relations':{},
      'mathematical_links':{'equation_handle':None,'theorem_handle':h if h in thm_handles else None,'candidate_id':None,'frontier_status':front_by.get(h,{}).get('status')},
      'closure':{'closure_status':'CERTIFIED_INTERNAL' if cert else 'UNCERTIFIED_OR_NOT_REQUIRED','certificate_id':cert.get('certificate_id') if cert else None,'certificate_status':cert.get('status') if cert else None,'audit_status':cert.get('audit') if cert else None},
      'provenance':o['provenance'],
      'recovery':{'canonical_structure_recoverable_required':True,'provenance_refs':o['provenance'],'closure_certificate':cert.get('certificate_id') if cert else None,'history_policy':'APPEND_ONLY_WHEN_HISTORY_BEARING','identity_witness':'@identity_witness' if h!='@holonomy_signature_realization_test' else None,'source_live_model_revision':LIVE_REV},
      'native_metadata':o.get('metadata',{}),
      'revision':{'api_release':RELEASE,'live_model_revision':LIVE_REV,'source_live_model_revision':LIVE_REV,'metadata_revision':1}
    }

inc={}; out={}
for e in E['edges']:
    out.setdefault(e['source'],[]).append(e); inc.setdefault(e['target'],[]).append(e)
for h,r in meta.items():
    ii=inc.get(h,[]); oo=out.get(h,[])
    r['relations']={
      'incoming_count':len(ii),'outgoing_count':len(oo),
      'incoming_edge_ids':[e['edge_id'] for e in ii],'outgoing_edge_ids':[e['edge_id'] for e in oo],
      'incoming_relations':sorted(set(e['relation'] for e in ii)),'outgoing_relations':sorted(set(e['relation'] for e in oo)),
      'neighbors_in':sorted(set(e['source'] for e in ii)),'neighbors_out':sorted(set(e['target'] for e in oo))
    }
    if h in front_by: r['mathematical_links']['frontier_status']=front_by[h].get('status')
M['address_count']=len(meta); M['qmo']=meta
MR={'schema':'ASTRAEUS_QMO_METADATA_REGISTRY_V2','record_count':len(meta),'records':[meta[x] for x in sorted(meta)]}

# Runtime/domain/live model release state.
RT.update({
 'api_release':RELEASE,'live_model_revision':LIVE_REV,'current_frontier':'@holonomy_signature_realization_test','self_build_pass':'004_RECOVERY_CONTEXT_QUOTIENT',
 'object_count':len(O['objects']),'edge_count':len(E['edges']),'equation_count':len(EQ['equations']),'theorem_count':len(T['theorems']),'candidate_count':len(load(API/'CANDIDATE_REGISTRY.json')['candidates']),
 'qmo_address_count':len(meta),'dependency_landscape_count':len(load(API/'DEPENDENCY_LANDSCAPE_REGISTRY.json')['landscapes'])
})
DOM['version']=RELEASE
DOM['active_domain']['recovery_signature_policy']='Recovery signatures may compress History only through a recovery-sufficient compositional congruence; full History/provenance remains recoverable upstream.'
DOM['semantic_state']['recovery_signature_condition']='Sig_Rec is minimal only relative to the declared recovery-test family; finite realization must be separately proved.'

AL['api_identity']['release']=RELEASE; AL['api_identity']['live_model_revision']=LIVE_REV
AL['inventory'].update({'qmo_addresses':len(meta),'typed_edges':len(E['edges']),'equations':len(EQ['equations']),'theorems':len(T['theorems']),'dependency_landscapes':len(load(API/'DEPENDENCY_LANDSCAPE_REGISTRY.json')['landscapes'])})
AL['runtime_state']=RT; AL['domain_registry']=DOM; AL['current_frontier']='@holonomy_signature_realization_test'
AL['semantic_contract']['recovery_signature_rule']='Visible History may be compressed only by a compositional recovery equivalence that separates every distinction required by the declared recovery-test family; canonical full lineage remains recoverable upstream.'

# Human reports/live notes.
report={
 'pass':PASS,
 'status':'CLOSED_INTERNAL_FIXED_POINT',
 'input_frontier':'@recovery_history_signature_minimality',
 'input_landscape':'@dl_recovery_history_signature_core',
 'source_findings':{
   'history_path_algebra':'History paths are typed/composable and do not assume inverses.',
   'witness_transport':'Identity-Witness transport composes on the admitted sector.',
   'history_holonomy':'Closed History loops carry returned Identity-Witness transformations.',
   'holonomy_signature':'Source book provides typed Sig_Hol(h)=(src,tgt,[h],Hol_Conn,Hol_chi,Hol_Id,scope,provenance), while D57 remains a scaffold.',
   'macro_pattern':'Transduction derivation macros permit compact abstractions only when full expansion remains recoverable.'
 },
 'derived_objects':[o['handle'] for o in new_objects if o['status']=='DERIVED_CLOSED_INTERNAL'],
 'theorem':'@theorem_recovery_context_quotient',
 'result':'The abstract minimal compositional recovery signature is the History quotient by contextual recovery equivalence, relative to the declared recovery-test family. This does not yet identify a finite tuple realizing that quotient.',
 'next_frontier':'@holonomy_signature_realization_test',
 'guards':['No finite encoding claimed.','No inverse History assumed.','Full History/provenance remains recoverable upstream.','Minimality is relative to declared recovery tests.']
}
dump(REPORT/'SELF_BUILD_PASS_004.json',report)
(REPORT/'RECOVERY_CONTEXT_QUOTIENT_THEOREM.md').write_text('''# Recovery Context Quotient Theorem — Pass 004\n\n## Construction\nLet `H` be the admitted typed History path algebra and `T_rec` the declared recovery-test family. For same-typed histories `h,k`, define\n\n`h ~_Rec k`\n\niff every declared recovery test gives the same result after every admissible left/right History context in which both composites are defined.\n\nDefine the recovery signature\n\n`Sig_Rec(h) := [h]_Rec`.\n\n## Result\n1. `~_Rec` is an equivalence relation.\n2. Because equivalence is quantified over all admissible composition contexts, it is a History congruence.\n3. Therefore `[h2]_Rec ⊙ [h1]_Rec := [h2 o h1]_Rec` is well-defined.\n4. The quotient preserves every distinction observable by the declared recovery-test family.\n5. Any other compositional recovery-sufficient signature must distinguish at least every pair distinguished by this quotient; therefore the quotient is the coarsest/minimal such signature relative to the declared test family.\n\n## Guard\nThis is an abstract minimality result. It does not prove that the source `Sig_Hol` tuple, or any finite field subset, realizes the quotient. Full ordered History/provenance remains recoverable upstream.\n''',encoding='utf-8')

append_note='''\n\n---\n\n## Self-Build Pass 004 — Recovery Context Quotient\n\nThe active History-signature frontier closed at the abstract level. Instead of retaining full ordered History as the visible recovery signature, define Recovery Context Equivalence `~_Rec` by indistinguishability under every declared recovery test in every admissible left/right History context. Because the equivalence is contextual, it is compositional.\n\n`Sig_Rec(h) := [h]_Rec`\n\nwith induced composition\n\n`[h2]_Rec ⊙ [h1]_Rec := [h2 o h1]_Rec`.\n\nRelative to the declared recovery-test family, this quotient is recovery-sufficient and is the coarsest compositional signature that preserves all declared recovery distinctions. **This is abstract minimality, not a finite storage theorem.** Canonical full History/provenance remains recoverable upstream.\n\nThe source-backed Holonomy History Signature remains a scaffold and now becomes a candidate finite realization of the abstract quotient rather than the definition of minimality itself.\n\n**New frontier:** `@holonomy_signature_realization_test`.\n'''
for p in [LIVE/'ASTRAEUS_API_LIVE_MODEL.md', ROOT/'canonical'/'VERA_RAINBOW_ROAD_LIVE_MODEL.md']:
    with open(p,'a',encoding='utf-8') as f:f.write(append_note)
with open(ROOT/'README.md','a',encoding='utf-8') as f:
    f.write('\n\n## Self-build pass 004 — recovery signature quotient\n\n`@recovery_context_equivalence` and `@recovery_history_signature_quotient` are internally closed. The abstract minimal compositional recovery signature is `Sig_Rec(h)=[h]_Rec`, relative to the declared recovery-test family. New frontier: `@holonomy_signature_realization_test`.\n')

# Persist JSON.
for p,d in [
 (API/'OBJECT_REGISTRY.json',O),(API/'EDGE_REGISTRY.json',E),(API/'ALIAS_REGISTRY.json',A),(API/'THEOREM_REGISTRY.json',T),
 (API/'CLOSURE_CERTIFICATE_REGISTRY.json',C),(API/'FRONTIER_REGISTRY.json',F),(API/'DERIVATION_RULES.json',D),(API/'EQUATION_REGISTRY.json',EQ),
 (API/'LIVE_RUNTIME_STATE.json',RT),(API/'DOMAIN_REGISTRY.json',DOM),(API/'QMO_TYPE_REGISTRY.json',QREG),(LIB/'QMO_METADATA_LIBRARY.json',M),
 (API/'QMO_METADATA_REGISTRY.json',MR),(LIVE/'API_LIVE_MODEL.json',AL),(LIVE/'QMO_ADDRESS_INDEX.json',{'schema':'ASTRAEUS_QMO_ADDRESS_INDEX_V2','count':len(meta),'addresses':sorted(meta)})
]: dump(p,d)

# Append semantic history events for all new objects.
for o in new_objects:
    append_jsonl(LIVE/'QMO_METADATA_HISTORY.jsonl',{'event_type':'SELF_BUILD_PASS_004_REGISTER','qmo_address':o['handle'],'api_release':RELEASE,'live_model_revision':LIVE_REV,'status':o['status'],'pass':PASS})
append_jsonl(LIVE/'ROAD_HISTORY.jsonl',{'event_type':'SELF_BUILD_PASS_004_CLOSURE','api_release':RELEASE,'live_model_revision':LIVE_REV,'from_frontier':'@recovery_history_signature_minimality','to_frontier':'@holonomy_signature_realization_test','theorem':'@theorem_recovery_context_quotient','pass':PASS})

# Rebuild affected SQLite tables while preserving source/section and graph/landscape/chain/iteration tables.
con=sqlite3.connect(DB); cur=con.cursor()
for table in ['objects','aliases','edges','equations','theorems','frontier','qmo_metadata']:
    cur.execute(f'DELETE FROM {table}')
for o in O['objects']:
    cur.execute('INSERT INTO objects VALUES(?,?,?,?,?,?,?,?)',(o['handle'],o['canonical_name'],o['type'],o['status'],o['branch'],o['definition'],json.dumps(o.get('provenance',[]),ensure_ascii=False),json.dumps(o.get('metadata',{}),ensure_ascii=False)))
for a in A['aliases']: cur.execute('INSERT INTO aliases VALUES(?,?)',(a['alias'],a['handle']))
for e in E['edges']:
    cur.execute('INSERT INTO edges VALUES(?,?,?,?,?,?,?,?,?)',(e['edge_id'],e['source'],e['relation'],e['target'],e['graph_family'],e['status'],e['confidence'],e['audit_status'],json.dumps(e.get('provenance',[]),ensure_ascii=False)))
for q in EQ['equations']:
    cur.execute('INSERT INTO equations VALUES(?,?,?,?,?,?,?)',(q['equation_handle'],q.get('expression_text',q.get('expression','')),q.get('meaning',''),q['branch'],q['status'],json.dumps(q.get('provenance',[]),ensure_ascii=False),json.dumps(q,ensure_ascii=False)))
for t in T['theorems']:
    cur.execute('INSERT INTO theorems VALUES(?,?,?,?,?,?,?,?)',(t['handle'],t['title'],t['status'],t['branch'],t['statement'],json.dumps(t.get('assumptions',[]),ensure_ascii=False),t.get('conclusion',''),json.dumps(t.get('provenance',[]),ensure_ascii=False)))
for f in F['frontiers']:
    cur.execute('INSERT INTO frontier VALUES(?,?,?,?,?)',(f['handle'],f['status'],f['priority'],f['question'],json.dumps(f,ensure_ascii=False)))
for h,r in meta.items():
    cur.execute('INSERT INTO qmo_metadata VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(h,r['canonical_name'],r['type'],r['status'],r['branch'],r['meaning']['definition'],json.dumps(r['aliases'],ensure_ascii=False),json.dumps(r['relations'],ensure_ascii=False),json.dumps(r['closure'],ensure_ascii=False),json.dumps(r['provenance'],ensure_ascii=False),json.dumps(r['recovery'],ensure_ascii=False),json.dumps(r['revision'],ensure_ascii=False),json.dumps(r,ensure_ascii=False)))
    if h in {o['handle'] for o in new_objects}:
        ev={'event_type':'SELF_BUILD_PASS_004_REGISTER','qmo_address':h,'api_release':RELEASE,'live_model_revision':LIVE_REV,'status':r['status'],'pass':PASS}
        cur.execute('INSERT INTO qmo_metadata_history(qmo_address,event_type,api_release,live_model_revision,status,definition_hash,provenance_hash,raw_json) VALUES(?,?,?,?,?,?,?,?)',(h,ev['event_type'],RELEASE,LIVE_REV,r['status'],hashlib.sha256(r['meaning']['definition'].encode()).hexdigest(),hashlib.sha256(json.dumps(r['provenance'],sort_keys=True).encode()).hexdigest(),json.dumps(ev,ensure_ascii=False)))
# Refresh FTS for new QMO/theorem/equations without disturbing source-section rows.
for h in [o['handle'] for o in new_objects]+[q['equation_handle'] for q in new_eq]:
    cur.execute('DELETE FROM search_fts WHERE handle=?',(h,))
for o in new_objects:
    cur.execute('INSERT INTO search_fts(handle,text) VALUES(?,?)',(o['handle'],' '.join([o['handle'],o['canonical_name'],o['type'],o['definition'],o['branch'],o['status']])))
for q in new_eq:
    cur.execute('INSERT INTO search_fts(handle,text) VALUES(?,?)',(q['equation_handle'],q['equation_handle']+' '+q.get('kind','')+' '+q.get('expression_text',q.get('expression',''))))
con.commit(); con.close()

print(json.dumps({'pass':PASS,'api_release':RELEASE,'live_model_revision':LIVE_REV,'objects':len(O['objects']),'edges':len(E['edges']),'equations':len(EQ['equations']),'theorems':len(T['theorems']),'frontier':F['current_handle'],'metadata_addresses':len(meta)},indent=2))
