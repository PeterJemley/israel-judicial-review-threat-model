#!/usr/bin/env python3
"""Carry the first draw and its verification from the frame as built into the corrected frame (change log (al)).

Usage: python3 carry_over_frame.py AS_BUILT_CSV CORRECTED_CSV MERGE_DEFECT_JSON OUT_CSV
A corrected row is matched to the as-built row that carried the same law (the Basic Law first named in
the title, the amendment number, and the passage date). A law that was merged into another law's row is
matched to that row and marked as the merged partner. Adds first_draw_seq, first_draw_sampled and
first_draw_match; carries verified, verification_search and related_cases only where the law matched
is the one the as-built row was titled for, since the verification searched that title.
"""
import sys, csv, io, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_frame import law_identity

def ident(r): return law_identity(r["title_he"]) + (r["passage_date"],)

def main(old_csv, new_csv, defect_json, out_csv):
    old = list(csv.DictReader(io.open(old_csv, encoding="utf-8")))
    new = list(csv.DictReader(io.open(new_csv, encoding="utf-8")))
    md = json.load(io.open(defect_json, encoding="utf-8"))
    by_ident = {ident(r): r for r in old}
    by_seq = {r["seq"]: r for r in old}
    partner = {}
    for g in md["groups"]:
        s = str(g["frame_rows"][0]["seq"])
        for l in g["distinct_laws"]:
            partner[(l["subject"], l["amendment_no"], l["passage_dates"][0])] = s
    cols = list(new[0].keys())
    i = cols.index("sampled") + 1
    extra = ["first_draw_seq", "first_draw_sampled", "first_draw_match", "verified", "verification_search", "related_cases"]
    cols = cols[:i] + extra + [c for c in cols[i:] if c not in extra]
    unmatched = []
    for r in new:
        o = by_ident.get(ident(r))
        if o is not None:
            r["first_draw_match"] = "same law"
            for c in ("verified", "verification_search", "related_cases"): r[c] = o.get(c, "")
        else:
            s = partner.get(ident(r))
            if s is None: unmatched.append(r["seq"]); continue
            o = by_seq[s]
            r["first_draw_match"] = f"merged into as-built row {s}, titled '{o['title_en']}'"
            for c in ("verified", "verification_search", "related_cases"): r[c] = ""
        r["first_draw_seq"] = o["seq"]
        r["first_draw_sampled"] = o["sampled"]
    with io.open(out_csv, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
        for r in new: w.writerow({c: r.get(c, "") for c in cols})
    sampled = [r for r in new if r["sampled"] == "Yes"]
    out = {"rows": len(new), "sampled": len(sampled),
           "sampled_in_both_draws_same_law": [r["seq"] for r in sampled if r["first_draw_sampled"] == "Yes" and r["first_draw_match"] == "same law"],
           "sampled_now_merged_partner_of_first_draw_row": [r["seq"] for r in sampled if r["first_draw_sampled"] == "Yes" and r["first_draw_match"] != "same law"],
           "sampled_new": [r["seq"] for r in sampled if r["first_draw_sampled"] != "Yes"],
           "first_draw_rows_dropped": sorted({int(r["first_draw_seq"]) for r in new if r["first_draw_sampled"] == "Yes"} - {int(r["first_draw_seq"]) for r in sampled if r["first_draw_sampled"] == "Yes" and r["first_draw_match"] == "same law"}),
           "unverified_sampled": [r["seq"] for r in sampled if not r["verified"]],
           "unmatched": unmatched}
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main(*sys.argv[1:5])
