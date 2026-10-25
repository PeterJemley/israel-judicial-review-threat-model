#!/usr/bin/env python3
"""Check that numbers stated in the repository's prose match the committed data (audit of 2026-10-25).

Usage: python3 analysis/check_numbers.py [--list]
Run from the repository's root. Each check recomputes one number from the data files (the frame,
the two codebooks, the coders' files, the assembly summaries, or t1_revised.py) and looks for the
sentence or table cell that states it, with the computed value written in. A check fails when that
text is not found, which means either the number has drifted from the data or the wording around it
has changed; either way the line wants a look. Prints one line per check, then a count, and exits
non-zero if any check fails. --list prints the checks without running them.

The checks cover numbers the data can reproduce. Numbers taken from outside sources (vote tallies,
dates, counts reported by a court) are traced in research/audit-2026-10-25.md, not here.
"""
import sys, os, csv, json, io, re
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "analysis"))
import t1_revised as t1

def path(p): return os.path.join(ROOT, p)
def rows(p): return list(csv.DictReader(io.open(path(p), encoding="utf-8")))
def load(p): return json.load(io.open(path(p), encoding="utf-8"))
def text(p): return io.open(path(p), encoding="utf-8").read()

WORDS = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split()
def word(n, cap=False):
    w = WORDS[n] if n < len(WORDS) else str(n)
    return w.capitalize() if cap else w

FRAME = rows("research/frame/basic-law-frame.csv")
AS_BUILT = rows("research/frame/basic-law-frame-as-built.csv")
SAMPLE = rows("codebook/comparison-sample.csv")
M4 = rows("codebook/m4-codebook.csv")
SAMPLE_SUM = load("research/coding-sample-2026-10-22/assembly-summary-redraw.json")

def yes(v): return v.strip().lower() in ("yes", "y", "true", "1")
challenged = [r for r in FRAME if yes(r["challenged"])]
sampled = [r for r in FRAME if yes(r["sampled"])]
first_draw = [r for r in FRAME if yes(r["first_draw_sampled"])]
through_2023 = [r for r in FRAME if (r["passage_date"] or "9999") <= "2023-01-31"]
def decade(d): return sum(1 for r in FRAME if r["passage_date"][:3] == d)
def subject(s): return sum(1 for r in FRAME if r["subject"] == s)
def sample_count(col, val): return sum(1 for r in SAMPLE if r[col] == val)
def kappa(var): return SAMPLE_SUM["agreement"][var]
primary = [r for r in M4 if r["primary_analysis"] == "Yes" and r["class"] != "uncoded"]
FIRST = [r for r in AS_BUILT if yes(r["sampled"])]
REDRAW = [r for r in FRAME if yes(r["sampled"])]
in_both = [r for r in REDRAW if yes(r["first_draw_sampled"])]
def by(rows, col, val): return sum(1 for r in rows if r[col] == val)
def decades(rows):
    """'two from the 1950s, ..., and five from the 2020s', the wording of research/frame/README.md."""
    parts = [f"{word(by_decade)} from the {d}0s" for d, by_decade in sorted(Counter(r["passage_date"][:3] for r in rows).items())]
    return ", ".join(parts[:-1]) + " and " + parts[-1]
def readers(r): return [x for x in r["readers"].split("+") if x]
def detect_first_run(): return t1.detect(len(primary), sum(1 for r in primary if r["outcome"] == "Adverse"),
    sum(1 for r in primary if r["class"] == "discordant" and r["decision_rule_prediction"] == "Adverse"),
    sum(1 for r in primary if r["class"] == "discordant" and r["decision_rule_prediction"] == "Not adverse"))

# (file, text with {} for the computed value, function giving the value or a tuple of values)
CHECKS = [
    # The frame
    ("README.md", "the Knesset passed {} Basic Laws or changes to them", lambda: len(FRAME)),
    ("README.md", "Basic Law: The Knesset ({}) and Basic Law: The Government ({})", lambda: (subject("Knesset"), subject("Government"))),
    ("README.md", "| 1950s | {} |", lambda: decade("195")),
    ("README.md", "| 1960s | {} |", lambda: decade("196")),
    ("README.md", "| 1970s | {} |", lambda: decade("197")),
    ("README.md", "| 1980s | {} |", lambda: decade("198")),
    ("README.md", "| 1990s | {} |", lambda: decade("199")),
    ("README.md", "| 2000s | {} |", lambda: decade("200")),
    ("README.md", "| 2010s | {} |", lambda: decade("201")),
    ("README.md", "| 2020s, to July 2026 | {} |", lambda: decade("202")),
    ("README.md", "{} of the {} have come before the Supreme Court", lambda: (word(len(challenged), True), len(FRAME))),
    ("research/frame/README.md", "| Rows (laws titled Basic Law, 12 February 1958 to 13 July 2026) | {} |", lambda: len(FRAME)),
    ("research/frame/README.md", "| Challenged rows | {} |", lambda: len(challenged)),
    ("research/frame/README.md", "| Unchallenged rows, the population for the draw | {} |", lambda: len(FRAME) - len(challenged)),
    ("research/frame/README.md", "| Laws through January 2023 | {} |", lambda: len(through_2023)),
    ("research/frame/README.md", "The corrected frame has {} laws through that date", lambda: len(through_2023)),
    ("research/frame/README.md", "| Reader entries merged into them | {} |", lambda: sum(len(readers(r)) for r in FRAME)),
    ("research/frame/README.md", "| Rows reported by more than one reader (indirect amendments) | {} |", lambda: sum(1 for r in FRAME if len(readers(r)) > 1)),
    ("research/frame/README.md", "| Rows whose date is a publication date, not a passage date | {} |", lambda: sum(1 for r in FRAME if r["date_basis"] != "passed")),
    ("research/frame/README.md", "The frame as built gave {} laws", lambda: sum(1 for r in AS_BUILT if (r["passage_date"] or "9999") <= "2023-01-31")),
    ("research/frame/README.md", "{} rows. Seven were in the codebook already", lambda: word(len(challenged), True)),
    ("research/frame/README.md", "- {} rows carry the gazette publication date", lambda: word(sum(1 for r in FRAME if r["date_basis"] != "passed"), True)),
    ("research/frame/README.md", "- {} ordinary statutes that touched Basic Laws", lambda: word(sum(len(load(f"research/frame/frame-{n}.json")["ordinary_statute_amendments"]) for n in ("knesset", "government", "economy-judiciary-rights")), True)),
    ("research/frame/README.md", "two docket readers, {} rows each", lambda: "eighteen" if all(len(load(f"research/frame/verification-{x}.json")["rows"]) == 18 for x in "ab") else "unequal"),
    ("research/frame/README.md", "{} pairs were settled by printed evidence, {} by amendment numbers and {} by bill order", lambda: tuple(word(sum(1 for p in load("research/frame/same-page-order.json")["pages"] if p["basis"].startswith(b)), b == "printed") for b in ("printed", "amendment", "bill"))),
    ("codebook/README.md", "It holds {} rows", lambda: word(len(M4))),
    ("codebook/README.md", "An adjudicator settled their {} disagreements", lambda: word(len(load("research/coding-2026-10-22/adjudications.json")["adjudications"]))),
    # The two draws
    ("research/frame/README.md", "It gives {} rows. By subject: Knesset {}, Government {}, State Economy {}, Freedom of Occupation {}, President {}", lambda: (len(FIRST),) + tuple(by(FIRST, "subject", s) for s in ("Knesset", "Government", "State Economy", "Freedom of Occupation", "President"))),
    ("research/frame/README.md", "By kind: {} amendments, {} temporary provisions, {} enactments, {} re-enactment.", lambda: tuple(by(FIRST, "kind", k) for k in ("amendment", "temporary provision", "enactment", "re-enactment"))),
    ("research/frame/README.md", "By decade: {}. Two of the 36", lambda: decades(FIRST)),
    ("research/frame/README.md", "{} of the {} carry a publication date rather than a passage date. The draw is deterministic", lambda: (word(sum(1 for r in FIRST if r["date_basis"] != "passed"), True), len(FIRST))),
    ("research/frame/README.md", "It gives {} rows. By subject: Knesset {}, Government {}, Jerusalem {}, President {}, State Economy {}, Judiciary {}, the budget temporary Basic Laws {}", lambda: (len(REDRAW),) + tuple(by(REDRAW, "subject", s) for s in ("Knesset", "Government", "Jerusalem", "President", "State Economy", "Judiciary", "State Budget (temporary Basic Law)"))),
    ("research/frame/README.md", "By kind: {} amendments, {} enactments, {} temporary provisions.", lambda: tuple(by(REDRAW, "kind", k) for k in ("amendment", "enactment", "temporary provision"))),
    ("research/frame/README.md", "By decade: {}. Two of the 39", lambda: decades(REDRAW)),
    ("research/frame/README.md", "{} of the {} carry a publication date rather than a passage date.\n", lambda: (word(sum(1 for r in REDRAW if r["date_basis"] != "passed"), True), len(REDRAW))),
    ("research/frame/README.md", "| In both draws | {} |", lambda: len(in_both)),
    ("research/frame/README.md", "| In the first draw only, now out of the sample | {} |", lambda: len(FIRST) - len(in_both)),
    ("research/frame/README.md", "| In the redraw only | {} |", lambda: len(REDRAW) - len(in_both)),
    ("medina-threat-conjecture-note.md", "The corrected frame has {} rows, {} challenged and {} unchallenged.", lambda: (len(FRAME), len(challenged), len(FRAME) - len(challenged))),
    ("medina-threat-conjecture-note.md", "The redraw under (ah) gives {} rows. {} rows are in both draws", lambda: (len(REDRAW), word(len(in_both), True))),
    ("medina-threat-conjecture-note.md", "Twenty-eight rows of the first draw leave the sample and {} rows enter it.", lambda: len(REDRAW) - len(in_both)),
    # The comparison sample
    ("README.md", "**The {} unchallenged laws.**", lambda: len(SAMPLE)),
    ("README.md", "{} did not move away from the democratic values, or made them stronger", lambda: sample_count("deviation_tier", "None") + sample_count("deviation_tier", "Entrenches")),
    ("README.md", "{} moved away from them a little, and none moved away a lot", lambda: sample_count("deviation_tier", "Limited")),
    ("README.md", "only {} helped the government that was in office at the time", lambda: sample_count("situated_beneficiary", "Yes")),
    ("README.md", "For {} of the {} laws, the surviving records do not show how each member voted", lambda: (sample_count("coalition_only", ""), len(SAMPLE))),
    ("research/coding-sample-2026-10-22/README.md", "All {} rows were coded", lambda: SAMPLE_SUM["rows_coded"]),
    ("research/coding-sample-2026-10-22/README.md", "| situated_beneficiary | Yes {}, No {} |", lambda: (sample_count("situated_beneficiary", "Yes"), sample_count("situated_beneficiary", "No"))),
    ("research/coding-sample-2026-10-22/README.md", "| named_beneficiary | Yes {}, No {} |", lambda: (sample_count("named_beneficiary", "Yes"), sample_count("named_beneficiary", "No"))),
    ("research/coding-sample-2026-10-22/README.md", "| immediate_effect | Yes {}, Deferred {} |", lambda: (sample_count("immediate_effect", "Yes"), sample_count("immediate_effect", "Deferred"))),
    ("research/coding-sample-2026-10-22/README.md", "| coalition_only | Yes {}, No {}, blank {} |", lambda: (sample_count("coalition_only", "Yes"), sample_count("coalition_only", "No"), sample_count("coalition_only", ""))),
    ("research/coding-sample-2026-10-22/README.md", "| expedited | Yes {}, No {}, blank {} |", lambda: (sample_count("expedited", "Yes"), sample_count("expedited", "No"), sample_count("expedited", ""))),
    ("research/coding-sample-2026-10-22/README.md", "| deviation_tier | None {}, Entrenches {}, Limited {}, Sharp {} |", lambda: tuple(sample_count("deviation_tier", v) for v in ("None", "Entrenches", "Limited", "Sharp"))),
    ("research/coding-sample-2026-10-22/README.md", "| direction | Neutral {}, Liberal {}, Illiberal {} |", lambda: tuple(sample_count("direction", v) for v in ("Neutral", "Liberal", "Illiberal"))),
    ("research/coding-sample-2026-10-22/README.md", "| litigation_timing | Yes {}, No {} |", lambda: (sample_count("litigation_timing", "Yes"), sample_count("litigation_timing", "No"))),
    ("research/coding-sample-2026-10-22/README.md", "it is computable on {} rows: F = 1 on {} row, F = 2 on {} and F = 3 on {}", lambda: (sum(1 for r in SAMPLE if r["F"] != ""), word(sample_count("F", "1")), word(sample_count("F", "2")), word(sample_count("F", "3")))),
    ("research/coding-sample-2026-10-22/README.md", "On {} of those rows the decision rule predicts Adverse", lambda: word(sum(1 for r in SAMPLE if r["class"] == "discordant" and r["decision_rule_prediction"] == "Adverse"))),
    ("medina-threat-conjecture-note.md", "coalition_only is blank on {} rows because no surviving record names the voters, so F is computable on {} rows", lambda: (sample_count("coalition_only", ""), sum(1 for r in SAMPLE if r["F"] != ""))),
    ("medina-threat-conjecture-note.md", "the coders agreed on {} to {} of the {} rows for each variable", lambda: (min(a["agree"] for a in SAMPLE_SUM["agreement"].values()), max(a["agree"] for a in SAMPLE_SUM["agreement"].values()), len(SAMPLE))),
    ("medina-threat-conjecture-note.md", "The adjudicator settled {} disagreements", lambda: word(len(load("research/coding-sample-2026-10-22/adjudications-redraw-all.json")["adjudications"]))),
]
for var in ["named_beneficiary", "immediate_effect", "coalition_only", "expedited", "scope", "temporary_provision", "targets_judiciary", "deviation_tier", "direction"]:
    CHECKS.append(("research/coding-sample-2026-10-22/README.md", "| " + var + " | {} | {} |", lambda var=var: (kappa(var)["agree"], f"{kappa(var)['kappa']:.2f}")))
CHECKS += [
    # T1 on the nine rows
    ("README.md", "Only {} of the nine laws did, and the test needs at least six", lambda: word(sum(1 for r in M4 if r["class"] == "discordant"))),
    ("README.md", "python3 analysis/t1_revised.py detect {} {} {} {}", lambda: tuple(detect_first_run()[k] for k in ("N", "K", "D_A", "D_N"))),
    ("README.md", "The check prints \"{}\"", lambda: detect_first_run()["verdict_before_outcomes"]),
    ("research/coding-2026-10-22/results.md", "K rises from 4 to {} of {}", lambda: (detect_first_run()["K"], detect_first_run()["N"])),
    ("research/coding-2026-10-22/results.md", "the attainable range of S is {} to {}, p is {} at both extremes", lambda: (detect_first_run()["S_min_attainable"], detect_first_run()["S_max_attainable"], detect_first_run()["p_at_S_max"])),
    ("medina-threat-conjecture-note.md", "Inconclusive, declared before outcomes, on {} discordant row against the minimum of six", lambda: word(detect_first_run()["discordant"])),
]

def run():
    failed = 0
    cache = {}
    for f, template, fn in CHECKS:
        v = fn()
        phrase = template.format(*(v if isinstance(v, tuple) else (v,)))
        body = cache.setdefault(f, text(f))
        ok = phrase in body
        failed += not ok
        print(("ok    " if ok else "FAIL  ") + f + ": " + phrase)
    print(f"{len(CHECKS) - failed} of {len(CHECKS)} checks pass")
    return failed

if __name__ == "__main__":
    if "--list" in sys.argv:
        for f, template, _ in CHECKS: print(f + ": " + template)
    else:
        sys.exit(1 if run() else 0)
