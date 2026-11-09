# Issue 13: T1 under the alternative rule (9 November 2026; exploratory)

**What was run.**
- **Fixed first.** The alternative rule and the expectations were committed (e35820e) before the script was written. They are in [README.md](README.md).
- **The results** come from `python3 analysis/open_list_issue13.py`. Every figure matched the expectations worked out by hand.

## The primary-analysis rows

| Row | Court's outcome | 22 Oct table | Alternative rule (line) | Elite prediction |
|---|---|---|---|---|
| 4, the 1994 override | Adverse | Undetermined | Not adverse (4′) | Adverse |
| 5, the 2016 budget | Adverse | Undetermined | Adverse (1′) | Not adverse |
| 6, the 2020 budget | Adverse | Adverse | Adverse (1′) | Not adverse |
| 7, the Nation-State law | Adverse | Adverse | Adverse (3′) | Adverse |
| 8, Incapacity | Adverse | Adverse | Adverse (1′) | Not adverse |
| 9, Reasonableness | Adverse | Adverse | Adverse (1′) | Adverse |

Row 1, Basic Law: Human Dignity and Liberty, is uncoded under both rules, because its `coalition_only` cell is blank.

## T1's configuration

| | 22 Oct table | Alternative rule |
|---|---|---|
| Rows in the primary analysis (N) | 6 | 6 |
| Ruled against by the Court (K) | 6 | 6 |
| Discordant, decision rule predicting Adverse (D_A) | 2 | 3 |
| Discordant, decision rule predicting Not adverse (D_N) | 0 | 1 |
| Discordant rows against the minimum of six | 2 | 4 |
| Verdict | Inconclusive | Inconclusive |

**Against the known outcomes**, among the discordant rows:
- the 22 October table's decision rule is right on 2 of 2;
- the alternative rule is right on 3 of 4;
- the elite thesis is right on the fourth, the 1994 override.

`[attested: analysis/open_list_issue13.py]`

**The comparison sample.** Its predicted classes move from concordant 8, discordant 3, undetermined 1 to concordant 8, discordant 4, undetermined 0. The 27 uncoded rows are unchanged.

**Row 10,** the 2025 Judicial Selection amendment, is uncoded under both rules. The two rules agree on it whatever its blank `coalition_only` cell becomes.

## What this shows, and its limits

**Reading the table as the judgments do turns two Undetermined rows into tests.**
- **The 2016 budget law** is Adverse under the alternative rule: it is a temporary provision, and was passed for a situated beneficiary. The Court issued a warning of nullification. It adds a discordant row the decision rule gets right.
- **The 1994 override,** the Meatrael row, is Not adverse under the alternative rule. It had opposition support, a Limited departure, and no suspicious characteristic. The Court nonetheless ruled against it: it upheld the statute passed under the override, but read the override narrowly, which the project codes Adverse (step 4). So the 1994 override becomes the first discordant row the decision rule gets wrong.

`[conjectural]`

**The minimum is still not met.** Four discordant rows remain short of six, so T1 stays Inconclusive under either rule.

**Limits.**
- **The rule came after the outcomes.** It was written knowing every outcome, so the comparison against outcomes is exploratory and cannot count as a test.
- **One characteristic is not coded.** The rule uses two of *Shafir*'s three suspicious characteristics. The third, poor fit with the constitutional fabric, is not coded. Neither is the narrower rule in HCJ 2412/23 that immediate effect alone raises suspicion for a Basic Law concerning the prime minister.
- **`situated_beneficiary` was itself designed after outcomes were known.** It was built on a closed list fixed after the first run (change log (ac) to (af)).
- **The decision is the author's.** The 22 October table stays the primary rule unless the author decides otherwise.
