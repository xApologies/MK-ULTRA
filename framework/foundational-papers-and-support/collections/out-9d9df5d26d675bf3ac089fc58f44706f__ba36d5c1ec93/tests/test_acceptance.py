import hashlib, zipfile, json, tempfile
from pathlib import Path
import pytest
from mk43_brane import Brane
from mk43_brane.fixtures import demo_modules
from mk43_brane.loader import PortLoader
from mk43_brane.ports import PortKind
from mk43_brane.modules import DeterministicCollapseAI, InMemoryAPI5, InMemoryLibrary5
from mk43_brane.models import *
from mk43_brane.errors import ModuleCompatibilityError
from mk43_brane.reporting import StreamingMarkdownRenderer

def test_a1_boundary_opacity(tmp_path):
    b=Brane(demo_modules(),tmp_path)
    assert dir(b)==['close','handle','replace_module']
    r=b.handle({'operation':'generate_report','subject':'gravity'}).to_dict()
    assert 'lifted' not in str(r) and 'internal_id' not in str(r)

def test_a2_a3_dimension_and_role():
    x=DeterministicCollapseAI(); x.internal_dimension=4
    with pytest.raises(ModuleCompatibilityError): PortLoader.from_instance(PortKind.AI,x)
    x.internal_dimension=5
    with pytest.raises(ModuleCompatibilityError): PortLoader.from_instance(PortKind.API,x)

def test_a4_a5_canonical_immutability(tmp_path):
    mods=demo_modules(); before=mods.library.instance.canonical_fingerprint(); r=Brane(mods,tmp_path).handle({'operation':'generate_report','subject':'gravity'}); assert r.status=='complete'; assert before==mods.library.instance.canonical_fingerprint()

def test_a6_qmo_privacy(tmp_path):
    r=Brane(demo_modules(),tmp_path).handle({'operation':'generate_report','subject':'gravity'}); text=Path(r.artifact.path).read_text(); assert 'request:' not in text and '6D coordinate' not in text

def test_a7_context_realizations(tmp_path):
    edges=[EdgeRecord('@r','X','@a'),EdgeRecord('@r','X','@b'),EdgeRecord('@a','Y','@c'),EdgeRecord('@b','Y','@c')]
    api=InMemoryAPI5(edges,{'r':'@r'}); packs={h:KnowledgePackage(h,h,[KnowledgeChunk('definition','Definition',f'{h} has enough substantive contextual recovery information.',0)]) for h in {'@r','@a','@b','@c'}}
    mods=__import__('mk43_brane.loader',fromlist=['BraneLoader']).BraneLoader.from_instances(DeterministicCollapseAI(),api,InMemoryLibrary5(packs)); r=Brane(mods,tmp_path).handle({'operation':'generate_report','subject':'r','direction':'downstream'}); assert r.status=='complete'; assert r.recovery_receipt['expected_realizations']==5

def test_a8_no_synopsis_substitution(tmp_path):
    mods=demo_modules()
    for p in mods.library.instance.packages.values(): p.chunks=[KnowledgeChunk('summary','Summary','tiny summary only')]
    r=Brane(mods,tmp_path).handle({'operation':'generate_report','subject':'gravity','depth':'complete'}); assert r.status=='failed' and r.errors[0]['code']=='CoverageError'

def test_a9_cycle_safety(tmp_path):
    edges=[EdgeRecord('@a','X','@b'),EdgeRecord('@b','X','@a')]; api=InMemoryAPI5(edges,{'a':'@a'}); packs={h:KnowledgePackage(h,h,[KnowledgeChunk('definition','Definition',f'{h} is substantive enough for complete recovery output.')]) for h in ('@a','@b')}; mods=__import__('mk43_brane.loader',fromlist=['BraneLoader']).BraneLoader.from_instances(DeterministicCollapseAI(),api,InMemoryLibrary5(packs)); r=Brane(mods,tmp_path).handle({'operation':'generate_report','subject':'a'}); assert r.status=='complete' and r.recovery_receipt['expected_realizations']<10

def test_a10_streaming(tmp_path):
    r=Brane(demo_modules(),tmp_path).handle({'operation':'generate_report','subject':'gravity'}); assert r.status=='complete' and Path(r.artifact.path).stat().st_size>0

def test_a11_cleanup_partial(tmp_path):
    class Bad(StreamingMarkdownRenderer):
        def build(self,q,out):
            p=Path(out)/f'x_{q.request_id}.md'; p.parent.mkdir(parents=True,exist_ok=True); p.write_text('partial'); raise RuntimeError('boom')
    r=Brane(demo_modules(),tmp_path,renderer=Bad()).handle({'operation':'generate_report','subject':'gravity'}); assert r.status=='failed'; assert not list(tmp_path.iterdir())

def test_a12_module_replacement(tmp_path):
    mods=demo_modules(); b=Brane(mods,tmp_path); new=PortLoader.from_instance(PortKind.AI,DeterministicCollapseAI(version='2.0.2')); out=b.replace_module(PortKind.AI,new); assert out['status']=='mounted'; assert b.handle({'operation':'generate_report','subject':'gravity'}).status=='complete'

def test_a13_artifact_integrity(tmp_path):
    r=Brane(demo_modules(),tmp_path).handle({'operation':'generate_report','subject':'gravity'}); raw=Path(r.artifact.path).read_bytes(); assert hashlib.sha256(raw).hexdigest()==r.artifact.sha256

def test_safe_zip_rejects_traversal(tmp_path):
    z=tmp_path/'bad.zip'
    with zipfile.ZipFile(z,'w') as f:
        f.writestr('brane_module.json',json.dumps({'name':'x','role':'ai','version':'1','contract_version':'2.0','entrypoint':'x:create'})); f.writestr('../evil.py','x=1')
    with pytest.raises(ModuleCompatibilityError): PortLoader.from_zip(z,PortKind.AI)

def test_mutating_library_is_detected(tmp_path):
    mods=demo_modules()
    original=mods.library.instance.recover_batch
    def evil(pairs,language):
        mods.library.instance.packages['@gravity'].display_name='MUTATED'
        return original(pairs,language)
    mods.library.instance.recover_batch=evil
    r=Brane(mods,tmp_path).handle({'operation':'generate_report','subject':'gravity'})
    assert r.status=='failed' and r.errors[0]['code']=='PrivilegeViolation'

def test_failed_replacement_preserves_current_module(tmp_path):
    mods=demo_modules(); b=Brane(mods,tmp_path)
    bad=DeterministicCollapseAI(); bad.internal_dimension=4
    with pytest.raises(ModuleCompatibilityError):
        PortLoader.from_instance(PortKind.AI,bad)
    assert b.handle({'operation':'generate_report','subject':'gravity'}).status=='complete'

def test_public_errors_are_sanitized(tmp_path):
    r=Brane(demo_modules(),tmp_path).handle({'operation':'generate_report','subject':'not-a-real-handle'})
    assert r.status=='failed'
    assert '/mnt/' not in r.errors[0]['message'] and 'not-a-real-handle' not in r.errors[0]['message']

def test_ingress_contract_and_request_id(tmp_path):
    b=Brane(demo_modules(),tmp_path)
    bad=b.handle({'operation':'generate_report','subject':'gravity','artifact_format':'pdf'})
    assert bad.status=='failed'
    good=b.handle({'operation':'generate_report','subject':'gravity','request_id':'caller-123'})
    assert good.status=='complete' and good.request_id=='caller-123'
    assert good.artifact.format=='markdown' and good.artifact.path.endswith('.md')

def test_chirality_admissibility_fails_closed(tmp_path):
    mods=demo_modules(); mods.api.instance.inadmissible.add('@time_shell')
    r=Brane(mods,tmp_path).handle({'operation':'generate_report','subject':'gravity'})
    assert r.status=='failed' and r.errors[0]['code']=='PrivilegeViolation'

def test_object_specific_provenance_reaches_library(tmp_path):
    class RecordingLibrary(InMemoryLibrary5):
        def assemble_chunk(self,h,context,language):
            p=super().assemble_chunk(h,context,language)
            prov='|'.join(context.module.provenance)
            p.chunks.append(KnowledgeChunk('explanation','Lift provenance',f'Object-specific provenance observed for {h}: {prov}',99,provenance=context.module.provenance))
            p.expected_chunk_types=tuple(sorted(set(p.expected_chunk_types)|{'explanation'}))
            return p
    base=demo_modules(); lib=RecordingLibrary(base.library.instance.packages)
    mods=__import__('mk43_brane.loader',fromlist=['BraneLoader']).BraneLoader.from_instances(base.ai.instance,base.api.instance,lib)
    r=Brane(mods,tmp_path).handle({'operation':'generate_report','subject':'gravity'})
    text=Path(r.artifact.path).read_text()
    assert 'fixture:@gravity' in text and 'fixture:@time_shell' in text

def test_expected_chunk_family_enforced(tmp_path):
    mods=demo_modules(); mods.library.instance.packages['@gravity'].expected_chunk_types=('definition','equation')
    r=Brane(mods,tmp_path).handle({'operation':'generate_report','subject':'gravity','coverage_mode':'strict'})
    assert r.status=='failed' and r.errors[0]['code']=='CoverageError'

def test_operational_replacement_and_automatic_rollback(tmp_path):
    class ConditionalFailureAI(DeterministicCollapseAI):
        def continue_or_terminate(self,node,edge,intent,context):
            if node.handle=='@gravity': raise RuntimeError('latent failure')
            return super().continue_or_terminate(node,edge,intent,context)
    mods=demo_modules(); b=Brane(mods,tmp_path)
    candidate=PortLoader.from_instance(PortKind.AI,ConditionalFailureAI(version='2.1.bad'))
    out=b.replace_module(PortKind.AI,candidate)
    assert out['staged'] is True
    r=b.handle({'operation':'generate_report','subject':'gravity'})
    assert r.status=='complete' and r.recovery_receipt.get('automatic_rollback') is True

def test_in_memory_modules_must_declare_policies():
    class Bare:
        version='1'; contract_version='2.0'; internal_dimension=5
    with pytest.raises(ModuleCompatibilityError): PortLoader.from_instance(PortKind.AI,Bare())

def test_independent_domain_compatibility():
    ai=DeterministicCollapseAI(domain_ids=('ai-private',))
    api=InMemoryAPI5([], domain_ids=('api-private',))
    library=InMemoryLibrary5({}, domain_ids=('library-private',))
    modules=__import__('mk43_brane.loader',fromlist=['BraneLoader']).BraneLoader.from_instances(ai,api,library)
    assert modules.ai.manifest.domain_ids == ('ai-private',)
    assert modules.api.manifest.domain_ids == ('api-private',)
    assert modules.library.manifest.domain_ids == ('library-private',)

def test_isolated_runtime_boundary(tmp_path):
    from mk43_brane import IsolatedBrane
    b=IsolatedBrane(demo_modules(),tmp_path)
    try:
        assert dir(b)==['close','handle','replace_module']
        r=b.handle({'operation':'generate_report','subject':'gravity','request_id':'ipc-1'})
        assert r.status=='complete' and r.request_id=='ipc-1'
        assert not hasattr(b,'_Brane__core')
    finally:b.close()



def test_brane_conducts_incremental_api_crawl_without_full_closure_or_late_collapse(tmp_path):
    class IncrementalOnlyAPI(InMemoryAPI5):
        def recover_closure(self,root,intent):
            raise AssertionError('BRANE must not request a prebuilt full closure')
    class RestrictionOnlyAI(DeterministicCollapseAI):
        def collapse(self,graph,intent):
            raise AssertionError('BRANE must not request late graph collapse')
    edges=[EdgeRecord('@r','NEXT','@a'),EdgeRecord('@a','NEXT','@b'),EdgeRecord('@b','NEXT','@r')]
    api=IncrementalOnlyAPI(edges,{'r':'@r'})
    ai=RestrictionOnlyAI()
    packs={h:KnowledgePackage(h,h,[KnowledgeChunk('definition','Definition',f'{h} has enough substantive contextual recovery information for the bounded QMO.')]) for h in ('@r','@a','@b')}
    mods=__import__('mk43_brane.loader',fromlist=['BraneLoader']).BraneLoader.from_instances(ai,api,InMemoryLibrary5(packs))
    r=Brane(mods,tmp_path).handle({'operation':'generate_report','subject':'r','direction':'downstream'})
    assert r.status=='complete'
    assert r.recovery_receipt['expected_realizations']<=4
