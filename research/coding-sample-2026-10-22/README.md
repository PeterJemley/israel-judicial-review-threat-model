# Coding of the comparison sample, 22 October 2026

This folder holds the blind coding of the comparison sample, part (c) of the unit in the revised T1 (issue 9). The sample is every third unchallenged law titled Basic Law, in chronological order, from the frame in `research/frame`. Its result is assembled into `codebook/comparison-sample.csv`. The sample is not in T1's primary analysis. It serves the exploratory secondary analysis of the challenge stage (the note's T1 section, step 14), and it shows what an unchallenged enactment looks like on the same columns as the challenged ones.

## Two draws, six batches

The sample was drawn twice on 22 October 2026 (the note's change log items (aj) and (al)).

- Batches 1 to 3 coded the first draw, 36 rows from the frame as built. Their files use that frame's row numbers. During batch 2 a coder found that one sampled row held two laws, which exposed the defect described in `research/frame/README.md`.
- The frame was corrected and the sample drawn again: 39 rows. Eight rows are in both draws. Batches 4 to 6 coded the 31 rows that entered the sample, and recoded the 2001 President amendment as a single law. Their files use the corrected frame's row numbers.
- `rows-redraw.json` lists the 39 rows of the sample in force. For each row it gives the batch whose files hold its coding and the number under which that batch filed it. Six rows keep their batch 1 coding. One row, Basic Law: The Judiciary (Amendment No. 2) of 2002, keeps its batch 2 coding under the first draw's number 70. `rows.json` is the first draw's manifest, kept as a record.

## Roles and files

Each row was coded by five roles, each in a separate agent working from one sheet and barred from every other file here.

- Two coders, A and B, coded nine predictors and the final-vote record blind to outcomes: `coder-A-b{n}.json`, `coder-B-b{n}.json`, from `coding-sheet.md` (first draw) or `coding-sheet-redraw.md`.
- A circumstances reader coded `situated_beneficiary` from the closed list (ae), as clarified by (af): `circumstances-b{n}.json`, from `circumstances-sheet.md` or `circumstances-sheet-redraw.md`.
- A docket reader, not blind, coded whether litigation on the subject was pending at passage: `docket-b{n}.json`, from `docket-sheet.md` or `docket-sheet-redraw.md`. For the redraw the outcome was attached separately, from the verification of the sampled rows recorded in the frame.
- An adjudicator settled the coders' disagreements and the interpretive questions on `situated_beneficiary`, under the same prohibitions as the coders. Its sheets are `adjudication-b1.md`, `adjudication-b3.md` and `adjudication-redraw.md`. The redraw adjudicator's output is `adjudications-redraw-all.json`. `analysis/split_adjudication.py` filed it by batch as `adjudications-b2.json`, `-b4.json`, `-b5.json` and `-b6.json`.
- `vote-extracts-redraw.json` holds the candidate final-reading votes the coders were given for laws passed from October 2003 on. `analysis/vote_extracts.py` drew them from the Knesset's plenum-vote tables as mirrored by Open Knesset.

`analysis/assemble_sample.py` assembles the sample from these files. Its summary is `assembly-summary-redraw.json`. The first draw's batch 2 and 3 files and its batch 3 adjudication are records of rows that left the sample.

## Results

All 39 rows were coded and every disagreement was settled. All 39 outcomes are Not challenged, from the verification recorded in the frame.

Agreement between the two coders before adjudication, over the 39 rows:

| Variable | Rows agreed | Kappa |
|---|---|---|
| named_beneficiary | 38 | 0.79 |
| immediate_effect | 38 | 0.79 |
| coalition_only | 38 | 0.95 |
| expedited | 37 | 0.92 |
| scope | 38 | 0.00 |
| temporary_provision | 39 | 1.00 |
| targets_judiciary | 39 | 1.00 |
| deviation_tier | 34 | 0.80 |
| direction | 38 | 0.79 |

The kappa of zero for `scope` reflects one disagreement where 38 of 39 cells are No; agreement was 38 of 39.

Coded values after adjudication:

| Variable | Values |
|---|---|
| situated_beneficiary | Yes 3, No 36 |
| named_beneficiary | Yes 3, No 36 |
| immediate_effect | Yes 36, Deferred 3 |
| coalition_only | Yes 5, No 8, blank 26 |
| expedited | Yes 18, No 13, blank 8 |
| deviation_tier | None 17, Entrenches 10, Limited 12, Sharp 0 |
| direction | Neutral 36, Liberal 2, Illiberal 1 |
| litigation_timing | Yes 4, No 35 |

The three rows Yes on both beneficiary signs are Basic Law: The Government (Amendment No. 5) of 1991, the 2009 budget temporary provision and the 2015 budget extension. The adjudicator held that the 1991 law's transitional clause exempts the sitting government alone from a new limit (item 4). It held that the 2009 and 2015 laws each move a dissolution deadline then running against the sitting government (item 3). It also held that a provision keyed to a budget year is not the sitting government's own measure under item 4, so the three 2020 budget laws the reader had coded Yes are No.

`coalition_only` is blank on 26 rows because no surviving record names the voters at the final reading. Before the plenum-vote tables begin in October 2003, only the 1958 and 1980 rows have a coded value. F, the count of the four signs, needs all four coded, so it is computable on 12 rows: F = 1 on one row, F = 2 on nine and F = 3 on two. On three of those rows the decision rule predicts Adverse and the Court's stated signs predict Not adverse: the 2015 budget extension, the 2018 war-powers amendment and the June 2020 State Economy amendment. These laws were never challenged, so the prediction is not tested here.

The docket reader's four Yes codes on litigation timing are the 2000 Jerusalem amendment, the 2014 Referendum Basic Law, the 2016 Knesset Amendment No. 45 and the December 2020 State Economy law. The readers flag the 2000 and 2016 codes as uncertain. The 2000 code rests on a filing date inferred from a docket number. The 2016 code rests on a court proceeding the record does not name.

## The one-vote check

Change log item (ah) expected each sampled row to have exactly one final-reading vote, with no two rows sharing one.

| | Rows |
|---|---|
| Final vote found | 19 |
| Final vote found and recorded as approving this law alone | 18 |
| Final vote found, coverage of other laws not established (1980 Jerusalem law) | 1 |
| No final-reading record found | 20 |
| Vote shared by two rows, or one vote approving two laws | 0 |

The expectation is not refuted on the 19 rows where a vote was found, and it is untested on the other 20. Those 20 passed between 1959 and 2003, and none has an archived plenum record. Where a companion law passed the same day, the coders found it had its own vote wherever a record survives: in 1958, 2006, 2013, 2018 and December 2020. For the two pairs printed on one gazette page in 2001 and 2003, no record survives, though the Knesset's agenda lists the laws as separate items.

## Limits

- Every coder, reader and adjudicator worked without the Knesset's own websites, which are geo-blocked (issue 6). Gazette texts came from Internet Archive captures, and votes and agenda dates from the Open Knesset mirror. Explanatory notes were reachable for only a few rows.
- The verification readers searched without the judiciary's database. Three rows want a court-database check: the 2014 Referendum Basic Law and the June and July 2020 State Economy amendments.
- The coders exhausted a shared web-search budget, so press searches for pre-2003 tallies were few.
