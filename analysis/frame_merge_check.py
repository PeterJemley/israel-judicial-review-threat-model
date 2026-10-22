#!/usr/bin/env python3
"""Find frame rows that merge two distinct laws (defect found 22 October 2026).

build_frame.py merges reader entries that share a Sefer HaHukkim issue and page. Two separately
titled laws printed on the same page then collapse into one row. This check groups the readers'
entries by that key and reports every group whose entries name different laws, judged by the
subject and amendment number in the Hebrew title and by the Knesset law-PDF id in the sources.

Usage: python3 frame_merge_check.py FRAME_DIR FRAME_CSV OUT_JSON
"""
import sys, json, csv, io, os, re, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_frame import gazette_key, subject_of, amendment_no

PDF = re.compile(r"(\d+_lsr_\d+)\.pdf")

def law_id(e):
    return (subject_of(e.get("title_he")), amendment_no(e.get("title_he")))

def main(d, frame_csv, out):
    groups = {}
    for path in sorted(glob.glob(os.path.join(d, "frame-*.json"))):
        reader = os.path.basename(path)[6:-5]
        for e in json.load(io.open(path, encoding="utf-8")).get("entries", []):
            k = gazette_key(e.get("gazette"))
            if not k: continue
            pdfs = sorted({m for s in (e.get("source") or []) for m in PDF.findall(s)})
            groups.setdefault(k, []).append({"reader": reader, "title_he": e.get("title_he"), "title_en": e.get("title_en"),
                                             "passage_date": e.get("passage_date"), "gazette": e.get("gazette"),
                                             "law": law_id(e), "pdfs": pdfs})
    rows = list(csv.DictReader(io.open(frame_csv, encoding="utf-8")))
    by_key = {}
    for r in rows:
        k = gazette_key(r["gazette"])
        if k: by_key.setdefault(k, []).append(r)
    found = []
    for k, es in sorted(groups.items()):
        laws = {}
        for e in es:
            laws.setdefault(e["law"], []).append(e)
        if len(laws) < 2: continue
        frame_rows = by_key.get(k, [])
        found.append({
            "gazette_key": list(k),
            "frame_rows": [{"seq": int(r["seq"]), "title_en": r["title_en"], "passage_date": r["passage_date"],
                            "challenged": r["challenged"], "sampled": r["sampled"]} for r in frame_rows],
            "distinct_laws": [{"subject": law[0], "amendment_no": law[1],
                               "titles_he": sorted({e["title_he"] for e in v}),
                               "titles_en": sorted({e["title_en"] for e in v if e["title_en"]}),
                               "passage_dates": sorted({e["passage_date"] for e in v if e["passage_date"]}),
                               "law_pdfs": sorted({p for e in v for p in e["pdfs"]}),
                               "readers": sorted({e["reader"] for e in v})} for law, v in sorted(laws.items())]})
    missing = sum(len(g["distinct_laws"]) - len(g["frame_rows"]) for g in found)
    summary = {"rows_in_frame": len(rows), "merged_groups": len(found), "laws_missing_from_frame": missing,
               "rows_in_corrected_frame": len(rows) + missing,
               "sampled_rows_affected": [fr["seq"] for g in found for fr in g["frame_rows"] if fr["sampled"] == "Yes"],
               "challenged_rows_affected": [fr["seq"] for g in found for fr in g["frame_rows"] if fr["challenged"] == "Yes"],
               "groups": found}
    io.open(out, "w", encoding="utf-8").write(json.dumps(summary, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps({k: v for k, v in summary.items() if k != "groups"}, ensure_ascii=False))
    for g in found:
        print(g["gazette_key"], [fr["seq"] for fr in g["frame_rows"]], "|",
              " + ".join(f'{l["subject"]} {l["amendment_no"] or "(enactment)"} {l["passage_dates"]} {l["law_pdfs"]}' for l in g["distinct_laws"]))

if __name__ == "__main__":
    main(*sys.argv[1:4])
