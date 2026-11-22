#!/usr/bin/env python3
import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(n): return json.load(open(ROOT/'api'/n,encoding='utf-8'))
front=load('FRONTIER_REGISTRY.json')
proc=subprocess.run([sys.executable,str(ROOT/'runtime'/'rainbow_road_runtime.py'),'close'],capture_output=True,text=True,check=True)
report={'pass':'SELF_BUILD_PASS_002_RAINBOW_ROAD','domain':'@rainbow_road_recursive_domain','frontier':front.get('current_handle'),'runtime_frontier':front.get('runtime_handle'),'closure_preview':json.loads(proc.stdout),'promotion_policy':'VALID INTERNAL CLOSURE CERTIFICATE MAY SELF-PROMOTE; DOMAIN EXTENSIONS REQUIRE AUDIT','next_action':'Run counterexample crawl inside Rainbow Road and use perturbation sandbox for structural stress tests.'}
print(json.dumps(report,indent=2,ensure_ascii=False))
