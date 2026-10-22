# The frame: every law titled Basic Law, 1958 to 2026

Built on 22 October 2026 under the counting rule in the note's change log item (ah): one row per law titled Basic Law as passed by the Knesset at its third reading, however many Basic Laws it amends; new Basic Laws, re-enactments, amendments and temporary provisions alike; ordinary statutes that touch a Basic Law listed separately and not counted. The frame is the population from which the comparison sample of the revised T1 is drawn (issue 9) and the list against which the challenged set of part (a) is completed (issue 8).

## Files

- `basic-law-frame.csv`: the frame, 122 rows in chronological order of passage, with title, passage date and its basis, gazette reference, the Basic Laws the law amends, kind, canonical subject, whether it was challenged and by what case, the `sampled` column from the draw of 22 October 2026, which readers reported it, sources and notes.
- `frame-knesset.json`, `frame-government.json`, `frame-economy-judiciary-rights.json`: the three readers' lists, saved verbatim, each with the ordinary statutes it found, the Wikisource-versus-Nevo discrepancies it recorded, and its deviations.
- `challenges.json`: the challenge reader's list of every Basic Law enactment or amendment attacked before the Court, with the cases it considered and rejected.
- `summary.json`: the counts the build script printed.

## How it was built

Three readers each took a group of Basic Laws and read, for each, the amendment history on Hebrew Wikisource and on Nevo, cross-checking the two and recording every discrepancy; passage dates were read from the "passed by the Knesset on" footnote of the gazette text, reached through Internet Archive captures of the Knesset's PDFs because the Knesset's own sites are geo-blocked (issue 6). The Government reader also used the Knesset's national legislation database as mirrored by Open Knesset, which lists every law bound to each Basic Law with its gazette reference and direct-or-indirect classification; that mirror is a route the other readers did not use and issue 6 now names. A fourth reader compiled the challenges from Chief Justice Hayut's survey in the Reasonableness judgment, Versa, the petitioners' own sites and the Hebrew press. The build script merges the lists on the gazette issue and page, so a law that two readers reported from two Basic Laws' histories is one row, and matches each challenge to a row by subject, passage date and amendment number.

## Counts and checks

| Quantity | Value |
|---|---|
| Rows (laws titled Basic Law, 12 February 1958 to 13 July 2026) | 122 |
| Reader entries merged into them | 139 |
| Rows reported by more than one reader (indirect amendments) | 15 |
| Challenged rows | 14 |
| Unchallenged rows, the population for the draw | 108 |
| Rows whose date is a publication date, not a passage date | 5 |
| Laws through January 2023 | 114 |
| Basic-Law changes through January 2023, counting each Basic Law a law amends | 159 |

Two checks. First, Hayut's opinion in the Reasonableness judgment (para 83) counts 139 changes to Basic Laws from 1958 to January 2023. The frame has 114 laws through that date and 159 changes if each Basic Law a law amends is counted once; the Court's figure lies between the two, and the counting rule behind it is not stated, so the comparison neither confirms nor refutes completeness. It does bound the frame: a count of 114 laws is not far below the Court's, and the frame cannot be missing many laws unless the Court's count is of laws. Second, the three readers' counts agree with Hebrew Wikipedia's amendment counts for every Basic Law, with the discrepancies each recorded.

The one expectation recorded before the draw, that every sampled row has exactly one final-reading vote and no two share one, cannot be checked until the sampled rows are coded; it is carried forward.

## Marked as challenged

Fourteen rows. Seven were in the codebook already: the 1992 Basic Law: Human Dignity and Liberty, the 1994 Freedom of Occupation re-enactment with its override clause, the 2016 and 2020 budget measures, the Nation-State law, and the two 2023 amendments. Seven were not: Basic Law: The Government (Amendment No. 9) of 1999, on the number of ministers (HCJ 5160/99, dismissed); the 2010 amendment extending the biennial budget (HCJ 4908/10 Bar-On, dismissed); Basic Law: The Knesset (Amendment No. 44) of 2016, the expulsion law (HCJ 5744/16 Ben Meir, dismissed); Basic Law: The Government (Amendment No. 8 and Temporary Provision) of 2020, the rotation government (HCJ 2905/20, dismissed); Basic Law: The Government (Amendment No. 11) of 2022, behind the Deri appointment (HCJ 8948/22, the attack on the amendment left undecided); Basic Law: The Judiciary (Amendment No. 4) of 2025, the Judicial Selection Committee (pending); and Basic Law: Torah Study of 13 July 2026 (pending). The 1994 row carries two challenges, Porat and Mitrael. These seven are the candidates for new rows under issue 8, each to be coded under the protocol like any other; nothing from the challenge list is entered in the codebook by hand.

## Gaps a reader should know

- Five rows carry the gazette publication date because no archive capture of the Knesset PDF exists: three 2020 amendments to the State Economy temporary provision and the 2023 Amendments No. 13 and 14 to Basic Law: The State Economy. A passage date is at most days earlier and the ordering is unaffected unless another law passed in between.
- The window from December 2025 to October 2026 could not be checked against the Knesset's own database; Wikisource and Nevo show nothing after Basic Law: The Government (Amendment No. 13) of May 2025 except Basic Law: Torah Study.
- Two laws bear the published title Basic Law: The Knesset (Amendment No. 8), one of 1974 and one of 1981, and none bears No. 5; Nevo renumbers the 1974 law. The frame keeps published titles. Basic Law: The Knesset (Amendment No. 16) is an ordinary statute and is in the separate list.
- The challenge reader did not reach the judgments on the judiciary's site; its classifications for the 1994 Porat petition and the 1999 case are provisional, as its notes say, and the outcome classes it recorded are the reader's, not the protocol's step 4 codings, which the docket reader assigns when a row is coded.
- Eleven ordinary statutes that touched Basic Laws (transitional laws, two convening laws, a fiscal-year law, and the 1994 committee-size law the Knesset numbered as a Basic Law amendment) are in the readers' lists and not in the frame, as the counting rule requires.

## The draw

Made on 22 October 2026 under the rule in item (ah), by the build script's `--draw` flag: every third unchallenged row from the first in chronological order, positions 1, 4, 7 and so on, with no seed and no judgment. It gives 36 rows. By subject: Knesset 11, Government 9, State Economy 7, Freedom of Occupation 2, President 2, and one each of the Army, Jerusalem, State Comptroller, Judiciary and budget temporary Basic Laws. By kind: 26 amendments, 5 temporary provisions, 4 enactments, 1 re-enactment. By decade: two from the 1950s, one from the 1960s, two from the 1970s, four from the 1980s, nine from the 1990s, seven from the 2000s, six from the 2010s and five from the 2020s. Two of the 36 carry a publication date rather than a passage date. The draw is deterministic from the frame, so a corrected frame changes the draw; any row added or removed before the sampled rows are coded shifts every later position, and the change log records any such shift. A sampled row that the docket reader finds to have been challenged moves to part (a) and is not replaced.

## What comes next

The docket reader verifies each of the 36 rows as unchallenged, with the search recorded; then the rows are coded under the coding sheet with the usual roles, outcome Not challenged.
