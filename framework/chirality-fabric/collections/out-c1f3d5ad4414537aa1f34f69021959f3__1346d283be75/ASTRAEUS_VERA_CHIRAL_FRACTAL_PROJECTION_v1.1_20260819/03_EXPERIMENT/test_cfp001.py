#!/usr/bin/env python3
import json, math
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'06_DATA'
S=json.load(open(D/'CFP001_EXPERIMENT_SUMMARY.json'))
assert S['finite_histories']==4096
assert S['z2_holonomy']['gauge_classes']==8
assert S['z2_holonomy']['holonomy_signatures']==8
assert S['z2_holonomy']['cycle_rank']==3
assert S['projection_identifiability']['shape_stack_rank']==4
assert S['projection_identifiability']['shape_stack_nullity']==4
assert S['projection_identifiability']['full_probe_rank']==8
assert S['projection_identifiability']['full_probe_nullity']==0
assert abs(S['hidden_dimension']['middle_third_cantor_factor_dimension']-math.log(2)/math.log(3))<1e-15
assert abs(S['hidden_dimension']['hidden_chirality_history_dimension']-2*math.log(2)/math.log(3))<1e-15
assert abs(S['E056_bridge']['leverage_ratio']-114.83665649076548)<1e-10
z=pd.read_csv(D/'z2_k4_gauge_class_summary.csv')
assert len(z)==8 and (z['assignments']==8).all() and (z['unique_holonomy_signatures']==1).all()
print('CFP-001 tests: 11/11 PASS')
