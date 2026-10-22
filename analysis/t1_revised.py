#!/usr/bin/env python3
"""T1 as revised on 2026-10-22: exact permutation analysis and pre-outcome checks.

Usage:
  python3 t1_revised.py null N K D_A D_N            # exact null of S, tails, type-one rate
  python3 t1_revised.py detect N K D_A D_N          # detectability check at attainable extremes
  python3 t1_revised.py predict CSV                 # apply the prediction table to a coded CSV
  python3 t1_revised.py kappa A.json B.json         # per-variable Cohen's kappa between two coders
  python3 t1_revised.py shuffle N K D_A D_N [reps]  # implementation check by shuffling

S = (discordant rows matching the decision-rule prediction) - (matching the elite prediction).
Under permutation of K Adverse labels over N primary rows with D_A discordant rows predicted
Adverse and D_N predicted Not adverse by the decision rule, X_A ~ hypergeometric draws of
Adverse into group A, X_N into group N, jointly multivariate hypergeometric, and
S = (X_A - (D_A - X_A)) - ((D_N - X_N) - X_N) = 2*X_A - 2*X_N + D_N - D_A.
"""
import sys, json, csv, math, random
from collections import Counter, defaultdict

def comb(n, k):
    if k < 0 or k > n: return 0
    return math.comb(n, k)

def null_dist(N, K, DA, DN):
    """Exact distribution of S as a dict value -> probability."""
    rest = N - DA - DN
    total = comb(N, K)
    dist = defaultdict(float)
    for xa in range(0, DA + 1):
        for xn in range(0, DN + 1):
            xr = K - xa - xn
            if xr < 0 or xr > rest: continue
            p = comb(DA, xa) * comb(DN, xn) * comb(rest, xr) / total
            S = 2 * xa - 2 * xn + DN - DA
            dist[S] += p
    return dict(dist)

def two_sided_p(dist, s):
    upper = sum(p for v, p in dist.items() if v >= s)
    lower = sum(p for v, p in dist.items() if v <= s)
    return min(1.0, 2 * min(upper, lower))

def null_mean(dist):
    return sum(v * p for v, p in dist.items())

def type_one_rate(dist):
    """Probability under the null that the step 8 rule rejects (p < 0.05)."""
    return sum(p for v, p in dist.items() if two_sided_p(dist, v) < 0.05)

def detect(N, K, DA, DN):
    dist = null_dist(N, K, DA, DN)
    smax, smin = max(dist), min(dist)
    mean = null_mean(dist)
    out = {
        "N": N, "K": K, "D_A": DA, "D_N": DN, "discordant": DA + DN,
        "null_mean": round(mean, 4),
        "S_max_attainable": smax, "p_at_S_max": round(two_sided_p(dist, smax), 4),
        "S_min_attainable": smin, "p_at_S_min": round(two_sided_p(dist, smin), 4),
        "exact_type_one_rate": round(type_one_rate(dist), 4),
    }
    out["supported_detectable"] = out["p_at_S_max"] < 0.05 and smax > mean
    out["refuted_detectable"] = out["p_at_S_min"] < 0.05 and smin < mean
    out["minimum_six_met"] = (DA + DN) >= 6
    out["verdict_before_outcomes"] = ("proceed" if out["minimum_six_met"] and out["supported_detectable"] and out["refuted_detectable"] else "Inconclusive, declared before outcomes")
    return out

def shuffle_check(N, K, DA, DN, reps=1000, seed=1):
    dist = null_dist(N, K, DA, DN)
    rng = random.Random(seed)
    labels = [1] * K + [0] * (N - K)
    rejections = 0
    for _ in range(reps):
        rng.shuffle(labels)
        xa = sum(labels[:DA]); xn = sum(labels[DA:DA + DN])
        S = 2 * xa - 2 * xn + DN - DA
        if two_sided_p(dist, S) < 0.05: rejections += 1
    return {"shuffle_rate": rejections / reps, "exact_rate": round(type_one_rate(dist), 4), "within_0.02": abs(rejections / reps - type_one_rate(dist)) <= 0.02}

# ---- prediction table (T1 revised, Predictions) ----
# The beneficiary sign is `situated_beneficiary` in the primary analysis and `named_beneficiary`
# in the secondary analysis of step 11a (change log (ac), 2026-10-22).
PRIMARY_BENEFICIARY = "situated_beneficiary"
TEXT_BENEFICIARY = "named_beneficiary"

def signs(bkey=PRIMARY_BENEFICIARY):
    return [bkey, "immediate_effect", "coalition_only", "expedited"]

SIGNS = signs()

def F_of(row, bkey=PRIMARY_BENEFICIARY):
    f = 0
    f += 1 if row[bkey] == "Yes" else 0
    f += 1 if row["immediate_effect"] == "Yes" else 0   # Deferred counts as absent
    f += 1 if row["coalition_only"] == "Yes" else 0
    f += 1 if row["expedited"] == "Yes" else 0
    return f

def decision_rule_prediction(row, variant=False, bkey=PRIMARY_BENEFICIARY):
    """Returns (prediction, table_row_number) or ("Undetermined", 6)."""
    F = F_of(row, bkey); tier = row["deviation_tier"]; co = row["coalition_only"]
    first_threshold = 3 if variant else 4
    fifth_max = 2 if variant else 3
    if F >= first_threshold: return ("Adverse", 1)
    if tier == "Sharp": return ("Adverse", 2)
    if tier == "Limited" and co == "Yes": return ("Adverse", 3)
    if tier == "Limited" and co == "No" and F <= 1: return ("Not adverse", 4)
    if tier in ("Entrenches", "None") and F <= fifth_max: return ("Not adverse", 5)
    return ("Undetermined", 6)

def elite_prediction(row):
    return "Adverse" if row["direction"] == "Illiberal" else "Not adverse"

def required(bkey=PRIMARY_BENEFICIARY):
    return signs(bkey) + ["deviation_tier", "direction"]

REQUIRED = required()

def classify(row, variant=False, bkey=PRIMARY_BENEFICIARY):
    if any((row.get(k) or "") == "" for k in required(bkey)): return ("uncoded", None, None, None)
    d, trow = decision_rule_prediction(row, variant, bkey)
    if d == "Undetermined": return ("undetermined", d, elite_prediction(row), trow)
    e = elite_prediction(row)
    group = {1: "purpose-driven", 2: "content-driven"}.get(trow, "tier-and-support-driven")
    return ("discordant" if d != e else "concordant", d, e, group)

def predict_csv(path, variant=False, bkey=PRIMARY_BENEFICIARY):
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    out = []
    for r in rows:
        norm = {k: (r.get(k) or "").split(" (")[0].strip() for k in required(bkey)}
        cls, d, e, grp = classify(norm, variant, bkey)
        out.append({"case": r["case"], "F": F_of(norm, bkey) if all(norm[k] for k in signs(bkey)) else None,
                    "class": cls, "decision_rule": d, "elite": e, "group": grp,
                    "primary": r.get("primary_analysis", ""), "outcome": r.get("outcome", "")})
    return out

def kappa(a, b):
    """Cohen's kappa for two aligned lists of labels (blanks included as a label)."""
    n = len(a)
    if n == 0: return None
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)

def kappa_report(pa, pb):
    A = json.load(open(pa)); B = json.load(open(pb))
    keys = sorted((k for k in set(A) & set(B) if k.isdigit()), key=lambda k: int(k))
    variables = sorted({v for k in keys for v in A[k]} | {v for k in keys for v in B[k]})
    rep = {}
    for v in variables:
        la = [str((A[k].get(v) or {}).get("value", "")) for k in keys]
        lb = [str((B[k].get(v) or {}).get("value", "")) for k in keys]
        rep[v] = {"kappa": None if kappa(la, lb) is None else round(kappa(la, lb), 3),
                  "agree": sum(1 for x, y in zip(la, lb) if x == y), "n": len(keys),
                  "disagreements": [k for k, x, y in zip(keys, la, lb) if x != y]}
    return rep

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "null":
        N, K, DA, DN = map(int, sys.argv[2:6]); d = null_dist(N, K, DA, DN)
        print(json.dumps({"null_mean": null_mean(d), "support": sorted(d), "type_one_rate": type_one_rate(d)}, indent=1))
    elif cmd == "detect":
        print(json.dumps(detect(*map(int, sys.argv[2:6])), indent=1))
    elif cmd == "shuffle":
        args = list(map(int, sys.argv[2:7])); print(json.dumps(shuffle_check(*args), indent=1))
    elif cmd == "predict":
        variant = len(sys.argv) > 3 and sys.argv[3] == "variant"
        for r in predict_csv(sys.argv[2], variant): print(json.dumps(r, ensure_ascii=False))
    elif cmd == "kappa":
        print(json.dumps(kappa_report(sys.argv[2], sys.argv[3]), indent=1, ensure_ascii=False))
