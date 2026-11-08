# Legal-database run of 5 November 2026: what it found, and what it changes

**What this is.** The author asked ten questions of Westlaw, Lexis and Bloomberg Law on 5 November 2026, using law-school access. The questions are in [prompt.txt](prompt.txt). The answer is kept unchanged in [results.md](results.md). This note sets each finding against the project and says what it changes.

**What "the project" is.** This repository tests a sentence in Barak Medina's 2026 article (I·CON, p. 685): that the 2023 judicial plan posed "an imminent risk to Israel's existence as a democracy". It reads the claim through the threat-assessment formula Threat = Capability × Intent. The main document is [the note](../../medina-threat-conjecture-note.md). The **codebook** ([codebook/m4-codebook.csv](../../codebook/m4-codebook.csv)) is the project's table of laws titled Basic Law that were challenged before the High Court, one row per law, each coded blind on the same columns.

**How the run was done.** A language-model agent ran the searches in the author's browser, from the prompt. Its `attested` tags mean the agent opened that source. This note has not re-read any of them. None of the three databases held an Israeli judgment, so every holding the run reports comes through English scholarship or the press.

**Tags.**
- `[run: ...]`: a finding of the run, with the run's own tag:
  - `attested`: the agent opened the source;
  - `lead`: it saw only a snippet or headnote, the same as the project's `[search-lead]`;
  - `conjectural`: the agent's own inference.
- `[attested: ...]`: a project file read for this note.
- `[conjectural]`: this note's inference.

## In brief

- **The main note changes in two descriptions only.** The run changes no coded cell, no number and no verdict.
- **Four open issues gain evidence:** 11, 12, 13 and 22. None of them reaches its stopping rule, so all four stay open.
- **One point is time-sensitive.** The 2025 amendment that changes the Judicial Selection Committee takes effect when the 26th Knesset first meets. That meeting is reported for 10 November 2026. No ruling on the petitions against the amendment was found.
- **Two of the note's descriptions of earlier scholarship were made exact**, at the author's direction (change log (bf); see Q9 below).
- **The companion note** setting the American and Israeli checks side by side ([2026-11-05-us-israel-juxtaposition.md](../2026-11-05-us-israel-juxtaposition.md)) gains sources on four points.

## Question by question

**Q1. When a Knesset statute takes effect if it names no date (issue 22)**

- **Why it matters.** The codebook's `immediate_effect` column codes a law with no commencement clause as taking effect on publication. That is the project's own rule (change log (aa)); no statutory default has been found for it. `[attested: issue 22]`
- **Found:**
  - Saban and Amara say legislation comes into force on publication in the Official Gazette, citing Article 10 of the Law and Administration Ordinance. They hedge the point. They write about delays in the Arabic version, not about a statute with no commencement clause or about a Basic Law. `[run: attested, Lexis, 36 Isr. L. Rev. 5, 22 n.24]`
  - Section 17 of the Interpretation Ordinance sets a publication default for regulations. That is a separate rule, for subordinate legislation. `[run: attested, Westlaw, 3 U. Pa. J. Const. L. 581, 628]`
  - No case and no passage from Navot or Barak was found.
- **Effect:** one scholarly source applies Article 10 to legislation in general. It does not meet issue 22's stopping rule, because it does not deal with a statute that names no date. The issue stays open. The email to Suzie Navot stands, with Yaniv Roznai as the fallback on 25 November. `[conjectural]`

**Q2. The petitions against the March 2025 Judicial Selection amendment (codebook row 10)**

- **Found:**
  - The Court approved conditional orders on 2 December 2025. A conditional order requires the Knesset and the government to explain why the law should not be struck down. `[run: attested, Lexis, Jerusalem Post, 3 December 2025, which says "Tuesday"; the date is the run's derivation]`
  - Eleven justices heard the case on 21 June 2026. `[run: attested, Lexis, JNS and Jerusalem Post, June 2026]`
  - No ruling was found in reports through 5 November 2026, and no report on whether the Court issued an interim order. `[run: attested, Lexis, titles read to 5 November]`
  - The amendment takes effect when the next Knesset begins its term. `[run: attested, Lexis, Jpost.com, 27 July 2026]`
  - The 26th Knesset's first session is set for 10 November. `[run: attested, Lexis, MENAFN, 3 November 2026]`
  - The HCJ numbers were not found.
- **Effect on row 10:** none. The row's docket entry, which records the case as Pending with no ruling found to 13 October, now holds to 5 November in the English press. `[attested: change log (bb)]`
- **Time-sensitive:** unless the Court rules or issues an interim order first, the amendment takes effect on 10 November. `[run: conjectural]` The check-in of 11 November will record what happened.
- **A second amendment starts the same day.** Under the Court's January 2024 ruling, the Incapacity amendment also applies from the start of the 26th Knesset. `[run: attested, Lexis, Jerusalem Post, 4 January 2024]` That matches codebook row 8, coded Deferred to the 26th Knesset. `[attested: research/frame/challenges.json]` So both deferred amendments come into force on the same day. `[conjectural]`
- **Where the press disagrees:** reports give six or nine consolidated petitions, and five or six members as the new committee's threshold. The project relies on neither figure.

**Q3. Hasson, HCJ 5555/18, the Nation-State law (issue 12, codebook row 7)**

- **Why it matters.** Row 7 is coded Adverse, the project's outcome class for a ruling that went against the law in any degree: struck down, deferred, warned against or read narrowly. The coding rests on the Court's summary, which says sections 1, 4 and 7 are read narrowly. Issue 12 asks whether that is a true narrowing or ordinary harmonising interpretation. `[attested: research/coding-2026-10-22/docket.json, row 7; issue 12]`
- **Found:**
  - Eleven justices rejected 15 petitions, 10 to 1, with Justice Kara (also spelled Karra) dissenting. No petition is reported as granted in part. `[run: attested, Lexis, Times of Israel, 8 July 2021; Dotan, 56 Isr. L. Rev. 521]`
  - The majority read section 4 as leaving Arabic's existing status in place. `[run: attested, Lexis, Efron & Wattad, 24 Cardozo J. Conflict Resol. 1, 2–3]` Pinto reads the Court differently: as declining to call Arabic an official language with special status. `[run: attested, Lexis, 7 Cardozo Int'l & Comp. L. Rev. 215, 232–33]`
  - Dotan says the law was "construed narrowly by the Court". `[run: attested, Lexis, 56 Isr. L. Rev. 521, 535 n.70]`
  - Nothing was found specific to sections 1 or 7.
- **Effect:** the vote and the petition count match the docket entry. The cell is not settled:
  - The reading of section 4 may only restate the section's own clause preserving Arabic's prior status. `[conjectural: the law's text not checked here]`
  - Dotan's "construed narrowly" is one scholar's description.
  - Row 7 stays Adverse and flagged, and issue 12 stays open. The judgment itself is still needed.

**Q4. The two budget cases, and the Court's signs of abuse (issues 11 and 13, codebook rows 5 and 6)**

- **Academic Center of Law and Business, HCJ 8260/16 (2017):**
  - The Court left the temporary amendment in place and warned that a repeat could expect to be revoked: a "revocation alert", in Dishon's words, not the Court's. `[run: attested, Lexis, 51 Isr. L. Rev. 389, 408]`
  - Justice Rubinstein wrote the ruling. `[run: attested, Lexis, Rolef, Jerusalem Post, 11 September 2017, an opinion piece]`
  - The panel and the vote were not found, so the docket entry's "seven justices" is not corroborated.
  - Dotan's footnote dates the case to 2007 and says the amendment was struck down. Dishon and Rolef say it was not annulled. `[run: attested]` The project's record agrees with Dishon and Rolef. `[attested: docket.json, row 5]`
- **Shafir, HCJ 5969/20 (2021):**
  - The ruling is reported as 6 to 3. The amendment was not annulled, because the money had already been distributed. `[run: attested, Lexis, Jpost.com, 23 May 2021]`
  - This matches the docket entry: nine justices, 6 to 3. `[attested: docket.json, row 6]`
- **The signs of abuse (issue 13).** The project codes four signs that Medina reports as the Court's guideline (p. 699):
  - the amendment addresses a specific interest of the current government;
  - it takes effect at once;
  - only coalition members voted for it;
  - it was expedited.
- **What the run found:**
  - No source the run opened shows the Court listing these four, as a set or as a presumption.
  - The accounts of *Shafir* describe a two-stage test. The Court first asks whether the norm has the features of a constitutional norm, from a list that is not closed: stability, generality, and coherence with the constitutional framework. If the norm lacks them, the respondents may justify it. `[run: attested, Lexis, Rosner, 27 German L.J. 216, 227]`
  - A presumption from immediate effect appears only as Ofra Bloch's own proposal. `[run: attested, Lexis, 85 Md. L. Rev. 112, 135]`
- **Effect:** this is a lead that the Court's test differs from the project's four-sign conjunction. Issue 13's stopping rule calls such a difference a criticism of the test's design. The finding is not yet established:
  - The run read accounts of *Shafir* only.
  - The four signs Medina reports may come from a later judgment, HCJ 2412/23 (Incapacity) or HCJ 5658/23 (Reasonableness), which the run did not search for this question. `[conjectural]`
  - Issue 13 stays open, and the prediction table is unchanged.

**Q5. Incapacity, HCJ 2412/23: the vote on personal purpose (issue 11, codebook row 8)**

- **Found:** no separate count. The sources report one 6-to-5 ruling that both found a personal purpose and deferred the amendment. Bloch reports the 6-to-5 split as the declaration of abuse itself. Justice Mintz, writing for the minority, denied that the law was personal. `[run: attested, Lexis, Times of Israel, 3 January 2024; 85 Md. L. Rev. at 133–34]`
- **Effect:**
  - The project's record of the panel matches. `[attested: research/frame/challenges.json]`
  - The prompt assumed two separate counts. The English sources do not support that assumption.
  - Whether any minority justice accepted the finding of personal purpose remained open after the run. It was settled on 8 November from the judgment itself: four dissenters found no personal purpose, and one, Justice Willner, held the question irrelevant ([2026-11-05-court-signs.md](../2026-11-05-court-signs.md), addendum).

**Q6. Who can refuse to seat a certified Knesset member**

- **Not found** in English sources. The companion note now says a search was made.

**Q7. Avi Maoz and the coalition, March 2025 (codebook row 10)**

- **Why it matters.** Row 10's coalition-only cell is blank by the author's decision of 5 November 2026. Maoz, Noam's one member, cast the only vote for that did not come from a coalition faction, and no source showed whether Noam was still in the coalition. `[attested: change log (bb)]`
- **Found:**
  - Maoz resigned from the government on 24 March 2025. `[run: attested, Lexis, Jpost.com, 24 March 2025, citing N12]`
  - No report says he or Noam left the coalition.
  - On 8 April 2025 the Times of Israel listed him among "several coalition lawmakers" seeking a seat on a panel, without dating his application. `[run: attested, Lexis]`
- **Effect:** consistent with the record in (bb), and nothing settled. The cell stays blank.

**Q8. The American and British points (the companion note)**

- **(a) Benn's case:** Justices Gorman and McNair held that Anthony Wedgwood Benn could not keep his Commons seat after succeeding to his father's peerage, and that the runner-up took the seat without a new election. `[run: attested, Lexis, Tillman, 2025 Harv. J.L. & Pub. Pol'y Per Curiam 1, n.13]` The date of decision and the court's formal name were not found.
- **(b) Barr:** the Associated Press interview of 1 December 2020 is now read in the AP story as printed the next day. `[run: attested, Lexis, Spokesman-Review, 2 December 2020, at A3]`
- **(c) David Cole on federal injunctions:** not found. The companion note cut the figures on 6 November, for want of a written source.

**Q9. Earlier scholarship the note cites (the note's prior-art list)**

- **(a) Roznai, Dixon & Landau (2023):**
  - They use "proto-abusive" at pp. 294 and 301–04, and define it at p. 302. `[run: attested, Lexis, 56 Isr. L. Rev. 292]`
  - At p. 302 they write that "the effect of a law may itself be prima facie evidence of the intent". `[run: attested]`
  - The note said, in its prior-art list and its ontology section, that they "treat effect as prima facie evidence of intent". Their word is "may". Both places now quote them with the page (change log (bf); errors list, entry 75).
- **(b) Roznai & Cohen (2023):**
  - The phrase "institutional vulnerability" does not appear.
  - They call Israel "especially vulnerable to populism, because of its unique institutional design factors" (p. 502), and argue the point at pp. 509–10. `[run: attested, Lexis, 56 Isr. L. Rev. 502]`
  - The note's prior-art list used the phrase, though not in quotation marks. It now quotes their words with the pages (change log (bf)).
- **(c) Singer (1958):** not found. It stays unchecked, as the verification pass of 4 November recorded. `[attested: research/2026-11-04-external-claims.md]`

**Q10. The 1992 vote by party:** not found. No effect.

## What the run leaves open

- The text of section 10(a), and any Israeli case applying it to a Knesset law.
- The HCJ numbers of the 2025 petitions.
- Sections 1 and 7 in Hasson.
- The Court's own words in both budget cases, and the panel and vote in *Academic Center*.
- Whether the Court ever lists the four signs together, in any judgment.
- Who can refuse to seat a certified member.
- Singer's formula, and its page.
