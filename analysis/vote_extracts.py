#!/usr/bin/env python3
"""Extract the Knesset plenum votes on a sampled law's passage day, with per-faction counts (change log (al)).

Usage: python3 vote_extracts.py FRAME_CSV DATA_DIR OUT_JSON SEQ [SEQ ...]
DATA_DIR holds kns_plenumvote.csv, kns_plenumvoteresult.csv and kns_persontoposition.csv from the
Open Knesset mirror (production.oknesset.org/pipelines/data/knesset/ and .../members/), which cover
October 2003 onward. For each row, every vote whose title names a Basic Law bill on the subject's
Basic Law is listed, on the passage date or the day after (a sitting that runs past midnight records
its later votes under the next day), or for a row dated by publication, in the fourteen days before it. Vote titles are bill titles, whose numbers can differ from the law's, so the extract
lists candidates and leaves to the coder which vote approved the law; votes on reservations are
counted, not listed. Third-reading votes carry
counts by faction, the faction being the member's on the day of the vote.
"""
import sys, csv, io, json, os, re, datetime, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_frame import SUBJECTS, norm_text

SUBJ_KW = {name: kw for kw, name in SUBJECTS}

def window(r):
    d = datetime.date.fromisoformat(r["passage_date"][:10])
    if r["date_basis"] == "passed": return d, d + datetime.timedelta(days=1)
    return d - datetime.timedelta(days=14), d

def main(frame_csv, data, out, seqs):
    frame = {r["seq"]: r for r in csv.DictReader(io.open(frame_csv, encoding="utf-8"))}
    want = {s: frame[s] for s in seqs}
    votes = {}
    for v in csv.DictReader(io.open(os.path.join(data, "kns_plenumvote.csv"), encoding="utf-8")):
        if "יסוד" not in v["VoteTitle"]: continue
        vd = datetime.date.fromisoformat(v["VoteDateTime"][:10])
        for s, r in want.items():
            lo, hi = window(r)
            kw = SUBJ_KW.get(r["subject"], "")
            if lo <= vd <= hi and kw and norm_text(kw) in norm_text(v["VoteTitle"]):
                votes.setdefault(v["Id"], {"vote": v, "seqs": []})["seqs"].append(s)
    final_ids = {i for i, x in votes.items() if "שלישית" in x["vote"]["ForOptionDesc"] or "שלישית" in x["vote"]["VoteSubject"]}
    results = collections.defaultdict(list)
    for x in csv.DictReader(io.open(os.path.join(data, "kns_plenumvoteresult.csv"), encoding="utf-8")):
        if x["VoteID"] in votes: results[x["VoteID"]].append(x)
    positions = collections.defaultdict(list)
    for p in csv.DictReader(io.open(os.path.join(data, "kns_persontoposition.csv"), encoding="utf-8")):
        if p["FactionID"]: positions[p["PersonID"]].append(p)
    def faction(mk, when):
        for p in positions.get(mk, []):
            if p["StartDate"][:10] <= when and (not p["FinishDate"] or when <= p["FinishDate"][:10]): return p["FactionName"]
        return "faction not recorded"
    extracts = {}
    for s in seqs:
        lines, reservations = [], 0
        for i, x in sorted(votes.items(), key=lambda kv: kv[1]["vote"]["VoteDateTime"]):
            if s not in x["seqs"]: continue
            v = x["vote"]; res = results.get(i, [])
            if "הסתייגות" in v["ForOptionDesc"]:
                reservations += 1; continue
            tally = collections.Counter(r["ResultDesc"] for r in res)
            stage = v["ForOptionDesc"] or v["VoteSubject"]
            line = (f"vote {i}, {v['VoteDateTime'].replace('T', ' ')[:16]}, '{v['VoteTitle']}', {stage} ({v['VoteMethodDesc']}): "
                    f"{tally.get('בעד', 0)} for, {tally.get('נגד', 0)} against, {tally.get('נמנע', 0)} abstain")
            if i in final_ids:
                when = v["VoteDateTime"][:10]
                parts = []
                for desc, label in (("בעד", "For"), ("נגד", "Against"), ("נמנע", "Abstain")):
                    by = collections.Counter(faction(r["MkId"], when) for r in res if r["ResultDesc"] == desc)
                    if by: parts.append(f"{label}: " + ", ".join(f"{k} {n}" for k, n in by.most_common()))
                if parts: line += ". " + ". ".join(parts)
            lines.append(line + ".")
        lo, hi = window(frame[s])
        if reservations: lines.append(f"plus {reservations} votes on reservations, not listed.")
        extracts[s] = " | ".join(lines) if lines else f"no plenum vote on a Basic Law bill on this subject found in the Open Knesset vote table between {lo} and {hi}"
    io.open(out, "w", encoding="utf-8").write(json.dumps(extracts, ensure_ascii=False, indent=1) + "\n")
    for s in seqs: print(s, extracts[s][:300])

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:])
