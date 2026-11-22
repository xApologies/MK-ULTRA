"""Constructed curved fixture: demonstrates installed composition, not native generation."""
from pathlib import Path
import sys,json
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import sympy as s
from mk43_integration.handoff import attach_evaluated_readout,zero_matrix,metric_code,decode_metric_code
from mk43_integration.translator import Frame

def main():
    t,r,y,z=s.symbols('t r y z', real=True); coords=(t,r,y,z)
    bg=s.diag(-1,1,1,1)
    g=s.diag(-1,1,(1+r*r)**2,1)
    frame=Frame(coords,s.ImmutableMatrix(s.eye(4)),('real coordinates, smooth complete local fixture; (-+++)',))
    record={'matter_fields':{},'boundary_data':{'type':'local fixture'},'gauge_conventions':'fixed chart','units':{'c':1,'kappa':1},'native_history_reference':'none: synthetic evaluated output'}
    result=attach_evaluated_readout(background=bg,perturbation=g-bg,source_upper=s.zeros(4),frame=frame,
      probe_normals=s.eye(4),cosmological_constant=0,coupling=1,retained_data=record,
      source_reference='synthetic fixture, NOT evaluated microscopic MK43 solution',domain_witness='r real, smooth, diagonal (-+++) everywhere')
    back=result.roundtrip(); geometry=result.geometry()
    print(json.dumps({'scope':'synthetic curved readout; no native projection implementation claimed',
      'metric_roundtrip':zero_matrix(back.metric-g),'source_roundtrip':zero_matrix(back.source_upper),
      'retained_fields_roundtrip':back.retained_data==result.readable.retained_data,
      'metric_codec_roundtrip':zero_matrix(decode_metric_code(metric_code(g))-g),
      'scalar_curvature':str(geometry['scalar_curvature']),
      'vacuum_equation_satisfied':geometry['residual_identically_zero'],
      'domain_check':result.assumptions},indent=2))
if __name__=='__main__':main()
