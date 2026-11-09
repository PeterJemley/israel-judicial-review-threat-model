# Issue 33: results (9 November 2026; exploratory)

**What was run.**
- **The sheet.** It is in [sheet.md](sheet.md), and the expectations are in [README.md](README.md). Both were committed (3389ecd) before either coder ran.
- **The coders.** Two coders, each a separate language-model agent given only the sheet, coded the five rows. Their returns are [coder-A.json](coder-A.json) and [coder-B.json](coder-B.json), committed as filed.
- **Agreement.** They agreed on all ten cells, so nothing went to the adjudicator. The agreed codes are in [final.json](final.json).
- **The results** come from `python3 analysis/sensitivity_issue33.py`.

**A gap in the sources.** The web.archive.org captures listed on the sheet could not be fetched: the connection reset on every try. Both coders read the same Knesset PDFs at their original fs.knesset.gov.il addresses, which the captures wrap, and the Nation-State law on Hebrew Wikisource.

## The codes

| Row | Original | Recoded | Expected before recoding | As expected? |
|---|---|---|---|---|
| seq 16, Basic Law: Jerusalem (1980) | Entrenches, Neutral | Limited, Illiberal | Limited, Illiberal | Yes |
| seq 64, Jerusalem (Amendment), 2000 | None, Neutral | Limited, Illiberal | Limited, Illiberal | Yes |
| seq 103, Jerusalem (Amendment No. 2), 2018 | None, Neutral | Limited, Illiberal | Limited, Illiberal | Yes |
| seq 127, Jerusalem (Amendment No. 3), 2024 | None, Neutral | Limited, Illiberal | No change, unless its text concerns territory, status or transfer of authority | No |
| codebook row 7, the Nation-State law (2018) | Limited, Illiberal | Sharp, Illiberal | Limited or Sharp, even odds | Within the expectation |

**What each recoded row turns on, in the coders' words:**
- **Seq 16.** Section 1, "ירושלים השלמה והמאוחדת היא בירת ישראל", reaches the area annexed in 1967. It is declaratory, so the departure is Limited. Contradiction outranks the holy-places clause (section 3).
- **Seq 64.** New sections 5 and 6 fix the 1967 area inside Jerusalem and bar transferring authority over it to a foreign body. Section 7 entrenches them. The effect is indirect: no national group is named.
- **Seq 103.** The bar in section 6 now needs eighty members to change, and covers the municipal area as it stood when the amendment took effect.
- **Seq 127.** New section 6A bars any official representation of a foreign state in Jerusalem unless it is a diplomatic mission accredited to Israel. Both coders called this their closest call. It rests on their inference that the missions excluded would be those dealing with the Palestinians. Without that inference, both say, the code is None.
- **Row 7.** Section 7 ("ותפעל על מנת לעודד ולקדם") requires the state to act to promote Jewish settlement, and section 1(c) reserves national self-determination to the Jewish people. Both coders read section 7 as directly requiring different treatment by national group, so Sharp.

`[attested: coder-A.json, coder-B.json]`

## What changes, and what does not

**T1 does not change.** Its current configuration is the same both ways:
- six rows in the primary analysis;
- six of them ruled against by the Court;
- two discordant rows, both with the decision rule predicting Adverse.

That is still short of the minimum of six discordant rows, so the result stays Inconclusive. Row 7 is predicted Adverse whether its departure is Limited (with `coalition_only` Yes) or Sharp, and its direction was already Illiberal.

**The comparison sample's description changes:**

| Comparison sample (39 laws) | Original | Recoded |
|---|---|---|
| No departure from the five values, or entrenches one | 27 | 23 |
| Limited departure | 12 | 16 |
| Sharp departure | 0 | 0 |
| Illiberal direction | 1 | 5 |
| Predicted classes (concordant, discordant, undetermined; 27 uncoded either way) | 8, 3, 1 | 6, 4, 2 |

The sample's predicted classes move in three places:
- **Seq 127** becomes discordant. The decision rule predicts Not adverse and the elite thesis predicts Adverse.
- **Seq 16** becomes undetermined.
- **Seq 103** is predicted Adverse by both the decision rule and the elite thesis, yet the law was never challenged.

These classes feed the challenge-stage analysis, which has not been run.

## What this shows, and its limits

- **The scores are sensitive to the baseline; T1's verdict is not.** For exactly the laws Rosen-Zvi and Yarom name, the project's scores depend on how widely "equality" is read. Read as the sheet reads it, every Jerusalem law becomes a limited, illiberal departure, and the Nation-State law a sharp one. T1's verdict is not sensitive to this, because the one recoded law that reached the Court was predicted to be ruled against either way. `[conjectural]`
- **The rule came after the data.** It was written after the original codes were seen. The result is exploratory and does not replace the primary codes.
- **The coders are not independent of each other.** Both are instances of the same kind of model. Their full agreement is weaker evidence than agreement between two independent human coders would be. The README's limits section sets out the same point for all the project's coding.
- **One code rests on an inference.** The 2024 code rests on the coders' reading of which foreign missions section 6A would exclude, which the text does not state.
- **The scope is small.** Only five rows were recoded. Basic Law: Israel Lands and the amendments to section 7A are not in the codebook or the sample.
- **The author's decision.** On 9 November 2026 the author decided to keep the primary codes, with this recode reported beside them. Issue 33 is closed.
