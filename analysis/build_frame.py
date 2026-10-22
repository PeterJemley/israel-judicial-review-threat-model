#!/usr/bin/env python3
"""Build the chronological frame of laws titled Basic Law (change log (ah)).

Usage: python3 build_frame.py FRAME_DIR OUT_CSV [--draw]
Reads every frame-*.json in FRAME_DIR (each with "entries"), challenges.json (with "challenged") and
same-page-order.json (the printed order of laws passed the same day on the same gazette page).
One row per law as passed; entries reported by two readers for the same law (indirect amendments)
are merged when they share the gazette issue and page and name the same law (the Basic Law first
named in the title and the amendment number), else on title and year. Rows are ordered by passage
date, then gazette issue and page as numbers, then printed order on the page. Challenged enactments
are matched on subject, passage date (or year) and amendment number. With --draw, every third
unchallenged row from the first in chronological order is marked sampled (positions 1, 4, 7, ...).

Corrected on 22 October 2026 (change log (al)): the first version merged on issue and page alone,
which collapsed eight pairs of separately titled laws printed on one page into single rows, read
a date as the page where the page had one digit, and ordered same-day rows by the text of the
gazette reference. analysis/frame_merge_check.py keeps the first version's key as a record.
"""
import sys, json, csv, io, os, re, glob

DIGITS = re.compile(r"\d+")
SUBJECTS = [("לימוד תורה", "Torah Study"), ("מדינת הלאום", "Nation State"), ("כבוד האדם", "Human Dignity and Liberty"),
            ("חופש העיסוק", "Freedom of Occupation"), ("משאל עם", "Referendum"), ("תקציב המדינה", "State Budget (temporary Basic Law)"),
            ("משק המדינה", "State Economy"), ("השפיטה", "Judiciary"), ("מבקר המדינה", "State Comptroller"), ("ירושלים", "Jerusalem"),
            ("הצבא", "Army"), ("נשיא המדינה", "President"), ("מקרקעי ישראל", "Israel Lands"), ("הממשלה", "Government"), ("הכנסת", "Knesset")]

def norm_text(s):
    s = s or ""
    for a, b in (("״", '"'), ("׳", "'"), ("־", "-"), ("–", "-"), ("—", "-")):
        s = s.replace(a, b)
    s = re.sub(r"[\s\-:(),.'\"]+", " ", s)
    return s.strip().lower()

def subject_of(title):
    """The Basic Law named earliest in the title (so an indirect amendment named later does not win)."""
    t = norm_text(title)
    hits = [(t.find(norm_text(kw)), -len(kw), name) for kw, name in SUBJECTS if norm_text(kw) in t]
    return min(hits)[2] if hits else ""

KIND_RANK = {"enactment": 0, "re-enactment": 1, "temporary provision": 2, "amendment and temporary provision": 3, "amendment": 4}

PAGE = re.compile(r"(?:עמוד|עמ['׳’]?)\s*(\d+)")

def gazette_key(g):
    """(issue, page) of a Sefer HaHukkim reference: the page is the number after the page marker,
    the issue the first number of two or more digits before it. None if either is missing."""
    g = g or ""
    m = PAGE.search(g)
    if not m: return None
    issue = [n for n in DIGITS.findall(g[:m.start()]) if len(n) >= 2]
    return (issue[0], m.group(1)) if issue else None

def year_of(d):
    m = re.match(r"(\d{4})", d or "")
    return m.group(1) if m else ""

def amendment_no(title):
    t = (title or "").replace("׳", "'").replace("״", '"')
    m = re.search(r"תיקון\s*מס['\"]?\s*(\d+)", t)
    return m.group(1) if m else ""

def law_identity(title_he):
    """The Basic Law first named in the title and the amendment number ("" for none)."""
    return (subject_of(title_he), amendment_no(title_he))

def entry_key(e):
    gk = gazette_key(e.get("gazette"))
    if gk: return ("g",) + gk + law_identity(e.get("title_he"))
    return ("t", norm_text(e.get("title_he")), year_of(e.get("passage_date")))

SUFFIX = re.compile(r"\s+[—–-]\s+indirect amendment\b.*$")

def own_title_en(t):
    """The law's own English title, without a reader's ' — indirect amendment of ...' suffix."""
    return SUFFIX.sub("", t or "")

def load_page_order(d):
    """{(issue, page): {law_identity: rank}} from same-page-order.json."""
    path = os.path.join(d, "same-page-order.json")
    out = {}
    if not os.path.exists(path): return out
    for g in json.load(io.open(path, encoding="utf-8")).get("pages", []):
        out[tuple(g["gazette"])] = {(x["subject"], x["amendment_no"]): i for i, x in enumerate(g["order"])}
    return out

def sort_key(r, page_order):
    gk = gazette_key(r["gazette"])
    issue, page = (int(gk[0]), int(gk[1])) if gk else (10**6, 10**6)
    rank = page_order.get(gk, {}).get(law_identity(r["title_he"]), 0) if gk else 0
    return (r["passage_date"] or "9999", issue, page, rank)

def load_frames(d):
    rows, order = {}, []
    for path in sorted(glob.glob(os.path.join(d, "frame-*.json"))):
        reader = os.path.basename(path)[6:-5]
        data = json.load(io.open(path, encoding="utf-8"))
        for e in data.get("entries", []):
            k = entry_key(e)
            src = e.get("source") or []
            src = src if isinstance(src, list) else [src]
            if k in rows:
                r = rows[k]
                r["amends"] = sorted(set(r["amends"]) | set(e.get("amends") or []))
                r["readers"] = sorted(set(r["readers"]) | {reader})
                if KIND_RANK.get(e.get("kind", ""), 9) < KIND_RANK.get(r["kind"], 9): r["kind"] = e["kind"]
                r["sources"] = sorted(set(r["sources"]) | set(src))
                if (not r["passage_date"] or r["date_basis"] != "passed") and e.get("passage_date") and e.get("date_basis") == "passed":
                    r["passage_date"] = e["passage_date"]; r["date_basis"] = "passed"
                if e.get("note"): r["notes"].append(f"{reader}: {e['note']}")
            else:
                te = e.get("title_en", "") or ""
                notes = [f"{reader}: {e['note']}"] if e.get("note") else []
                if own_title_en(te) != te:
                    notes.append(f"build: title_en shortened from the reporting reader's phrasing '{te}' to the law's own title, because the suffix led coders to treat the row as the indirect amendment only")
                rows[k] = {"key": k, "title_he": e.get("title_he", ""), "title_en": own_title_en(te),
                           "passage_date": e.get("passage_date", "") or "", "date_basis": e.get("date_basis", ""),
                           "gazette": e.get("gazette", ""), "amends": sorted(set(e.get("amends") or [])),
                           "principal_subject": e.get("principal_subject", ""), "kind": e.get("kind", ""),
                           "sources": sorted(set(src)), "notes": notes, "readers": [reader]}
                order.append(k)
    return [rows[k] for k in order]

def match_challenge(c, rows):
    """Match on subject, then exact passage date (or year), then amendment number (both present and equal, or both absent)."""
    ctitle = c.get("enactment_title_he") or ""
    cs = subject_of(ctitle); cd = (c.get("passage_date") or "")[:10]; cy = year_of(cd); cn = amendment_no(ctitle)
    full_date = bool(re.match(r"\d{4}-\d{2}-\d{2}$", cd))
    cands = []
    for r in rows:
        if subject_of(r["title_he"]) != cs: continue
        rd = (r["passage_date"] or "")[:10]
        if full_date and rd != cd: continue
        if not full_date and year_of(rd) != cy: continue
        rn = amendment_no(r["title_he"])
        if cn and rn != cn: continue
        if not cn and rn: continue
        cands.append(r)
    return cands[0] if len(cands) == 1 else None

def main(d, out, draw=False):
    rows = load_frames(d)
    page_order = load_page_order(d)
    rows.sort(key=lambda r: sort_key(r, page_order))
    for r in rows:
        r["subject"] = subject_of(r["title_he"]) or r["principal_subject"]
        r["challenged"] = "No"; r["challenge_case"] = ""; r["challenge_outcome"] = ""
    cpath = os.path.join(d, "challenges.json")
    chal = json.load(io.open(cpath, encoding="utf-8")) if os.path.exists(cpath) else {"challenged": []}
    unmatched = []
    for c in chal.get("challenged", []):
        r = match_challenge(c, rows)
        if r:
            r["challenged"] = "Yes"
            r["challenge_case"] = "; ".join(x for x in [r["challenge_case"], c.get("case", "")] if x)
            r["challenge_outcome"] = "; ".join(x for x in [r["challenge_outcome"], f"{c.get('outcome_class','')} ({c.get('judgment_date','')})"] if x)
        else:
            unmatched.append(c.get("enactment_title_he") or c.get("enactment_title_en"))
    if draw:
        pos = 0
        for r in rows:
            r["sampled"] = ""
            if r["challenged"] == "No":
                r["sampled"] = "Yes" if pos % 3 == 0 else "No"; pos += 1
    cols = ["seq", "passage_date", "date_basis", "title_he", "title_en", "kind", "subject", "principal_subject", "amends", "gazette",
            "challenged", "challenge_case", "challenge_outcome"] + (["sampled"] if draw else []) + ["readers", "sources", "notes"]
    with io.open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
        for i, r in enumerate(rows, 1):
            row = {"seq": i, "passage_date": r["passage_date"], "date_basis": r["date_basis"], "title_he": r["title_he"], "title_en": r["title_en"],
                   "kind": r["kind"], "subject": r["subject"], "principal_subject": r["principal_subject"], "amends": " | ".join(r["amends"]),
                   "gazette": r["gazette"], "challenged": r["challenged"], "challenge_case": r["challenge_case"], "challenge_outcome": r["challenge_outcome"],
                   "readers": "+".join(r["readers"]), "sources": " | ".join(r["sources"]), "notes": " || ".join(r["notes"])}
            if draw: row["sampled"] = r.get("sampled", "")
            w.writerow(row)
    by_subject = {}
    for r in rows: by_subject[r["subject"]] = by_subject.get(r["subject"], 0) + 1
    summary = {"rows": len(rows), "entries_read": sum(len(r["readers"]) for r in rows),
               "challenged": sum(1 for r in rows if r["challenged"] == "Yes"),
               "unchallenged": sum(1 for r in rows if r["challenged"] == "No"),
               "merged_from_more_than_one_reader": sum(1 for r in rows if len(r["readers"]) > 1),
               "published_or_year_only_dates": sum(1 for r in rows if r["date_basis"] != "passed"),
               "rows_through_january_2023": sum(1 for r in rows if (r["passage_date"] or "9999") <= "2023-01-31"),
               "by_subject": by_subject, "unmatched_challenges": unmatched}
    if draw: summary["sampled"] = sum(1 for r in rows if r.get("sampled") == "Yes")
    print(json.dumps(summary, indent=1, ensure_ascii=False))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], draw=("--draw" in sys.argv))
