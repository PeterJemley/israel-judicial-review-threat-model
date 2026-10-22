# Blind recoding of the nine rows under T1 as revised on 2026-10-22: results

Date of run: 22 October 2026. Protocol: the note's section "T1 as revised on 2026-10-22". Files in this folder: `coding-sheet.md` (what the coders saw), `coder-A.json` and `coder-B.json` (their sheets, saved verbatim), `agreement.json` (per-variable agreement), `adjudications.json` (the eleven settled disagreements with sources), `docket.json` (litigation timing and outcomes with judgment dates), `assembly-summary.json` (the pre-outcome checks as the code printed them). The assembled table is `codebook/m4-codebook.csv`; the table it replaces is kept as `codebook/m4-codebook-illustrative-2026-10-22.csv`. The code is in `analysis/`.

## Roles, and what blinding was achieved

Four roles were filled by four separate language-model agents, each run with only the material its role allows: two coders working from the coding sheet (enactment titles, dates, text locations and vote extracts, with the forbidden-source rules), an adjudicator who settled coder disagreements from the same sources, and a docket reader who coded litigation timing and outcomes from judgments and dockets. The adjudicator and the docket reader ran at the same time in separate sessions and did not see each other's work. The coders did not see each other's sheets, the note, this repository, or any judgment. The author of the note did not hold any of the four roles.

Three limits on that blinding are disclosed. First, the coders are language models that have read widely about these enactments; withholding documents does not remove what they already know, and the note says so for the notorious rows (Nation-State, Incapacity, Reasonableness). Both coders reported seeing court outcomes in web-search result snippets for enactments 2, 5, 6, 8 and 9 and reported not opening those pages. Second, the Knesset's own sites were geo-blocked for every role, so the coders used the sources the sheet allows in that case: the NYU Faculty Digital Archive's mirror of the Knesset record (Divrei HaKnesset), Hebrew Wikisource and Nevo copies of the gazette text, press reports of tallies and readings, and encyclopedia articles on each government's composition; the adjudicator added Internet Archive captures of two Knesset gazette PDFs. Third, the sequence in step 7 of the protocol was not kept exactly: the docket reader delivered litigation timing, outcomes and judgment dates in one report, so the orchestrator who assembled the table had seen the outcomes before the detectability check was computed. The check itself is computed by code from N, K and the fixed predictions, and its result does not depend on which rows are Adverse, so the lapse could not change the verdict; it is a deviation all the same and is logged in the note (change log (ab)).

## Agreement between the coders

| Variable | Kappa | Agree | Disagreements (enactment) |
|---|---|---|---|
| temporary_provision | 1.000 | 9 of 9 | none |
| coalition_only | 0.830 | 8 of 9 | 8 |
| direction | 0.812 | 8 of 9 | 8 |
| deviation_tier | 0.757 | 8 of 9 | 2 |
| named_beneficiary | 0.743 | 8 of 9 | 2 |
| targets_judiciary | 0.609 | 8 of 9 | 4 |
| expedited | 0.571 | 7 of 9 | 2, 3 |
| scope | 0.400 | 7 of 9 | 2, 8 |
| immediate_effect | 0.000 | 8 of 9 | 8 |
| required_majority_met | 0.000 | 8 of 9 | 3 |

The two zero kappas are degenerate, not low agreement: on `immediate_effect` both coders gave Yes on every row they coded and differed only on enactment 8, which one coder left blank; on `required_majority_met` only enactments 2 and 3 take a value and one coder left 3 blank. Kappa is undefined or zero when one coder's marginal has a single category, and the raw agreement is the better reading for those two. Several disagreements were one coder's blank against the other's value, where one coder found the record and the other did not.

## Adjudications

Eleven cells were settled. Enactment 2 (the 1969 financing law): `named_beneficiary` No, `expedited` Yes (first reading between 22 January and 18 February 1969, final vote 19 February), `scope` No, `deviation_tier` Limited, all from the original gazette text (Internet Archive capture of the Knesset PDF) and the Knesset record for January and February 1969. Enactment 3 (the 1969 ratification law): `expedited` Yes (tabled for first reading 8 July 1969, passed 15 July) and `required_majority_met` Yes, on the record of the third reading: 68 for, 8 against, 5 abstaining. Enactment 4 (the 1994 override clause): `targets_judiciary` No, because the clause's subject is the validity of statutes under stated conditions and names no court. Enactment 8 (the 2023 Incapacity amendment): `immediate_effect` Yes by absence of a clause, on the gazette text (the deferral label on Wikisource is an editorial note about a later event, not part of the enactment); `coalition_only` blank, because press reports give the tally (61 to 47) with conflicting lists of absentees and no faction breakdown of the votes in favor, and the sheet requires a blank when the record is unavailable; `scope` No, because the text redefines the incapacity determination rather than removing it and supplies its own mechanisms; `direction` Neutral, because the text and the explanatory notes as quoted engage none of the three axes, the clause barring judicial review having been dropped before passage.

## The recoded table

| Row | Enactment | Beneficiary | Immediate | Coalition-only | Expedited | Scope | Temporary | Judiciary | Tier | Direction | Litigation pending | Outcome | Judgment |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Human Dignity and Liberty 1992 | No | Yes | blank | No | No | No | No | Entrenches | Liberal | No | Not adverse | 1995-11-09 |
| 2 | Elections financing law 1969 | No | Yes | blank | Yes | No | Yes | No | Limited | Neutral | No | Adverse | 1969-07-03 |
| 3 | Confirmation of validity law 1969 | No | Yes | blank | Yes | No | Yes | No | Limited | Neutral | No | Not adverse | 1977; 1981-07-28 |
| 4 | Freedom of Occupation override 1994 | No | Yes | No | Yes | No | No | No | Limited | Illiberal | No | Not adverse | 1996-11-25 |
| 5 | Two-year budget 2016 | Yes | Yes | No | Yes | No | Yes | No | Limited | Neutral | No | Adverse | 2017-09-06 |
| 6 | Budget deadline 2020 | Yes | Yes | Yes | Yes | No | Yes | No | Limited | Neutral | No | Adverse | 2021-05-23 |
| 7 | Nation-State 2018 | No | Yes | Yes | No | No | No | No | Limited | Illiberal | No | Adverse | 2021-07-08 |
| 8 | Incapacity 2023 | No | Yes | blank | Yes | No | No | No | Limited | Neutral | Yes | Adverse | 2024-01-03 |
| 9 | Reasonableness 2023 | No | Yes | Yes | Yes | Yes | No | Yes | Sharp | Illiberal | Yes | Adverse | 2024-01-01 |

`required_majority_met` is Yes for row 3 and blank for row 2 (the record shows a voice vote with no count). Every cell's source and supporting quotation is in the JSON files; the CSV's `provenance` column says for each predictor whether the coders agreed, the adjudicator settled it, or both left it blank.

Four rows are excluded from the primary analysis as uncoded because `coalition_only` is blank: 1992 (no faction breakdown of the 17 March 1992 vote found), the two 1969 statutes (no per-member record; the 1969 statutes are Article 4 rows in any case), and Incapacity 2023 (tally only). The Open Knesset vote tables that supplied the 2016, 2018 and 2020 breakdowns cover October 2003 to July 2021, so the 2023 rows need the Knesset's own site or a press source that lists the votes by member.

## Classification under the prediction table

| Row | F | Tier | Coalition-only | Decision-rule prediction | Elite-interest prediction | Class | Group |
|---|---|---|---|---|---|---|---|
| 4 | 2 | Limited | No | Undetermined | Adverse | undetermined | table row 6 |
| 5 | 3 | Limited | No | Undetermined | Not adverse | undetermined | table row 6 |
| 6 | 4 | Limited | Yes | Adverse | Not adverse | discordant | purpose-driven |
| 7 | 2 | Limited | Yes | Adverse | Adverse | concordant | tier-and-support-driven |
| 9 | 3 | Sharp | Yes | Adverse | Adverse | concordant | content-driven |

The author's expectations recorded in step 12 of the protocol: 2020 Neutral (met), Reasonableness Illiberal (met), Incapacity turning on whether removing the Court's role is read as narrowing judicial review (the coders read the enacted text as engaging no court and coded Neutral; the row is uncoded for other reasons). The 2016 row is Undetermined, as step 12 said it would be.

## Pre-outcome checks (steps 7 and 9)

Configuration: N = 5 primary rows coded, K = 4 Adverse, D_A = 1 discordant row predicted Adverse by the decision rule, D_N = 0.

- Minimum of six discordant rows: not met (one).
- Attainable S: from −1 to 1; null mean 0.6; two-sided p at the largest attainable S is 1.0 and at the smallest is 0.4. Neither a Supported nor a Refuted result is detectable.
- Verdict declared before outcomes, by code: **Inconclusive**.
- Step 9: exact type-one rate of the decision rule under the null is 0; the shuffle check on 1000 datasets returned 0.0, within 0.02 of the exact rate. The implementation check passes, trivially, because no result can reach 0.05 on this configuration.

## Exploratory results, reported because step 7 failed

- Observed S = 1: the single discordant row, the 2020 budget-deadline amendment (all four signs present, Neutral direction), had an Adverse outcome, as the decision rule predicted and the elite-interest rival did not. Two-sided p = 1.0. One row is one row.
- Step 10 (groups): the one discordant row is purpose-driven; the content-driven and tier-and-support-driven groups are empty.
- Step 11 (variant table, F of 3 or more as the presumption of abuse): the 2016 budget row becomes a second discordant row, also predicted Adverse and also Adverse in fact; D_A = 2, D_N = 0, attainable S from 0 to 2, p at the extremes 1.0 and 0.8; still undetectable; observed S = 2.
- Step 12 (notorious rows excluded): removing rows 7, 8 and 9 leaves the 1994, 2016 and 2020 rows; the configuration is N = 3, K = 2, D_A = 1, and the verdict is the same. Every row in the table was coded before the revision, so the protocol's "every row coded before this revision excluded" analysis has no rows.
- Step 15 (R5): the weak form's test needs at least four rows in each group; the judiciary-narrowing group has one row (Reasonableness), so the test is not run. The strong form, that the Court intervenes only against enactments that narrow the judiciary, is contradicted on the blind-coded subjects: the 1969 financing law, the 2016 and 2020 budget measures and the 2018 Nation-State law all drew interventions and all are coded `targets_judiciary` No.
- Sensitivity on the judgment-call predictors (each flipped in turn): on row 6, Neutral to Illiberal makes it concordant and Yes to No on `coalition_only` makes it undetermined, and either flip leaves no discordant row at all; on row 4, Limited to Sharp makes it Adverse-predicted and concordant with its Illiberal direction; on row 5, Limited to Sharp makes it Adverse-predicted and discordant with its Neutral direction, raising the count to two. No flip raises the discordant count to six, so no flip changes the verdict.

## Outcome cells flagged by the docket reader

- Row 7, Nation-State: coded Adverse under the protocol's rule that an enactment upheld and narrowed by interpretation is Adverse (HCJ 5555/18, 10 to 1, interpreted ss. 1, 4 and 7 consistently with the other Basic Laws). The case is usually reported as upholding the law; a reader who does not treat harmonising interpretation as narrowing would code Not adverse. The row is concordant, so the flip changes K from 4 to 3 and not S; the verdict is unchanged.
- Row 4, Freedom of Occupation override: coded Not adverse by the docket reader, who could not verify from the sources reached whether the Court qualified the override's shield. Medina reports that it did: the Court ruled that a law enacted under the override would still be subject to scrutiny under Basic Law: Human Dignity and Liberty, which "effectively limited the override clause" (Medina, 2026, pp. 697–698). Under the protocol's precedence rule that is a narrowing by interpretation and the cell should read Adverse. The cell is left as the docket reader coded it and flagged, because changing an outcome after assembly on the author's reading of the article is the move the protocol forbids; it is referred to the docket reader for a second look at HCJ 4676/94 itself. The row is undetermined, so either value leaves S unchanged; with Adverse, K becomes 5 and the null distribution degenerates.

## What this run establishes

Under the pre-registered rule, the first run of the revised T1 is Inconclusive, declared before outcomes on the basis of one discordant row against a minimum of six. Nothing in the exploratory results is evidence for or against Claim C. What the run does establish is procedural: the protocol can be executed end to end by separate roles from legislative records with the Knesset's sites blocked; two independent coders agree on most cells and their disagreements are mostly one coder finding a record the other did not; and the form signs and direction do not move together perfectly even in nine rows, since the one row with all four signs is Neutral in direction. The record T1 needs is the full unit of the protocol's step 1, and the next piece of work is the comparison sample and the remaining challenged Basic Law amendments, not more analysis of these nine.

## Issues touched by this run

- Issue 4 (replace Hebrew Wikipedia and Wikisource lines with gazette or press sources): the 1969 ratification law's tally (68 to 8 to 5) and passage date (15 July 1969) are now from the Knesset record; the 1969 financing law's text is now from the gazette; the 1996 Meatrael outcome still rests on Hebrew Wikipedia and press.
- Issue 5 (the Incapacity deadline): resolved in HCJ 2412/23 itself, as read by the docket reader: the attorney general's response was due 12 March 2023; on 13 March the Court extended the deadline to 26 March; the amendment passed on 23 March; on 29 March the Court struck the incapacity petitions. Both dates in the research notes were right.
- Issue 2 (the Resler judgment): still unread; the docket reader coded row 3 from the Court's 1981 account and Klinghoffer (1983).
