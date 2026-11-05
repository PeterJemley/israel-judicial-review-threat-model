#!/usr/bin/env python3
"""Count the Basic-Law changes in a frame through a date (issue 20; change log (bc)).

Usage: python3 frame_counts.py FRAME_CSV [THROUGH, default 2023-01]

The rule: each Basic Law a law amends is counted once, and a law that amends none (a new Basic Law,
or a temporary provision naming no other Basic Law) is counted once. Entries in the `amends` column
are matched to a Basic Law by its Hebrew keyword or English name, so one law listed under both names
counts once. A re-enactment repeals one Basic Law and enacts another on the same subject (the 1992
and 2001 Government laws, the 1994 Freedom of Occupation law): under the stated rule these are two
Basic Laws, the repealed and the new, so the re-enacted subject counts twice. The other reading,
counting the re-enacted subject once, is printed alongside.
"""
import sys, csv, io, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_frame import SUBJECTS, norm_text

ENGLISH = [(name, name) for _, name in SUBJECTS] + [("The Military", "Army"), ("President of the State", "President"),
           ("Nation State of the Jewish People", "Nation State"), ("State Budget", "State Budget (temporary Basic Law)")]

def basic_law_of(entry):
    """The Basic Law an `amends` entry names, by the keyword found earliest in it; None if none is found."""
    t = norm_text(entry)
    hits = [(t.find(norm_text(k)), -len(k), n) for k, n in SUBJECTS + ENGLISH if norm_text(k) in t]
    return min(hits)[2] if hits else None

def changes(row, reenactment_twice=True):
    """The number of Basic-Law changes one law makes."""
    named = {basic_law_of(e) for e in row["amends"].split(" | ") if e.strip()}
    named.discard(None)
    n = max(1, len(named))
    if reenactment_twice and row["kind"] == "re-enactment" and row["subject"] in named:
        n += 1
    return n

def unmatched(rows):
    return [(r["seq"], e) for r in rows for e in r["amends"].split(" | ") if e.strip() and basic_law_of(e) is None]

def counts(frame_csv, through="2023-01"):
    rows = [r for r in csv.DictReader(io.open(frame_csv, encoding="utf-8")) if r["passage_date"][:len(through)] <= through]
    return {"laws": len(rows),
            "changes": sum(changes(r, True) for r in rows),
            "changes_reenactment_once": sum(changes(r, False) for r in rows),
            "reenactments": [r["seq"] for r in rows if r["kind"] == "re-enactment"],
            "unmatched_entries": unmatched(rows)}

if __name__ == "__main__":
    import json
    print(json.dumps(counts(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "2023-01"), indent=1, ensure_ascii=False))
