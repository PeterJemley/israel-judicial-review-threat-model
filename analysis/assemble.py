#!/usr/bin/env python3
"""Assemble the recoded codebook from the blind-coding files and run the pre-outcome checks.

Usage: python3 assemble.py CODING_DIR OUT_CSV
Reads coder-A.json, coder-B.json, adjudications.json (optional), docket.json (optional) in CODING_DIR.
"""
import sys, json, csv, io, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from t1_revised import classify, F_of, detect, SIGNS

ENACTMENTS = {
 "1": ("Basic Law: Human Dignity and Liberty (1992)", 1992, "Basic Law", "a2"),
 "2": ("Knesset and Local Authorities Elections (Financing, Limitation of Expenses and Audit) Law, 5729-1969", 1969, "Regular statute", "b"),
 "3": ("Elections (Confirmation of Validity of Laws) Law, 5729-1969", 1969, "Regular statute", "b"),
 "4": ("Basic Law: Freedom of Occupation (Amendment), 1994 (override clause)", 1994, "Basic Law amendment", "a"),
 "5": ("Basic Law: State Budget for 2017 and 2018 (Special Provisions) (Temporary Provision), 2016", 2016, "Basic Law amendment (temporary provision)", "a"),
 "6": ("Basic Law: The Knesset (Amendment No. 50, Temporary Provision), 2020", 2020, "Basic Law amendment (temporary provision)", "a"),
 "7": ("Basic Law: Israel, the Nation State of the Jewish People (2018)", 2018, "Basic Law", "a"),
 "8": ("Basic Law: The Government (Amendment No. 12), 2023", 2023, "Basic Law amendment", "a"),
 "9": ("Basic Law: The Judiciary (Amendment No. 3), 2023", 2023, "Basic Law amendment", "a"),
}
PREDICTORS = ["named_beneficiary","immediate_effect","coalition_only","expedited","scope","temporary_provision","targets_judiciary","required_majority_met","deviation_tier","direction"]

def load(d, name):
    p = os.path.join(d, name)
    return json.load(io.open(p, encoding="utf-8")) if os.path.exists(p) else None

def main(d, out):
    A = load(d, "coder-A.json"); B = load(d, "coder-B.json")
    ADJ = load(d, "adjudications.json") or {"adjudications": []}
    DOCK = load(d, "docket.json") or {}
    adj = {(str(a["enactment"]), a["variable"]): a for a in ADJ.get("adjudications", [])}
    rows = []
    for k, (title, year, etype, unit) in ENACTMENTS.items():
        row = {"id": k, "case": title, "year": year, "enactment_type": etype, "unit": unit}
        prov = {}
        for v in PREDICTORS:
            va = (A.get(k, {}).get(v) or {}).get("value", "") if A else ""
            vb = (B.get(k, {}).get(v) or {}).get("value", "") if B else ""
            if (k, v) in adj:
                row[v] = adj[(k, v)]["value"]; prov[v] = "adjudicated"
            elif va == vb:
                row[v] = va; prov[v] = "agreed" if va != "" else "both blank"
            else:
                row[v] = ""; prov[v] = f"disagreement unresolved (A={va!r}, B={vb!r})"
        dk = DOCK.get(k, {})
        row["litigation_timing"] = (dk.get("litigation_timing") or {}).get("value", "")
        row["outcome"] = (dk.get("outcome") or {}).get("value", "")
        row["judgment_date"] = (dk.get("outcome") or {}).get("judgment_date", "") or ""
        jy = int(row["judgment_date"][:4]) if row["judgment_date"][:4].isdigit() else None
        row["primary_analysis"] = "Yes" if (unit in ("a", "a2") and jy and jy >= 1995 and row["outcome"] in ("Adverse", "Not adverse")) else "No"
        cls, dpred, epred, grp = classify({**{s: row[s] for s in SIGNS}, "deviation_tier": row["deviation_tier"], "direction": row["direction"]})
        row["F"] = F_of(row) if all(row[s] for s in SIGNS) else ""
        row["class"] = cls; row["decision_rule_prediction"] = dpred or ""; row["elite_prediction"] = epred or ""; row["group"] = grp or ""
        row["provenance"] = "; ".join(f"{v}: {prov[v]}" for v in PREDICTORS)
        rows.append(row)
    cols = ["id","case","year","enactment_type","unit"] + PREDICTORS + ["litigation_timing","outcome","judgment_date","primary_analysis","F","class","decision_rule_prediction","elite_prediction","group","provenance"]
    with io.open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    prim = [r for r in rows if r["primary_analysis"] == "Yes" and r["class"] in ("concordant","discordant","undetermined")]
    N = len(prim); K = sum(1 for r in prim if r["outcome"] == "Adverse")
    disc = [r for r in prim if r["class"] == "discordant"]
    DA = sum(1 for r in disc if r["decision_rule_prediction"] == "Adverse"); DN = len(disc) - DA
    summary = {"rows": len(rows), "primary_rows_coded": N, "K_adverse": K, "discordant": len(disc),
               "D_A": DA, "D_N": DN,
               "discordant_rows": [(r["id"], r["case"][:40], r["decision_rule_prediction"], r["elite_prediction"], r["group"]) for r in disc],
               "uncoded_or_excluded": [(r["id"], r["class"], r["primary_analysis"]) for r in rows if r["primary_analysis"] != "Yes" or r["class"] == "uncoded"]}
    summary["detectability"] = detect(N, K, DA, DN) if N > 0 else "no primary rows"
    print(json.dumps(summary, indent=1, ensure_ascii=False))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
