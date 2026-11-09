# Issue 13: an alternative prediction rule read from the judgments (exploratory)

**Author.** Peter Jemley, who maintains this project.

**What this is.** The next step that [issue 13](https://github.com/PeterJemley/israel-judicial-review-threat-model/issues/13)'s stopping rule requires, taken at the author's direction on 9 November 2026: say how T1's prediction table would change, and record fresh expectations.
- **T1** is the project's blind test: it scores each challenged Basic Law on warning signs and compares the prediction with how the Court ruled.
- **The difference already logged.** The Court's test differs from the table's four-sign count (change log (bi), (bj); [court-signs note](../2026-11-05-court-signs.md)). That difference is logged as a criticism of the test's design.
- **What this note adds:** an alternative rule, set out below and fixed before it is computed.
- **Status.** The rule is written after every outcome in the codebook was known. So it is exploratory, and it is offered as a secondary analysis beside the table fixed on 22 October, not as a replacement. Whether to adopt it is for the author.

## What the judgments say, in brief

*Shafir*'s two stages, restated by Hayut in HCJ 5658/23 (para. 58) and by Grosskopf in HCJ 2412/23 (para. 13):
- **Stage 1.** If an amendment shows a "suspicious characteristic", from a list that is not closed, the burden shifts to the government to justify it. The characteristics are:
  - lack of stability (a temporary provision);
  - lack of generality (a personal norm, or one serving a particular government);
  - poor fit with the constitutional fabric.
- **What signals a personal purpose.** It is found from an open list of indications weighed together: haste, timing, immediate effect and content (HCJ 2412/23, Vogelman, para. 54).
- **Immediate effect** never suffices by itself (para. 53).
- **Coalition-only votes** sharpen a generality concern at most (HCJ 5658/23, Hayut, para. 192).

## The alternative rule (fixed before it is computed)

The project already codes two of the three suspicious characteristics:
- `situated_beneficiary`: a personal purpose, read from the circumstances of enactment on a closed list (change log (ac) to (af));
- `temporary_provision`: lack of stability.

The third, poor fit with the constitutional fabric, is not coded.

| Line | Condition on the row | Prediction | Source in the judgments |
|---|---|---|---|
| 1′ | A suspicious characteristic: `situated_beneficiary` Yes or `temporary_provision` Yes | Adverse, as a rebuttable presumption (the burden shifts to the government) | HCJ 5658/23, para. 58; HCJ 2412/23, Vogelman paras. 54 and 56, Grosskopf para. 13 |
| 2′ | Otherwise, `deviation_tier` Sharp | Adverse | unchanged (Medina pp. 684, 701) |
| 3′ | Otherwise, `deviation_tier` Limited and `coalition_only` Yes | Adverse | unchanged (p. 701) |
| 4′ | Otherwise, `deviation_tier` Limited and `coalition_only` No | Not adverse | p. 701, without the F threshold |
| 5′ | Otherwise, `deviation_tier` Entrenches or None | Not adverse | p. 684, without the F threshold |

**What is the same as the 22 October table:**
- the immediate-effect and expedited signs are not counted on their own, because the judgments treat them as indications of a personal purpose, which `situated_beneficiary` already records;
- the elite-interest prediction is unchanged (Adverse if `direction` is Illiberal);
- a row counts as coded only if it is coded under the 22 October table, so the two rules are compared on the same rows. In practice, `coalition_only` must not be blank.

**What is different:** no row is Undetermined under the alternative rule.

## Expectations, worked out by hand before the script is written

**The primary-analysis rows:**

| Row | Suspicious characteristic? | Prediction, 22 Oct table | Prediction, alternative rule | Elite prediction | Class under the alternative rule |
|---|---|---|---|---|---|
| 4, the 1994 override | No | Undetermined | Not adverse (line 4′) | Adverse | discordant, decision rule Not adverse |
| 5, the 2016 budget | Yes (both) | Undetermined | Adverse (1′) | Not adverse | discordant, decision rule Adverse |
| 6, the 2020 budget | Yes (both) | Adverse | Adverse (1′) | Not adverse | discordant, decision rule Adverse |
| 7, the Nation-State law | No | Adverse | Adverse (3′) | Adverse | concordant |
| 8, Incapacity | Yes (situated) | Adverse | Adverse (1′) | Not adverse | discordant, decision rule Adverse |
| 9, Reasonableness | Yes (situated) | Adverse | Adverse (1′) | Adverse | concordant |

**Expected configuration.**
- Under the 22 October table: N 6, K 6, D_A 2, D_N 0.
- Under the alternative rule: N 6, K 6, D_A 3, D_N 1, so four discordant rows against the minimum of six. Still Inconclusive.

**What the outcomes will then show.** All four discordant rows were ruled against by the Court. The alternative rule therefore gets three right (rows 5, 6 and 8), and the elite thesis gets one (row 4, the 1994 override, which had opposition support and no suspicious characteristic).

**For rows not yet decided (fresh expectations).**
- **Row 10, the 2025 Judicial Selection amendment, outcome Pending.** It has no suspicious characteristic (it is deferred, general, and not a temporary provision), and its `deviation_tier` is Limited.
  - Its `coalition_only` cell is blank by the author's decision, so it stays uncoded.
  - If that cell were Yes, the alternative rule would predict Adverse (line 3′), as would the 22 October table.
  - If it were No, both rules would predict Not adverse.
  - So the two rules agree on row 10 whatever the cell becomes.
- **Rows added later under issue 8** will be predicted by both rules, side by side.
