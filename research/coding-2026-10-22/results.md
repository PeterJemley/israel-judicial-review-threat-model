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

*As first run. Row 4's outcome was later recoded Adverse (third addendum); the situated beneficiary values are in the addenda (pointer added 25 October 2026, change log (ap)).*

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

*As first run, with the named beneficiary in F. With the situated beneficiary, which the primary analysis now uses, Reasonableness has F of 4 and moves to the purpose-driven group with the same prediction, and the 1994 override keeps F of 2 (second addendum). No row's class changes (pointer added 25 October 2026, change log (ap)).*

| Row | F | Tier | Coalition-only | Decision-rule prediction | Elite-interest prediction | Class | Group |
|---|---|---|---|---|---|---|---|
| 4 | 2 | Limited | No | Undetermined | Adverse | undetermined | table row 6 |
| 5 | 3 | Limited | No | Undetermined | Not adverse | undetermined | table row 6 |
| 6 | 4 | Limited | Yes | Adverse | Not adverse | discordant | purpose-driven |
| 7 | 2 | Limited | Yes | Adverse | Adverse | concordant | tier-and-support-driven |
| 9 | 3 | Sharp | Yes | Adverse | Adverse | concordant | content-driven |

The author's expectations recorded in step 12 of the protocol: 2020 Neutral (met), Reasonableness Illiberal (met), Incapacity turning on whether removing the Court's role is read as narrowing judicial review (the coders read the enacted text as engaging no court and coded Neutral; the row is uncoded for other reasons). The 2016 row is Undetermined, as step 12 said it would be.

## Pre-outcome checks (steps 7 and 9)

*As first run. After row 4 was recoded Adverse, K is 5 of 5, S cannot vary, and p is 1.0 at both extremes; the verdict is unchanged (third addendum; pointer added 25 October 2026, change log (ap)).*

Configuration: N = 5 primary rows coded, K = 4 Adverse, D_A = 1 discordant row predicted Adverse by the decision rule, D_N = 0.

- Minimum of six discordant rows: not met (one).
- Attainable S: from −1 to 1; null mean 0.6; two-sided p at the largest attainable S is 1.0 and at the smallest is 0.4. Neither a Supported nor a Refuted result is detectable.
- Verdict declared before outcomes, by code: **Inconclusive**.
- Step 9: exact type-one rate of the decision rule under the null is 0; the shuffle check on 1000 datasets returned 0.0, within 0.02 of the exact rate. The implementation check passes, trivially, because no result can reach 0.05 on this configuration.

## Exploratory results, reported because step 7 failed

*As first run. After row 4 was recoded Adverse (third addendum), the step 12 configuration is N = 3, K = 3, and the verdict is the same (pointer added 25 October 2026, change log (ap)).*

- Observed S = 1: the single discordant row, the 2020 budget-deadline amendment (all four signs present, Neutral direction), had an Adverse outcome, as the decision rule predicted and the elite-interest rival did not. Two-sided p = 1.0. One row is one row.
- Step 10 (groups): the one discordant row is purpose-driven; the content-driven and tier-and-support-driven groups are empty.
- Step 11 (variant table, F of 3 or more as the presumption of abuse): the 2016 budget row becomes a second discordant row, also predicted Adverse and also Adverse in fact; D_A = 2, D_N = 0, attainable S from 0 to 2, p at the extremes 1.0 and 0.8; still undetectable; observed S = 2.
- Step 12 (notorious rows excluded): removing rows 7, 8 and 9 leaves the 1994, 2016 and 2020 rows; the configuration is N = 3, K = 2, D_A = 1, and the verdict is the same. Every row in the table was coded before the revision, so the protocol's "every row coded before this revision excluded" analysis has no rows.
- Step 15 (rival R5): the weak form's test needs at least four rows in each group; the judiciary-narrowing group has one row (Reasonableness), so the test is not run. The strong form, that the Court intervenes only against enactments that narrow the judiciary, is contradicted on the blind-coded subjects: the 1969 financing law, the 2016 and 2020 budget measures and the 2018 Nation-State law all drew interventions and all are coded `targets_judiciary` No.
- Sensitivity on the judgment-call predictors (each flipped in turn): on row 6, Neutral to Illiberal makes it concordant and Yes to No on `coalition_only` makes it undetermined, and either flip leaves no discordant row at all; on row 4, Limited to Sharp makes it Adverse-predicted and concordant with its Illiberal direction; on row 5, Limited to Sharp makes it Adverse-predicted and discordant with its Neutral direction, raising the count to two. No flip raises the discordant count to six, so no flip changes the verdict.

## Outcome cells flagged by the docket reader

- Row 7, Nation-State: coded Adverse under the protocol's rule that an enactment upheld and narrowed by interpretation is Adverse (HCJ 5555/18, 10 to 1, interpreted ss. 1, 4 and 7 consistently with the other Basic Laws). The case is usually reported as upholding the law; a reader who does not treat harmonising interpretation as narrowing would code Not adverse. The row is concordant, so the flip changes K from 4 to 3 and not S; the verdict is unchanged.
- Row 4, Freedom of Occupation override: coded Not adverse by the docket reader, who could not verify from the sources reached whether the Court qualified the override's shield. Medina reports that it did: the Court ruled that a law enacted under the override would still be subject to scrutiny under Basic Law: Human Dignity and Liberty, which "effectively limited the override clause" (Medina, 2026, pp. 697–698). Under the protocol's precedence rule that is a narrowing by interpretation and the cell should read Adverse. The cell is left as the docket reader coded it and flagged, because changing an outcome after assembly on the author's reading of the article is the move the protocol forbids; it is referred to the docket reader for a second look at HCJ 4676/94 itself. The row is undetermined, so either value leaves S unchanged; with Adverse, K becomes 5 and the null distribution degenerates.

## What this run establishes

Under the pre-registered rule, the first run of the revised T1 is Inconclusive, declared before outcomes on the basis of one discordant row against a minimum of six. Nothing in the exploratory results is evidence for or against Claim C. What the run does establish is procedural: the protocol can be executed end to end by separate roles from legislative records with the Knesset's sites blocked; two independent coders agree on most cells and their disagreements are mostly one coder finding a record the other did not; and the form signs and direction do not move together perfectly even in nine rows, since the one row with all four signs is Neutral in direction. (With the situated beneficiary of the addenda, Reasonableness also has all four signs; it is Illiberal, so the 2020 row is still the only one with all four signs and a Neutral direction. Note added 25 October 2026, change log (ap).) The record T1 needs is the full unit of the protocol's step 1, and the next piece of work is the comparison sample and the remaining challenged Basic Law amendments, not more analysis of these nine.

## Issues touched by this run

- Issue 4 (replace Hebrew Wikipedia and Wikisource lines with gazette or press sources): the 1969 ratification law's tally (68 to 8 to 5) and passage date (15 July 1969) are now from the Knesset record; the 1969 financing law's text is now from the gazette; the 1996 Meatrael outcome still rests on Hebrew Wikipedia and press.
- Issue 5 (the Incapacity deadline): resolved in HCJ 2412/23 itself, as read by the docket reader: the attorney general's response was due 12 March 2023; on 13 March the Court extended the deadline to 26 March; the amendment passed on 23 March; on 29 March the Court struck the incapacity petitions. Both dates in the research notes were right.
- Issue 2 (the Resler judgment): still unread; the docket reader coded row 3 from the Court's 1981 account and Klinghoffer (1983).

## Addendum, later on 22 October 2026: the situated beneficiary sign

After the run above, the beneficiary sign was split in two (note, change log item (ac)): `named_beneficiary` stays as the coders coded it from the text and explanatory notes, and `situated_beneficiary` was added, coded by a circumstances reader from a closed list of facts dated no later than the day of passage, without any outcome or judgment. The sheet is `circumstances-sheet.md`; the reader's report is `circumstances.json`, saved verbatim. (This first reader's report is now kept as `circumstances-ac.json`, and `circumstances.json` holds the second reader's, as change log (af) records. Note added 25 October 2026, change log (ap).) The situated sign enters F in the primary analysis; the text sign enters F in the pre-registered secondary analysis 11a. The expectations for the nine rows were recorded in item (ac) before the reader ran.

### The reader's values against the recorded expectations

| Row | Enactment | Expected | Coded | Admissible fact the reader relied on |
|---|---|---|---|---|
| 1 | Human Dignity and Liberty 1992 | No | No | none found; connection would rest on motive |
| 2 | Elections financing law 1969 | No | **Yes** | item 4: the law names the factions of the outgoing Knesset and the single election of 28 October 1969 |
| 3 | Confirmation of validity law 1969 | No | **Yes** | item 4: a one-off validation of three named laws |
| 4 | Freedom of Occupation override 1994 | No | **Yes** | item 3 and item 4: section 10, a temporary provision, re-sets the two-year saving of prior legislation; the override clause gives override laws a four-year expiry |
| 5 | Two-year budget 2016 | Yes | Yes | item 4: a temporary provision confined to the 2017 and 2018 budgets |
| 6 | Budget deadline 2020 | Yes | Yes | item 3: the deadline of 25 August 2020 moved to 23 December 2020 |
| 7 | Nation-State 2018 | No | No | none found; only petitions filed after passage |
| 8 | Incapacity 2023 | Yes | Yes | item 1: incapacity petitions filed 24 January and 9 February 2023; item 2: the attorney general's letter of 1 February 2023 |
| 9 | Reasonableness 2023 | Yes | Yes | item 2: the attorney general's position of 4 January 2023 that the Deri appointment was outside the bounds of reasonableness, with the amendment expressly covering appointment decisions |

Six of nine expectations met; three missed, all three on the list's temporal items, a moved deadline or a single-instance or sunset clause, read as the rule is written. The misses stand as coded and are not re-scored. What they show is a defect in the rule as written rather than in the reader's application of it: items 3 and 4 are satisfied by any dated or temporary clause, whether or not the person or government whose position changes is identifiable as distinct from everyone else the clause touches, and "the sitting government" admits a reading on which every incumbent faction, or any government relying on existing law, counts. The rule as intended required a position altered for the sitting government or an officeholder specifically, in a way successors or other actors would not share. A tightened list is recorded in the note as a candidate for a later run and is not applied to this one.

### Effect on the analysis

With the situated sign in F, row 4 moves from F of 2 to 3 and stays Undetermined; row 9 moves from F of 3 to 4 and from the content-driven to the purpose-driven group with the same prediction; rows 5, 6 and 7 are unchanged; rows 1, 2, 3 and 8 remain uncoded in the primary analysis or outside it. The configuration is again N = 5, K = 4, D_A = 1, D_N = 0; the verdict before outcomes is again Inconclusive; the secondary analysis 11a reproduces the first run exactly. The two analyses classify no row differently; they differ in the group label of one row and in F for two.

### Disclosures for this pass

The reader is a language model and reported court outcomes reaching it through search-result summaries for every enactment but the 2016 budget, none opened. It read pages through a fetch tool that summarises text, instructed to omit decisions. It did not consult the judiciary's docket. For the 1969 ratification law and the 1994 override it could not establish a pending proceeding from any permitted source without reading decision text, so those codings rest on the enactments' own clauses alone. Its sources for the 2023 rows are dated press reports from before passage; the 2023 Incapacity coding also cites the indictment of January 2020 as a pending proceeding concerning the prime minister.

## Second addendum, 22 October 2026: the situated sign under the tightened list

The closed list was tightened (note, change log item (ae)) and a fresh circumstances reader, with no knowledge of the first reader's work, coded the nine rows under it from the amended sheet. Its report is `circumstances.json`; the first reader's report under the earlier list is kept as `circumstances-ac.json`. Fresh expectations had been recorded in item (ae) before the reader ran.

### The reader's values against the recorded expectations

| Row | Enactment | Expected | Coded | What the reader relied on |
|---|---|---|---|---|
| 1 | Human Dignity and Liberty 1992 | No | No | no clause, proceeding or step found; link would rest on motive |
| 2 | Elections financing law 1969 | No | No | the single-instance clause touches every incumbent faction alike |
| 3 | Confirmation of validity law 1969 | No | No | a blanket validation; no permitted dated source for a pending petition |
| 4 | Freedom of Occupation override 1994 | No | No | the saving deadline binds any government relying on existing law; the override is general |
| 5 | Two-year budget 2016 | Yes | Yes | item 4: a temporary provision for the sitting government's own budget, tabled as a government bill |
| 6 | Budget deadline 2020 | Yes | Yes | item 3: a dissolution deadline that bound the sitting government, moved on the night it ran out |
| 7 | Nation-State 2018 | No | No | no clause, proceeding or step found |
| 8 | Incapacity 2023 | Yes | Yes | item 2: the attorney general's letter of 1 February 2023; item 1: the unfitness petition of 9 February 2023 with responses ordered by 12 March |
| 9 | Reasonableness 2023 | Yes | Yes | item 1: the petition against the Ben Gvir appointment, on reasonableness grounds, pending on the day of passage |

Nine of nine expectations met. The reader flagged an ambiguity in the tightened wording on rows 8 and 9: both enactments are general in form, so on a reading under which a rule that successors would also enjoy is never Yes, both would be No. The reader coded them Yes on the reading that the alteration which must be unshared is the alteration in the live matter, not the form of the rule, which is the reading the list was written to express; the note's change log item (af) makes that explicit in step 3 and discloses that the clarification was written after the reader's choice was seen. Under the alternative reading row 9 would fall from F of 4 to 3 and stay Adverse-predicted from the Sharp row, and row 8 is uncoded in any case, so the verdict is the same under both readings.

### Effect on the analysis

The 1994 override returns to F of 2 and stays Undetermined. Reasonableness stays at F of 4 in the purpose-driven group. The configuration is N = 5, K = 4, D_A = 1, D_N = 0; Inconclusive before outcomes; the secondary analysis 11a reproduces the first run; the two analyses classify no row differently and differ only in the group label of Reasonableness.

### Disclosures for this pass

- The reader is a language model and reported court outcomes reaching it through search-result titles and summaries for every enactment but the 1992 Basic Law and the 1969 ratification law, none opened.
- The reader's working folder, which the session shares with earlier work, already held files whose names included case names (among them files named for the 1969 and 1995 cases and for petitions); the reader reported not opening them and using four Knesset file identifiers from their names only to re-download the same gazette PDFs through the Internet Archive. That is a leak of case names into a role meant not to see them, and future readers are to be given a fresh folder and told not to list the shared one.
- For Reasonableness the reader opened the article reporting the disposition of the Ben Gvir appointment petition, instructing its fetch tool to return only the publication date and filing date; the headline, seen in search results, had already disclosed that petition's disposition, which is not the enactment's outcome.
- For Incapacity the gazette text of the amendment could not be retrieved, and the reader took the quoted text of the operative section from a Knesset court filing hosted by a research institute, dated after passage; the extraction exposed lines of the Knesset's arguments, which the reader reported not using.
- The 1969 ratification law is No for want of a permitted dated source for the earlier petition; the reader notes the cell should be revisited if one is supplied. Under the list it would be No in any case, because the petition had been decided before passage and a judgment already given is not an admissible fact.

## Third addendum, 22 October 2026: the Meatrael outcome cell settled

A docket reader on its outcome pass read HCJ 4676/94 Mitrael Ltd. v. Knesset, 50(5) PD 15, in full in Hebrew from the official report (Nevo's PDF, via an Internet Archive capture of 15 January 2025; the live file needs a login). Facts from the report: judgment of 25 November 1996, nine justices, unanimous, Barak P. writing the only reasoned opinion, petition dismissed, order nisi cancelled, the Meat and Meat Products Law 1994 upheld. The 26 November date in earlier sources is the date of the Globes report.

**Coding: Adverse**, replacing the first docket reader's Not adverse, which is kept in docket.json as the superseded coding. The ratio of paragraphs 18 and 21 to 23 holds that an override law is protected only within Basic Law: Freedom of Occupation, may be found invalid under Basic Law: Human Dignity and Liberty, and is shielded there only on three cumulative conditions, applied to the facts and made the basis of dismissal. Under step 4, upheld-and-narrowed is Adverse. Two further limits in the judgment do not support the coding on their own: paragraph 15, that the clause cannot validate a law abolishing the right altogether, is a general statement not applied; paragraph 16, on basic principles an override law cannot infringe, is expressly left undecided.

**The alternative reading, recorded.** Section 8's own words shield an override law only against section 4 of the same Basic Law, so holding that it does not immunise a law under the other Basic Law can be read as literal application rather than narrowing, and the three-condition test then extends the clause's effect to incidental dignity infringements rather than narrowing it; the Court also reasoned on three assumptions arguendo and declined to decide them. The reader's confidence in the coding is medium for that reason; the facts are high. The reader also notes that the brief it received named review under Basic Law: Human Dignity and Liberty as an example of what would count as narrowing, which is disclosed here as a possible steer, although the reader found that holding to be the ratio on its own reading.

**Effect on the analysis.** The row is undetermined, so S is unchanged at 1. K rises from 4 to 5 of 5, so under the null every permutation gives the same labels and S is fixed: the attainable range of S is 1 to 1, p is 1.0 at both extremes, and the verdict before outcomes is again Inconclusive. The shuffle check agrees with the exact rate. Issue 7 is closed and issue 4's Meatrael line now rests on the report.
