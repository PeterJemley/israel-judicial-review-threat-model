#!/usr/bin/env python3
"""Build the codebook's descriptive columns (issue 16; change log (bd)).

Usage: python3 descriptive.py [--refresh]
Writes codebook/m4-descriptive.csv, keyed by the codebook's row id:
- days from the first reading to the final vote, with both dates;
- the votes for at the final reading, the opposition members among them, and their share of the votes for;
- for each number, the source.

Rows from October 2003 on are read from the Knesset's open-data service (KNS_PlenumVote and
KNS_PlenumVoteResult, by bill ID). The final vote is the vote accepting the bill at its third reading.
The first reading is the last vote before it that sends the bill to committee for its second and third
readings: the service labels some preliminary readings that way too (the Nation-State bill's of 10 May
2017, which the coders and the project's records give as the preliminary reading), so earlier such votes
are listed in the note column, not used. Where the service lacks the final vote, the row falls back to
the coders' notes, and a row coded `coalition_only` Yes still has an opposition share of 0. The raw query
results are kept in research/descriptive-2026-11-05/knesset-votes.json, and --refresh queries the service
again. Which members voted for as opposition members comes from the coding files, never from this
script: a row coded `coalition_only` Yes has none; a row coded No has the members the coders named
(CROSS_PARTY below, each checked against the roll call); a row with the cell blank gets no share.
Rows before October 2003 take the number of days only where both coders gave the same exact number in
their notes, and no share. Nothing is typed in by hand except the bill IDs and the coders' names,
each cited.
"""
import sys, os, re, csv, io, json, datetime, subprocess, urllib.parse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def path(p): return os.path.join(ROOT, p)

# Knesset bill IDs (KNS_Bill), found by name in the Knesset's open data on 4 and 5 November 2026.
BILL = {"5": 2006018, "6": 2143677, "7": 565913, "8": 2201424, "9": 2207472, "10": 2201200}
# Opposition members who voted for, as the coders named them (research/coding-2026-10-22/coder-A.json,
# row 5, coalition_only note: "Nachman Shai (Zionist Union, opposition) voted for").
CROSS_PARTY = {"5": [("נחמן", "שי")]}
CACHE = path("research/descriptive-2026-11-05/knesset-votes.json")
API = "https://knesset.gov.il/OdataV4/ParliamentInfo/"

def get(entity, flt):
    out, skip = [], 0
    while True:
        url = API + entity + "?" + urllib.parse.urlencode({"$filter": flt, "$skip": str(skip)})
        r = json.loads(subprocess.run(["curl", "-sS", "-m", "120", url], capture_output=True, text=True, check=True).stdout)["value"]
        out += r
        if len(r) < 100: return out
        skip += 100

def refresh():
    data = {}
    for rid, bill in BILL.items():
        votes = get("KNS_PlenumVote", f"ItemID eq {bill}")
        first = [v for v in votes if "להכנה לקריאה שניה" in v["ForOptionDesc"]]
        final = [v for v in votes if "שלישית" in v["ForOptionDesc"] and v["ForOptionDesc"].startswith("לקבל")]
        data[rid] = {"bill": bill, "first_reading": first, "final_reading": final,
                     "final_results": get("KNS_PlenumVoteResult", f"VoteID eq {final[-1]['Id']}") if final else []}
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    with io.open(CACHE, "w", encoding="utf-8") as f: json.dump(data, f, ensure_ascii=False, indent=1)

def exact_days(note):
    """The number of days in a coder's note, only if it is stated as an exact number."""
    if not note or re.search(r"at least|at most|more than|fewer than|before|between", note): return None
    m = re.findall(r"(\d+)\s*days", note)
    return int(m[-1]) if len(m) == 1 or (m and len(set(m)) == 1) else None

def main():
    if "--refresh" in sys.argv or not os.path.exists(CACHE): refresh()
    kn = json.load(io.open(CACHE, encoding="utf-8"))
    A = json.load(io.open(path("research/coding-2026-10-22/coder-A.json"), encoding="utf-8"))
    B = json.load(io.open(path("research/coding-2026-10-22/coder-B.json"), encoding="utf-8"))
    code = {r["id"]: r for r in csv.DictReader(io.open(path("codebook/m4-codebook.csv"), encoding="utf-8"))}
    out = []
    for rid, r in code.items():
        row = {"id": rid, "case": r["case"], "first_reading_date": "", "final_vote_date": "", "days_first_to_final": "", "days_source": "",
               "votes_for": "", "opposition_votes_for": "", "opposition_share": "", "share_source": "", "note": ""}
        if rid in kn and kn[rid]["final_reading"] and kn[rid]["first_reading"]:
            k = kn[rid]; fz = k["final_reading"][-1]
            before = [v for v in k["first_reading"] if v["VoteDateTime"] < fz["VoteDateTime"]]
            f1 = before[-1]
            if len(before) > 1:
                row["note"] = "earlier committee-referral votes not used as the first reading: " + ", ".join(f"{v['Id']} ({v['VoteDateTime'][:10]})" for v in before[:-1])
            d1 = datetime.date.fromisoformat(f1["VoteDateTime"][:10]); dz = datetime.date.fromisoformat(fz["VoteDateTime"][:10])
            row.update(first_reading_date=str(d1), final_vote_date=str(dz), days_first_to_final=(dz - d1).days,
                       days_source=f"Knesset open data, KNS_PlenumVote {f1['Id']} and {fz['Id']} (bill {k['bill']})")
            ayes = [x for x in k["final_results"] if x["ResultDesc"] == "בעד"]
            row["votes_for"] = len(ayes)
            src = f"Knesset open data, KNS_PlenumVoteResult for vote {fz['Id']}"
            co = r["coalition_only"].split(" (")[0].strip()
            if co == "Yes":
                row.update(opposition_votes_for=0, opposition_share="0", share_source=src + "; coalition_only Yes in the codebook")
            elif co == "No" and rid in CROSS_PARTY:
                found = [n for n in CROSS_PARTY[rid] if any(x["FirstName"] == n[0] and x["LastName"] == n[1] for x in ayes)]
                if len(found) != len(CROSS_PARTY[rid]): raise SystemExit(f"row {rid}: a named cross-party member is not among the votes for")
                row.update(opposition_votes_for=len(found), opposition_share=f"{len(found)}/{len(ayes)}",
                           share_source=src + "; opposition members as named in coder-A.json and checked in the roll call")
        else:
            da = exact_days((A.get(rid, {}).get("expedited") or {}).get("note")); db = exact_days((B.get(rid, {}).get("expedited") or {}).get("note"))
            if da is not None and da == db:
                row.update(days_first_to_final=da, days_source="both coders' notes on expedited (research/coding-2026-10-22/coder-A.json, coder-B.json)")
            if r["coalition_only"].split(" (")[0].strip() == "Yes":
                row.update(opposition_votes_for=0, opposition_share="0", share_source="coalition_only Yes in the codebook (no roll call in the Knesset's open data)")
        if rid in kn and row["days_first_to_final"] != "":
            da = exact_days((A.get(rid, {}).get("expedited") or {}).get("note")); db = exact_days((B.get(rid, {}).get("expedited") or {}).get("note"))
            if da is not None and da == db and da != row["days_first_to_final"]:
                row["note"] = (row["note"] + "; " if row["note"] else "") + f"the coders' notes give {da} days"
        out.append(row)
    cols = list(out[0].keys())
    with io.open(path("codebook/m4-descriptive.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\r\n"); w.writeheader(); w.writerows(out)
    for row in out: print(row["id"], row["days_first_to_final"], row["opposition_share"], "|", row["days_source"][:60], "|", row["share_source"][:50])

if __name__ == "__main__":
    main()
