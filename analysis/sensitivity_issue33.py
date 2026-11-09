#!/usr/bin/env python3
"""Issue 33: report T1 and the comparison sample with the recoded rows, beside the original codes.

Usage: python3 sensitivity_issue33.py [FINAL_JSON]
FINAL_JSON defaults to research/recode-2026-11-09-issue33/final.json: the adjudicated recode,
keyed "16", "64", "103", "127" (comparison-sample seq) and "row7" (codebook row 7), each with
`deviation_tier` and `direction` values. Nothing is written; the primary codes are not changed.
The recode is exploratory (issue 33): its rule was written after the original codes were seen.
"""
import sys, os, io, csv, json
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t1_revised as t1

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def path(p): return os.path.join(ROOT, p)
def load_csv(p): return list(csv.DictReader(io.open(path(p), encoding="utf-8")))
def norm(r): return {k: (r.get(k) or "").split(" (")[0].strip() for k in t1.required()}

def value(cell):
    return cell.get("value", "") if isinstance(cell, dict) else (cell or "")

def classify_rows(rows):
    out = []
    for r in rows:
        cls, d, e, grp = t1.classify(norm(r))
        out.append({**r, "class": cls, "decision_rule_prediction": d or "", "elite_prediction": e or "", "group": grp or ""})
    return out

def configuration(rows):
    primary = [r for r in rows if r.get("primary_analysis") == "Yes" and r["class"] != "uncoded"]
    det = t1.detect(len(primary), sum(1 for r in primary if r["outcome"] == "Adverse"),
                    sum(1 for r in primary if r["class"] == "discordant" and r["decision_rule_prediction"] == "Adverse"),
                    sum(1 for r in primary if r["class"] == "discordant" and r["decision_rule_prediction"] == "Not adverse"))
    return {k: det[k] for k in ("N", "K", "D_A", "D_N", "discordant", "minimum_six_met", "verdict_before_outcomes")}

def sample_summary(rows):
    tiers = Counter(r["deviation_tier"] for r in rows)
    return {"none_or_entrenches": tiers["None"] + tiers["Entrenches"], "limited": tiers["Limited"], "sharp": tiers["Sharp"],
            "tiers": dict(sorted(tiers.items())), "direction": dict(sorted(Counter(r["direction"] for r in rows).items())),
            "classes": dict(sorted(Counter(r["class"] for r in rows).items()))}

def compute(final_path=None):
    """The comparison as a dict: changed rows, T1's configuration both ways, the sample's summary both ways."""
    final = json.load(io.open(final_path or path("research/recode-2026-11-09-issue33/final.json"), encoding="utf-8"))
    recode = {k: {c: value(v.get(c)) for c in ("deviation_tier", "direction")} for k, v in final.items()}
    code = load_csv("codebook/m4-codebook.csv")
    sample = load_csv("codebook/comparison-sample.csv")
    code_re = [dict(r, **recode["row" + r["id"]]) if ("row" + r["id"]) in recode else dict(r) for r in code]
    sample_re = [dict(r, **recode[r["seq"]]) if r["seq"] in recode else dict(r) for r in sample]
    a, b = classify_rows(code), classify_rows(code_re)
    sa, sb = classify_rows(sample), classify_rows(sample_re)
    changed = [{"row": ("codebook " + r["id"]) if "id" in r else ("sample seq " + r["seq"]),
                "case": r["case"][:60], "original": [o["deviation_tier"], o["direction"], o["class"], o["decision_rule_prediction"], o["elite_prediction"]],
                "recoded": [r["deviation_tier"], r["direction"], r["class"], r["decision_rule_prediction"], r["elite_prediction"]]}
               for o, r in list(zip(a, b)) + list(zip(sa, sb))
               if (o["deviation_tier"], o["direction"]) != (r["deviation_tier"], r["direction"])]
    return {"recoded_rows_changed": changed,
            "T1_current_configuration": {"original": configuration(a), "recoded": configuration(b)},
            "comparison_sample": {"original": sample_summary(sa), "recoded": sample_summary(sb)}}

if __name__ == "__main__":
    print(json.dumps(compute(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
