# Issue 33: a sensitivity recode of the Jewish-side Basic Laws (exploratory)

**Author.** Peter Jemley, who maintains this project.

**What this is.** A sensitivity check, run at the author's direction on 9 November 2026 ([issue 33](https://github.com/PeterJemley/israel-judicial-review-threat-model/issues/33)). It recodes two columns for the laws Rosen-Zvi and Yarom name on the Jewish side of Israel's "Jewish and democratic" formula, under a widened reading of equality. It reports the results beside the original codes.
- **The two columns.** `deviation_tier` is how far a law departs from five democratic values. `direction` is whether it moves the constitutional order in a liberal or illiberal direction.
- **Why it is exploratory.** The rule was written after the original codes were seen, so the result is assessed after the data were known. It does not replace the primary codes.

**Why.** Rosen-Zvi and Yarom argue that Medina's account of Israel's constitutional identity leaves out its Jewish side. They read Basic Law: Jerusalem as reinforcing "the subjection of Palestinians living in the eastern parts of the city to Israeli rule", while granting that its effect on material rights is "mostly indirect" (I·CON 24 (2026), p. 718). The project's coders score each law against five democratic values: free and equal elections, core human rights and equality, separation of powers, the rule of law, and an independent judiciary. They coded the Jerusalem laws as engaging the values only through their holy-places clause, or not at all. The reply proposes no list of values. The widened reading on the sheet is the project's own construction along the reply's lines. See [2026-11-09-reply-and-rejoinder.md](../2026-11-09-reply-and-rejoinder.md), objections O4 to O8.

**Result (9 November 2026).** The two coders agreed on all ten cells. All four Jerusalem laws became a limited, illiberal departure, and the Nation-State law a sharp one. T1's result is unchanged; the comparison sample's count of laws that do not depart from the values falls from 27 to 23. Of the five rows, four came out as expected; the exception was the 2024 amendment. See [results.md](results.md).

## Fixed before any recoding (committed before the coders ran)

**Which rows.** The selection rule takes the Basic Laws the reply names as Jewish-leaning, and amendments to them:
- Basic Law: Jerusalem (p. 718);
- Basic Law: Israel Lands (p. 718);
- the Nation-State law (pp. 719–720);
- amendments adding or changing section 7A of Basic Law: The Knesset (p. 717 n. 30).

In the project's data, these are:
- comparison-sample seq 16, 64, 103 and 127 (Basic Law: Jerusalem, 1980, and its amendments of 2000, 2018 and 2024);
- codebook row 7 (the Nation-State law, 2018).

Basic Law: Israel Lands (frame seq 5) and the four 7A amendments (frame seq 24, 74, 84 and 102) are in neither the codebook nor the comparison sample, so they are not recoded. `[attested: research/frame/basic-law-frame.csv; codebook/comparison-sample.csv]`

**The rule.** It is in [sheet.md](sheet.md). It widens what engages "core human rights and equality", and reads "preferring Jewish identity" in `direction` the same way. Everything else on the original coding sheet stands.

**The procedure.**
- **Coding.** Two coders, each a separate language-model agent given only sheet.md, code the five rows. They are not shown the original codes.
- **Adjudication.** An adjudicator, a third agent, gets the sheet and both coders' returns, and rules on each disagreement with reasons.
- **Reporting.** The results are reported beside the original codes, with T1's configuration and the comparison sample's summary computed both ways.
- **Blinding.** For row 7, the Court's ruling is public knowledge and cannot be withheld. For the four Jerusalem rows, no ruling exists, since none was challenged.

**Expectations, recorded before recoding.**

| Row | Original code | Expected under the widened reading | Why |
|---|---|---|---|
| seq 16, Jerusalem 1980 | Entrenches, Neutral | Limited, Illiberal | The law declares Jerusalem "complete and united" as the capital, which reaches the annexed east: a declaratory, group-differential effect. Contradiction outranks the holy-places clause. A coder who reads that section as status only would keep Entrenches. |
| seq 64, Jerusalem 2000 | None, Neutral | Limited, Illiberal | It defines the city's territory and bars transferring authority to a foreign body, with an entrenchment clause: indirect, by territory and political status. |
| seq 103, Jerusalem 2018 | None, Neutral | Limited, Illiberal | Expected if it raises the majority needed to change the transfer bar, as the reply's reference to eighty MKs suggests: entrenchment of a group-differential provision. |
| seq 127, Jerusalem 2024 | None, Neutral | No change, unless its text concerns territory, status or transfer of authority | Its content was not read before this record was made. |
| row 7, Nation-State 2018 | Limited, Illiberal | Limited or Sharp, even odds | Sharp if a coder reads section 7 (Jewish settlement as a national value the state "will act to encourage") as directly authorizing different treatment. The original coder named Sharp as the alternative reading. |

**Expected consequences.**
- **T1.** Row 7 is predicted Adverse whether it is Limited (with `coalition_only` Yes) or Sharp. The illiberal-direction prediction is unchanged. So T1's configuration is expected not to change.
- **The comparison sample.** If all four Jerusalem rows become Limited, the sample's count of laws that did not depart from the five values, or entrenched them, falls from 27 to 23. The count of Limited departures rises from 12 to 16. Illiberal direction rises from 1 to 5.
