# The frame: every law titled Basic Law, 1958 to 2026

Built on 22 October 2026 under the counting rule in the note's change log item (ah): one row per law titled Basic Law as passed by the Knesset at its third reading, however many Basic Laws it amends; new Basic Laws, re-enactments, amendments and temporary provisions alike; ordinary statutes that touch a Basic Law listed separately and not counted. The frame is the population from which the comparison sample of the revised T1 is drawn (issue 9) and the list against which the challenged set of part (a) is completed (issue 8).

The frame was corrected later the same day, after coding of the first draw had begun, and the sample was drawn again from the corrected frame (change log item (al)). The section "The defect and its correction" below explains why. The frame as first built, with the first draw and its verification, is kept as a record.

## Files

- `basic-law-frame.csv`: the corrected frame, 130 rows in chronological order of passage, with title, passage date and its basis, gazette reference, the Basic Laws the law amends, kind, canonical subject, whether it was challenged and by what case, the `sampled` column from the redraw, which readers reported it, sources and notes. Three columns tie each row to the first draw: `first_draw_seq` is the row of the frame as built that carried the law, `first_draw_sampled` is that row's value in the first draw, and `first_draw_match` says whether the law was the one that row was titled for or the second law merged into it. The verification columns are carried over only where the law is the one the first-draw row was titled for, since the verification searched that title.
- `basic-law-frame-as-built.csv`: the frame as first built, 122 rows, with the first draw and its verification. It is superseded and kept as a record.
- `merge-defect.json`: the eight merged rows of the frame as built, from `analysis/frame_merge_check.py`.
- `same-page-order.json`: the printed order of laws passed the same day on the same gazette page, with the evidence for each pair and the rule applied where there was none.
- `frame-knesset.json`, `frame-government.json`, `frame-economy-judiciary-rights.json`: the three readers' lists, saved verbatim, each with the ordinary statutes it found, the Wikisource-versus-Nevo discrepancies it recorded, and its deviations.
- `challenges.json`: the challenge reader's list of every Basic Law enactment or amendment attacked before the Court, with the cases it considered and rejected.
- `summary.json`: the counts the build script printed for the frame as built. The corrected build's counts are in the table below.
- `verification-sheet.md`: the brief the docket readers worked from for the first draw's rows; `verification-a.json`, `verification-a2.json` and `verification-b.json`: their reports, saved verbatim; `verification-summary.json`: what `analysis/apply_verification.py` printed when it applied them to the frame as built.

## How it was built

Three readers each took a group of Basic Laws and read, for each, the amendment history on Hebrew Wikisource and on Nevo, cross-checking the two and recording every discrepancy; passage dates were read from the "passed by the Knesset on" footnote of the gazette text, reached through Internet Archive captures of the Knesset's PDFs because the Knesset's own sites are geo-blocked (issue 6). The Government reader also used the Knesset's national legislation database as mirrored by Open Knesset, which lists every law bound to each Basic Law with its gazette reference and direct-or-indirect classification; that mirror is a route the other readers did not use and issue 6 now names. A fourth reader compiled the challenges from Chief Justice Hayut's survey in the Reasonableness judgment, Versa, the petitioners' own sites and the Hebrew press. The build script merges two readers' entries into one row when they share the gazette issue and page and name the same law, judged by the Basic Law first named in the title and the amendment number. A law that two readers reported from two Basic Laws' histories is therefore one row. The script orders rows by passage date, then by gazette issue and page as numbers, then by printed order on a shared page, and matches each challenge to a row by subject, passage date and amendment number.

## Counts and checks

| Quantity | Value |
|---|---|
| Rows (laws titled Basic Law, 12 February 1958 to 13 July 2026) | 130 |
| Reader entries merged into them | 143 |
| Rows reported by more than one reader (indirect amendments) | 11 |
| Challenged rows | 14 |
| Unchallenged rows, the population for the draw | 116 |
| Rows whose date is a publication date, not a passage date | 5 |
| Laws through January 2023 | 122 |
| Basic-Law changes through January 2023, counting each Basic Law a law amends once | 141 |

Two checks. First, Hayut's opinion in the Reasonableness judgment (para 83) counts 139 changes to Basic Laws from 1958 to January 2023. The corrected frame has 122 laws through that date, and 141 changes if each Basic Law a law amends is counted once. The Court's figure lies between the two, and the counting rule behind it is not stated, so the comparison neither confirms nor refutes completeness. It does bound the frame: the frame cannot be missing many laws unless the Court's count is of laws. The frame as built gave 114 laws and a figure of 159 changes. That figure was wrong: it counted a Basic Law twice where a reader listed it under both its English and its Hebrew name. Counted once each, the frame as built gives 137. Second, the three readers' counts agree with Hebrew Wikipedia's amendment counts for every Basic Law, with the discrepancies each recorded.

The one expectation recorded before the draw, that every sampled row has exactly one final-reading vote and no two share one, could not be checked until the sampled rows were coded. It has since been checked on the redraw: see "The one-vote check" in `research/coding-sample-2026-10-22/README.md`.

## Marked as challenged

Fourteen rows. Seven were in the codebook already: the 1992 Basic Law: Human Dignity and Liberty, the 1994 Freedom of Occupation re-enactment with its override clause, the 2016 and 2020 budget measures, the Nation-State law, and the two 2023 amendments. Seven were not: Basic Law: The Government (Amendment No. 9) of 1999, on the number of ministers (HCJ 5160/99, dismissed); the 2010 amendment extending the biennial budget (HCJ 4908/10 Bar-On, dismissed); Basic Law: The Knesset (Amendment No. 44) of 2016, the expulsion law (HCJ 5744/16 Ben Meir, dismissed); Basic Law: The Government (Amendment No. 8 and Temporary Provision) of 2020, the rotation government (HCJ 2905/20, dismissed); Basic Law: The Government (Amendment No. 11) of 2022, behind the Deri appointment (HCJ 8948/22, the attack on the amendment left undecided); Basic Law: The Judiciary (Amendment No. 4) of 2025, the Judicial Selection Committee (pending); and Basic Law: Torah Study of 13 July 2026 (pending). The 1994 row carries two challenges, Porat and Mitrael. These seven are the candidates for new rows under issue 8, each to be coded under the protocol like any other; nothing from the challenge list is entered in the codebook by hand.

## Gaps a reader should know

- Five rows carry the gazette publication date because no archive capture of the Knesset PDF exists: three 2020 amendments to the State Economy temporary provision and the 2023 Amendments No. 13 and 14 to Basic Law: The State Economy. A passage date is at most days earlier and the ordering is unaffected unless another law passed in between.
- The window from December 2025 to October 2026 could not be checked against the Knesset's own database; Wikisource and Nevo show nothing after Basic Law: The Government (Amendment No. 13) of May 2025 except Basic Law: Torah Study.
- Two laws bear the published title Basic Law: The Knesset (Amendment No. 8), one of 1974 and one of 1981, and none bears No. 5; Nevo renumbers the 1974 law. The frame keeps published titles. Basic Law: The Knesset (Amendment No. 16) is an ordinary statute and is in the separate list.
- Two laws bear the published title Basic Law: The President of the State (Amendment No. 6), one of 16 October 2001 and one of 28 July 2003; the gazette prints both so. WIPO Lex numbers the 2001 law No. 5, "originally numbered 6", and the Government reader found that Nevo and the Knesset database count the 1969 pensions statute as the President law's first amendment. The frame keeps published titles.
- The challenge reader did not reach the judgments on the judiciary's site; its classifications for the 1994 Porat petition and the 1999 case are provisional, as its notes say, and the outcome classes it recorded are the reader's, not the protocol's step 4 codings, which the docket reader assigns when a row is coded.
- Eleven ordinary statutes that touched Basic Laws (transitional laws, two convening laws, a fiscal-year law, and the 1994 committee-size law the Knesset numbered as a Basic Law amendment) are in the readers' lists and not in the frame, as the counting rule requires.

## The first draw, superseded

Made on 22 October 2026 under the rule in item (ah), from the frame as built, by the build script's `--draw` flag: every third unchallenged row from the first in chronological order, positions 1, 4, 7 and so on, with no seed and no judgment. It gives 36 rows. By subject: Knesset 11, Government 9, State Economy 7, Freedom of Occupation 2, President 2, and one each of the Army, Jerusalem, State Comptroller, Judiciary and budget temporary Basic Laws. By kind: 26 amendments, 5 temporary provisions, 4 enactments, 1 re-enactment. By decade: two from the 1950s, one from the 1960s, two from the 1970s, four from the 1980s, nine from the 1990s, seven from the 2000s, six from the 2010s and five from the 2020s. Two of the 36 carry a publication date rather than a passage date. The draw is deterministic from the frame, so a corrected frame changes the draw; any row added or removed before the sampled rows are coded shifts every later position, and the change log records any such shift. A sampled row that the docket reader finds to have been challenged moves to part (a) and is not replaced.

## Verification of the first draw

On 22 October 2026 two docket readers, eighteen rows each, searched for any petition or appeal that attacked a sampled enactment's validity, binding force or application as an abuse of constituent power, in the order the verification sheet sets: Hayut's survey in the Reasonableness judgment and the Bar-On judgment, Hebrew Wikipedia's Basic Law articles, the petitioners' sites, Versa, and Hebrew and English press searches. The 1992 Basic Law: The Government, which one reader had first searched only through its State Economy provision, was searched again as a whole law in a second pass. Result: no challenge found on any of the 36 rows, each with its search recorded in the `verification_search` column and the cases that applied or interpreted the enactment, without attacking it, in `related_cases`. No row moved to the challenged set, so the sample stands at 36 and the draw is unchanged.

Three limits. First, every verdict rests on absence in the sources searched: neither reader reached the judiciary's database or Nevo's case search, and the petitioners' case lists surfaced only through web searches, so a petition that left no trace in Hayut's survey, Wikipedia or the press would be missed. Second, one judgment call is recorded on the 2020 State Economy temporary provision (row 101 of the frame as built, row 109 of the corrected frame): the Shafir petitions attacked the later Amendment No. 50 to Basic Law: The Knesset, which amended that provision, not the provision as enacted in April 2020; the reader coded no challenge and said a reviewer who treats an attack on a later amendment of a provision as an attack on the provision would re-code. Third, the readers could not read most of the amendments' own texts, because the Knesset's PDFs are geo-blocked and the archive was unreachable from their fetch tool, so several rows' contents are described from secondary sources and flagged in the notes; that affects the coding to come, not the verification.

## The defect and its correction

On 22 October 2026, while the sample was being coded, one coder reported that sampled row 67 of the frame as built held two laws: Basic Law: The President of the State (Amendment No. 6) and Basic Law: The Knesset (Amendment No. 34). Both came from one bill, passed on 16 October 2001 and are printed on the same gazette page, but each has its own title and its own Knesset PDF. The build script merged reader entries on the gazette issue and page alone, so two separately titled laws printed on one page became one row. `analysis/frame_merge_check.py` groups the readers' entries by that key and reports every group that names more than one law; its output is `merge-defect.json`.

| Gazette issue, page | Frame row | Laws merged into it | Passage date |
|---|---|---|---|
| 1016, 168 | 17 | Knesset Amendments No. 7 and No. 8 | 1 April 1981 |
| 1494, 42 | 37 | Government Amendment No. 8; Knesset Amendment No. 17 | 19 and 12 December 1994 |
| 1568, 112 | 46 | Knesset Amendments No. 21 and No. 22 | 28 February 1996 |
| 1568, 113 | 44 | Government Amendments No. 4 and No. 5 | 28 February 1996 |
| 1582, 234 | 47 | President Amendment No. 3; Knesset Amendment No. 23 | 12 March 1996 |
| 1809, 2 (keyed as 30) | 67 (sampled) | President Amendment No. 6; Knesset Amendment No. 34 | 16 October 2001 |
| 1898, 524 | 72 | President Amendments No. 6 and No. 7 | 28 July 2003 |
| 2715, 636 | 98 | Government Amendment No. 6; Knesset Amendment No. 47 | 30 April 2018 |

The table gives the row numbers of the frame as built. In every group the laws have different Knesset PDFs, listed in `merge-defect.json`. None of the eight rows is challenged, so the defect does not touch the challenged set. Row 37 merged laws passed a week apart and carried the later date, 19 December 1994.

The same key had two smaller faults. Where the page had one digit, it read the publication date as the page: the 2001 laws on page 2 were keyed to "30" from 30 October 2001. And the script ordered laws passed the same day by the text of the gazette reference, so a reference written "1568, page 113" sorted before one written with the Hebrew year first, "1568, page 112".

The correction. The corrected build reads the page as the number after the page marker. It merges two entries only when they also name the same law. It orders same-day rows by issue and page as numbers. Two laws passed the same day and printed on the same page are put in printed order, under a rule fixed before the redraw and recorded in `same-page-order.json`:
- printed order where the issue's table of contents shows it, or a footnote in which one law cites the other's page as an earlier amendment;
- otherwise, for laws amending the same Basic Law, their published amendment numbers;
- otherwise, the order of their bills.

Four pairs were settled by printed evidence, one by amendment numbers and two by bill order. The eighth pair passed on different days. The build also strips a reader's "indirect amendment" suffix from an English title, which had been done by hand on four rows of the frame as built. A check against the frame as built found every law accounted for, no law twice, and no field changed on a row that was not split. Besides the eight splits, two rows of February 1996 moved one place each because of the numeric ordering.

## The redraw

Made on 22 October 2026 from the corrected frame under the same rule in item (ah): every third unchallenged row from the first in chronological order, positions 1, 4, 7 and so on, with no seed and no judgment. It gives 39 rows. By subject: Knesset 15, Government 7, Jerusalem 4, President 3, State Economy 3, Judiciary 2, the budget temporary Basic Laws 2, and one each of the Army, State Comptroller and Referendum Basic Laws. By kind: 29 amendments, 5 enactments, 5 temporary provisions. By decade: two from the 1950s, one from the 1960s, two from the 1970s, four from the 1980s, ten from the 1990s, nine from the 2000s, six from the 2010s and five from the 2020s. Two of the 39 carry a publication date rather than a passage date.

The shift from the first draw:

| | Rows |
|---|---|
| In both draws | 8 |
| In the first draw only, now out of the sample | 28 |
| In the redraw only | 31 |

The eight in both draws are the six rows numbered 1 to 16, which precede the first merged row, and two later laws: Basic Law: The President of the State (Amendment No. 6) of 2001, now alone in its row, and Basic Law: The Judiciary (Amendment No. 2) of 2002. The first draw's verification and coding are kept as records and do not enter the comparison sample except for these eight rows.

## Verification and coding of the redraw

The 31 rows that entered the sample were verified on 22 October 2026 under `verification-sheet-redraw.md` by two docket readers (`verification-redraw-a.json`, `verification-redraw-b.json`). No challenge was found on any row, so all 39 sampled rows stand, each with its search recorded in the `verified`, `verification_search` and `related_cases` columns (`verification-redraw-summary.json`). The readers worked without the judiciary's database, and three rows want a court-database check: Basic Law: Referendum (2014), whose enactment overtook a petition against the earlier referendum statute, and the June and July 2020 amendments to the 2020 State Economy temporary provision, which petitions against a later amendment of the same provision may have reached.

The 39 rows were then coded with all roles. The coding, the adjudication and the one-vote check are described in `research/coding-sample-2026-10-22/README.md`, and the assembled rows are in `codebook/comparison-sample.csv`.
