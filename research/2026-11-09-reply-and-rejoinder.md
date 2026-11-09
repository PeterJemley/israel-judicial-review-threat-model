# The published exchange on Medina's article: Rosen-Zvi and Yarom's reply, and Medina's rejoinder

**Author.** Peter Jemley, who maintains this project.

**What this is.** A research note recording the two published responses to Barak Medina's article, and saying where each point touches the project.

**What "the project" is.** This repository tests a sentence in Medina's 2026 article in the *International Journal of Constitutional Law* (I·CON), p. 685: that the 2023 judicial plan posed "an imminent risk to Israel's existence as a democracy". The main document, "the note", is [medina-threat-conjecture-note.md](../medina-threat-conjecture-note.md); the [README](../README.md) is the plain-language entry point.

**Sources.**
- **The reply.** Issi Rosen-Zvi and Meir H. Yarom, "Constitutional methodology and the perils of positivity: A reply to Barak Medina", I·CON 24(2) (2026), pp. 709–722, https://doi.org/10.1093/icon/moag054. It is open access under CC BY. It was read in full from the copy the author supplied on 4 November 2026, and again for this note.
- **The rejoinder.** Barak Medina, "Democratic Legitimacy and Constitutional Identity—A Rejoinder", I·CON blog (ICONnect), https://www.iconnectblog.com/democratic-legitimacy-and-constitutional-identity-a-rejoinder/. It was read in full on 9 November 2026. The page gives its publication time as 27 June 2026; its own suggested citation gives 1 July 2026. A blog post has no page numbers, so it is quoted by the post.

**Tags.**
- `[attested: reply, p. n]`: the reply, read.
- `[attested: rejoinder]`: Medina's blog post, read.
- `[conjectural]`: this note's inference.

**Labels used below.**
- **The sliding scale:** Medina's account of the Court's doctrine. The more an amendment departs from Israel's unwritten constitution, the broader the support it needs. The reply calls it "an equilibrium requirement".
- **T1:** the project's blind test. It scores each challenged Basic Law on four warning signs, without the coders being shown the ruling, and compares the scores with how the Court ruled.
- **The baseline:** the five democratic values the project's coders score each law's departure against (`deviation_tier`). These are free and equal elections, basic rights and equality, separation of powers, the rule of law, and independent courts.

## 1. The reply's objections, one by one

Each objection is followed by Medina's answer in the rejoinder, where he gave one.

**O1. Description or justification.** The article shows "apparent vacillation between description and justification". In places it describes the Court; elsewhere it offers "a novel reading" justified on moral grounds. `[attested: reply, p. 714 n. 19]`
- *Medina's answer:* his argument "primarily seeks to explain the approach adopted by the Israeli Supreme Court. While the Court has not articulated its reasoning in precisely the terms I offer, the theory aligns with the rationale expressed in its decisions." `[attested: rejoinder]`
- *Where it touches the project:* this is the question T1 asks of the warning signs. In the two judgments the project read for issue 13, the Court weighs an open list of indications of a personal purpose. It does not state Medina's four signs as a set (change log (bi), (bj)). `[conjectural]`

**O2. Two concepts with an unclear relation.** Medina grounds the unwritten constitution in constitutional identity, but "the nature of this grounding relation remains obscure". `[attested: reply, p. 715]`
- *Medina's answer:* none directly.

**O3. Too broad: sociological sources.** For Dworkin, "sociological elements are, in principle, irrelevant for establishing legal content". Courts "are not clearly equipped to derive such empirical inferences". Medina's method is closer to "living constitutionalism". `[attested: reply, p. 716]`
- *Medina's answer:* "Sociological and moral factors are essential in forming a state's core values." `[attested: rejoinder]`

**O4. Too narrow: ordinary legislation left out.** The Law of Return, the Absentees' Property Law and the Citizenship and Entry into Israel Law (Temporary Provision) offer "crucial insight into the kind of state Israel is. They cannot be ignored in reconstructing the content of its constitutional law." `[attested: reply, pp. 717–718]`
- *Medina's answer:* his three sources (the Declaration of Independence, section 7A of Basic Law: The Knesset, and Basic Law: Human Dignity and Liberty) are "chief among the relevant formal sources, but definitely not exclusive ones". `[attested: rejoinder]`

**O5. Selective constitutional materials.** Basic Laws on the Jewish side of the formula are left out.
- Basic Law: Jerusalem "reinforce[s] the subjection of Palestinians living in the eastern parts of the city to Israeli rule". It also burdens any future transfer of authority over the city.
- Basic Law: Israel Lands bars transfer of the lands, which matters given the Jewish National Fund's policy of leasing land mainly to Jewish citizens.

`[attested: reply, p. 718]`
- *Medina's answer:* as for O4.
- *Where it touches the project:* the comparison sample, which scores 39 laws no one took to court, includes both laws. Basic Law: Jerusalem (1980) is coded *Entrenches*, on its clause protecting the holy places and free access to them. Its 2000 amendment, which fixes the city's territory and bars transferring authority over it, is coded as engaging none of the five values. `[attested: codebook/comparison-sample.csv, seq 16 and 64; research/coding-sample-2026-10-22/coder-A-b1.json, coder-A-b5.json]` On the reply's reading, both codes understate how far these laws depart from equal treatment. `[conjectural]`

**O6. The chronology does not hold.** Medina explains the early Basic Laws, passed by simple majorities, as structural laws that did not touch rights.
- The reply calls this "untenable": the early Basic Laws affected the Arab minority's rights.
- Basic Law: Human Dignity and Liberty does not apply to laws passed before it. That shields past violations, which departs from the liberal reading.

`[attested: reply, pp. 718–719]`
- *Medina's answer:* Israel's identity "has evolved". The 1992 law, with policy and public changes at the time, "marked a constitutional transformation toward a more liberal identity". `[attested: rejoinder]`

**O7. The Nation-State law.** It passed 62 to 55, and as formally valid law, "Israel's constitutional identity should arguably have been recalibrated following its adoption". Medina declines to do this. `[attested: reply, p. 720]` On Hasson, the reply says that "while Hasson mitigated some of the most problematic consequences of the Basic Law, it can hardly be said to have neutralized them entirely". `[attested: reply, p. 720 n. 46]`
- *Medina's answer:* "in its 2021 Hasson decision, the Court effectively neutralized this law"; it "interpreted it in a way that rendered it functionally irrelevant". `[attested: rejoinder]` In the article itself he writes that the Court interpreted Article 7 "in a way that rendered it ineffective". `[attested: Medina, p. 698]`
- *Where it touches the project:* codebook row 7 codes Hasson as Adverse, because the law was upheld but read narrowly. Issue 12 asks whether that was a true narrowing. Medina's reading supports the code, and the reply's reading supports a weaker form of it. The judgment itself is still unread. `[conjectural]`

**O8. The result of the selectivity.** Medina's account "effectively sidelines subconstitutional materials and illiberal, Jewish-leaning constitutional provisions". It also "raises concerns about the Court's ability to shape the dataset to support preferred interpretive outcomes", and gives "a somewhat overly optimistic portrayal" of Israeli constitutional law. `[attested: reply, p. 720]` The result is "an enormous transfer of power to the Court without achieving the purpose of safeguarding minority rights". `[attested: reply, p. 711]`
- *Medina's answer:* he concedes that Israel "remains far from the liberal democratic ideal", and that pre-1992 laws, the occupation and Gaza-war policies "challenge the Court's liberal democratic framing". He defends the Court's reading as "plausible—albeit contestable". `[attested: rejoinder]`
- *Where it touches the project:* the project codes every law against the five-value baseline. The note already says that baseline is contested on this account ("What this revision tests"). `[attested: medina-threat-conjecture-note.md]`

**O9. "Overwhelming" support is undefined, and public support cannot be measured.**
- The reply asks "what does 'overwhelming' political and public support entail?"
- Courts lack the tools "to assess the level of support a given provision enjoys".
- Seats and polls diverge: polls give the governing coalition 40 to 50 seats' worth of support, against its 68 seats.

`[attested: reply, p. 721]`
- *Medina's answer:* the threshold is context-dependent (see O10). He does not say how a court would measure public support.
- *Where it touches the project:* T1 measures cross-party support by one opposition vote for (the `coalition_only` sign), not by public support. The project cannot measure public support either. `[conjectural]`

**O10. "Bipartisan" in a multi-party Knesset.** "It is not evident what 'bipartisan' means in a plural, multi-party system." In Israel, bipartisan decision-making "correlates only weakly with minority protection, especially for the Arab minority". The reply cites 73 MKs voting in July 2025 to expel the Arab MK Ayman Odeh: "political alignments based on a unified bloc of Jewish MKs can readily satisfy this condition". `[attested: reply, p. 722]`
- *Medina's answer:* "where the proposed amendment affects interests in conflict between Jewish and Arab citizens, the procedural requirement could—indeed should—be interpreted to include support from parties representing the Arab-Palestinian minority". `[attested: rejoinder]`
- *Where it touches the project:* one opposition vote from a Jewish party satisfies the project's cross-party sign, whatever the law's subject. Medina's answer suggests a variant, for laws touching Jewish–Arab interests: count the cross-party sign as met only when an Arab party voted for. `[conjectural]`

**O11. The logic would uphold majority restrictions of minority rights.** "If a given Knesset were to muster an overwhelming (Jewish) majority in favor of restricting minority rights ... the equilibrium logic would require the Court to uphold such a measure." So the proposal "is not only inadequate for protecting minorities—it may, in fact, place them at risk". `[attested: reply, p. 722]`
- *Medina's answer:* the model should be judged against its alternatives. A judge-made "eternity clause", protecting core values against any amendment, risks undermining public trust. And his constraint "is not limitless": "If a broad political consensus emerges to abandon liberal democratic values, and the Knesset enacts accordingly, the constraint of constitutional identity will lose its efficacy." `[attested: rejoinder]`
- *Where it touches the project:* the note's matrix M0 already records this as a prediction of the sliding scale. `[attested: medina-threat-conjecture-note.md, Prior art]`

**Two footnotes the project already uses.**
- Section 7A has been used to disqualify Arab parties' candidates. The Court "overturned many of these decisions, not all". `[attested: reply, p. 717 n. 30]`
- The Incapacity amendment stipulated "that only medical reasons can ground the prime minister's incapacity". `[attested: reply, p. 710 n. 4]`

## 2. Two notes on the rejoinder's wording

- Medina refers to the Court having struck down "the 2024 amendment" to Basic Law: The Judiciary. The amendment was passed in July 2023 and struck down on 1 January 2024. `[attested: codebook/m4-codebook.csv, row 9]` His words are quoted as written.
- The rejoinder answers three critiques: bipartisan support (O9 to O11), the Dworkinian sources (O3), and the liberal characterization of Israel's identity (O4 to O8). It does not answer O2 (the two concepts' relation), or O9's question of how a court would measure public support.

## 3. What this changes in the project

- **The README** now carries the exchange, briefly, in each section it bears on, with one fuller account under "The published reply to Medina, and his answer". It was written at the author's direction on 9 November 2026.
- **The note's Prior art** now includes the rejoinder (change log (bk)).
- **Two issues are opened, both exploratory**, meaning set after the data were seen. No recoding is done yet.
  - [Issue 33](https://github.com/PeterJemley/israel-judicial-review-threat-model/issues/33): recode the Jerusalem laws, and any other Jewish-side Basic Laws in the data, against a baseline widened as the reply proposes, as a sensitivity check.
  - [Issue 34](https://github.com/PeterJemley/israel-judicial-review-threat-model/issues/34): test a variant of the cross-party sign that, for laws touching Jewish–Arab interests, counts only an Arab party's support.
- **No coded cell, number or verdict changes.**
