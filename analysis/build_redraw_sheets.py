#!/usr/bin/env python3
"""Build the manifest and the role sheets for the redrawn comparison sample (change log (al)).

Usage: python3 build_redraw_sheets.py REPO_ROOT
Reads research/frame/basic-law-frame.csv (the corrected frame with the redraw) and
research/coding-sample-2026-10-22/vote-extracts-redraw.json, and the first draw's sheets as templates.
Writes, in research/coding-sample-2026-10-22: rows-redraw.json (all 39 sampled rows, each with the batch
and the sequence number under which its coding is filed), coding-sheet-redraw.md, circumstances-sheet-redraw.md
and docket-sheet-redraw.md (batches 4 to 6); and research/frame/verification-sheet-redraw.md (the rows that
entered the sample). The rules and definitions are copied from the first draw's sheets unchanged.
"""
import sys, os, io, csv, json

BATCHES = {4: ["19", "22", "25", "28", "31", "35", "39", "42", "45", "48", "51"],
           5: ["54", "57", "61", "64", "67", "70", "73", "79", "82", "85", "89"],
           6: ["92", "95", "99", "103", "106", "111", "114", "118", "122", "127"]}
# Rows kept from the first draw: corrected-frame seq -> (batch, seq used in that batch's files).
KEPT = {"1": (1, "1"), "4": (1, "4"), "7": (1, "7"), "10": (1, "10"), "13": (1, "13"), "16": (1, "16"), "76": (2, "70")}
COVERAGE_START = "2003-10-20"

def links(r):
    src = [s.strip() for s in r["sources"].split(" | ") if s.strip()]
    wiki = next((s for s in src if "wikisource" in s), "")
    arch = next((s for s in src if "web.archive.org" in s and "_lsr_" in s), "")
    nevo = next((s for s in src if "nevo.co.il" in s), "")
    return wiki, arch, nevo

def date_phrase(r):
    if r["date_basis"] == "passed": return f"passed {r['passage_date']}"
    return f"passed by {r['passage_date']} (publication date; the passage date is days earlier)"

def vote_phrase(r, ex):
    if r["passage_date"] < COVERAGE_START:
        return ("outside the plenum-vote tables' coverage (20 October 2003 onward); find the recorded tally from the "
                "Knesset record or press reports of the vote, and say which.")
    e = ex.get(r["seq"], "")
    if not e or e.startswith("no plenum vote"):
        return ("no vote on a Basic Law bill on this subject appears in the Knesset's plenum-vote tables for this date; "
                "find the recorded tally from the Knesset record or press, and say which.")
    return ("candidate votes from the Knesset's plenum-vote tables as mirrored by Open Knesset (vote titles are bill "
            "titles, whose numbers can differ from the law's; establish which vote approved this law, and whether it "
            "approved any other law): " + e)

def line(r, batch, ex=None, with_vote=False):
    wiki, arch, nevo = links(r)
    amends = r["amends"] or "none, a new Basic Law"
    t = (f"- seq {r['seq']} (batch {batch}): {r['title_he']} — {r['title_en']}; {date_phrase(r)}; {r['gazette']}; "
         f"kind: {r['kind']}; amends: {amends}. Text: " + "; ".join(x for x in (wiki, arch, nevo) if x) + ".")
    if with_vote: t += " Vote record: " + vote_phrase(r, ex)
    return t

def split_sheet(path):
    s = io.open(path, encoding="utf-8").read()
    b = s.index("## Batches"); e = s.index("## Enactments"); o = s.index("## Output")
    return s[:b], s[o:]

BATCH_TEXT = ("## Batches\n\nThis sheet covers the rows that entered the comparison sample when it was drawn again from the "
              "corrected frame on 22 October 2026. Sequence numbers are the corrected frame's. "
              "Batch 4: seq 19 to 51. Batch 5: seq 54 to 89. Batch 6: seq 92 to 127. Code only the batch you were given.\n\n")

def main(root):
    fr = os.path.join(root, "research", "frame"); cs = os.path.join(root, "research", "coding-sample-2026-10-22")
    rows = {r["seq"]: r for r in csv.DictReader(io.open(os.path.join(fr, "basic-law-frame.csv"), encoding="utf-8"))}
    sampled = [s for s, r in rows.items() if r["sampled"] == "Yes"]
    ex = json.load(io.open(os.path.join(cs, "vote-extracts-redraw.json"), encoding="utf-8"))
    batch_of = {s: b for b, ss in BATCHES.items() for s in ss}
    assert set(batch_of) | set(KEPT) == set(sampled), sorted(set(sampled) ^ (set(batch_of) | set(KEPT)), key=int)
    manifest = []
    for s in sorted(sampled, key=int):
        r = rows[s]; wiki, arch, nevo = links(r)
        b, coded = KEPT.get(s, (batch_of.get(s), s))
        manifest.append({"seq": s, "batch": b, "coded_seq": coded, "first_draw_seq": r["first_draw_seq"],
                         "first_draw_sampled": r["first_draw_sampled"], "title_he": r["title_he"], "title_en": r["title_en"],
                         "passage_date": r["passage_date"], "date_basis": r["date_basis"], "gazette": r["gazette"],
                         "subject": r["subject"], "kind": r["kind"], "amends": r["amends"], "wikisource": wiki,
                         "archive": arch, "nevo": nevo, "vote_extract": ex.get(s, "") if b >= 4 else ""})
    io.open(os.path.join(cs, "rows-redraw.json"), "w", encoding="utf-8").write(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n")
    new = [(b, s) for b, ss in BATCHES.items() for s in ss]

    head, tail = split_sheet(os.path.join(cs, "coding-sheet.md"))
    head = head.replace("# Coding sheet for the comparison sample, 2026-10-22", "# Coding sheet for the comparison sample, redraw, 2026-10-22", 1)
    head = head.replace("## Variables", "- The Knesset's plenum-vote table (kns_plenumvote), its per-member results (kns_plenumvoteresult) and its member-position table (kns_persontoposition), mirrored by Open Knesset at production.oknesset.org/pipelines/data/knesset/ and .../members/, are Knesset voting data and may be read directly; they cover October 2003 onward.\n\n## Variables", 1)
    body = "## Enactments\n\n" + "\n".join(line(rows[s], b, ex, True) for b, s in new) + "\n\n"
    io.open(os.path.join(cs, "coding-sheet-redraw.md"), "w", encoding="utf-8").write(head + BATCH_TEXT + body + tail)

    head, tail = split_sheet(os.path.join(cs, "circumstances-sheet.md"))
    head = head.replace("# Circumstances sheet for the comparison sample, 2026-10-22", "# Circumstances sheet for the comparison sample, redraw, 2026-10-22", 1)
    head = head.replace("Press archives with dated articles are permitted for reports dated on or before passage.",
                        "Press archives with dated articles are permitted for reports dated on or before passage. Knesset committee protocols and bill records are mirrored by Open Knesset (production.oknesset.org/pipelines/data/). WIPO Lex holds consolidated Hebrew texts of several Basic Laws with notes on each amendment. Nevo's pages may now require a login.", 1)
    body = "## Enactments\n\n" + "\n".join(line(rows[s], b) for b, s in new) + "\n\n"
    io.open(os.path.join(cs, "circumstances-sheet-redraw.md"), "w", encoding="utf-8").write(head + BATCH_TEXT + body + tail)

    head, tail = split_sheet(os.path.join(cs, "docket-sheet.md"))
    head = head.replace("# Docket sheet for the comparison sample, 2026-10-22", "# Docket sheet for the comparison sample, redraw, 2026-10-22", 1)
    old_outcome = head[head.index("The outcome of every enactment on this sheet"):head.index("## Sources and rules")]
    head = head.replace(old_outcome, "These enactments are being verified separately as never having been attacked before the Court, and their outcome is attached after that verification. Do not search for challenges and do not record an outcome.\n\n", 1)
    tail = ("## Output\n\nReturn one JSON object with a key for each sequence number in your batch (as a string). Each value is an object "
            "with one key, `litigation_timing` (an object with \"value\", \"source\", \"support\", \"note\", the note naming any judgment "
            "the enactment responded to). Add a top-level \"deviations\" list: sources not reached, searches not completed, anything a "
            "reviewer should check.\n")
    body = "## Enactments\n\n" + "\n".join(line(rows[s], b) for b, s in new) + "\n\n"
    io.open(os.path.join(cs, "docket-sheet-redraw.md"), "w", encoding="utf-8").write(head + BATCH_TEXT + body + tail)

    v = io.open(os.path.join(fr, "verification-sheet.md"), encoding="utf-8").read()
    v = v.replace("# Verification sheet for the comparison sample, 2026-10-22", "# Verification sheet for the comparison sample, redraw, 2026-10-22", 1)
    v = v.replace("For each of the 36 enactments below", "For each of the enactments below assigned to you", 1)
    a, o = v.index("## The rows"), v.index("## Output")
    half = {s: ("A" if i < 16 else "B") for i, (b, s) in enumerate([(b, s) for b, s in new if s != "73"])}
    vlines = []
    for b, s in new:
        if s == "73": continue
        r = rows[s]
        vlines.append(f"- seq {s} (reader {half[s]}): {r['title_he']} — {r['title_en']}; passed {r['passage_date']} ({r['date_basis']}); "
                      f"{r['gazette']}; amends: {r['amends'] or 'none (enactment)'}; kind: {r['kind']}.")
    v = v[:a] + ("## The rows\n\nThese are the rows that entered the comparison sample when it was drawn again from the corrected frame. "
                 "Sequence numbers are the corrected frame's. Search only the rows marked with your reader letter.\n\n" + "\n".join(vlines) + "\n\n") + v[o:]
    io.open(os.path.join(fr, "verification-sheet-redraw.md"), "w", encoding="utf-8").write(v)
    print(json.dumps({"manifest_rows": len(manifest), "new_rows_to_code": len(new),
                      "verification_rows": len(vlines), "reader_A": [s for s in half if half[s] == "A"], "reader_B": [s for s in half if half[s] == "B"]}))

if __name__ == "__main__":
    main(sys.argv[1])
