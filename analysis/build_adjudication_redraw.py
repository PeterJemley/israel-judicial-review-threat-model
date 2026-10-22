#!/usr/bin/env python3
"""Build the adjudication sheet for the redrawn comparison sample (change log (al)).

Usage: python3 build_adjudication_redraw.py CODING_DIR OUT_MD
Part 1 lists every cell on which the two coders disagree, for the rows coded in batches 4 to 6 and for
the one batch 2 row kept in the redraw. Part 2 puts interpretive questions on situated_beneficiary.
Earlier rulings (batches 1 and 3 of the first draw) are given as precedent, each named by its law's
title, since the first draw's sequence numbers refer to the frame as built.
"""
import sys, os, io, json, glob, re

VARS = ["named_beneficiary", "immediate_effect", "coalition_only", "expedited", "scope",
        "temporary_provision", "targets_judiciary", "deviation_tier", "direction"]

def load(p): return json.load(io.open(p, encoding="utf-8"))

def defs(d):
    s = io.open(os.path.join(d, "coding-sheet-redraw.md"), encoding="utf-8").read()
    out = [l for l in s.splitlines() if re.match(r"- `(%s)`:" % "|".join(VARS), l)]
    c = io.open(os.path.join(d, "circumstances-sheet-redraw.md"), encoding="utf-8").read()
    var = c[c.index("## The variable"):c.index("## Rules of the sheet")].replace("## The variable", "").strip()
    return out, var

def cell(c):
    c = c or {}
    t = f"value '{c.get('value', '')}'. Source: {c.get('source', '')}. Support: {c.get('support', '')}."
    if c.get("note"): t += f" Note: {c['note']}"
    return t

def main(d, out):
    first = {m["seq"]: m for m in load(os.path.join(d, "rows.json"))}
    redraw = load(os.path.join(d, "rows-redraw.json"))
    by_coded = {(m["batch"], m["coded_seq"]): m for m in redraw}
    defs_list, situated = defs(d)
    lines = ["# Adjudication sheet, comparison sample redraw (batches 4 to 6 and one kept row), with interpretive questions, 2026-10-22", ""]
    lines.append("You are the adjudicator. Two coders coded the enactments below independently from legislative records; they disagreed on the cells in Part 1. A single circumstances reader coded `situated_beneficiary`; Part 2 puts questions on its codings that rest on a reading of the closed list. Settle each item from the permitted sources (the enactment's text as published, Knesset voting data or press reports of the tally, records of the government's composition, reading dates from Knesset records or press, explanatory notes where reachable; for Part 2 also dated filings and press dated on or before passage) and under the prohibitions: no court judgment, no summary of one, no page whose subject is litigation about an enactment, no commentary on how a court treated it, no file in the repository other than this sheet, and no recollection of how an enactment fared. Where the coders differ because one found a record and the other did not, verify it and adopt the value it supports. Where they differ in judgment under a definition, apply the definition's words and its precedence rules, say which reading you adopt and why, and decide like cases alike: several rows here are the same kind of enactment (budget temporary provisions of 2009, 2015 and 2020), and your rulings on them should agree with each other and with the earlier rulings below unless their texts differ in a way the definition makes relevant. A blank is the right answer where no permitted source settles a cell. Sequence numbers are those of the corrected frame. Work in a fresh subfolder of your scratch directory and do not list or open other folders there. Do not write or modify any file; return your result in your final message only.")
    situated = re.sub(r"\s+", " ", situated).strip()
    if not situated.startswith("`situated_beneficiary`"): situated = "`situated_beneficiary`: " + situated
    lines += ["", "## Definitions", ""] + defs_list + ["- " + situated, ""]
    lines += ["## Earlier rulings on the same definitions, for consistency", "",
              "Two adjudicators settled disagreements in the first draw of this sample earlier today. Their rulings are below, each named by the law's title. They are not binding where the definition's words point otherwise, but a departure from them should be explained.", ""]
    for p in sorted(glob.glob(os.path.join(d, "adjudications-b[13]*.json"))):
        data = load(p)
        for a in data.get("adjudications", []):
            m = first.get(str(a["enactment"]), {})
            lines.append(f"- {m.get('title_en', '?')} ({m.get('passage_date', '')[:4]}), `{a['variable']}`: {a['value']}. {a.get('reason', '')}")
        for a in data.get("interpretive_rulings", []):
            m = first.get(str(a["enactment"]), {})
            lines.append(f"- {m.get('title_en', '?')} ({m.get('passage_date', '')[:4]}), `situated_beneficiary`: {a['value']}. Reading adopted: {a.get('reading_adopted', '')} {a.get('reason', '')}")
    lines += ["", "## Part 1: coder disagreements", ""]
    n = 0; index = []
    for b in (2, 4, 5, 6):
        pa, pb = os.path.join(d, f"coder-A-b{b}.json"), os.path.join(d, f"coder-B-b{b}.json")
        if not (os.path.exists(pa) and os.path.exists(pb)): continue
        A, B = load(pa), load(pb)
        for k in [x for x in A if x.isdigit()]:
            m = by_coded.get((b, k))
            if m is None: continue
            for v in VARS:
                va, vb = (A[k].get(v) or {}).get("value", ""), (B.get(k, {}).get(v) or {}).get("value", "")
                if va == vb: continue
                n += 1; index.append({"item": n, "seq": m["seq"], "batch": b, "coded_seq": k, "variable": v})
                where = f"batch {b}" + (f", coded under the first draw's number {k}" if k != m["seq"] else "")
                lines.append(f"### {n}. seq {m['seq']} ({where}): {m['title_he']} ({m['title_en']}; passed {m['passage_date']}), `{v}`")
                lines.append(f"- Coder A: {cell(A[k].get(v))}")
                lines.append(f"- Coder B: {cell(B[k].get(v))}")
                lines.append("")
    lines += ["## Part 2: interpretive questions on `situated_beneficiary`", ""]
    C = {}
    for p in glob.glob(os.path.join(d, "circumstances-b[456].json")):
        for k, v in load(p).items():
            if k.isdigit(): C[k] = v["situated_beneficiary"]
    def circ(seq):
        c = C.get(seq, {})
        return f"Circumstances reader's coding: {c.get('value', '')}. Admissible fact relied on: {c.get('admissible_fact', '')} Note: {c.get('note', '')}"
    title = {m["seq"]: m for m in redraw}
    qs = [
        ("Q1", ["28"], "Does item 4 cover a transitional clause that applies a new rule to the government in office but exempts that government alone, for its own term, from one limit the rule sets (here a cap on a ministerial committee's size), so that successor governments are bound and it is not?"),
        ("Q2", ["99"], "Does item 1 reach a repeal of a general rule enacted while a court proceeding was pending on whether that rule had operated in a particular case, where the repeal is prospective, names no party, and the record links the two only through the committee chair's stated wish that the court 'understand the direction'?"),
        ("Q3", ["85", "95", "111", "114", "118"], "These five budget temporary provisions were coded Yes under item 3 (a deadline binding the sitting government moved) or item 4 (a single-instance clause for the sitting government's own budget or spending year). A government formed later in the same budget period would operate under the same provisions. Does that partial sharing defeat 'unshared by successors', and is a provision confined to a budget year or to a named budget the sitting government's 'own measure' within item 4? Rule on each of the five, and decide them alike unless their texts differ in a way the definition makes relevant."),
    ]
    for q, seqs, text in qs:
        names = "; ".join(f"seq {s}: {title[s]['title_he']} ({title[s]['title_en']}; passed {title[s]['passage_date']})" for s in seqs)
        lines.append(f"### {q}. {names}")
        lines.append(f"- Question: {text}")
        for s in seqs: lines.append(f"- seq {s}. {circ(s)}")
        lines.append("")
    lines += ["## Output", "",
              "Return exactly one JSON object with a key \"adjudications\" holding a list with one object per Part 1 item, in order: {\"item\": <item number>, \"enactment\": <seq as a number>, \"variable\", \"value\", \"source\", \"support\" (a quotation of at most 25 words or a data point), \"reason\" (two to four sentences)}; a key \"interpretive_rulings\" holding a list with one object per enactment named in Part 2: {\"question\", \"enactment\", \"variable\": \"situated_beneficiary\", \"value\", \"reading_adopted\" (one sentence stating how the item is read), \"reason\" (two to four sentences)}; and a key \"deviations\". No prose outside the JSON."]
    io.open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    io.open(os.path.splitext(out)[0] + "-index.json", "w", encoding="utf-8").write(json.dumps(index, indent=1) + "\n")
    print(json.dumps({"items": n, "by_batch": {b: sum(1 for i in index if i["batch"] == b) for b in (2, 4, 5, 6)}}))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
