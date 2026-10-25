#!/usr/bin/env python3
"""Apply the docket readers' verification of the sampled rows to the drawn frame, without redrawing.

Usage: python3 apply_verification.py FRAME_CSV VERIFICATION_JSON [VERIFICATION_JSON ...]
Each JSON has "rows": [{"seq", "verdict", "search", "related_cases", "case", "filed", "judgment_date",
"outcome_class", "source", "note"}], as the verification sheet specifies. The draw made at commit
a3bcabf (883948a before the history rewrite of 25 October 2026) is frozen: a sampled row found to have been challenged is marked challenged and its sampled
value becomes "Moved to (a)"; no other row's sampled value changes (change log (ah), no back-filling).
"""
import sys, json, csv, io

def main(frame_csv, jsons):
    rows = list(csv.DictReader(io.open(frame_csv, encoding="utf-8")))
    cols = list(rows[0].keys())
    for c in ("verified", "verification_search", "related_cases"):
        if c not in cols: cols.append(c)
    by_seq = {r["seq"]: r for r in rows}
    seen, moved, errors = [], [], []
    for path in jsons:
        data = json.load(io.open(path, encoding="utf-8"))
        for v in data.get("rows", []):
            seq = str(v.get("seq", "")).strip()
            r = by_seq.get(seq)
            if r is None: errors.append(f"no row with seq {seq!r} in {path}"); continue
            if r.get("sampled") != "Yes" and r.get("sampled") != "Moved to (a)":
                errors.append(f"seq {seq} is not a sampled row"); continue
            seen.append(seq)
            verdict = (v.get("verdict") or "").strip()
            r["verified"] = f"2026-10-22: {verdict}"
            r["verification_search"] = v.get("search", "") or ""
            rc = v.get("related_cases", "")
            r["related_cases"] = rc if isinstance(rc, str) else " | ".join(str(x) for x in rc)
            if verdict.lower().startswith("challenged"):
                r["challenged"] = "Yes"
                r["challenge_case"] = v.get("case", "") or ""
                r["challenge_outcome"] = f"{v.get('outcome_class','')} ({v.get('judgment_date','')})"
                r["sampled"] = "Moved to (a)"
                moved.append((seq, r["title_he"], r["challenge_case"]))
    with io.open(frame_csv, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
        for r in rows: w.writerow({c: r.get(c, "") for c in cols})
    sampled = [r for r in rows if r.get("sampled") in ("Yes", "Moved to (a)")]
    unverified = [r["seq"] for r in sampled if not r.get("verified")]
    print(json.dumps({"sampled_rows": len(sampled), "verified": len(seen), "unverified_seqs": unverified,
                      "moved_to_part_a": moved, "remaining_in_sample": sum(1 for r in rows if r.get("sampled") == "Yes"),
                      "errors": errors}, indent=1, ensure_ascii=False))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
