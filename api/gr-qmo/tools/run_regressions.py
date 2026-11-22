"""Rerun unchanged checkpoint suites in temporary copies, preserving old results."""
from pathlib import Path
import argparse,json,subprocess,sys,tempfile,shutil,time,os
ROOT=Path(__file__).resolve().parents[1]
SUITES=[
('MK43_Graviton_TimeShell_Handoff_v0_1','code/checks.py','results/CHECK_RESULTS.json','active'),
('Genesis_GR_Translation_Closure','code/checks.py','results/CHECK_RESULTS.json','active'),
('MKUltra_Chirality_Energy_Mass_Bridge','code/checks.py','results/CHECK_RESULTS.json','active'),
('Genesis_GR_Metric_Source_Realization','checks.py','CHECK_RESULTS.json','active'),
('Genesis_GR_Regular_Completion_v0_1','code/checks.py','results/CHECK_RESULTS.json','reference_new_model_not_activated')]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=ROOT/'reruns/regressions');ap.add_argument('--timeout',type=int,default=180);ap.add_argument('--suite',choices=[v[0] for v in SUITES]);args=ap.parse_args()
    out=args.output.resolve();out.mkdir(parents=True,exist_ok=True);summary=[]
    previous=out/'SUMMARY.json'
    if args.suite and previous.exists():summary=json.loads(previous.read_text())['suites']
    for name,script,result,activation in SUITES:
        if args.suite and name!=args.suite:continue
        print('RUN '+name,flush=True);start=time.monotonic()
        with tempfile.TemporaryDirectory(prefix='mk43_regression_') as td:
            temp=Path(td)/name;shutil.copytree(ROOT/'checkpoints/expanded'/name,temp)
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
            try:
                process=subprocess.run([sys.executable,str(temp/script)],cwd=temp,env=env,capture_output=True,text=True,timeout=args.timeout)
                log=process.stdout+'\n'+process.stderr;ok=process.returncode==0
                data=json.loads((temp/result).read_text()) if (temp/result).exists() else {}
                tests=data.get('checks',data.get('tests',[]));total=len(tests)
                ok=ok and total>0 and all(v.get('passed',False) for v in tests)
            except Exception as exc:log=repr(exc);data={};total=0;ok=False
            (out/(name+'.log')).write_text(log);(out/(name+'.json')).write_text(json.dumps(data,indent=2)+'\n')
            row={'suite':name,'activation':activation,'passed':ok,'named_checks':total,'seconds':round(time.monotonic()-start,3)}
            summary=[v for v in summary if v['suite']!=name]+[row];print(json.dumps(row),flush=True)
    report={'all_passed':all(v['passed'] for v in summary),'suites_executed':len(summary),'total_named_checks':sum(v['named_checks'] for v in summary),'suites':summary,'scope':'preserved mathematical/example suites, not the 35-item physics audit; alternative GRC matter remains reference-only'}
    previous.write_text(json.dumps(report,indent=2)+'\n');return 0 if report['all_passed'] else 1
if __name__=='__main__':raise SystemExit(main())
