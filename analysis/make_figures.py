#!/usr/bin/env python3
"""Draw the project's figures as static SVG, in light and dark versions, with a table for each.

Usage: python3 analysis/make_figures.py
Run from the repository's root. Reads the frame, the codebook, the comparison sample and T1's rule
(analysis/t1_revised.py) for the measured figures, and the curated files in figures/sources/
(ledger.csv, errors.csv, jigsaw.json) for the ledger, the errors list and the imagined jigsaw.
Writes figures/<name>-light.svg and figures/<name>-dark.svg, figures/data/<name>.csv, and
figures/README.md, which carries each figure's caption, alt text and table. Counts and statistics
drawn from the data are computed here from those files. The ledger, the errors list and the jigsaw
are curated by hand in figures/sources/, each row citing its basis. A few fixed values are set here,
each saying where it comes from: the ten laws of figure 4, the first run's configuration, and the
scope dates.
"""
import sys, os, io, csv, json, re
from collections import Counter, defaultdict
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "analysis"))
import t1_revised as t1

def path(*p): return os.path.join(ROOT, *p)
def rows(p): return list(csv.DictReader(io.open(path(p), encoding="utf-8")))
def yes(v): return v.strip().lower() in ("yes", "y", "true", "1")

# Colours: measured figures use three validated categorical slots and neutrals; the imagined
# figure alone uses violet. Values from the reference palette, validated all-pairs in both modes.
THEMES = {
    "light": dict(surface="#fcfcfb", ink="#0b0b0b", ink2="#52514e", muted="#898781", grid="#e1e0d9",
                  axis="#c3c2b7", blue="#2a78d6", orange="#eb6834", aqua="#1baf7a", none="#d8d7d0",
                  noneink="#0b0b0b", violet="#6250d6", wash="0.14", onfill="#ffffff"),
    "dark": dict(surface="#1a1a19", ink="#f0efec", ink2="#c3c2b7", muted="#898781", grid="#2c2c2a",
                 axis="#383835", blue="#3987e5", orange="#d95926", aqua="#199e70", none="#4a4a46",
                 noneink="#f0efec", violet="#9085e9", wash="0.22", onfill="#ffffff"),
}
FONT = "system-ui, -apple-system, 'Segoe UI', sans-serif"
WORDS = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen".split()

def esc(s): return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def wrap(text, chars):
    out, line = [], ""
    for w in str(text).split():
        if line and len(line) + 1 + len(w) > chars: out.append(line); line = w
        else: line = (line + " " + w).strip()
    if line: out.append(line)
    return out

def txt(x, y, s, size=12, fill="ink", weight="normal", anchor="start", th=None, italic=False):
    st = ' font-style="italic"' if italic else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
            f'fill="{th[fill] if fill in th else fill}"{st}>{esc(s)}</text>')

def lines(x, y, ls, size, lh, th, fill="ink", weight="normal", anchor="start"):
    return "".join(txt(x, y + i * lh, l, size, fill, weight, anchor, th) for i, l in enumerate(ls))

def doc(w, h, title, desc, body, th):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
            f'aria-labelledby="t d" font-family="{FONT}">\n<title id="t">{esc(title)}</title>\n<desc id="d">{esc(desc)}</desc>\n'
            f'<rect width="{w}" height="{h}" fill="{th["surface"]}"/>\n{body}\n</svg>\n')

CHIPS = {"measured": "MEASURED", "calculation": "CALCULATION", "record": "FROM THE RECORD", "imagined": "IMAGINED. NOT A RESULT."}

def header(th, w, title, subtitle, kind="measured"):
    """Title block with a chip saying what kind of figure it is: measured, a calculation, from the record, or imagined."""
    chip = CHIPS[kind]; imagined = kind == "imagined"
    cw = 8 + len(chip) * 7.2
    col = th["violet"] if imagined else th["ink2"]
    b = (f'<rect x="24" y="18" width="{cw:.0f}" height="20" rx="10" fill="none" stroke="{col}" stroke-width="1.5"/>'
         + txt(24 + cw / 2, 32, chip, 11, col, "bold", "middle", th))
    tw, sw = int((w - 48) / 10.6), int((w - 48) / 7.2)
    b += lines(24, 64, wrap(title, tw), 19, 24, th, "ink", "600")
    n = len(wrap(title, tw))
    b += lines(24, 64 + n * 24 + 2, wrap(subtitle, sw), 13, 18, th, "ink2")
    return b, 64 + n * 24 + 2 + len(wrap(subtitle, sw)) * 18

def footer(th, y, notes, w):
    b, yy = "", y
    for n in notes:
        ls = wrap(n, int((w - 48) / 6.4))
        b += lines(24, yy, ls, 11, 15, th, "ink2"); yy += len(ls) * 15 + 4
    return b, yy

def write_svg(name, w, hfun):
    for mode, th in THEMES.items():
        h, title, desc, body = hfun(th)
        io.open(path("figures", f"{name}-{mode}.svg"), "w", encoding="utf-8").write(doc(w, h, title, desc, body, th))

def write_csv(name, header_row, data):
    os.makedirs(path("figures", "data"), exist_ok=True)
    with io.open(path("figures", "data", f"{name}.csv"), "w", encoding="utf-8", newline="") as f:
        wr = csv.writer(f); wr.writerow(header_row); wr.writerows(data)

def md_table(header_row, data):
    s = "| " + " | ".join(header_row) + " |\n|" + "---|" * len(header_row) + "\n"
    return s + "".join("| " + " | ".join(str(c).replace("|", "/") for c in r) + " |\n" for r in data)

FRAME = rows("research/frame/basic-law-frame.csv")
SAMPLE = rows("codebook/comparison-sample.csv")
M4 = rows("codebook/m4-codebook.csv")
SCOPE_FRAME = ("Scope: Israel; laws titled Basic Law as passed at third reading, 12 February 1958 to 13 July 2026. "
               "Dates are passage dates from the gazette footnotes, except five publication dates. Entries from December 2025 to October 2026 could not be checked against the Knesset's own database. "
               "Source: research/frame/basic-law-frame.csv (gazette texts through Internet Archive captures, Hebrew Wikisource, Nevo); "
               "challenges from the Court's own surveys in HCJ 5658/23 and HCJ 4908/10 and from searches, classed provisionally by the challenge reader.")
# The codebook's Basic Law rows, by their row in the frame (the two 1969 statutes are not Basic Laws).
M4_FRAME = {"1": "34", "4": "37", "5": "100", "6": "115", "7": "108", "8": "123", "9": "125"}
STEP4 = {M4_FRAME[r["id"]]: r["outcome"] for r in M4 if r["id"] in M4_FRAME}
SHORT = {"34": "Human Dignity and Liberty", "37": "Freedom of Occupation (re-enactment)",
         "60": "The Government (Amendment No. 9)", "86": "State Budget for 2009 and 2010 (Amendment)",
         "98": "The Knesset (Amendment No. 44)", "100": "State Budget for 2017 and 2018",
         "108": "Nation State of the Jewish People", "110": "The Government (Amendment No. 8)",
         "115": "The Knesset (Amendment No. 50)", "121": "The Government (Amendment No. 11)",
         "123": "The Government (Amendment No. 12)", "125": "The Judiciary (Amendment No. 3)",
         "128": "The Judiciary (Amendment No. 4)", "130": "Torah Study"}
README = []

# ---------------------------------------------------------------- 1. Basic Laws by year
def fig1():
    years = list(range(1958, 2027))
    ch = Counter(r["passage_date"][:4] for r in FRAME if yes(r["challenged"]))
    un = Counter(r["passage_date"][:4] for r in FRAME if not yes(r["challenged"]))
    data = [[y, un[str(y)], ch[str(y)], un[str(y)] + ch[str(y)]] for y in years]
    write_csv("fig1-basic-laws-by-year", ["year", "not_challenged", "challenged", "total"], data)
    peak = max(data, key=lambda d: d[3])
    n_ch, n_all = sum(ch.values()), len(FRAME)
    title = f"Laws titled Basic Law passed each year, 1958 to 2026: {n_all} laws, {n_ch} of which later came before the Supreme Court"
    sub = "Each column is one year. Orange marks the laws that were later challenged before the Supreme Court or whose binding force it decided."
    desc = (f"Column chart of the {n_all} laws titled Basic Law passed each year from 1958 to 2026. Most years before 1990 have none to two; "
            f"the busiest year is {peak[0]} with {peak[3]}. {n_ch} later came before the Court, challenged or ruled on as to their binding force; the first passed in 1992 and the last in 2026.")
    def draw(th):
        w = 960; b, y0 = header(th, w, title, sub)
        top, x0, pw, ph = y0 + 40, 60, 870, 230
        ymax = 14; sx = pw / len(years); bw = min(8.0, sx - 3)
        def Y(v): return top + ph - v / ymax * ph
        for tk in (0, 5, 10):
            b += f'<line x1="{x0}" x2="{x0+pw}" y1="{Y(tk):.1f}" y2="{Y(tk):.1f}" stroke="{th["grid" if tk else "axis"]}" stroke-width="1"/>'
            b += txt(x0 - 8, Y(tk) + 4, tk, 11, "muted", anchor="end", th=th)
        for i, (yr, u, c, tot) in enumerate(data):
            cx = x0 + i * sx + sx / 2
            if u:
                h = u / ymax * ph
                r = 3 if not c else 0
                b += f'<path d="{bar_path(cx - bw/2, Y(0), bw, h, r)}" fill="{th["blue"]}"><title>{yr}: {u} did not come before the Court</title></path>'
            if c:
                h = c / ymax * ph; base = Y(u) - (2 if u else 0)
                b += f'<path d="{bar_path(cx - bw/2, base, bw, h, 3)}" fill="{th["orange"]}"><title>{yr}: {c} came before the Court</title></path>'
            if yr % 10 == 0: b += txt(cx, top + ph + 16, yr, 11, "muted", anchor="middle", th=th)
        pi = years.index(peak[0]); px = x0 + pi * sx + sx / 2
        b += txt(px, Y(peak[3]) - 6, f"{peak[3]} in {peak[0]}", 11, "ink2", anchor="middle", th=th)
        ly = top - 14
        b += f'<rect x="{x0}" y="{ly-9}" width="10" height="10" rx="2" fill="{th["blue"]}"/>' + txt(x0 + 16, ly, f"Did not come before the Court ({n_all - n_ch})", 12, "ink", th=th)
        b += f'<rect x="{x0+270}" y="{ly-9}" width="10" height="10" rx="2" fill="{th["orange"]}"/>' + txt(x0 + 286, ly, f"Came before the Court ({n_ch})", 12, "ink", th=th)
        fb, yy = footer(th, top + ph + 44, [SCOPE_FRAME, "Table: figures/data/fig1-basic-laws-by-year.csv."], w)
        return yy + 10, title, desc, b + fb
    write_svg("fig1-basic-laws-by-year", 960, draw)
    dec = Counter(r["passage_date"][:3] + "0s" for r in FRAME)
    dch = Counter(r["passage_date"][:3] + "0s" for r in FRAME if yes(r["challenged"]))
    README.append(("fig1-basic-laws-by-year", title, desc,
        "The full list of laws titled Basic Law, counted by year of passage. " + SCOPE_FRAME,
        md_table(["Decade", "Laws passed", "Of them, came before the Court"], [[d, dec[d], dch[d]] for d in sorted(dec)])))

def bar_path(x, ybase, w, h, r):
    """A column growing up from ybase, square at the base, rounded by r at the data end."""
    r = min(r, w / 2, h)
    yt = ybase - h
    if r <= 0: return f"M{x:.1f},{ybase:.1f}V{yt:.1f}H{x+w:.1f}V{ybase:.1f}Z"
    return (f"M{x:.1f},{ybase:.1f}V{yt+r:.1f}Q{x:.1f},{yt:.1f} {x+r:.1f},{yt:.1f}H{x+w-r:.1f}"
            f"Q{x+w:.1f},{yt:.1f} {x+w:.1f},{yt+r:.1f}V{ybase:.1f}Z")

# ---------------------------------------------------------------- 2. The challenged laws
def parse_outcome(s):
    """Split the frame's challenge_outcome into (class, date) pairs, keeping the reader's words."""
    out = []
    for part in s.split("; "):
        part = part.strip()
        # the date is the last parenthesis that opens with a year or "pending"; a class may carry its own parenthesis
        cut = max(i for i in range(len(part)) if part.startswith(" (", i) and re.match(r"\d{4}|pending", part[i + 2:]))
        out.append((part[:cut], part[cut + 2:-1]))
    return out

def year_of(d):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", d)
    if m: return int(m.group(1)) + (int(m.group(2)) - 1) / 12 + int(m.group(3)) / 365, False
    m = re.match(r"(\d{4})", d)
    return (int(m.group(1)) + 0.5, True) if m else (None, True)

def fig2():
    ch = [r for r in FRAME if yes(r["challenged"])]
    data = []
    for r in ch:
        oc = parse_outcome(r["challenge_outcome"])
        words = "; ".join(f"{c} ({d})" for c, d in oc)
        data.append([r["seq"], r["title_en"], r["passage_date"], words, STEP4.get(r["seq"], "not yet coded"), r["challenge_case"]])
    write_csv("fig2-challenged-laws", ["frame_row", "title", "passed", "provisional_outcome", "t1_step4_code", "cases"], data)
    n_adv = sum(1 for d in data if d[4] == "Adverse"); n_not = sum(1 for d in data if d[4] == "Not adverse")
    title = f"The {len(data)} laws titled Basic Law that came before the Court: passage, and what the Court did"
    sub = ("Each line runs from passage to judgment. The words on the right are the challenge reader's provisional outcome classes; "
           "shape and colour give T1's step-4 code where a docket reader has coded the law.")
    desc = (f"Timeline of the {len(data)} laws that came before the Court, from passage to judgment, 1992 to 2026. {n_adv} are coded Adverse under T1's step 4, "
            f"{n_not} Not adverse, and {len(data) - n_adv - n_not} are not yet coded; for two, no ruling had been found when last checked, on 21 and 22 October 2026.")
    def draw(th):
        w = 1040; b, y0 = header(th, w, title, sub)
        top, lw, x0, pw, rh = y0 + 46, 270, 300, 380, 36
        y_min, y_max = 1990, 2027
        def X(v): return x0 + (v - y_min) / (y_max - y_min) * pw
        for yr in range(1990, 2030, 5):
            b += f'<line x1="{X(yr):.1f}" x2="{X(yr):.1f}" y1="{top-6}" y2="{top + rh*len(data)}" stroke="{th["grid"]}" stroke-width="1"/>'
            b += txt(X(yr), top - 12, yr, 11, "muted", anchor="middle", th=th)
        asof, _ = year_of("2026-10-22")
        for i, d in enumerate(data):
            r = ch[i]; y = top + i * rh + rh / 2
            code = d[4]; col = th["orange"] if code == "Adverse" else th["blue"] if code == "Not adverse" else th["muted"]
            p, _ = year_of(r["passage_date"])
            oc = parse_outcome(r["challenge_outcome"])
            last_c, last_d = oc[-1]
            j, approx = year_of(last_d) if last_d != "pending" else (asof, False)
            b += txt(24, y + 4, SHORT[r["seq"]] + f" ({r['passage_date'][:4]})", 12, "ink", th=th)
            b += f'<line x1="{X(p):.1f}" x2="{X(j):.1f}" y1="{y:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="2" stroke-linecap="round"/>'
            b += f'<circle cx="{X(p):.1f}" cy="{y:.1f}" r="3" fill="{th["ink2"]}"/>'
            b += end_mark(X(j), y, code, last_d == "pending" or approx, th)
            pend = " (no ruling found by 21 October 2026)" if r["seq"] == "128" else " (at the challenge reader's search, 22 October 2026)"
            ol = wrap(d[3].replace(" (pending)", pend).replace(
                "Not decided (moot/withdrawn/premature/in limine)", "Not decided: the Court found it unnecessary to rule on the amendment"), 48)
            b += lines(x0 + pw + 18, y + 4 - (len(ol) - 1) * 6.5, ol, 11, 13, th, "ink2")
        ly = top + rh * len(data) + 26
        b += f'<circle cx="{24+3}" cy="{ly-4}" r="3" fill="{th["ink2"]}"/>' + txt(36, ly, "Passed", 12, "ink", th=th)
        b += end_mark(110, ly - 4, "Adverse", False, th) + txt(122, ly, "Judgment, Adverse under T1 step 4", 12, "ink", th=th)
        b += end_mark(360, ly - 4, "Not adverse", False, th) + txt(372, ly, "Not adverse", 12, "ink", th=th)
        b += end_mark(480, ly - 4, "", False, th) + txt(492, ly, "Not yet coded", 12, "ink", th=th)
        b += end_mark(610, ly - 4, "", True, th) + txt(622, ly, "Hollow: no ruling found, or judgment dated by year only", 12, "ink", th=th)
        notes = ["Under T1's step 4 a law the Court upheld but read narrowly counts as Adverse, so the provisional class and the code can differ "
                 "(the 1994 and 2018 rows). The challenge reader's classes for the 1994 Porat petition and the 1999 case are provisional, as its notes say. "
                 "Where a law was challenged twice, the line ends at the later judgment. Human Dignity and Liberty was not petitioned against; the Court decided its binding force in Mizrahi Bank (research/frame/challenges.json). "
                 "The 2025 row: no ruling found by 21 October 2026 (research/2025-2026-timeline.md). The 2026 row: pending at the challenge reader's search on 22 October 2026 (research/frame/challenges.json).",
                 SCOPE_FRAME, "T1 codes: codebook/m4-codebook.csv. Table: figures/data/fig2-challenged-laws.csv."]
        fb, yy = footer(th, ly + 30, notes, w)
        return yy + 10, title, desc, b + fb
    write_svg("fig2-challenged-laws", 1040, draw)
    README.append(("fig2-challenged-laws", title, desc,
        "The challenged laws, from passage to judgment. Outcome words are provisional; T1's step-4 code is shown where it exists.",
        md_table(["Frame row", "Law", "Passed", "Provisional outcome", "T1 step-4 code"], [[d[0], SHORT[d[0]], d[2], d[3], d[4]] for d in data])))

def end_mark(x, y, code, hollow, th):
    col = th["orange"] if code == "Adverse" else th["blue"] if code == "Not adverse" else th["muted"]
    fill = th["surface"] if hollow else col
    ring = f' stroke="{th["surface"]}" stroke-width="2"' if not hollow else f' stroke="{col}" stroke-width="2"'
    if code == "Adverse": return f'<path d="M{x:.1f},{y-6:.1f}L{x+6:.1f},{y+5:.1f}L{x-6:.1f},{y+5:.1f}Z" fill="{fill}"{ring}/>'
    if code == "Not adverse": return f'<rect x="{x-5:.1f}" y="{y-5:.1f}" width="10" height="10" fill="{fill}"{ring}/>'
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{fill}"{ring}/>'

# ---------------------------------------------------------------- 3. Warning signs in the sample
SIGNS = [("situated_beneficiary", "Alters, in a way others would not share, the position of the government or an officeholder in a matter live on the day it passed (situated; the primary version)", {"Yes": "present", "No": "absent"}),
         ("named_beneficiary", "Addresses a specific interest of the government or an officeholder, on its text (named; the secondary version)", {"Yes": "present", "No": "absent"}),
         ("immediate_effect", "Takes effect within a year, and not only after the next election", {"Yes": "present", "Deferred": "absent"}),
         ("coalition_only", "No opposition member voted for it at the final reading", {"Yes": "present", "No": "absent"}),
         ("expedited", "Expedited: final vote within 30 days of first reading, or a shortened committee stage", {"Yes": "present", "No": "absent"})]

def fig3():
    data = []
    for col, label, mp in SIGNS:
        c = Counter(mp.get(r[col], "not known") for r in SAMPLE)
        data.append([col, label, c["present"], c["absent"], c["not known"]])
    write_csv("fig3-signs-in-sample", ["column", "sign", "present", "absent", "not_known"], data)
    F = Counter(r["F"] for r in SAMPLE if r["F"] != "")
    nF = sum(F.values()); n = len(SAMPLE)
    title = f"The four warning signs Medina reports the Court uses, in the {n} sampled laws where no challenge was found"
    sub = ("Each bar is one sign across the same laws: how many show it, how many do not, and how many cannot be scored from the surviving record. "
           "The beneficiary sign is shown in both its versions. The thresholds are the project's own (note, T1 as revised, step 3).")
    desc = (f"Stacked bars for four warning signs, the beneficiary sign in two versions, across {n} sampled laws where no challenge was found. "
            + "; ".join(f"{d[1].split(' (')[0]}: {d[2]} present, {d[3]} absent, {d[4]} not known" for d in data)
            + f". All four signs can be scored on {nF} laws: " + ", ".join(f"{F[k]} show {k}" for k in sorted(F)) + ".")
    def draw(th):
        w = 960; b, y0 = header(th, w, title, sub)
        top, x0, pw, bh, gap = y0 + 44, 24, 600, 22, 56
        for i, (col, label, p, a, u) in enumerate(data):
            y = top + i * gap
            b += txt(x0, y - 8, label, 12, "ink", th=th)
            x = x0
            for v, key, name in ((p, "orange", "present"), (a, "blue", "absent"), (u, "none", "not known")):
                if not v: continue
                wd = v / n * pw - 2
                b += f'<rect x="{x:.1f}" y="{y:.1f}" width="{wd:.1f}" height="{bh}" rx="3" fill="{th[key]}"><title>{v} {name}</title></rect>'
                if wd >= 22: b += txt(x + wd / 2, y + 15, v, 11, "onfill" if key != "none" else "noneink", "600", "middle", th)
                x += wd + 2
            b += txt(x0 + pw + 14, y + 15, f"{p} present, {a} absent, {u} not known", 11, "ink2", th=th)
        ly = top + len(data) * gap + 6
        for k, (key, name) in enumerate((("orange", "Sign present"), ("blue", "Sign absent"), ("none", "Not known from the record"))):
            b += f'<rect x="{x0 + k*170}" y="{ly-9}" width="10" height="10" rx="2" fill="{th[key]}"/>' + txt(x0 + k * 170 + 16, ly, name, 12, "ink", th=th)
        notes = [f"All four signs can be scored on {nF} of the {n} laws: " + ", ".join(f"{F[k]} show {WORDS[int(k)]}" for k in sorted(F)) +
                 ". Not known is drawn as such, never as absent: for most laws passed before October 2003 no surviving record names the voters at the final reading.",
                 "Scope: Israel; laws titled Basic Law, 1958 to 2026. Sample: every third law in the full list with no challenge found, in order of passage, from the first "
                 "(change log (ah), (al)); no challenge was found in the searches made, which did not reach the court database. Coded by two coders from legislative "
                 "records without opening any judgment, the situated sign by a separate reader, and disagreements settled by an adjudicator. "
                 "Source: codebook/comparison-sample.csv. Table: figures/data/fig3-signs-in-sample.csv."]
        fb, yy = footer(th, ly + 24, notes, w)
        return yy + 10, title, desc, b + fb
    write_svg("fig3-signs-in-sample", 960, draw)
    README.append(("fig3-signs-in-sample", title, desc,
        "How often the warning signs Medina reports appear in sampled Basic Laws where no challenge was found, with unknowns kept apart.",
        md_table(["Sign", "Present", "Absent", "Not known"], [[d[1], d[2], d[3], d[4]] for d in data])))

# ---------------------------------------------------------------- 4. T1's reach
def fig4():
    N = 10
    data = []
    for K in range(5, 11):
        for D in range(1, 7):
            ok = []
            if D >= 6:
                for DA in range(1, D + 1):
                    r = t1.detect(N, K, DA, D - DA)
                    if r["supported_detectable"] and r["refuted_detectable"]: ok.append(f"{DA}/{D-DA}")
            data.append([N, K, D, "yes" if ok else "no", "; ".join(ok)])
    write_csv("fig4-t1-reach", ["N", "K", "discordant", "verdict_possible", "passing_splits"], data)
    # The first run's configuration as results.md records it (N = 5, K = 4, one discordant law predicted Adverse),
    # and the same after the 1994 row was recoded Adverse in the third addendum (K = 5).
    first, recoded = t1.detect(5, 4, 1, 0), t1.detect(5, 5, 1, 0)
    title = "Can T1 reach a verdict on this record? Only if every codable law left is discordant, and only for some numbers of Adverse outcomes"
    sub = ("A calculation from T1's rule as revised on 22 October 2026, written after nine rows' outcomes were known and fixed before the blind recoding. "
           "It uses only the number of laws (N), the number with Adverse outcomes (K) and the number on which T1's two predictions differ.")
    desc = ("Grid of the configurations T1 could face with ten coded laws. A verdict is possible only with six discordant laws and six or seven Adverse "
            "outcomes, or five if a contestable Adverse code were reversed; with eight or more Adverse outcomes, or fewer than six discordant laws, no verdict is possible. "
            "The first run had five laws, four Adverse and one discordant, and could reach no verdict; nor could it after the 1994 row was recoded Adverse.")
    def draw(th):
        w = 960; b, y0 = header(th, w, title, sub, kind="calculation")
        top, x0, cw, chh = y0 + 70, 200, 118, 52
        b += txt(x0 + 3 * cw, top - 40, "Laws on which T1's two predictions differ (discordant)", 12, "ink", "600", "middle", th)
        for D in range(1, 7):
            b += txt(x0 + (D - 1) * cw + cw / 2, top - 14, D if D < 6 else "6, the minimum", 12, "ink2", anchor="middle", th=th)
        b += txt(24, top - 14, "Adverse outcomes (K), of 10", 12, "ink", "600", th=th)
        for i, K in enumerate(range(5, 11)):
            y = top + i * chh
            b += txt(24, y + chh / 2 + 4, f"K = {K}" + (" (only if a contestable" if K == 5 else ""), 12, "ink2", th=th)
            if K == 5: b += txt(24, y + chh / 2 + 18, "code were reversed)", 12, "ink2", th=th)
            for D in range(1, 7):
                d = [r for r in data if r[1] == K and r[2] == D][0]
                x = x0 + (D - 1) * cw
                if d[3] == "yes":
                    b += f'<rect x="{x+1}" y="{y+1}" width="{cw-2}" height="{chh-2}" rx="4" fill="{th["blue"]}" fill-opacity="{th["wash"]}" stroke="{th["blue"]}" stroke-width="1.5"/>'
                    b += check(x + 14, y + 18, th["blue"]) + txt(x + 26, y + 22, "verdict possible", 11, "ink", "600", th=th)
                    every = len(d[4].split("; ")) == D
                    b += txt(x + 10, y + 40, "every split" if every else "splits " + d[4].replace("; ", ", "), 10, "ink2", th=th)
                else:
                    b += f'<rect x="{x+1}" y="{y+1}" width="{cw-2}" height="{chh-2}" rx="4" fill="none" stroke="{th["grid"]}" stroke-width="1"/>'
                    b += txt(x + cw / 2, y + chh / 2 + 4, "below the minimum" if D < 6 else "no verdict", 11, "muted", anchor="middle", th=th)
        y = top + 6 * chh + 26
        notes = [f"Where the project stands: the first run had N = {first['N']} coded laws, {first['K']} of them Adverse, and {first['discordant']} discordant; "
                 f"T1's check returned \"{first['verdict_before_outcomes']}\". After the 1994 row was recoded Adverse, K = {recoded['K']} of {recoded['N']} and the check "
                 f"again returned \"{recoded['verdict_before_outcomes']}\" (research/coding-2026-10-22/results.md, third addendum).",
                 "Why ten: on the challenge reader's provisional outcome classes, the frame holds 11 challenged Basic Laws decided from Mizrahi Bank (1995) onward "
                 "with an outcome of Adverse or Not adverse; five are coded, "
                 "the 1992 law cannot be coded until a record names its voters, and five remain codable (the Incapacity amendment, issue 19, and the four "
                 "judged laws of issue 8). Six of the ten already have Adverse outcomes, so K is at least 6, unless a contestable code is reversed: the Nation-State "
                 "and 1994 codes are both flagged (codebook/README.md; ledger F11). The existing discordant law is one the decision "
                 "rule predicts Adverse, so every split has at least one such law. A split such as 3/3 gives the discordant laws the decision rule predicts Adverse, then those it predicts Not adverse.",
                 "Calculation: analysis/t1_revised.py, detect, for every split. Audit: research/audit-2026-10-25.md, finding 3. Table: figures/data/fig4-t1-reach.csv."]
        fb, yy = footer(th, y, notes, w)
        return yy + 10, title, desc, b + fb
    write_svg("fig4-t1-reach", 960, draw)
    README.append(("fig4-t1-reach", title, desc,
        "Where T1's rule can return a verdict, with ten coded laws. A calculation, not evidence.",
        md_table(["K (Adverse of 10)", "Discordant", "Verdict possible", "Passing splits"], [[d[1], d[2], d[3], d[4] or "none"] for d in data])))

def check(x, y, col):
    return f'<polyline points="{x-5},{y} {x-1.5},{y+3.5} {x+5},{y-4}" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'

# ---------------------------------------------------------------- 5. Geometry: the sliding scale
TIERS = ["Entrenches", "None", "Limited", "Sharp"]
SUPPORT = [("Yes", "Coalition only"), ("No", "At least one opposition vote"), ("", "Not known")]

def fig5():
    marks = []
    for r in SAMPLE: marks.append((r["deviation_tier"], r["coalition_only"], "never", r["title_en"], r["passage_date"]))
    for mid, seq in M4_FRAME.items():
        r = [x for x in M4 if x["id"] == mid][0]
        marks.append((r["deviation_tier"], r["coalition_only"], r["outcome"], SHORT[seq], r["year"]))
    cells = defaultdict(list)
    for m in marks: cells[(m[0], m[1])].append(m)
    data = [[t, lab, sum(1 for m in cells[(t, s)] if m[2] == "never"), sum(1 for m in cells[(t, s)] if m[2] == "Adverse"),
             sum(1 for m in cells[(t, s)] if m[2] == "Not adverse")] for s, lab in SUPPORT for t in TIERS]
    write_csv("fig5-sliding-scale", ["deviation_tier", "coalition_only", "never_challenged", "challenged_adverse", "challenged_not_adverse"], data)
    n_never = sum(1 for m in marks if m[2] == "never"); n_ch = len(marks) - n_never
    title = f"Where {len(marks)} coded Basic Laws sit on two axes of the sliding scale that Medina reads in the Court's approach"
    sub = ("Across: whether and how far the law contradicts the five democratic values, as the coders scored it. Down: whether any opposition member voted for it. "
           "Each mark is one law.")
    desc = (f"A grid of deviation tier against coalition-only passage for {n_never} sampled laws where no challenge was found and {n_ch} challenged Basic Laws coded under T1. "
            + "; ".join(f"{d[0]}, {d[1].lower()}: {d[2]} with no challenge found, {d[3]} Adverse, {d[4]} Not adverse" for d in data if d[2] or d[3] or d[4]) + ".")
    def draw(th):
        w = 980; b, y0 = header(th, w, title, sub)
        top, x0, cw, chh = y0 + 54, 210, 180, 96
        for i, t in enumerate(TIERS): b += txt(x0 + i * cw + cw / 2, top - 12, t, 12, "ink", "600", "middle", th)
        b += txt(x0 + 2 * cw, top - 32, "Deviation tier, as coded: Entrenches and None contradict no value; Limited and Sharp contradict one (ordered steps, not distances)", 11, "ink2", anchor="middle", th=th)
        for j, (s, lab) in enumerate(SUPPORT):
            y = top + j * chh
            b += lines(24, y + chh / 2, wrap(lab, 22), 12, 15, th, "ink", "600")
            for i, t in enumerate(TIERS):
                x = x0 + i * cw
                b += f'<rect x="{x+2}" y="{y+2}" width="{cw-4}" height="{chh-4}" rx="4" fill="none" stroke="{th["grid"]}" stroke-width="1"/>'
                ms = sorted(cells[(t, s)], key=lambda m: (m[2] != "Adverse", m[2] != "Not adverse"))
                for k, m in enumerate(ms):
                    mx = x + 18 + (k % 8) * 19; my = y + 22 + (k // 8) * 19
                    if m[2] == "never": b += f'<circle cx="{mx}" cy="{my}" r="5" fill="{th["aqua"]}" stroke="{th["surface"]}" stroke-width="2"><title>{esc(m[3])} ({m[4][:4]}): no challenge found</title></circle>'
                    else: b += end_mark(mx, my, m[2], False, th).replace("/>", f"><title>{esc(m[3])} ({m[4][:4]}): {m[2]}</title></path>" if m[2] == "Adverse" else f"><title>{esc(m[3])} ({m[4][:4]}): {m[2]}</title></rect>", 1)
                if ms: b += txt(x + cw - 10, y + chh - 12, f"{len(ms)}", 11, "ink2", anchor="end", th=th)
        ly = top + 3 * chh + 24
        b += f'<circle cx="{x0+5}" cy="{ly-4}" r="5" fill="{th["aqua"]}"/>' + txt(x0 + 16, ly, f"No challenge found ({n_never})", 12, "ink", th=th)
        b += end_mark(x0 + 210, ly - 4, "Adverse", False, th) + txt(x0 + 222, ly, "Challenged, Adverse under T1 step 4", 12, "ink", th=th)
        b += end_mark(x0 + 470, ly - 4, "Not adverse", False, th) + txt(x0 + 482, ly, "Challenged, Not adverse", 12, "ink", th=th)
        notes = ["The scale: the sliding scale is Medina's reading of the Court's approach, which he presents as the article's main novelty (p. 681). "
                 "In it, the greater an amendment's departure from the unwritten constitution, the more stringent the procedural requirements, among them "
                 "the majority needed for enactment, the government's immediate interest and whether the amendment takes effect at once (pp. 702, 708). Neither axis here is a distance. The tiers are ordered steps; positions inside a cell only keep the marks apart; and "
                 "\"at least one opposition vote\" is not broad support. Breadth needs the opposition's share of the vote, which is not yet recorded (issue 16).",
                 "Scope: Israel; laws titled Basic Law, 1958 to 2026. Laws: the 39 sampled laws where no challenge was found and the 7 challenged Basic Laws in the codebook; "
                 "the two 1969 statutes in the codebook are ordinary laws and are left out. Values coded from legislative records by coders who did not open the "
                 "judgments, though both reported seeing court outcomes in search snippets for four of the challenged laws (results.md); outcome-blindness is not "
                 "claimed for them. Coalition-only passage "
                 "is not known where no record names the voters, mostly before October 2003.",
                 "Sources: codebook/comparison-sample.csv, codebook/m4-codebook.csv. Table: figures/data/fig5-sliding-scale.csv."]
        fb, yy = footer(th, ly + 26, notes, w)
        return yy + 10, title, desc, b + fb
    write_svg("fig5-sliding-scale", 980, draw)
    README.append(("fig5-sliding-scale", title, desc,
        "A geometry of the coded laws on the two axes of the sliding scale. The axes are ordered categories, not distances.",
        md_table(["Deviation tier", "Coalition-only passage", "No challenge found", "Challenged, Adverse", "Challenged, Not adverse"], data)))

# ---------------------------------------------------------------- 6. Ledger
STATUS = {"established": ("Established", "blue"), "refuted": ("Refuted", "orange"), "contested": ("Contested", "aqua"),
          "unclear": ("Unclear", None), "inconclusive": ("Inconclusive under a rule set before the run", "none"),
          "not-yet-checkable": ("Not yet checkable", None)}

def status_square(x, y, s, th, size=18):
    name, key = STATUS[s]
    c = x + size / 2; m = y + size / 2
    if key in ("blue", "orange", "aqua"):
        b = f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="3" fill="{th[key]}"/>'
        g = th["onfill"]
    elif key == "none":
        b = f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="3" fill="{th["none"]}"/>'; g = th["noneink"]
    else:
        b = f'<rect x="{x+0.75}" y="{y+0.75}" width="{size-1.5}" height="{size-1.5}" rx="3" fill="none" stroke="{th["muted"]}" stroke-width="1.5"/>'; g = th["ink"]
    if s == "established": b += check(c, m, g)
    elif s == "refuted": b += f'<path d="M{c-4},{m-4}L{c+4},{m+4}M{c+4},{m-4}L{c-4},{m+4}" stroke="{g}" stroke-width="2" stroke-linecap="round"/>'
    elif s == "contested": b += (f'<path d="M{c-5},{m-2.5}H{c+5}M{c+2.5},{m-5}L{c+5},{m-2.5}L{c+2.5},{m}M{c+5},{m+2.5}H{c-5}M{c-2.5},{m}L{c-5},{m+2.5}L{c-2.5},{m+5}" '
                                 f'stroke="{g}" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    elif s == "unclear": b += f'<text x="{c}" y="{m+4.5}" font-size="13" font-weight="bold" text-anchor="middle" fill="{g}">?</text>'
    elif s == "inconclusive": b += f'<path d="M{c-4.5},{m-2.5}H{c+4.5}M{c-4.5},{m+2.5}H{c+4.5}" stroke="{g}" stroke-width="2" stroke-linecap="round"/>'
    else: b += "".join(f'<circle cx="{c+dx}" cy="{m}" r="1.4" fill="{g}"/>' for dx in (-4, 0, 4))
    return b

def fig6():
    L = rows("figures/sources/ledger.csv")
    write_csv("fig6-ledger", ["id", "section", "item", "status", "basis"], [[r["id"], r["section"], r["item"], STATUS[r["status"]][0], r["basis"]] for r in L])
    cnt = Counter(r["status"] for r in L)
    title = f"Ledger: the status of {len(L)} claims and results, as the record stands"
    sub = ("One square per claim or result, grouped by section: the note's four claims, its rivals and its evidence items, then checks on the data from the "
           "repository's records. Every status has a glyph as well as a colour, and every row cites its basis in the table.")
    desc = (f"A list of {len(L)} claims and results with their status: " + ", ".join(f"{cnt[k]} {STATUS[k][0].lower()}" for k in STATUS if cnt[k]) +
            ". None of the four claims is established or refuted.")
    def draw(th):
        w = 980; b, y0 = header(th, w, title, sub, kind="record")
        y = y0 + 34
        x = 24
        for k in STATUS:
            b += status_square(x, y - 13, k, th, 16) + txt(x + 22, y, STATUS[k][0], 12, "ink", th=th)
            x += 30 + len(STATUS[k][0]) * 6.6
            if x > w - 220: x = 24; y += 24
        y += 34
        sec = None
        for r in L:
            if r["section"] != sec:
                sec = r["section"]; y += 8
                b += txt(24, y, sec, 13, "ink", "600", th=th) + f'<line x1="24" x2="{w-24}" y1="{y+7}" y2="{y+7}" stroke="{th["grid"]}"/>'
                y += 24
            ls = wrap(r["item"], 104)
            b += status_square(24, y - 13, r["status"], th) + txt(52, y, r["id"], 11, "muted", "600", th=th)
            b += lines(88, y, ls, 12, 16, th, "ink")
            b += txt(w - 24, y, STATUS[r["status"]][0].split(" under")[0], 11, "ink2", anchor="end", th=th)
            y += len(ls) * 16 + 8
        notes = ["Rule: the ledger lists the note's four claims, its rivals, the results in \"What the evidence already says\", and the checks run on the data. "
                 "Readings and tests are not listed: readings make no claim of their own, and each test's result is listed under the claim it bears on. "
                 "Statuses follow the record; quoted wording keeps the sources' strength, and claims are attributed to whoever makes them.",
                 "Basis for every row: figures/data/fig6-ledger.csv (from figures/sources/ledger.csv)."]
        fb, yy = footer(th, y + 10, notes, w)
        return yy + 10, title, desc, b + fb
    write_svg("fig6-ledger", 980, draw)
    README.append(("fig6-ledger", title, desc,
        "The note's claims, rivals and evidence items, and the main checks on the data, each with its status and the basis for it.",
        md_table(["ID", "Section", "Claim or result", "Status", "Basis"], [[r["id"], r["section"], r["item"], STATUS[r["status"]][0], r["basis"]] for r in L])))

# ---------------------------------------------------------------- 7. Errors list
STATE = {"corrected": ("Corrected", "blue"), "recorded": ("Recorded, not undone", "none"), "open": ("Open", "orange")}

def fig7():
    E = sorted(rows("figures/sources/errors.csv"), key=lambda e: (e["date"], int(e["id"])))
    write_csv("fig7-errors", ["id", "date", "band", "kind", "what_was_wrong", "caught_by", "corrected_in", "state"],
              [[e[k] for k in ("id", "date", "band", "kind", "what_was_wrong", "caught_by", "corrected_in", "state")] for e in E])
    cnt = Counter(e["state"] for e in E); bands = Counter(e["band"] for e in E)
    title = f"Errors list: {len(E)} mistakes found so far in the project's own work, what caught each, and where each stands"
    sub = "Grouped into research errors, errors in reviews of the work, and process errors. Each row names its date, its kind and what caught it."
    desc = (f"A list of {len(E)} errors: {bands['research']} in the research, {bands['review']} in reviews and {bands['process']} in process. "
            f"{cnt['corrected']} are corrected, {cnt['recorded']} recorded and not undone, and {cnt['open']} open.")
    def draw(th):
        w = 1040; b, y0 = header(th, w, title, sub, kind="record")
        y = y0 + 34; x = 24
        for k, (nm, key) in STATE.items():
            b += state_dot(x + 7, y - 4, k, th) + txt(x + 18, y, nm, 12, "ink", th=th); x += 40 + len(nm) * 6.6
        y += 30
        heads = [(24, "Date"), (110, "Kind"), (250, "What was wrong"), (700, "What caught it"), (w - 24, "State")]
        for hx, hn in heads: b += txt(hx, y, hn, 11, "muted", "600", "end" if hn == "State" else "start", th)
        y += 10
        for band, bname in (("research", "Research"), ("review", "Reviews of the work"), ("process", "Process")):
            y += 18; b += txt(24, y, bname, 13, "ink", "600", th=th) + f'<line x1="24" x2="{w-24}" y1="{y+7}" y2="{y+7}" stroke="{th["grid"]}"/>'
            y += 24
            for e in [e for e in E if e["band"] == band]:
                a, k2, c = wrap(e["what_was_wrong"], 70), wrap(e["kind"], 20), wrap(e["caught_by"], 40)
                b += txt(24, y, e["date"], 11, "ink2", th=th) + lines(110, y, k2, 11, 14, th, "ink2")
                b += lines(250, y, a, 12, 15, th, "ink") + lines(700, y, c, 11, 14, th, "ink2")
                b += state_dot(w - 30, y - 4, e["state"], th)
                y += max(len(a) * 15, len(c) * 14, len(k2) * 14) + 10
        notes = ["Rule: an error is listed if it reached the repository's record (a commit, the change log or an issue), or was made in a review given to the author, "
                 "and was later found wrong, whether it has since been corrected, recorded without being undone, or is still open. Each date is the day the error was found. Drafts corrected before they "
                 "were committed are not listed. No error recorded so far is a mistranslation; much of the work rests on Hebrew sources read by language-model "
                 "readers, so that is not evidence that none has occurred.",
                 "Where each was corrected: figures/data/fig7-errors.csv (from figures/sources/errors.csv), which cites the change-log item, commit or issue."]
        fb, yy = footer(th, y + 6, notes, w)
        return yy + 10, title, desc, b + fb
    write_svg("fig7-errors", 1040, draw)
    README.append(("fig7-errors", title, desc,
        "The mistakes found so far in the project's own work, with what caught each and where each stands.",
        md_table(["#", "Date", "Kind", "What was wrong", "What caught it", "Corrected in", "State"],
                 [[e["id"], e["date"], e["kind"], e["what_was_wrong"], e["caught_by"], e["corrected_in"], STATE[e["state"]][0]] for e in E])))

def state_dot(x, y, s, th):
    nm, key = STATE[s]
    if key == "none": return f'<circle cx="{x}" cy="{y}" r="5" fill="{th["none"]}"/>'
    if s == "open": return f'<circle cx="{x}" cy="{y}" r="4.5" fill="none" stroke="{th[key]}" stroke-width="2"/>'
    return f'<circle cx="{x}" cy="{y}" r="5.5" fill="{th[key]}"/>' + check(x, y, th["onfill"]).replace('stroke-width="2"', 'stroke-width="1.6"')

# ---------------------------------------------------------------- 8. The imagined jigsaw
SETTLED = {"established", "refuted"}

def fig8():
    J = json.load(io.open(path("figures/sources/jigsaw.json"), encoding="utf-8"))
    L = {r["id"]: r for r in rows("figures/sources/ledger.csv")}
    pieces = []
    for p in J["pieces"]:
        st = [L[i]["status"] for i in p["items"]]
        s = sum(1 for x in st if x in SETTLED); part = sum(1 for x in st if x in SETTLED or x == "inconclusive")
        fill = "filled" if s == len(st) else "half" if part else "empty"
        pieces.append(dict(p, fill=fill, settled=s, n=len(st)))
    write_csv("fig8-jigsaw", ["piece", "question", "items", "settled_items", "fill"],
              [[p["id"], p["question"], " ".join(p["items"]), f"{p['settled']} of {p['n']}", p["fill"]] for p in pieces])
    title = "Imagined jigsaw: how the project's questions might fit around its ideal"
    sub = ("Imagined. Not a result. Each piece is a question. It half-fills when an item named on it is established, refuted, or inconclusive under a rule "
           "set before the run, and fills only when all are established or refuted; a fill is not progress toward an answer. Threads join pieces; their conclusions are conjectures.")
    desc = ("An imagined figure, drawn in violet. Seven pieces surround an empty centre, the project's ideal: "
            + "; ".join(f"{p['question']} ({p['fill'].replace('half', 'half-filled').replace('empty', 'empty and tilted')}, {p['settled']} of {p['n']} items established or refuted)" for p in pieces)
            + ". Three numbered threads join pieces; each is captioned below with its premises and a conjecture.")
    import math
    def draw(th):
        w = 1000; b, y0 = header(th, w, title, sub, kind="imagined")
        cx, cy, R = w / 2, y0 + 330, 285
        pw, ph = 214, 104
        pos = {}
        for k, p in enumerate(pieces):
            a = -math.pi / 2 + k * 2 * math.pi / len(pieces)
            pos[p["id"]] = (cx + R * math.cos(a), cy + R * 0.92 * math.sin(a))
        labels = ""
        for t in J["threads"]:
            # a thread runs centre to centre behind the pieces; its number sits where it leaves the first piece
            (x1, y1), (x2, y2) = pos[t["from"]], pos[t["to"]]
            b += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{th["violet"]}" stroke-width="1.5" stroke-opacity="0.75"/>'
            dx, dy = x2 - x1, y2 - y1
            te = min((pw / 2 + 18) / abs(dx) if dx else 9, (ph / 2 + 18) / abs(dy) if dy else 9)
            qx, qy = x1 + te * dx, y1 + te * dy
            labels += f'<circle cx="{qx:.1f}" cy="{qy:.1f}" r="11" fill="{th["surface"]}" stroke="{th["violet"]}" stroke-width="1.5"/>' + txt(qx, qy + 4, t["n"], 11, "violet", "bold", "middle", th)
        b += f'<circle cx="{cx}" cy="{cy}" r="104" fill="{th["surface"]}" stroke="{th["violet"]}" stroke-width="2"/>'
        cl = wrap(J["centre"], 24)
        b += lines(cx, cy - (len(cl) - 1) * 7 + 4, cl, 11, 14, th, "violet", "600", "middle")
        for p in pieces:
            x, y = pos[p["id"]]
            rot = f' transform="rotate(-6 {x:.1f} {y:.1f})"' if p["fill"] == "empty" else ""
            fillc = th["violet"] if p["fill"] == "filled" else "none"
            b += f'<g{rot}>'
            b += f'<rect x="{x-pw/2:.1f}" y="{y-ph/2:.1f}" width="{pw}" height="{ph}" rx="10" fill="{th["surface"]}"/>'
            b += f'<rect x="{x-pw/2:.1f}" y="{y-ph/2:.1f}" width="{pw}" height="{ph}" rx="10" fill="{fillc}" stroke="{th["violet"]}" stroke-width="2"/>'
            if p["fill"] == "half":
                b += f'<path d="M{x-pw/2+10:.1f},{y-ph/2:.1f}H{x:.1f}V{y+ph/2:.1f}H{x-pw/2+10:.1f}Q{x-pw/2:.1f},{y+ph/2:.1f} {x-pw/2:.1f},{y+ph/2-10:.1f}V{y-ph/2+10:.1f}Q{x-pw/2:.1f},{y-ph/2:.1f} {x-pw/2+10:.1f},{y-ph/2:.1f}Z" fill="{th["violet"]}" fill-opacity="{th["wash"]}"/>'
            ink = "onfill" if p["fill"] == "filled" else "ink"
            b += lines(x - pw / 2 + 12, y - ph / 2 + 20, wrap(p["question"], 30), 12, 15, th, ink, "600")
            fl = {"filled": "Filled", "half": "Half-filled", "empty": "Empty, tilted: open"}[p["fill"]]
            b += txt(x - pw / 2 + 12, y + ph / 2 - 40, fl, 11, ink, "600", th=th)
            b += txt(x - pw / 2 + 12, y + ph / 2 - 26, f"{p['settled']} of {p['n']} established or refuted", 11, ink, th=th)
            b += txt(x - pw / 2 + 12, y + ph / 2 - 11, "Items: " + ", ".join(p["items"]), 10, "ink2" if p["fill"] != "filled" else "onfill", th=th)
            b += '</g>'
        b += labels
        y = cy + R + ph / 2 + 30
        b += txt(24, y, "Threads (imagined; premises from the record, conclusions conjectures)", 13, "violet", "600", th=th); y += 20
        for t in J["threads"]:
            ls = wrap(f"{t['n']}. Premises: {t['premises']} Conjecture: {t['conjecture']}", 150)
            b += lines(24, y, ls, 11, 15, th, "ink"); y += len(ls) * 15 + 6
        notes = ["Rule for pieces: " + J["rule"], "Item IDs are the ledger's (figures/data/fig6-ledger.csv). Pieces: figures/data/fig8-jigsaw.csv, from figures/sources/jigsaw.json."]
        fb, yy = footer(th, y + 6, notes, w)
        return yy + 10, title, desc, b + fb
    write_svg("fig8-jigsaw", 1000, draw)
    README.append(("fig8-jigsaw", title, desc,
        "Imagined. Not a result. The project's questions as pieces around its ideal, with three conjectural threads.",
        md_table(["Piece", "Question", "Items", "Settled", "Drawn as"], [[p["id"], p["question"], ", ".join(p["items"]), f"{p['settled']} of {p['n']}",
                 {"filled": "filled", "half": "half-filled", "empty": "empty and tilted"}[p["fill"]]] for p in pieces])
        + "\n" + "".join(f"Thread {t['n']} ({t['from']} to {t['to']}). Premises: {t['premises']} Conjecture: {t['conjecture']}\n\n" for t in J["threads"])))

# ---------------------------------------------------------------- README
def write_readme():
    s = ["# Figures", "",
         "Eight figures of the project: four measured from its data, one calculation from T1's rule, a ledger and an errors list drawn from its record, "
         "and one imagined figure. Each carries a label saying which. Measured and imagined are kept apart: the imagined figure alone is drawn in violet "
         "and says so in its title. Each figure comes in a light and a dark version.", "",
         "Counts and statistics drawn from the data are computed by `analysis/make_figures.py` from the files each figure names. The ledger, the errors "
         "list and the jigsaw are curated by hand in `figures/sources/`, and every row there cites its basis. A few fixed values are set in the script, "
         "each with its source: the ten laws of figure 4, the first run's configuration, and the scope dates.", "",
         "Every title, caption and label was tested against the sources by a separate reader before publication. Its findings, and what was changed in "
         "response, are in [corrections.md](corrections.md).", "",
         "Rebuild them from the repository's root with `python3 analysis/make_figures.py`.", ""]
    for name, title, desc, caption, table in README:
        s += [f"## {title}", "",
              f'<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="{name}-dark.svg">\n  <img src="{name}-light.svg" alt="{esc(desc)}">\n</picture>', "",
              caption, "", f"Alt text: {desc}", "", "<details><summary>Table view</summary>", "", table, "</details>", ""]
    io.open(path("figures", "README.md"), "w", encoding="utf-8").write("\n".join(s))

if __name__ == "__main__":
    os.makedirs(path("figures"), exist_ok=True)
    for f in (fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8): f()
    write_readme()
    print("wrote", len(README), "figures to figures/")
