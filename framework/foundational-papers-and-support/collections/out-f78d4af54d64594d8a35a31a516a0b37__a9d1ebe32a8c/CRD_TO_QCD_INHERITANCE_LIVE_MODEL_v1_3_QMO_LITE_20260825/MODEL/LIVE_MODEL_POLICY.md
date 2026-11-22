# Live Model / Roadmap Policy

A **major break** is any of:

- theorem or proof closure;
- no-go/failure that changes the search space;
- source correction or supersession;
- new typed mathematical object/map;
- roadmap branch/remap;
- finish-line verdict.

At a major break, create the next cumulative live-model checkpoint. Each checkpoint must include:

1. current roadmap and finish line;
2. all active results plus explicit retired/superseded results;
3. SQLite query surface with mathematical addresses and metadata;
4. recovery prompt;
5. source hashes/provenance;
6. machine-readable state and verification report;
7. checksums and parent-checkpoint reference.

Do not checkpoint every scratch calculation. The checkpoint is the lily pad: enough to resume after a thread limit or model loss without re-deriving closed work.
