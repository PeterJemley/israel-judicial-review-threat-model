# History rewrite of 19 November 2026: old and new commit IDs

On 19 November 2026 the repository's history was rewritten at the author's direction, as change log item (bo) of the note records. Every commit received a new ID. The earlier rewrite, of 25 October 2026, is recorded in [history-rewrite-2026-10-25.md](history-rewrite-2026-10-25.md), which is kept as it was; its "New ID" column gives the IDs that this table lists as old.

**What changed.**
- **Authors and committers.** Every commit's author and committer is now the author's name with his GitHub no-reply address. This replaces the language-model assistant's name, and the author's personal email address, on the commits that carried them. Merges made on GitHub keep GitHub as committer.
- **One file removed.** The instructions file kept in the repository for that assistant is removed from every commit; its rules are now kept privately. The 2 commits that changed only that file are dropped.
- **Messages and the ignore rule.** Four commit messages that named that file, or the private notes file, are reworded. The ignore rule for private notes is generalised, in every commit, to `*.local.md`.
- **Unchanged.** Dates and all other files are unchanged.
- **Cited IDs.** The files that cite a commit ID now give the new ID with the old one beside it.

**What it does not reach.** GitHub keeps the original commits behind each pull request's page. Its guidance says that after a rewrite, old commits may stay accessible "Through any pull requests that reference them", and that "GitHub Support won't remove non-sensitive data" (docs.github.com, "Removing sensitive data from a repository", read 19 November 2026).

138 commits before the rewrite; 136 after. Oldest first.

| Old ID | New ID | Commit title | Old ID cited in |
|---|---|---|---|
| fc90f89 | 9938ff5 | Fourth correction of the revised T1 before coding |  |
| e980c21 | cd25d24 | Fifth correction of the revised T1; design stands as reviewed |  |
| 8da7f14 | 712f30a | Bring the codebook README into line with the fifth correction of T1 |  |
| 5cd8c49 | 99a8897 | First run of the revised T1: blind recoding of the nine rows, inconclusive before outcomes |  |
| b0507c2 | 58d10de | Pre-register the situated beneficiary sign before coding it (change log (ac)) | the note, change log (ae) |
| 1f2a9b2 | 73ea0c9 | Code the situated beneficiary sign and rerun the primary analysis (change log (ad)) |  |
| 6bad456 | f8ad3cb | Tighten the closed list for the situated sign before further coding (change log (ae)) |  |
| 636d668 | da8652c | Recode the situated sign under the tightened list: nine of nine expectations met (change log (af)) |  |
| e25962e | 12b74ca | Point the READMEs at issue 6, the Knesset-access blocker, pinned and first in the queue |  |
| 0c0b29d | 23888a5 | Point the README at the research queue (issues 7 to 17) and date the research notes' headers |  |
| 8245e82 | d90bf46 | Settle the Meatrael outcome cell on the judgment: Adverse, 25 November 1996 (change log (ag)) |  |
| 9c0f4af | e82e006 | Settle the counting rule for the unit and the comparison sample (change log (ah)) |  |
| d0e25b7 | d5e8b59 | Build the chronological frame of every law titled Basic Law, 1958 to 2026 (change log (ai)) |  |
| a3bcabf | 97850c6 | Draw the comparison sample: every third unchallenged row from the first, 36 rows (change log (aj)) | analysis/apply_verification.py |
| ee28846 | eec2703 | Verify the 36 sampled rows as unchallenged, with the searches recorded (change log (ak)) |  |
| fe8f4c7 | 88aa1d6 | Coding sheets for the comparison sample: coders, circumstances reader and docket reader, in three batches |  |
| d21f91d | 1d3cebb | Comparison sample, batch 1: both coders' sheets, the circumstances and docket readers' reports, the adjudication sheet; frame titles of four merged rows corrected |  |
| 4866caa | 61da02a | Comparison sample, batch 1 assembled: eight adjudications, twelve rows in codebook/comparison-sample.csv |  |
| f06a10a | 35f1297 | Comparison sample: docket reports for batches 2 and 3, Coder A and the circumstances reader for batch 3 |  |
| bcc636a | da66306 | Comparison sample, batch 3: Coder B's sheet and the adjudication sheet (thirteen disagreements, three interpretive questions) |  |
| de588a0 | b719b5a | Comparison sample, batch 2: Coder B's sheet and the circumstances reader's sheet; frame defect recorded (eight rows merge two laws printed on one gazette page) |  |
| d9dd6d1 | d48d319 | Correct the frame to 130 rows and draw the comparison sample again: 39 rows, 31 new (change log (al)) |  |
| 703492f | 1021e96 | Assembly reads the redraw manifest: coding looked up by batch and filed row number, outcome from the frame's verification |  |
| ec5fdf1 | 5a2b74d | Comparison sample, batch 2: Coder A's sheet (one row, the 2002 Judiciary amendment, stays in the redrawn sample) |  |
| fc6b81b | 837ff7a | Comparison sample, redraw: circumstances sheets for batches 4 and 5, docket sheet for batch 6 | errors list, entry 37; figures/corrections.md |
| 8f156a4 | 3b6d919 | Comparison sample, redraw: circumstances sheet for batch 6 |  |
| 0eb8217 | 952fdeb | Comparison sample, redraw: docket sheet for batch 4 |  |
| d80969b | 0379ed0 | Comparison sample, redraw: docket sheet for batch 5 |  |
| 7dcd1c0 | c3586d6 | Redraw verification, reader B: no challenge found on fifteen rows, two flagged for a court-database check |  |
| 90d570f | 12ed0fe | Comparison sample, redraw: Coder A's sheet for batch 6 |  |
| 1838dcb | 18f8071 | Comparison sample, redraw: Coder B's sheet for batch 6 |  |
| 0d9dfe4 | b5f68a7 | Redraw verification, reader A, applied with reader B: no challenge found on any of the 31 entering rows; all 39 sampled rows verified, none moved to part (a) |  |
| c9170b0 | 4c5e188 | Comparison sample, redraw: Coder A's sheet for batch 4 |  |
| 1a7a770 | a27c057 | Comparison sample, redraw: Coder B's sheet for batch 4 |  |
| b399793 | 5a9d605 | Comparison sample, redraw: Coder B's sheet for batch 5 |  |
| 7c8fb95 | 1f98fa2 | Comparison sample, redraw: Coder A's sheet for batch 5 |  |
| a870518 | ca79673 | Comparison sample, redraw: adjudication sheet (ten coder disagreements, three interpretive questions on situated_beneficiary) |  |
| b88d53e | b9139a6 | Comparison sample, redraw: adjudications filed by batch, all 39 rows assembled, one-vote check (change log (am)) |  |
| cd9ee58 | 60dbb51 | README: how to use the repository, in two sections: to stay informed (plain language) and to check the work (tested commands) |  |
| 008e07f | c101b4a | Note: add a key to its labels, spell out the R- readings where they occur, and mark rivals R1 to R5 as rivals | research/audit-2026-10-25.md |
| 4c40e4e | f18f9f6 | Audit against the evidence: every number traced, a number-check script, change log (an) |  |
| c1184a3 | a993e3b | Record the history rewrite of 25 October 2026: old and new commit IDs, citations updated, change log (ao) |  |
| 8e730e9 | 6e23ed1 | Apply the audit's prose corrections for findings 1, 2, 5, 7, 8 and 9 (change log (ap)) | errors list |
| bfaebf3 | 913dad4 | README: say why Medina rejects the elite critique of the Court (pp. 684-685) |  |
| c9eb28b | e91ff9d | README: tighten the account of Medina's reply to the elite critique to his text (pp. 683-685) | errors list, entries 31 and 35 |
| 3547cba | db52562 | README: open in plain language, explain conjecture, add it to the glossary |  |
| 137f8ad | 118de2d | README: state Threat = Capability x Intent as the basis of the analyses, with each term explained | errors list, entry 32 |
| 050c516 | 3a1de8d | Figures: eight figures of the project, in light and dark versions, with tables, alt text and a record of corrections |  |
| e400000 | 65986a5 | Correct four overstatements found while drawing the figures (change log (aq)) | research/review-2026-10-28-round1.md |
| eb53389 | e1de290 | Adversarial review of the note, round 1 (28 October 2026) |  |
| 5506a75 | 3f4a451 | Apply the round-1 review's four findings that concede the argument (change log (ar)) |  |
| 91392e4 | b5896e6 | Apply the round-1 review's findings 5 to 24, which weaken the argument (change log (as)) |  |
| 90233b4 | 3191fd7 | Apply the round-1 review's findings 25 to 34, which cost attention only (change log (at)) |  |
| 0e9d1b1 | 142376c | Apply the round-1 review's clarity marks (change log (au)) |  |
| bc333f9 | 45158c1 | Research: first verification pass on the round-1 review's external claims |  |
| 3c355ec | dropped | (changed only the assistant's instructions file) |  |
| d27a024 | e1c3e14 | Apply the attested external claims (change log (av)) |  |
| 77c5712 | 9af5959 | Meatrael settled from the supplied translation (change log (aw)) |  |
| 67fcbbe | ea65bc3 | Rosen-Zvi and Yarom's reply read in full (change log (ax)) |  |
| 40d38c2 | cc45e93 | Research: the Knesset's own vote service also ends in July 2021; its main and file sites answer with a bot check |  |
| 06b56b3 | e7979d5 | Correct the Baron passage against p. 682 (change log (ay)); errors entry 73 |  |
| aa60d76 | bfd45a4 | Research: vote extract for the Incapacity amendment's final reading (issue 19) |  |
| 64a438c | 4c81252 | Code the Incapacity row's coalition-only cell from the Knesset record (change log (az); issue 19) |  |
| 0ce2826 | b18a135 | Record the author's decision to keep Noam as a coalition faction (change log (az); results.md fourth addendum) |  |
| 68afe81 | 4f01516 | README queue as of 4 November; codebook README: the 1994 outcome no longer flagged (change log (aw)) |  |
| 082fcf4 | 23b8613 | Issue 15: reading dates and tallies checked against the Knesset's open data (change log (ba)) |  |
| 9f8e699 | 01905cd | Issue 10: sheets and vote extract for the 2025 Judicial Selection amendment's row |  |
| dd2a39c | 2111538 | Issue 10: the docket reader's first attempt, search summaries only, kept as superseded |  |
| a074f62 | 05d298a | Issue 10: the circumstances reader's report (situated_beneficiary No; the enactment commences with the 26th Knesset) |  |
| 34d789a | b2ddb3e | Issue 10: coder A's sheet |  |
| 91c89b4 | 22fdf4f | Issue 10: coder B's sheet (two cells left blank: immediate_effect, coalition_only) |  |
| 0d2b6b0 | 7fa09c9 | Issue 10: the docket reader's report (litigation timing No, provisional; outcome Pending as of 4 November 2026) |  |
| 7566905 | a677e5b | Issue 10: add the March 2025 Judicial Selection amendment as codebook row 10 (change log (bb)) |  |
| ebae1ac | 7091c93 | Research: Harel (Haaretz, 4 Nov 2026) evaluated through the project; predictions recorded before they resolve |  |
| 3342fdf | 0a4161b | Research: Harel evaluation, Claim C settled with the author (p. 685 half counted, exploratory; framing reply; Sohlberg as context) |  |
| 90054a0 | 2ab4a3b | Record the author's decision to leave row 10's coalition-only cell blank (change log (bb)) |  |
| 39f42d7 | 41e6dd3 | Issue 20: script the frame's Basic-Law change counts (change log (bc)) |  |
| b7f9c57 | 226ba78 | Issue 16: the codebook's descriptive columns, in a companion file (change log (bd)) |  |
| a532de3 | 7abe747 | Restate T2 on two axes, target and aim (change log (be); issue 23); confirm the re-enactment rule (bc) |  |
| 6cf933b | 31ee9ec | README up to date as of 5 November: contents, status, Knesset access, the issue queue |  |
| 1fd1aa7 | 0799dbc | Merge pull request #24 from PeterJemley/main-1qm4lu |  |
| 85db832 | aa9bfa8 | Harel evaluation: explain the project's labels inline where they first appear, for a reader new to the project |  |
| a8f9ed9 | 361383f | Merge pull request #25 from PeterJemley/main-1qm4lu |  |
| 4683840 | dropped | (changed only the assistant's instructions file) |  |
| fe9aeeb | 3cff7c3 | Harel evaluation: gloss MKs and Basic Laws, and restate R1, R3 and H1-H4 where they reappear |  |
| 85e09a3 | 61d6808 | Merge pull request #26 from PeterJemley/main-1qm4lu |  |
| a274752 | 5db6eda | Harel evaluation: say at the top that H1-H5 are hypotheses and P1-P5 predictions, with each named |  |
| a292a75 | 10b55d1 | Merge pull request #27 from PeterJemley/main-1qm4lu |  |
| 8b2237e | 5a2d3a1 | Research: the United States and Israel after their 2026 elections, the checks side by side |  |
| 3bb6741 | 5dce35d | Merge pull request #28 from PeterJemley/main-1qm4lu |  |
| 66a1772 | b0403fe | Research: the legal-database run of 5 November 2026, and what it changes |  |
| 28494b4 | 5b4f3ac | Note: quote Roznai, Dixon & Landau and Roznai & Cohen with pages (change log (bf)) |  |
| a506a91 | 174e30e | Merge pull request #29 from PeterJemley/main-1qm4lu |  |
| 33bf10e | 1b2a6f2 | Research: where the Court states its signs of abuse, from the Reasonableness judgment (issue 13) |  |
| 2f0e31f | 22ce199 | Outside-reader corrections to the Harel evaluation, the US-Israel comparison and the README (change log (bg)) |  |
| 77b61d1 | 799c4db | Record the author's decisions on the outside reader's four points (change log (bh)) |  |
| 34d2b9c | 43fa2c5 | Merge pull request #30 from PeterJemley/main-1qm4lu |  |
| 0e3d3b4 | 55fafde | Research: the Incapacity judgment read for the Court's signs of abuse (issues 11 and 13) |  |
| 666a51e | 2a9c2d0 | Note: log the Court's signs as read in the two judgments (change log (bi)); row 8's docket note cites the judgment |  |
| e8c4175 | c404f60 | Merge pull request #31 from PeterJemley/main-1qm4lu |  |
| a0d2ef4 | 2eb3d2a | Note: quote Medina's p. 699 on the Court's guidelines (change log (bj)) |  |
| 0bc443a | e0bcb26 | Merge pull request #32 from PeterJemley/main-1qm4lu |  |
| ec37177 | 663095f | README and note: carry Rosen-Zvi and Yarom's reply and Medina's rejoinder (change log (bk)) |  |
| 51a6d16 | e3444b1 | README: rewrite the passages on the reply and rejoinder after a fidelity review |  |
| f4e842f | 2fa5605 | Merge pull request #35 from PeterJemley/main-1qm4lu |  |
| 3389ecd | 4504c5d | Issue 33: recode sheet, selection rule and expectations, fixed before the coders run | research/recode-2026-11-09-issue33/results.md |
| f620182 | 3aa6516 | Issue 33: script reporting T1 and the comparison sample with the recoded rows beside the original codes |  |
| f84e1fb | 5cf3284 | Issue 33: coder A's return |  |
| 20154ca | efb3d0b | Issue 33: coder B's return |  |
| 80db80c | ec0b376 | Issue 33: results of the sensitivity recode (change log (bl)); exploratory |  |
| 9fd6479 | 8df0079 | Issue 33: record the author's decision to keep the primary codes |  |
| 46e8830 | e21cda3 | Merge pull request #36 from PeterJemley/main-1qm4lu |  |
| 5ab6cda | 69e697f | Issue 34: qualifying rule, Arab-party definition and expectations, fixed before any roll call is read | research/variant-2026-11-09-issue34/results.md |
| 949dd94 | 1f69255 | Issue 34: results of the Arab-party variant of the cross-party sign (change log (bm)); exploratory |  |
| 4377c03 | 8f09f52 | Ignore the private per-person notes file |  |
| 1b255cc | 6ae7b2e | Issue 34: record the author's decision to keep the primary sign |  |
| 9685dd3 | c391cf3 | Merge pull request #37 from PeterJemley/main-1qm4lu |  |
| e35820e | 7c88bfd | Issue 13: the alternative rule read from the judgments, with expectations, fixed before it is computed | research/revision-2026-11-09-issue13/results.md |
| 049bb91 | a2579ca | Issue 13: an alternative prediction rule read from the judgments (change log (bn)); exploratory |  |
| f7cdb41 | 97d3691 | Issue 13: record the author's decision to keep the 22 October table as the primary rule |  |
| 614100c | 0c26e2d | Merge pull request #38 from PeterJemley/main-1qm4lu |  |
| 924fe99 | 4c7e8fd | Check-in of 10 November: record P1 (refuted), progress on E1, and the Judicial Selection amendment's start |  |
| 050b955 | ef8b520 | Check-in of 10 November: corrections after an outside reader's review |  |
| 7c9958f | 66b645d | Check-in of 10 November: P1 recorded, E1 progress, the Judicial Selection amendment's start (#39) |  |
| 3b124ef | 4992e6d | Three constitutional settlements: a comparative research note, and the author's Bickel summary with its provenance |  |
| 1dee687 | b0c9059 | Three settlements and Bickel provenance: corrections after an outside reader's review |  |
| b0a8aa7 | 83be9af | Three constitutional settlements, and the author's Bickel summary with its provenance (#42) |  |
| 09abab6 | 0831f55 | Three settlements: quote the four Inner Temple passages the author checked against the video |  |
| 126ba19 | 4c6658d | Three settlements: quote the four Inner Temple passages checked against the video (#43) |  |
| c2f3f62 | 0646ef5 | Check-in of 17 November: the speaker vote was on the agenda but not yet held |  |
| 5ed71c5 | 260a786 | Check-in of 17 November: corrections after an outside reader's review |  |
| 7651f57 | 33eddfc | Check-in of 17 November: the speaker vote on the agenda, no result yet (#44) |  |
| 297d23e | 095f06d | E1 supported: Kahana elected Knesset speaker on 17 November, 66 to 52 |  |
| ef3fd06 | dc1e5ad | E1 result: corrections after an outside reader's review |  |
| bee1ef2 | c3f31fb | E1 supported: Kahana elected Knesset speaker on 17 November, 66 to 52 (#45) |  |
| 70e84ff | 44a5c8d | Check of 19 November: the speaker roll calls, the repeal bills, and P2 to P4 so far |  |
| 485f22d | bb9074d | Check of 19 November: corrections after an outside reader's review |  |
| 5b16851 | b7f44e7 | Check of 19 November: speaker roll calls, repeal bills, P2 to P4 so far (#46) |  |
