#!/usr/bin/env python3
"""Assemble the comparison sample's codebook from the batch coding files (change log (ah), (aj), (ak)).

Usage: python3 assemble_sample.py CODING_DIR OUT_CSV
Reads rows.json and, for each batch n, coder-A-b{n}.json, coder-B-b{n}.json, adjudications-b{n}.json
(optional), circumstances-b{n}.json (optional), docket-b{n}.json (optional). Writes one row per sampled
enactment with the same predictor columns as the main codebook, the predictions under both beneficiary
signs for description, the outcome (Not challenged), provenance, and the one-vote check fields.
"""
import sys, json, csv, io, os, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from t1_revised import classify, F_of, signs, PRIMARY_BENEFICIARY, TEXT_BENEFICIARY, kappa

CODER_PREDICTORS = ["named_beneficiary","immediate_effect","coalition_only","expedited","scope","temporary_provision","targets_judiciary","deviation_tier","direction"]
PREDICTORS = ["named_beneficiary","situated_beneficiary","immediate_effect","coalition_only","expedited","scope","temporary_provision","targets_judiciary","deviation_tier","direction"]
PRED_IN = ["named_beneficiary","situated_beneficiary","immediate_effect","coalition_only","expedited","deviation_tier","direction"]

def load_all(d, prefix):
    out = {}
    for path in sorted(glob.glob(os.path.join(d, f"{prefix}-b*.json"))):
        data = json.load(io.open(path, encoding="utf-8"))
        for k, v in data.items():
            if k.isdigit(): out[k] = v
    return out

def load_adj(d):
    adj = {}
    for path in sorted(glob.glob(os.path.join(d, "adjudications-b*.json"))):
        for a in json.load(io.open(path, encoding="utf-8")).get("adjudications", []):
            adj[(str(a["enactment"]), a["variable"])] = a
    return adj

def main(d, out):
    manifest = json.load(io.open(os.path.join(d, "rows.json"), encoding="utf-8"))
    A, B = load_all(d, "coder-A"), load_all(d, "coder-B")
    C, K = load_all(d, "circumstances"), load_all(d, "docket")
    adj = load_adj(d)
    rows, agree = [], {v: [] for v in CODER_PREDICTORS}
    for m in manifest:
        k = m["seq"]
        if k not in A and k not in B: continue
        row = {"seq": k, "batch": m["batch"], "case": m["title_he"], "title_en": m["title_en"], "year": m["passage_date"][:4], "passage_date": m["passage_date"],
               "enactment_type": m["kind"], "subject": m["subject"], "unit": "c"}
        prov = {}
        for v in CODER_PREDICTORS:
            va = (A.get(k, {}).get(v) or {}).get("value", "") or ""
            vb = (B.get(k, {}).get(v) or {}).get("value", "") or ""
            if k in A and k in B: agree[v].append((va, vb))
            if (k, v) in adj: row[v] = adj[(k, v)]["value"]; prov[v] = "adjudicated"
            elif va == vb: row[v] = va; prov[v] = "agreed" if va else "both blank"
            else: row[v] = ""; prov[v] = f"disagreement unresolved (A={va!r}, B={vb!r})"
        sb = (C.get(k, {}).get("situated_beneficiary") or {})
        row["situated_beneficiary"] = sb.get("value", "") or ""; prov["situated_beneficiary"] = f"circumstances reader, closed list {sb.get('list_version','(ae)')}" if row["situated_beneficiary"] else "not coded"
        dk = K.get(k, {})
        row["litigation_timing"] = (dk.get("litigation_timing") or {}).get("value", "") or ""
        row["outcome"] = (dk.get("outcome") or {}).get("value", "Not challenged") if dk else "Not challenged"
        row["primary_analysis"] = "No"
        pred_in = {s: row[s] for s in PRED_IN}
        cls, dp, ep, grp = classify(pred_in, bkey=PRIMARY_BENEFICIARY)
        row["F"] = F_of(row, PRIMARY_BENEFICIARY) if all(row[s] for s in signs(PRIMARY_BENEFICIARY)) else ""
        row["class"], row["decision_rule_prediction"], row["elite_prediction"], row["group"] = cls, dp or "", ep or "", grp or ""
        cls_t, dp_t, ep_t, grp_t = classify(pred_in, bkey=TEXT_BENEFICIARY)
        row["F_text"] = F_of(row, TEXT_BENEFICIARY) if all(row[s] for s in signs(TEXT_BENEFICIARY)) else ""
        row["class_text"], row["decision_rule_prediction_text"], row["group_text"] = cls_t, dp_t or "", grp_t or ""
        row["elite_prediction"] = row["elite_prediction"] or (ep_t or "")
        fa = (A.get(k, {}).get("final_vote_record") or {}); fb = (B.get(k, {}).get("final_vote_record") or {})
        row["final_vote_A"] = str(fa.get("value", "")) + (f" [{fa.get('note','')}]" if fa.get("note") else "")
        row["final_vote_B"] = str(fb.get("value", "")) + (f" [{fb.get('note','')}]" if fb.get("note") else "")
        row["provenance"] = "; ".join(f"{v}: {prov[v]}" for v in PREDICTORS)
        rows.append(row)
    cols = ["seq","batch","case","title_en","year","passage_date","enactment_type","subject","unit"] + PREDICTORS + ["litigation_timing","outcome","primary_analysis","F","class","decision_rule_prediction","elite_prediction","group","F_text","class_text","decision_rule_prediction_text","group_text","final_vote_A","final_vote_B","provenance"]
    with io.open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    kap = {v: {"kappa": (None if kappa([a for a, b in p], [b for a, b in p]) is None else round(kappa([a for a, b in p], [b for a, b in p]), 3)) if p else None,
               "agree": sum(1 for a, b in p if a == b), "n": len(p)} for v, p in agree.items()}
    shared = {}
    for r in rows:
        ids = set(re.findall(r"vote\s*(\d{3,6})", r["final_vote_A"] + " " + r["final_vote_B"]))
        for i in ids: shared.setdefault(i, []).append(r["seq"])
    summary = {"rows_coded": len(rows), "by_batch": {b: sum(1 for r in rows if r["batch"] == b) for b in (1, 2, 3)},
               "agreement": kap,
               "unresolved_disagreements": [(r["seq"], v) for r in rows for v in CODER_PREDICTORS if r["provenance"].find(f"{v}: disagreement") >= 0],
               "F_distribution": {str(f): sum(1 for r in rows if r["F"] == f) for f in (0, 1, 2, 3, 4)},
               "uncoded_for_F": [r["seq"] for r in rows if r["F"] == ""],
               "direction": {dv: sum(1 for r in rows if r["direction"] == dv) for dv in ("Illiberal", "Liberal", "Neutral", "")},
               "one_vote_check": {"vote_ids_shared_by_two_rows": {i: s for i, s in shared.items() if len(s) > 1},
                                  "rows_reporting_a_joint_vote_or_no_final_vote": [(r["seq"], r["final_vote_A"][:120]) for r in rows if re.search(r"also approved|joint|together with|no final vote|not found|could not", (r["final_vote_A"] + r["final_vote_B"]).lower())]}}
    print(json.dumps(summary, indent=1, ensure_ascii=False))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
