# Local QMO Mini API

Database:

    genesis_chirality_closure_qmo.sqlite

Examples:

    python mini_api.py get @closure/structural_chirality_fabric
    python mini_api.py get @resolution
    python mini_api.py get @chirality/byte
    python mini_api.py provenance
    python mini_api.py provenance @void
    python mini_api.py closure
    python mini_api.py closure @update/native_multiscale
    python mini_api.py deps @resolution
    python mini_api.py equations @update/native_multiscale
    python mini_api.py frontier
    python mini_api.py retired
    python mini_api.py sources
    python mini_api.py status

SQLite is the authoritative local metadata/provenance/QMO index for this package.

Current-authority views do not erase mistakes or superseded material. Retired and historical material remains queryable through provenance, aliases, and source receipts.
