# Local QMO Mini API

Database: `genesis_chirality_qmo.sqlite`

Examples:

    python mini_api.py status
    python mini_api.py get @resolution/operator
    python mini_api.py get @void
    python mini_api.py get @chirality/byte
    python mini_api.py deps @open/native_multiscale_update_law
    python mini_api.py equations @update/native_multiscale
    python mini_api.py provenance @chirality/byte
    python mini_api.py search Rainbow
    python mini_api.py open

SQLite is the authoritative local index for QMO metadata, dependencies, equations, authority, provenance, aliases, source receipts, tests, and open questions.
