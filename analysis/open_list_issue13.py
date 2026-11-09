#!/usr/bin/env python3
"""Issue 13: T1 under an alternative prediction rule read from the judgments, beside the 22 October table.

Usage: python3 open_list_issue13.py
The alternative rule (research/revision-2026-11-09-issue13/README.md): a suspicious characteristic
(situated_beneficiary Yes or temporary_provision Yes) predicts Adverse; otherwise Sharp predicts Adverse,
Limited with coalition_only Yes predicts Adverse, Limited with coalition_only No predicts Not adverse, and
Entrenches or None predicts Not adverse. A row counts as coded only if it is coded under the 22 October
table, so both rules are compared on the same rows. Nothing is written; exploratory.
"""
import sys, os, json
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t1_revised as t1
from sensitivity_issue33 import load_csv, norm, configuration

def open_list_prediction(r):
    if r.get("situated_beneficiary") == "Yes" or r.get("temporary_provision") == "Yes":
        return ("Adverse", "1'")
    tier, co = r["deviation_tier"], r["coalition_only"]
    if tier == "Sharp": return ("Adverse", "2'")
    if tier == "Limited" and co == "Yes": return ("Adverse", "3'")
    if tier == "Limited" and co == "No": return ("Not adverse", "4'")
    if tier in ("Entrenches", "None"): return ("Not adverse", "5'")
    return ("Undetermined", "")

def classify_open(rows):
    out = []
    for r in rows:
        n = norm(r)
        cls, _, _, _ = t1.classify(n)
        if cls == "uncoded":
            out.append({**r, "class": "uncoded", "decision_rule_prediction": "", "elite_prediction": "", "line": ""})
            continue
        d, line = open_list_prediction({**n, "temporary_provision": (r.get("temporary_provision") or "").split(" (")[0].strip()})
        e = t1.elite_prediction(n)
        c = "undetermined" if d == "Undetermined" else ("discordant" if d != e else "concordant")
        out.append({**r, "class": c, "decision_rule_prediction": d, "elite_prediction": e, "line": line})
    return out

def classify_table(rows):
    out = []
    for r in rows:
        cls, d, e, _ = t1.classify(norm(r))
        out.append({**r, "class": cls, "decision_rule_prediction": d or "", "elite_prediction": e or ""})
    return out

def compute():
    code = load_csv("codebook/m4-codebook.csv")
    sample = load_csv("codebook/comparison-sample.csv")
    a, b = classify_table(code), classify_open(code)
    sa, sb = classify_table(sample), classify_open(sample)
    rows = [{"id": x["id"], "case": x["case"][:50], "outcome": x["outcome"],
             "table": [x["class"], x["decision_rule_prediction"]], "alternative": [y["class"], y["decision_rule_prediction"], y["line"]],
             "elite": y["elite_prediction"]} for x, y in zip(a, b) if x.get("primary_analysis") == "Yes"]
    def discordant_hits(rs):
        p = [r for r in rs if r.get("primary_analysis") == "Yes" and r["class"] == "discordant"]
        return {"decision_rule_right": sum(1 for r in p if r["decision_rule_prediction"] == r["outcome"]),
                "elite_right": sum(1 for r in p if r["elite_prediction"] == r["outcome"])}
    return {"primary_rows": rows,
            "T1_current_configuration": {"table": configuration(a), "alternative": configuration(b)},
            "discordant_rows_against_outcomes": {"table": discordant_hits(a), "alternative": discordant_hits(b)},
            "row10": {"table": next(x["class"] for x in a if x["id"] == "10"), "alternative": next(x["class"] for x in b if x["id"] == "10")},
            "comparison_sample_classes": {"table": dict(sorted(Counter(r["class"] for r in sa).items())),
                                          "alternative": dict(sorted(Counter(r["class"] for r in sb).items()))}}

if __name__ == "__main__":
    print(json.dumps(compute(), indent=1, ensure_ascii=False))
