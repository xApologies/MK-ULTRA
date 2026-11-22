# MK43 Library 1.B

Complete executable realization of the accepted Library 1.0 Alpha.

## Core rule

The QMO supplies mathematical addresses. The Library returns everything encoded beneath those addresses.

## Features

- empty operational SQLite library;
- exhaustive pull by address;
- QMO-shaped ordered recovery;
- add one, add many, and atomic model-package import;
- append and versioned replacement;
- remove with rollback;
- purge for accidental admissions;
- aliases, relations, model membership, provenance, receipts, hashes;
- request-isolated read-only contexts;
- BRANE 2.1 Library⁵ manifest and entry point;
- preserved Library 1.0 Alpha.

## Entry point

`mk43_library1b:create_module`

## CLI

`python -m mk43_library1b.cli --db library.sqlite3 add package.json`
`python -m mk43_library1b.cli --db library.sqlite3 recover @Handle`
`python -m mk43_library1b.cli --db library.sqlite3 purge @Handle`
