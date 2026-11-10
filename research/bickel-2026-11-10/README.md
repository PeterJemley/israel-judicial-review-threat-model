# Bickel's *The Least Dangerous Branch*: the author's summary, and how the project uses it

**What this is.** [summary.md](summary.md) is the project author's own summary of Alexander M. Bickel, *The Least Dangerous Branch: The Supreme Court at the Bar of Politics*, 2d ed., with a foreword by Harry H. Wellington (New Haven: Yale University Press, 1986). It is kept here unchanged, exactly as he supplied it on 10 November 2026. This page records where it comes from, how the project may use it, and how its Israeli material compares with the project's own records.

**What "the project" is.** This repository tests a sentence in Barak Medina's 2026 article in the *International Journal of Constitutional Law* (I·CON), p. 685: that the 2023 judicial plan posed "an imminent risk to Israel's existence as a democracy". It reads the claim through the threat-assessment formula Threat = Capability × Intent: what an actor can do, multiplied by what it means to do. The main document is [the note](../../medina-threat-conjecture-note.md); the [README](../../README.md) is the plain-language entry point.

**Why Bickel.** Bickel's book (first published 1962) is the classic American account of what courts can do against elected majorities, and of why they sometimes should not decide. It is the American side of the comparison in [2026-11-10-three-settlements.md](../2026-11-10-three-settlements.md).

## Provenance

- **Who wrote it.** Peter Jemley, the project's author, from his PDF of the 2nd edition. `[author's statement, 10 November 2026]`
- **How its quotations were checked.** The author checked them against the printed pages of the 2nd edition, in two rounds, on 9 and 10 November 2026. `[author's statement, 10 November 2026]` The summary's own "About this summary" records 34 corrections in the first round and 30 in the second, the second made on the page images. `[attested: summary.md]`
- **What this project has and has not read.** It has read the summary, not the book.

## How the project uses it

- **Tag.** `[summary: Bickel, p. n]` marks a statement or quotation taken from the summary, with Bickel's page in the 2nd edition. A quotation with this tag was checked on the page by the author, not by this project.
- **In research notes,** Bickel may be quoted from the summary under that tag. This was decided by the author on 10 November 2026.
- **In the main note,** Bickel is quoted only after the passage has been checked on page images the author sends. None has been sent yet.
- **Not from the book.** Two of the summary's sections are not from the book: "Reception and later developments", and "Bridges to the Israeli comparison", which sets Bickel's ideas beside Israeli cases. Their claims are the summary's own. The Israeli ones are checked against the project's records below before the project uses them.
- **Summary versus book.** A comparison drawn from Bickel supplies questions and candidate readings for the project. It is never evidence about Israeli facts.

## The Israeli material in the Bridges, set against the project's records

Checked on 10 November 2026. The "codebook" is the project's table of laws titled Basic Law that were challenged before the High Court, one numbered row per law ([codebook/m4-codebook.csv](../../codebook/m4-codebook.csv)). The "docket" is the project's record of each ruling ([coding-2026-10-22/docket.json](../coding-2026-10-22/docket.json)).

**Consistent with the project's records**
- **Mizrahi Bank:** decided 9 November 1995. `[attested: codebook row 1]`
- ***Shafir* (HCJ 5969/20):** decided 23 May 2021, 6 to 3, with a warning of invalidity rather than annulment. `[attested: docket row 6]`
  - The summary describes the law as "temporary budget amendments to the Basic Laws". Row 6 records it more narrowly, as Basic Law: The Knesset (Amendment No. 50, Temporary Provision), 2020.
  - The warning concerned future amendments of Basic Law: The State Economy. `[attested: codebook row 6 for the title; docket row 6 for the warning]`
- ***Hasson* (HCJ 5555/18):** 10 to 1, with 15 petitions. `[attested: docket row 7; research/legal-db-2026-11-05/README.md, Q3]`
- **The Reasonableness ruling (HCJ 5658/23, 1 January 2024):** 12 of 15 justices held that the Court may review Basic Laws in extreme cases, and 8 of 15 voided the amendment. `[attested: docket row 9]`
- **The override clause:** re-enacted on 9 March 1994. `[attested: docket row 4, citing Wikisource]`
- **The 2025 Judicial Selection amendment:** 67 votes for at its final reading. `[attested: codebook/m4-descriptive.csv, row 10, from the Knesset's open data]`

**Points that need care**
- **HCJ 3872/93.** The summary could not confirm this number for the 1993 Meatrael (Mitral) decision.
  - The project's list of challenged laws records it as *Mitral Ltd. v. Prime Minister*, 22 October 1993, on the authority of Hebrew Wikipedia. `[attested: research/frame/challenges.json]`
  - Neither the summary nor the project has the judgment, so the number stays unconfirmed in both.
- **Two Ressler cases.** They should not be confused:
  - Bridge 3's *Ressler v. Minister of Defence* (HCJ 910/86, 1988) is the standing and justiciability case.
  - Codebook row 3 rests on a different case, HCJ 60/77 *Ressler* (1977), on the 1969 law confirming the validity of election laws. `[attested: docket row 3]`
- **Upholding or ruling against.** Bridges 4 and 9 describe *Hasson* and the 1994 override (HCJ 4676/94) as the Court upholding the laws. The project codes both rows Adverse, under its rule that a law upheld but read narrowly counts as Adverse. `[attested: docket rows 4 and 7]`
  - Both descriptions can be true; they count different things.
  - Issue 12 asks whether *Hasson* was a true narrowing.
  - Issue 40 proposes coding the remedy itself, on Bickel's distinction between checking, legitimating and doing neither.
- **Bridge 10's open question.** The bridge asks whether the Court has ruled on the Judicial Selection amendment and whether the amendment is in force. The project's check-in of 10 November 2026 found the following, recorded under row 5 of [the comparison note](../2026-11-05-us-israel-juxtaposition.md):
  - no ruling or interim order in the reports read before the 26th Knesset first met that day;
  - so, by its text, the amendment took effect on 10 November;
  - no source read said it is treated as in force.

**Not checked by this project:**
- *Ressler* (1988) and its headnotes;
- the Nakba Law case (HCJ 3429/11);
- *Rubinstein* (1998);
- *Dapei Zahav* (1980);
- the Harari Decision (1950);
- Netanyahu's statements of July and August 2023, which come from the Times of Israel, whose site shows a bot check from this project's environment;
- the Kohelet and Globes pieces the summary cites.
