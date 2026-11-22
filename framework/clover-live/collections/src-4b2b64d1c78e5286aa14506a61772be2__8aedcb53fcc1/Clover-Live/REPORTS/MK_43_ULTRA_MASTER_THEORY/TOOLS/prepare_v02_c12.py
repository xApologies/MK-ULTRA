from __future__ import annotations
import hashlib, json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
WORKSPACE=ROOT/"REPORTS/MK_43_ULTRA_MASTER_THEORY"
LEDGER=WORKSPACE/"chapter_ledger.jsonl"
API_LEDGER=ROOT/"MODEL/LIVE_MODEL/LIBRARY/LIBRARY_4_1/full_api_handle_ledger_08m.jsonl"
CHAPTER_ID="V02-C12"
HANDLES=sorted({
    "@continuity_perturbation","@correspondence_to_known_quantum_field_theory","@detector_observable",
    "@einstein_field_equation","@field_level_handoff_theorem","@gauge_condition","@general_relativity",
    "@geometry","@gravitational_helicon_mode","@graviton","@gravity","@helicon",
    "@linearized_field_equation","@metric_perturbation","@metric_tensor","@projected_spacetime_metric",
    "@quantum_field_in_curved_spacetime","@readable_space_time","@readable_spacetime",
    "@spin_2_projection","@stress_energy_tensor","@time_shell","@time_shell_projection_operator",
    "@vacuum_wave_equation","@weak_field_metric_perturbation",
})

def sha256(path:Path)->str:
    d=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(8*1024*1024),b""): d.update(b)
    return d.hexdigest()

def read_jsonl(path:Path)->list[dict[str,object]]:
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

def write_jsonl(path:Path,rows:list[dict[str,object]])->None:
    t=path.with_suffix(path.suffix+".tmp")
    t.write_text("".join(json.dumps(r,ensure_ascii=False,sort_keys=True)+"\n" for r in rows),encoding="utf-8")
    os.replace(t,path)

def main()->None:
    rows=read_jsonl(LEDGER); chapter=next(r for r in rows if r["chapter_id"]==CHAPTER_ID)
    if chapter.get("status")!="PLANNED" or chapter.get("path") is not None: raise RuntimeError("chapter boundary changed")
    api={str(r["short_handle"]) for r in read_jsonl(API_LEDGER)}; missing=sorted(set(HANDLES)-api)
    if missing: raise RuntimeError(f"handles absent from Library 4.1: {missing}")
    chapter.update({"handles":HANDLES,"handle_count":len(HANDLES),"assignment_basis":"Library 4.1 conventional-physics translation address set spanning Helicon, Graviton, Time Shell projection, metric perturbation, general relativity, curved-spacetime fields, and observables","assignment_api_ledger_sha256":sha256(API_LEDGER)})
    write_jsonl(LEDGER,rows)
    toc_path=WORKSPACE/"MASTER_TOC.md"; toc=toc_path.read_text(encoding="utf-8")
    old=f"- {CHAPTER_ID} [PLANNED] Translation into Conventional Physics - 0 assigned handles"; new=f"- {CHAPTER_ID} [PLANNED] Translation into Conventional Physics - {len(HANDLES)} assigned handles"
    if old in toc: toc_path.write_text(toc.replace(old,new),encoding="utf-8",newline="\n")
    elif new not in toc: raise RuntimeError("TOC assignment boundary is unexpected")
    receipt={"schema":"mk-ultra-tome-chapter-handle-assignment/v1","created_at":datetime.now(timezone.utc).isoformat(),"chapter_id":CHAPTER_ID,"assigned_handle_count":len(HANDLES),"handles":HANDLES,"basis":"Native Library 4.1 address selection for a provenance-preserving translation from framework handoff objects to conventional field, gravity, metric, gauge, and observable language","library_api_ledger_path":API_LEDGER.relative_to(ROOT).as_posix(),"library_api_ledger_sha256":sha256(API_LEDGER),"missing_handles":[],"chapter_ledger_sha256_after":sha256(LEDGER)}
    (WORKSPACE/"V02_C12_handle_assignment_receipt.json").write_text(json.dumps(receipt,indent=2,ensure_ascii=False,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"chapter_id":CHAPTER_ID,"assigned":len(HANDLES)}))

if __name__=="__main__": main()
