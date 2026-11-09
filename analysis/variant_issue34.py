#!/usr/bin/env python3
"""Issue 34: report T1 and the comparison sample with the Arab-party variant of the cross-party sign.

Usage: python3 variant_issue34.py
For the rows that qualify (research/variant-2026-11-09-issue34/README.md), `coalition_only` is replaced by
`coalition_only_arab`: No if a member of an Arab party voted for at the final reading, Yes if the roll call
shows none did, blank if no member-by-member roll call is available. Other rows keep `coalition_only`.
The roll calls are in research/variant-2026-11-09-issue34/roll-calls.json. Nothing is written; the primary
sign is not changed. Exploratory: the variant was defined after the data were seen.
"""
import sys, os, io, json
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sensitivity_issue33 import path, load_csv, classify_rows, configuration, sample_summary

QUALIFYING_CODEBOOK = {"1", "7"}
QUALIFYING_SAMPLE = {"1", "16", "64", "103", "127"}

def variant_values():
    rolls = json.load(io.open(path("research/variant-2026-11-09-issue34/roll-calls.json"), encoding="utf-8"))["rows"]
    def v(key):
        r = rolls.get(key)
        if r is None: return ""
        return "No" if r["arab_party_votes_for"] else "Yes"
    return ({k: v("row" + k) for k in QUALIFYING_CODEBOOK}, {k: v(k) for k in QUALIFYING_SAMPLE})

def compute():
    vc, vs = variant_values()
    code = load_csv("codebook/m4-codebook.csv")
    sample = load_csv("codebook/comparison-sample.csv")
    code_v = [dict(r, coalition_only=vc[r["id"]]) if r["id"] in vc else dict(r) for r in code]
    sample_v = [dict(r, coalition_only=vs[r["seq"]]) if r["seq"] in vs else dict(r) for r in sample]
    a, b = classify_rows(code), classify_rows(code_v)
    sa, sb = classify_rows(sample), classify_rows(sample_v)
    changed = [{"row": ("codebook " + r["id"]) if "id" in r else ("sample seq " + r["seq"]), "case": r["case"][:60],
                "original": [o["coalition_only"], o["class"], o["decision_rule_prediction"], o["elite_prediction"]],
                "variant": [r["coalition_only"], r["class"], r["decision_rule_prediction"], r["elite_prediction"]]}
               for o, r in list(zip(a, b)) + list(zip(sa, sb)) if o["coalition_only"] != r["coalition_only"]]
    def co(rows): return dict(sorted(Counter(r["coalition_only"] or "blank" for r in rows).items()))
    return {"qualifying": {"codebook": sorted(QUALIFYING_CODEBOOK, key=int), "sample": sorted(QUALIFYING_SAMPLE, key=int)},
            "variant_values": {"codebook": vc, "sample": vs},
            "rows_changed": changed,
            "T1_current_configuration": {"original": configuration(a), "variant": configuration(b)},
            "comparison_sample": {"original": {**sample_summary(sa), "coalition_only": co(sa)},
                                  "variant": {**sample_summary(sb), "coalition_only": co(sb)}},
            "combined_with_issue33": combined(code_v, sample_v)}

def combined(code_v, sample_v):
    """The variant together with issue 33's exploratory recode of deviation_tier and direction."""
    final = json.load(io.open(path("research/recode-2026-11-09-issue33/final.json"), encoding="utf-8"))
    rc = {k: {c: (v[c]["value"] if isinstance(v[c], dict) else v[c]) for c in ("deviation_tier", "direction")} for k, v in final.items()}
    code_c = [dict(r, **rc["row" + r["id"]]) if ("row" + r["id"]) in rc else dict(r) for r in code_v]
    sample_c = [dict(r, **rc[r["seq"]]) if r["seq"] in rc else dict(r) for r in sample_v]
    c, sc = classify_rows(code_c), classify_rows(sample_c)
    return {"T1_current_configuration": configuration(c),
            "sample_classes": dict(sorted(Counter(r["class"] for r in sc).items())),
            "qualifying_sample_rows": [{"seq": r["seq"], "deviation_tier": r["deviation_tier"], "direction": r["direction"],
                                        "coalition_only": r["coalition_only"], "class": r["class"],
                                        "decision_rule_prediction": r["decision_rule_prediction"], "elite_prediction": r["elite_prediction"]}
                                       for r in sc if r["seq"] in QUALIFYING_SAMPLE]}

if __name__ == "__main__":
    print(json.dumps(compute(), indent=1, ensure_ascii=False))
