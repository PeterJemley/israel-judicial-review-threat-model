#!/usr/bin/env python3
"""File the redraw adjudicator's rulings by batch (change log (am)).

Usage: python3 split_adjudication.py CODING_DIR ALL_JSON
The adjudicator rules by corrected-frame sequence number. The assembly looks coding up by batch and by the
number under which each batch filed it, so each ruling is written to adjudications-b{batch}.json with
"enactment" set to that number (the kept batch 2 row was filed under its first-draw number).
"""
import sys, os, io, json

def main(d, path):
    rows = {m["seq"]: m for m in json.load(io.open(os.path.join(d, "rows-redraw.json"), encoding="utf-8"))}
    data = json.load(io.open(path, encoding="utf-8"))
    out = {}
    for key in ("adjudications", "interpretive_rulings"):
        for a in data.get(key, []):
            m = rows[str(a["enactment"])]
            b = m["batch"]
            r = dict(a); r["enactment"] = int(m["coded_seq"]); r["frame_seq"] = int(m["seq"])
            out.setdefault(b, {"adjudications": [], "interpretive_rulings": [], "note": f"Filed from {os.path.basename(path)} by analysis/split_adjudication.py; 'enactment' is the number under which batch {b} filed the row, 'frame_seq' the corrected frame's."})[key].append(r)
    for b, v in sorted(out.items()):
        p = os.path.join(d, f"adjudications-b{b}.json")
        assert not os.path.exists(p), p
        io.open(p, "w", encoding="utf-8").write(json.dumps(v, ensure_ascii=False, indent=1) + "\n")
        print(p, len(v["adjudications"]), len(v["interpretive_rulings"]))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
