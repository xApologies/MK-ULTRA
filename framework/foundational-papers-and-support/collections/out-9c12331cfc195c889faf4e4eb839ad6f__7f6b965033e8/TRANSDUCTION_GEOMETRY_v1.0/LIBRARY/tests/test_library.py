from pathlib import Path
from transduction_library import TransductionLibrary

def test_library():
    root=Path(__file__).resolve().parents[1]
    lib=TransductionLibrary(root/"state/library.sqlite3")
    assert lib.healthcheck()
    x=lib.export_address("@global_transduction_object")
    assert x["resolved"]
    assert len(x["content_blocks"]) >= 10
    y=lib.export_address("@connection")
    assert y["resolved"] and y["handle"]=="@transduction_connection"
    m=lib.recover_model("@transduction_qmo")
    assert m["resolved"] and len(m["members"]) >= 30
    lib.close()
