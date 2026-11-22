"""Installation and constructed-fixture checks; no new native-physics certificate."""
from pathlib import Path
import sys,json,copy,sqlite3
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
import sympy as s
from mk43_integration.handoff import *
from mk43_integration.translator import Frame
from tools.integrity import verify,sha256
checks=[]
def check(name,condition,scope='installed adapter on supplied fixture'):
    checks.append({'name':name,'passed':bool(condition),'scope':scope})
    if not condition:raise AssertionError(name)
def reject(name,fn,exception=ValueError):
    try:fn()
    except exception:check(name,True,'negative control')
    else:check(name,False,'negative control')
def main():
    t,x,y,z=s.symbols('t x y z',real=True);coords=(t,x,y,z)
    frame=Frame(coords,s.ImmutableMatrix(s.eye(4)),('fixed real chart (-+++)',))
    bg=s.diag(-1,1,1,1);g=s.diag(-1,1,(1+x*x)**2,1)
    meta={'matter_fields':{'label':'retained original matter packet'},'boundary_data':{'domain':'test'},'gauge_conventions':'fixed test chart','units':{'c':1,'kappa':1}}
    before=copy.deepcopy(meta)
    kw=dict(background=bg,source_upper=s.zeros(4),frame=frame,probe_normals=s.eye(4),cosmological_constant=0,coupling=1,retained_data=meta,source_reference='synthetic fixture',domain_witness='all real coordinates; supplied smooth diagonal metric (-+++)')
    r=attach_evaluated_readout(perturbation=g-bg,**kw);back=r.roundtrip();geometry=r.geometry()
    check('full_metric_roundtrip',zero_matrix(back.metric-g))
    check('independent_source_roundtrip',zero_matrix(back.source_upper))
    check('original_retained_data_roundtrip',back.retained_data==r.readable.retained_data)
    check('caller_data_not_mutated',meta==before)
    check('payload_original_matter_kept',json.loads(back.retained_data[0][1])['matter_fields']==meta['matter_fields'])
    check('source_not_created_from_einstein',geometry['residual_identically_zero'] is False)
    check('curved_metric_scalar',s.simplify(geometry['scalar_curvature']+4/(1+x*x))==0)
    check('signature_check',r.assumptions['signature']=='exact_sign_check_in_symbol_assumptions')
    rr=attach_native_continuity(continuity=g-bg,time_shell=lambda q:q,**kw)
    check('supplied_projection_callback_composed',zero_matrix(rr.readable.metric-g),'explicit identity fixture, not actual Pi_T')
    reject('missing_native_callback_rejected',lambda:attach_native_continuity(continuity=g-bg,time_shell=None,**kw),MissingNativeOperator)
    for key,val in [('retained_data',{}),('domain_witness',''),('source_reference',''),('probe_normals',s.zeros(4))]:
        reject('reject_missing_or_invalid_'+key,lambda key=key,val=val:attach_evaluated_readout(perturbation=g-bg,**{**kw,key:val}))
    for label,m in [('euclidean',s.eye(4)),('degenerate',s.diag(-1,1,1,0)),('asymmetric',s.Matrix([[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))]:
        reject('reject_'+label+'_metric',lambda m=m:attach_evaluated_readout(perturbation=m-bg,**kw))
    reject('asymmetric_source_rejected',lambda:attach_evaluated_readout(perturbation=g-bg,**{**kw,'source_upper':s.Matrix([[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])}))
    check('metric_codec_roundtrip',zero_matrix(decode_metric_code(metric_code(g))-g),'optional component codec only')
    reject('metric_codec_scale_rejected',lambda:metric_code(g,0))
    S=s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],[s.Rational(4,5),s.Rational(3,5)],[0,0]]);v=s.Matrix([2,-3])
    check('mode_image_inverse',zero_matrix(recover_mode_on_image(S,S*v)-v),'finite synthetic isometry')
    reject('mode_outside_image_rejected',lambda:recover_mode_on_image(S,s.Matrix([0,0,1])))
    reject('nonisometric_mode_map_rejected',lambda:recover_mode_on_image(2*S,S*v))
    A=s.diag(s.Rational(1,2),s.Rational(1,3));B=s.eye(2);J=s.Matrix([[1,2]]);dm=s.Matrix([1,2])
    check('feedback_response',fixed_point_response(A,B,J,dm)==s.Matrix([8]),'finite evaluated derivative fixture')
    reject('singular_feedback_rejected',lambda:fixed_point_response(s.eye(2),B,J,dm))
    check('history_energy_telescopes',history_energy([2,5,8],2)==history_energy([2,5],2)+history_energy([5,8],2),'native scalar accounting')
    check('closed_history_zero_net_not_zero_content',history_energy([4,7,4],2)==0,'scalar change')
    reject('nonpositive_native_unit_rejected',lambda:history_energy([1,2],0))
    health=verify(ROOT,manifest=False)
    check('base_source_and_index_integrity',health['ok'],'source preservation')
    check('original_handle_count_preserved',health['native_handles']==2384,'index')
    check('full_active_parent_edges_preserved',health['active_parent_edges']==75429,'index')
    check('complete_active_qmo_edge_count',health['database']['edges']==75457,'index')
    check('unchanged_parent_edges_preserved',health['unchanged_parent_edge_records']==75419,'index')
    check('two_direction_records_corrected',health['corrected_parent_edge_records']==2,'index')
    check('three_stale_derived_edges_retired',health['retired_parent_edge_records']==3,'index')
    check('legacy_api_graph_not_loaded',health['legacy_api_4_3_graph_loaded'] is False,'index')
    check('no_dangling_dependencies',health['dangling_dependencies']==0,'index')
    c=sqlite3.connect(ROOT/'registry/GR_QMO.sqlite')
    check('all_qmo_objects_preserved',c.execute('SELECT COUNT(*) FROM objects').fetchone()[0]==2397,'index')
    check('correct_time_shell_realization',c.execute("SELECT COUNT(*) FROM edges WHERE source='@time_shell_projection' AND relation='REALIZES' AND target='@metric_perturbation'").fetchone()[0]==1,'index')
    check('correct_reverse_lookup',c.execute("SELECT COUNT(*) FROM edges WHERE source='@metric_perturbation' AND relation='REALIZED_BY' AND target='@time_shell_projection'").fetchone()[0]==1,'index')
    check('old_time_shell_direction_absent',c.execute("SELECT COUNT(*) FROM edges WHERE source='@metric_perturbation' AND relation='REALIZES' AND target='@time_shell_projection'").fetchone()[0]==0,'index')
    check('retired_downstream_edges_absent',c.execute("SELECT COUNT(*) FROM edges WHERE (source='@graviton' AND relation='PROJECTS_TO' AND target='@time_shell_projection') OR (source='@linear_metric_perturbation' AND relation='REALIZES' AND target='@time_shell_projection') OR (source='@spin_2_projection' AND relation='PROJECTS_TO' AND target='@time_shell_projection')").fetchone()[0]==0,'index')
    check('all_integration_edges_expose_conditions',c.execute("SELECT COUNT(*) FROM edges WHERE origin='GR_QMO_INTEGRATION' AND json_array_length(json_extract(metadata,'$.conditions')) > 0").fetchone()[0]==28,'index')
    check('mass_v3_import_registered',c.execute("SELECT kind FROM objects WHERE handle='@mass'").fetchone()[0]=='imported_source_object')
    check('native_time_shell_record_preserved',c.execute("SELECT kind FROM objects WHERE handle='@time_shell'").fetchone()[0]=='inherited_handle');c.close()
    audit=json.loads((ROOT/'registry/GRAVITY_AUDIT_INHERITED.json').read_text())['items']
    check('audit_12_not_promoted',audit[11]['recorded_status']=='NOT_YET_TESTED_EXTERNAL_DATA')
    check('audit_provisional_statuses_retained',all(audit[i-1]['recorded_status'].startswith('PROVISIONAL_PASS') for i in (19,30)))
    cp=json.loads((ROOT/'registry/CHECKPOINTS.json').read_text())
    check('fourteen_checkpoints_registered',len(cp)==14)
    check('experimental_foam_not_active',next(x for x in cp if x['id']=='MKUltra_ER_TimeShell_Integration_v0_1')['activation']=='experimental_archive')
    check('translator_preserved_bytewise',sha256(ROOT/'mk43_integration/translator.py')==sha256(ROOT/'checkpoints/expanded/Genesis_GR_Translation_Closure/code/translator.py'))
    report={'all_passed':all(c['passed'] for c in checks),'named_checks':len(checks),'checks':checks,'scope':'installation, algebra, source preservation and constructed fixtures only'}
    out=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'reruns/INSTALLATION_TESTS.json';out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'all_passed':report['all_passed'],'named_checks':len(checks),'output':str(out)}))
if __name__=='__main__':main()
