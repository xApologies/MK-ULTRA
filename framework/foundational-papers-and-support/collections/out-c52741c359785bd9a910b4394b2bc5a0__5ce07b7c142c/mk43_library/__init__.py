from pathlib import Path
from .library import MK43Library

def create_module():
    db = Path(__file__).resolve().parent.parent / "state" / "library.sqlite3"
    return MK43Library(db)

__all__=["MK43Library","create_module"]
