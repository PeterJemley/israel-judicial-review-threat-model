# Adversarial review of the note, round 1, 28 October 2026

**Target.** medina-threat-conjecture-note.md as of commit e400000. The body was read in depth, and the change log only for contradictions with the body. Nothing in the note has been changed.

**Readers.** There were two readers, each a language-model agent run fresh, and neither knew what the other was doing.
- **What they were given:** the note, the article's text extracted from the published PDF, the project's records under research/, codebook/ and analysis/, and the note's assignment.
- **What they were not given:** the audit of 25 October, the figures and their corrections record, the README, the git history or the issues.
- **The substance reader** checked quotations, pin cites, numbers, internal logic, method, and fit: whether a source cited correctly reaches the point it is used for.
- **The clarity reader** read the note once, as an educated reader new to Israeli law, and marked every place they stopped.

**How the findings were checked.** Every substance finding was checked against the source it relies on.
- A script matched every quotation the reader relied on against its file. All matched, after allowing for line-break hyphens in the extracted article.
- The passages behind each finding were then read in the note, the article and the records.

The check results are:
- **Confirmed:** the defect is there, for the reason given.
- **Confirmed in part:** what does not hold is stated.
- **Interpretive:** a reading defensible either way, for the author to decide.

No finding was rejected outright.

**Severity** is graded by what the defect costs:
- **Concedes the argument:** it hands an opponent the best reply.
- **Weakens it:** it leaves a claim unsupported or a counterargument unmet.
- **Costs attention only:** it changes nothing in the argument.

**Counts.**

| Band | Findings | Confirmed | Confirmed in part | Interpretive |
|---|---|---|---|---|
| Concedes | 4 | 4 | 0 | 0 |
| Weakens | 20 | 14 | 3 | 3 |
| Costs attention | 10 | 9 | 1 | 0 |
| **Total** | **34** | **27** | **4** | **3** |

One finding (24) was moved up from Costs attention to Weakens when it was checked, because "invalid" hardens what the Court did. The clarity reader's marks are listed separately below.

## What holds up

Protect these in revision.
- **Quotations.** The p. 685 sentence is quoted exactly. So are these, each at its stated page:
  - the Baron quotation (p. 682);
  - Hasson's five values (p. 698);
  - the four signs (p. 699);
  - "likely", "may be permissible" and "may suffice";
  - "discovered" (p. 708);
  - 64 of 120, and 3 to 7.5 percent (p. 686);
  - 32 to 21 (p. 694);
  - fn. 4;
  - "delayed to the next Knesset" (p. 701).
- **Pin cites.** The pages for sections 3.1, 3.2 and 4.1 and for each case discussed are right. Item 6, as corrected in change log (aq), matches p. 708.
- **The prediction table, as a table.** Its rows cover every combination and never conflict, and its three discordant groups cover every discordant row.
- **The statistics.** Holding K fixed in the permutation test means a high Adverse base rate cannot bias S, and the two-sided p for a null that is not centred is right.
- **The numbers.** analysis/t1_revised.py reproduces the first run (N = 5, K = 4; p at the extremes 1.0 and 0.4), the degenerate K = 5 case, and the step 11 and step 12 configurations. Predicting from the CSV gives exactly one discordant row (2020), and check_numbers.py passes 75 of 75.
- **The inconclusive result is stated plainly.** "S = 1 … not evidence either way" is not softened.
- **Earlier corrections are carried through.** The Resler withdrawal is carried through item 5, the doctrine matrix and the closing paragraph. The (aq) separation of the Shin Bet and attorney-general dismissals matches the timeline.
- **The hardening disclosure.** "What this revision tests" says truthfully which of Medina's words the project hardens into definite predictions.
- **The 2025 and 2026 figures in M1** that the timeline holds all match it, as do the 2016, 2018 and 2020 tallies against the verification pass.

## Findings that concede the argument

**1. The verdicts are qualified on one side only.**
- **Where:** "What each outcome would teach", at "Claim C supported: among challenged enactments", against "What this revision tests", at "counts against the claim as this project has operationalized it".
- **What is wrong:** A miss counts only against the project's operationalization, and the Refuted row says so. The Supported row credits Claim C itself, and adds "independently of direction", which is more than S above the null mean shows. As written, T1 can support Medina but never refute him.
- **Check:** Confirmed.
- **Reader's fix:** Qualify both verdicts the same way, and restate Supported as "the doctrine's predictions beat direction on discordant rows".

**2. C-model's forbidding clause is contradicted by the note's own record, and its open term is misnamed.**
- **Where:** item 9, at "a candidate refutation of its forbidding clause, pending the definition", and M1's 2025 row, at "the Basic Law amendment instrument is re-used".
- **What is wrong:**
  - Item 9 says the clause waits on the definition of "instrument". Change log (p) corrected this: the undefined term is "closed".
  - Change log (p) also says that on the class reading the 2020 and 2023 amendments were already re-uses after the 2017 invalidity warning and the 2021 Shafir ruling. The body never mentions those earlier re-uses.
  - Leaving "closed" undefined keeps the clause from being refuted on either reading. The class reading is already refuted, and the narrow reading forbids almost nothing.
- **Check:** Confirmed. The definition is open as issue 17.
- **Reader's fix:** Define "closed", apply T4 to the 2016 to 2025 record, and on the class reading record the clause as refuted.

**3. Rival R2 is declared refuted beyond any test.**
- **Where:** "What this note does not claim", at "The refutation of rival R2 on the two 2023 amendments stands".
- **What is wrong:**
  - The paragraph opens "Nothing here is a finding" and then asserts a refutation that holds "whatever T1 through T4 show".
  - R2 is refuted "by the Court's own form indicators (pp. 701–702)". The T1 revision says indicators taken from judgments cannot test a rival that distrusts the Court's reasons.
  - The blind record undercuts the refutation for Incapacity. It has `scope` No because the text "supplies its own mechanisms", which is the alternative oversight R2 predicts, and `coalition_only` blank.
- **Check:** Confirmed against codebook/m4-codebook.csv, row 8.
- **Reader's fix:** Confine the claim to Reasonableness, on facts sourced apart from the Court (coalition-only vote, immediate effect, no alternative oversight). Mark Incapacity open, and delete "whatever T1 through T4 show".

**4. M1 says intent was low, and the power undiscovered, before late 2022. Medina says otherwise.**
- **Where:** M1, at "Before late 2022 | Low | High, undiscovered", and R-actor, at "Threat near zero before the January 2023 plan".
- **What is wrong:**
  - p. 708 says the simple-majority amendment power "has been 'discovered' and exploited" "in recent years, especially since" the end of 2022.
  - p. 696 says "In recent years, the Knesset has increasingly exploited its power".
  - p. 707 says the shift came "In the past decade", with the 2018 Nation-State Basic Law as "a pivotal piece of legislation".
  - The project's own 2016, 2018 and 2020 rows carry abuse signs and drew interventions.
  - R-actor's prediction therefore fails on the paper's own evidence, and "What the evidence already says" does not record that.
- **Check:** Confirmed. Change log (aq) corrected the same overstatement in item 6 on 28 October but left M1 unchanged.
- **Reader's fix:** Split M1's first row, for example into before about 2015, and 2015 to 2022 with intent rising. Add an evidence item recording that R-actor's prediction fails.

## Findings that weaken it

**5. Purpose is placed outside the sliding scale, where Medina's text puts it inside.**
- **Where:** "What this revision tests", at "Medina's sliding scale pairs deviation from the unwritten constitution with breadth".
- **What is wrong:**
  - p. 708 lists among the requirements that rise with deviation "the government's immediate interest in the amendment, whether the amendment takes effect immediately or is delayed".
  - p. 700 makes the purpose finding depend on content: "Where doubt remains, an amendment will be declared invalid only if it also violates the third constraint".
  - The prediction table treats F apart from tier.
  - R-doctrine and C-doctrine call the doctrine "deviation × support × purpose", while the formalisation says purpose is "not a term in the ratio".
- **Check:** Confirmed in part. The reader said the note cites p. 708 for purpose as separate; it cites p. 699. The rest holds.
- **Reader's fix:** Say that pp. 700 and 708 support an interaction, and state the separate-purpose design as the project's choice. Add a secondary analysis in which the F threshold varies by tier.

**6. The doctrine matrix contradicts the prediction table and misplaces the must-match control.**
- **Where:** the doctrine matrix, at "Valid only if purpose is legitimate. Incapacity failed here" and "Valid. Human Dignity and Liberty passed with 32 votes".
- **What is wrong:**
  - The cell for a coalition-only, limited contradiction says the amendment is valid if its purpose is legitimate. p. 701 ("permissible if the amendment serves a legitimate purpose and is supported by at least some opposition members") and the table's third row both make it Adverse regardless of purpose.
  - Human Dignity and Liberty sits under "Narrow support, coalition only". Medina adds "(although the support was bipartisan)" (p. 694), and M4 has "No, bipartisan".
  - The two columns treat narrow support and bipartisan support as opposites, so the matrix cannot place narrow bipartisan support.
  - T1 measures one opposition vote, not breadth, so "tests … the support condition directly" holds for p. 701's condition, not for breadth.
- **Check:** Confirmed.
- **Reader's fix:** Rebuild the matrix with three support levels: coalition-only; some opposition (p. 701); overwhelming (pp. 702, 707).

**7. C-doctrine's forbidding clause does not match the prediction table.**
- **Where:** C-doctrine, at "a bipartisan, limited-deviation amendment being struck".
- **What is wrong:** The clause omits p. 701's purpose condition, and it speaks of "struck" where the table speaks of Adverse.
- **Check:** Confirmed in part. The reader said the 2016 row (one opposition vote, Limited, Adverse) is the forbidden event. It drew an invalidity warning, not a strike, so it is not the event as written. The mismatch between "struck" and Adverse is the defect.
- **Reader's fix:** Restate the clause from the prediction table.

**8. The Fisher test is said to separate rival R5 from the decision rule, and step 15 says it does not.**
- **Where:** "What each outcome would teach", at "The weak R5 is supported against the decision-rule claim".
- **What is wrong:** Step 15 says the rows that separate the weak R5 from the decision-rule claim are the abusive-form enactments that do not target the judiciary, which is a different set. Judiciary-narrowing rows engage the independent-judiciary value, so the decision rule also predicts a higher Adverse rate for them.
- **Check:** Confirmed.
- **Reader's fix:** Say the Fisher result separates the weak R5 from neither rival.

**9. Claim C may come from p. 684 rather than the p. 685 sentence.**
- **Where:** "The question", at "Claim C (not elite interest). The Court's doctrine protecting those checks".
- **What is wrong:**
  - The p. 685 sentence says the threats are not to elite interests. The claim about the Court's doctrine comes from p. 684, where fn. 4 cites the elite critique.
  - T1 tests the p. 684 claim. By the note's own account it cannot test the identity and rights content the p. 685 sentence concerns.
- **Check:** Interpretive. The note reads the sentence as Medina's reply to the critique on p. 684, and issue 21 is open on that reply. The part about T1's reach is confirmed by the note's own "It does not test the content constraint on identity and rights values".
- **Reader's fix:** Separate the p. 685 claim (T2's catalogue) from the p. 684 claim (T1), and say T1 cannot reach the p. 685 sentence.

**10. The elite-interest rival is measured by ideology only.**
- **Where:** T1 revised, at "The elite-interest prediction is Adverse if `direction` is Illiberal".
- **What is wrong:** p. 685 names "private interests or ideologies of the liberal elite", and p. 684 names "hegemonic status". A version of the rival in which the Court acts against a governing bloc whatever the content is not represented.
- **Check:** Confirmed as a gap in the design. The reader adds that the one discordant row, the 2020 government's own deadline move, fits such a version; that reading is interpretive.
- **Reader's fix:** Name an interests or enacting-bloc version of the rival, and either code an enactor variable or list the version as untested.

**11. Claim A answers with Hasson's values rather than the sentence's own list, and drops "imminent".**
- **Where:** "The question", Claim A, at "remove the institutional checks that make Israel a democracy".
- **What is wrong:**
  - The antecedent of "These" at p. 685 is Medina's own list: "the right to vote, treating all citizens as equals, and preserving at least a minimal form of separation of powers". The note substitutes Hasson's five values (p. 698).
  - The note calls those values "institutional checks", where Medina treats the checks as the means and the values as what is threatened.
  - Neither Claim A nor Claim B keeps "imminent".
- **Check:** Confirmed.
- **Reader's fix:** Start from the p. 685 list, keep means and ends apart, and add imminence as a claim with a time test.

**12. "Very existence" has an identity reading the note never considers, and R-chain's anchors are thin.**
- **Where:** item 8, at "Bears on Claim B: it is asserted, not argued", and R-chain.
- **What is wrong:**
  - Medina glosses Baron's "existential threats" as "the imminent threat to Israel's democratic identity" (p. 682). On that reading, T3's "Claim B collapses into Claim A" is what Medina means, not a refutation.
  - The "civil war" of fn. 9 is a newspaper headline quoting the prime minister, cited for the delay.
  - p. 688 says the Partition Plan "defined each state's core constitutional identity", not a guarantee of survival.
- **Check:** The identity reading is interpretive; "and, in fact, to Israel's very existence" may signal more than identity. The weak anchors are confirmed.
- **Reader's fix:** Add an identity reading with its own prediction, and recast item 8 as "asserted on the security reading".

**13. Item 1 hardens Medina's wording.**
- **Where:** item 1, at "reservist refusals, business and allied pressure stopped the full plan", and M1's "reservist refusals".
- **What is wrong:**
  - Medina says reservists "declared that they would withdraw from service if the government implemented its plan" (p. 686).
  - He says the government "did not propose the full plan for a final vote … and delayed the majority of the legislative process" (p. 687).
  - He says "the subsequent war halted" its plans (p. 687).
  - "Refusals" also pre-loads C-chain's observable.
- **Check:** Confirmed. The reader also argues that M1's "Paused by the war" should code intent as High, since the minister "repeatedly called for a renewal" (p. 687); that point is interpretive.
- **Reader's fix:** Use "delayed" and "declared they would withdraw".

**14. Item 3's "the sliding scale operated as it predicts" is circular.**
- **What is wrong:** Medina builds the sliding scale from these rulings, so they agree with it by construction. p. 700 also presents Incapacity as "A notable example of implementing this constraint", meaning purpose, not the scale.
- **Check:** Confirmed.
- **Reader's fix:** "Consistent with, by construction."

**15. The body still says "declared before outcomes", and claims more blinding than the run achieved.**
- **Where:** T1 revised, opening, at "Its result under the pre-registered rule is Inconclusive, declared before outcomes"; "Roles and blinding".
- **What is wrong:**
  - Change log (ap) and (aq) corrected the same overstatement in the README and the codebook README, but the body keeps it.
  - results.md records three things the body does not:
    - "the orchestrator who assembled the table had seen the outcomes", where the body says the docket reader assembles the CSV;
    - both coders reported seeing outcomes for rows 2, 5, 6, 8 and 9, which include the one discordant row (2020) and step 11's second (2016);
    - the circumstances reader saw outcomes for every row but the 1992 law and the 1969 ratification law.
  - The body disclaims blindness only for the notorious rows.
  - The body never says the four roles were filled by language-model agents. That is only in results.md and the change log.
- **Check:** Confirmed. analysis/check_numbers.py pins the phrase "Inconclusive, declared before outcomes", so the check must be changed with the text.
- **Reader's fix:** Use (ap)'s wording, extend the blindness disclaimer to every row with reported exposure, and say the exploratory S rests entirely on such rows.

**16. The must-match control cannot fail as restated, and its result is not reported.**
- **Where:** step 3, `immediate_effect`, at "by the convention of Israeli practice recorded in the research notes".
- **What is wrong:**
  - The restated criterion is that the control must not have all four signs and must be Not adverse. The blind record has the 1992 law with `expedited` No and `coalition_only` blank, so it cannot have all four, and its outcome is known.
  - Neither the body nor results.md reports the control's result.
  - The research notes call effect on publication an inference.
- **Check:** Confirmed in part. Two sentences on, the body itself calls the convention "a coding rule of this project", so only the phrase "convention of Israeli practice" remains to fix.
- **Reader's fix:** Report the control's result and say it is close to tautological, or keep the original criterion and revise the indicator.

**17. The nine-row run is called pre-registered, though those rows shaped the rule.**
- **Where:** step 1, at "that miss is disclosed, and it is the reason the Article 4 rows".
- **What is wrong:** The primary analysis was restricted to rows decided after 1995 after the 1969 miss was seen, and was then run on the same nine rows. Change log (aa) says "That restriction was written after seeing those rows".
- **Check:** Confirmed for the label; it is the same point as figure 4's correction C2. The reader also argues that calling Article 4 "a different doctrine (pp. 693–694)" is the project's own characterization, since Medina presents Bergman as one of "Two seminal precedents" of one approach (p. 693). That point is interpretive.
- **Reader's fix:** Label the nine-row run exploratory, and treat the restriction as confirmatory only on new rows.

**18. The next step named for nine rows cannot help T1.**
- **Where:** "What each outcome would teach", at "the rest of the unit in step 1, the comparison sample first".
- **What is wrong:** The comparison sample enters only step 14, so coding it adds no primary rows. Change log (am) says as much. The body also omits the audit's point, in change log (an), that on the full unit the minimum of six is reached only if all five rows still codable are discordant.
- **Check:** Confirmed.
- **Reader's fix:** State that T1 on the Israeli record is likely to stay inconclusive however the coding comes out, and name the next data that could decide it.

**19. T2's decision rule leaves outcomes uncovered.**
- **Where:** T2, at "rival R3 supported if at least one substantive identity move appears".
- **What is wrong:**
  - No clause covers a mix of trial or attorney-general moves with structural moves and no identity move, or no moves at all.
  - R1 and R4 overlap, since moves against the attorney general are also structural.
  - "At least one" may already be met by the note's own records: the disqualification motions in item 9, and Basic Law: Torah Study in M1.
- **Check:** Confirmed for the gaps; the last point is interpretive.
- **Reader's fix:** Give proportions, thresholds and a rule for mixed cases, and refile item 9's disqualification sentence under R3.

**20. T3 fixes no thresholds and no trigger.**
- **What is wrong:** No thresholds are given, M5's refuters ("No measurable change", "Never invoked") are open-ended, and "within a year of enactment" has no date, since the package was never enacted. The 2023 enactments were followed by the October 7 mobilisation.
- **Check:** Confirmed.
- **Reader's fix:** Fix the trigger, the numbers, the window and the war confound, or label C-chain untestable for now.

**21. "Claim A is the best supported" is asserted, and C-A cannot be tested.**
- **Where:** "What this note does not claim".
- **What is wrong:** No test among T1 to T4 bears on C-A. Its forbidden event needs the full package enacted, so nothing in the record can bear on it.
- **Check:** Confirmed.
- **Reader's fix:** Say that C-A cannot be tested on the present record.

**22. M3 says extra-legal pressure blocks Basic Law amendments, though both 2023 amendments passed.**
- **Where:** M3, extra-legal row.
- **What is wrong:** The cell cites pp. 686–687, but item 2 records "Two amendments passed anyway", and p. 687 says the government "succeeded in passing in 2023 amendments … by partisan vote". The other cells in the row carry no source.
- **Check:** Confirmed.
- **Reader's fix:** "Partial: delayed the plan; did not block either amendment". Mark the other cells as conjecture.

**23. M2 files an ordinary statute under Basic Law amendment, and conflicts with M1.**
- **What is wrong:**
  - Bergman concerned an ordinary statute ("the Knesset legislated election rules … by a majority that fell short", p. 693). It is listed under "Basic Law amendment", and again under "Regular statute".
  - "Appointments plan 2023, not enacted" stands beside M1's enacted 27 March 2025 Judicial Selection Committee amendment.
  - "Attorney general removal risk" predates the 2025 dismissal.
- **Check:** Confirmed.
- **Reader's fix:** Move Bergman, and date M2 as the paper's attack surface.

**24. "Invalid on purpose alone" hardens what the Court did to Incapacity.**
- **Where:** the doctrine matrix, at "low-deviation on content and invalid on purpose alone"; also "Incapacity failed here".
- **What is wrong:** The Court "decided that the amendment would take effect only after the next general elections" (p. 701). Item 3 says "delayed".
- **Check:** Confirmed. Moved up from Costs attention, because the project's rule is that "struck down in part" and similar wording must not harden.
- **Reader's fix:** "Deferred".

## Findings that cost attention only

**25. Passages that read as if T1 had not run.**
- **What is wrong:**
  - The Status line says "conjecture, untested".
  - The R5 row says "on the author's expected coding", where change log (ab) records the strong form contradicted on the blind-coded subjects.
  - C-doctrine and the doctrine matrix speak of "six form indicators". The 21 October log records that M4 overstated the six as a list the Court states as a set, and the body elsewhere uses "Medina's four Court-stated signs".
  - Steps 12 and 15 say "blank until blind coders fill it", and all nine `targets_judiciary` cells are now filled.
- **Check:** Confirmed. Steps 12 and 15 are, by design, disclosures on the illustrative cells (step 16), but nothing tells the reader so.

**26. "The purpose constraint was first applied in 2017 (p. 699)".** Medina writes "One example is a 2017 case". The project's notes record the 2011 Bar-On warning. Check: confirmed.

**27. "After the article's cut-off".** No source gives the cut-off, and the article itself mentions 2025: "in 2025, the government returned to advancing its plan" (p. 687). Check: confirmed.

**28. M1 details not in the timeline.** "Dismissed (March)" for the Shin Bet chief, "frozen at once", "no interim orders found", and a second 2026 measure with deferred effect are not in research/2025-2026-timeline.md. Check: confirmed in part. The base-rate remark in item 9 is in the timeline, as an unsourced caveat. Change log (aq) kept "(March)" without checking it against the timeline.

**29. Step 11a.** It is "pre-registered" though results.md says it "reproduces the first run exactly". "Neither verdict is preferred after the fact" blurs which analysis is primary. Check: confirmed in part.

**30. The formalisation's claim to make C-doctrine and C-model "one thing".** No step shows it, nothing in it addresses instrument switching, and support appears both in the numerator (seats) and in the threshold. Check: confirmed.

**31. The prediction table's "Entrenches or None" row cites p. 684.** p. 684 speaks only of entrenching amendments, so None is the project's extension. Check: confirmed.

**32. Two analyses that do nothing.**
- The sensitivity analysis flips `scope`, which enters no prediction.
- Step 12's analysis "with every row coded before this revision excluded" is empty, since all nine rows were coded before it.

Check: confirmed.

**33. Two ontology entries are sourced loosely.**
- Section 4.2 (pp. 702–703) is "The irreversibility of incorporating the unwritten constitution into Basic Laws", not the reversibility of a threat.
- "Kept separate from effect evidence (after Roznai, Dixon & Landau)" sits uneasily with the prior-art gloss that the same authors treat "effect as prima facie evidence of intent".

Check: confirmed.

**34. Step 12 shortens Medina.** Step 12 says Medina "says both 2023 amendments affected the Court's authority". He writes "directly and indirectly impacted the Court's authority" (p. 687), and the "indirectly" matters for Incapacity's `targets_judiciary`. Check: confirmed.

## External claims to verify

The reader could not check these from the project's files. Load-bearing ones are marked. None should be resolved from memory.

1. **Load-bearing: what Resler (HCJ 60/77) held, and which law it concerned.** Settled by 31(2) PD 556. Issue 2.
2. **Load-bearing: the faction breakdown of the 23 March 2023 Incapacity final vote.** Settled by the Knesset plenum record. Issues 19 and 6.
3. **Load-bearing: whether a Knesset statute with no commencement clause takes effect on publication.** Settled by Israeli interpretation-law authority or a ruling.
4. **Load-bearing for the one discordant row: Rafi Peretz's faction on 24 August 2020.** Settled by the House Committee decision of 14 July 2020. Issue 6.
5. **Load-bearing for K: whether Meatrael narrowed the 1994 amendment or applied it literally.** Settled by 50(5) PD 15, paras 18–23.
6. **The faction breakdown of the 17 March 1992 Human Dignity and Liberty vote**, needed to make the control codable. Issue 6.
7. **Bar-On (HCJ 4908/10, 2011):** whether it applied the abuse constraint or only announced it.
8. **The article's acceptance or cut-off date.** Settled by the publisher's article history.
9. **The M1 details in finding 28.** Settled by the cited reports, the gazette, and the election-appeal records. Issue 10.
10. **The prior-art characterizations** (Singer, Landau-Wells, Cox, Aven & Guikema, Grillo et al., Bermeo, Riedl et al., Roznai, Dixon & Landau, Navot, Hostovsky Brandes & Roznai). Settled by each article.
11. **Reference metadata.** The DOIs given for Hostovsky Brandes & Roznai (2024) and Riedl et al. (2024) suggest 2025. Settled by Crossref.

## The clarity reader's marks

The reader opened only the note.

### The costliest problems

**A. No orientation.** The note never says:
- that Israel has no single written constitution, and the Basic Laws serve as one;
- that the Knesset can amend the Basic Laws by simple majority;
- that the Court has held them binding since 1995;
- that "the Court" is Israel's Supreme Court.

The 1995 fact first appears in T1 revised, step 1, and "Knesset as constituent assembly" in Appendix 1. Until then, Claim A, R-structure, C-doctrine and evidence items 3 to 9 stall.

**B. One doctrine, about nine names:** "the Court's doctrine", "sliding scale", "identity limit", "unwritten constitution", "content constraint", "constituent-power doctrine", "decision rule", "decision-rule claim", "Medina's doctrine".

**C. One set of indicators, many names, and a count that changes:** "abuse indicators", "purpose indicators", "six form indicators", "form score", "Medina's four Court-stated signs", F, "the Court's signs". The count goes from six to four without explanation, and Appendix 1 lists seven.

**D. Two words used two ways.** "Row" means both an enactment and a line of the prediction table, as in "a row is assigned to the first applicable table row". "Decision rule" means both the Court's doctrine and the test's verdict rule.

**E. Cases named under two keys.** The body names cases by enactment year (2016, 2020, 2018, the 1969 financing statute). The matrices name them by case and judgment (Two-year budget 2016, Shafir 2021, Hasson 2021, Bergman 1969). The two 1969 laws are never said to be different laws.

**F. Done or planned?** In T1 revised it is unclear whether blind recoding has happened. The opening and step 16 say it has; steps 12 and 15 say "blank until blind coders fill it".

**G. Who did the coding.** The body's "two coders, blind to outcome" reads as people. That they were language models is only in the change log.

### Marks in the order met

The reader's own ordering. The ones that cost the reader most are marked **(costly)**.

- **Labels key.** The key has to warn about a clash between labels. "Claim C" also clashes with the C- conjectures: C-A concerns Claim A, while C-doctrine concerns Claim C.
- **"As asked."** Asked by whom? The formula's source (Singer 1958) comes only in Prior art.
- **(costly) Claim A, "the five values the Court listed in Hasson".**
  - The Court is not named.
  - Hasson is not introduced; its subject, the Nation-State law, appears only in M2 and M4.
  - The 2023 "Legal Reform" is not described.
  - "Core human rights" is not an institutional check.
- **Claim C, "The Court's doctrine".** The first of the unnamed doctrine names.
- **Readings, "Intent list p. 685".** The items on the list appear only in rival R3's row.
- **Readings, "the coalition".** Not identified until item 6.
- **"The January 2023 plan".** The same plan also goes by "the plan", "the full plan", "the 2023 package", "the overhaul", "the Levin plan", "appointments plan 2023" and "a renewed legislative package".
- **R-structure, "amendment by simple majority".** Amendment of what? Basic Laws have not been mentioned, and the Knesset is not glossed.
- **R-structure, "the 'discovered' power".** Unexplained.
- **R-structure, "decades before 2022".** Everything else in the note says 2023.
- **(costly) R-doctrine, "the Court's sliding scale".** It is used about 80 lines before it is explained.
- **R-doctrine, "abuse indicators" and "purpose indicators".** Are they the same thing?
- **R-chain, "Partition Plan guarantee".** Unexplained.
- **Item 3, "Reasonableness … Incapacity".** Bare names: what the two amendments did is given only in C-A. "Operated as it predicts" comes before any predictions are set out.
- **Item 4, "identity limit".** Is it the sliding scale?
- **(costly) Item 5, the worst single passage.**
  - "The row" has no referent yet.
  - "Article 4" of what?
  - "The revised T1" is a forward reference.
  - "Primary-analysis row" and "the required majority" are unexplained.
  - "On checking": checked by whom?
  - The reader could not tell whether Medina was being corrected, or whether it mattered.
  - Reader's fix: use the plain Resler sentence from "What this note does not claim", and move the row bookkeeping into T1.
- **Item 6.** The orientation in problem A is most needed here.
- **(costly) Item 9.**
  - Which amendment?
  - Shin Bet and the Judicial Selection Committee are not glossed.
  - A file path appears in running text.
  - There are forward references to C-model.
  - The reader could not see why the disqualification of Arab party lists bears on R-chain.
  - "Lists" means party slates.
- **C-A, "horizontal check".** Explained only in Prior art. "Appointment control" does not say it means judicial appointments.
- **(costly) C-doctrine, "the enforceable threshold rises".** Threshold of what? "The unwritten constitution" is new here, and "the six form indicators" are listed only in T1.
- **C-model, "the same fact".** The reader could not see the step from it. "Non-additivity" is unexplained, and the reader could not see why switching instruments forbids re-use.
- **(costly) The formalisation, "coalition seats divided by the threshold".** Is the threshold in seats? Support appears on both sides. The claim to make the two conjectures one thing is not shown.
- **R1, "the trial, the attorney general".** Whose trial? The prime minister is not named until the outcome table. "What the coalition did with the unreasonableness power" reads as a power the coalition gained.
- **R3, "(Medina's reading)".** Clashes with the R- readings.
- **(costly) R5.** Whose self-interest? "Strong form", "rows in hand" and "decision-rule claim" are undefined there, and Fisher's test is unexplained.
- **Prior art.** "Salami tactic" and "first-brick problem" have no gloss.
- **T1, "Single change".** A change from what? "Since 1958" is not explained, and the tiers are defined after five uses.
- **T1, the must-match control.** What the 1992 law is, and why it is the clean case, are not said.
- **T1, "which must be computed before coding".** What is computed?
- **T4, "One re-use refutes".** Item 9 has already reported a candidate re-use, so has T4 run?
- **(costly) T1 revised, opening.** The headline result is given in terms defined 30 or more lines later. Reader's fix: one plain sentence first, such as "only one case in the record separates the two explanations; the test needs six, so it could not decide".
- **"The must-match control's criterion is restated in step 3".** A chain of pointers.
- **"Content constraint".** A new name. Whether purpose is an axis or a separate screen differs between sections, and F is used before it is defined.
- **(costly) "Four roles are kept apart".** The count works only if the two coders count as two roles, and then a fifth is added.
- **"Notorious".** The Nation-State law has not been introduced.
- **"By its second limb".** The reader went back to find the limbs.
- **"The order, the fixed start at position one …".** The passage only points elsewhere.
- **(costly) Step 1, "the 1969 financing statute".** The reader took it for the Resler law of item 5; it is Bergman's.
- **(costly) "Constituent-power doctrine".** Constituent power is never explained.
- **"The choice under item (a): issue 1".** Three opaque pointers, and "(a)" clashes with unit part (a).
- **(costly) "F is the count of Medina's four Court-stated signs".** T1 had six; where did the other two go?
- **(costly) "A row is assigned to the first applicable table row".** Two meanings of row. "Permutation pool" and S are used before they are defined.
- **(costly) "Decision-rule prediction (Medina's doctrine …)".** The term changes meaning here.
- **Step 6, "the two-sided p is twice the smaller".** The "so" before it does not show why.
- **Step 7, "a detectability check, not a power computation".** The distinction is not explained.
- **(costly) Step 12, "the 2020 budget-deadline amendment".** The reader could not map 2020, 2016 or 2018 to M4's names. "The author's expectation is an expectation" says nothing as a sentence.
- **(costly) Step 15 against step 16.** Has the blind coding happened?
- **Step 15, "drew interventions".** The reader had to work out that an interpretation counts as Adverse.
- **Step 16, "m4" in file names.** It ties to M4 only for a reader who notices.
- **Outcome table.** Three rows for a superseded plan come first.
- **Outcome table, "rather than the prime minister".** The body's first mention of the PM.
- **"Claim C rests on a design."** Cryptic.
- **The R2 sentence.** It rests on the Court's indicators, which T1 revised says cannot test a rival that distrusts them, and it sits beside "Nothing here is a finding".
- **Appendix 1, "Justice Baron's pairing".** Who is Baron, and what pairing?
- **Appendix 1, "Knesset as constituent assembly".** The key to the doctrine; it belongs in the opening.
- **Appendix 1, "interpretation".** Listed both as an instrument and as a constraint. The list also has six values where the rest of the note has five.
- **The doctrine matrix.**
  - It has no M-number.
  - Human Dignity and Liberty sits under "coalition only", while M4 says "No, bipartisan" (substance finding 6).
- **M1.**
  - Party names are not glossed.
  - "Supreme Court" appears only here.
  - "Two of the Court's signs": which two?
- **M2.** "Meatrael", "Levin plan": the reader could map Bergman and Hasson only here.
- **M4, "No bipartisan support including Arab parties".** In the Coalition-only column, it reads as either Yes or No.
- **The change log.**
  - Pointers by date match many entries.
  - The entry item 5 needs, (i), is not cited by letter.
  - Superseded designs read as current, as with (v)'s sign test.
  - The disclosure about language-model coders is found only by reading far in.

### Closing questions

1. **Main conclusion, from memory:**
   - Medina's sentence bundles four claims of unequal standing.
   - Claim A is best supported, by the paper's own evidence.
   - Claim B is asserted with no tested mechanism.
   - Claim C is untested, its one run inconclusive.
   - Claim D is probably too simple.
   
   The strongest reason given is that abusive-form enactments are nearly all also illiberal, so only discordant cases can tell the doctrine from the elite explanation, and there is one where six are needed. The reader was unsure whether the conclusion concerns Medina's sentence or the coding study: the note's weight shifts from the first to the second, and the original question is answered mainly in an appendix.
2. **Where the reader would have stopped:**
   - first nearly at item 5 (Resler);
   - for good at the `situated_beneficiary` bullet in T1 revised, step 3, a long run of coding rules with no stakes in view.

   Nothing after it would have drawn the reader back except the outcome table.

### What reads easily (do not touch)

- The four-claim breakdown.
- The pattern of items 1, 2, 7 and 8: one fact, then one "Bears on" sentence.
- C-chain, and C-doctrine's "Forbids" clause.
- Rivals R1 to R4, and the last three rows.
- Prior art.
- T2 and T3.
- "Why the revision", the best paragraph in the note.
- The first half of "What this revision tests".
- The step 4 outcome classes, the step 8 decision rule, the end of step 11a, and step 14.
- "What this revision does not claim".
- The Resler sentence in "What this note does not claim".
- M3 and M5 as grids.
- The labels key.

## Errors in the corrections of 28 October

Change log (aq) missed three things:
- It corrected item 6's account of p. 708 but not M1's matching row (finding 4).
- It corrected the codebook README's sentence on the first run but not the body's "declared before outcomes" (finding 15).
- It kept M1's "(March)" without checking it against the timeline (finding 28).
