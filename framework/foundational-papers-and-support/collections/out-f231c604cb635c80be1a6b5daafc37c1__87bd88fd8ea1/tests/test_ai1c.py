import sys,copy,hashlib,json
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
# Import the separately supplied mk43_brane dependency from the Python environment.
from mk43_ai1c import create_module
from mk43_ai1c.models import Decision
from mk43_ai1c.errors import InterpretationError,RootAuthorityError,ExternalModuleError
from mk43_brane.models import RuntimeRequest,EdgeRecord,CanonicalGraph
from mk43_brane.loader import PortLoader
from mk43_brane.ports import PortKind
@pytest.fixture
def ai(): return create_module()
@pytest.fixture
def req(): return RuntimeRequest.from_dict({'operation':'generate_report','subject':'@Root','request_id':'r1','options':{}})
@pytest.fixture
def graph():
 g=CanonicalGraph('@Root',{'@Root','@A','@B','@C','@D'},[])
 for e in [EdgeRecord('@Root','DEPENDS_ON','@A','p1'),EdgeRecord('@Root','RELATES','@B','p2'),EdgeRecord('@A','LEADS_TO','@C','p3'),EdgeRecord('@C','CYCLES','@Root','p4'),EdgeRecord('@B','LEADS_TO','@D','p5')]: g.add_edge(e)
 return g
class GoodAPI:
 def probe_subject(self,s): return ['@Root']
 def resolve(self,h): return {'handle':h}
class BadAPI:
 def probe_subject(self,s): raise RuntimeError('offline')
class BadRecoverAPI(GoodAPI):
 def recover_closure(self,*a,**k): raise RuntimeError('graph unavailable')
class PartialLibrary:
 def recover(self,h):
  if h=='@B': raise RuntimeError('missing body')
  return {'handle':h}

def test_01_manifest():
 m=json.loads((ROOT/'brane_module.json').read_text()); assert m['role']=='ai' and m['version']=='1.C.1' and m['entrypoint']=='mk43_ai1c:create_module'
def test_02_declarations(ai): assert (ai.contract_version,ai.internal_dimension,ai.canonical_state_policy,ai.rewrite_policy)==('2.0',5,'READ_ONLY','DERIVED_ONLY')
def test_03_methods(ai): assert all(callable(getattr(ai,x)) for x in ('interpret','rank','continue_or_terminate','place_continuation','collapse','validate_collapse','dimension_model','fork_request_context','canonical_fingerprint','healthcheck'))
def test_04_health(ai): assert ai.healthcheck()
def test_05_context(ai): assert ai.fork_request_context() is not ai
def test_06_root_authority(ai,req): assert ai.interpret_structured(req,GoodAPI()).root_authority=='API5'
def test_07_root_from_api(ai,req): assert ai.interpret(req,GoodAPI()).root_hint=='@Root'
def test_08_root_failure(ai,req):
 with pytest.raises(RootAuthorityError): ai.interpret(req,BadAPI())
def test_09_unverified_compat(ai,req): assert ai.interpret(req).root_hint=='@Root'
def test_10_rank_stable(ai,graph):
 c=graph.neighbors('@Root'); assert [x.target for x in ai.rank(c,{})]==[x.target for x in ai.rank(c,{})]
def test_11_four_states(ai,req,graph):
 i=ai.interpret(req); n=type('N',(),{'depth':0})(); assert ai.continue_or_terminate(n,graph.edges[0],i,{}) in {x.value for x in Decision}
def test_12_terminate(ai,graph):
 r=RuntimeRequest.from_dict({'operation':'generate_report','subject':'@Root','options':{'termination_handles':['@A']}}); x=ai.collapse(graph,ai.interpret(r)); assert '@A' in x.continuation_handles
def test_13_defer(ai,graph):
 r=RuntimeRequest.from_dict({'operation':'generate_report','subject':'@Root','options':{'defer_handles':['@B']}}); x=ai.collapse(graph,ai.interpret(r)); assert '@B' in x.frontier
def test_14_invalid_separate(ai,graph):
 r=RuntimeRequest.from_dict({'operation':'generate_report','subject':'@Root','options':{'invalid_handles':['@B']}}); x=ai.collapse(graph,ai.interpret(r)); assert any(z.candidate_handle=='@B' for z in x.rejected_invalid) and '@B' not in x.frontier
def test_15_cycle(ai,req,graph): assert ai.collapse(graph,ai.interpret(req)).cycle_references
def test_16_no_mutation(ai,req,graph):
 b=copy.deepcopy(graph); ai.collapse(graph,ai.interpret(req)); assert graph==b
def test_17_receipt_derived(ai,req,graph):
 ai.collapse(graph,ai.interpret(req)); r=ai.validation_receipt(); assert r.valid and r.metrics['nodes_used']>0 and r.deterministic_order and r.invalid_separated
def test_18_legacy_cap_options_do_not_define_completion(ai,graph):
 r=RuntimeRequest.from_dict({'operation':'generate_report','subject':'@Root','options':{'edge_budget':1,'node_budget':1,'depth_budget':1,'time_budget_ms':1}}); realization=ai.collapse(graph,ai.interpret(r)); assert len(realization.ordered_nodes)>1 and ai.validation_receipt().budget_compliant
def test_19_determinism(ai,req,graph):
 ai.collapse(graph,ai.interpret(req)); a=ai.validation_receipt().output_fingerprint; ai.collapse(graph,ai.interpret(req)); assert ai.validation_receipt().output_fingerprint==a
def test_20_api_failure_receipt(ai,req):
 i=ai.interpret(req,GoodAPI())
 with pytest.raises(ExternalModuleError): ai.recover_graph(BadRecoverAPI(),i)
 assert ai.failure_receipt().code=='API_RECOVERY_FAILED' and not ai.failure_receipt().partial
def test_21_library_partial(ai,req,graph):
 x=ai.collapse(graph,ai.interpret(req)); result=ai.recover_library_partial(PartialLibrary(),ai.plan_library_recovery(x)); assert result['partial'] and result['packages'] and result['failures'][0].code=='LIBRARY_HANDLE_FAILED'
def test_22_validate(ai,req,graph):
 x=ai.collapse(graph,ai.interpret(req)); ai.validate_collapse(x,graph)
def test_23_no_qmo(ai,req,graph): assert not hasattr(ai.collapse(graph,ai.interpret(req)),'qmo')
def test_24_provenance(ai,req,graph): ai.collapse(graph,ai.interpret(req)); assert ai.decision_provenance()
def test_25_alpha_preserved(): assert (ROOT/'ALPHA_1_0_PRESERVED/MK43_AI_v1_0_ALPHA/README.md').is_file()
def test_26_prior_release_preserved(): assert (ROOT/'PREVIOUS_RELEASE_1_B_PRESERVED/README.md').is_file()
def test_27_zip_self_load():
 z=ROOT.parent/'MK43_AI_v1.C_FULL.zip'
 if not z.exists(): pytest.skip('sealed zip not adjacent during source test')
 lm=PortLoader.from_zip(z,PortKind.AI,hashlib.sha256(z.read_bytes()).hexdigest()); assert lm.instance.healthcheck(); lm.close()
