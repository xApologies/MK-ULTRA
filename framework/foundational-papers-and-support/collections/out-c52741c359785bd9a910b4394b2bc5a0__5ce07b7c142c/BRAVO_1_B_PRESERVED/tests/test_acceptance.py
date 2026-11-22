import json, sqlite3, tempfile, pathlib, pytest
from mk43_library1b import MK43Library
from mk43_library1b.library import ValidationError,ConflictError,LibraryError

def pkg(h='@A',typ='object',body='Alpha',deps=None):
 return {'handle':h,'object_type':typ,'canonical_math':[h+'=1'],'aliases':[],'content_blocks':[{'content_type':'definition','title':h,'body':body,'ordinal':0},{'content_type':'equation','title':'Eq','body':h+'=1','ordinal':1},{'content_type':'analogy','title':'Analogy','body':'Like A','ordinal':2},{'content_type':'model','title':'Model','body':'Model A','ordinal':3}], 'provenance':[{'source':'test'}], 'relations':deps or [], 'package_version':'1'}
def model():
 return {'package_handle':'@Model','package_name':'Model','root_handle':'@A','addresses':[pkg('@A'),pkg('@B')],'relations':[{'source_handle':'@A','relation_type':'depends_on','target_handle':'@B','required':True}],'package_version':'1'}

def test_01_empty_init(): assert MK43Library().healthcheck()
def test_02_empty_pull(): assert MK43Library().recover('@A').unresolved_reason=='address_not_populated'
def test_03_add_one():
 l=MK43Library();l.add_address(pkg());assert l.recover('@A').resolved
def test_04_invalid_atomic():
 l=MK43Library();f=l.canonical_fingerprint()
 with pytest.raises(ValidationError):l.add_address({'handle':'@X'})
 assert l.canonical_fingerprint()==f
def test_05_add_many():
 l=MK43Library();l.add_many([pkg('@A'),pkg('@B')]);assert l.recover('@B').resolved
def test_06_add_many_atomic_conflict():
 l=MK43Library();l.add_address(pkg('@A'));f=l.canonical_fingerprint()
 with pytest.raises(ConflictError):l.add_many([pkg('@B'),pkg('@A')])
 assert l.canonical_fingerprint()==f
def test_07_model_order():
 l=MK43Library();l.add_package(model());assert [p.handle for p in l.recover_model('@Model')['packages']]==['@A','@B']
def test_08_alias():
 l=MK43Library();p=pkg();p['aliases']=['@Alias'];l.add_address(p);assert l.recover('@Alias').handle=='@A'
def test_09_complete_pull():
 l=MK43Library();l.add_address(pkg());assert len(l.recover('@A').chunks)==4
def test_10_batch_order():
 l=MK43Library();l.add_many([pkg('@A'),pkg('@B')]);assert [p.handle for p in l.recover_batch(['@B','@A'])]==['@B','@A']
def test_11_qmo_order():
 l=MK43Library();l.add_many([pkg('@A'),pkg('@B')]);r=l.pull_qmo({'qmo_id':'q','ordered_nodes':[{'handle':'@B'},{'handle':'@A'}]});assert [p.handle for p in r.recovered]==['@B','@A']
def test_12_qmo_unresolved():
 l=MK43Library();r=l.pull_qmo({'ordered_nodes':[{'handle':'@X','depth':2}]});assert r.unresolved[0]['depth']==2
def test_13_coverage():
 l=MK43Library();l.add_address(pkg());r=l.pull_qmo({'ordered_nodes':[{'handle':'@A'},{'handle':'@X'}]});assert r.coverage==.5
def test_14_equations():
 l=MK43Library();l.add_address(pkg());assert len(l.recover_equations('@A'))==1
def test_15_models():
 l=MK43Library();l.add_address(pkg());assert len(l.recover_models('@A'))==1
def test_16_analogies():
 l=MK43Library();l.add_address(pkg());assert len(l.recover_analogies('@A'))==1
def test_17_explanations():
 l=MK43Library();l.add_address(pkg());assert len(l.recover_explanations('@A'))==1
def test_18_deterministic_chunk():
 l=MK43Library();l.add_address(pkg());assert [c.content for c in l.assemble_chunk('@A').chunks]==[c.content for c in l.assemble_chunk('@A').chunks]
def test_19_replace_stable():
 l=MK43Library();l.add_address(pkg(body='v1'));l.replace_address('@A',pkg(body='v2'));assert l.recover('@A').chunks[0].content=='v2'
def test_20_history():
 l=MK43Library();l.add_address(pkg(body='v1'));l.replace_address('@A',pkg(body='v2'));assert l.export_address('@A',1)['content_blocks'][0]['body']=='v1'
def test_21_remove():
 l=MK43Library();l.add_address(pkg());l.remove_address('@A');assert not l.recover('@A').resolved
def test_22_remove_rollback():
 l=MK43Library();l.add_address(pkg());r=l.remove_address('@A');l.rollback_transaction(r.receipt_id);assert l.recover('@A').resolved
def test_23_purge():
 l=MK43Library();l.add_address(pkg());l.purge_address('@A');assert not l._exists_any('@A')
def test_24_purge_alias():
 l=MK43Library();p=pkg();p['aliases']=['@Alias'];l.add_address(p);l.purge_address('@A');assert not l._conn.execute('select 1 from aliases').fetchone()
def test_25_purge_receipt_no_content():
 l=MK43Library();l.add_address(pkg(body='SECRET'));r=l.purge_address('@A');row=l._conn.execute('select * from purge_receipts').fetchone();assert 'SECRET' not in json.dumps(dict(row))
def test_26_duplicate_reject():
 l=MK43Library();l.add_address(pkg());
 with pytest.raises(ConflictError):l.add_address(pkg())
def test_27_missing_required_dependency():
 l=MK43Library();m=model();m['relations'][0]['target_handle']='@Missing'
 with pytest.raises(ValidationError):l.add_package(m)
def test_28_optional_dependency():
 l=MK43Library();m=model();m['relations'][0]={'source_handle':'@A','relation_type':'see','target_handle':'@Missing','required':False};l.add_package(m);assert l.healthcheck()
def test_29_fingerprint_changes():
 l=MK43Library();f=l.canonical_fingerprint();l.add_address(pkg());assert f!=l.canonical_fingerprint()
def test_30_failed_write_fingerprint():
 l=MK43Library();f=l.canonical_fingerprint();
 with pytest.raises(ValidationError):l.add_address({})
 assert f==l.canonical_fingerprint()
def test_31_context_readonly():
 l=MK43Library();c=l.fork_request_context();
 with pytest.raises(PermissionError):c.add_address(pkg())
def test_32_context_sees_canon():
 l=MK43Library();l.add_address(pkg());c=l.fork_request_context();assert c.recover('@A').resolved
def test_33_sql_injection_inert():
 l=MK43Library();assert not l.recover("@A'; DROP TABLE objects;--").resolved;assert l.healthcheck()
def test_34_provenance():
 l=MK43Library();l.add_address(pkg());assert l.recover('@A').chunks[0].provenance
def test_35_language_default():
 l=MK43Library();l.add_address(pkg());assert l.recover('@A').resolved
def test_36_unsupported_language():
 l=MK43Library();l.add_address(pkg());assert l.recover('@A',language='fr').unresolved_reason=='language_not_available'
def test_37_order_hash_deterministic():
 l=MK43Library();l.add_address(pkg());p={'ordered_nodes':[{'handle':'@A'}]};assert l.pull_qmo(p).order_hash==l.pull_qmo(p).order_hash
def test_38_restart(tmp_path):
 db=tmp_path/'x.db';l=MK43Library(db);l.add_address(pkg());l.close();assert MK43Library(db).recover('@A').resolved
def test_39_index_rebuild_equivalence():
 l=MK43Library();l.add_address(pkg());x=l.recover('@A').chunks;l._conn.execute('REINDEX');assert x==l.recover('@A').chunks
def test_40_manifest_contract():
 m=json.load(open(pathlib.Path(__file__).parents[1]/'brane_module.json'));assert m['role']=='library' and m['internal_dimension']==5
def test_41_required_methods():
 l=MK43Library();required=['recover','recover_batch','recover_model','recover_equations','recover_models','recover_analogies','recover_explanations','assemble_chunk','dimension_model','fork_request_context','canonical_fingerprint','healthcheck'];assert all(callable(getattr(l,x,None)) for x in required)
def test_42_dimensions(): assert set(MK43Library().dimension_model())=={'identity','dependency','chirality','recursion','provenance'}
def test_43_remove_package():
 l=MK43Library();l.add_package(model());l.remove_package('@Model');assert not l.recover('@A').resolved
def test_44_purge_package():
 l=MK43Library();l.add_package(model());l.purge_package('@Model');assert not l._exists_any('@A')
def test_45_append_content():
 l=MK43Library();l.add_address(pkg());l.append_content('@A',{'content_type':'example','title':'E','body':'Example'});assert any(c.chunk_type=='example' for c in l.recover('@A').chunks)
def test_46_preview(): assert MK43Library().preview_transaction({'operation':'ADD_ONE','package':pkg()}).valid
def test_47_invalid_preview(): assert not MK43Library().preview_transaction({'operation':'ADD_ONE','package':{}}).valid
def test_48_model_unresolved(): assert MK43Library().recover_model('@None')['status']=='unresolved'
def test_49_exhaustive_default():
 l=MK43Library();l.add_address(pkg());assert {c.chunk_type for c in l.recover('@A').chunks}=={'definition','equation','analogy','model'}
def test_50_qmo_no_internal_exposure():
 l=MK43Library();r=l.pull_qmo({'qmo_id':'q','ordered_nodes':[]});assert not hasattr(r,'connection') and not hasattr(r,'_conn')
